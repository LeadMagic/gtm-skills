# LeadMagic Bulk Enrichment — Batch Pipeline Spec

End-to-end CSV batch design for find, validate, enrich, and CRM export.

## Pipeline Stages

```
INTAKE → DEDUPE → ICP FILTER → ENRICH → VERIFY → QA → EXPORT → SUPPRESS
```

Each stage produces a checkpoint file for failure recovery.

## Stage Specs

### 1. Intake (Input QA)

Required columns (minimum):

| Column | Required | Notes |
|---|---|---|
| first_name | Y | |
| last_name | Y | |
| company_domain | Y | Prefer domain over company name |
| email | N | If present, validate not find |
| crm_id | N | For idempotent CRM update |
| icp_tier | N | Enables segment filtering |

Reject rows: missing domain, competitor domain, personal email domains for B2B.

### 2. Dedupe + Suppress

- Dedupe key: `email` OR `first_name+last_name+domain`
- Suppress: existing customers, unsub list, DNC, blocklist domains
- Output: `batch-01-clean.csv`

### 3. ICP Filter (DAMA quality gate)

Filter before enrichment — saves 30-40% credits:

```
employee_count in range
AND industry in target
AND country in territory
```

Output: `batch-02-icp.csv`

### 4. Enrich (LeadMagic batch)

| Job Type | Input | Output Fields |
|---|---|---|
| Find email | name + domain | email, find_status |
| Validate | email | verify_status, sub_status |
| Enrich person | email | title, phone, linkedin |
| Enrich company | domain | size, industry, tech |

Batch size: 100-500 rows per job (rerunnable chunks).

### 5. Verify Gate (Pat Spielmann)

**Hard rule:** Only `verify_status IN (valid, deliverable)` proceed to export-for-send.

| Status | Action |
|---|---|
| valid | → send-ready export |
| invalid | → suppress + log |
| risky/catch-all | → catch_all_queue (separate workflow) |
| unknown | → manual review queue |

### 6. QA Sample

Before full export:

- Random 50-row audit: spot-check title accuracy, email format
- Bounce history if re-validating old list
- Credit burn vs row count reconciliation

### 7. CRM Export

Idempotent upsert map:

| LM Field | CRM Field | Overwrite Rule |
|---|---|---|
| verify_status | lm_email_status | Always update |
| title | jobtitle | Only if CRM empty |
| phone | phone | Only if CRM empty |
| last_verified | last_verified | Always update |

Never overwrite rep-edited fields without rule.

### 8. Sequencer Export

Filter: verify_status = valid AND suppression = false

Map to platform handoff docs (Smartlead/Instantly/Lemlist).

## Webhook Callback Pattern

For async batches:

```
POST completion webhook → n8n → branch by verify_status
  → valid: CRM upsert + optional sequencer queue
  → invalid: suppression list append
  → error: Slack alert + retry queue
```

## Monthly Monitoring

| Metric | Target |
|---|---:|
| Valid rate post-waterfall | >85% |
| Find rate (ICP-filtered) | >70% |
| Credit per send-ready row | <6 |
| Re-verify stale (>90d) | 100% coverage |

Cross-ref: `leadmagic-waterfall/references/waterfall-column-spec.md`, `integration-checklist.md`

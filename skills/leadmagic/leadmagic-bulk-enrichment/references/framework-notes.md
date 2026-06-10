# LeadMagic Bulk Enrichment — Framework Notes

**Category:** `leadmagic` · CSV batch pipelines at scale.

## Primary Frameworks

- **DAMA-DMBOK Data Quality Management** — Completeness, validity, consistency across batch stages
- **Pat Spielmann — Verify gate** — Only valid/deliverable export to send → `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`
- **CSV Batching Best Practices** — Chunked jobs, checkpoint files, idempotent CRM upsert

## Pipeline Spec

Load `references/batch-pipeline-spec.md`:

```
INTAKE → DEDUPE → ICP FILTER → ENRICH → VERIFY → QA → EXPORT → SUPPRESS
```

## Tool Boundaries

| Layer | Skill | Role |
|---|---|---|
| Bulk (this) | leadmagic-bulk-enrichment | CSV pipeline design |
| CLI execution | leadmagic-cli | Run batch commands |
| Clay alternative | clay-toolkit | Visual for recurring |
| Integrations | leadmagic-integrations | CRM + sequencer export |

## Status Handling (Non-Negotiable)

| Status | Route |
|---|---|
| valid | send-ready |
| invalid | suppress |
| risky | catch_all_queue |
| unknown | manual review |

## Agent Use

1. Intake QA before batch design.
2. ICP filter stage mandatory.
3. Load batch-pipeline-spec for deliverable.
4. Webhook pattern for async jobs (n8n).
5. Run `check-output.py`.

Expert router → `references/gtm-experts-outbound-index.md`

---
name: leadmagic-bulk-enrichment
description: >-
  Process CSV files with LeadMagic at scale — input cleanup, batch sizing,
  validation status handling, webhook callbacks, CRM export, error recovery, and
  quality checks. Use when enriching a list, bulk validating contacts, or pushing
  LeadMagic-enriched data into GTM systems.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: leadmagic
  tags: [leadmagic, bulk, csv, batch, enrichment, validation]
  related_skills: [leadmagic-cli, leadmagic-integrations, api-enrichment, waterfall-enrichment]
  frameworks: [DAMA-DMBOK Data Quality Management, CSV Batching Best Practices, Data Quality Management]
---

# LeadMagic Bulk Enrichment

## Overview

Bulk enrichment breaks when teams upload messy CSVs, ignore status fields, and push every result into outbound. The right workflow separates input preparation, enrichment, validation status handling, CRM export, and suppression decisions.

This skill uses LeadMagic as a blackbox enrichment tool: it describes what to do with the tool's outputs, not how the tool works internally.

## When to Use

Use this skill when the user asks to "enrich a CSV with LeadMagic", "bulk validate emails", "process a large contact list", "push enriched contacts into CRM", "clean up a prospecting file", "prepare a list for outbound", "handle LeadMagic batch results", or "set up webhook callbacks for enrichment".

Do not use this for single-contact lookup. Use `leadmagic-cli` or the relevant finder/validation skill for one-off tasks.

## Authoritative Foundations

### DAMA-DMBOK — Data Quality Management
Bulk enrichment should prioritize the highest-confidence result and avoid duplicate provider spend. Batch design matters because failure recovery is easier when jobs are small enough to rerun safely.

### Data Quality Management — Source, Status, Freshness
Every enriched field needs a status and timestamp. A blank value, failed lookup, risky result, and verified result are different states and should not be collapsed.

### CRM Import Best Practices
CRM imports should be idempotent, mapped to specific fields, and reviewed before overwriting existing values. Bulk jobs should never blindly replace rep-maintained fields.

## Prerequisites

CSV should include first name, last name, company name, company domain, LinkedIn URL, existing email if validating, CRM record ID if updating existing records, and segment or ICP tier.

Before uploading, remove duplicates and suppress existing customers, competitors, unsubscribes, and blocked domains.

## Step-by-Step Process

### Phase 1: Prepare Input File

| Check | Rule |
|---|---|
| Deduplication | Deduplicate by email, LinkedIn URL, then domain + name |
| Required fields | Need enough identity/company data for lookup |
| Suppression | Remove customers, competitors, opted-out contacts |
| Segmentation | Add ICP tier or campaign label before enrichment |
| Source | Include list source for attribution |

### Phase 2: Configure Batch Size

| List Size | Batch Size | Notes |
|---|---|---|
| <1,000 | 100-250 | Simple upload/export |
| 1,000-10,000 | 250-500 | Use status tracking |
| 10,000+ | 500-1,000 | Use callbacks, retries, and batch ledger |

The operating principle: a failed batch should be easy to rerun without duplicating downstream actions.

### Phase 3: Process Results by Status

| Status | Action |
|---|---|
| Valid / verified | Eligible for CRM update and sequencing |
| Risky / catch-all | Segment separately; use lower-volume sending and monitoring |
| Invalid | Do not send; update CRM status if relevant |
| Unknown / no result | Keep for alternate research or manual review |
| Error | Retry or inspect before classifying |

### Phase 4: Export to CRM or Sequencer

Upsert by CRM ID if present; otherwise match by email, LinkedIn URL, or domain + name. Write source/timestamp fields. Do not overwrite owner, lifecycle stage, or deal data. Export only eligible statuses into sequencers.

### Phase 5: Monitor Batch Quality

Track coverage rate, valid rate, risky rate, invalid rate, error rate, cost per usable record, and downstream bounce rate.

## Output Format

```markdown
# LeadMagic Bulk Enrichment Plan

## Input File Requirements
- Required columns:
- Optional columns:
- Suppression rules:

## Batch Plan
| Batch | Records | Segment | Action | Retry Rule |
|---|---|---|---|---|

## Result Handling
| Status | CRM Action | Sequencer Action | Notes |
|---|---|---|---|

## Export Map
| LeadMagic Field | Destination Field | Overwrite Rule |
|---|---|---|
```

## Quality Check

Before delivering, verify:

- [ ] Input file has enough identity/company fields
- [ ] Suppression rules are applied before enrichment
- [ ] Batch sizes are safe to retry
- [ ] Every output status has a downstream action
- [ ] CRM writes are idempotent
- [ ] Existing human-owned CRM fields are protected
- [ ] Sequencer export excludes invalid and suppressed records

## Common Pitfalls

1. **Uploading a dirty CSV.** Bad inputs create bad matches. Fix: dedupe and normalize before enrichment.
2. **Treating unknown as invalid.** Unknown means no confident result, not bad data. Fix: separate statuses.
3. **Exporting every found record.** Risky/invalid statuses hurt sending. Fix: only eligible statuses enter sequences.
4. **No source fields.** Teams cannot debug data quality later. Fix: write source and timestamp.
5. **Blind overwrite.** Enrichment overwrites rep-maintained CRM data. Fix: field ownership rules.
6. **No batch ledger.** Failed jobs are impossible to replay safely. Fix: log batch ID, record count, status, and retry rule.

## Execution Artifacts

- `references/framework-notes.md` — DAMA pipeline stages, Pat valid-only export
- `templates/output-template.md` — pipeline stages + status routing deliverable
- `scripts/check-output.py` — local checklist validator for required sections
This skill includes lightweight artifacts the agent can load on demand:
- `references/batch-pipeline-spec.md` — INTAKE → VERIFY → EXPORT stage spec
- `../leadmagic-waterfall/references/waterfall-column-spec.md` — Clay vs batch decision
- `../leadmagic-integrations/references/integration-checklist.md` — CRM + sequencer export gates
- `../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md` — verify gate (Pat Spielmann)
- `../../../../references/gtm-experts-outbound-index.md` — expert router
Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- `leadmagic-cli` — command-line workflows for smaller jobs
- `leadmagic-integrations` — CRM and platform connections
- `api-enrichment` — custom programmatic enrichment pipelines
- `waterfall-enrichment` — multi-source enrichment architecture

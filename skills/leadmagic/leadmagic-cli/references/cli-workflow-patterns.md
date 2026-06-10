# LeadMagic CLI — Workflow Patterns

Terminal automation patterns for find → verify → enrich → push pipelines.

## Pattern A: CSV Scrub Pipeline

```bash
# 1. Find missing emails
lm find --input leads.csv --output leads-found.csv

# 2. Verify all emails (including existing)
lm validate --input leads-found.csv --output leads-verified.csv

# 3. Filter valid only
lm filter --input leads-verified.csv --status valid --output send-ready.csv
```

Always validate before push — Pat Spielmann verify-before-send.

## Pattern B: Push to Sequencer

```bash
# After validate pass
lm integrations smartlead push --campaign <id> --input send-ready.csv
# or
lm integrations instantly push --campaign <id> --input send-ready.csv
```

Pre-check: send-ready.csv has verify_status = valid on every row.

Cross-ref sequencer handoff:
- smartlead-workflows/references/clay-enrollment-handoff.md
- instantly-sequences/references/clay-enrollment-handoff.md

## Pattern C: Role-Based Find

```bash
lm find-roles --domain acme.com --titles "VP Sales,Head of RevOps" --output acme-dms.csv
lm validate --input acme-dms.csv --output acme-dms-verified.csv
```

Pair with list-building for ICP account lists.

## Pattern D: Scheduled Re-Verify (Cron)

```bash
# CRM export >90 days since last_verified
lm validate --input crm-stale.csv --output crm-refreshed.csv
# Import status back to CRM — invalid → SDR task
```

## Pattern E: Clay Export Post-Process

When Clay CSV export lacks verify filter:

```bash
lm validate --input clay-export.csv --output clay-verified.csv
lm filter --status valid --input clay-verified.csv --output clay-send.csv
```

Cheaper than re-running full Clay waterfall on export.

## Error Handling

| Error | Action |
|---|---|
| Rate limit | Backoff + smaller batch (--batch-size 100) |
| Invalid API key | Check env; never log key |
| Partial CSV fail | `--continue-on-error`; review error log |
| Empty find | Flag row manual_review — do not guess |

## Credit Discipline

- Find + validate = 2 credits minimum per contact
- Run ICP filter in spreadsheet/CLI before find on large lists
- Compare CLI cost vs Clay credits for one-time vs recurring

Cross-ref waterfall: `leadmagic-waterfall/references/waterfall-column-spec.md`

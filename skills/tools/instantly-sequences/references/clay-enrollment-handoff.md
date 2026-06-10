# Clay → Instantly Enrollment Handoff

Use when Clay table (or clay-loops-toolkit ACTION table) pushes contacts to Instantly.

## Pre-Push Gate (Pat Spielmann — verify-before-send)

Only enroll rows where **all** conditions pass:

```
email_valid = true
AND verify_status IN (valid, deliverable)
AND suppression = false
AND icp_score >= threshold
AND personalization column not empty (why_now OR hook_line)
```

Cross-ref: `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

## Required Clay Export Fields

| Field | Source | Instantly Map |
|---|---|---|
| `email` | LeadMagic Find + COALESCE | Email |
| `first_name` | Enrich Person | First Name |
| `last_name` | Enrich Person | Last Name |
| `company` | Source / Enrich | Company |
| `title` | Enrich Person | Custom: Title |
| `why_now` | Claygent / formula | Custom: Personalization |
| `source_url` | Monitor table | Custom: Signal URL |
| `lm_verify_status` | Verify Email | Custom: Verify Status |

## Integration Methods

| Method | When | Notes |
|---|---|---|
| Clay native Instantly integration | <5k rows, recurring | Map custom fields in Clay UI |
| CSV export → Instantly upload | One-time batch | Dedupe against blocklist first |
| `lm integrations instantly push` | CLI automation | Requires leadmagic-cli + verify pass |
| Webhook (n8n OUT-01) | Real-time loop | n8n-toolkit → Instantly API |

## Clay Loops Routing

From `tools/clay-loops-toolkit` ACTION table:

1. Filter `route = sequencer` (not `human_review` or `ae_champion`)
2. Map `signal_type` → Instantly campaign (one signal = one campaign)
3. Pass `why_now` into Email 1 merge field — do not genericize

Load loop catalog: `../../../tools/clay-loops-toolkit/references/loop-catalog.md`

## Eric Nowoslawski Volume Check

Before scaling enrollment:

- Confirm 2+ weeks warmup on all sending accounts
- Max 30-50 sends/day/mailbox (Instantly rotation)
- Unit economics gate passed (TAM, LTV) — `eric-nowoslawski-outbound.md`

## Post-Enrollment

- Enable duplicate detection across campaigns
- Auto-pause on bounce threshold
- Route INTERESTED replies → reply-handling / CRM within SLA

# Clay Loop Blueprint — [L0X Loop Name]

**Tool path:** `tools/clay-loops-toolkit` · **Play skill:**

## Context

| Field | Value |
|---|---|
| Signal type | funding / job_change / hiring / stale_opp / champion / net_new / post_meeting |
| ICP tier | 1 / 2 / 3 |
| Cadence | daily / weekly |
| GTM play | `funding-signal-play` / etc. |

## 4-Table Architecture

| Table | Purpose | Key Columns |
|---|---|---|
| 1. Source | Raw accounts/contacts | `domain`, `crm_id`, owner |
| 2. Monitor | Cheap signal detect | `signal_detected`, `signal_date`, `signal_type` |
| 3. Enrich | LeadMagic if signal | Find → Verify → Enrich (see below) |
| 4. Action | Route | `icp_score`, `route`, `why_now` |

## Monitor Logic

```
IF [condition] THEN signal_detected = true, signal_date = today
AND signal_date within [14d / 30d] window
```

## LeadMagic Enrich Columns (conditional)

| # | Column | Credits | Run If |
|---|---|---:|---|
| 1 | LeadMagic Find Email | 1 | signal_detected |
| 2 | LeadMagic Verify Email | 1 | email found |
| 3 | LeadMagic Enrich Person | 2 | verify = valid |
| (+) | LeadMagic Job Change | — | job change loops only |

## Signal Score

| Band | Score | Action |
|---|---|---|
| Tier-1 route | 80–100 | sequencer / AE queue |
| Human review | 50–79 | CRM task |
| Log only | 20–49 | CRM property update |
| Stop | 0–19 | no action |

## Routing Matrix

| Destination | Threshold | Required Fields |
|---|---|---|
| Sequencer | 80+, email_valid | `email`, `why_now`, `source_url`, play ID |
| CRM task | 50+ | SPICED-lite, `source_url` |
| Slack | tier-1 signal | account, owner, signal |

## Credit Budget

- Per row (signal=true): ___ LeadMagic credits
- Monthly cap: ___
- Monitor-only rows: ___ credits

## Quality Check

- [ ] One signal per loop
- [ ] LeadMagic verify before sequencer
- [ ] Suppression check column
- [ ] Signal age filter
- [ ] Play skill message template linked

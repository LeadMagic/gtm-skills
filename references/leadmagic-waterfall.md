# LeadMagic Waterfall — Clay Loops

Default enrichment chain for **Table 3: ENRICH** when `signal_detected = true`.
Load `leadmagic-toolkit` for credentials and API details.

## Standard Contact Loop (Funding, Hiring, ICP Net-New)

| Order | Clay Column | LeadMagic Action | Credits | Run If |
|---|---|---|---:|---|
| 1 | Find Email | name + domain → email | 1 | signal_detected |
| 2 | Verify Email | email → deliverable status | 1 | email not empty |
| 3 | Enrich Person | email → title, phone, social | 2 | verify = valid |
| 4 | Formula | `email_valid` | 0 | always |

**Stop conditions:**
- Verify = invalid → set `route = human_review`, do not sequencer
- Find empty → optional Apollo fallback (`clay-toolkit` waterfall) OR manual queue
- Never guess email with Claygent in loops

## Job Change / Champion Loop

| Order | Clay Column | LeadMagic Action | Credits | Run If |
|---|---|---|---:|---|
| 1 | Job Change | linkedin_url → change detected | varies | on schedule |
| 2 | Formula | `signal_detected` = change in 30d | 0 | — |
| 3 | Find Email | new company context | 1 | signal_detected |
| 4 | Verify Email | | 1 | email found |
| 5 | Enrich Person | | 2 | valid |

Cross-ref open CRM opp for champion variant → route to AE not sequencer.

## Stale Opp / Post-Meeting (Light Touch)

| Order | Action | Credits |
|---|---|---:|
| 1 | Verify Email (existing CRM email) | 1 |
| 2 | Formula — refresh `last_verified` | 0 |

No find/enrich person unless email invalid and opp tier-1.

## Conditional Run (Clay UI)

Set each LeadMagic column:
- **Run condition:** `{{signal_detected}}` = true
- **Or:** formula `IF(signal_detected, run, skip)`

## Output Fields for ACTION Table

| Field | Source Column |
|---|---|
| `email` | Find Email |
| `email_status` | Verify Email |
| `email_valid` | Formula |
| `title` | Enrich Person |
| `phone` | Enrich Person |
| `leadmagic_credits_used` | Sum formula |

## Credit Budget Formula

```
per_signal_row = 1 (find) + 1 (verify) + 2 (enrich) = 4 credits typical
monthly_estimate = daily_signals × 4 × 30
```

Add 1–2 credits if job change column runs on same row.

## Integration with Sequencer

Only pass rows where:
```
email_valid = true
AND suppression = false
AND icp_score >= 80
AND signal_date within window
AND source_url not empty
```

Map to `sequencing-toolkit` enrollment webhook or native Clay integration.

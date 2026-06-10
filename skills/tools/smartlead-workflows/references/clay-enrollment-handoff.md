# Clay → Smartlead Enrollment Handoff

Use when Clay table (or clay-loops-toolkit ACTION table) pushes contacts to Smartlead.

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

| Field | Source | Smartlead Map |
|---|---|---|
| `email` | LeadMagic Find + COALESCE | Email |
| `first_name` | Enrich Person | First Name |
| `last_name` | Enrich Person | Last Name |
| `company` | Source / Enrich | Company Name |
| `title` | Enrich Person | Custom Variable: title |
| `why_now` | Claygent / formula | Custom Variable: why_now |
| `source_url` | Monitor table | Custom Variable: signal_url |
| `lm_verify_status` | Verify Email | Custom Variable: verify |

## Integration Methods

| Method | When | Notes |
|---|---|---|
| `lm integrations smartlead push --campaign <id>` | CLI batch | leadmagic-cli after verify |
| Clay → Smartlead native | Recurring loops | Map custom variables in Clay |
| CSV upload | One-time | Segment by persona before upload |
| API via n8n OUT-01 | Real-time | n8n-toolkit webhook pattern |

## Clay Loops Routing

From `tools/clay-loops-toolkit` ACTION table:

1. Filter `route = sequencer`
2. One signal type → one Smartlead campaign (ColdIQ signal-to-action)
3. Train AI categorization on INTERESTED / NOT NOW / UNSUBSCRIBE before scale

Load: `../../../tools/clay-loops-toolkit/references/leadmagic-waterfall.md`

## Eric Nowoslawski Infra (Smartlead-native)

Eric runs largest Smartlead deployments — reference for scale:

- Unlimited mailboxes: 15-25 mailboxes per campaign rotation
- 30-50 sends/day/mailbox; open tracking OFF
- Master inbox for all reply triage
- Canonical: `../../../outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md`

## Post-Enrollment

- Configure AI reply labels before launch
- A/B test subject at campaign level (500+ sends before winner)
- Bounce >3% → pause campaign, audit verify gate

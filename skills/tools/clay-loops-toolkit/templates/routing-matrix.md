# Clay Loop Routing Matrix — [Loop ID]

**Tool path:** `tools/clay-loops-toolkit`

## Score Bands → Actions

| Score | Label | CRM | Sequencer | Slack | Stop |
|---:|---|---|---|---|---|
| 80–100 | Tier-1 | upsert + owner | enroll if `human_approved` | tier-1 #signals | |
| 50–79 | Review | task for AE | no | optional | |
| 20–49 | Log | update `last_signal` only | no | no | |
| 0–19 | Suppress | no outbound | no | no | yes |

## Required Gates (all outbound paths)

| Gate | Rule |
|---|---|
| LeadMagic verify | `email_valid = true` |
| Suppression | not customer, not opted out |
| Signal age | funding/job change ≤14d; hiring ≤30d |
| SPICED | `why_now` + `source_url` populated |
| Play match | message from correct play skill |

## Field Mapping to Sequencer

| Clay Column | Sequencer Field |
|---|---|
| email | email |
| first_name | firstName |
| company | companyName |
| why_now | custom: personalization |
| source_url | custom: personalization_source |
| play_id | campaign / tag |

## n8n Handoff (optional)

When routing needs multi-system logic, webhook to `n8n-toolkit` OUT-02 with
`human_approved` flag — do not bypass LeadMagic verify in n8n.

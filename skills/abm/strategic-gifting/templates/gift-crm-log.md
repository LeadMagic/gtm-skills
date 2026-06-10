# CRM Fields — Gift Tracking

## Contact / Lead Properties

| Field | Type | Example |
|---|---|---|
| `gift_last_sent_date` | Date | 2025-06-01 |
| `gift_last_type` | Select | Physical / eGift / DM |
| `gift_last_amount` | Currency | 125 |
| `gift_policy_limit` | Currency | 100 |
| `gift_story_note` | Text | "Bourbon — call 5/28" |
| `gift_platform` | Select | Sendoso / Manual |

## Opportunity (optional)

| Field | Type |
|---|---|
| `gift_influenced_touch` | Checkbox |
| `gift_total_spend` | Rollup |

## Activity

Log task: **Gift delivered — follow up within 24h** on tracking event.

## Reporting

- Gift spend by account tier
- Meetings within 14d of gift send
- Policy limit breaches (should be zero)

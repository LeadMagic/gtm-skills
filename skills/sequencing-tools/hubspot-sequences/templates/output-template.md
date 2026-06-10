# HubSpot Sequences Deliverable

## Context
- Company / product:
- ICP tier:
- Enrollment: rep-triggered / workflow / both
- Clay loops? Y/N

## Framework Basis
- HubSpot Sequences best practices
- Pat Spielmann — verify-before-enroll
- Guillaume — multichannel task principles

## CRM Properties
| Property | Type | Source |
|---|---|---|
| lm_email_status | Dropdown | LeadMagic verify |
| last_verified | Date | Auto |
| personalization_snippet | Text | Clay |

## Workflow Enrollment Gate
```
IF lm_email_status = valid AND last_verified < 90d
  → enroll sequence by persona
ELSE → create task
```
Spec: `references/enrichment-enrollment-gate.md`

## Sequence Template
| Step | Type | Delay |
|---:|---|---|
| 1 | Email | Day 0 |

Merge token: {{personalization_snippet}}

## Clay Loops → HubSpot (if applicable)
- ACTION table → HubSpot list → workflow → Sequence
- Champion job change → AE task (not Sequence)

## Rep-Triggered Rules
- [ ] Sidebar shows verify status
- [ ] Block enroll if invalid/stale

## Quality Check
- [ ] Properties created before workflow
- [ ] Pair hubspot-setup for workflow limits
- [ ] clay-loops-toolkit if signal-driven

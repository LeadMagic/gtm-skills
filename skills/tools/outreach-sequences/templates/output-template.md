# Outreach Sequences Deliverable

## Context
- Company / product:
- ICP tier: enterprise
- CRM:
- Clay / n8n integration? Y/N

## Framework Basis
- Outreach trigger architecture
- Pat Spielmann — verify-before-enroll
- Eric Nowoslawski — Clay → CRM → Outreach at agency scale

## CRM Field Map
| CRM Field | Source | Outreach Trigger |
|---|---|---|
| lm_email_status | LeadMagic | = valid |
| signal_tag | Clay loop | Sequence selection |
| personalization_snippet | Claygent | Step 1 merge |

## Enrollment Gate
- [ ] No list-import auto-enroll without verify
- [ ] Clay → CRM → Outreach preferred path
- Spec: `references/enrichment-enrollment-gate.md`

## Trigger Architecture
| Trigger | Condition | Sequence |
|---|---|---|
|  |  |  |

## Sequence Steps
| Step | Type | Day |
|---:|---|---:|
| 1 | Email | 0 |

## Quality Check
- [ ] Verify gate in all enrollment paths
- [ ] clay-toolkit table blueprint if Clay source
- [ ] n8n OUT-01 if real-time loop

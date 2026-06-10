# Salesloft Cadences Deliverable

## Context
- Company / product:
- ICP tier: enterprise
- CRM: Salesforce / HubSpot / other
- Signal loops? Y/N

## Framework Basis
- Salesloft Rhythm — email + call + LinkedIn
- Pat Spielmann — verify-before-enroll via CRM fields

## CRM Custom Fields
| Field | Populated By | Used In |
|---|---|---|
| lm_email_status | LeadMagic verify | Enrollment rule |
| last_verified | Timestamp | Stale re-verify |
| personalization_snippet | Clay | Cadence merge |

## Enrollment Gate
- [ ] Workflow: verify before cadence enroll
- [ ] Invalid email → SDR task (not auto-enroll)
- Spec: `references/enrichment-enrollment-gate.md`

## Cadence Design
| Step | Type | Day | Task Required? |
|---:|---|---:|---|
| 1 | Email | 0 |  |
| 2 | Call | 2 | Y |

## Signal Loop Integration (if applicable)
- clay-loops-toolkit → CRM → cadence trigger
- One signal → one cadence

## Governance
- [ ] Admin approval if >500 contacts
- [ ] Conversation intelligence for coaching only

## Quality Check
- [ ] CRM fields exist before cadence build
- [ ] Pat verify gate in enrollment rules
- [ ] clay-toolkit / leadmagic-waterfall cross-ref if enrichment upstream

# Lemlist Setup Deliverable

## Context
- Company / product:
- ICP tier:
- Multichannel? Y/N
- Clay source? Y/N

## Framework Basis
- Guillaume Moubeche — problem-first, 4-9 touches
- Pat Spielmann — verify + Full-Circle multichannel
- Lemlist — lemwarm, personalization variables

## Lemwarm Status
| Mailbox | Reputation Score | Ready? |
|---|---:|---|
|  |  | >95 |

## Multichannel Sequence
| Day | Channel | Content Source |
|---:|---|---|
| 0 | Email | problem_hook (Clay) |
|  | LinkedIn |  |
|  | Call |  |

## Clay Enrollment Gate
- [ ] verify_status = valid
- [ ] problem_hook mapped (Guillaume CTC)
- [ ] Channel-native copy (no email paste to LI)
- Spec: `references/clay-enrollment-handoff.md`

## Personalization Variables
| Variable | Clay Column |
|---|---|
| {{firstName}} |  |
| {{companyName}} |  |
| {{problem_hook}} |  |

## Metrics
| Metric | Target |
|---|---:|
| Reply rate |  |
| LinkedIn accept rate |  |

## Quality Check
- [ ] lemwarm >95 before launch
- [ ] Guillaume cadence structure (4-9 touches)
- [ ] Pat verify gate on Clay rows

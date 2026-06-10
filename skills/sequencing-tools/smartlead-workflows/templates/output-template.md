# Smartlead Workflows Deliverable

## Context
- Company / product:
- ICP tier:
- Mailbox count target:
- Clay source? Y/N

## Framework Basis
- Eric Nowoslawski — Smartlead at scale (15-25 mailboxes/campaign)
- Pat Spielmann — verify-before-send
- Smartlead — AI categorization, master inbox

## Infrastructure Checklist
| Item | Status |
|---|---|
| Domains + mailboxes connected |  |
| DNS verified |  |
| Warmup 2-3 weeks |  |
| Master inbox configured |  |

## Campaign Configuration
| Setting | Value |
|---|---|
| Mailboxes in rotation |  |
| Sends/day/mailbox | 30-50 |
| Sequence steps |  |
| Plain text only | Y |

## Clay Enrollment Gate
- [ ] Pre-push verify gate documented
- [ ] Custom variables: why_now, verify_status, signal_url
- Spec: `references/clay-enrollment-handoff.md`

## AI Reply Categorization
| Category | Label | Auto-Action |
|---|---|---|
| Positive | INTERESTED |  |
| Neutral | NOT NOW |  |
| Negative | UNSUBSCRIBE | block |

## A/B Test Plan
| Variable | Variants | Sample Size |
|---|---|---|
| Subject |  | 500+ |

## Optimization Cadence
| Metric | Target |
|---|---:|
| Reply rate | >2% |
| Bounce rate | <3% |

## Quality Check
- [ ] Eric mailbox math documented
- [ ] AI categories trained before scale
- [ ] Clay handoff if enrichment upstream

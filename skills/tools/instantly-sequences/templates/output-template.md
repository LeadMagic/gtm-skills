# Instantly Sequences Deliverable

## Context
- Company / product:
- ICP tier: SMB / mid-market / enterprise
- Volume target (sends/day):
- Clay source? Y/N

## Framework Basis
- Eric Nowoslawski — infra volume and warmup
- Pat Spielmann — verify-before-send from Clay
- Instantly — rotation, unified inbox, A/B

## Infrastructure Checklist
| Item | Status | Notes |
|---|---|---|
| Secondary domains purchased |  |  |
| SPF/DKIM/DMARC configured |  |  |
| Mailboxes connected + warming |  |  |
| Custom tracking domain |  |  |
| 2-3 week warmup complete |  |  |

## Campaign Configuration
| Setting | Value |
|---|---|
| Steps |  |
| Delay between steps |  |
| Sends/day/mailbox | ≤50 |
| A/B variants |  |
| Open tracking | OFF |
| Schedule (timezone) |  |

## Clay Enrollment Gate
- [ ] email_valid = true on all enrolled rows
- [ ] why_now / personalization mapped to merge fields
- [ ] Duplicate detection enabled
- Spec: `references/clay-enrollment-handoff.md`

## Inbox Workflow
| Reply Label | Action | Owner |
|---|---|---|
| Interested |  |  |
| Not now |  |  |
| Unsubscribe |  |  |

## Optimization Cadence
| Metric | Target | Review |
|---|---|---|
| Reply rate | >2% | Weekly |
| Bounce rate | <3% | Daily |
| Spam rate | <0.1% | Weekly |

## Risks / Pitfalls
-

## Quality Check
- [ ] Eric infra defaults applied (secondary domains, volume caps)
- [ ] Pat verify gate if Clay source
- [ ] Warmup complete before launch
- [ ] Cross-ref clay-toolkit / leadmagic-waterfall if enrichment upstream

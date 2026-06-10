# LeadMagic Waterfall Deliverable

## Context
- Clay table purpose:
- ICP tier:
- Target coverage %:
- Sequencer destination:

## Framework Basis
- Pat Spielmann — Cold to Gold (verify before copy/sequencer)
- Ziellab 3-waterfall architecture
- clay-toolkit table patterns

## Waterfall Diagram
| Step | Provider | Credits | Run Condition |
|---:|---|---:|---|
| 0 | ICP filter | 0 | always |
| 1 | LM Find | 1 | ICP pass |
| 2 | Fallback | 1 | previous empty |
| 5 | LM Verify | 1 | email found |
| 7 | LM Enrich | 2 | valid |

Full spec: `references/waterfall-column-spec.md`

## Clay Column Config
- [ ] COALESCE formula for Best Email
- [ ] email_valid formula
- [ ] Catch-all branch defined
- [ ] Claygent for why_now only (not email find)

## Credit Budget
| Metric | Value |
|---|---:|
| Est. rows/month |  |
| Credits/row (avg) |  |
| Monthly total |  |
| Cap/row | ≤6 |

## Verification Gate
- [ ] LM Verify on every found email
- [ ] Valid-only filter before sequencer push
- [ ] Catch-all routed separately

## Sequencer Handoff
- Platform:
- Export fields mapped:
- Cross-ref: instantly/smartlead/lemlist clay-enrollment-handoff

## Quality Check
- [ ] ICP filter before enrichment
- [ ] Test batch 50 rows validated
- [ ] Pat verify-before-send documented

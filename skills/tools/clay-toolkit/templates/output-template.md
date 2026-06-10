# Clay Table Blueprint: [Name]

## Context
- GTM use case: outbound / ABM / signal / hygiene
- ICP tier:
- Blueprint base: (1 Outbound / 2 ABM / 3 Signal / 4 Hygiene)
- Est. row volume:

## Table Architecture

| # | Column | Type | Provider/Prompt | Conditional |
|---|---|---|---|---|
| 1 |  |  |  |  |

## Waterfall

| Field | Provider 1 | Provider 2 | Provider 3 | Verify |
|---|---|---|---|---|
| Email |  |  |  | Y |

## Formulas
- ICP score:
- Suppression check:
- clay_status:

## Output
| Destination | Condition | Fields pushed |
|---|---|---|
| CRM |  |  |
| Sequencer |  |  |

## Credit Estimate
- Per row:
- Monthly total:

## Quality Check
- [ ] Company/person tables separated (if contacts)
- [ ] Waterfall conditional logic set
- [ ] clay_status gate before export
- [ ] AI prompts from ai-prompts-toolkit (if LLM columns)
- [ ] Suppression before sequencer

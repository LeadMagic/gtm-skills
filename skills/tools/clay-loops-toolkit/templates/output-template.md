# Clay Loops Toolkit — Deliverable

## Context
- Company / product:
- Owner:
- Date:

## Summary
[One paragraph: what this deliverable decides or enables]

## Core output

<!-- Structure derived from SKILL.md Output Format -->
Clay Loop blueprint using `templates/loop-blueprint.md`:

### Loop type + GTM play skill
| Item | Detail |
|---|---|
| [field] | [value] |

### 4-table column map with LeadMagic waterfall
| Item | Detail |
|---|---|
| [field] | [value] |

### Monitor formula + signal age filter
| Item | Detail |
|---|---|
| [field] | [value] |

### Score bands + routing matrix
| Item | Detail |
|---|---|
| [field] | [value] |

### Credit budget (per row + monthly cap)
| Item | Detail |
|---|---|
| [field] | [value] |

### Integration endpoints (CRM, sequencer, n8n)
| Item | Detail |
|---|---|
| [field] | [value] |

## Frameworks Applied

- **Clay — Loops recurring GTM automation**
- **LeadMagic — Email find, verify, job change, person enrich on Clay**
- **ColdIQ — Signal-to-Action Routing**
- **Winning by Design — SPICED Critical Event**

## Quality check

- [ ] One signal type per loop
- [ ] Monitor columns are cheap; enrich only on `signal_detected = true`
- [ ] LeadMagic Verify gate before sequencer or CRM outbound
- [ ] `why_now`, `source_url`, `signal_date` on every routed row
- [ ] Suppression check before any send action
- [ ] Signal age filter (14d funding/job change)
- [ ] Matching play skill referenced for message template
- [ ] Credit cap documented per row and monthly

## Next steps
1. 
2. 
3. 

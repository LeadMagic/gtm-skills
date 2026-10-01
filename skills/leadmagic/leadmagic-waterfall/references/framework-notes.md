# Leadmagic Waterfall — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations — not as decoration.

## Primary Frameworks

- **LeadMagic docs — Email finder and validation** — Run find and validate as separate steps; only valid results should reach a sending tool.
- **DAMA-DMBOK — Data quality dimensions** — Score each waterfall step on accuracy, completeness, validity, and timeliness, not coverage alone.
- **Clay — Waterfall enrichment** — Query providers in sequence and stop at the first validated result to control cost.

## Deep-dive references

| File | Authority | Use when |
|---|---|---|
| `references/waterfall-column-spec.md` | Leadmagic Waterfall reference | Extended waterfall column spec detail |

## Templates

- `templates/output-template.md` — Primary deliverable shell

## Agent routing

| Question | Action |
|---|---|
| Full process | Follow `SKILL.md` step-by-step |
| Build deliverable | Start from `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |

Before final output, cite which framework shaped the recommendation.

# Campaign Governance — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations — not as decoration.

## Primary Frameworks

- **Google Analytics — Campaign URL (UTM) parameters** — Standardize utm_source, utm_medium, and utm_campaign values in a shared dictionary; inconsistent casing and synonyms split reporting.
- **Salesforce — Campaign hierarchy and campaign influence** — Nest campaigns (program → campaign → tactic) so influence and ROI roll up to the program level.
- **Winning by Design — Revenue Architecture** — Bowtie lifecycle model — align sales, marketing, and CS on stage-based outcomes.
- **PMI — RACI matrix** — Assign exactly one Accountable owner per launch task and separate Responsible, Consulted, and Informed roles.

## Deep-dive references

| File | Authority | Use when |
|---|---|---|
| `references/campaign-naming-conventions.md` | Campaign Governance reference | Extended campaign naming conventions detail |
| `references/utm-governance.md` | Campaign Governance reference | Extended utm governance detail |

## Templates

- `templates/output-template.md` — Primary deliverable shell
- `templates/campaign-hierarchy-register.md` — Role-specific deliverable
- `templates/utm-parameter-sheet.md` — Role-specific deliverable

## Agent routing

| Question | Action |
|---|---|
| Full process | Follow `SKILL.md` step-by-step |
| Build deliverable | Start from `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |

Before final output, cite which framework shaped the recommendation.

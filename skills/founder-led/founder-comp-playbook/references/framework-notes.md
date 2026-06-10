# Founder Comp Playbook — Framework Notes

Reference index for `SKILL.md`. Founder compensation is **governance + signal**, not just cash.

## Primary Frameworks

- **Patrick Campbell (ProfitWell)** — founder salary bands by stage; underpaying signals risk to investors.
- **Carta / Pulley cap table data** — equity refresh and dilution modeling for founder grants.
- **SaaS Capital compensation surveys** — CEO/CRO cash comp by ARR band.
- **YC standard docs** — 4-year vest, 1-year cliff for founder-adjacent exec grants.

## Decision Rules

| Stage | Cash guidance | Equity note |
|---|---|---|
| Pre-revenue | Minimal livable salary | Preserve founder % for seed |
| $1–5M ARR | Market minus 20–30% | Refresh grants for co-founders if diluted |
| $5–20M ARR | Approaching market | Separate operating vs board roles |
| $20M+ ARR | Market comp | Performance equity tied to ARR/EBITDA |

## Agent Routing

| Question | Action |
|---|---|
| Model founder package | Use `templates/output-template.md` |
| Exec comp comparison | Cross-link `executive-compensation`, `equity-management` |
| Validate output | Run `scripts/check-output.py` |

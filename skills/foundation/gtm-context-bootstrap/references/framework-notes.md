# GTM Context Bootstrap — Framework Notes

## Framework mapping

| Framework | Context fields it controls | Evidence boundary |
|---|---|---|
| April Dunford — Obviously Awesome | Alternatives, capabilities, value, segment, category | Differentiation requires comparative evidence |
| Jobs to Be Done | Trigger, desired progress, anxieties, habits | Record the situation, not only buyer demographics |
| Geoffrey Moore — Beachhead | Initial segment, whole-product needs, adjacency | Do not label the entire addressable market as the beachhead |
| Peep Laja — Message Mining | Quote bank, objections, desired outcomes | Keep source language separate from synthesized copy |

## Claim states

- **Verified** — supported by a named source that is current for the claim.
- **Owner-confirmed** — explicitly confirmed by the accountable user but not independently sourced.
- **Assumption** — plausible working input that must not be presented as fact.
- **Contradicted** — two or more sources disagree; preserve each version.
- **Unknown** — required input has not been established.

## Freshness guidance

Pricing, packaging, product capabilities, customer counts, integrations, compliance status, and team ownership should always carry an `as_of` date. Stable origin stories or durable operating principles may use the source date without a recurring refresh schedule.

## Routing

Use `templates/output-template.md` for the deliverable and validate it with `scripts/check-output.py`. Load source documents only as needed; the context pack should remain a compact index, not a duplicate archive.

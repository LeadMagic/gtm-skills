# Programmatic SEO — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- **Programmatic SEO** — Template-driven pages at scale; each URL must pass the "would a human write this?" test.
- **Animalz / HubSpot cluster model** — Pillar + cluster internal linking; programmatic pages feed clusters, not replace pillars.
- **Google Search Central** — Indexability, canonicals, thin-content policies; noindex low-value variants.

**Parent playbook:** `references/seo-strategy-playbook.md` (repo root) · **Cluster skill:** `pillar-pages`

## pSEO page types (B2B SaaS)

| Type | Example pattern | Risk | Gate |
|---|---|---|---|
| Integration pages | `[Product] + [Integration]` | Thin if no unique workflow | Require 3+ product-specific steps |
| Use-case pages | `[Job] for [Industry]` | Duplicate across industries | Unique customer proof per vertical |
| Comparison pages | `[Competitor] alternative` | Legal + stale pricing | Quarterly refresh + legal review |
| Location pages | `[Service] in [City]` | Doorway pages if no local proof | Only if real customers/offices exist |
| Glossary / definition | `[Term] meaning` | Low conversion | Link to pillar + product CTA |

## Thin-content decision tree

```
1. Does the page answer a query a human would search with purchase intent?
   → NO: noindex or merge into pillar
2. Is there ≥300 words of unique value not duplicated on sibling URLs?
   → NO: add data, screenshots, or merge
3. Does the page have a conversion path (demo, tool, template)?
   → NO: add CTA before publishing batch
4. Can you refresh all variants in one template change?
   → NO: reduce template variables until maintainable
```

## Agent routing

| Question | Action |
|---|---|
| Full SEO strategy | `seo-strategy` + `references/seo-strategy-playbook.md` |
| Hub architecture | `pillar-pages` |
| FAQ / schema | `faq-seo` |
| AI search visibility | `aeo-strategy`, `citation-harvesting` |
| Build deliverable | `templates/output-template.md` |
| Validate output | `scripts/check-output.py` |

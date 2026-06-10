# FAQ SEO — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- **FAQ schema (JSON-LD)** — `FAQPage` for eligible Q&A; must match visible on-page content.
- **Featured snippet optimization** — Question as H2/H3; answer in 40–60 words first, then depth.
- **Google Search Central** — No hidden FAQ content; no duplicate FAQ blocks across URLs.

**Parent playbook:** `references/seo-strategy-playbook.md` · **AI search pair:** `aeo-strategy`

## FAQ sourcing hierarchy

| Priority | Source | Why |
|---|---|---|
| 1 | Sales calls / support tickets | Real buyer language |
| 2 | G2 / review site questions | Evaluation-stage intent |
| 3 | "People also ask" (manual review) | Search demand signal |
| 4 | Competitor FAQ pages | Gap analysis only — rewrite answers |
| 5 | LLM-generated questions | Last resort — must be validated by SME |

## Schema checklist

- [ ] Each `Question` has matching visible text on page
- [ ] Answers are complete sentences (not "click here")
- [ ] No FAQ schema on pages with &lt;3 genuine questions
- [ ] FAQ block appears once per URL (not site-wide duplicate)
- [ ] Pricing/legal FAQs reviewed by counsel

## Snippet format template

```markdown
### [Exact question buyers ask]?

[Direct answer in 1–2 sentences, 40–60 words.]

[Supporting detail, proof point, or link to pillar.]
```

## Agent routing

| Question | Action |
|---|---|
| Pillar + cluster context | `pillar-pages`, `seo-strategy` |
| Programmatic FAQ at scale | `pseo-strategy` (template variables) |
| LLM / AI Overviews | `aeo-strategy` |
| Build deliverable | `templates/output-template.md` |
| Validate output | `scripts/check-output.py` |

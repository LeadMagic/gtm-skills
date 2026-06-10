# Pillar Pages — Framework Notes

Hub-and-spoke content architecture for B2B SEO.

## Primary frameworks

- **HubSpot Topic Cluster Model** — One pillar (broad intent) + 8–15 cluster articles linking up.
- **Animalz Content Strategy** — Pillar depth (3–5K words) with original POV, not aggregator fluff.
- **Ahrefs cluster methodology** — One pillar per money keyword; internal links contextual, not footer-only.

**Parent playbook:** `references/seo-strategy-playbook.md` · **Programmatic scale:** `pseo-strategy`

## Pillar anatomy

| Section | Purpose |
|---|---|
| Executive summary | Answer the query in first 100 words |
| Problem framing | ICP pain in their language |
| Evaluation criteria | How buyers shortlist (feeds comparison clusters) |
| Solution approach | Your methodology — not product pitch |
| Product integration | Where your product fits (1 section, clear CTA) |
| FAQ block | 5–10 questions → `faq-seo` schema |
| Cluster links | 8–15 contextual links to spokes |

## Cluster qualification

Include a spoke only if:

- [ ] Unique search intent (not synonym of another spoke)
- [ ] Can rank independently (not just long-tail of pillar H1)
- [ ] Links to pillar with descriptive anchor text
- [ ] Has conversion path (template, demo, tool)

## Refresh cadence

| Pillar tier | Refresh | Trigger |
|---|---|---|
| T1 money keyword | Quarterly | Ranking drop, competitor launch |
| T2 evaluating | Semi-annual | Product feature change |
| T3 learning | Annual | Stats outdated |

## Agent routing

| Question | Action |
|---|---|
| Keyword tiers + measurement | `seo-strategy` + `references/seo-strategy-playbook.md` |
| Programmatic spokes | `pseo-strategy` |
| FAQ schema | `faq-seo` |
| Build deliverable | `templates/output-template.md` |
| Validate output | `scripts/check-output.py` |

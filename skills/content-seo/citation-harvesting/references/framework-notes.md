# Citation Harvesting — Framework Notes

Track when LLMs and AI search engines cite your brand, pages, and content.

## Primary frameworks

- **Digital PR / link earning** — Citations follow authority; earn mentions via original research and expert content.
- **AEO monitoring** — Systematic checks across ChatGPT, Perplexity, Google AI Overviews, Copilot.
- **Moz / Ahrefs brand monitoring** — Traditional backlink + unlinked mention tracking as baseline.

**Pair skill:** `aeo-strategy` (optimize pages for citation) · **SEO hub:** `seo-strategy`

## Citation audit cadence

| Frequency | Action | Owner |
|---|---|---|
| Weekly | Run 10–20 ICP prompt queries across 3 AI engines | Content / SEO |
| Monthly | Log citation rate % by topic cluster | RevOps or marketing ops |
| Quarterly | Refresh pages with declining citations | Content + product marketing |

## Prompt bank template (ICP queries)

Build 20–50 prompts from sales discovery questions:

| Category | Example prompt |
|---|---|
| Category definition | "What is the best [category] for [ICP]?" |
| Comparison | "[Competitor] vs alternatives for [use case]" |
| How-to | "How do I [job-to-be-done] without [pain]?" |
| Vendor shortlist | "Top tools for [workflow] in 2026" |

Score each run: **Cited** (brand + URL) · **Mentioned** (brand only) · **Absent**

## Improvement loop

```
citation-harvesting (measure) → aeo-strategy (fix page structure)
→ faq-seo / pillar-pages (add definitional depth)
→ digital PR / original research (earn third-party citations)
```

## Agent routing

| Question | Action |
|---|---|
| Optimize for citations | `aeo-strategy` |
| SEO measurement stack | `seo-strategy`, `gtm-metrics` |
| Build deliverable | `templates/output-template.md` |
| Validate output | `scripts/check-output.py` |

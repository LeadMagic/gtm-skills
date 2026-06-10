# AEO Strategy — Framework Notes

Answer Engine Optimization — visibility in AI Overviews, ChatGPT, Perplexity, and copilots.

## Primary frameworks

- **AEO (Answer Engine Optimization)** — Structure content so LLMs can cite you: clear definitions, authoritative sources, schema, fresh dates.
- **E-E-A-T** — Experience, Expertise, Authoritativeness, Trustworthiness — author bios, citations, original data.
- **Product-Led SEO (Eli Schwartz)** — Pages that demonstrate product use rank in both search and AI answers.

**Parent playbook:** `references/seo-strategy-playbook.md` · **Citation tracking:** `citation-harvesting`

## AEO content patterns

| Pattern | Implementation | AI citation likelihood |
|---|---|---|
| Definitive definition | "What is [X]?" with sourced definition + your product angle | High |
| Comparison table | `[You] vs [Competitor]` with feature matrix | High |
| Original benchmark | Proprietary data with methodology | Very high |
| Step-by-step how-to | Numbered steps with screenshots | Medium–high |
| Expert quote block | Named practitioner + credential | Medium |

## Technical signals

- `Article` + `Organization` schema with `author` linked to real profiles
- `dateModified` updated on refresh (LLMs favor recency)
- Clear H1 → H2 hierarchy; one topic per section
- Internal links to canonical pillar (helps graph understanding)
- Avoid paywalled answers for top-of-funnel definitional content

## Agent routing

| Question | Action |
|---|---|
| FAQ + schema | `faq-seo` |
| Track LLM mentions | `citation-harvesting` |
| SEO keyword tiers | `seo-strategy` + `references/seo-strategy-playbook.md` |
| Demand creation context | `references/chris-walker-mental-models.md` |
| Build deliverable | `templates/output-template.md` |
| Validate output | `scripts/check-output.py` |

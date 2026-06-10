---
name: pseo-strategy
description: >-
  Programmatic SEO — build scalable, template-driven content pages for long-tail
  keywords. Triggers on: "pSEO", "programmatic SEO", "scalable SEO", "template SEO",
  "mass content generation".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: content-seo
  tags: [content-seo, pSEO, programmatic, scalable, templates]
  frameworks:
    - "Programmatic SEO Framework"
    - "Animalz Content Strategy"
    - "Google Search Central — SEO Starter Guide"
---

# Programmatic SEO (pSEO)

## Overview
Programmatic SEO generates hundreds or thousands of pages from templates and
data, targeting long-tail keywords at scale. "[Category] for [Industry]",
"[Integration] + [Integration]", "[City] [Service]" — these patterns can
generate massive organic traffic when done right, and penalties when done wrong.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Programmatic SEO Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Animalz Content Strategy.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Google Search Central — SEO Starter Guide.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Build programmatic SEO"
- "pSEO strategy"
- "Scale content with templates"
- "Generate landing pages at scale"

## Step-by-Step Process

### Phase 1: pSEO Pattern Identification
Find patterns where template + data = unique valuable page:

**Valid patterns:**
- "[Integration A] + [Integration B]" — 100 integrations → 10,000 potential pages
- "[Category] for [Industry]" — 10 categories × 20 industries = 200 pages
- "[Job Title] [Metric] Benchmarks" — 20 titles × 5 metrics = 100 pages
- "[Tool] vs [Tool]" — 20 tools → 190 comparison pages
- "Best [Category] for [Use Case]" — same math

**Invalid patterns (will get penalized):**
- Thin content with no unique value
- Near-duplicate pages with only city/name swapped
- Auto-generated text without data
- Pages that don't answer a real search query

### Phase 2: Data Source Assembly
Each pSEO page needs real data:
- **Internal data:** Your product usage data, customer data (anonymized), benchmarks
- **API data:** Enrichment APIs, directories, databases
- **Public data:** Government datasets, industry reports, open data
- **Scraped data:** Competitor data, pricing, reviews (legal and ethical scraping only)

### Phase 3: Template Design
Build a content template with:
- **Unique data fields:** What changes per page (industry name, integration name, etc.)
- **Static content:** What stays the same (product description, methodology, CTA)
- **Dynamic content rules:** "If industry = healthcare, mention HIPAA compliance.
  If industry = fintech, mention SOC2."
- **Quality threshold:** Minimum word count (500+), minimum data points (3+),
  unique value proposition per page

### Phase 4: Indexation Strategy
Critical: not all pSEO pages should be indexed.

- **Index:** Pages that provide unique value, have real data, and target search
  queries with volume
- **No-index:** Pages with no search volume, thin content, or near-duplicate content
- **Canonical:** Pages that are variations of a primary page should canonical to
  the primary

Start with 20-50 pages. Measure. If they rank and convert, scale to 200-500.
If they don't, fix the template before scaling.

### Phase 5: Quality & Safety
- **Human review:** Every template gets human review before deployment. Every
  batch of generated pages gets spot-checked (10% sample).
- **Factual accuracy:** Data must be verifiable. No hallucinated statistics.
- **Thin content prevention:** Pages under 300 words get auto-no-indexed.
- **Duplicate detection:** Content similarity check before publishing.
- **Gradual rollout:** Deploy 10 pages → monitor 2 weeks → if no issues, deploy
  50 → monitor 2 weeks → scale to full batch.

## Output Format
pSEO strategy document with: pattern identification, data source inventory,
template design, indexation rules, and quality control process.



## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls

1. **Writing for search engines, not humans.** Keyword-stuffed content that reads like a robot wrote it. Fix: write for your ICP first, optimize for search second.
2. **Publishing and praying.** Creating content without a distribution plan. Fix: every piece gets a 30-day promotion calendar across email, social, and paid.
3. **Ignoring content freshness.** 2-year-old content with outdated data and examples still ranking. Fix: quarterly content audit — update or retire stale pieces.

## Implementation Depth

Use this section when the user asks for a finished asset, not a high-level explanation.

### Diagnostic Questions

1. What is the primary motion: founder-led, sales-led, product-led, partner-led, or lifecycle-led?
2. Which ICP tier is the output for: small business, mid-market, enterprise, or mixed?
3. What proof is available today: customer stories, usage data, third-party validation, screenshots, or none?
4. What system will execute the work: CRM, sequencer, warehouse, support desk, product analytics, or manual workflow?
5. What decision will the user make from this output: launch, prioritize, route, rewrite, score, coach, or measure?

### Framework Application

Map the recommendation explicitly to the named frameworks in this skill:

- Programmatic SEO Framework: apply only the part that directly improves the requested deliverable.
- Animalz Content Strategy: apply only the part that directly improves the requested deliverable.
- Google Search Central — SEO Starter Guide: apply only the part that directly improves the requested deliverable.

### Deliverable Standard

A strong output from this skill includes:

- A crisp diagnosis of the current situation
- A recommended path with tradeoffs, not a generic list
- A concrete artifact the user can use immediately: table, script, checklist, scorecard, sequence, dashboard spec, or implementation plan
- A measurement plan with leading and lagging indicators
- Risks and edge cases called out before execution

### Adaptation Rules

- For small business: reduce complexity, shorten time-to-value, and prioritize owner/operator clarity.
- For mid-market: include workflow ownership, handoffs, integrations, and enablement assets.
- For enterprise: include governance, risk, procurement, stakeholder mapping, and proof requirements.


## Execution Artifacts

- `references/framework-notes.md` — Ahrefs pSEO patterns, Schwartz product-led gates, Pattern 25 routing
- `references/seo-strategy-playbook.md` — Repo root: §5 programmatic SEO and thin-content gates
- `skills/foundation/using-gtm-skills/SKILL.md` — Pattern 25: B2B SEO Stack (step 3)
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills
- seo-strategy, aeo-strategy, content-marketing, list-building, data-enrichment-strategy

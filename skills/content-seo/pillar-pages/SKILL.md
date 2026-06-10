---
name: pillar-pages
description: >-
  Design and build pillar pages with topic clusters — comprehensive hub pages that
  rank for high-intent keywords. Triggers on: "pillar page", "topic cluster", "hub
  page", "cornerstone content", "SEO pillar".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: content-seo
  tags: [content-seo, pillar-pages, topic-clusters, cornerstone-content, seo]
  related_skills: [seo-strategy, pseo-strategy, faq-seo, content-marketing]
  frameworks:
    - "Ahrefs / Backlinko — Content Cluster Model"
    - "Eli Schwartz — Product-Led SEO"
    - "HubSpot Topic Cluster Model"
    - "Google Search Central — SEO Starter Guide"
---

# Pillar Pages & Topic Clusters

## Overview
Pillar pages are comprehensive, authoritative pages that cover a topic broadly
and link to detailed cluster content on specific subtopics. This architecture
signals to Google that you're the authority on the topic, boosting rankings
across the entire cluster.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **HubSpot Topic Cluster Model.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Animalz Content Strategy.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Google Search Central — SEO Starter Guide.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Build a pillar page"
- "Topic cluster strategy"
- "Cornerstone content"
- "Pillar page for [topic]"

## Step-by-Step Process

### Phase 1: Pillar Topic Selection
A pillar topic must be:
- **High search volume:** 500-5,000+ monthly searches
- **High business value:** Directly related to your product/ICP
- **Broad enough for clusters:** At least 10-15 subtopics
- **Evergreen:** Not news-dependent, will be relevant for years
- **Competitive but winnable:** Check current top 10 — if they're all DR 70+ sites
  and you're DR 30, pick a different pillar

### Phase 2: Cluster Mapping
Map the pillar's universe:
- **Core subtopics:** 8-12 key areas the pillar must cover
- **Cluster content:** 3-5 detailed articles per subtopic
- **Question clusters:** The 20-30 questions people ask about this topic
  (from People Also Ask, Reddit, Quora, customer conversations)
- **Internal link map:** Every cluster article links to the pillar. The pillar
  links to every cluster article. Cluster articles link to each other where relevant.

### Phase 3: Pillar Page Structure
- **H1:** [Topic]: The Complete Guide (or similar)
- **Executive summary:** 2-3 paragraphs. What this covers, who it's for, key
  takeaways. This is what Google shows in featured snippets.
- **Table of contents:** Jump links to each section
- **Section per subtopic:** Each H2 covers one subtopic. 200-400 words per section.
  Link to the full cluster article for "deep dive."
- **Data & examples:** Original data, customer examples, screenshots, case studies
- **Visual elements:** Diagrams, charts, comparison tables, infographics
- **Expert contributions:** Quotes from internal experts, customers, industry voices
- **Total length:** 3,000-5,000 words. Long enough to be comprehensive, not so
  long that nobody reads it.

### Phase 4: Internal Linking
- **Pillar → Cluster:** In each pillar section, link to the full cluster article
  with descriptive anchor text
- **Cluster → Pillar:** Every cluster article links to the pillar with a standard
  "Part of our [Topic] guide" callout
- **Cluster → Cluster:** Cross-link between related cluster articles
- **Navigation:** The pillar is linked from the main navigation or resource center
- **New content:** Every new article on this topic gets a link from the pillar
  and links back to the pillar

### Phase 5: Maintenance & Updates
- **Quarterly review:** Check rankings, traffic, and conversion for the pillar
  and all cluster content
- **Annual refresh:** Update data, examples, screenshots, and expert quotes.
  Republish with updated date.
- **Cluster expansion:** Add new cluster articles as you identify new subtopics
- **Performance optimization:** Improve page speed, mobile experience, and
  Core Web Vitals for the pillar page

## Output Format
Pillar page plan with: topic selection justification, cluster map, content
outline, internal linking diagram, and maintenance calendar.



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

- HubSpot Topic Cluster Model: apply only the part that directly improves the requested deliverable.
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

- `references/framework-notes.md` — Ahrefs cluster model, Schwartz product-led pillars, Pattern 25 routing
- `references/seo-strategy-playbook.md` — Repo root: §3 keyword tiers and cluster structure
- `skills/foundation/using-gtm-skills/SKILL.md` — Pattern 25: B2B SEO Stack (step 2)
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills
- seo-strategy, content-marketing, faq-seo, citation-harvesting, landing-pages

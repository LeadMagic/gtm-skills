---
name: seo-strategy
description: >-
  B2B SEO strategy — keyword research, content architecture, technical SEO, link
  building, measurement. Triggers on: "SEO strategy", "search engine optimization",
  "B2B SEO", "keyword research", "SEO plan".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: content-seo
  tags: [content-seo, seo, keyword-research, search-optimization, b2b]
  related_skills:
    [
      pillar-pages,
      pseo-strategy,
      faq-seo,
      aeo-strategy,
      citation-harvesting,
      content-marketing,
      content-syndication,
    ]
  frameworks:
    - "Eli Schwartz — Product-Led SEO"
    - "Rand Fishkin — SparkToro Audience Research"
    - "Ahrefs / Backlinko — Content Cluster Methodology"
    - "Google E-E-A-T Guidelines"
    - "Google Search Central — SEO Starter Guide"
---

# B2B SEO Strategy

## Overview

B2B SEO is fundamentally different from B2C SEO — you're not optimizing for
traffic volume, you're optimizing for pipeline. A single #1 ranking for a
high-intent keyword like "email verification API" is worth more than 50
rankings for informational queries. This skill covers the full B2B SEO motion.

## Frameworks Referenced

- **Eli Schwartz — Product-Led SEO** ([productledseo.com](https://www.productledseo.com/)). Build content around buyer jobs-to-be-done and product capabilities — not generic category definitions. Free tools on high-intent pages.
- **Rand Fishkin — SparkToro** ([sparktoro.com](https://sparktoro.com/)). Audience research before keyword volume — where ICP spends time, what language they use, who influences them.
- **Ahrefs / Backlinko** ([ahrefs.com/blog](https://ahrefs.com/blog/)). Three-tier keyword architecture, pillar-cluster structure, technical audit checklist.
- **Google E-E-A-T + Search Central** ([developers.google.com/search](https://developers.google.com/search/docs)). Experience signals, schema, indexability.

**Deep playbook:** `references/seo-strategy-playbook.md` (repo root) — technical SEO, content clusters, programmatic SEO, measurement.

## When to Use

- "Build our SEO strategy"
- "Keyword research"
- "SEO plan"
- "Improve search rankings"
- "B2B SEO"

## Step-by-Step Process

### Phase 1: Keyword Research

Build a keyword universe in 3 tiers:

**Tier 1 — High Intent (Buying):**

- "best [category] software", "[category] pricing", "[competitor] alternative",
  "[category] vs [competitor]", "buy [category]"
- Target: 10-20 keywords. These convert to pipeline.
- Content: Comparison pages, pricing pages, alternative pages, category pages

**Tier 2 — Medium Intent (Evaluating):**

- "[category] for [industry]", "[category] features", "[category] reviews",
  "how to choose [category]"
- Target: 30-50 keywords. These convert to email list and demo requests.
- Content: Use case pages, feature pages, buyer's guides

**Tier 3 — Low Intent (Learning):**

- "how to [do something your product enables]", "what is [category]",
  "[metric] benchmarks"
- Target: 100-200 keywords. These build authority and feed Tier 1-2 through
  internal links.
- Content: Blog posts, guides, benchmarks, templates

### Phase 2: Content Architecture

- **Pillar pages:** One comprehensive page per Tier 1 keyword. 3,000-5,000 words.
  Links to all related cluster content.
- **Cluster content:** Supporting articles for each pillar. Link back to pillar.
- **Programmatic pages:** Template-driven pages for long-tail (e.g., "[Category]
  for [Industry]" → 50 pages from a template).
- **Content freshness:** Update Tier 1 content quarterly. Republish with new date
  when significant changes. Add new data, examples, and internal links.

### Phase 3: Technical SEO

- **Indexability:** Every valuable page must be indexable. No-index thin content.
- **Page speed:** Core Web Vitals passing. B2B buyers are on enterprise networks
  — slow pages lose them.
- **Mobile:** Responsive design. Over 40% of B2B search now happens on mobile devices.
- **Structured data:** Article, FAQ, HowTo, Product schema where applicable.
- **Internal linking:** Every Tier 1 page links to relevant Tier 2 pages.
  Every Tier 2 page links to relevant Tier 3 pages. Every new post gets 3-5
  internal links from existing content.
- **XML sitemap:** Auto-generated, submitted to Search Console, updated on publish.

### Phase 4: Link Building for B2B

- **Guest posts on industry publications:** 1-2 per month. Quality over quantity.
- **Original research:** Publish data studies. Journalists and bloggers link to
  data. Earns 10-50 backlinks per study.
- **Free tools:** Build free calculators, templates, generators. Earns passive
  backlinks forever.
- **Partner pages:** Integration partners and co-marketing partners link to you.
- **Podcast appearances:** Most podcasts include backlinks in show notes.
- **Avoid:** Link farms, PBNs, paid links. Google penalizes this aggressively.

### Phase 5: Measurement

- **Traffic:** Organic sessions, keyword rankings, click-through rate
- **Conversion:** Demo requests from organic, trial signups from organic,
  email subscribers from organic
- **Pipeline:** Opportunities from organic, pipeline value from organic,
  close rate of organic-sourced deals
- **ROI:** Pipeline value / SEO investment (content + tools + time)

## Output Format

SEO strategy document with: keyword universe, content architecture, technical
audit, link building plan, and measurement dashboard.

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

## Execution Artifacts

- `references/framework-notes.md` — Schwartz, Fishkin, Ahrefs keyword tiers and routing
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator
- `references/seo-strategy-playbook.md` — Repo root: full SEO playbook (Schwartz, Fishkin, Ahrefs)
- `skills/foundation/using-gtm-skills/SKILL.md` — Pattern 25: B2B SEO Stack (step 1)

## Related Skills

- aeo-strategy, pseo-strategy, pillar-pages, content-marketing, content-syndication

---
name: aeo-strategy
description: >-
  Builds an answer engine optimization (AEO/GEO) plan so content gets cited by
  ChatGPT, Perplexity, Gemini, Claude, and Google AI Overviews: answer-first
  structure, entity coverage, citation-worthy data, and AI-visibility
  measurement. Use when the user wants to rank in AI search results or get their
  brand cited by AI assistants. Triggers on: "AEO", "answer engine
  optimization", "AI search", "generative engine optimization", "GEO", "optimize
  for AI search", "get cited by ChatGPT".
license: MIT
compatibility: Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, OpenCode, Goose, Hermes, Windsurf, Zed
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: content-seo
  tags: [content-seo, AEO, AI-search, answer-engine, generative-search]
  frameworks:
    - "Google Search Central — AI features and your website"
    - "Google Search Central — SEO Starter Guide"
    - "Aggarwal et al. — GEO (Generative Engine Optimization, 2023)"
    - "schema.org structured data"
---

# Answer Engine Optimization (AEO)

## Overview

AI search engines (ChatGPT, Perplexity, Gemini, Claude) are capturing 10-30%
of B2B search traffic. Traditional SEO doesn't optimize for AI answers.
AEO ensures your content is the source AI engines cite when users ask questions
in your domain. This skill covers the strategy.

## Authoritative Foundations
- **Google Search Central — AI features and your website** — AI Overviews and AI Mode draw on pages that are indexed and snippet-eligible; there is no special markup, so SEO fundamentals decide inclusion.
- **Google Search Central — SEO Starter Guide** — Write people-first content with clear headings and descriptive anchors so pages are easy to crawl, understand, and quote.
- **Aggarwal et al. — GEO (Generative Engine Optimization, 2023)** — In controlled tests, adding citations, statistics, and quotations raised a page's visibility in generative answers; add evidence, not keywords.
- **schema.org structured data** — Mark up organizations, products, FAQs, and authors so engines can resolve entities and attribute answers to your brand.

## When to Use

- "Optimize for AI search"
- "AEO strategy"
- "Get cited by ChatGPT"
- "Generative engine optimization"
- "Rank in AI search results"

## Step-by-Step Process

### Phase 1: Understand How AI Search Works

AI search engines:

1. Receive a user query
2. Search the web for relevant sources (often using Bing/Google APIs)
3. Read the top sources
4. Synthesize an answer, citing specific sources
5. Present the answer with citations

Your goal: be the source they cite. This requires being the most authoritative,
clear, and well-structured source on the topic.

### Phase 2: AEO Content Principles

- **Authoritative voice:** Cite specific data, name specific experts, reference
  specific studies. AI engines weight named sources higher.
- **Clear structure:** Use H2/H3 headers that mirror the questions people ask.
  "What is [X]?" → H2. "How does [X] work?" → H2. "What are the benefits of [X]?" → H2.
- **Concise answers:** Start each section with a 1-2 sentence definitive answer
  before expanding. AI engines extract these as the "answer snippet."
- **Source citations:** Link to primary sources (studies, reports, official docs).
  AI engines follow citations to verify claims.
- **Entity-rich content:** Mention specific companies, products, people, and
  concepts by name. AI engines build knowledge graphs from entities.
- **Schema markup:** FAQ schema, HowTo schema, Article schema. Helps AI engines
  parse your content structure.

### Phase 3: Content Formats AI Engines Prefer

- **Definitions:** "What is [X]?" — clear, authoritative definition within 50 words
- **Comparisons:** "[X] vs [Y]" — structured comparison table, clear recommendation
- **How-to guides:** Step-by-step with numbered steps, clear prerequisites
- **Statistics/data:** "2026 [X] benchmarks" — tables, charts, sourced data
- **Listicles:** "Top 10 [X] tools" — numbered list with structured descriptions
- **FAQ pages:** Question-answer format, grouped by topic

### Phase 4: Technical AEO

- **Indexability:** AI engines can't cite content they can't crawl. Ensure
  your content is publicly accessible (no paywalls, no login walls).
- **Page speed:** AI engines time out on slow pages. Core Web Vitals passing.
- **Structured data:** Implement FAQ, HowTo, Article, and Organization schema.
- **RSS/API feeds:** Make content available via RSS and API for direct ingestion.
- **LLMs.txt:** Create an llms.txt file at your root domain listing your key
  content pages with descriptions (emerging standard for AI crawlability).

### Phase 5: Measurement

- **AI citation tracking:** Monitor whether your content is cited in AI answers.
  Tools are emerging for this; currently manual sampling works.
- **Brand mentions in AI:** Track whether your brand appears in AI answers vs
  competitors.
- **AI-referred traffic:** Check referrer headers for AI search engines.
- **Correlation with traditional SEO:** AEO optimization almost always improves
  traditional SEO rankings too.

## Output Format

AEO strategy document with: AI search landscape analysis, content optimization
guidelines, content format priorities, technical implementation checklist, and
measurement framework.

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

- AEO Framework: apply only the part that directly improves the requested deliverable.
- Google Search Generative Experience Guidelines: apply only the part that directly improves the requested deliverable.
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

- `references/framework-notes.md` — AEO content principles, schema checklist, Pattern 25 routing
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator
- `references/seo-strategy-playbook.md` — Repo root: §8 AEO / AI search overlap
- the `using-gtm-skills` skill — Pattern 25: B2B SEO Stack (step 4)

## Related Skills

- seo-strategy, pseo-strategy, content-marketing, pillar-pages, faq-seo

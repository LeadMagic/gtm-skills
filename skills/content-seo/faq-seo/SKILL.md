---
name: faq-seo
description: >-
  Build FAQ pages that capture featured snippets and People Also Ask traffic —
  question-driven content strategy. Triggers on: "FAQ SEO", "featured snippet",
  "People Also Ask", "question SEO", "answer content".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: content-seo
  tags: [content-seo, faq, featured-snippets, people-also-ask, questions]
  frameworks: [Google Featured Snippet Optimization, FAQ Schema Best Practices]
---

# FAQ SEO

## Overview
FAQ content captures featured snippets (position zero), People Also Ask boxes,
and voice search results. These are the highest-visibility SERP features —
and they're often the lowest-competition ranking opportunities. This skill
covers question-driven content strategy.

## When to Use
- "Build FAQ content"
- "Target featured snippets"
- "People Also Ask strategy"
- "Question-based SEO"
- "Voice search optimization"

## Step-by-Step Process

### Phase 1: Question Mining
Find the questions your ICP is asking:

- **Google People Also Ask:** Search your core keywords. Mine the PAA boxes.
  Expand each question for more PAA questions. Repeat 3-4 levels deep.
- **Google Autocomplete:** Type your keyword + "how", "what", "why", "when",
  "where", "can", "do", "is" — capture all suggestions.
- **AnswerThePublic / AlsoAsked.com:** Automated question mining tools
- **Reddit:** Search your topic in relevant subreddits. Sort by top posts.
  Look for questions in post titles and comments.
- **Quora:** Search your topic. Sort by most followed questions.
- **Customer conversations:** Sales calls, support tickets, onboarding questions.
  These are the questions with real business intent behind them.
- **Competitor FAQ pages:** What questions are they answering? What are they
  missing that you can own?

### Phase 2: Question Prioritization
Score each question on:
- **Search volume:** 50+ monthly searches preferred
- **Business relevance:** Does answering this lead to your product?
- **Featured snippet opportunity:** Does the current snippet suck? (Short answer,
  no source, from a weak site)
- **Competition:** Can you outrank the current #1? Check domain rating of the
  page currently ranking.

### Phase 3: FAQ Content Structure
For each question, create a dedicated section:

**Format for featured snippets:**
- **Question as H2 or H3:** Exact or near-exact match to the query
- **Answer in 40-60 words:** Clear, definitive, authoritative. Start with the
  answer, then elaborate. This is what Google pulls for the snippet.
- **Elaboration:** 100-300 words expanding on the answer with examples, data,
  or context
- **Related links:** Link to deeper content on the topic

**FAQ page structure:**
- Group questions by topic (H2 per topic group)
- 10-20 questions per page
- FAQ schema markup on every question-answer pair
- Table of contents at the top (jump links to each question)
- CTA after the most business-relevant question

### Phase 4: Schema Implementation
Implement FAQ schema on every question page:
```json
{
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is email verification?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Email verification is the process of..."
    }
  }]
}
```

This makes your content eligible for rich results in Google — the expandable
Q&A format that takes up significant SERP real estate.

### Phase 5: Measurement
- **Featured snippet wins:** Track which questions you own the snippet for
- **PAA appearances:** Track which questions you appear in the PAA box
- **FAQ traffic:** Organic traffic to FAQ pages
- **FAQ-to-conversion:** How many FAQ visitors go on to product pages, sign up,
  or request demos
- **Voice search:** Track voice search queries (available in Search Console
  with some filtering)

## Output Format
FAQ strategy document with: question inventory, prioritization matrix, content
template, schema implementation, and measurement dashboard.



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

## Related Skills
- seo-strategy, aeo-strategy, pillar-pages, content-marketing, landing-pages

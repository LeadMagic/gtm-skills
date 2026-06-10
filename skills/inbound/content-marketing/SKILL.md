---
name: content-marketing
description: >-
  Build content marketing strategies that generate pipeline — SEO/AEO optimization,
  pillar page design, programmatic SEO, content-to-pipeline mapping. Use when the
  user wants to plan content strategy, build a content calendar, improve SEO,
  create pillar content, or generate pipeline from content. Triggers on: "content
  marketing", "SEO strategy", "content strategy", "blog", "pillar page", "content
  calendar", "AEO", "AI search optimization", "programmatic SEO", or any request
  about content-driven growth.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: inbound
  tags: [content, seo, marketing, blogging, strategy]
  related_skills: [landing-pages, social-selling, lead-magnets, seo-strategy, pillar-pages, content-syndication, paid-social-strategy, attribution]
  frameworks:
    - "Dharmesh Shah (HubSpot) — Inbound Methodology & Flywheel"
    - "Chris Walker — Demand Creation & Dark Social"
    - "Eli Schwartz — Product-Led SEO"
    - "Eugene Schwartz — Awareness Levels"
    - "Joe Pulizzi — Content Tilt"
    - "Donald Miller — StoryBrand"
---

# Content Marketing

## Overview

Content marketing that doesn't generate pipeline is just blogging. The
difference is strategy: knowing which content types convert at which
funnel stages, optimizing for AI search (not just Google), and building
content assets that become compounding lead generators.

This skill builds a content strategy that maps to your funnel, prioritizes
by conversion potential, and produces measurable pipeline outcomes — not
just pageviews.

## When to Use

- "Build a content strategy"
- "Plan our content calendar"
- "Improve our SEO"
- "Write pillar content"
- "Set up programmatic SEO"
- "Optimize for AI search (AEO/GEO)"
- "What should we write about?"

## Authoritative Foundations

Eugene Schwartz's five awareness levels determine content type by funnel
stage: Unaware → Problem-Aware → Solution-Aware → Product-Aware → Most Aware.
Each stage requires different content.

Joe Pulizzi's Content Tilt principle: find the intersection where your
expertise meets an underserved audience need. That's your content
differentiation.

Donald Miller's StoryBrand framework structures content around the
customer as hero and your product as guide.

**Dharmesh Shah (HubSpot)** — Inbound flywheel: Attract → Engage → Delight.
Content earns permission; delighted customers accelerate the flywheel via
advocacy and NRR. Contrast with outbound-first and with Walker-style ungated
demand creation. Canonical → `references/dharmesh-shah-hubspot-inbound.md`.
Pattern 27 in `using-gtm-skills`.

**Chris Walker (Refine Labs)** — Demand creation over lead capture. Most B2B
influence happens in dark social (Slack, DMs, podcasts) — optimize for frequency
and education, not form-fill volume. See `references/chris-walker-mental-models.md`.
Pattern 26. Pair with Pattern 27 — Walker builds awareness; inbound captures fit.

**Eli Schwartz — Product-Led SEO** — Map content to product jobs-to-be-done.
SEO strategy detail → `seo-strategy` + `references/seo-strategy-playbook.md`.

## Step-by-Step Process

### Phase 1: Content Audit and Gap Analysis

1. Inventory existing content: pages, posts, guides, tools
2. Score each piece by: traffic, conversions, recency, competitive position
3. Map content to funnel stages — where are the gaps?
4. Identify highest-ROI content types for your ICP

### Phase 2: Content Strategy by Funnel Stage

| Stage | Content Type | Goal | SEO Approach |
|---|---|---|---|
| Unaware | Educational blog, industry data | Capture attention | Long-tail informational keywords |
| Problem-Aware | How-to guides, checklists | Build awareness of the problem | How-to and problem-keyword queries |
| Solution-Aware | Comparison pages, webinars | Position your category | Category and comparison keywords |
| Product-Aware | Case studies, demos, trials | Convert to customer | Brand and product keywords |
| Most Aware | Pricing pages, ROI calculators | Close the deal | Brand + pricing keywords |

### Phase 3: SEO/AEO Optimization

**Traditional SEO (Google):**
- Target keywords with purchase intent, not just volume
- Build topical authority with pillar pages and cluster content
- Technical SEO: speed, mobile, schema markup

**AI Search Optimization (ChatGPT, Perplexity, Gemini):**
- Write clear, factual, well-sourced content
- Structure content for extractability (clear headers, definitions, data)
- Build brand mentions across trusted domains
- Optimize for question-answer format (FAQ sections prominent)

### Phase 4: Content Calendar and Cadence

Minimum viable content cadence by stage:

| Stage | Recommended Cadence |
|---|---|
| <$1M ARR | 2-4 posts/month + 1 pillar per quarter |
| $1-10M ARR | 4-8 posts/month + 2 pillars per quarter |
| $10M+ ARR | 8-16 posts/month + monthly pillars + programmatic |

Every piece should have a conversion path: CTA → relevant lead magnet or
demo request.

## Output Format

Content strategy document with:
- Content audit (traffic, conversions, gaps)
- Topic clusters and pillar page plan
- Content calendar (3-month minimum)
- SEO keyword map with search volumes and intent
- AI search optimization checklist
- Content-to-pipeline measurement framework

## Quality Check

- [ ] Every content piece has a defined funnel stage and conversion goal
- [ ] Topic clusters mapped to ICP pain points and search intent
- [ ] Pillar pages planned with cluster content schedule
- [ ] AI search optimization applied (not just Google SEO)
- [ ] Content calendar published with owner and deadline
- [ ] Measurement: pipeline attributed to content, not just traffic

## Common Pitfalls

1. **Content without conversion paths.** A blog post with 10K views and no
   CTA is a branding expense, not a growth asset. Every piece converts.

2. **SEO without AI search.** As of 2026, AI-powered search (ChatGPT,
   Perplexity) drives significant B2B traffic. Optimize for both.

3. **Volume over strategy.** 50 average posts lose to 10 excellent ones
   that build topical authority. Quality clusters > volume.

4. **No content updates.** Stale content loses rankings. Refresh top
   performers quarterly with new data, examples, and links.

5. **Writing for everyone.** Content that targets "business leaders"
   targets no one. Write for your specific ICP — their title, their
   problems, their reading habits.

## Crisis pause rules

During Sev 2+ incidents (Pattern 33): pause scheduled campaigns, paid social, and thought-leadership posts that look tone-deaf. Demand-creation content resumes after comms lead clears — coordinate with `gtm-leadership` and `references/crisis-management-playbook.md`. Chris Walker dark social still runs; **do not** argue with critics in comment threads.

## Execution Artifacts

- `references/crisis-management-playbook.md` — when to pause content (Pattern 33)
- `references/framework-notes.md` — Named frameworks and reference tables
- `references/dharmesh-shah-hubspot-inbound.md` — Repo root: flywheel, attract-engage-delight
- `references/chris-walker-mental-models.md` — Repo root: demand creation, dark social, frequency
- `references/seo-strategy-playbook.md` — Repo root: Product-Led SEO, content clusters
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **landing-pages**: Conversion pages for content-driven traffic
- **lead-magnets**: Gated content that converts readers to leads
- **social-selling**: Distribute content through LinkedIn and social

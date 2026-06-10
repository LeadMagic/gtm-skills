---
name: marketing-strategy
description: >-
  Build complete B2B marketing strategies — channel mix, budget allocation,
  content strategy, demand generation, brand building, and measurement framework.
  Use when building a marketing plan, allocating marketing budget, designing
  multi-channel campaigns, or creating a marketing operating system. Triggers on:
  "marketing strategy", "marketing plan", "demand generation", "brand strategy",
  "marketing budget", "channel strategy", or any marketing planning request.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: analytics
  tags: [marketing, strategy, demand-gen, brand, channels, budget]
  related_skills: [paid-advertising, content-marketing, content-distribution, social-media-strategy, attribution]
  frameworks: [Product-Led Marketing, Schwartz Awareness Levels, Pulizzi Content Tilt]
---

# Marketing Strategy

## Overview

Marketing strategy is the allocation of scarce resources across channels to
maximize pipeline and revenue. Not "what should we post?" — "given our ICP,
budget, and stage, where does every dollar and hour go?"

This skill builds a complete marketing operating plan: channel mix, budget
allocation by funnel stage, content strategy, demand generation, brand building,
and measurement. The output is a strategy document, not a list of tactics.

## Authoritative Foundations

- **Product-Led Marketing** — Shapes deliverables for this skill — Marketing strategy is the allocation of scarce resources across channels to
maximize pipeline and revenue.
- **Schwartz Awareness Levels** — Shapes deliverables for this skill — Marketing strategy is the allocation of scarce resources across channels to
maximize pipeline and revenue.
- **Pulizzi Content Tilt** — Shapes deliverables for this skill — Marketing strategy is the allocation of scarce resources across channels to
maximize pipeline and revenue.

## When to Use

- "Build our marketing strategy"
- "Plan our marketing for Q1"
- "Allocate marketing budget"
- "Which channels should we invest in?"
- "Design a demand generation engine"
- "Create a marketing operating plan"
- "What should marketing own vs sales?"

## Step-by-Step Process

### Phase 1: Channel Mix by Stage

| Stage | <$1M ARR | $1-10M ARR | $10M+ ARR |
|---|---|---|---|
| **Primary** | Founder-led content + outbound | Content + paid + events | Brand + multi-channel |
| **Content** | LinkedIn (founder), blog | Blog, newsletter, webinars | Editorial, video, podcast |
| **Paid** | None (too early) | LinkedIn + Google (test) | LinkedIn + Google + Meta + programmatic |
| **Events** | None | 1-2 conferences/year | Owned events + major conferences |
| **PR/Media** | Podcast guesting | Trade publications | Tier 1 media + analyst relations |
| **Partners** | None | Integration partners | Full partner ecosystem |

### Phase 2: Budget Allocation

Marketing budget as % of ARR:
- **<$1M ARR:** 20-40% (investment mode, founder-led)
- **$1-5M ARR:** 15-25%
- **$5-20M ARR:** 10-20%
- **$20M+ ARR:** 8-15%

Allocate across channels:
| Channel | Seed/<$1M | Growth/$1-10M | Scale/$10M+ |
|---|---|---|---|
| Content & SEO | 40% | 30% | 25% |
| Paid acquisition | 0% | 25% | 30% |
| Events & field | 10% | 15% | 20% |
| Brand & PR | 5% | 10% | 15% |
| Product marketing | 15% | 10% | 5% |
| Tools & ops | 30% | 10% | 5% |

### Phase 3: Demand Generation Architecture

**Top of funnel (awareness):** Content marketing, paid social, PR, events.
Goal: reach ICP, generate traffic and brand searches. Metric: traffic, brand
search volume, social following.

**Middle of funnel (consideration):** Webinars, case studies, comparison pages,
gated content. Goal: capture contact information, educate buyer. Metric:
MQLs, email subscribers, content downloads.

**Bottom of funnel (conversion):** Demo requests, free trials, sales outreach.
Goal: create sales-qualified opportunities. Metric: pipeline generated,
opportunities created.

**Post-funnel (expansion):** Customer marketing, advocacy, referrals. Goal:
expansion revenue and word-of-mouth. Metric: NRR, referral revenue.

### Phase 4: Brand Building

Brand compounds. It's the reason someone chooses you over a cheaper competitor.

**Brand assets to build:**
- Distinctive point of view (not "we're the best" — "here's what we believe
  that others don't")
- Original research and data (your unique data is your best content)
- Customer stories (named, specific, quantified)
- Executive thought leadership (founder brand = company brand at <$10M ARR)
- Visual identity and design system (consistent across every touchpoint)

**Measurement:** Brand search volume, direct traffic growth, win rate on
competitive deals, inbound demo request growth.

### Phase 5: Marketing-Sales Handoff

Marketing generates demand. Sales converts it. The handoff is where most
companies break.

**MQL definition (marketing side):** ICP fit confirmed + meaningful engagement
(content download, webinar attendance, pricing page visit). Clear criteria,
not "they seem interested."

**SQL definition (sales side):** MQL + explicit buying signal (demo request,
trial sign-up, contact form with budget information).

**SLA:** MQL → first sales touch within 15 minutes (speed-to-lead is the
single biggest conversion lever). Track: MQL→SQL conversion rate, SQL→
opportunity rate, marketing-sourced pipeline.

## Output Format

Marketing strategy document with: channel mix by stage, budget allocation,
demand generation architecture, brand building plan, content calendar (quarterly),
marketing-sales SLA, and KPI dashboard.

## Quality Check

- [ ] Channel mix appropriate for ARR stage
- [ ] Budget allocation by channel with rationale
- [ ] MQL and SQL definitions documented and agreed upon
- [ ] Marketing-sales SLA defined and measured
- [ ] Brand building plan (not just demand gen)
- [ ] Measurement framework: pipeline and revenue, not just leads

## Common Pitfalls

1. **No strategy, just tactics.** "Let's post on LinkedIn and run some ads"
   without a channel mix and budget is a tactic list, not a strategy.

2. **Too many channels too early.** A $1M ARR company doesn't need events,
   programmatic, and TikTok. 2-3 channels done well beats 8 channels done
   poorly.

3. **Marketing-sales misalignment.** Marketing measured on MQLs, sales
   measured on closed revenue. Different incentives, different behaviors.
   Align on pipeline generated, not leads.

4. **Brand as an afterthought.** Brand is the thing that makes outbound
   reply rates go up, paid CPC go down, and win rates increase. Invest
   before you need it.

## Execution Artifacts

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections
This skill includes lightweight artifacts the agent can load on demand:
Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- **paid-advertising**: Paid channel execution
- **content-marketing**: Content strategy and SEO
- **content-distribution**: Multi-channel content distribution
- **attribution**: Marketing ROI measurement

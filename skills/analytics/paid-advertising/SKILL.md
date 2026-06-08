---
name: paid-advertising
description: >-
  Build and manage paid advertising campaigns across B2B platforms — LinkedIn Ads,
  Google Ads, Meta (Facebook/Instagram) Ads, TikTok Ads, and programmatic. Use when
  launching paid campaigns, allocating ad budget, selecting platforms, or optimizing
  paid acquisition. Triggers on: "paid ads", "LinkedIn ads", "Google Ads", "Meta
  ads", "Facebook ads", "TikTok ads", "advertising", "paid acquisition", "ad
  budget", "ad campaign", or any request about paid marketing.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: analytics
  tags: [paid-ads, advertising, linkedin, google, meta, acquisition]
  related_skills: [ad-creative-strategy, a-b-testing, attribution, gtm-metrics]
  frameworks: [Meta Advantage+ Framework, Google Performance Max, LinkedIn Campaign Manager]
---

# Paid Advertising

## Overview

Paid advertising is a dial, not a switch. Start small, measure everything,
double down on what works. B2B advertising is fundamentally different from
B2C — smaller audiences, higher CPCs, longer conversion cycles. Platform
selection matters more than budget size.

This skill covers platform selection, budget allocation, campaign structure,
and measurement across the four major B2B ad platforms plus programmatic.

## Frameworks Referenced

This skill is grounded in named GTM frameworks and operator methodologies, not generic advice:

- **Meta Advantage+ Framework** — used as the named operating framework for this playbook.
- **Google Performance Max** — used as the named operating framework for this playbook.
- **LinkedIn Campaign Manager** — used as the named operating framework for this playbook.

## When to Use

- "Launch paid ads"
- "Which ad platform should I use?"
- "Set up LinkedIn Ads"
- "Allocate ad budget"
- "Optimize Google Ads for B2B"
- "Run Meta ads for SaaS"
- "Measure ad ROI"

## Step-by-Step Process

### Phase 1: Platform Selection

| Platform | Best For | CPC Range | Min Budget | B2B Fit |
|---|---|---|---|---|
| **LinkedIn Ads** | B2B targeting by title, company, industry | $5-15 CPC | $3-5K/mo | Highest — native B2B |
| **Google Ads** | Intent capture (search), retargeting (display) | $2-10 CPC | $2-5K/mo | High — capture demand |
| **Meta (FB/IG)** | Top-of-funnel awareness, retargeting | $1-5 CPC | $1-3K/mo | Medium — audience building |
| **TikTok Ads** | Brand awareness, younger demographics | $0.50-3 CPC | $1-3K/mo | Low-Medium — emerging B2B |
| **Programmatic** | Scale, retargeting, account-based | $2-8 CPM | $5-10K/mo | Medium — ABM |

**For most B2B SaaS, stack priority:** LinkedIn (targeting) → Google (intent capture) → Meta (retargeting). Add TikTok and programmatic when the first three are profitable.

### Phase 2: LinkedIn Ads Deep Dive

LinkedIn is the highest-intent B2B ad platform. Targeting by job title, company
size, industry, and skills means you reach exactly your ICP.

**Ad formats:**
- **Sponsored Content:** In-feed single image, carousel, or video. Best for
  awareness and content promotion.
- **Message Ads (InMail):** Direct message to prospects. Higher engagement,
  higher cost. Best for event invites and demo offers.
- **Text Ads:** Small sidebar/dashboard ads. Low CPC, low volume. Best for
  ongoing brand presence.
- **Document Ads:** Lead gen forms attached to downloadable content. Highest
  conversion for gated assets.

**Campaign structure:**
1. **Top-of-funnel:** Sponsored content promoting educational content. CTA:
   "Read more" or "Download guide." Target: ICP title + industry.
2. **Middle-of-funnel:** Retargeting website visitors with case studies. CTA:
   "See how [similar company] achieved [result]."
3. **Bottom-of-funnel:** Message Ads to decision-makers who engaged. CTA:
   "Book a demo."

**Budget:** Start at $3-5K/mo. LinkedIn minimums are higher than other
platforms. Test for 6-8 weeks before judging ROI.

### Phase 3: Google Ads for B2B

**Search campaigns:** Bid on keywords your ICP searches: problem phrases
("[problem] solution"), competitor names ("[competitor] alternative"),
category terms ("best [category] software").

**Performance Max:** Google's AI-driven campaign type. Combines search,
display, YouTube, discovery, and Gmail. Feed it audience signals (customer
lists, website visitors) and conversion goals. Works well for B2B when fed
quality conversion data.

**Budget:** Start at $2-5K/mo. Monitor search terms report weekly. Add
negative keywords aggressively — B2B search terms leak to consumer intent
quickly.

### Phase 4: Meta Ads for B2B

Meta's strength is audience building and retargeting, not intent capture.

**Campaign types:**
- **Lead Ads:** Native forms within FB/IG. Lowest friction for gated content.
- **Retargeting:** Website visitors, content engagers, video viewers.
- **Lookalike audiences:** Seed from customer list or LinkedIn followers.

**Budget:** Start at $1-3K/mo. Meta needs 50+ conversions/week for algorithm
optimization. Below that, manual bidding outperforms automated.

### Phase 5: Measurement

Track everything. Every ad dollar must be attributable.

**Platform pixels:** LinkedIn Insight Tag, Meta Pixel, Google Ads conversion
tag, TikTok Pixel. Install all four on your website.

**UTM parameters:** Standardize across all campaigns. `utm_source=linkedin`
`utm_medium=cpc` `utm_campaign=product_demo_q1`. Consistent naming prevents
attribution chaos.

**KPIs by funnel stage:**
- **Top-of-funnel:** CPM, CTR, CPC (efficiency metrics)
- **Middle-of-funnel:** Landing page conversion rate, lead quality
- **Bottom-of-funnel:** Cost per demo, cost per opportunity, pipeline generated
- **ROI:** Revenue attributed ÷ ad spend. Target: 3:1+ for B2B, but expect
  6-12 month payback on enterprise deals.

**Attribution:** B2B sales cycles are 3-12 months. First-touch and last-touch
both matter. Multi-touch attribution is ideal. At minimum: track UTM source
through CRM to closed-won.

## Output Format

Paid advertising plan with: platform selection rationale, budget allocation
by platform and funnel stage, campaign structure per platform, creative
requirements, pixel/tracking setup, and KPI dashboard.

## Quality Check

- [ ] Platform selection matches ICP and budget
- [ ] All four major pixels installed (LinkedIn, Google, Meta, TikTok)
- [ ] UTM parameters standardized across all campaigns
- [ ] Campaign structure has clear funnel stage per campaign
- [ ] Budget allocation per platform with rationale
- [ ] Measurement: cost per demo, pipeline, closed revenue (not just leads)

## Common Pitfalls

1. **LinkedIn as the only platform.** LinkedIn gets you targeting but misses
   intent capture (Google) and retargeting (Meta). Run all three.

2. **Not enough budget to test.** LinkedIn at $1K/mo won't produce meaningful
   data. Minimum $3K/mo for 6-8 weeks to validate.

3. **B2C metrics for B2B.** Cost per lead is meaningless if those leads don't
   become pipeline. Measure cost per opportunity and revenue.

4. **No retargeting.** 97% of first-time visitors don't convert. Retargeting
   captures the other 97%.

5. **Creative fatigue.** Same ad for 6 weeks burns out. Rotate creative every
   2-3 weeks. Test multiple variants simultaneously.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- **ad-creative-strategy**: Creative development and testing
- **a-b-testing**: Experiment framework for ad tests
- **attribution**: Multi-touch attribution models
- **gtm-metrics**: Revenue attribution and ROI

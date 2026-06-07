---
name: expansion-selling
description: >-
  Complete expansion and upsell playbook for B2B SaaS — consumption-based
  upsell triggers, cross-sell identification, seat expansion, tier upgrades,
  NRR growth strategies, land-and-expand motions, expansion propensity scoring,
  and measuring expansion revenue. Use when designing expansion motions,
  identifying upsell opportunities, or growing NRR. Triggers on: "expansion
  selling", "upsell strategy", "NRR growth", "land and expand", "cross-sell",
  "expansion revenue", "seat expansion".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "2.0.0"
  author: LeadMagic
  category: growth
  tags: [expansion, upsell, cross-sell, nrr, land-expand, revenue-growth]
  related_skills: [churn-prevention, cs-playbooks, cs-analytics-dashboards, pricing-strategy, customer-onboarding]
  frameworks:
    - "Winning by Design — Bowtie Funnel (post-sale expansion)"
    - "Reforge — Expansion Revenue and Product-Qualified Accounts"
    - "Gainsight — Expansion Selling Framework"
    - "Jason Lemkin (SaaStr) — NRR as the ultimate SaaS metric"
---

# Expansion Selling

## Overview

The most profitable revenue doesn't come from new customers — it comes from
existing ones. New customer acquisition costs 5-7x more than expanding an
existing account. Yet most companies treat expansion as an afterthought. The
mistake: waiting for customers to ask for more instead of systematically
identifying and executing expansion opportunities. This skill covers the
complete expansion playbook: triggers, scoring, execution, and measurement.

## When to Use

Trigger phrases: "expansion strategy", "upsell playbook", "NRR growth",
"land and expand", "cross-sell identification", "seat expansion triggers",
"tier upgrade strategy", "expansion revenue playbook"

## Expansion Triggers (Ranked by Conversion Rate)

| Trigger | Signal | Conversion Rate | Action |
|---|---|---|---|
| Usage approaching limit | "You've used 85% of your plan" | 25-35% | Proactive upgrade offer + migration support |
| Feature request for higher tier | "Can we get SSO?" | 40-60% | "That's in Growth tier. Here's an instant upgrade path." |
| Multi-team adoption | Multiple departments using product | 20-30% | Enterprise upsell with centralized billing |
| New hire at customer | Customer adds headcount | 15-25% | Seat expansion + training for new team |
| QBR uncovers new use case | Customer articulates expansion use case | 30-50% | Proposal within 1 week of QBR |
| Champion requests API access | Building on your platform | 50%+ | Platform/Enterprise tier with API + support |
| Positive NPS + healthy usage | Happy, active customer | 15-25% | Case study ask, then expansion conversation |

## Step-by-Step Process

### Phase 1: Identify Expansion Opportunities

**Expansion Propensity Score:**
```
Score = (Usage approaching limit: +30) +
        (Multi-team adoption: +25) +
        (Requested higher-tier feature: +25) +
        (NPS Promoter: +10) +
        (QBR attendance: +10)

Score > 70: Expansion playbook NOW
Score 40-69: Nurture — showcase advanced features
Score < 40: Focus on adoption before expansion
```

### Phase 2: Expansion Plays

**Play 1: Seat Expansion**
- Trigger: Customer adds team members. Usage per seat increasing.
- Play: "Your team has grown. 5 new team members will benefit from [product].
  Here's a prorated seat expansion for this month."
- Economics: ACV increases linearly with seats. Simple. Predictable.

**Play 2: Tier Upgrade**
- Trigger: Customer requests feature in higher tier, or usage exceeds plan limits.
- Play: "All the features you've asked for are in Growth. Here's a side-by-side
  of what you get. First month at current rate to make the transition easy."
- Economics: ARPU increases. Margin typically improves at higher tiers.

**Play 3: Cross-Sell**
- Trigger: Customer buys Product A. Complementary Product B solves adjacent need.
- Play: "Customers who use [Product A] typically add [Product B] within 6 months.
  Here's how they work together. Bundled pricing for existing customers."
- Economics: New product line revenue without new logo acquisition cost.

**Play 4: Enterprise Expansion**
- Trigger: Multi-team usage, SSO request, API access, security review.
- Play: Enterprise tier with dedicated CSM, SSO, API access, custom SLA, volume
  pricing. "You've outgrown self-serve. Here's the enterprise experience."
- Economics: 3-10x ACV increase. Stickier customer. Higher retention.

### Phase 3: Expansion Economics

**NRR Formula:**
NRR = (Starting MRR + Expansion - Contraction - Churn) / Starting MRR

**Target NRR by stage:**
- Seed: 100%+ (aspirational)
- Series A: 105%+
- Series B: 110%+
- Growth: 115%+

**Expansion as % of New Revenue:**
Best-in-class SaaS: 30-40% of net new ARR comes from expansion
Median SaaS: 15-25%

### Phase 4: Expansion Playbook Execution

**CSM expansion cadence:**
- Month 1-2: Onboarding. No expansion talk. Deliver value first.
- Month 3: Identify expansion triggers. Document use cases.
- Month 4-6: First expansion conversation. Plant the seed.
- Month 6-12: Execute expansion. Close upgrade or cross-sell.

## Quality Checklist

- [ ] Expansion triggers automated (usage approaching limit = alert)
- [ ] Expansion propensity scored for every account
- [ ] NRR tracked monthly with target by customer segment
- [ ] CSM comp tied to NRR (not just retention)
- [ ] Expansion plays documented for each trigger type

## Common Pitfalls

1. **Expanding too early.** Asking for upsell during onboarding = churn risk.
   Fix: Deliver value first. Expand after month 3+.
2. **No expansion comp for CSMs.** CSMs comped on retention only = no expansion.
   Fix: Variable comp tied to NRR. 50% base, 50% variable on NRR target.
3. **Missing consumption triggers.** Customer usage spikes. Nobody notices.
   Fix: Automated alerts when usage hits 80% of plan limit.
4. **One-size expansion play.** Seat expansion for every customer ignores
   cross-sell and tier upgrade opportunities. Fix: Multiple playbooks.


## Output Format

The agent should produce a structured deliverable:

```markdown
# [Deliverable Title]

## Summary
[1-2 sentence summary of what was produced]

## Key Outputs
- [Output item 1]
- [Output item 2]
- [Output item 3]
```

## Quality Check

Before delivering, verify:
- [ ] All required sections complete
- [ ] Output matches the user's stated need
- [ ] No vague or unsupported claims
- [ ] Frameworks cited where applicable

## Common Pitfalls

1. **Incomplete output.** The deliverable is missing critical sections. Fix: verify against the output template before delivering.
2. **Generic advice without specifics.** "Improve your process" without concrete steps. Fix: every recommendation must have a specific action.
3. **Missing framework citations.** Advice without named authorities. Fix: cite the specific framework that grounds each recommendation.
## Related Skills

- `churn-prevention` — Retention is the foundation of expansion
- `cs-playbooks` — Customer success framework
- `cs-analytics-dashboards` — Health scores, expansion propensity
- `pricing-strategy` — Tier design that enables expansion
- `customer-onboarding` — Onboarding that sets up expansion
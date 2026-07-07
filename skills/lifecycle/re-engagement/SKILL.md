---
name: re-engagement
description: >-
  Design re-engagement campaigns for dormant leads and inactive customers —
  win-back sequences, reactivation offers, sunset policies. Triggers on:
  "re-engagement", "win-back", "reactivation", "dormant leads", "inactive customers".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: lifecycle
  tags: [lifecycle, re-engagement, win-back, reactivation, dormant]
  frameworks:
    - "Win-Back Campaign Framework"
    - "Retention Science Methodology"
    - "Reforge — Lifecycle Marketing"
---

# Re-Engagement Campaigns

## Overview

Dormant leads and inactive customers are your lowest-hanging fruit — they already
know you, and reactivation costs 5-7x less than new acquisition. But re-engagement
requires different messaging than new prospect outreach. This skill covers win-back
sequences for both prospects and customers.

## Authoritative Foundations

- **Win-Back Campaign Framework** — Named methodology governing recommendations in this skill's process.
- **Retention Science Methodology** — Named methodology governing recommendations in this skill's process.
- **Reforge — Lifecycle Marketing** — Startup operating cadence — default alive, talk to users, launch fast.

## When to Use

- "Re-engage dormant leads"
- "Win back inactive customers"
- "Reactivation campaign"
- "Sunset policy"
- "Re-engagement sequence"

## Lifecycle Stage

**Engagement** (dormant users) and **Retention** (win-back). Index → `references/gtm-lifecycle-stages.md`.  
Metrics → `references/lifecycle-metrics-by-stage.md` (Engagement + Retention).

## Core Principle

> The biggest mistake in re-engagement is sending "We miss you!" emails.
> Nobody cares that you miss them. They care about what's changed since
> they last engaged — new features, new data, new proof points that make
> your product more valuable now than when they left.

## Step-by-Step Process

### Phase 1: Segmentation

Segment by dormancy type:

**Dormant Leads (never bought):**

- **Cold:** 3-6 months since last engagement. Standard re-engagement sequence.
- **Frozen:** 6-12 months. Condensed sequence. "We've changed" angle.
- **Dead:** 12+ months. One-and-done email. If no reply, suppress.

**Inactive Customers (bought, stopped using or churned):**

- **Lapsed user:** Still paying but not using. Usage dropped >50% for 30+ days.
  Health risk play, not win-back.
- **Recent churn:** Cancelled <90 days ago. Win-back with "what we've fixed" angle.
- **Old churn:** Cancelled 90+ days ago. Different product/market by now. Low probability.

### Phase 2: "What's New" Inventory

Before reaching out, document what's changed since they last engaged:

- 3 biggest product improvements
- 2 new integrations or features
- 1-2 new case studies from their industry
- Any pricing or packaging changes that benefit them
- New data/benchmarks/research relevant to their world

### Phase 3: Re-Engagement Sequences

**Dormant Lead Sequence (3 touches over 14 days):**

- **Touch 1 (Day 1):** "Since you downloaded [original asset]..." + mention 1 new
  thing + soft CTA: "Here's an updated version / related resource."
- **Touch 2 (Day 7):** New insight relevant to their original interest.
  "We published new research on [topic] — thought you'd find it useful."
- **Touch 3 (Day 14):** Breakup. "Closing your file. If [original problem] is
  still relevant, our [new feature] has been getting great feedback.
  Here if you need it."

**Inactive Customer Sequence (3 touches over 21 days):**

- **Touch 1 (Day 1):** "We've made some changes since you left — specifically
  [top 2 improvements]. Would you be open to a 15-minute walkthrough?"
- **Touch 2 (Day 10):** Customer story. "Since you left, [similar company]
  achieved [result] using the features we've added. Here's the case study."
- **Touch 3 (Day 21):** Direct offer. "Come back for [incentive: 1 month free,
  waived setup, etc.]. Here's a link to reactivate in 2 clicks."

### Phase 4: Win-Back Offers

For churned customers, consider:

- **1 month free:** Low cost, high take rate. Best for recent churn.
- **Waived setup/migration:** If complexity was the reason they left
- **Grandfathered pricing:** If price increase caused churn
- **Feature unlock:** "Come back and we'll include [add-on] free for 6 months"
- **No offer:** Some churns aren't worth winning back (bad fit, competitor
  is better for their use case). Let them go.

### Phase 5: Sunset Policy

- **Dormant leads:** After 3-touch sequence with no reply → 6-month cooldown →
  one more attempt → if no reply, suppress from all marketing.
- **Churned customers:** After win-back sequence with no reply → annual check-in
  email only. Don't keep hammering.
- **GDPR compliance:** After 24 months of no engagement, delete or anonymize
  data unless legal requirement to retain.
- **List hygiene:** Remove unengaged contacts quarterly to maintain sender
  reputation and reduce ESP costs.

## Output Format

Re-engagement campaign design with: segmentation criteria, "what's new" inventory,
sequences per segment, win-back offer structure, and sunset policy.

## Quality Check

Before delivering, verify:

- [ ] Dormant leads segmented by recency: cold (3-6 months), frozen (6-12 months), dead (12+ months) — each with a different touch cadence
- [ ] Inactive customers segmented separately: lapsed user (still paying, usage dropped), recent churn (<90 days), old churn (90+ days)
- [ ] 'What's New' inventory completed before first outreach — minimum 3 product improvements, 2 new features/integrations, 1-2 relevant case studies
- [ ] Dormant lead sequence: 3 touches over 14 days, ending with breakup (no infinite nurture)
- [ ] Inactive customer sequence: 3 touches over 21 days, with a specific win-back offer on touch 3
- [ ] Sunset policy defined: dormant leads suppress after 2 sequences; churned customers get annual check-in only; 24-month no-engagement = deletion

## Common Pitfalls

1. **'We miss you' framing.** Generic emotional appeals signal template outreach and produce low response. Fix: open with a specific change since they last engaged — product improvement, new integration, industry-relevant case study.
2. **Same treatment for all dormancy levels.** A 3-month-dormant lead and an 18-month-dead lead are not the same audience. Fix: segment by recency — cold gets full sequence, frozen gets condensed, dead gets one email before suppression.
3. **No sunset policy.** Contacts receive re-engagement emails indefinitely, damaging sender reputation and burning ESP budget. Fix: hard stop after defined touch count; 6-month cooldown before second attempt; suppress after second sequence failure.
4. **Offering discounts to recent churn.** A customer who cancelled last month for a product gap won't return for 10% off. Fix: lead with product changes, not price — 'we fixed the thing you left over' converts better than 'come back for less.'
5. **Treating lapsed users as churned.** A customer who stopped using but is still paying needs a health intervention, not a win-back offer. Fix: separate lapsed-user play (usage recovery, CSM outreach) from churned-customer play (product changes, return offer).

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator
  **Canonical lifecycle (repo root):** `references/gtm-lifecycle-stages.md` (Engagement, Retention) · `references/lifecycle-metrics-by-stage.md`

## Related Skills

- mql-nurture, churn-prevention, email-deliverability, cold-email-strategy, lifecycle-drips

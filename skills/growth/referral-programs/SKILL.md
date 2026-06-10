---
name: referral-programs
description: >-
  Design customer and partner referral programs — 3-tier comp structure,
  double-sided incentive design, referral tracking, platform integration,
  viral mechanics, fraud prevention, and measuring referral revenue against
  published benchmarks. Use when building a referral program, designing
  referral incentives, or launching a customer referral engine. Triggers on:
  "referral program", "referral marketing", "customer referrals", "partner
  referrals", "double-sided rewards", "referral tracking".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "2.1.0"
  author: LeadMagic
  category: growth
  tags: [referral, affiliate, partner, word-of-mouth, customer-referral]
  related_skills: [customer-marketing, partner-programs, cs-playbooks, growth-hacking-tactics, expansion-selling]
  frameworks:
    - "Schmitt, Skiera & Van den Bulte — Referral Programs and Customer Value (Journal of Marketing, 2011)"
    - "GrowSurf / OpenView / SaaSquatch — B2B SaaS Referral Benchmarks"
    - "Nielsen — Trust in Advertising Research"
    - "Dropbox / PayPal — Documented double-sided referral case studies"
---

# Referral Programs

## Overview

Nielsen research shows ~88% of people trust recommendations from someone
they know over any other channel. That trust advantage is the mechanism behind
referral programs — it cannot be bought with ad spend. The mistake teams make:
having no formal referral program and relying on customers to refer spontaneously.
Schmitt, Skiera & Van den Bulte's 2011 study in the *Journal of Marketing*
found referred customers had ~16% higher lifetime value, higher contribution
margin, AND higher retention than non-referred customers — but the effect was
not uniform. Referral programs are less effective at acquiring older or low-margin
customers, which means design matters: the right incentive targets the right
segment, or the economics invert. This skill builds referral programs with
correct incentive structure, fraud-proof mechanics, benchmark-anchored
measurement, and a concrete output reviewable before launch.

## When to Use

- "Build a referral program" or "design referral incentives"
- "Customer referral engine" or "referral marketing"
- "Double-sided rewards" or "referral mechanics"
- "Partner referrals" or "affiliate program"
- "Word of mouth strategy" or "referral tracking"
- "Referral program benchmarks" or "referral CAC"

## Authoritative Foundations

- **Schmitt, Skiera & Van den Bulte — "Referral Programs and Customer Value"
  (Journal of Marketing, 2011; Wharton / Goethe).** The canonical academic
  study on referral program outcomes. Key finding: referred customers generate
  ~16% higher CLV, higher contribution margin, and higher retention than
  non-referred customers acquired through other channels. Critical caveat: the
  effect was weakest for older customers and lower-margin segments — which means
  you cannot assume every referred customer is a better customer. This justifies
  building a double-sided design (reward currency tied to product value metric)
  and targeting the ask at high-margin, high-engagement segments. Used in
  Phase 1 (segment selection) and Phase 6 (measurement benchmarks).
- **Dropbox and PayPal — Documented double-sided referral case studies.**
  Dropbox's double-sided storage reward (500MB to referrer, 500MB to referred)
  drove 3,900% user growth in 15 months. The design lesson: reward currency =
  product value metric (storage for a storage product). PayPal's early $20→$10
  cash reward drove ~7-10% daily user growth; it worked because cash-in-payments
  trust was the adoption barrier — the reward matched the friction. Both programs
  converged on double-sided design. See references/framework-notes.md for the
  incentive design decision tree.
- **GrowSurf / OpenView / SaaSquatch / Cello — B2B SaaS Referral Benchmarks.**
  Published statistics roundup: 20-40% of new SaaS customers attributable to
  referral or word-of-mouth; referred customers show 16-25% higher LTV and ~20%
  lower churn; referred leads convert 3-5x higher than paid acquisition; healthy
  participation rate is 5-15% of active users; invitation acceptance is 25-40%;
  referral CAC typically runs 40-60% below blended CAC; in-app referral prompts
  generate ~4x more shares than email-only asks. Full benchmark table in
  references/framework-notes.md.
- **Nielsen — Trust in Advertising Research.** ~88% of consumers trust
  recommendations from people they know over any other channel. This is the
  psychological foundation for why referred leads convert at 3-5x paid — the
  trust transfer from referrer to prospect is a structural advantage that no
  creative or copy optimization can replicate.

## Step-by-Step Process

### Phase 1: Segment and Incentive Design

**Target the right segment first.** Per Schmitt et al., the CLV lift is real
but not uniform. Before setting incentives, identify the customer cohort most
likely to produce high-value referred customers: typically the customer who
(a) uses the product frequently, (b) operates in networks of similar companies,
and (c) has seen a concrete, shareable outcome. Build the ask sequence around
this cohort — not your entire install base.

**Referral types by motion:**

| Type | Referrer | Referred | Use When |
|---|---|---|---|
| Customer referral | Existing paying customer | Prospect in their network | B2B SaaS; relationship-based sales |
| Affiliate / partner | External promoter or partner | Prospect | High-volume, transactional products |
| Employee referral | Staff member | Job candidate or customer | Talent pipeline; lower frequency |
| Investor referral | Board member or investor | Prospect or partner | Enterprise; warm intro network |

**Incentive model selection (match reward to product value metric):**

| Model | Example | Design Lesson | Best For |
|---|---|---|---|
| Double-sided cash | "$100 to you, $100 to them" | Cash works when trust or price is the barrier | High-ACV products; financial tools |
| Double-sided product credit | "1 month free each" | Reinforces core product value (Dropbox model) | SaaS with low marginal cost; credit drives usage |
| Feature unlock | "Unlock premium features with 3 referrals" | Reward = perceived product ceiling | Freemium; consumer-facing SaaS |
| Status / priority | "Jump the waitlist" | Scarcity drives action; social proof for new referral | Pre-launch; invite-only products |
| Charitable donation | "$50 donated in your name" | Appeals to mission-driven buyers; lower direct cost | Nonprofit, mission-aligned brands |

### Phase 2: Economics and Compensation Structure

**Standard B2B referral comp:** 10-15% of first-year contract value. Pay as a
one-time reward on first payment — not on sign-up. Paying on sign-up means you
absorb cost from leads that never convert; paying on collection eliminates that
fraud vector.

**Three-tier structure (base → Silver → Gold):**

| Tier | Referrals | Commission | Additional Benefits |
|---|---|---|---|
| Base | 1-5 | 10% of year-1 ACV | Referral dashboard; public acknowledgment |
| Silver | 6-15 | 12% of year-1 ACV | Priority support; early feature access |
| Gold | 16+ | 15% of year-1 ACV | Co-marketing; executive sponsor; advisory input |

Non-monetary benefits at each tier increase stickiness and reduce pure cash
dependency — SaaSquatch data shows credit and product rewards often outperform
cash in SaaS referral programs because they deepen product engagement.

### Phase 3: Mechanics and Referral Flow

**Standard referral flow:**
1. Referrer receives unique trackable link (auto-generated on signup or via portal)
2. Referrer shares via email, social, or 1:1 message
3. Prospect clicks link → tagged with referrer ID at landing page
4. Prospect signs up → attribution recorded
5. Prospect completes first payment → referrer reward triggered
6. Referrer sees conversion status in live dashboard

**In-app prompt placement:** Per GrowSurf research, in-app referral prompts
generate ~4x more shares than email-only asks. Place prompts at activation
milestones (first meaningful outcome reached) and after positive NPS responses,
not on the day of signup.

**Fraud prevention rules (hard rules, not suggestions):**
- Pay on collection, not on sign-up
- Track email domain to prevent self-referral (block referrer's own domain)
- Require the referred account to reach a minimum usage milestone before reward pays
- Cap reward per referrer per month during launch to detect gaming patterns

### Phase 4: Tooling

For B2B SaaS, tool selection by scale:

| Tool | Best For | Notable Features |
|---|---|---|
| PartnerStack | B2B SaaS partner + customer referral | Multi-program, payout management, partner portal |
| Rewardful | Stripe-native SaaS affiliate/referral | Simple setup, Stripe integration, low overhead |
| FirstPromoter | SaaS affiliate and referral | Real-time dashboards, tiered commissions |
| Referral Rock | SMB referral programs | Multi-incentive, campaign builder |
| Friendbuy | E-commerce and SaaS | A/B testing, double-sided reward flows |

PartnerStack or Rewardful cover most B2B SaaS cases. Choose Rewardful for
Stripe-native billing simplicity; choose PartnerStack when managing both
customer referrals and partner/reseller programs in a single platform.

### Phase 5: Launch Sequence

1. **Soft launch (weeks 1-2):** Recruit 10-20 high-NPS customers manually.
   Message: "You've seen results with [product]. Would you refer peers?"
   Do not rely on email automation alone — personal outreach doubles response rate.
2. **Program announcement (week 3):** Email to full customer base with clear
   incentive and one-click link generation.
3. **In-app activation (week 3):** Place referral CTA at key activation milestone.
4. **Monthly leaderboard (ongoing):** Email top referrers their rank; surface
   Gold-tier progress to Silver referrers. Gamification increases participation
   without increasing cash spend.
5. **Quarterly review:** Audit referral cohort quality vs non-referral cohort
   on retention and expansion. Adjust incentive tier thresholds based on data.

### Phase 6: Measurement

Benchmark your program against published SaaS referral data. Full source table
in references/framework-notes.md.

| Metric | Benchmark (B2B SaaS) | Red Flag |
|---|---|---|
| Referral share of new customers | 20-40% | < 5% = no program traction |
| Participation rate (active users) | 5-15% | < 3% = friction or wrong incentive |
| Invitation acceptance rate | 25-40% | < 10% = wrong target segment or weak offer |
| Referral CAC vs blended CAC | 40-60% lower | Above blended = fraud or high gift/cash cost |
| Referred customer LTV vs non-referred | +16-25% | Negative = wrong segment being referred |
| Referred customer churn vs non-referred | ~20% lower | Parity = program not selecting best-fit customers |
| Referred leads conversion rate vs paid | 3-5x higher | < 1.5x = referral quality issue |

## Output Format

Referral program design document containing: (1) segment selection rationale
with ICP profile of target referrer cohort; (2) incentive structure — model
selection with design-lesson rationale mapped to product value metric, full
three-tier compensation table with non-monetary benefits; (3) economics model —
estimated referral CAC, year-1 reward cost as % of ACV, and payback period;
(4) referral mechanics flow — step-by-step from link generation to reward payout,
including fraud prevention rules; (5) tooling recommendation with selection
rationale; (6) launch sequence with week-by-week milestones; (7) measurement
dashboard — benchmark table with program-specific targets and red-flag thresholds
anchored to published B2B SaaS data.

## Quality Check

Before delivering, verify:
- [ ] Incentive model maps reward currency to the product's core value metric (not arbitrary cash)
- [ ] Comp structure pays on collection, not on sign-up (fraud prevention hardcoded)
- [ ] Participation rate target set at 5-15% of active users — not "all customers"
- [ ] In-app referral prompt placement is at activation milestone, not day-of-signup
- [ ] Measurement dashboard includes LTV and churn comparison, not just lead volume
- [ ] Referral CAC estimate is calculated and compared to blended CAC
- [ ] Segment selection excludes cohorts where Schmitt et al. show weakest CLV lift

## Common Pitfalls

1. **One-sided incentives.** "$50 to you if your friend signs up" underperforms
   double-sided offers because there is no social obligation — the referrer feels
   they are extracting value from a friend. Fix: always reward both sides (Dropbox,
   PayPal both demonstrated this). If budget is constrained, halve the single-sided
   amount and split it.
2. **Paying on sign-up, not collection.** 100 sign-ups, 0 paying → $5,000 in
   rewards for nothing. Fix: reward triggers on first payment or minimum milestone.
   Encode this as a non-negotiable rule in your referral platform configuration.
3. **No referral dashboard for referrers.** Referrers share, then have no
   visibility on whether referrals converted. They stop sharing after 1-2
   attempts. Fix: real-time dashboard showing clicks, sign-ups, conversions, and
   pending reward for every referrer.
4. **Asking at the wrong moment.** Referral asks sent during onboarding — before
   the customer has experienced value — generate low participation. Fix: trigger
   the ask at the first meaningful activation milestone (first outcome achieved,
   first positive NPS response), not on day zero.

## Execution Artifacts

- `references/framework-notes.md` — Benchmarks, incentive decision tree, fraud rules
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator
**Lifecycle (Referral stage):** `references/gtm-lifecycle-stages.md` · `references/lifecycle-skill-index.md` · Pattern 18 in `using-gtm-skills`
**Canonical lifecycle (repo root):** `references/gtm-lifecycle-stages.md` (Referral) · `references/lifecycle-metrics-by-stage.md` · `skills/analytics/gtm-metrics/templates/stage-health-scorecard.md`

## Related Skills

- customer-marketing, partner-programs, cs-playbooks, growth-hacking-tactics, expansion-selling

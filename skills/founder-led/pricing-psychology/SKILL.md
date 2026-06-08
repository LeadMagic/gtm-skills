---
name: pricing-psychology
description: >-
  SaaS pricing psychology and tactics for B2B founders. Use when designing
  pricing tiers, testing price points, building pricing pages, handling
  discounting strategy, adding new pricing dimensions, or optimizing
  monetization. Covers anchoring, decoy effect, charm pricing, framing,
  versioning, and willingness-to-pay research methodology.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: founder-led
  tags: [pricing, psychology, monetization, tiers, packaging, anchoring, discounting]
  related_skills: [pricing-strategy, roi-calculator, pricing-page-builder, deal-desk, sales-enablement]
  frameworks:
    - "Madhavan Ramanujam (Monetizing Innovation) — Willingness-to-pay research"
    - "Dan Ariely — Predictably Irrational (anchoring, decoy effect, relativity)"
    - "Patrick Campbell (ProfitWell/Price Intelligently) — SaaS pricing data"
    - "Richard Thaler — Nudge (choice architecture, default effects)"
    - "Robert Cialdini — Influence (scarcity, social proof in pricing)"
    - "Jason Cohen (WP Engine) — The 3-tier trap and Goldilocks pricing"
---

# Pricing Psychology

## Overview

Most SaaS companies price by guessing or copying competitors. The mistake:
setting price based on cost-plus or competitor-minus-10% instead of
value-based pricing anchored in how humans actually perceive value. Pricing
is the highest-leverage revenue lever — a 1% price increase typically delivers
11% profit increase (McKinsey). This skill covers the psychology of pricing,
research methods, tier architecture, and testing frameworks.

## When to Use

Trigger phrases: "pricing psychology", "pricing tiers design", "pricing page",
"price anchoring", "decoy pricing", "willingness to pay", "pricing test",
"discounting strategy", "value-based pricing", "price increase"

## Authoritative Foundations

### Ramanujam — Monetizing Innovation
The 4 failures of pricing:
1. **Feature shock:** Building features nobody will pay for
2. **Minivation:** Underpricing features people would pay more for
3. **Hidden gem:** Not charging for something people value highly
4. **Undead:** Keeping features nobody uses because "someone might"

**The rule:** Do willingness-to-pay research BEFORE building. Not after.

### Dan Ariely — Predictably Irrational
**Anchoring:** The first price a buyer sees becomes their reference point.
If you show Enterprise at $999/mo first, Starter at $199 seems cheap.
If you show Starter at $99 first, Starter at $199 seems expensive.

**Decoy effect (asymmetric dominance):**
| Plan | Price | Features |
|---|---|---|
| Basic | $29 | 5 features |
| **Pro** | **$49** | **15 features** |
| Enterprise | $99 | 17 features |

Pro is the target. Enterprise exists to make Pro look like better value
than Enterprise (nearly as many features, half the price). Basic is the
entry point.

**The Economist example (classic Ariely):**
- Web only: $59
- Print only: $125  ← THE DECOY (nobody buys it)
- Web + Print: $125
Result: Web only 16% → 68% chose Web + Print when decoy present.

### Patrick Campbell — SaaS Pricing Data
- Companies that change pricing once/year grow 2x faster than those that don't
- The optimal number of pricing tiers is 3-4 (more = paralysis)
- 70% of SaaS companies are under-priced (they're leaving money on the table)
- Annual billing should offer 10-20% discount, not 2 months free (too aggressive)

## Step-by-Step Process

### Phase 1: Pricing Research

**Willingness-to-Pay (WTP) Research (Ramanujam method):**

1. **Feature prioritization:** List 10-20 features. Ask prospects: "Which of
   these would you pay for? Rank by value."
2. **Van Westendorp Price Sensitivity Meter:** Ask 4 questions:
   - At what price would this be so expensive you'd never consider it? (Too expensive)
   - At what price would this be expensive but you'd still consider it? (Expensive/high)
   - At what price would this be a bargain? (Cheap/good value)
   - At what price would this be so cheap you'd question its quality? (Too cheap)
3. **Gabor-Granger:** Start at a high price, ask "would you buy at $X?"
   If yes, increase. If no, decrease. Find the maximum acceptable price.
4. **Conjoint analysis:** Present trade-offs: "Feature A at $X vs Feature B at
   $Y vs Feature C at $Z." What do they choose?

**Minimum viable pricing research (do this week):**
- Interview 10 customers: "At what price would this product be too expensive
  that you'd never consider buying it?"
- Interview 10 lost deals: "Was price a factor in your decision? What would
  have made this a 'no-brainer' purchase?"
- Survey 50 prospects: Van Westendorp 4-question survey

### Phase 2: Tier Architecture

**The 3-Tier Rule (Jason Cohen):**
- **Good:** The entry point. Low friction, low commitment. Goal: adoption.
- **Better:** The target. Where you want most customers. Goal: value capture.
- **Best:** The anchor. Expensive. Goal: make Better look great.

**Tier design principles:**

1. **Limit dimensions.** 3-5 pricing dimensions max. Common SaaS dimensions:
   - Users/seats
   - Usage volume (emails, API calls, contacts, events)
   - Features (access to specific capabilities)
   - Support level (email → chat → dedicated CSM)
   - SSO/Security (enterprise gate)

2. **Use the decoy.** The middle tier should be the obvious choice. The top
   tier should be clearly premium. The bottom tier should be clearly limited.

3. **Price the delta.** The price jump between tiers should feel justified by
   the value jump. If Starter is $49 and Growth is $199, the value jump needs
   to feel 4x.

4. **Annual discount architecture:**
   - 10-20% for annual (not "2 months free" = 17%, that's fine)
   - Don't offer monthly on Enterprise (annual only)
   - Show annual as default, monthly as option

**Example tier architecture (value metric: contacts/month):**

| Dimension | Starter | Growth | Enterprise |
|---|---|---|---|
| Price/month (annual) | $49 | $199 | $999 |
| Contacts | 1,000 | 10,000 | 100,000 |
| Users | 1 | 5 | Unlimited |
| Email finding | 500/mo | 5,000/mo | Unlimited |
| Integrations | None | CRM | CRM + Webhooks |
| Support | Chat | Priority | Dedicated CSM |
| SSO | No | No | Yes |

**The Growth tier is the target.** Starter captures price-sensitive. Enterprise
makes Growth look like incredible value and captures enterprise demand.

### Phase 3: Pricing Page Psychology

**Left-to-right pricing (most common):**
Cheapest → Mid → Most expensive
Starter → Growth → Enterprise

**Right-to-left pricing (anchoring play):**
Most expensive → Mid → Cheapest
Enterprise → Growth → Starter

**Which to use:** Left-to-right is safer. Right-to-left works when you have
a genuinely premium product and want to anchor high. Test both.

**Pricing page rules:**

1. **One recommended tier.** Highlight it. "Most Popular" badge. This reduces
   choice paralysis. 70-80% of customers will choose the recommended tier
   if it's well-positioned.

2. **Charm pricing (psychology):**
   - $49 feels cheaper than $50 (left-digit effect)
   - $199 feels cheaper than $200
   - Use for SMB/self-serve. For enterprise, round numbers feel more premium.

3. **Remove the currency symbol when possible:**
   - "$49/mo" vs "49/mo" — removing $ reduces "pain of paying" (neuroeconomics research)
   - Only works for self-serve. Enterprise expects $.

4. **Monthly vs Annual toggle:**
   - Default to annual pricing (higher LTV, lower churn, better cash flow)
   - Show monthly as secondary
   - Annual savings: "$49/mo billed annually ($588/yr)" vs "Monthly $69/mo"

5. **Feature comparison:**
   - Checkmarks for included features
   - Dashes or empty for excluded (don't use X marks — they're hostile)
   - "Contact us" for Enterprise (don't list a price if it's custom)

6. **Risk reversal:**
   - "Free 14-day trial, no credit card required"
   - "30-day money-back guarantee"
   - "Cancel anytime"

### Phase 4: Testing Pricing

**What to test:**
1. Price points ($49 vs $59 vs $69 for Starter)
2. Tier count (3 vs 4 tiers)
3. Tier names (Starter/Growth/Enterprise vs Basic/Pro/Business)
4. Metric (per-user vs per-contact vs flat-rate)
5. Annual discount (10% vs 17% vs 20%)

**Testing methodology:**
- A/B test on pricing page (requires enough traffic — 1,000+ visits/month per variant)
- Customer interviews: "At what price would you walk away?"
- Sales team feedback: "What are the top 3 pricing objections?"
- Win/loss analysis: correlate price point with close rate

**How to raise prices on existing customers:**
- Grandfather existing customers for 12 months (they appreciate it)
- Give 90 days notice: "Your price will increase from $49 to $59 on [date]"
- Add value before raising: "We've added X, Y, Z features since you joined"
- Segment: power users (can pay more) vs at-risk (be careful)
- Expect 5-10% churn, compensated by 10-20% revenue increase from remaining

### Phase 5: Discounting Psychology

**When to discount:**
- Annual prepay (10-20% — standard, expected)
- Multi-year contracts (lock in revenue, give discount)
- Volume (legitimate scaling discount)
- Non-profit/education (segment-based)

**When NOT to discount:**
- First-call discounts ("50% off if you sign today") — desperate, trains bad behavior
- Competitor-match discounts — race to the bottom
- "I need to check with my manager" discounts — destroys pricing integrity

**Discount framing:**
- BAD: "We'll give you 20% off" (sounds like your price was fake)
- GOOD: "The annual plan includes a 17% discount" (standard, expected)
- BAD: "We can come down to $39" (you just lost all leverage)
- GOOD: "At $49/mo annual, you'll save $240/year vs monthly" (framing as savings)

**The Concession Menu (instead of discounting):**
- "I can't reduce the price, but I can include onboarding at no cost" ($1,000 value)
- "I can't discount, but I can give you 2 months free on an annual contract"
- "I can't reduce the per-seat price, but I can cap your seats at 50 while you grow"

## Output Format

```
PRICING STRATEGY — [Company]

Research Summary:
- WTP range: $X - $Y (Van Westendorp optimal price point: $Z)
- Competitor pricing: [range and positioning]
- Price sensitivity by segment: [data]

Tier Architecture:
| Dimension | Starter | Growth | Enterprise |
|---|---|---|---|
| Price (annual) | $X | $Y | $Z — TARGET |
| ... | | | |

Pricing Page Plan:
- Layout: [left-to-right / right-to-left]
- Recommended tier: [name]
- Annual default: [yes/no — savings X%]
- Risk reversal: [trial/guarantee details]

Testing Plan:
- Test 1: [variable] — hypothesis — success metric
- Test 2: ...

Price Increase Plan:
- Segments: [who, how much, when, grandfathering]
- Communication: [timeline, channel, messaging]
```

## Implementation Checklist

- [ ] WTP research conducted (interviews, survey, or conjoint — not guesswork)
- [ ] 3 tiers with one clear "recommended" (the decoy/recommendation effect)
- [ ] Tier price deltas justified by value jumps (no random gaps)
- [ ] Annual pricing shown as default with 10-20% savings
- [ ] Pricing page has risk reversal (trial, guarantee, or both)
- [ ] Discounting policy documented (when, how much, who approves)
- [ ] Concession menu exists (alternatives to straight discounts)
- [ ] Price increase process defined (notice period, grandfathering, communication)

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Cost-plus pricing.** "Our costs are $X, so we charge $X + 30%." This
   ignores what customers are willing to pay. You might be leaving 50%+ on
   the table. Fix: Value-based pricing. What is the problem worth to them?

2. **Competitor-minus pricing.** "Competitor charges $100, we'll charge $80."
   This starts a race to the bottom. The cheapest option is not the best
   option — it's the cheapest. Fix: Differentiate on value, not price.

3. **Too many tiers.** 5+ tiers creates analysis paralysis. Prospects can't
   decide, so they leave. Fix: 3 tiers. 4 maximum. Each with a clear persona.

4. **Flat pricing with no expansion.** If every customer pays the same price,
   your revenue is capped at customer count. Fix: Add a usage dimension
   (contacts, emails, API calls, seats) so revenue grows with customer usage.

5. **Founder discount reflex.** "They asked for a discount, so I gave them
   20%." This trains customers to ask and destroys your pricing integrity. Fix:
   Concession menu, not straight discounts. "I can't reduce the price, but I
   can..."

6. **No annual option.** Monthly billing = monthly churn risk. Annual billing
   = 12 months of committed revenue, lower churn, better cash flow. Fix:
   Always offer annual with 10-20% discount. Default to annual on pricing page.

## Related Skills

- `pricing-strategy` — Ramanujam pricing models, tier design, packaging
- `roi-calculator` — Business case construction, 3-scenario projections
- `pricing-page-builder` — Page design, tier layout, conversion optimization
- `deal-desk` — Pricing models, discount guidance, proposals
- `sales-enablement` — Value communication, pricing objection handling

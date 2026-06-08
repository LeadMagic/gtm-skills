---
name: pricing-strategy
description: >-
  Design SaaS pricing strategy using willingness-to-pay research, packaging, value metrics, competitive anchors, and expansion paths. Produces pricing hypotheses, package architecture, discount guardrails, and test plan. Use when setting prices, changing packages, evaluating usage-based pricing, or fixing monetization.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: foundation
  tags: [pricing, monetization, tiers, packaging, willingness-to-pay, discount]
  related_skills: [gtm-context, competitive-intel, positioning-messaging, deal-desk]
  frameworks: [Madhavan Ramanujam Monetizing Innovation, Price Intelligently, ProfitWell, OpenView SaaS Benchmarks]
---
# Pricing Strategy

## Overview

The most expensive pricing mistake in B2B SaaS is pricing to cost-plus or competitor-minus rather than pricing to value. When pricing is disconnected from willingness-to-pay, companies either leave revenue on the table (pricing too low, the most common error) or kill their pipeline (pricing too high for the perceived value). The non-obvious rule is that the pricing model — the unit of value you charge for — is more important than the price point itself. A well-designed model that aligns with how customers perceive value can support aggressive price points. A misaligned model makes even discount prices feel expensive.

This skill produces a complete pricing strategy grounded in Madhavan Ramanujam's "Monetizing Innovation" 2x2 framework (willingness-to-pay vs pricing model), the Price Intelligently/ProfitWell methodology for value-based pricing research, and OpenView's SaaS benchmarks for stage-appropriate pricing patterns. The deliverables include a Pricing Model Recommendation (which model to use and why), a Tier Structure Design (feature differentiation, pricing anchors, expansion paths), a Willingness-to-Pay Analysis (based on customer research), a Competitive Pricing Comparison, and Discount Authority Guidelines (who can discount, by how much, and when).

The pricing strategy is designed to be a living document — pricing should be reviewed quarterly in early-stage companies and at least annually in scaled companies. This skill provides the initial design and the framework for ongoing optimization.

## When to Use

- User says "design our pricing" or "create pricing strategy" → activate this skill
- User asks "how should we price this" or "what pricing model" → use this skill
- User mentions "monetization," "tier design," "packaging," "price increase" → this skill applies
- User is launching a new product or entering a new market and needs pricing
- Current pricing feels arbitrary or was set without research
- User needs discount authority guidelines for the sales team
- After gtm-context and competitive-intel are complete

Do NOT use for:
- Deal-specific pricing for a single prospect — use deal-desk for that
- ROI/business case construction for a specific deal — use roi-calculator
- Pricing page copy or UX design — use landing-pages or design-system-gtm

## Authoritative Foundations

- **Madhavan Ramanujam — Monetizing Innovation.** The 2x2 framework that plots willingness-to-pay against pricing model alignment. Products in the top-right quadrant (high willingness-to-pay, aligned model) are pricing-optimized. Products in the bottom-left (low willingness-to-pay, misaligned model) need fundamental redesign, not discounting. This skill uses the 2x2 as the diagnostic framework for pricing model selection.

- **Price Intelligently (Patrick Campbell) / ProfitWell.** The value-based pricing methodology: survey customers to measure relative preference across feature bundles, use Van Westendorp and Gabor-Granger techniques to establish willingness-to-pay ranges, and design tiers based on value differentiation rather than arbitrary feature splits. This skill adapts these techniques for agent-assisted execution.

- **OpenView — SaaS Benchmarks and Expansion Revenue.** OpenView's research on pricing benchmarks by company stage, the importance of expansion revenue (NRR > 120% for top-quartile companies), and the pricing model patterns that drive high NRR. Applied in tier design and expansion path planning.

- **Simon-Kucher & Partners — Pricing Power Framework.** The concept that pricing power comes from differentiation that customers value. The skill applies this by linking to the unique capabilities and defensible differentiators from the positioning-messaging skill.

- **Zuora — Subscription Model Index.** Subscription pricing patterns across B2B SaaS: per-seat, per-usage, tiered, hybrid, freemium, and enterprise. This skill maps each pattern to the conditions where it's optimal.

## Prerequisites

- **Upstream skills:** gtm-context (provides ICP, ACV, deal size, buying committee) and competitive-intel (provides competitive pricing data).
- **Required inputs:** ICP definition, current or planned product features, competitive pricing data (at minimum: how competitors price and what tiers they offer), current or target ACV range.
- **Optional:** Historical pricing data (average deal size, discounting patterns, win rate by price band), customer willingness-to-pay survey data, churn-by-plan data.
- **Optional tools:** LeadMagic Company Search API can identify companies within specific revenue bands to validate TAM by pricing segment.

## Step-by-Step Process

### Phase 1: Intake

Ask all questions at once:

1. What is your current pricing model? (Per-seat, per-usage, tiered subscription, flat-rate, freemium, hybrid — or not yet set.)
2. What is your current price point (or range) and how was it determined?
3. What is your target ACV range? ($1K-$5K, $5K-$25K, $25K-$100K, $100K+)
4. Who is the economic buyer for your product? What budget does this typically come from?
5. List your product's features. Which features do your best customers value most?
6. What do your top 3 competitors charge? (Provide as much detail as you have — public pricing, estimated, unknown.)
7. What is your current discounting practice? (Average discount %, who can approve, when discounts are used.)
8. What is your gross margin? (Revenue minus COGS as percentage. This determines your pricing floor.)
9. Do you have any willingness-to-pay data? (Customer surveys, win/loss data showing price objections, A/B pricing tests.)
10. What is your growth strategy? (Land-and-expand, high-velocity SMB, enterprise top-down, product-led self-serve.)

### Phase 2: Research

**Competitive Pricing Deep-Dive:** For each named competitor, collect:
- Published pricing (list prices for each tier)
- Pricing model (per-seat, per-usage, flat, hybrid)
- What's included at each tier
- Free tier / freemium offering (what's free, what triggers payment)
- Known discounting patterns (from sales team intelligence, G2 reviews, Glassdoor)
- Pricing page URL and any pricing-related marketing claims
- Recent pricing changes (have they raised or lowered?)

**Market Pricing Benchmarks:** Research pricing patterns in your category:
- What is the modal pricing model in your category? (Per-seat dominates in collaboration tools. Per-usage dominates in API/infrastructure. Tiered flat-rate dominates in SMB SaaS.)
- What is the typical price range for your target ACV segment?
- Are prices in your category rising or falling?

**Unit Economics Analysis:** Calculate your pricing parameters:
- **Floor:** Cost to serve one customer (COGS per customer). You cannot sustainably price below this.
- **Ceiling:** The value your product creates for the customer. A product that saves $100K/year can be priced up to some fraction of that — typically 10-30% for B2B SaaS.
- **Target Zone:** Between 20-50% of the cost of the best alternative (including status quo cost).
- **Gross Margin at Proposed Price:** (Price - COGS) / Price. Should exceed 70% for SaaS companies.

### Phase 3: Execution

**Step 1: Pricing Model Selection (Ramanujam 2x2)**

Evaluate candidate pricing models against two dimensions: willingness-to-pay and model alignment.

**Pricing Model Options:**

| Model | Description | Best When |
|-------|-------------|-----------|
| Per-Seat / Per-User | Charge per user per month | Value scales with user count; product is collaborative |
| Usage-Based | Charge per unit of consumption (API calls, data volume, events) | Value is directly proportional to usage; product is infrastructure-like |
| Tiered Flat-Rate | Fixed price for each tier with feature differentiation | Value is feature-based; clear feature-value segmentation exists |
| Freemium | Free tier with paid upgrades | Product has viral adoption; free users convert at meaningful rates |
| Hybrid | Per-seat base plus usage overages | Value has both a fixed component (access) and variable component (usage) |
| Enterprise / Custom | Negotiated annual contracts | ACV > $50K; each deal requires custom scope |

**Model Selection Criteria:**
- Value alignment: Does the unit of pricing match how the customer perceives value?
- Revenue predictability: Can you forecast revenue with this model?
- Growth alignment: Does the model support your growth strategy (land-and-expand vs high-velocity)?
- Competitive fit: Does the model differentiate you or match the category norm?
- Operational complexity: Can your billing system support this model?

Select the primary model and describe the rationale. If appropriate, recommend a secondary model for enterprise/large accounts.

**Step 2: Tier Structure Design**

Design 3-4 tiers using the principle of value-based feature differentiation:

**Tier Design Principles:**
- **Good-Better-Best:** Three tiers is optimal for most B2B SaaS products. A fourth "Enterprise" tier for custom deals.
- **Feature Differentiation, Not Feature Gating:** Each tier should unlock meaningful new value, not just remove arbitrary limits. The upgrade from Tier 1 to Tier 2 should feel like a natural expansion of capability, not a paywall.
- **The Pricing Anchor Effect:** The highest tier's price serves as an anchor that makes the middle tier look like the best value. The middle tier should be the one you want most customers to choose.
- **Gap Ratios:** Price gaps between tiers should follow approximate ratios of 1:2:4 or 1:3:6 depending on value differentiation.

For each tier, specify:
- **Tier name and price** (monthly and annual, with annual discount if applicable)
- **Included features** (be specific — "advanced reporting" is too vague)
- **Limits** (users, usage, storage, integrations — whatever applies to your model)
- **Target customer profile** (which ICP segment should buy this tier)
- **Upgrade trigger** (what event or need should cause a customer to move up)
- **Key differentiator from the tier below** (the one thing that makes this tier worth the price increase)

**Step 3: Willingness-to-Pay Analysis**

If survey data or customer interviews are available, analyze willingness-to-pay. If not, construct a proxy analysis:

**Van Westendorp Price Sensitivity Questions:**
- At what price would this product be so expensive you'd never consider it? (Too expensive)
- At what price would this product be expensive but you'd still consider it? (Expensive)
- At what price would this product be a bargain? (Bargain)
- At what price would this product be so cheap you'd question its quality? (Too cheap)

Plot the responses to identify:
- **Optimal Price Point (OPP):** The intersection of "too expensive" and "too cheap" curves.
- **Indifference Price Point (IDP):** The price at which equal numbers find it expensive and cheap.
- **Range of Acceptable Prices:** The band between the "expensive" and "bargain" curves.

**Proxy Analysis (when no direct data exists):**
- Estimate willingness-to-pay based on the cost of the best alternative
- Benchmark against comparable products in adjacent categories
- Use the "10% of value created" heuristic for B2B SaaS (product saves $100K, price at ~$10K)

**Step 4: Competitive Pricing Comparison**

Build a comparison table:

| Feature/Capability | Your Product | Competitor A | Competitor B | Competitor C |
|-------------------|-------------|-------------|-------------|-------------|
| Pricing Model | [Model] | [Model] | [Model] | [Model] |
| Entry Price | [$] | [$] | [$] | [$] |
| Mid-Tier Price | [$] | [$] | [$] | [$] |
| Top-Tier Price | [$] | [$] | [$] | [$] |
| Key Differentiator | [What you offer they don't] | | | |

Analyze your position:
- Are you priced above, at, or below the category average? Why?
- If below: can you justify a higher price based on differentiation?
- If above: can you point to specific value that justifies the premium?

**Step 5: Discount Authority Guidelines**

Establish rules for when, how much, and who can discount:

**Discount Tiers:**

| Authority Level | Max Discount | Conditions | Approval Required |
|----------------|-------------|------------|-------------------|
| SDR/BDR | 0% | No discount authority | N/A |
| AE | 10% | Multi-year commitment only | Manager approval |
| Senior AE / Team Lead | 15% | Competitive deal, multi-year | Documented |
| Sales Manager | 20% | Strategic account, competitive must-win | VP sign-off |
| VP Sales / CRO | 30% | Enterprise deal, logo acquisition, strategic | CEO for >25% |
| CEO | Any | Extraordinary circumstances only | Documented rationale |

**Discount Triggers (when to offer):**
- Multi-year commitment (standard: 5-10% for annual, 10-15% for 2-year, 15-20% for 3-year)
- Volume / bundling (standard: 5-15% for multiple products)
- Competitive displacement (case-by-case, must document competitor and price gap)
- Early-stage logo acquisition (strategic, limit to first 10-20 customers)
- Non-profit / education (standard: 10-25%)

**Discount Anti-Patterns (when not to offer):**
- "The prospect asked for a discount" — not a reason
- End of quarter pressure — deals should close on value, not discount urgency
- "Competitor X is cheaper" — unless competitor X offers equivalent value (rarely true)
- "It's a big logo" — unless there's a defined logo program with documented strategic value

### Phase 4: Delivery

Present in this order:
1. Executive Recommendation (model, tiers, price ranges, one-paragraph rationale)
2. Pricing Model Analysis (Ramanujam 2x2 assessment)
3. Tier Structure Design (full detail for each tier)
4. Willingness-to-Pay Analysis (with methodology and assumptions)
5. Competitive Pricing Comparison
6. Discount Authority Guidelines
7. Implementation Roadmap (what needs to change operationally to support this pricing)

## Output Format

```markdown
# Pricing Strategy: [Company Name]

## Executive Recommendation

**Recommended Pricing Model:** [Model name]
**Tiers:** [Number of tiers] with [annual/monthly] pricing
**Price Range:** [$X - $Y] per [unit]
**Target ACV:** [$Z]
**Rationale:** [One paragraph]

---

## 1. Pricing Model Analysis (Ramanujam 2x2)

### Willingness-to-Pay Assessment
[Analysis of WTP for target customers]

### Model Alignment Assessment
[How well each candidate model aligns with customer value perception]

### Selected Model
**Model:** [Name]
**Rationale:** [Why this model was selected]
**Trade-offs:** [What this model gives up vs alternatives]

### 2x2 Positioning
- Willingness-to-Pay: [High/Medium/Low]
- Model Alignment: [High/Medium/Low]
- Quadrant: [Top-Right = optimized, Bottom-Left = needs redesign]

---

## 2. Tier Structure Design

### Tier 1: [Name] — $[Price]/[unit]
- Target: [ICP segment]
- Features: [List]
- Limits: [List]
- Upgrade Trigger: [When they need Tier 2]
- Key Differentiator: [What Tier 2 offers that makes the upgrade compelling]

### Tier 2: [Name] — $[Price]/[unit]
- Target: [ICP segment]
- Features: [List]
- Limits: [List]
- Upgrade Trigger: [When they need Tier 3]
- Key Differentiator: [What Tier 3 offers]

### Tier 3: [Name] — $[Price]/[unit]
- Target: [ICP segment]
- Features: [List]
- Limits: [List]
- Upgrade Trigger: [When they need Enterprise]
- Key Differentiator: [What Enterprise offers]

### Enterprise: [Name] — Custom Pricing
- Target: [Enterprise ICP segment]
- Features: [List plus custom scope]
- Minimum Commitment: [Annual, multi-year, minimum seats/usage]

### Annual Discount
- Annual commitment: [X]% discount
- 2-year commitment: [Y]% discount
- 3-year commitment: [Z]% discount

---

## 3. Willingness-to-Pay Analysis

### Methodology
[Van Westendorp, Gabor-Granger, surveys, proxy analysis — what was used]

### Key Findings
- Optimal Price Point: [$X]
- Indifference Price Point: [$Y]
- Range of Acceptable Prices: [$A - $B]
- Too Expensive Threshold: [$C]
- Too Cheap Threshold: [$D]

### Assumptions and Limitations
[Transparent statement of methodology limitations]

---

## 4. Competitive Pricing Comparison

| Feature/Capability | Us | Competitor A | Competitor B | Competitor C |
|-------------------|----|-------------|-------------|-------------|
| Model | [Model] | [Model] | [Model] | [Model] |
| Entry Price | [$] | [$] | [$] | [$] |
| Mid-Tier Price | [$] | [$] | [$] | [$] |
| Top-Tier Price | [$] | [$] | [$] | [$] |

### Position Analysis
- Category average mid-tier price: [$X]
- Our mid-tier price: [$Y] = [Above/At/Below] category average
- Justification: [Why our position is correct]

---

## 5. Discount Authority Guidelines

| Level | Max Discount | Conditions | Approval |
|-------|-------------|------------|----------|
| AE | 10% | [Conditions] | Manager |
| Senior AE | 15% | [Conditions] | VP |
| Sales Manager | 20% | [Conditions] | VP |
| VP Sales | 30% | [Conditions] | CEO |
| CEO | Any | [Documented rationale] | Board optional |

### Discount Triggers
| Trigger | Standard Discount | Notes |
|---------|------------------|-------|
| Annual commitment | [X]% | [Notes] |
| Multi-year (2+) | [Y]% | [Notes] |
| Logo acquisition | [Z]% | [Notes — cap on number] |
| Competitive displacement | Case-by-case | [Notes] |

---

## 6. Implementation Roadmap

### Immediate (Week 1-2)
- [ ] [Action item]

### Short Term (Month 1)
- [ ] [Action item]

### Medium Term (Month 2-3)
- [ ] [Action item]
```

## Quality Check

Before delivering, verify:

- [ ] Does the pricing model align with how customers perceive value?
- [ ] Are there 3-4 tiers with clear differentiation between them?
- [ ] Does the middle tier represent the best value (anchor effect)?
- [ ] Are annual discounts offered to improve cash flow and reduce churn?
- [ ] Is the pricing floor above COGS (positive gross margin at every tier)?
- [ ] Is the pricing ceiling below a defensible fraction of value created?
- [ ] Are discount guidelines specific (who, how much, when, approval)?
- [ ] Is the competitive comparison honest about competitor pricing?
- [ ] Are implementation steps actionable and time-bound?
- [ ] Would a new AE know exactly what discount they can offer without asking?

## Common Pitfalls

1. **Pricing based on competitor pricing minus 10%.** This is the race to the bottom. If you're always 10% cheaper than the category leader, you're training the market to see you as the discount option. Price based on your value, not their price. If your value is higher, price higher. If it's lower, fix the product, not the price.

2. **Feature gating instead of feature differentiation.** When Tier 1 has "up to 5 reports" and Tier 2 has "unlimited reports," the customer feels punished for choosing Tier 1. When Tier 1 has "standard reports" and Tier 2 has "custom reports with AI insights," the customer feels they're getting more value at Tier 2. Design tiers around capability unlocks, not artificial limits.

3. **Too many tiers.** Four tiers is the maximum most buyers can evaluate. Five or more creates decision paralysis and reduces conversion. Three is optimal for most B2B SaaS products: an entry tier that's easy to buy, a middle tier that's the obvious best value, and a top tier for power users.

4. **No annual plan or insufficient annual discount.** Annual billing improves cash flow, reduces churn, and increases valuation multiples. Standard annual discounts range from 10-20%. If your annual discount is less than 10%, few customers will choose it. If it's more than 25%, you're leaving too much revenue on the table.

5. **Discount guidelines that are too permissive.** "AEs can discount up to 20%" without conditions teaches AEs that discounting is the primary closing tool. Discount authority should be narrow by default with clear conditions for escalation. The best discount guideline is: "Discounts are offered in exchange for something — multi-year commitment, expansion, case study, reference."

6. **Enterprise tier that's just "contact us."** "Contact us for pricing" without any anchor or range drives away qualified enterprise buyers who need to budget before engaging. Provide a "starting at" price or a range. The actual price can be negotiated up from the starting point.

7. **Pricing that doesn't account for expansion revenue.** If your model is per-seat, the path to higher NRR is seat expansion. If your model is usage-based, it's consumption growth. If your model is tiered, it's upgrades. Design the tier structure so that expansion is a natural path, not a forced upsell.

8. **Treating pricing as fixed once set.** Pricing should be reviewed quarterly in early-stage companies and at least annually in scaled companies. Market conditions change, competitors move, and value perception evolves. The pricing strategy document should include a review cadence and triggers for revisiting (e.g., "revisit if win rate drops below X%").

## Related Skills

- **gtm-context**: Run before this skill. Provides ICP, ACV, deal size, and buying committee data.

- **competitive-intel**: Run before this skill. Provides competitor pricing intelligence and competitive positioning.

- **positioning-messaging**: Run before this skill. Provides unique capabilities and defensible differentiators that justify price premiums.

- **deal-desk**: Run after this skill. Consumes pricing model and discount guidelines for deal-specific pricing decisions.

- **roi-calculator**: Run after this skill. Uses the pricing tiers to build ROI projections that justify the investment to economic buyers.

- **saas-metrics-calculator**: Run after this skill. Uses the pricing model to project unit economics (LTV, CAC payback, NRR) at different price points.

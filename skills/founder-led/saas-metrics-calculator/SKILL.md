---
name: saas-metrics-calculator
description: >-
  Calculate and interpret SaaS metrics for founders: MRR, ARR, NRR, GRR, churn, CAC payback, LTV:CAC, burn multiple, Rule of 40, cohort retention, and scenario models. Use when building investor updates, dashboards, board materials, pricing decisions, or growth diagnostics.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.2.0"
  author: LeadMagic
  category: founder-led
  tags: [saas, metrics, calculator, benchmarks, kpis, unit-economics]
  related_skills: [financial-modeling, gtm-metrics, pricing-strategy, churn-prevention, expansion-selling, board-meeting-prep, saas-outcomes, exiting-company]
  frameworks:
    - "David Skok — SaaS Metrics 2.0"
    - "Jason Lemkin (SaaStr) — Burn Multiple"
    - "David Sacks — Burn Multiple (via SaaStr)"
    - "Bessemer Venture Partners — Rule of 40"
    - "SaaS Capital — B2B SaaS Benchmarks"
    - "KeyBanc — Private SaaS Survey"
    - "Meritech Capital — Public SaaS Benchmarks"
---
# SaaS Metrics Calculator

## Overview

SaaS metrics answer whether your business model works. The mistake: cherry-picking
the metric that makes you look good (usually ARR growth) and ignoring the metric
that tells the truth (usually churn or CAC payback). This skill calculates all
key metrics from minimal inputs, applies stage-aware benchmarks, diagnoses which
lever to pull first, and produces board-ready, investor-ready output. Every
formula is documented. Every benchmark is sourced. For **exit weight by buyer
type**, load `references/metric-definitions-exit-weight.md`.

## Authoritative Foundations

- **David Skok (forEntrepreneurs).** LTV:CAC, CAC payback, fully loaded S&M —
  canonical formulas for diligence.
- **Jason Lemkin / David Sacks.** Burn multiple = net burn ÷ net new ARR;
  primary capital-efficiency gate at Series A+. → `references/david-sacks-saas-metrics.md`
- **Bessemer Cloud Atlas.** Rule of 40, stage benchmarks, PLG essays.
  → `references/bessemer-cloud-atlas.md`
- **SaaS Capital / KeyBanc.** Stage benchmarks for private B2B SaaS.
- **Meritech Capital.** Public SaaS cohort — implied ARR, Rule of 40 composition, NRR medians. `references/meritech-saas-benchmarks.md`. Reconcile private vs public → `references/benchmark-reconciliation.md`.

## When to Use

Trigger phrases: "calculate my SaaS metrics", "what is my LTV:CAC ratio?",
"how long is my CAC payback?", "what is my NRR?", "run a complete metrics
analysis", "what should my metrics be at this stage?", "SaaS benchmarks",
"board metrics dashboard", "investor metrics package"

## The Core Metrics (18 Formulas)

### Revenue Metrics

**MRR (Monthly Recurring Revenue)**
= Sum of all **committed** monthly subscription revenue. Normalize annual contracts to
monthly: Annual ÷ 12. Exclude one-time PS unless board asks for total revenue.

**Deep dive:** definition variants (committed vs recognized vs billings), ASC 606 summary,
consumption, deferred revenue → `references/saas-mrr-accounting-nuances.md`.
Bridge template → `references/templates/mrr-bridge-template.md`.
Bookings vs billings vs revenue → `references/bookings-billings-revenue-matrix.md`.
Definition conflicts → `references/benchmark-reconciliation.md` (MRR / ARR row).

**ARR (Annual Run Rate)**
= MRR × 12 (for monthly businesses) OR sum of annual contract values

**ARPA (Average Revenue Per Account)**
= MRR ÷ Paying Customers

**ARR per Employee**
= ARR ÷ Total Full-Time Employees
- $0-5M ARR: $50-100K is normal (you're investing)
- $10-50M ARR: $100-200K is good
- $100M+: $200K+ is efficient

### Churn Metrics

**Logo Churn Rate (monthly)**
= Customers Lost in Month ÷ Customers at Start of Month

**Revenue Churn Rate (monthly)**
= Churned MRR ÷ MRR at Start of Month

**NRR (Net Revenue Retention)**
= (Starting MRR + Expansion MRR - Contraction MRR - Churned MRR) ÷ Starting MRR
- >100%: Growing within existing base (good)
- >120%: Best-in-class enterprise SaaS
- <100%: Shrinking — churn > expansion

**GRR (Gross Revenue Retention)**
= (Starting MRR - Churned MRR - Contraction MRR) ÷ Starting MRR
- Excludes expansion (purity test of retention only)
- >80% is good. >90% is excellent.

**SaaS Quick Ratio**
= (New MRR + Expansion MRR) ÷ (Churned MRR + Contraction MRR)
- >4x: Excellent — growing 4x faster than shrinking
- 2-4x: Healthy
- <2x: Each new dollar is partially canceled by churn
- <1x: Shrinking

### Unit Economics

**CAC (Customer Acquisition Cost — fully loaded)**
= Total S&M Spend ÷ New Customers Acquired
Total S&M includes: salaries (SDRs, AEs, managers, VP Sales), marketing team,
tools (CRM, outreach, enrichment), ad spend, events, content production.
NOT just ad spend.

**LTV (Contribution Margin Method — correct)**
= (ARPA × Gross Margin %) ÷ Monthly Churn Rate

**LTV:CAC Ratio**
= LTV ÷ CAC
- 3-5x: Healthy (invest more in growth)
- 5-10x: Very efficient (you could be spending more on growth)
- <3x: CAC too high or LTV too low (fix before scaling)

**CAC Payback Period (months)**
= CAC ÷ (ARPA × Gross Margin %)
- <12 months: Good (recover investment within a year)
- 12-18 months: Acceptable for higher-ACV products
- >24 months: Dangerous (capital-intensive, slow returns)

### Efficiency Metrics

**Magic Number**
= Net New ARR (current quarter) ÷ S&M Spend (prior quarter)
- >1.0: Efficient growth (invest more)
- 0.5-1.0: Moderate (optimize before scaling)
- <0.5: Inefficient (fix GTM before spending more)

**Burn Multiple**
= Net Cash Burn ÷ Net New ARR
- <1x: Excellent (burning less than $1 for $1 of new ARR)
- 1-2x: Good
- >2x: Worrying — high burn relative to growth
- David Sacks: "The burn multiple is the single best measure of capital efficiency."

**Rule of 40**
= Revenue Growth Rate % + Profit Margin %
- >40%: Healthy SaaS business
- 0-40%: Acceptable at scale
- <0%: Unsustainable

**Revenue per Employee**
= ARR ÷ Total Employees
- See ARR per Employee above

## Step-by-Step Process

### Phase 1: Input Collection

**Minimum inputs needed (these 10 numbers):**

| # | Input | Where to Find It |
|---|---|---|
| 1 | Current MRR | Stripe/Chargebee/Recurly dashboard |
| 2 | Last month's MRR | Same source, prior period |
| 3 | Paying customers (current) | Billing system |
| 4 | New customers acquired (month) | CRM — opportunity closed-won |
| 5 | Customers lost (month) | CRM — opportunity closed-lost (churn reason) |
| 6 | Expansion MRR added (month) | Billing system — upgrades |
| 7 | Contraction MRR (month) | Billing system — downgrades |
| 8 | Churned MRR (month) | Billing system — cancellations |
| 9 | Total S&M spend (month, fully loaded) | Accounting system |
| 10 | Gross Margin % | Accounting system (Revenue - COGS) ÷ Revenue |

### Phase 2: Calculation

Calculate all 18 metrics using the formulas above. Present in three buckets:
1. Revenue & Growth (MRR, ARR, ARPA, ARR/Employee)
2. Retention & Health (Churn, NRR, GRR, Quick Ratio)
3. Efficiency & Unit Economics (LTV, CAC, LTV:CAC, CAC Payback, Magic Number,
   Burn Multiple, Rule of 40)

### Phase 3: Stage-Aware Benchmarking

| Metric | Pre-Seed | Seed ($500K-2M) | Series A ($2-10M) | Series B ($10-50M) | Growth ($50M+) |
|---|---|---|---|---|---|
| **YoY Growth** | N/A (PMF) | 100-300%+ | 80-150% | 50-100% | 30-50% |
| **NRR** | >100% (aspirational) | >100% | >105% | >110% | >115% |
| **GRR** | >80% | >85% | >88% | >90% | >92% |
| **Logo Churn (mo)** | <3% | <2.5% | <2% | <1.5% | <1% |
| **LTV:CAC** | >3x | 3-5x | 3-5x | 3-5x | 4-6x |
| **CAC Payback (mo)** | <12 | <12 | <12 | <15 | <18 |
| **Magic Number** | >0.5 | >0.75 | >0.75 | >0.75 | >1.0 |
| **Burn Multiple** | >3x (investing) | <2x | <1.5x | <1.5x | <1x |
| **Rule of 40** | N/A | >20% | >30% | >35% | >40% |
| **Gross Margin** | >70% | >72% | >75% | >75% | >78% |

### Phase 4: Diagnosis and Recommendations

**Diagnostic decision tree:**

1. **If Churn > 2% monthly:** Fix retention before scaling growth. High churn
   makes every marketing dollar less valuable. Root cause: onboarding, product
   gaps, or wrong ICP.
2. **If CAC Payback > 18 months:** Fix GTM efficiency before adding headcount.
   Root cause: low conversion rates, undersized ACV, or expensive channels.
3. **If NRR < 100%:** You're leaking revenue faster than you can fill. Fix
   expansion (upsells, cross-sells) before hiring more SDRs.
4. **If Magic Number < 0.5:** Stop spending on growth. Fix conversion rates,
   target better ICP, or increase ACV.
5. **If Burn Multiple > 2x:** You're burning too much per dollar of growth.
   Either growth is too slow or costs are too high. PE and late-stage buyers
   discount above 1.5x (Lemkin).

Load `references/metric-definitions-exit-weight.md` for exit/raise weight by metric.

**The lever order (highest ROI first):**
1. Reduce churn (1% monthly churn reduction = 10-20% LTV increase)
2. Improve NRR (expansion > new logo acquisition cost)
3. Increase ACV (move upmarket, better pricing)
4. Optimize CAC (channel mix, conversion rates)
5. Add headcount (when metrics support it)

## Output Format

```
SAAS METRICS DASHBOARD — [Company] — [Month Year]

REVENUE & GROWTH
| Metric | Current | Last Month | YoY | Benchmark | Status |
|---|---|---|---|---|---|
| MRR | $X | $X | | | |
| ARR | $X | $X | $X | | |
| Net New ARR | $X | | | | |
| YoY Growth | X% | | | [stage] | |

RETENTION & HEALTH
| Metric | Current | Target | Benchmark | Status |
|---|---|---|---|---|
| Logo Churn | X% | | | |
| NRR | X% | | | |
| GRR | X% | | | |
| Quick Ratio | Xx | | | |

UNIT ECONOMICS & EFFICIENCY
| LTV | $X | | | |
| CAC | $X | | | |
| LTV:CAC | Xx | | | |
| CAC Payback | X mo | | | |
| Magic Number | X | | | |
| Burn Multiple | Xx | | | |
| Rule of 40 | X% | | | |

PRIORITY ACTIONS (ranked by ROI):
1. [Action 1] — expected impact: [metric change]
2. [Action 2]
3. [Action 3]
```

## Implementation Checklist

- [ ] LTV uses contribution-margin method (NOT raw revenue)
- [ ] CAC includes fully-loaded S&M spend (NOT just ad spend)
- [ ] Same time period for spend and new customers
- [ ] Metrics segmented by channel and cohort where possible
- [ ] Benchmarks matched to current ARR stage
- [ ] Red-flagged metrics have specific recommended actions
- [ ] NRR and GRR both calculated (NRR includes expansion, GRR doesn't)
- [ ] Burn Multiple calculated alongside Magic Number (they tell different stories)

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Raw-revenue LTV.** Using total revenue instead of contribution margin.
   If your gross margin is 70%, raw LTV overstates by 43%. Fix: Always use
   ARPA × Gross Margin % ÷ Monthly Churn Rate.

2. **Under-counting CAC.** "Our CAC is $200" but you only counted ad spend,
   not the salaries of the 4 SDRs and 2 AEs who closed those customers. Fix:
   Fully-loaded CAC. All S&M expense ÷ new customers.

3. **Mixing time periods.** Using last month's spend but this quarter's new
   customers creates garbage metrics. Fix: Same period. If you spent $100K in
   Q1 and acquired 50 customers, use Q1 for both.

4. **Company-wide averages hiding problems.** Your enterprise segment might
   have LTV:CAC of 8x while SMB is 1.5x. Average says 3x — which is false
   comfort. Fix: Segment by channel, cohort, and customer size.

5. **Ignoring the Burn Multiple.** Growth at all costs is dead. A company growing
   100% with a 3x Burn Multiple is less healthy than a company growing 50% with
   a 1x Burn Multiple. Fix: Report Burn Multiple alongside growth rate.

6. **Annualizing monthly churn wrong.** Monthly churn of 2% ≠ 24% annual churn.
   It compounds: 1 - (1 - 0.02)^12 = 21.5%. Fix: Use the compound formula or
   track actual annual churn from cohort data.

## Execution Artifacts

- `references/metric-definitions-exit-weight.md` — formulas, benchmarks, exit weight by buyer
- `references/david-sacks-saas-metrics.md` — burn multiple, efficiency gates (repo root)
- `references/bessemer-cloud-atlas.md` — Rule of 40, VC-stage benchmarks (repo root)
- `references/saas-mrr-accounting-nuances.md` — **canonical** MRR/ARR accounting deep dive (repo root)
- `references/bookings-billings-revenue-matrix.md` — bookings vs billings vs GAAP revenue (repo root)
- `references/templates/mrr-bridge-template.md` — logo + expansion − contraction − churn (repo root)
- `references/framework-notes.md` — routing index
- `templates/output-template.md` — deliverable shell
- `scripts/check-output.py` — deliverable validator

**Canonical lifecycle (repo root):** `references/lifecycle-metrics-by-stage.md` (per-stage formulas) · `references/gtm-lifecycle-stages.md` · `references/templates/stage-health-scorecard.md`

**Cross-skill:** `exiting-company/references/due-diligence-metrics-pack.md`, `fundraising-strategy/references/vc-milestone-gates.md`, `financial-modeling/references/unit-economics-exit-bridge.md`

## Related Skills

- `financial-modeling` — SaaS P&L, cash flow, runway, headcount model
- `gtm-metrics` — Pipeline velocity, CAC by channel, WbD GTM Index
- `pricing-strategy` — Pricing impact on ARPU and LTV
- `churn-prevention` — Early warning signals, health scoring, intervention
- `expansion-selling` — Consumption triggers, NRR growth
- `board-meeting-prep` — Board-ready metrics dashboard

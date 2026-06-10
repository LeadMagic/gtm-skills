---
name: financial-modeling
description: >-
  SaaS financial modeling for founders — operating model, runway, headcount,
  DCF valuation, consumption-based pricing models, cohort analysis, unit
  economics by segment, ARR bridge/build, 3-scenario forecasting, and
  board-ready financials. Use when building financial model, projecting
  runway, modeling fundraising, valuation, or planning headcount. Covers
  discounted cash flow, consumption revenue models, expansion modeling,
  and SaaS-specific valuation.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "2.2.0"
  author: LeadMagic
  category: founder-led
  tags: [financial-model, saas-metrics, runway, unit-economics, dcf, valuation, consumption-pricing]
  related_skills: [saas-metrics-calculator, fundraising-strategy, board-meeting-prep, pricing-strategy, pricing-psychology, co-founder-dynamics, yc-ecosystem, investor-updates]
  frameworks:
    - "David Skok (Matrix Partners) — SaaS Unit Economics"
    - "Ben Murray (The SaaS CFO) — SaaS Financial Operations"
    - "Aswath Damodaran (NYU Stern) — DCF Valuation"
    - "Bessemer Venture Partners — Cloud 100 Benchmarks"
    - "Christoph Janz (Point Nine) — SaaS Napkin"
    - "Jason Lemkin (SaaStr) — Growth Efficiency, Burn Multiple"
    - "KeyBanc SaaS Survey — ARR multiple comps"
    - "Meritech Capital — Public SaaS Benchmarks & Meritech Rule of 40"
    - "Force Management — Pod Economics & Headcount Planning"
---

# SaaS Financial Modeling

## Overview

Most founder financial models are fiction — aggressive growth curves with no
operational logic underneath. The mistake: building a top-down model ("we'll
capture 1% of a $100B market") instead of a bottom-up operating model ("we'll
hire 3 AEs at $120K OTE, each producing $800K quota in month 6"). This skill
covers building a real operating model that investors trust, boards respect,
and YOU can use to make decisions. Now includes DCF valuation, consumption-based
pricing models, cohort analysis, and full ARR bridge/build methodology.

## When to Use

Trigger phrases: "financial model", "SaaS P&L", "runway calculation", "DCF
valuation", "consumption pricing model", "cohort analysis", "ARR bridge",
"headcount plan", "revenue forecast", "409A valuation", "unit economics model",
"annual GTM budget", "operating budget", "variance review", "QuickBooks vs NetSuite"

## Authoritative Foundations

### David Skok — SaaS Unit Economics
LTV = (ARPA × Gross Margin %) ÷ Monthly Churn Rate. LTV/CAC > 3x is investable.
CAC Payback < 12 months is good.

### Aswath Damodaran — DCF Valuation
"The value of any asset is the present value of its expected future cash flows."
For startups: high growth + high risk = high WACC (20-30% for early stage).

### Ben Murray — The SaaS CFO
Three P&L layers: Revenue (new + expansion - churn), COGS (20-30%), OpEx
(S&M + R&D + G&A). Model per-head where possible. PE exits require EBITDA
bridge — see `references/unit-economics-exit-bridge.md`.

### Meritech Capital — Public SaaS Benchmarks
For IPO-track scenarios, compare implied ARR growth, FCF margin, and Meritech Rule of 40 to public medians. `references/meritech-saas-benchmarks.md`. Private stage gates remain in `references/benchmark-reconciliation.md`.

### Force Management — Pod Economics & Headcount Planning
Bottom-up headcount from pod economics: group SDR/AE/SE/CSM into pods, run
pod cost % of ARR (target ≤35% at 80% ramp), link quota attainment distribution
to hiring triggers. See `references/force-management-playbook.md` (repo root)
and `references/unit-economics-exit-bridge.md`.

## Step-by-Step Process

### Phase 1: Revenue Model (Bottom-Up)

Do NOT model "1% of market." Model customers × average revenue.

```
Monthly Revenue Model:

New Customers = (SDR meetings × demo conversion rate) + inbound + expansion
Average ACV = $X (new logo) / $X (expansion)
Monthly Churn = Previous month customers × monthly churn rate
Net New MRR = (New × ACV) + Expansion - Churned
```

**Revenue inputs to get right:**
- SDR productivity: 8-12 meetings/month per SDR
- Demo conversion: 20-30% for qualified meetings
- Sales cycle: 30-90 days depending on ACV
- AE ramp: 3-6 months to full quota
- Monthly churn: 1-3% SMB, 0.5-1% mid-market, <0.5% enterprise

### Phase 2: Headcount Model

Model every hire with: role, salary, start month, ramp, fully-loaded cost.
Fully-loaded = base × 1.25-1.35 (benefits, payroll tax, tools, equipment).

**S&M Headcount by ARR Stage (benchmarks):**
| ARR | AEs | SDRs | CSMs | Managers |
|---|---|---|---|---|
| $0-1M | Founder(s) | — | — | — |
| $1-3M | 1-3 | 2-4 | 1 | — |
| $3-10M | 5-10 | 5-10 | 3-5 | SDR Mgr, VP Sales |
| $10-20M | 10-20 | 10-15 | 5-10 | Full management layer |

### Phase 3: Operating P&L

```
MONTHLY P&L STRUCTURE:

REVENUE: New MRR + Expansion MRR - Churned MRR = Net New MRR
COST OF REVENUE (20-30%): Hosting, APIs, support team
GROSS PROFIT / Gross Margin %
OPERATING EXPENSES:
  S&M: Headcount + tools + ad spend + events
  R&D: Headcount + tools + infra
  G&A: Headcount + rent + legal + SaaS tools
NET OPERATING INCOME (Loss)
```

### Phase 4: Cash Flow & Runway

```
Starting Cash: $X
+ Inflows: customer cash (monthly/annual) + expansion
- Outflows: payroll (60-70%), infra, tools, marketing, rent, legal
= Net Cash Burn
Runway (months) = Cash ÷ |Monthly Net Cash Burn|
```

**Runway rules:** 18+ months post-raise. Start fundraising at 9-12 months left.
Cash-zero date is NOT when you start fundraising — it's when you're dead.

### Phase 5: Scenario Planning

Load `references/gtm-budget-playbook.md` for annual S&M/R&D/G&A structure,
headcount-driven build, vendor budget tie to `gtm-spend-management`, and monthly
variance cadence. Worksheet → `skills/gtm-ops/gtm-spend-management/templates/annual-gtm-budget-worksheet.md`.

| Driver | Conservative | Base Case | Aggressive |
|---|---|---|---|
| Monthly churn | 3% | 2% | 1% |
| Demo conversion | 15% | 25% | 35% |
| ACV | $10K | $15K | $20K |
| AE ramp (months) | 6 | 4 | 3 |
| Hiring speed | 45 days | 30 days | 21 days |

Conservative should feel uncomfortable. It's a stress test, not a wish.

## Consumption-Based Pricing Models

**What they are:** Customers pay based on usage, not seats. Examples: AWS
(per compute hour), Twilio (per SMS/API call), Snowflake (per credit),
Stripe (per transaction). Consumption models align price with value.

**Modeling consumption revenue:**

```
CONSUMPTION REVENUE MODEL

Base Metric: [API calls / compute hours / events / contacts]
Usage Tiers:
- Light (0-1K units): X% of customers, avg Y units/mo, $Z/unit
- Medium (1K-10K): X% of customers, avg Y/mo, $Z/unit
- Heavy (10K-100K): X% of customers, avg Y/mo, $Z/unit
- Enterprise (100K+): X% of customers, avg Y/mo, $Z/unit

Monthly Revenue = Σ (customers in tier × avg usage × unit price)
```

**Key consumption metrics:**
- **NRR:** Best-in-class consumption companies hit 130%+ NRR (usage compounds)
- **Usage Growth Rate:** 5-10% MoM per existing customer = healthy
- **Dormancy Rate:** % of customers with zero usage in a month. <5% healthy.
- **Commitment Coverage:** % of committed spend consumed. <80% at renewal = risk.

**Consumption model pitfalls:**
- Revenue unpredictability → Fix: Annual commitments with true-up
- Pricing complexity → Fix: Usage dashboards, spend alerts, never-exceed caps
- Volume discounting → Fix: Tiered pricing from day 1, no custom discounts

**Hybrid models (best of both):**
- Platform fee (predictable) + consumption (growth-aligned)
- Seat minimum + usage above threshold
- "Starter includes X units, then $Y/unit above"

## Expansion Revenue Modeling

**The 5 expansion levers:**

| Lever | Model As | Contribution to NRR |
|---|---|---|
| Seat expansion | New seats × ACV | 3-8% of starting ARR |
| Usage growth | Consumption increase × unit price | 5-15% of starting ARR |
| Tier upgrade | (New price - Old) × Upgrading | 2-5% of starting ARR |
| Cross-sell | New product ACV × Attach rate | 2-10% of starting ARR |
| Price increases | Increase % × Retained customers | 3-5% of starting ARR |

**Expansion formula:**
```
Expansion ARR = (Starting ARR × Seat Exp %) +
                (Starting Usage × Usage Growth % × Unit Price) +
                (Upgrading × Tier Delta) +
                (Eligible × Cross-Sell Attach % × Cross-Sell ACV) +
                (Retained × Price Increase %)
```

## DCF Valuation for SaaS Companies

**When to use DCF:** Fundraising, 409A valuations, acquisition offers, or
understanding what your company is actually worth. DCF is the gold standard.

**The DCF formula:**
```
Enterprise Value = Σ (FCF_t ÷ (1 + WACC)^t) + Terminal Value

Where:
- FCF = EBIT × (1 - Tax Rate) + D&A - Capex - Δ Working Capital
- WACC = 12-25% for startups (higher = riskier stage)
- t = year 1 through 5
- Terminal Value = FCF_Year5 × (1 + g) ÷ (WACC - g)
  (g = perpetual growth rate, 2-4%)
```

### DCF Step-by-Step

**Step 1: Project Revenue (5 years)**
```
Year 1: Starting ARR × (1 + growth rate)
Year 2: Year 1 × (1 + decaying growth rate)
...decay toward terminal growth rate (3-5%)
```

**Growth rate decay (benchmarks):**
| Year | Early Stage | Growth Stage | Mature |
|---|---|---|---|
| 1 | 150-300% | 60-100% | 30-50% |
| 2 | 80-150% | 40-80% | 25-40% |
| 3 | 50-80% | 30-50% | 20-30% |
| 4 | 30-50% | 20-35% | 15-25% |
| 5 | 20-35% | 15-25% | 10-20% |

**Step 2: Project Margins**
```
Gross Margin: 65-75% early → 75-85% mature
S&M as % of Revenue: 80-120% early → 20-30% mature
R&D: 40-60% early → 15-25% mature
G&A: 15-25% early → 8-12% mature
EBITDA Margin: -50% early → 15-30% mature
```

**Step 3: Calculate Free Cash Flow**
```
Revenue - COGS = Gross Profit
- S&M - R&D - G&A = EBITDA
- D&A (2-5% of revenue) = EBIT
- Taxes (21% federal + state, startup NOLs typically offset)
= NOPAT
+ D&A - Capex (3-5% revenue) - Δ Working Capital (5-10% revenue change)
= Unlevered Free Cash Flow
```

**Step 4: Calculate WACC**
```
Cost of Equity = Risk-Free Rate (~4%) + (Beta × ERP) + Startup Premium
- Beta: 1.5-2.5 for SaaS
- ERP (Equity Risk Premium): 5-6%
- Startup Premium: 5-15% depending on stage

Early stage WACC: 20-30%
Growth stage WACC: 15-20%
Mature SaaS WACC: 10-15%
```

**Step 5: Terminal Value**
```
TV = FCF_Year5 × (1 + g) ÷ (WACC - g)
g = 2-4% (can't exceed GDP growth long-term)
```

**Step 6: Enterprise Value & Sensitivity**
```
EV = PV(Year 1-5 FCFs) + PV(Terminal Value)

SENSITIVITY TABLE (WACC × Terminal Growth):
| WACC →    | 12%   | 15%   | 18%   | 22%   | 25%   |
| g = 2%    | $X M  | $X M  | $X M  | $X M  | $X M  |
| g = 3%    | $X M  | $X M  | $X M  | $X M  | $X M  |
| g = 4%    | $X M  | $X M  | $X M  | $X M  | $X M  |
```

**DCF quick-check (reality test):**
- Early-stage SaaS: 10-20× forward ARR (growth rate dependent)
- Growth-stage: 8-15× forward ARR
- Mature: 5-10× forward ARR
If your DCF is outside these bands, check your assumptions.

For exit planning, connect unit economics → P&L → ARR and EBITDA multiples via
`references/unit-economics-exit-bridge.md`. Sensitivity template →
`exiting-company/templates/valuation-sensitivity-table.md`.

**Earn-out / deferred consideration:** Model **cash at close**, earn-out scenarios
(base / max), and 3-year hold — not headline EV alone. Worksheet →
`exiting-company/templates/earn-out-term-sheet-review.md`. Structure norms →
`references/benchmark-reconciliation.md`. **Typical not guaranteed** — CPA for tax timing.

### DCF Pitfalls for Startups

1. **Terminal value dominates.** 80-90% of startup DCF = terminal value (most
   speculative part). Fix: Conservative terminal growth (2-3%). Wide sensitivity.
2. **Growth rate optimism.** "100% growth for 5 years" = nonsense. Fix: Model
   realistic decay. Even the best decay toward market growth rates.
3. **WACC too low.** 10% WACC for seed stage = utility-level risk pricing.
   Fix: Early stage WACC = 20-30%.
4. **No sensitivity.** Single-point DCF = guess. Range = analysis. Fix: Always
   build sensitivity table.

## SaaS Cohort & Unit Economics Deep-Dive

### Cohort Analysis

**Why cohorts matter:** Aggregate churn of 2% hides that Q1 cohort churns at
5% and Q4 at 0.5%. One is a problem you can't see in aggregate.

**Cohort retention curve (power law):**
Retention(t) = a × t^(-b). Where a ≈ 100%, b = churn decay factor.

**Monthly cohort table:**
| Cohort | M0 MRR | M1 | M3 | M6 | M12 | Est LTV |
|---|---|---|---|---|---|---|
| Jan 2025 | $X | $X | $X | $X | $X | $X |
| Feb 2025 | $X | $X | $X | $X | — | $X (est) |

**Cohort CAC payback:** Aggregate "8 months" can hide Q2 cohort taking 14
months. Fix: Track CAC payback per cohort, not just aggregate.

### Unit Economics by Segment

| Segment | ACV | Churn | LTV | CAC | LTV:CAC | Payback |
|---|---|---|---|---|---|---|
| SMB (<$1K ACV) | $X | X% | $X | $X | Xx | X mo |
| Mid-Market ($1-10K) | $X | X% | $X | $X | Xx | X mo |
| Enterprise ($10K+) | $X | X% | $X | $X | Xx | X mo |

**Decision rule:** If LTV:CAC < 3x, stop acquiring in that segment until fixed.

### ARR Build vs. ARR Bridge

**ARR Build (forward-looking):**
Starting ARR + New ARR + Expansion - Churned - Contraction = Ending ARR

**ARR Bridge (backward analysis):**
Starting ARR + New Logo + Expansion - Logo Churn - Contraction - Downsell = Ending

The bridge tells WHERE growth came from. The build projects WHERE it will come from.

**Revenue lens:** Model **recognized revenue** in P&L; use **committed MRR bridge** for
board ARR/NRR. Reconcile gaps (prepay, PS, implementation delay) via
`references/saas-mrr-accounting-nuances.md` and `references/bookings-billings-revenue-matrix.md`.

## Accounting Stack for SaaS (Founder Timing)

| Stage | Stack | Hire trigger |
|---|---|---|
| Pre-$500K ARR | QuickBooks Online or Xero + Stripe/billing + bookkeeper (Pilot/Bench class) | Founder + part-time bookkeeper |
| $500K–$3M ARR | QBO/Xero + billing + fractional CFO | First finance hire = controller or strong fractional CFO |
| $3M–$15M ARR | Evaluate NetSuite; dedicated controller | VP Finance when board/investor reporting >20 hrs/mo founder |
| $15M+ / multi-entity | NetSuite or ERP | Full-time CFO |

**Chart of accounts (minimum):** Subscription revenue, PS revenue, COGS (hosting), S&M, R&D, G&A, deferred revenue.

**Tax / 409A / QSBS awareness (not advice):** `references/saas-tax-founder-awareness.md` · Carta 409A · CPA handoff triggers.

**Bootstrap path:** `solo-founder-gtm` · `saas-outcomes/templates/bootstrap-capital-plan.md`.

## Output Format

```
SAAS FINANCIAL MODEL — [Company]

Summary (Base Case — 36 months):
- Ending ARR: $X M
- Headcount: X
- Gross Margin: X%
- Magic Number: X
- LTV:CAC: Xx
- CAC Payback: X months
- NRR: X%
- Rule of 40: X%
- Runway: X months
- Break-Even: [month/year or N/A]

DCF Valuation:
- Enterprise Value (Base): $X M
- Sensitivity Range: $X M - $Y M
- Implied ARR Multiple: Xx

Consumption Model (if applicable):
- Unit: [metric], Unit Price: $X
- Usage Growth Rate: X% MoM
- Dormancy Rate: X%

Key Assumptions: [10-15 key drivers documented]
Funding Requirement: $X M at month Y, runway post-raise: X months
```

## Implementation Checklist

- [ ] Revenue modeled bottom-up (customers × ACV), not top-down (market %)
- [ ] Headcount has every role, start date, and fully-loaded cost (1.3x salary)
- [ ] Churn modeled monthly with compounding, not annual averaging
- [ ] AE ramp curve built (0% M1, 50% M3, 100% M6)
- [ ] Three scenarios: Conservative, Base, Aggressive (internally consistent)
- [ ] Cash flow includes ALL costs (insurance, legal, SaaS tools)
- [ ] LTV/CAC uses fully-loaded CAC (all S&M, not just ad spend)
- [ ] DCF uses appropriate WACC (20-30% early stage)
- [ ] Terminal growth capped at 3-4% (GDP growth ceiling)
- [ ] Sensitivity table built (WACC ±5%, growth ±10%, terminal g ±1%)
- [ ] Cohort analysis segmented (not just aggregate metrics)
- [ ] ARR bridge built alongside ARR build (where growth came from)

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Top-down revenue modeling.** "1% of $100B market" = fiction. Fix: Model
   customers × ACV with realistic acquisition.

2. **Zero churn assumption.** No SaaS has zero churn. Fix: 1-3% monthly churn
   minimum for SMB, 0.5-1% for mid-market.

3. **Instant AE productivity.** AEs don't close month 1. Fix: Ramp curve:
   0% M1, 50% M3, 100% M6.

4. **Terminal value dominates DCF.** 80-90% of startup value from terminal =
   speculative. Fix: Conservative terminal growth (2-3%). Wide sensitivity.

5. **WACC too low for startups.** 10% WACC for seed stage implies utility-level
   risk. Fix: Early stage WACC = 20-30%. Risk is real.

6. **Aggregate metrics hiding segment problems.** 2% churn average hides 5%
   SMB churn and 0.5% Enterprise. Fix: Segment everything.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator
- `references/gtm-budget-playbook.md` — **canonical** annual GTM budget (repo root)
- `skills/gtm-ops/gtm-spend-management/templates/annual-gtm-budget-worksheet.md` — budget worksheet (gtm-spend-management skill)
- `references/saas-mrr-accounting-nuances.md` — MRR/recognition reconcile (repo root)
- `references/saas-tax-founder-awareness.md` — tax/409A/QSBS handoffs (repo root)
- `references/bookings-billings-revenue-matrix.md` — cash vs committed ARR (repo root)
- `references/unit-economics-exit-bridge.md` — LTV/NRR/EBITDA → valuation multiple bridge
**Cross-skill (journey / exit):** `gtm-spend-management` (vendor budget) · `saas-metrics-calculator` (MRR bridge) · `saas-outcomes/references/journey-stage-gates.md`, `saas-outcomes/references/bootstrap-founder-playbook.md`, `saas-outcomes/templates/bootstrap-capital-plan.md`, `saas-outcomes/templates/journey-planning-worksheet.md`, `saas-outcomes/references/valuation-multiples.md`, `exiting-company/templates/valuation-sensitivity-table.md`, `exiting-company/templates/earn-out-term-sheet-review.md`, `exiting-company/references/negotiating-earn-out.md`, `exiting-company/references/buyer-readiness-checklist.md`, `saas-metrics-calculator/references/metric-definitions-exit-weight.md`, `references/benchmark-reconciliation.md`

## ⚠️ Disclaimer

This skill provides general informational guidance based on publicly available frameworks and operator experience. It is NOT legal advice, accounting advice, tax advice, financial advice, insurance advice, or professional services advice.

Consult qualified professionals for your specific situation — attorneys for legal/equity matters, CPAs for tax and accounting, licensed brokers for insurance, and certified security assessors for compliance. This skill does not create a professional-client relationship. Use it as a starting point for research and preparation.

## Related Skills

- `saas-metrics-calculator` — Complete SaaS metrics with stage benchmarks
- `fundraising-strategy` — Fundraising process, SAFEs, term sheets
- `board-meeting-prep` — Board deck, metrics presentation
- `pricing-strategy` — Tier design, monetization models
- `pricing-psychology` — Anchoring, decoy effect, willingness-to-pay
- `investor-updates` — Monthly investor communications
- `co-founder-dynamics` — Equity modeling, co-founder equity splits
- `yc-ecosystem` — YC funding context and valuation benchmarks

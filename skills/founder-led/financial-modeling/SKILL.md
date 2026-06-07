---
name: financial-modeling
description: >-
  SaaS financial modeling for founders. Use when building operating model,
  projecting runway, modeling fundraising scenarios, planning headcount,
  calculating unit economics, or building board-ready financials. Covers
  P&L, cash flow, balance sheet, SaaS metrics integration, and scenario planning.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, GitHub Copilot, Gemini CLI
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: founder-led
  tags: [financial-model, saas-metrics, runway, unit-economics, forecasting, p-and-l, board]
  related_skills: [saas-metrics-calculator, fundraising-strategy, board-meeting-prep, pricing-strategy, investor-updates]
  frameworks:
    - "David Skok (Matrix Partners) — SaaS unit economics and CAC payback"
    - "Christoph Janz (Point Nine) — SaaS napkin and financial architecture"
    - "Ben Murray (The SaaS CFO) — SaaS financial operations"
    - "Jason Lemkin (SaaStr) — Growth efficiency benchmarks"
    - "Bessemer Venture Partners — Cloud 100 operating metrics"
---

# SaaS Financial Modeling

## Overview

Most founder financial models are fiction — aggressive growth curves with no
operational logic underneath. The mistake: building a top-down model ("we'll
capture 1% of a $100B market") instead of a bottom-up operating model ("we'll
hire 3 AEs at $120K OTE, each producing $800K quota in month 6"). This skill
covers building a real operating model that investors trust, boards respect,
and — most importantly — YOU can use to make decisions.

## When to Use

Trigger phrases: "financial model", "SaaS P&L", "runway calculation", "operating
model", "unit economics model", "headcount plan", "hiring model", "revenue
forecast", "build financial projections", "investor model"

## Authoritative Foundations

### David Skok — SaaS Unit Economics
The core equation every SaaS model must solve:
- **CAC** (Customer Acquisition Cost) = Total S&M spend / New customers
- **LTV** (Lifetime Value) = ARPU × Gross Margin % / Monthly Churn %
- **Rule:** LTV/CAC > 3x is investable. Below 3x, fix unit economics before scaling.
- **CAC Payback Period:** CAC / (ARPU × Gross Margin %). Under 12 months is good.

### The SaaS P&L Structure (Ben Murray)
Three layers:
1. **Revenue:** New ARR + Expansion ARR - Churned ARR = Net New ARR
2. **COGS:** Hosting, third-party APIs, support team (target 20-30% of revenue for early SaaS)
3. **OpEx:** S&M, R&D, G&A. Calculate per-head where possible.

### Growth Efficiency — Magic Number (Bessemer)
Magic Number = Net New ARR (quarter) / S&M Spend (prior quarter)
- >1.0: Efficient growth — invest more
- 0.5-1.0: Moderate efficiency — optimize before scaling
- <0.5: Inefficient — fix go-to-market before spending more

## Step-by-Step Process

### Phase 1: Revenue Model (Bottom-Up)

**Do NOT model "1% of market."** Model customers × average revenue.

```
Monthly Revenue Model:

New Customers = (SDR meetings × demo conversion rate) + inbound leads + expansion
Average ACV = $X (new logo) / $X (expansion)
Monthly Churn = Previous month customers × monthly churn rate
Net New MRR = (New customers × ACV) + Expansion - (Churned customers × ACV)
```

**Revenue inputs to get right:**
- SDR productivity: 8-12 meetings/month per SDR
- Demo conversion: 20-30% for qualified meetings (industry average)
- Sales cycle: 30-90 days depending on ACV
- Ramp time: 3-6 months for AEs to hit full quota
- Monthly churn: 1-3% for SMB, 0.5-1% for mid-market, under 0.5% for enterprise

### Phase 2: Headcount Model

Model every hire with: role, salary, start month, ramp months, fully-loaded cost.

```
S&M Headcount by ARR Stage (benchmarks):

$0-1M:  Founder(s) do everything
$1-3M:  1-3 AEs, 2-4 SDRs, 1 CSM
$3-10M:  5-10 AEs, 5-10 SDRs, 3-5 CSMs, 1 SDR Manager, 1 VP Sales
$10-20M: 10-20 AEs, 10-15 SDRs, 5-10 CSMs, SDR Mgr, Sales Mgr, VP Sales, 1-2 SEs
```

**Fully-loaded cost = base salary × 1.25-1.35** (benefits, payroll tax, tools,
equipment). Use 1.3x as default multiplier.

### Phase 3: Operating P&L

```
MONTHLY P&L STRUCTURE:

REVENUE
  New MRR
  Expansion MRR
  Churned MRR (-)
  Net New MRR
  Total MRR

COST OF REVENUE (20-30%)
  Hosting/infrastructure
  Third-party APIs/tools
  Support team (prorated)

GROSS PROFIT
  Gross Margin % = Gross Profit / Revenue

OPERATING EXPENSES
  Sales & Marketing
    Headcount (SDRs, AEs, CSMs, managers, VP Sales)
    Tools (CRM, outreach, enrichment, analytics)
    Advertising spend
    Events/conferences
  Research & Development
    Headcount (engineers, designers, product)
    Tools/infrastructure
  General & Administrative
    Headcount (CEO, finance, legal, HR, ops)
    Rent, legal, insurance, SaaS tools

TOTAL OPEX

NET OPERATING INCOME (Loss)
  NOI Margin % = NOI / Revenue
```

### Phase 4: Cash Flow & Runway

```
CASH FLOW MODEL:

Starting Cash: $X

INFLOWS:
  New customer cash (monthly or annual)
  Expansion cash

OUTFLOWS:
  Payroll (largest line item — usually 60-70%)
  Infrastructure
  Tools/software
  Marketing spend
  Rent/office
  Legal/accounting
  Other

Net Cash Burn = Inflows - Outflows (negative = burning)

Runway (months) = Cash / |Monthly Net Cash Burn|
```

**Runway rules:**
- Always have 18+ months of runway after a raise
- Start fundraising when you have 9-12 months left (process takes 3-6 months)
- Cash-zero date is NOT when you start fundraising — it's when you're dead

### Phase 5: Scenario Planning

Build 3 scenarios with different assumptions:

| Driver | Conservative | Base Case | Aggressive |
|---|---|---|---|
| Monthly churn | 3% | 2% | 1% |
| Demo conversion | 15% | 25% | 35% |
| ACV | $10K | $15K | $20K |
| AE ramp (months) | 6 | 4 | 3 |
| Hiring speed | 45 days/hire | 30 days/hire | 21 days/hire |

**Each scenario must be internally consistent.** You can't have aggressive
revenue with conservative hiring and low costs. If you're growing 2x YoY,
your OpEx must support that growth.

### Phase 6: Board-Ready Output

Every model must produce these 5 outputs:

1. **Monthly P&L** — 36-month projection, monthly granularity
2. **Headcount plan** — every role, start date, cost
3. **Cash flow / Runway** — monthly burn, zero-cash date, funding milestones
4. **SaaS metrics dashboard** — ARR, NRR, LTV/CAC, CAC Payback, Magic Number, Gross Margin, Rule of 40
5. **Scenario comparison** — Conservative vs Base vs Aggressive on key outputs

## Output Format

```
SAAS FINANCIAL MODEL

Summary (Base Case — 36 months):
- Ending ARR: $X M
- Ending Headcount: X
- Gross Margin: X%
- Magic Number: X
- LTV/CAC: X
- CAC Payback: X months
- NRR: X%
- Rule of 40: X% (Growth % + Profit %)
- Runway: X months (without additional capital)
- Cumulative Cash Burn: $X M
- Break-Even Month: [month/year or "not in forecast period"]

Key Assumptions:
[Table of 10-15 key drivers with values]

Funding Requirement:
- Raise: $X M at month Y
- Expected runway post-raise: X months
```

## Quality Checklist

- [ ] Revenue is modeled bottom-up (customers × ACV), not top-down (market %)
- [ ] Headcount model has every role, start date, and fully-loaded cost
- [ ] Churn is modeled monthly, not annually averaged
- [ ] AE ramp time is realistic (3-6 months, not 0)
- [ ] Hiring lags are modeled (30-45 days from req to start)
- [ ] Three scenarios built: Conservative, Base, Aggressive
- [ ] Cash flow includes ALL costs (don't forget insurance, legal, SaaS tools)
- [ ] Scenarios are internally consistent (fast growth = high spend)
- [ ] LTV/CAC uses fully-loaded CAC (all S&M, not just ad spend)
- [ ] Runway calculation uses net burn, not P&L loss

## Common Pitfalls

1. **Top-down revenue modeling.** "We'll capture 1% of a $100B market" is
   fiction. You capture customers, not market share. Fix: Model customers ×
   ACV with realistic acquisition assumptions.

2. **Zero churn assumption.** No SaaS has zero churn. Even best-in-class loses
   3-5% annually. Fix: Model 1-3% monthly churn minimum for SMB, 0.5-1% for
   mid-market.

3. **Instant AE productivity.** AEs don't close deals month 1. Typical ramp:
   0% quota month 1, 50% month 3, 100% month 6. Fix: Build a ramp curve.

4. **Ignoring fully-loaded costs.** Salary × 1.0 is wrong. Benefits, payroll
   tax, equipment, tools add 25-35%. Fix: Use 1.3x multiplier on all salaries.

5. **Modeling annual averages for monthly businesses.** Churn compounds
   monthly, revenue is collected monthly, cash burns monthly. Annual models
   hide cash crunches. Fix: 36-month model with monthly granularity.

6. **Optimism bias in all scenarios.** If even your "conservative" case shows
   hockey-stick growth and 18-month break-even, you're not being conservative.
   Fix: Conservative case should feel uncomfortable. It's a stress test.

## Related Skills

- `saas-metrics-calculator` — Complete SaaS metrics with stage benchmarks
- `fundraising-strategy` — When and how to raise capital
- `board-meeting-prep` — Board deck structure, metrics presentation
- `pricing-strategy` — Tier design, monetization models
- `investor-updates` — Monthly investor communications

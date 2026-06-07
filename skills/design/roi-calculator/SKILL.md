---
name: roi-calculator
description: >-
  Build ROI calculators and business cases — 3-scenario projections (conservative,
  moderate, aggressive), payback period analysis, TCO comparison, assumption
  documentation, MEDDICC integration, value driver identification. Use when
  building ROI models, creating business cases, quantifying value for prospects,
  or supporting economic buyer conversations. Triggers on: "ROI calculator",
  "business case", "ROI model", "value calculator", "TCO comparison", "payback
  period", "build the business case".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "2.0.0"
  author: LeadMagic
  category: design
  tags: [roi, calculator, business-case, financial, value-selling, meddic]
  related_skills: [deal-desk, pricing-strategy, saas-metrics-calculator, sales-enablement, demo-scripts]
  frameworks:
    - "Madhavan Ramanujam — Monetizing Innovation (WTP research)"
    - "ValueSelling Framework — Value pyramid and quantified value"
    - "David Skok — SaaS Unit Economics"
    - "MEDDICC — Economic Buyer + Metrics (quantified value)"
    - "Gartner — TCO and ROI methodology"
---

# ROI Calculator

## Overview

An ROI calculator turns "this seems valuable" into "this pays for itself in
4.3 months with a 3-year ROI of 340%." It is the single most powerful document
in enterprise sales because it translates product capabilities into financial
outcomes that economic buyers can approve. The mistake: building a calculator
that overclaims and destroys credibility. The fix: conservative assumptions
with documented sources, so every number is defensible under scrutiny.

## When to Use

Trigger phrases: "build an ROI calculator", "create a business case", "calculate
the ROI for [prospect]", "quantify our value", "build a TCO comparison",
"payback period calculation", "3-year ROI projection", "value calculator",
"economic buyer justification", "MEDDICC metrics slide"

## 5 Types of ROI Calculators

| Type | Use When | Best For | Example |
|---|---|---|---|
| **Time Savings** | Your product eliminates manual work | Productivity tools, automation | "Eliminates 15 hours/week of manual data entry" |
| **Revenue Increase** | Your product generates more revenue | Sales tools, marketing platforms | "Increases reply rates from 3% to 12% = 4x pipeline" |
| **Cost Reduction** | Your product replaces existing spend | Infrastructure, tool consolidation | "Replaces 3 tools at $500/mo each with 1 at $800/mo" |
| **Risk Mitigation** | Your product prevents losses | Security, compliance, data | "Prevents average data breach cost of $4.45M" |
| **Hybrid (TCO)** | Your product impacts multiple areas | Enterprise platforms | Total cost of ownership: current vs proposed state |

## Step-by-Step Process

### Phase 1: Identify Value Drivers

**Map product capabilities to financial outcomes:**

| Capability | Value Driver | Metric | Data Source |
|---|---|---|---|
| Automated email finding | Reduced research time | Hours saved/week × hourly rate | Customer interviews |
| Email validation | Reduced bounce rate | Bounces prevented × cost per bounce | Deliverability data |
| CRM enrichment | Improved lead routing | Faster MQL→SQL × pipeline increase | Internal analytics |

**For each value driver, answer:**
1. What changes? (current state → future state)
2. How much changes? (specific number)
3. What's that worth? (× unit cost or value)
4. What's the source? (customer data, industry research, internal measurement)

### Phase 2: Build Scenario Models

**3 scenarios — every calculator needs all three:**

**Conservative (what 80%+ of customers achieve):**
- Use the LOW end of customer-reported ranges
- Exclude value drivers that are "nice to have" rather than proven
- This is the safe number — every customer should beat it

**Moderate (what typical customers achieve):**
- Use the MEDIAN of customer-reported ranges
- Include most value drivers with measured impact
- This is the expected outcome for most deployments

**Aggressive (what best customers achieve):**
- Use the HIGH end of customer-reported ranges
- Include all value drivers
- Requires full adoption and process change
- Frame as "potential" not "promised"

### Phase 3: Build the Calculator

**Structure for each scenario:**

```
SECTION 1: CURRENT STATE COSTS
  Current Tool Spend:        $X/year
  Current Labor Cost:         Hours × Rate × Occurrences = $X/year
  Current Error/Loss Cost:    Incidents × Cost per Incident = $X/year
  Current Opportunity Cost:   Missed Revenue = $X/year
TOTAL CURRENT COST:           $X/year

SECTION 2: PROPOSED SOLUTION COSTS
  Your Product Cost:          $X/year
  Implementation Cost:        $X (one-time)
  Training Cost:              $X (one-time)
  Ongoing Management:         Hours × Rate = $X/year
TOTAL SOLUTION COST:          $X/year (Year 1 includes one-time costs)

SECTION 3: PROJECTED BENEFITS
  Tool Savings:               $X/year (replaced tools)
  Labor Savings:              $X/year (time eliminated)
  Error Reduction:            $X/year (prevented losses)
  Revenue Increase:           $X/year (net new revenue)
TOTAL BENEFITS:               $X/year

SECTION 4: ROI CALCULATION
  Net Benefit (Year 1):       Benefits - Solution Cost = $X
  Payback Period:             One-Time Costs ÷ Monthly Net Benefit = X.X months
  1-Year ROI:                 (Net Benefit ÷ Solution Cost) × 100 = X%
  3-Year ROI:                 (3 × Annual Net Benefit ÷ 3-Year Solution Cost) × 100 = X%
  3-Year Net Present Value:   Sum of discounted cash flows = $X
```

### Phase 4: Assumption Documentation

**Every input must have a source, ranked by credibility:**

1. **Gold:** Your customer data (anonymized, aggregated)
   "Based on data from 50+ customers across 12 months"
2. **Silver:** Third-party research (named source, publicly available)
   "According to Gartner's 2026 Cost of Data Quality Report"
3. **Bronze:** Industry benchmarks (credible institution)
   "SDR average fully-loaded cost: $80K/year (Bridge Group 2026)"
4. **Copper:** Prospect-provided data (they validate it)
   "Per your team's estimate of 15 hours/week on manual research"

Never use "our estimate" or "industry average" without a specific source.

### Phase 5: MEDDICC Integration

The ROI calculator supports MEDDICC:
- **Metrics:** The calculator IS the metrics — quantified value for the economic buyer
- **Economic Buyer:** Send the calculator BEFORE meeting the EB. "Here's the
  quantified impact. I'd like 15 minutes to walk through the assumptions."
- **Champion:** Give the champion the calculator to socialize internally.
  "Share this with your CFO — the numbers are based on your actual team data."

### Phase 6: Deliverables

**Per-prospect, produce:**
1. **1-page executive summary** — key numbers, 3-scenario comparison, payback period
2. **Detailed calculator** — all inputs, formulas, assumptions, sources
3. **Slide version** — for the champion to put in their internal deck
4. **Live calculator** — web-based version they can adjust assumptions themselves

## Output Format

```
ROI BUSINESS CASE — [Prospect Name]

Prepared for: [Champion Name], [Title]
Date: [date]

EXECUTIVE SUMMARY
| Metric | Conservative | Moderate | Aggressive |
|---|---|---|---|
| Annual Benefit | $X | $X | $X |
| Annual Solution Cost | $X | $X | $X |
| Net Benefit (Y1) | $X | $X | $X |
| Payback Period | X.X mo | X.X mo | X.X mo |
| 3-Year ROI | X% | X% | X% |

VALUE DRIVER BREAKDOWN:
1. [Driver 1]: $X/yr — Source: [specific source]
2. [Driver 2]: $X/yr — Source: [specific source]
...

KEY ASSUMPTIONS:
- [Assumption 1]: [value] — Source: [gold/silver/bronze/copper]
- [Assumption 2]: [value] — Source: ...

NEXT STEP:
"Walk through assumptions with [Economic Buyer Name] to validate and refine."
```

## Quality Checklist

- [ ] 3 scenarios built (conservative, moderate, aggressive) with different assumptions
- [ ] Every assumption has a documented source (no "our estimate")
- [ ] Conservative scenario uses LOW end of customer-reported ranges
- [ ] Payback period calculated (months, not years — more precise)
- [ ] One-time costs separated from ongoing costs
- [ ] 1-year AND 3-year ROI calculated (3-year is the EB metric)
- [ ] Calculator can be shared as a slide (champion needs this)
- [ ] MEDDICC integration: calculator supports Metrics + Economic Buyer
- [ ] Numbers are defensible under CFO scrutiny

## Common Pitfalls

1. **Aggressive as default.** Showing only the aggressive scenario trains
   prospects to be skeptical. Fix: Lead with conservative. "Here's what
   we can confidently promise. Most customers achieve more."

2. **Unrealistic assumptions.** "You'll save 40 hours/week" when your best
   customer saves 10. CFOs spot this instantly and trust is destroyed. Fix:
   Use actual customer data, not aspirational numbers.

3. **Black-box calculator.** "Trust us, the math works" is not a business case.
   Prospects need to see and validate every assumption. Fix: Document every
   input with its source. Make the calculator transparent.

4. **One-size output.** A CFO cares about 3-year NPV. A VP Sales cares about
   pipeline increase. A CTO cares about implementation time. Fix: Create
   persona-specific summary tabs or views.

5. **No source on assumptions.** "Industry average" without naming the source
   is no better than "we guessed." Fix: Name the source: "Gartner 2026 Report,"
   "Internal customer data (50+ deployments)," "Bureau of Labor Statistics."

6. **Ignoring implementation cost.** "The software is $50K/year, therefore ROI
   is [benefits ÷ $50K]." Wrong. Implementation, training, migration, and
   opportunity cost of the transition period are real costs. Fix: Include all
   costs in Year 1. Model 3 years to amortize one-time costs.

## Related Skills

- `deal-desk` — Deal structuring using ROI outputs to justify price
- `pricing-strategy` — Pricing informed by willingness-to-pay and quantified value
- `saas-metrics-calculator` — SaaS-specific CAC, LTV, payback metrics
- `sales-enablement` — Pitch decks that use ROI data
- `demo-scripts` — Demo architecture that demonstrates value drivers

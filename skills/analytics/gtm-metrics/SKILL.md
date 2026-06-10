---
name: gtm-metrics
description: >-
  Build a GTM metrics system for SaaS: funnel conversion, pipeline velocity, win rates, CAC, payback, NRR, sales efficiency, growth accounting, and executive dashboards. Use when creating metrics dashboards, board reports, revenue reviews, operating cadence, or diagnosing growth constraints.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.4.0"
  author: LeadMagic
  category: analytics
  tags: [saas-metrics, cac, ltv, nrr, magic-number, rule-of-40, pipeline, gtm-index, benchmarks]
  related_skills: [campaign-analytics, attribution, saas-metrics-calculator, pipeline-management, saas-outcomes, financial-modeling]
  frameworks: [Winning by Design GTM Index, David Skok SaaS Metrics, Meritech Capital Public SaaS Benchmarks, Force Management Pod Economics, ChartMogul Benchmarks, OpenView Benchmarks, Henry Schuck (ZoomInfo) Public-Company GTM Metrics, John McMahon (CRO Board Reporting — 5-quarter model, productivity per rep), Frank Slootman (Snowflake Consumption Metrics), Dharmesh Shah (HubSpot) Flywheel NRR, Aneesh Lal (Wishly Group) B2B Influencer Attribution, Chris Walker (Refine Labs) Dark Social]
---
# GTM Metrics

## Overview

GTM Metrics establishes the canonical measurement framework for evaluating go-to-market health. The core principle: most SaaS companies measure the wrong things or measure the right things incorrectly. They track MRR without segmenting by cohort, calculate CAC without fully loading costs, and report NRR without distinguishing expansion from contraction. This skill prevents the existential mistake of running a GTM organization on bad math.

The non-obvious rule: every SaaS metric is stage-dependent. A 3-month CAC payback is spectacular at the enterprise level and mediocre in SMB. A 90% NRR is catastrophic for enterprise SaaS and acceptable for SMB. Benchmarks are meaningless without stage context. This skill applies stage-aware benchmarking to every metric.

This skill produces a complete GTM Metrics Dashboard including: the 6-metric core stack with stage-aware benchmarks, a Winning by Design GTM Index assessment scoring the organization 1-10 across 6 models, pipeline velocity analysis with bottleneck identification, cohort trend charts, and a board-ready executive summary with red/yellow/green status indicators.

## When to Use

- User says "GTM metrics" or "SaaS metrics dashboard" → activate this skill
- User asks "how efficient is our GTM" or "GTM efficiency" → use this skill
- User mentions "board metrics," "board deck," or "investor reporting" → activate for metric preparation
- User says "pipeline velocity," "CAC payback," "Magic Number," or "Rule of 40" → specific metric analysis
- User asks "how do we compare" or "benchmarks for our stage" → apply stage-aware benchmarks
- User mentions "Winning by Design" or "GTM Index" → score the organization
- Trigger phrases: SaaS metrics, pipeline metrics, NRR, LTV:CAC, unit economics, GTM efficiency, revenue efficiency, growth efficiency

Do NOT use for:
- Campaign-specific analytics (open rates, reply rates, meeting rates) → use campaign-analytics
- Pipeline management and hygiene (CRM data quality, stage definitions) → use pipeline-management
- Detailed calculator with interactive inputs → use saas-metrics-calculator
- Multi-touch marketing attribution → use attribution
- Deal-specific pricing and proposals → use deal-desk

## Authoritative Foundations

This skill draws from the following established methodologies:

- **Winning by Design — GTM Index** — 1-10 scoring across 6 models: Revenue Model (how you monetize), Data Model (how you measure), Math Model (unit economics), Operating Model (how you execute), Growth Model (how you acquire), GTM Model (how you go to market). Developed by Dominique Levin and Jacco van der Kooij. The GTM Index is how venture investors assess GTM maturity.

- **Winning by Design — Bowtie Model** — Revenue visualization extending the traditional funnel through retention and expansion. The bowtie measures acquisition, retention, and expansion as a continuous revenue system. Pipeline velocity sits at the neck of the bowtie.

- **David Skok (Matrix Partners) — SaaS Metrics** — Pipeline velocity formula (qualified opportunities × deal size × win rate ÷ sales cycle), CAC payback period as the defining GTM efficiency metric, and the importance of tracking cohort performance over time. Skok's work established the SaaS metrics canon.

- **ChartMogul / Baremetrics / OpenView — SaaS Benchmarks** — Industry-standard benchmarks segmented by ARR range, ACV, and go-to-market motion (product-led vs sales-led). These benchmarks are sourced from ChartMogul's open benchmark dataset (2,000+ SaaS companies), Baremetrics open benchmarks, and OpenView's annual SaaS benchmarks report.

- **SaaS Capital — Annual Survey** — The largest independent survey of private SaaS company metrics. Provides benchmarks for growth rate, churn, CAC payback, and Rule of 40 segmented by company size and growth stage.

- **Meritech Capital — Public SaaS Benchmarks** — ~120 public SaaS companies; implied ARR, Meritech Rule of 40 (growth 3× weighted), public NRR medians, EV/ARR multiples. Use for IPO-track board narratives. Load `references/meritech-saas-benchmarks.md`. Threshold conflicts → `references/benchmark-reconciliation.md`.

- **Dharmesh Shah (HubSpot) — Flywheel metrics** — NRR, advocacy, and referral velocity as flywheel fuel (Delight stage). Inbound pairs with measurable visitor ID; contrast Chris Walker dark social. `references/dharmesh-shah-hubspot-inbound.md`.

- **Force Management — Pod Economics** — Link company-level CAC payback and Magic Number to pod-level cost % of ARR, quota attainment distribution, and rep productivity curves by tenure. Use `references/force-management-playbook.md` when headcount planning informs the metrics dashboard.

- **Henry Schuck (ZoomInfo) — Public-Company GTM Metrics** — Earnings-season discipline: revenue/ARR bridge, adjusted operating margin, NRR/GRR by segment, seat vs consumption mix, S&M efficiency, and GTM operating metrics (speed-to-lead, SQL acceptance, demo yield) reported between quarters. Load `references/public-company-gtm-metrics.md` for board prep checklists and investor slide order.

- **John McMahon — CRO board reporting** — 5-quarter model; **productivity per rep**; **new logos vs expansion** mix; three-view forecast (commit/likely/upside) with MEDDICC proof. RevOps equips CRO for board — headcount, productivity, churn as scaling levers. Canonical → `gtm-leadership/references/cro-enterprise-strategy.md`.

- **Snowflake / Slootman — Consumption metrics** — Revenue recognized on usage, not bookings; track consumption run-rate, capacity reorder, downsell risk when bookings overshoot usage. Pair with Meritech public benchmarks for $100M+ ARR companies.

- **Aneesh Lal (Wishly Group) + Chris Walker — Influencer & dark social measurement** — B2B creator campaigns: per-creator landing pages, ICP engagement scrape, CRM 30-day lookback, self-reported influence on discovery calls. UTMs alone undercount LinkedIn influence. Load `references/b2b-influencer-measurement.md` + `references/chris-walker-mental-models.md`. 90-day program evaluation minimum.

## Prerequisites

- CRM data with at minimum 12 months of history: opportunities created, won, lost, deal amounts, close dates, and stage durations (HubSpot, Salesforce, or Attio)
- Financial data: fully-loaded sales and marketing spend (salaries, commissions, tools, events, ad spend, agency fees), COGS for gross margin calculation, total company revenue
- Customer contract data: starting MRR per customer, expansion MRR, contraction MRR, churned MRR, renewal dates
- Headcount data: SDR headcount, AE headcount, quota attainment, total revenue team size
- Recommended: 24+ months of historical data for reliable trend analysis and seasonality adjustment
- Optional: product usage data for consumption-based metrics and health scoring

## Step-by-Step Process

### Phase 1: Intake

Gather required information from the user. Ask all questions at once. Do not proceed until all answers are received.

Required intake questions:

1. **Company context**: Current ARR, growth rate, funding stage (seed, Series A, B, C+, bootstrapped), primary GTM motion (product-led, sales-led, hybrid), average ACV, target customer profile (SMB, mid-market, enterprise).

2. **Data access**: Can you provide CRM export (opportunities), financial data (S&M spend), billing data (MRR by customer), and headcount? What time period? (Minimum 12 months.)

3. **Metric purpose**: What decision is this analysis informing? (Board meeting, fundraising, operational planning, team restructuring, budget allocation?)

4. **Prior metrics**: Have you calculated these metrics before? If yes, what were the values and what methodology was used? This avoids restating conflicting numbers.

5. **Segmentation needs**: Do you need metrics segmented by: customer segment, geography, product line, acquisition channel, cohort (vintage)?

6. **Benchmark comparison**: Do you want comparison to industry benchmarks? If yes, confirm stage and segment for appropriate benchmark selection.

### Phase 2: Data Assembly and Validation

Assemble and validate all metric inputs:

1. **Revenue data validation**:
   - Reconcile CRM revenue with billing system revenue — they must match within 2%.
   - Classify revenue by type: new customer MRR, expansion MRR, contraction (downgrade) MRR, churned MRR.
   - Verify ARR calculation: MRR × 12 (do not include non-recurring revenue in ARR).

2. **S&M spend assembly**:
   - Fully-loaded cost basis: base salary + commission/bonus + benefits (30% load) + tools + training + travel for all revenue team members.
   - Classify spend: people cost, program spend (events, ads, content), tools/software, agency/vendor.
   - Allocate spend: direct acquisition cost vs brand/demand gen vs enablement.
   - Period alignment: match spend period to customer acquisition period (trailing 12 months recommended).

3. **Pipeline data standardization**:
   - Normalize CRM stage definitions across the dataset. Map all historical stages to a standard framework: Prospecting → Qualification → Discovery → Evaluation → Negotiation → Closed Won/Lost.
   - Calculate stage durations: entry date to exit date for every opportunity.
   - Flag anomalies: opportunities with negative duration (exit before entry), duration > 2x median (stalled), zero-value opportunities, duplicate records.

4. **Cohort construction**:
   - Monthly cohorts: group customers by month of first contract/invoice.
   - Track each cohort's MRR over time (month 0, month 1, month 2... month N).
   - Calculate cohort-level: retention rate, expansion rate, contraction rate, net retention.

### Phase 3: Core Metric Stack Calculation

Calculate the complete 6-metric core stack:

**Metric 1: Pipeline Velocity**

Pipeline velocity measures how quickly revenue moves through your pipeline.

```
Velocity = (Qualified Opportunities × Average Deal Size × Win Rate) ÷ Sales Cycle Length
```

Where:
- Qualified Opportunities: count of opportunities that entered the pipeline in the period
- Average Deal Size: mean ACV of closed-won deals in the period
- Win Rate: closed-won ÷ (closed-won + closed-lost) for the period
- Sales Cycle Length: median days from opportunity creation to close (won only)

Calculate for each quarter. Also calculate by segment and by acquisition channel.

**Diagnostic thresholds for velocity components**:
- Win rate < 15% → qualification or competitive positioning problem
- Sales cycle > 90 days for ACV < $25K → process inefficiency or poor qualification
- Win rate > 40% → may be sandbagging or too conservative in pipeline entry
- Opportunity count declining over 2+ quarters → top-of-funnel problem

**Metric 2: CAC (Fully-Loaded)**

```
CAC = Total S&M Spend (period) ÷ New Customers Acquired (period)
```

Critical rules:
- Use same time period for numerator and denominator.
- Only include new customer acquisition spend, not customer success/retention spend.
- Fully load all costs (salary + commission + benefits + tools).
- Use trailing 12-month or quarterly data (not monthly — too volatile).
- Calculate separately for each acquisition channel to identify efficiency differences.

**Metric 3: LTV (Contribution-Margin Based)**

```
LTV = (ARPA × Gross Margin %) ÷ Monthly Churn Rate
```

Critical rules:
- Use contribution-margin LTV, not raw-revenue LTV. Gross margin for SaaS is typically 70-85%.
- ARPA = Average Revenue Per Account. If you have multiple pricing tiers, calculate for the median customer.
- Monthly churn rate = customers lost in month ÷ customers at start of month.
- Alternative approach using customer lifetime: average customer lifetime in months × monthly ARPA × gross margin. Useful when churn rates are inconsistent.

**LTV:CAC Ratio**:

```
LTV:CAC = LTV ÷ CAC
```

Stage-aware benchmarks:
- Seed: 2-3:1 (you're still figuring out GTM)
- Series A: 3-4:1
- Series B: 4-5:1
- Scale/IPO-track: 5:1+
- Below 1:1: losing money on every customer. Existential threat.
- Above 10x: may be under-investing in growth (rare for VC-backed).

**CAC Payback Period**:

```
CAC Payback (months) = CAC ÷ (Monthly ARPA × Gross Margin %)
```

Stage-aware benchmarks:
- SMB (ACV <$10K): <12 months target
- Mid-market ($10-50K ACV): <18 months target
- Enterprise ($50K+ ACV): <24 months target
- Series A deal-breaker: 18+ months is red flag for investors

**Metric 4: Net Revenue Retention (NRR)**

```
NRR = (Starting MRR + Expansion - Contraction - Churned MRR) ÷ Starting MRR
```

Calculate for the most recent quarter (trailing 3 months) and for the trailing 12 months.

Stage-aware benchmarks:
- SMB: >100% is good (means expansion offsets churn)
- Mid-market: >110% is good
- Enterprise: >120% is good
- Below 100%: you're shrinking. Each quarter you lose more than you expand.
- Consistently >130%: excellent. Land-and-expand is working. Product has strong expansion hooks.

**NRR component analysis**:
- Expansion rate: expansion MRR ÷ starting MRR. What % of revenue base expanded? Target >15% for enterprise.
- Contraction rate: contraction MRR ÷ starting MRR. What % downgraded? Target <5%.
- Logo churn: customers lost ÷ starting customers. Separates revenue churn from customer churn. High revenue churn with low logo churn means big customers are leaving.

**Metric 5: Magic Number**

```
Magic Number = (Current Quarter ARR - Previous Quarter ARR) × 4 ÷ Previous Quarter S&M Spend
```

Measures how efficiently S&M spend produces new ARR.

Benchmarks:
- >1.0: Excellent. Every dollar of S&M produces >$1 of annualized new ARR.
- 0.75-1.0: Good. Efficient GTM spend.
- 0.5-0.75: Mediocre. Spend is producing returns but below efficiency threshold.
- <0.5: Concerning. S&M spend is inefficient. Time to investigate.
- Negative: Revenue declined quarter-over-quarter. Critical problem.

**When Magic Number is misleading**:
- The Magic Number compares current quarter ARR to previous quarter S&M spend. This assumes S&M spend in one quarter creates ARR in the next quarter. For enterprise sales with 6-12 month cycles, the correlation breaks. Use a 2-4 quarter lagged Magic Number for enterprise.
- Magic Number doesn't distinguish new vs expansion ARR. A high Magic Number driven entirely by expansion doesn't tell you about new customer acquisition efficiency.

**Metric 6: Rule of 40**

```
Rule of 40 = Revenue Growth Rate (%) + EBITDA Margin (%)
```

Use GAAP revenue growth rate (not ARR) and EBITDA margin (can use operating income if EBITDA unavailable).

Stage-adjusted targets:
- Early stage (<$5M ARR, high growth): >20% is acceptable (high growth offsets negative margins)
- Growth stage ($5-50M): >30% target
- Scale stage (>$50M): >40% target (the classic Rule of 40)

**When growth is negative or very high**:
- Growth rate >100% + negative 30% margin = Rule of 40 score of 70. Looks great on paper but unsustainable if growth can't continue. Add qualitative assessment.
- Negative growth + positive margin = <40 almost by definition. Company is in decline. Rule of 40 flags this but doesn't resolve it.

### Phase 4: Winning by Design GTM Index Scoring

Score the GTM organization 1-10 across the 6 WbD models:

**Model 1: Revenue Model (1-10)**
How do you monetize? Scoring criteria:
- 1-3: Revenue undefined. No clear pricing. Giving product away.
- 4-5: Simple pricing exists but not optimized. One-size-fits-all.
- 6-7: Tiered pricing with clear value metrics. Usage-based or seat-based aligned to value.
- 8-9: Pricing optimized by segment. Value-based pricing. Expansion built into pricing.
- 10: Revenue model is competitive advantage. Pricing drives land-and-expand. Customers self-select into higher tiers.

**Model 2: Data Model (1-10)**
How do you measure? Scoring criteria:
- 1-3: No CRM or spreadsheet only. No pipeline visibility. Metrics guessed.
- 4-5: CRM exists but data quality poor. Pipeline not trusted. Key metrics tracked manually.
- 6-7: CRM with clean data. Standard pipeline stages with exit criteria. Core metrics calculated monthly.
- 8-9: Full revenue operations stack. Cohort analysis. Attribution. Forecasting accuracy <10% error.
- 10: Data is company-wide operating system. Real-time dashboards. Predictive analytics. Data drives every GTM decision.

**Model 3: Math Model (1-10)**
Unit economics. Scoring criteria:
- 1-3: CAC/LTV unknown. No idea if acquiring customers is profitable.
- 4-5: CAC/LTV calculated but not fully loaded. Payback period unknown.
- 6-7: Fully-loaded CAC/LTV. Payback within target for stage. NRR tracked.
- 8-9: Unit economics excellent for stage. Payback <12 months. NRR >120%. Magic Number >0.75.
- 10: Best-in-class unit economics. Rule of 40 >40%. Efficient growth machine.

**Model 4: Operating Model (1-10)**
How do you execute? Scoring criteria:
- 1-3: No defined sales process. Founder does everything. No specialization.
- 4-5: Basic sales process exists. Some roles defined. Inconsistent execution.
- 6-7: Defined sales methodology (MEDDICC, Command of the Message). Role specialization (SDR/AE/CSM). Playbooks exist.
- 8-9: POD structure with optimal ratios. Process adherence measured. Coaching cadence established.
- 10: Operating model is scalable machine. Playbooks are living documents. New hires ramp in 90 days or less.

**Model 5: Growth Model (1-10)**
How do you acquire customers? Scoring criteria:
- 1-3: No repeatable acquisition. Relying on founder network. Word of mouth only.
- 4-5: One channel working inconsistently. No channel mix. No attribution.
- 6-7: Multiple channels producing. Outbound generating pipeline. Some inbound. Channel ROI tracked.
- 8-9: Diversified channel mix. Each channel has predictable output. Clear channel strategy and investment.
- 10: Growth flywheel spinning. Channels compound. CAC declining over time. Referral and partner channels scaling.

**Model 6: GTM Model (1-10)**
Overall GTM strategy coherence. Scoring criteria:
- 1-3: No GTM strategy. Reacting to whatever comes in. No ICP.
- 4-5: ICP defined but not operationally applied. Positioning unclear. Sales and marketing misaligned.
- 6-7: ICP operationalized. Positioning clear. Sales and marketing aligned on target and message.
- 8-9: Complete GTM system: ICP → positioning → messaging → channels → enablement → measurement all connected.
- 10: GTM model is competitive advantage. Category-creating or category-dominating. Competitors react to your moves.

**GTM Index Calculation**: Average of 6 model scores. Plot on a radar chart to visualize strengths and weaknesses.

| GTM Index | Stage Expectation | Interpretation |
|-----------|-------------------|----------------|
| 1-3 | Pre-Seed | Validating GTM, no repeatability |
| 4-5 | Seed | Some repeatability, early patterns |
| 6-7 | Series A | Scaling what works, gaps remain |
| 8-9 | Series B+ | Predictable, scalable GTM machine |
| 10 | IPO-Ready | World-class GTM organization |

### Phase 5: Cohort Trend Analysis

Build cohort views to separate signal from noise:

1. **Revenue cohort chart**: For each monthly cohort, plot MRR over the first 12-24 months. This reveals whether newer cohorts are performing better or worse than older cohorts at the same maturity.

2. **CAC payback by cohort**: How quickly does each cohort pay back CAC? Are newer cohorts paying back faster (efficiency improving) or slower (efficiency declining)?

3. **Logo retention by cohort**: What % of customers from each cohort are still active at month 12, 24, 36? Are retention rates improving or declining?

4. **NRR by cohort vintage**: Do older cohorts expand more (product stickiness increases with tenure) or contract (product loses relevance over time)?

5. **Channel cohort performance**: If cohorts can be tagged by primary acquisition channel, compare cohort performance by channel. This reveals which channels produce the best long-term customers, not just the cheapest acquisition.

### Phase 6: Dashboard Assembly and Benchmarking

Build the final dashboard with benchmarks:

1. **Core metric table**: Each of the 6 metrics with: current value, previous period value, quarter-over-quarter trend, stage-appropriate benchmark, benchmark comparison (above/below/at benchmark), and RAG status (green/yellow/red).

2. **GTM Index radar chart**: Visual representation of the 6 model scores. Identify the lowest-scoring models as priority improvement areas.

3. **Pipeline waterfall**: Starting pipeline → new opportunities → won → lost → ending pipeline. Shows pipeline generation and conversion health in one view.

4. **Executive summary** (board-ready):
   - 3-sentence GTM health assessment
   - Top 3 metrics performing above benchmark
   - Top 3 metrics requiring attention
   - Key cohort insight (single most important trend)
   - Recommended action for the next quarter

## Output Format

The agent should produce output in this structure:

```markdown
# GTM Metrics Dashboard
**Period:** [Q1 2024] | **Stage:** [Series A] | **Segment:** [Mid-Market]

## Executive Summary
[3-4 sentence assessment with key numbers highlighted]

## Core Metric Stack
| Metric | Current | Previous | QoQ Trend | Benchmark | vs Benchmark | Status |
|--------|---------|----------|-----------|-----------|-------------|--------|
| Pipeline Velocity | $X/mo | $Y/mo | ↑/↓/→ | - | - | 🟢🟡🔴 |
| CAC | $X | $Y | ↑/↓/→ | $Z | +/- X% | 🟢🟡🔴 |
| LTV:CAC | X:1 | Y:1 | ↑/↓/→ | Z:1 | +/- | 🟢🟡🔴 |
| CAC Payback | X mo | Y mo | ↑/↓/→ | Z mo | +/- X mo | 🟢🟡🔴 |
| NRR | X% | Y% | ↑/↓/→ | Z% | +/- X pp | 🟢🟡🔴 |
| Magic Number | X.X | Y.Y | ↑/↓/→ | 0.75 | +/- | 🟢🟡🔴 |
| Rule of 40 | X% | Y% | ↑/↓/→ | 30% | +/- X pp | 🟢🟡🔴 |

## GTM Index (Winning by Design)
| Model | Score (1-10) | Assessment |
|-------|-------------|------------|
| Revenue | X | [1 sentence] |
| Data | X | [1 sentence] |
| Math | X | [1 sentence] |
| Operating | X | [1 sentence] |
| Growth | X | [1 sentence] |
| GTM | X | [1 sentence] |
| **Overall** | **X.X** | **Stage: [expectation]** |

## Pipeline Waterfall
| Stage | Amount | Count | Conversion |
|-------|--------|-------|------------|
| Starting Pipeline | $X | N | - |
| + New Opportunities | $X | N | - |
| - Won | $X | N | X% |
| - Lost | $X | N | X% |
| = Ending Pipeline | $X | N | - |

## Cohort Highlights
[Key cohort insights with supporting data]

## Action Items
1. [Priority 1: what, why, expected impact]
2. [Priority 2: what, why, expected impact]
3. [Priority 3: what, why, expected impact]
```

## Quality Check

Before delivering, verify:

- [ ] Are all 6 core metrics calculated using the correct formulas (fully-loaded CAC, contribution-margin LTV)?
- [ ] Are benchmarks appropriate for the company's stage, ACV range, and GTM motion?
- [ ] Is the GTM Index scored with specific evidence for each model score, not just intuition?
- [ ] Are cohort trends included to separate real improvement from period-over-period noise?
- [ ] Does the executive summary read as board-ready (concise, data-backed, insight-driven)?
- [ ] Have data reconciliation checks been performed (CRM matches billing, spend is fully loaded)?
- [ ] Are anomalies flagged and explained (unusual spikes, data gaps, methodological changes)?
- [ ] Would a SaaS investor or board member find this dashboard comprehensive and credible?

## Common Pitfalls

1. **Calculating LTV without gross margin.** Raw-revenue LTV (ARPA ÷ churn) overstates value by 15-30% because it ignores COGS. Contribution-margin LTV is what matters. Investors will recalculate using gross margin — if your number doesn't match, you lose credibility.

2. **Using unloaded CAC.** Including only ad spend or tool costs in CAC while ignoring fully loaded salaries and benefits dramatically understates true acquisition cost. A "CAC" of $500 that should be $2,500 leads to terrible unit economics decisions. Include every dollar spent on acquiring customers.

3. **Mixing monthly and annual metrics.** CAC calculated from quarterly spend but divided by monthly new customers gives nonsensical results. Always align the time periods. Use quarterly or trailing 12-month CAC for stability.

4. **Comparing NRR across different segments.** SMB NRR benchmarks (100%+ good) and enterprise NRR benchmarks (120%+ good) are completely different scales. Comparing an SMB company's NRR to enterprise benchmarks creates false panic or false confidence.

5. **Interpreting Magic Number without considering sales cycle.** If your sales cycle is 6+ months, comparing current quarter ARR to previous quarter S&M spend understates efficiency. The spend from 2-3 quarters ago generated this quarter's ARR. Use lagged Magic Number for enterprise.

6. **Treating Rule of 40 as a precise metric.** Rule of 40 is a heuristic, not a law of physics. A company with 100% growth and -40% margin (score: 60) may be burning unsustainably. A company with 10% growth and 35% margin (score: 45) may be a better long-term business. Always pair Rule of 40 with qualitative assessment.

7. **Reporting metrics without cohort context.** "NRR improved from 95% to 105%" sounds great — unless the improvement is because you stopped acquiring new customers and only retained the best ones. Cohort analysis reveals whether metric improvements reflect genuine business improvement or composition effects.

8. **CRM bookings vs committed MRR.** Pipeline closed-won TCV ≠ board ARR. Prepay cash ≠ net new MRR. Fix: MRR bridge from billing; reconcile to CRM — `references/saas-mrr-accounting-nuances.md`, `references/benchmark-reconciliation.md`.

## Lifecycle Metrics Integration

Board and revenue metrics map to lifecycle stages via `references/lifecycle-metrics-by-stage.md`:
- **Acquisition:** CAC, MQL→SQL, Magic Number
- **Activation:** TTA, activation rate (pair with `references/activation-playbook.md`)
- **Revenue / Retention:** NRR, GRR, CAC payback, Rule of 40

Weekly/monthly ops cadence → `references/templates/lifecycle-monitoring-dashboard.md`.  
Stage rollup R/Y/G → `references/templates/stage-health-scorecard.md`.  
Canonical stage index → `references/gtm-lifecycle-stages.md`.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/b2b-influencer-measurement.md` — Influencer ROI, dark social, UTM limits (Wishly + Walker)
- `references/chris-walker-mental-models.md` — Dark social, demand creation frequency
- `references/public-company-gtm-metrics.md` — Henry Schuck / ZoomInfo earnings-season KPI stack
- `references/saas-mrr-accounting-nuances.md` — MRR variants, consumption, GAAP reconcile (repo root)
- `references/bookings-billings-revenue-matrix.md` — CRM vs finance ledger (repo root)
- `references/templates/mrr-bridge-template.md` — bridge worksheet (repo root)
- `../../management-leadership/gtm-leadership/references/cro-enterprise-strategy.md` — McMahon board metrics, Snowflake consumption KPIs (Pattern 31)
- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

**Canonical lifecycle (repo root):**
- `references/lifecycle-metrics-by-stage.md` — Per-stage formulas + R/Y/G
- `references/templates/lifecycle-monitoring-dashboard.md` — Weekly/monthly review
- `references/templates/stage-health-scorecard.md` — Leadership rollup
- `references/gtm-lifecycle-stages.md` — 7-stage index + Bowtie

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

**Cross-skill (exit/valuation):** `saas-metrics-calculator/references/metric-definitions-exit-weight.md`, `financial-modeling/references/unit-economics-exit-bridge.md`, `saas-outcomes/references/exit-metrics-matrix.md`

## Related Skills

- **saas-metrics-calculator**: Interactive calculator for scenario modeling. Use this skill for board-ready dashboards; use the calculator for what-if analysis.
- **campaign-analytics**: Campaign-level metrics feed into the Growth Model score of the GTM Index. Run after this skill to diagnose specific campaign underperformance.
- **attribution**: Channel-level attribution data improves CAC-by-channel calculations. Run alongside this skill for multi-channel GTM motions.
- **pipeline-management**: CRM data quality and stage definitions directly impact GTM metric accuracy. Run first if CRM data is unreliable.
- **investor-updates**: Use the dashboard output as the metrics section of monthly investor updates.
- **churn-prevention**: NRR decomposition identifies churn patterns. Feed churn data into prevention workflows.

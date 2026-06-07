---
name: saas-metrics-calculator
description: >-
  Calculate complete SaaS metrics — MRR, ARR, ARPA, Churn, LTV, CAC, LTV:CAC,
  CAC Payback, Magic Number, NRR, Rule of 40 — with stage-aware benchmarks.
  Uses ChartMogul, Baremetrics, OpenView, SaaS Capital benchmarks.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: founder-led
  tags: [saas, metrics, calculator, benchmarks, kpis]
  frameworks: [David Skok Unit Economics, ChartMogul/Baremetrics/OpenView Benchmarks 2025-2026]
---

# SaaS Metrics Calculator

## Overview
SaaS metrics answer whether your business model works. This skill calculates all key metrics from minimal inputs, applies stage-aware benchmarks, and flags metrics that need attention. Every formula is documented. Every benchmark is sourced.

## When to Use
- "Calculate my SaaS metrics"
- "What is my LTV:CAC ratio?"
- "How long is my CAC payback?"
- "What is my NRR?"
- "Run a complete metrics analysis"
- "What should my metrics be at this stage?"

## Step-by-Step Process
### Phase 1: Input Collection
Collect: MRR, paying customers, new customers acquired (month/quarter), total S&M spend (fully loaded), monthly churn rate (logo + revenue), expansion MRR, contraction MRR, gross margin %.

### Phase 2: Calculation
**MRR** = sum of all monthly subscriptions
**ARR** = MRR × 12 (or sum of annual contracts)
**ARPA** = MRR ÷ paying customers
**LTV (contribution-margin)** = (ARPA × Gross Margin %) ÷ Monthly Churn Rate
**CAC (fully-loaded)** = Total S&M Spend ÷ New Customers Acquired
**LTV:CAC** = LTV ÷ CAC
**CAC Payback (months)** = CAC ÷ (New MRR per Customer × Gross Margin %)
**NRR** = (Starting MRR + Expansion − Contraction − Churned MRR) ÷ Starting MRR
**Magic Number** = (Current Q ARR − Prior Q ARR) × 4 ÷ Prior Q S&M Spend
**Rule of 40** = Revenue Growth Rate % + Profit Margin %

### Phase 3: Benchmark Comparison
Compare against stage-aware benchmarks from ChartMogul, Baremetrics, and OpenView 2025-2026 data.

### Phase 4: Flag and Recommend
Red-flag metrics outside healthy ranges. Recommend which lever to pull first: reduce churn, improve pricing, optimize CAC, or increase expansion.

## Output Format
Complete metrics dashboard with all calculations, benchmark comparison, red/yellow/green flags, and prioritized recommendations.

## Stage-Aware Benchmarks
| Metric | Bootstrapped | SMB ($1-10M) | Mid-market ($10-100M) | Enterprise ($100M+) |
|---|---|---|---|---|
| LTV:CAC | 5-10x | 3-4x | 3-5x | 3x+ |
| CAC Payback | <12mo | <12mo | <18mo | <24mo |
| Monthly Churn | <3% | <3% | <2% | <1% |
| NRR | >100% | >100% | >110% | >120% |
| Gross Margin | >75% | >70% | >72% | >70% |
| Magic Number | >0.5 | >0.75 | >0.75 | >1.0 |

## Common Pitfalls
1. **Raw-revenue LTV** — use contribution-margin LTV only. Raw LTV overstates value by ignoring COGS.
2. **Under-counting CAC** — include fully-loaded salaries, tools, ad spend, events. Not just ad spend.
3. **Mixing time periods** — use same period for spend and new customers.
4. **Company-wide averages** — segment by channel and cohort. Averages hide problems.

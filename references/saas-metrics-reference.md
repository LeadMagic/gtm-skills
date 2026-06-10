# SaaS Metrics Reference

Shared reference for analytics, founder-led, and deal desk skills. **Formulas are canonical here.** **Benchmark thresholds** when sources conflict → `references/benchmark-reconciliation.md`.

Sources: ChartMogul, Baremetrics, OpenView, SaaS Capital, KeyBanc/Benchmarkit (private), **Meritech Capital** (public) — see `references/meritech-saas-benchmarks.md`.

## Core Metrics

### MRR / ARR
Monthly/Annual Recurring Revenue. The foundation.

### Churn Rate
- **Logo churn:** % of customers who cancel per month
- **Revenue churn:** % of MRR lost per month (includes downgrades)

| Stage | Good | Acceptable | Concerning |
|---|---|---|---|
| Bootstrapped | <3%/mo | 3-5%/mo | >5%/mo |
| SMB ($1-10M) | <3%/mo | 3-5%/mo | >5%/mo |
| Mid-market ($10-100M) | <2%/mo | 2-3%/mo | >3%/mo |
| Enterprise ($100M+) | <1%/mo | 1-2%/mo | >2%/mo |

### LTV (Customer Lifetime Value)

**Contribution-margin LTV** (what investors expect):
```
LTV = (ARPA × Gross Margin %) ÷ Monthly Churn Rate
```

Where ARPA = Average Revenue Per Account, Gross Margin = (Revenue − COGS) ÷ Revenue.

Never use raw-revenue LTV (ARPA ÷ churn) — it overstates value by ignoring COGS.

### CAC (Customer Acquisition Cost)

**Fully-loaded CAC:**
```
CAC = Total Sales & Marketing Spend ÷ New Customers Acquired
```

Include: salaries (fully loaded), commissions, ad spend, tools, events, agency fees. Use same period for spend and customers (quarterly or trailing 12 months).

### LTV:CAC Ratio

```
LTV:CAC = LTV ÷ CAC
```

| Stage | Minimum | Target | 
|---|---|---|
| Seed | 2:1 | 2-3:1 |
| Series A | 3:1 | 3.5-4:1 |
| Series B | 3.5:1 | 4-5:1 |
| Scale/IPO-track | 4:1 | 5:1+ |

Bootstrapped companies often hit 5-10x because organic acquisition is cheaper. Below 1:1 means you lose money on every customer. Above 10x may signal under-investment in growth.

### CAC Payback Period

```
CAC Payback (months) = CAC ÷ (New MRR per Customer × Gross Margin %)
```

| Segment | Target |
|---|---|
| SMB (ACV <$10K) | <12 months |
| Mid-market ($10K-$50K) | <18 months |
| Enterprise ($50K+) | <24 months |

Series A deal-breaker threshold: 18+ months.

### Net Revenue Retention (NRR)

```
NRR = (Starting MRR + Expansion − Contraction − Churned MRR) ÷ Starting MRR
```

| Stage | Good | Notes |
|---|---|---|
| SMB | >100% | Private median ~101% (KeyBanc) — see reconciliation |
| Mid-market | >110% | Series A gate ≥105% |
| Enterprise | >120% | Public leaders 120%+; Meritech public median ~108–111% |

Full threshold reconciliation → `references/benchmark-reconciliation.md`

### Magic Number

```
Magic Number = (Current Quarter ARR − Previous Quarter ARR) × 4 ÷ Previous Quarter S&M Spend
```

Measures go-to-market efficiency. ≥0.75 is good. <0.5 signals inefficient GTM spend.

### Rule of 40

```
Rule of 40 = Revenue Growth Rate (%) + Profit Margin (%)
```

Use EBITDA margin for the profit component. Early-stage companies often use gross margin as proxy.

| Stage | Target |
|---|---|
| Early | >20% |
| Growth | >30% |
| Scale | >40% |

## Calculation Cadence

- MRR, ARR, ARPA: monthly
- Churn, NRR: monthly with quarterly trend review
- CAC, LTV, Payback, Magic Number, Rule of 40: quarterly

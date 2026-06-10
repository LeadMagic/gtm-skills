# Due Diligence Metrics Pack

Standard metrics export for M&A, PE, or strategic diligence. Produce monthly; refresh within 30 days of process start.

**Sources:** David Skok (formulas), Ben Murray (SaaS P&L layers), KeyBanc SaaS Survey (benchmarks), Jason Lemkin (burn multiple).

## Cover Sheet (One Page)

| Field | Value | As-of date |
|---|---|---|
| ARR (contracted) | $ | |
| YoY growth | % | |
| NRR (TTM) | % | |
| GRR (TTM) | % | |
| Gross margin | % | |
| EBITDA margin | % | |
| Burn multiple (TTM) | x | |
| Magic number (last Q) | | |
| Rule of 40 | % | |
| CAC payback (mo) | | |
| LTV:CAC | x | |
| Top customer % ARR | % | |
| Headcount | | |

## Section 1: Revenue Bridge (Monthly, 24 mo)

```
Starting ARR
+ New logo ARR
+ Expansion ARR
− Contraction ARR
− Churned ARR
= Ending ARR
```

Export by: segment (SMB/MM/Ent), channel, geography if material.

## Section 2: Retention

| Table | Granularity |
|---|---|
| Logo churn (monthly) | 24 mo trend |
| Revenue churn (monthly) | 24 mo trend |
| NRR by cohort | Annual cohorts, 5 years if available |
| GRR by cohort | Same |
| Quick ratio | (New + Expansion) ÷ (Churn + Contraction) |

**Benchmarks:** NRR >110% PE-ready; GRR >90%; logo churn <2% monthly mid-market.

## Section 3: Unit Economics

| Metric | Formula | Segment breakdown |
|---|---|---|
| CAC | Fully loaded S&M ÷ new customers | By channel |
| LTV | (ARPA × GM%) ÷ monthly churn | By ACV band |
| LTV:CAC | LTV ÷ CAC | By segment |
| CAC payback | CAC ÷ (ARPA × GM%) | By segment |
| Magic number | Net new ARR (Q) ÷ S&M (prior Q) | Company + S&M efficiency |
| Burn multiple | Net burn ÷ net new ARR | TTM + quarterly |

Fully loaded S&M = salaries, commissions, tools, ads, events, agencies (Skok).

## Section 4: Customer Quality

- Top 20 customers: name, ARR, start date, contract term, NRR at account
- Concentration: top 1, 3, 10 as % ARR
- Churn list last 12 mo: reason codes
- Pipeline: weighted by stage (if strategic buyer)

**Red flag:** Top customer >20% ARR without mitigation plan.

## Section 5: P&L Summary (36 mo)

Ben Murray three layers:

1. **Revenue:** subscription vs services vs one-time (strip non-recurring for ARR multiple)
2. **COGS:** hosting, support, success (target GM 75%+)
3. **OpEx:** S&M, R&D, G&A — show trend as % of revenue

Include: EBITDA bridge, owner compensation normalization for SDE buyers.

## Section 6: GTM Efficiency

| Metric | Source |
|---|---|
| AE quota attainment distribution | CRM + comp |
| SDR → meeting → opp conversion | CRM |
| Win rate by segment | CRM |
| Sales cycle length | CRM |
| Founder-sourced vs team-sourced ARR | CRM attribution |

PE and strategic buyers use this to test **founder dependency**.

## Section 7: Projections (Optional, 3 Years)

- Base case only in data room until LOI
- Assumptions documented: churn, ACV, headcount, S&M as % new ARR
- Link to `financial-modeling/references/unit-economics-exit-bridge.md`

## Export Formats

- CSV for cohort and bridge tables
- PDF summary for cover sheet + narrative
- Secure data room (Notion, Docsend, or counsel platform)

## Cross-References

- Formulas + exit weight → `saas-metrics-calculator/references/metric-definitions-exit-weight.md`
- Readiness timeline → `buyer-readiness-checklist.md`
- Valuation sensitivity → `templates/valuation-sensitivity-table.md`

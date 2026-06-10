# Metric Definitions & Exit Weight

Formulas and how each metric affects exit/raise outcomes. **David Skok** established SaaS metric canon; **Jason Lemkin / David Sacks** burn multiple; **Bessemer** Rule of 40.

## Revenue

| Metric | Formula | Exit weight |
|---|---|---|
| **MRR** | Sum monthly subscription revenue | Base for ARR |
| **ARR** | MRR × 12 or sum ACV | Primary scale metric for multiples |
| **ARPA** | MRR ÷ paying customers | ACV band drives CAC payback tolerance |
| **Net new ARR** | New + expansion − churn − contraction (annualized) | Growth proof; burn multiple denominator |

## Retention

| Metric | Formula | Exit weight |
|---|---|---|
| **Logo churn (mo)** | Customers lost ÷ customers start | High churn → −1 to −3x multiple |
| **Revenue churn (mo)** | Churned MRR ÷ start MRR | PE/strategic diligence focus |
| **NRR** | (Start + expansion − contraction − churn) ÷ start | **Top 3 driver**; >110% PE-ready |
| **GRR** | (Start − contraction − churn) ÷ start | Purity test; >90% excellent |
| **Quick ratio** | (New + expansion MRR) ÷ (churn + contraction MRR) | >4x excellent; <2x fix retention |

## Unit Economics (Skok)

| Metric | Formula | Exit weight |
|---|---|---|
| **CAC** | Fully loaded S&M ÷ new customers | Understated CAC kills trust in diligence |
| **LTV** | (ARPA × GM%) ÷ monthly churn | Segment LTV required |
| **LTV:CAC** | LTV ÷ CAC | <3x blocks scale narrative |
| **CAC payback** | CAC ÷ (ARPA × GM%) | >18 mo → efficiency discount |

## Efficiency

| Metric | Formula | Exit weight |
|---|---|---|
| **Magic number** | Net new ARR (Q) ÷ S&M (prior Q) | >0.75 fundable; >1.0 premium |
| **Burn multiple** | Net burn ÷ net new ARR | <1x PE-friendly; >2x discount |
| **Rule of 40** | Growth % + EBITDA margin % | ≥40 public-premium proxy |
| **ARR / employee** | ARR ÷ FTE | Efficiency signal at scale |

## Stage Benchmarks (Summary)

| Metric | Pre-seed | Seed | Series A | Series B | PE-ready |
|---|---|---|---|---|---|
| YoY growth | PMF | 100–300% | 80–150% | 50–100% | 30–50% |
| NRR | >100% asp | >100% | >105% | >110% | >110% |
| GRR | >80% | >85% | >88% | >90% | >92% |
| Logo churn/mo | <3% | <2.5% | <2% | <1.5% | <1% |
| LTV:CAC | >3x | 3–5x | 3–5x | 3–5x | 4–6x |
| CAC payback | <12 | <12 | <12–15 | <15 | <18 |
| Magic number | >0.5 | >0.75 | >0.75 | >0.75 | >1.0 |
| Burn multiple | >3 OK | <2 | <2 | <1.5 | <1 |
| Rule of 40 | N/A | >20% | >30% | >35% | >40% |

Source blend: SaaS Capital, ChartMogul, KeyBanc — match stage in deliverables.

## Exit Weight by Buyer (Quick Reference)

| Metric | Strategic | PE | Bootstrap buyer |
|---|---|---|---|
| NRR | High | **Critical** | Medium |
| GRR | Medium | **Critical** | High |
| EBITDA | Low–Med | **Critical** | High (SDE) |
| Growth rate | **Critical** | Medium | Medium |
| Churn | High | **Critical** | **Critical** |
| Concentration | High | High | Medium |
| Magic number | Medium | High | Low |
| Burn multiple | Medium | **Critical** | N/A if profitable |

Full table → `saas-outcomes/references/exit-metrics-matrix.md`.

## Annualized Churn Note

Monthly churn `m` → annual logo retention = `(1 − m)^12`.  
Do not multiply monthly by 12.

## Cross-References

- Calculator workflow → `saas-metrics-calculator` SKILL.md
- MRR / ARR accounting deep dive → `references/saas-mrr-accounting-nuances.md`
- Bookings vs revenue → `references/bookings-billings-revenue-matrix.md`
- Definition conflicts → `references/benchmark-reconciliation.md`
- GTM funnel metrics → `gtm-metrics`
- P&L bridge → `financial-modeling/references/unit-economics-exit-bridge.md`
- Diligence export → `exiting-company/references/due-diligence-metrics-pack.md`

# SaaS Valuation Multiples Reference

Indicative ranges for planning — not transaction quotes. Refresh with **KeyBanc SaaS Survey**, **Bessemer Cloud 100**, **GetLatka** (bootstrap comps), and `financial-modeling` DCF for board work.

## ARR Multiple Drivers

| Driver | Pushes multiple up | Pushes multiple down |
|---|---|---|
| Growth | >40% YoY, accelerating | <20% or decelerating 3 quarters |
| Retention | NRR >120%, GRR >90% | NRR <100%, logo churn >10% annual |
| Margin | Rule of 40 ≥40 | Negative margin at scale without growth |
| Revenue quality | Subscription, multi-year | Services >15%, one-time |
| Concentration | No customer >10% ARR | Top 3 customers >40% |
| Efficiency | Burn multiple <1.5x, magic # >0.75 | Burn multiple >2x |
| Market | Category leader, expansion TAM | Commodity, single feature |
| GTM | Repeatable; founder <30% new ARR | Founder closes >50% of ARR |

## By Path (Private B2B SaaS)

| Path | Profile | Indicative ARR range |
|---|---|---|
| **Bootstrap sale** | $1–10M ARR, profitable, clean churn | 4–8x ARR; 3–6x SDE if owner-operated |
| **VC-backed** | 40%+ growth, NRR 115%+ | 8–15x ARR |
| **PE** | $10M+ ARR, EBITDA 15%+, NRR 110%+ | 8–12x ARR or 15–25x EBITDA |
| **Strategic premium** | Scarcity, bid, product fit | +2–5x vs financial buyer |

See `exit-metrics-matrix.md` for buyer-type weighting table.

## Rule of 40 & Burn Multiple

```
Rule of 40 = Revenue growth rate (%) + EBITDA margin (%)
Burn Multiple = Net cash burn ÷ Net new ARR
```

| Rule of 40 | Interpretation |
|---|---|
| ≥40 | Public-comp premium proxy (Bessemer) |
| 20–40 | Acceptable at scale |
| <20 | Discount unless strategic premium |

| Burn multiple | Interpretation (Lemkin/Sacks) |
|---|---|
| <1x | Capital-efficient; PE-friendly |
| 1–2x | Acceptable growth stage |
| >2x | Fix before raise or exit |

## Quick ARR Multiple Bands

| Growth (YoY) | Rough band | Notes |
|---|---|---|
| <20% | 2–5x | Profitability / EBITDA matter more |
| 20–40% | 4–8x | Rule of 40 weak → lower band |
| 40–80% | 6–12x | NRR >110% pushes up |
| 80%+ | 10–20x+ | Venture premium; revenue quality scrutinized |

## DCF (Hold vs Sell)

Use `financial-modeling/references/unit-economics-exit-bridge.md` for full bridge.

- **WACC:** 25–35% seed; 18–25% growth; 12–18% mature
- **Terminal growth:** 2–4%
- **Compare:** DCF equity vs LOI cash + earnout PV (`exiting-company/templates/valuation-sensitivity-table.md`)

## Bootstrap Exit Notes

- **SDE multiple** (owner-operated, <$2M ARR): 3–6x SDE (Latka/MicroAcquire comps)
- **Earnouts:** Probability-weight; never 100% in base case
- **409A vs market:** 409A for options; M&A uses market negotiation

## Checklist Before Quoting a Number

- [ ] ARR definition aligned (GAAP vs contracted vs recognized)
- [ ] Growth TTM and last-quarter annualized
- [ ] NRR and GRR with cohort definition
- [ ] Customer concentration listed
- [ ] One-time / services revenue stripped
- [ ] Method named (ARR vs EBITDA vs DCF vs SDE)
- [ ] Path named (bootstrap vs VC vs PE vs strategic)

## Cross-References

- Buyer matrix → `exit-metrics-matrix.md`
- Paths → `bootstrap-vs-vc-paths.md`
- M&A drivers → `exiting-company/references/valuation-drivers.md`
- Formulas → `saas-metrics-calculator/references/metric-definitions-exit-weight.md`

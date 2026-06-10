# Exit Metrics Matrix

What each buyer type weights at diligence. Use with `valuation-multiples.md` and `exiting-company/references/valuation-drivers.md`.

**Sources:** KeyBanc SaaS Survey (private multiples), **Meritech Capital** (public comps), Bessemer Rule of 40, David Skok (unit economics), Jason Lemkin (burn multiple), Nathan Latka (bootstrap M&A), Rob Walling (bootstrap path), SaaS Capital benchmarks. Threshold conflicts → `references/benchmark-reconciliation.md`.

## Buyer Weighting Table

| Buyer type | Metrics they weight | Red flags |
|---|---|---|
| **Strategic** | Product fit, customer overlap, talent, integration cost, TAM expansion | Customer concentration >20% one logo; IP gaps; hostile overlap with acquirer product |
| **PE (financial)** | EBITDA / FCF, NRR >110%, GRR >90%, predictable renewals, low churn, efficient GTM | High burn with no path to 20%+ EBITDA; founder closes >50% of ARR; services >15% revenue |
| **Acqui-hire / small M&A** | Team quality, tech stack, speed to integrate | Revenue <$500K with no product velocity; cap table disputes |
| **Bootstrap acquirer** (MicroAcquire, Latka-style) | Profitability, clean cap table, low churn, SDE/owner earnings | Messy books; 409A-only valuation story; undisclosed liabilities |
| **VC follow-on / growth equity** | TAM, growth rate, burn multiple, NRR, magic number | Burn multiple >3x at Series B+; NRR <100%; decelerating 3 quarters |

## Revenue Multiple Bands by Path (Indicative)

Refresh with KeyBanc + GetLatka comps before quoting. Ranges not guarantees.

| Profile | Bootstrapped / SMB sale | VC-backed private | PE platform |
|---|---|---|---|
| <$2M ARR, slow growth | 2–4x ARR or 3–6x SDE | 3–6x ARR (distressed) | Rare — acqui-hire |
| $2–10M ARR, 20–40% growth | 4–7x ARR | 5–10x ARR | 6–10x ARR if EBITDA+ |
| $10–30M ARR, 40%+ growth | 5–9x ARR | 8–15x ARR | 8–12x ARR + EBITDA focus |
| $30M+ ARR, efficient | 6–10x ARR | 10–20x ARR | 10–14x ARR or 15–25x EBITDA |

**PE note:** Sub-$50M ARR deals often blend **ARR multiple (growth)** with **EBITDA multiple (cash)**. Target: 15–25x EBITDA for mature SaaS with 20%+ margins (Ben Murray / SaaS CFO framing).

## Core Metric Benchmarks (Exit-Relevant)

| Metric | Bootstrap target | VC Series A/B | PE-ready |
|---|---|---|---|
| **NRR** | >100% | >110–120% | >110% (115%+ premium) |
| **GRR** | >85% | >88–90% | >92% |
| **Logo churn (monthly)** | <2.5% SMB | <2% | <1.5% |
| **Rule of 40** | N/A early; margin path | >30% at A; >40% at scale | EBITDA + growth ≥40 |
| **Burn multiple** | <1x (profitable) or N/A | <2x seed/A; <1.5x B | <1x preferred |
| **Magic number** | >0.75 | >0.75–1.0 | >1.0 |
| **CAC payback** | <12 mo | <12–15 mo | <18 mo at enterprise ACV |
| **LTV:CAC** | >3x (Skok) | 3–5x | 4–6x |
| **Gross margin** | >70% | >75% | >78% |
| **Customer concentration** | Top customer <15% | Top 3 <40% | Top customer <10% |

## Efficiency Metrics (Lemkin / Sacks)

```
Burn Multiple = Net Cash Burn ÷ Net New ARR (TTM or quarter annualized)
Magic Number = Net New ARR (Q) ÷ S&M Spend (prior Q)
Rule of 40 = Revenue Growth % + EBITDA Margin %
```

| Burn multiple | Interpretation |
|---|---|
| <1x | Capital-efficient; PE-friendly |
| 1–2x | Acceptable growth stage |
| >2x | Fix before raise or exit process — diligence discount |

## Path Decision Quick Check

| Signal | Lean bootstrap exit | Lean VC scale | Lean PE |
|---|---|---|---|
| TAM ceiling ~$20M ARR | ✓ | | |
| NRR >120%, large TAM | | ✓ | |
| $5M+ ARR, 25%+ EBITDA, NRR 110% | | | ✓ |
| Founder wants max control | ✓ | | |
| Competitors raising fast | | ✓ | |
| Growth slowing, profitable | ✓ or PE | | ✓ |

## Cross-References

- Exit optionality score → `exit-potential-scorecard.md`
- Journey stage 6 gate → `journey-stage-gates.md`
- Multiples detail → `valuation-multiples.md`
- Path operating rules → `bootstrap-vs-vc-paths.md`
- M&A prep → `exiting-company/references/buyer-readiness-checklist.md`
- Formulas → `saas-metrics-calculator/references/metric-definitions-exit-weight.md`
- P&L → multiple bridge → `financial-modeling/references/unit-economics-exit-bridge.md`
- VC round gates → `fundraising-strategy/references/vc-milestone-gates.md`

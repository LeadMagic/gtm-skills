# Valuation Drivers for SaaS Exits

What moves enterprise value in M&A. **Not legal or tax advice.**

**Sources:** KeyBanc SaaS Survey, David Skok (unit economics), Jason Lemkin (burn multiple, growth efficiency), Nathan Latka (bootstrap M&A comps), Ben Murray (SaaS CFO — EBITDA bridge).

## Primary Value Drivers (Ranked)

| Rank | Driver | Why buyers care | Target band |
|---|---|---|---|
| 1 | **Revenue growth (YoY)** | Future cash flows; strategic urgency | >40% premium; <20% discount |
| 2 | **NRR / GRR** | Expansion vs leakage | NRR >110%; GRR >90% |
| 3 | **Revenue quality** | Recurring, contracted, subscription | Services <15%; multi-year ↑ |
| 4 | **Gross margin** | Scalability | >75% SaaS |
| 5 | **Efficiency** | Capital to grow | Burn multiple <1.5x; magic number >0.75 |
| 6 | **EBITDA / FCF** | PE returns | 15–25%+ at PE scale |
| 7 | **Market position** | Strategic premium | Category leader or unique data/IP |
| 8 | **Team depth** | Integration risk | VP Sales + CS; founder <30% of new ARR |
| 9 | **Concentration** | Risk discount | Top customer <15% ARR |
| 10 | **Cap table** | Deal friction | Clean; no blocking prefs |

## EBITDA vs Revenue Multiples

| Buyer | Primary metric | Secondary | Typical range |
|---|---|---|---|
| Strategic (growth) | ARR × growth-adjusted multiple | Synergy NPV | 5–15x ARR; premium for fit |
| PE (platform) | EBITDA × multiple | ARR growth for upside | 15–25x EBITDA; 8–12x ARR hybrid |
| Bootstrap buyer | SDE or ARR | Churn, margin | 3–6x SDE; 4–8x ARR |
| Acqui-hire | Team value | Tech | $1–3M/engineer band |

**Bridge formula (planning):**

```
Implied EV (PE) ≈ EBITDA × EBITDA Multiple
Implied EV (Growth) ≈ ARR × ARR Multiple (growth, NRR, Rule of 40 adjusted)

Reconcile: If EBITDA multiple EV << ARR multiple EV, buyer is PE; if ARR >> EBITDA, strategic growth buyer.
```

See `financial-modeling/references/unit-economics-exit-bridge.md` for P&L → both multiples.

## Strategic vs Financial Buyer Criteria

### Strategic acquirer

- **Buys for:** Product gap, customer overlap, talent, defensive block
- **Weights:** Integration cost, TAM expansion, cross-sell rate
- **Premium when:** Competitive bid, unique asset, time-to-market > build
- **Discount when:** Overlap kills product line; antitrust; culture clash

### Financial (PE) acquirer

- **Buys for:** Cash yield, roll-up, operational improvement
- **Weights:** EBITDA, renewal predictability, GTM efficiency, low churn
- **Requires:** NRR >110%, path to 20%+ EBITDA, management bench or ops playbook
- **Discount when:** High burn, founder dependency, re-platforming cost

## Growth-Adjusted ARR Multiple (Quick Model)

Start with base band from KeyBanc growth tier, then adjust:

| Adjustment | Δ Multiple |
|---|---|
| NRR >120% | +1–3x |
| NRR <100% | −2–4x |
| Rule of 40 ≥40 | +1–2x |
| Top customer >20% ARR | −1–3x |
| Burn multiple >2x | −1–2x |
| Founder closes >50% ARR | −1–2x |
| Strategic scarcity / bid | +2–5x |

Use `templates/valuation-sensitivity-table.md` for low/base/high scenarios.

## Bootstrap Exit (Latka / MicroAcquire)

Sub-$10M ARR bootstrapped SaaS often trades on:

- **Growth + churn** more than absolute ARR
- **Owner earnings** (SDE) for owner-operated businesses
- **Clean books** — QuickBooks-grade, 24+ mo history
- **Searchable profile** — GetLatka, MicroAcquire, broker network

Latka 5 levers still apply at diligence: traffic, leads, conversion, pricing, churn.

## Red Flags That Kill or Delay Deals

- Missing IP assignment from contractors
- Customer concentration >25% one logo
- NRR <95% with no credible fix plan
- Undisclosed related-party revenue
- Cap table disputes or uncapped SAFE stack surprises
- Founder is only enterprise closer with no succession plan

## Cross-References

- Buyer weighting table → `saas-outcomes/references/exit-metrics-matrix.md`
- Readiness checklist → `buyer-readiness-checklist.md`
- Diligence data pack → `due-diligence-metrics-pack.md`
- Metric formulas → `saas-metrics-calculator/references/metric-definitions-exit-weight.md`

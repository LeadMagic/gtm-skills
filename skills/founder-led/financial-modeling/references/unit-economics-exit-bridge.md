# Unit Economics → Exit Value Bridge

Connect operating model to valuation multiples. Use with DCF in `financial-modeling` SKILL.md.

**Sources:** David Skok (LTV/CAC), Ben Murray (SaaS P&L), Aswath Damodaran (DCF), KeyBanc (ARR multiples), Jason Lemkin (burn multiple).

## The Bridge (Conceptual)

```
Unit economics (LTV, CAC, payback)
    ↓
Retention (NRR, GRR, cohort curves)
    ↓
Growth efficiency (magic number, burn multiple)
    ↓
P&L (GM, EBITDA margin, Rule of 40)
    ↓
Valuation method (ARR multiple vs EBITDA multiple vs DCF)
    ↓
Enterprise value → equity value (net debt, prefs)
```

## Step 1: Unit Economics → LTV Quality

```
LTV = (ARPA × Gross Margin %) ÷ Monthly Logo Churn Rate
LTV:CAC = LTV ÷ CAC
CAC Payback (mo) = CAC ÷ (ARPA × Gross Margin %)
```

| LTV:CAC | Exit implication |
|---|---|
| <3x | Discount 1–2x ARR multiple; fix before process |
| 3–5x | Baseline (Skok investable) |
| >5x | May support premium if growth holds |

## Step 2: Retention → Revenue Durability

```
NRR = (Start MRR + Expansion − Contraction − Churn) ÷ Start MRR
GRR = (Start MRR − Contraction − Churn) ÷ Start MRR
```

| NRR | Typical multiple impact |
|---|---|
| <100% | −2 to −4x vs growth peer |
| 100–110% | Baseline |
| 110–120% | +1 to +2x |
| >120% | Venture/strategic premium |

## Step 3: Efficiency → Capital Narrative

```
Magic Number = Net New ARR (Q) ÷ S&M Spend (prior Q)
Burn Multiple = Net Cash Burn ÷ Net New ARR
Rule of 40 = Growth % + EBITDA Margin %
```

Efficient growth (burn multiple <1.5x, magic number >0.75) supports **higher ARR multiple** and **PE interest**.

## Step 4: P&L → EBITDA Multiple (PE Path)

Example bridge (fill with your model):

| Line | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| ARR | $10M | $14M | $18M |
| Revenue (recognized) | $8M | $12M | $16M |
| Gross margin % | 78% | 80% | 82% |
| S&M % revenue | 35% | 30% | 25% |
| R&D % revenue | 20% | 18% | 15% |
| G&A % revenue | 12% | 10% | 9% |
| **EBITDA margin** | **11%** | **22%** | **33%** |
| EBITDA $ | $0.9M | $2.6M | $5.3M |

```
PE EV (illustrative) = EBITDA (Year 3 run-rate or TTM) × 18–22x
Growth EV (illustrative) = ARR × 8–12x (adjust for NRR, growth)
```

Reconcile both; buyer type determines which binds.

## Step 5: DCF Cross-Check

```
EV = Σ FCF_t / (1+WACC)^t + Terminal Value
Terminal Value = FCF_5 × (1+g) / (WACC − g)
```

| Stage | WACC band |
|---|---|
| Seed / early | 20–30% |
| Growth | 15–20% |
| Mature / PE | 10–15% |

If DCF EV differs >30% from ARR comp EV, document assumption delta (growth decay, margin ramp, terminal g).

## Sensitivity Drivers (Rank by Impact)

1. Revenue growth rate (±10% → largest EV swing)
2. NRR (±5 pts)
3. EBITDA margin at year 3
4. WACC / discount rate
5. Terminal growth rate (2–4% cap)

Use `exiting-company/templates/valuation-sensitivity-table.md` or duplicate in model.

## Hold vs Sell (After-Tax)

Compare:

- **Sale:** LOI cash + PV(earnout × probability) − tax − transaction costs
- **Hold:** DCF equity value at year 5 − continued dilution if VC path

Cross-ref: `saas-outcomes` Phase 5 exit timing heuristics.

## Cross-References

- Full DCF steps → `financial-modeling` SKILL.md (DCF section)
- Metric definitions → `saas-metrics-calculator/references/metric-definitions-exit-weight.md`
- Buyer drivers → `exiting-company/references/valuation-drivers.md`
- VC gates → `fundraising-strategy/references/vc-milestone-gates.md`

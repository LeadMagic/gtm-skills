# Valuation Sensitivity Table

Fill for board, fundraise, or M&A scenarios. **Ranges not quotes.**

## ARR Multiple Sensitivity

**Base inputs:**

| Input | Low | Base | High |
|---|---|---|---|
| ARR ($M) | | | |
| YoY growth % | | | |
| NRR % | | | |
| Base multiple (KeyBanc tier) | | | |

**Adjustments (cumulative on base multiple):**

| Factor | Low case | Base | High case |
|---|---|---|---|
| NRR adjustment | −2x if <100% | 0 | +2x if >120% |
| Concentration | −2x if top >20% | 0 | 0 |
| Burn multiple | −1x if >2x | 0 | +1x if <1x |
| Strategic premium | 0 | 0 | +3x if bid |

```
Implied EV = ARR × Adjusted Multiple
Equity value = EV − net debt − liquidation prefs (simplified — use counsel)
```

## EBITDA Multiple Sensitivity (PE)

| Input | Low | Base | High |
|---|---|---|---|
| TTM EBITDA ($M) | | | |
| EBITDA margin % | | | |
| Multiple | 14x | 18x | 22x |

```
PE EV = EBITDA × Multiple
```

## DCF Sensitivity (WACC × Terminal Growth)

| WACC ↓ / g → | 2% | 3% | 4% |
|---|---|---|---|
| 12% | $ | $ | $ |
| 15% | $ | $ | $ |
| 18% | $ | $ | $ |
| 22% | $ | $ | $ |

WACC bands: early 20–30%, growth 15–20%, mature 10–15% (Damodaran).

## Hold vs Sell (After-Tax)

| Scenario | Year 5 equity value | Probability | Weighted |
|---|---|---|---|
| Hold (DCF base) | $ | 100% | $ |
| LOI cash at close | $ | 90% | $ |
| Earnout (max) | $ | 40% | $ |
| Transaction costs + tax | −$ | 100% | −$ |

**Decision rule:** Sell when weighted LOI > hold DCF × (1 + founder preference discount for control).

## Cross-References

- Drivers → `../references/valuation-drivers.md`
- P&L bridge → `financial-modeling/references/unit-economics-exit-bridge.md`
- Multiples bands → `saas-outcomes/references/valuation-multiples.md`

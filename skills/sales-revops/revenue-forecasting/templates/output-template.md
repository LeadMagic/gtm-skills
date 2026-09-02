# Revenue Forecast Pack

## Context

- Revenue type: `[bookings/ARR/revenue/consumption]`
- Period and cutoff: `[period]`
- Currency and time zone: `[currency/time zone]`
- Owner and snapshot: `[owner/date]`
- Target: `[amount]`

## Framework Basis

- Forecast categories: `[definitions]`
- Historical model: `[cohort and period]`
- Evidence inspection: `[application]`

## Recommendation

`[Base forecast, range, confidence, and decision]`

## Category Definitions

| Category | Entry evidence | Removal rule | Owner |
|---|---|---|---|
| Commit | `[buyer evidence]` | `[rule]` | `[role]` |
| Likely | `[buyer evidence]` | `[rule]` | `[role]` |
| Upside | `[buyer evidence]` | `[rule]` | `[role]` |

## Forecast Bridge

| Component | Downside | Base | Upside | Evidence or assumption |
|---|---:|---:|---:|---|
| Closed | `[amount]` | `[amount]` | `[amount]` | `[source]` |
| Open pipeline | `[amount]` | `[amount]` | `[amount]` | `[method]` |
| Renewal/expansion/churn | `[amount]` | `[amount]` | `[amount]` | `[method]` |
| Total | `[amount]` | `[amount]` | `[amount]` | `[reconciliation]` |

## Opportunity Evidence and Risk

| Opportunity | Amount | Category | Buyer evidence | Risk | Next event | Scenario |
|---|---:|---|---|---|---|---|
| `[deal]` | `[amount]` | `[category]` | `[evidence]` | `[risk]` | `[date/event]` | `[case]` |

## Historical Assumptions

| Cohort | Sample | Conversion | Median timing | Slip rate | Limitation |
|---|---:|---:|---:|---:|---|
| `[cohort]` | `[n]` | `[rate]` | `[days]` | `[rate]` | `[constraint]` |

## Implementation Steps

| Action | Owner | Due | Artifact or system | Validation |
|---|---|---|---|---|
| `[action]` | `[owner]` | `[date]` | `[artifact]` | `[metric]` |

## Metrics

- Forecast absolute error: `[measure]`
- Directional bias: `[measure]`
- Commit attainment: `[measure]`
- Slip rate: `[measure]`

## Risks and Open Questions

- `[data, timing, concentration, or assumption risk]`

## Quality Check

- [ ] Forecast contract and snapshot are explicit.
- [ ] Scenarios reconcile to opportunity data.
- [ ] Evidence and judgment are distinguishable.
- [ ] Accuracy will be graded after the period.

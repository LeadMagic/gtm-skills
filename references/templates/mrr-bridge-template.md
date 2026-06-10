# MRR Bridge Template

**Use with:** `references/saas-mrr-accounting-nuances.md` · `saas-metrics-calculator` · board/investor packs.

Period: **Month / Quarter / Year** — specify and keep consistent.

---

## Summary Bridge

| Component | $ MRR | Notes |
|---|---|---|
| **Starting MRR** | | End of prior period |
| + New logo MRR | | First paid subscription only |
| + Expansion MRR | | Upsell, seats, tier, cross-sell recurring |
| − Contraction MRR | | Downgrades (partial) |
| − Churned MRR | | Full logo cancels |
| **= Ending MRR** | | Must tie to billing system |
| **Net new MRR** | | Ending − Starting |
| **Ending ARR** | | Ending MRR × 12 (if monthly norm) |

---

## Logo Bridge (Optional)

| Component | Logos |
|---|---|
| Starting paying logos | |
| + New logos | |
| − Churned logos | |
| **= Ending logos** | |

| Metric | Value |
|---|---|
| Logo churn rate | Churned ÷ Starting |
| ARPA | Ending MRR ÷ Ending logos |

---

## NRR / GRR (Dollar Cohort)

Base = **starting MRR** of cohort (usually prior period total installed base).

```
NRR = (Starting + Expansion − Contraction − Churn) ÷ Starting
GRR = (Starting − Contraction − Churn) ÷ Starting
```

| Metric | This period |
|---|---|
| Starting MRR (base) | |
| + Expansion | |
| − Contraction | |
| − Churn | |
| **NRR %** | |
| **GRR %** | |

Benchmarks → `references/benchmark-reconciliation.md`.

---

## Detail Tabs (Recommended)

### New Logo MRR

| Account | Segment | MRR | Start date | Sales owner | CRM opp ID |
|---|---|---|---|---|---|
| | | | | | |

### Expansion MRR

| Account | Type (seat/tier/usage) | Δ MRR | Effective date |
|---|---|---|---|
| | | | |

### Contraction MRR

| Account | Reason | Δ MRR |
|---|---|---|
| | | |

### Churn MRR

| Account | Churn date | Lost MRR | Reason code |
|---|---|---|---|
| | | | |

---

## Reconciliation Checklist

- [ ] Ending MRR ties to billing/subscription system
- [ ] PS / one-time excluded from MRR columns
- [ ] Annual contracts normalized (ACV ÷ 12)
- [ ] Pending cancels policy applied consistently
- [ ] CRM closed-won reconciled to committed MRR (bookings matrix)
- [ ] Meritech implied ARR **not** mixed with committed ARR without label

---

## Cross-References

- Definition variants → `references/saas-mrr-accounting-nuances.md`
- Bookings vs billings vs revenue → `references/bookings-billings-revenue-matrix.md`
- Calculator workflow → `saas-metrics-calculator`
- Exit diligence → `exiting-company/references/due-diligence-metrics-pack.md`

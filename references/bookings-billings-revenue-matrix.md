# Bookings vs Billings vs Revenue — GTM & Finance Matrix

**Canonical home:** `saas-metrics-calculator` (with `references/saas-mrr-accounting-nuances.md`).  
**Audience:** RevOps and founders aligning CRM, billing, and board metrics — **not** accounting advice.

---

## Three-Ledger View

| | **Bookings** | **Billings** | **Revenue (GAAP)** |
|---|---|---|---|
| **Timing** | Contract signed (order form) | Invoice sent / cash due | Earned per ASC 606 |
| **Typical source** | CRM closed-won, CPQ | Billing system (Stripe, Chargebee) | GL / ERP |
| **Annual prepay $120K** | +$120K in sign month (TCV) | +$120K invoice (or +$10K if monthly) | +$10K/month recognized |
| **Multi-year $300K / 3yr** | +$300K TCV (or ACV $100K/yr) | Per billing schedule | Ratable over term (usually) |
| **Implementation $30K** | Often in TCV | Invoiced per milestone | Recognized as delivered |
| **Usage overage** | May be in commit or true-up | Monthly invoice | As consumed |

---

## When Each Matters

### GTM & RevOps (primary: bookings → committed MRR)

- **Sales quota & comp:** Bookings / ACV at signature (with clawbacks for churn — policy-dependent).
- **Pipeline conversion:** CRM stage → closed-won **booking** date.
- **Board growth narrative:** Net new **committed ARR** (not billings spike from prepay).
- **Magic Number / burn multiple:** Numerator = net new **ARR** (committed), not billings.

**Gap to watch:** CRM pipeline vs GAAP revenue — enterprise 90-day+ implementation delays recognition; board should see **both** committed ARR bridge and revenue growth.

### Finance & fundraising (primary: revenue + billings)

- **Audit & due diligence:** GAAP revenue, deferred revenue roll-forward.
- **Rule of 40 (GAAP):** Growth on **recognized** revenue; margin on GAAP EBITDA/FCF.
- **Cash planning:** Billings and collections — prepay helps runway without changing monthly MRR.
- **Public comps:** Meritech implied ARR from **reported revenue** — see `references/meritech-saas-benchmarks.md`.

---

## Multi-Year Prepay Treatment

| Scenario | Bookings | Billings | Revenue | Committed MRR |
|---|---|---|---|---|
| 3-year, $360K, billed annually | $360K TCV at sign | $120K/yr | ~$10K/mo | $10K (ACV/12) |
| 3-year, full upfront | $360K | $360K month 1 | ~$10K/mo | $10K |
| 3-year, 20% YoY uplift | TCV $360K+ | Per schedule | May ramp with obligation | Use contract schedule |

**GTM anti-pattern:** Celebrating $360K "ARR added" on signing for upfront cash — correct **committed** add is $10K MRR ($120K ACV year 1 if flat).

**Earn-out / exit:** Buyers often use **committed ARR** or **NTM recurring revenue** — not cumulative bookings. EBITDA earn-outs may exclude revenue recognition timing benefits — `exiting-company/references/negotiating-earn-out.md`.

---

## CRM Pipeline vs GAAP Revenue Gap

Common causes:

1. **Implementation delay** — booking signed; go-live 60–120 days later → revenue starts late.
2. **Bundled PS** — subscription recognized over 12 mo; PS lumpy.
3. **Usage model** — booking = commit; revenue trails consumption.
4. **Contract modifications** — CRM not updated on downgrade.
5. **Channel/reseller** — booking at list; net revenue different.

**RevOps monthly reconcile:** CRM committed ARR ↔ billing system ↔ finance ARR schedule. Document variances >2% in board appendix.

---

## Consumption & Hybrid (Snowflake / Databricks)

| Layer | Bookings | Revenue |
|---|---|---|
| Capacity commit | RPO / TCV in CRM | Ratable or as consumed (policy) |
| Overages | Not in initial booking | Monthly true-up revenue |
| Platform + usage | Split in CPQ | Split obligations |

McMahon board lens: report **new logos vs expansion** on committed base; finance adds consumption run-rate vs commit coverage.

---

## Professional Services

| Question | GTM default | Finance |
|---|---|---|
| In Magic Number numerator? | No (subscription ARR only) | N/A |
| In quota? | Sometimes (split SKUs) | PS margin separate |
| In "ARR"? | Exclude from SaaS ARR | Total revenue includes |

---

## Quick Decision Tree

```
Board asks "how fast are we growing?"
  → Committed net new ARR bridge (RevOps)

CFO asks "are we GAAP-clean for audit?"
  → Revenue recognition schedule + deferred roll-forward

CEO asks "how long is runway?"
  → Billings, collections, burn (financial-modeling)

Investor compares to public SaaS index?
  → Label: private committed ARR ≠ Meritech implied ARR

Sales asks "did I hit quota?"
  → Bookings per comp plan (document exclusions)
```

---

## Cross-References

- MRR variants & ASC 606 summary → `references/saas-mrr-accounting-nuances.md`
- Metric formulas → `saas-metrics-calculator`, `references/saas-metrics-reference.md`
- Benchmark alignment → `references/benchmark-reconciliation.md`
- Budget & cash → `references/gtm-budget-playbook.md`, `financial-modeling`
- Exit diligence pack → `exiting-company/references/due-diligence-metrics-pack.md`

---

## Disclaimer

Matrix for operational alignment. Revenue recognition and tax treatment require **qualified CPA** sign-off on your facts and contracts.

# SaaS MRR & ARR Accounting Nuances

**Canonical home:** `saas-metrics-calculator` (operational metrics) · cross-link `financial-modeling` (P&L/cash) · reconcile definitions → `references/benchmark-reconciliation.md`.

**Audience:** GTM founders and RevOps operators who need to **audit metrics**, align CRM with finance, and talk credibly to CPAs — **not** a GAAP textbook or CPA replacement.

---

## Why This Doc Exists

Three teams often report three different "ARR" numbers:

| Team | Typical definition | Risk |
|---|---|---|
| **Sales / CRM** | Bookings at signature (TCV, annualized) | Inflates vs cash and GAAP |
| **RevOps / billing** | Committed recurring (normalized monthly) | May include non-recurring |
| **Finance / GAAP** | Revenue recognized per ASC 606 | Lags bookings; excludes one-time |

RevOps job: **one written definition** per board metric, with bridge tables when sources diverge.

---

## MRR Definition Variants

### Committed MRR (RevOps default)

Sum of **active subscription contracts**, normalized to monthly:

```
Annual contract $120K → MRR = $10K
Quarterly $30K → MRR = $10K
Multi-year prepay → still MRR = ACV ÷ 12 (not cash received)
```

**Include:** Core platform subscription, committed seat tiers, committed usage minimums.  
**Exclude:** One-time implementation, training, pass-through, non-recurring discounts unless contractually recurring.

### Recognized MRR (finance / GAAP proxy)

Revenue **recognized in the period** under ASC 606, expressed monthly. Differs from committed when:

- Multi-element arrangements (license + services)
- Ramp deals (price increases over term)
- Usage/consumption (recognized as consumed)
- Professional services (often separate performance obligation)

### Billings MRR (cash / collections lens)

**Invoice amount** in period ÷ contract months — or annual invoice ÷ 12 in invoice month.

| Lens | Best for |
|---|---|
| Committed MRR | Board ARR, NRR, GTM efficiency |
| Recognized MRR | GAAP reconciliation, audit |
| Billings MRR | Cash forecasting, collections |

**Rule:** Never compare your private committed ARR to Meritech **implied ARR** (Q revenue × 4) without a footnote — see `references/meritech-saas-benchmarks.md`.

---

## MRR Bridge Components

Standard bridge (forward and backward):

```
Ending MRR = Starting MRR
           + New Logo MRR
           + Expansion MRR
           − Contraction MRR
           − Churned MRR
```

| Component | Definition | Common mistakes |
|---|---|---|
| **New logo** | First paid subscription for account | Re-activation counted as new |
| **Expansion** | Upsell, cross-sell, seat add, tier upgrade | One-time PS in expansion |
| **Contraction** | Downgrade, seat remove, tier down | Partial churn mis-bucketed |
| **Churn** | Full logo cancel; MRR to zero | Pending cancel still in base |

Template → `references/templates/mrr-bridge-template.md`.

**Logo vs dollar:** Track **logo churn** and **revenue churn** separately. NRR/GRR use **dollar** cohort on starting MRR base — see `saas-metrics-calculator`.

---

## Annual Prepay vs Monthly Billing

| Billing | Committed MRR | Cash | Deferred revenue |
|---|---|---|---|
| Monthly | ACV ÷ 12 each month | ~MRR/month | Minimal |
| Annual upfront | ACV ÷ 12 (smooth) | 12× MRR in month 1 | 11/12 deferred |

**GTM mistake:** Using cash collected as "MRR added" in prepay month → **inflates** growth and Magic Number.

**Finance link:** Deferred revenue = cash/billings ahead of recognition. Rising deferred with flat committed MRR can mean prepay mix shift — not necessarily acceleration.

---

## Professional Services Revenue

| Treatment | When | SaaS metrics impact |
|---|---|---|
| **Exclude from MRR/ARR** | Implementation, onboarding, custom dev (default RevOps) | Keeps SaaS multiples clean |
| **Include in "total revenue"** | Finance P&L | Required for EBITDA |
| **Separate line in bridge** | Strategic board pack | Shows services drag on margin |

**PE/strategic diligence:** High PS % of revenue → lower SaaS multiple; buyers haircut or exclude from ARR.

**ASC 606 note:** PS often distinct performance obligation — recognized as delivered, not ratably with subscription unless bundled as one combined obligation (complex — **CPA required**).

---

## Consumption Revenue (Snowflake / Databricks Pattern)

| Metric | Meaning | GTM use |
|---|---|---|
| **Committed / capacity** | Customer prepays credits or minimum | Forecast stability |
| **Usage / consumption** | Actual compute/API consumed | NRR driver when usage grows |
| **Recognized revenue** | GAAP as usage occurs | Finance reporting |

**McMahon / Slootman lens:** Enterprise consumption companies track **bookings vs consumption run-rate**. Bookings ahead of usage = future revenue; bookings below usage = renewal/expansion risk.

**RevOps bridge:** Don't apply seat-based MRR formulas to pure usage without a **committed floor**. Hybrid: platform fee (MRR) + variable usage (monthly true-up).

Cross-link: `financial-modeling` consumption section · `gtm-metrics` Slootman row · `references/benchmark-reconciliation.md` (consumption metrics).

---

## Implied ARR vs Contractual ARR

| Definition | Formula | Use |
|---|---|---|
| **Contractual ARR** | Sum of active contract ACV (private) | Internal board, fundraising |
| **Committed MRR × 12** | RevOps normalized | NRR, Magic Number |
| **Implied ARR (Meritech)** | Quarterly **total revenue** × 4 | Public comps only |
| **Run-rate ARR** | Last month MRR × 12 | Early-stage shortcut (volatile) |

**Never** present implied ARR methodology as your private ARR without labeling — investors will re-cut on diligence.

---

## Deferred Revenue Relationship

```
Deferred revenue (balance sheet) ≈ Billings − Revenue recognized (cumulative, subscription portion)
```

**Founder/RevOps checks:**

- Prepay mix ↑ → deferred ↑ (healthy if churn low)
- Deferred flat, billings ↑ → recognition catching up or PS mix
- Deferred ↓ faster than churn → recognition front-loaded or contract shorten

Full journal entries → CPA. RevOps needs **directional** link for board Q&A.

---

## ASC 606 — Practitioner Summary (SaaS)

High-level only — **not tax or audit advice.**

1. **Identify contract** with customer (MSA + order form).
2. **Identify performance obligations** — typically: (a) SaaS access over time, (b) PS distinct if separately priced/standalone sellable.
3. **Allocate transaction price** to obligations (SSP or observable price).
4. **Recognize revenue** as obligations satisfied — subscription **over time** (ratably), PS **as delivered** or over time if distinct series.

**SaaS-specific wrinkles:**

- **Bundled PS** in year-one ACV → part may hit services COGS/revenue, not subscription MRR.
- **Material rights** (renewal discounts) → may defer part of initial deal.
- **Usage-based** → recognize as usage occurs (variable consideration estimates — CPA).

Handoff trigger: first enterprise MSAs with custom terms, multi-year ramps, or significant PS → engage SaaS-experienced CPA (see `references/saas-tax-founder-awareness.md` experts).

---

## Common RevOps Mistakes (Inflating / Deflating MRR)

| Mistake | Effect | Fix |
|---|---|---|
| Counting TCV at signing as MRR | Inflate | Normalize to monthly committed |
| Including one-time discounts as recurring | Inflate | Separate credits; expire promos |
| Excluding active expansions until renewal | Deflate | Track expansion at effective date |
| Treating pending churn as active | Inflate | Define cancel effective date policy |
| Mixing PS and subscription | Distorts NRR | Split lines in bridge |
| Annual prepay cash = new ARR | Inflate growth | Use committed MRR bridge |
| CRM "Amount" field without normalization | Garbage | CRM ACV field = annual committed only |
| Re-activations as new logo | Inflate new ARR | Policy: logo ID + 90-day rule |

---

## Bookings vs Billings vs Revenue

Deep matrix → `references/bookings-billings-revenue-matrix.md`.

**Quick GTM vs finance:**

| Metric | GTM cares when | Finance cares when |
|---|---|---|
| **Bookings** | Quota, pipeline, board growth story | Less (non-GAAP) |
| **Billings** | Cash runway, collections | AR, deferred |
| **Revenue** | Rule of 40 margin side | Audit, tax, public comps |

---

## Cross-References

| Topic | Doc / skill |
|---|---|
| Formulas & benchmarks | `saas-metrics-calculator`, `references/saas-metrics-reference.md` |
| Exit weight by metric | `saas-metrics-calculator/references/metric-definitions-exit-weight.md` |
| Public implied ARR | `references/meritech-saas-benchmarks.md` |
| Conflicting thresholds | `references/benchmark-reconciliation.md` |
| Earn-out / EBITDA vs MRR | `exiting-company/references/negotiating-earn-out.md`, `benchmark-reconciliation.md` |
| Budget & headcount tie | `references/gtm-budget-playbook.md` |
| Consumption modeling | `financial-modeling` SKILL — consumption section |

---

## Disclaimer

Practitioner summary for GTM operators. **Engage a qualified CPA** for GAAP policy, revenue recognition memos, audit, and tax. Definitions here align with common SaaS operator practice — your contracts and jurisdiction may differ.

# SaaS Tax & Finance Compliance — Founder Awareness

**Canonical home:** `financial-modeling` (with `founder-comp-playbook`, `exiting-company`, `fundraising-strategy`).  
**Not tax advice, not legal advice.** Typical situations only — **get professional advice** before acting.

---

## How to Use This Doc

| You need | Action |
|---|---|
| Sales tax on SaaS in new states | CPA + sales tax automation vendor |
| International VAT/GST | CPA with cross-border SaaS experience |
| R&D tax credit claim | CPA (often Kruze, Armanino-class firms) |
| QSBS at exit | Tax counsel + CPA — cap table from Carta |
| 409A for option grants | 409A provider (Carta, etc.) + counsel |
| Transfer pricing | Big-four or specialized TP firm |

---

## When Founders Need Tax Counsel (Handoff Triggers)

Engage qualified professionals when **any** of:

- Selling into **new US states** (physical or economic nexus)
- **International** customers (VAT, GST, MOSS, local registration)
- **Annual revenue >$1–2M** or preparing **Series A** (clean books + tax posture)
- **Profitable** or approaching profitability (estimated taxes, R&D credit planning)
- **Exit LOI signed** (structure, QSBS, asset vs stock, state nexus cleanup)
- **Multi-entity** or **foreign subsidiary**
- Employees in **multiple states** (payroll nexus interaction)

---

## US Sales Tax on SaaS (State Complexity)

SaaS taxability **varies by state** — some tax as software, some exempt, some data processing rules.

| Pattern | Implication |
|---|---|
| Economic nexus thresholds | ~$100K sales or 200 transactions (state-specific) |
| SaaS vs custom software | Different categories by state |
| Marketplace / reseller | Platform may collect (Stripe Tax, etc.) |

**GTM founder role:** Know that **new enterprise logos in new states** can create filing obligation — not to self-determine rates.

**Typical not guaranteed.** Public guides:

- [Kruze — sales tax for startups](https://kruzeconsulting.com/sales-tax-startups/)
- [a16z — startup accounting/tax overview](https://a16z.com/accounting-and-tax-services-for-startups/) (resource index)

Tools (evaluate with CPA): Stripe Tax, Avalara, TaxJar — automation ≠ advice.

---

## International VAT / GST

| Topic | Founder awareness |
|---|---|
| B2B reverse charge | Often customer accounts for VAT with valid VAT ID |
| B2C digital services | May require MOSS/OSS or local registration |
| UK / EU post-Brexit | Separate UK and EU considerations |

**Handoff:** CPA or firms with SaaS cross-border practice before scaling EU/UK paid ads + self-serve checkout.

---

## R&D Tax Credit (US — High Level)

- Federal **Research Credit** for qualifying wages, supplies, contract research
- Many states add credits
- Startups may offset **payroll tax** (up to limits) when not yet profitable — **IRC rules apply**

**Qualifying work (simplified):** New product/feature development, technical uncertainty, experimentation — **not** pure GTM or routine maintenance.

**Process:** Document projects contemporaneously; CPA prepares Form 6765 / payroll offset elections.

Public: [Kruze — R&D tax credits for startups](https://kruzeconsulting.com/rd-tax-credits-startups/)

---

## QSBS — Qualified Small Business Stock (Exit Angle)

Potential **federal capital gains exclusion** (up to limits, holding period, gross asset tests) for eligible **C-Corp** stock held ≥5 years.

**Founder exit planning:**

- Confirm **C-Corp** from formation (not LLC taxed as partnership for QSBS)
- Asset vs stock sale affects shareholder treatment — **very different**
- **Earn-out** and rollover equity complicate timing — see Pattern 32 cluster

Cross-link: `exiting-company/references/negotiating-earn-out.md` · `saas-outcomes/references/bootstrap-founder-playbook.md` · `references/benchmark-reconciliation.md` (earn-out vs EBITDA).

**Handoff:** Tax counsel before signing LOI — QSBS analysis is fact-specific.

Public: [a16z — QSBS overview for founders](https://a16z.com/qualified-small-business-stock/) (verify current IRC limits with CPA)

---

## 409A Valuations (Equity Comp)

Required for **stock option strike price** (IRC 409A) — independent valuation, typically annually or after material events (raise, major revenue change).

| Provider type | Examples |
|---|---|
| Cap table platforms | [Carta 409A](https://carta.com/409a/) |
| Accounting firms | Kruze, Armanino (often bundled) |

Cross-link: `founder-comp-playbook` · `equity-management` · `gtm-role-descriptions` comp templates.

**Not DIY** for option grants to employees.

---

## Transfer Pricing (International)

If US parent + foreign sub (or reverse): intercompany pricing for IP, services, support.

**Handoff only** — specialized TP advisors; do not set transfer prices from blog posts.

---

## Experts & Resources (Public URLs)

| Name | Focus | Public URL |
|---|---|---|
| **Kruze Consulting** | VC-backed startup CPA, SaaS rev rec, R&D credits, 409A | [kruzeconsulting.com](https://kruzeconsulting.com/) · [SaaS accounting](https://kruzeconsulting.com/startup-accounting/) |
| **Pilot.com** | Bookkeeping + tax for startups | [pilot.com](https://pilot.com/) |
| **Bench** | Bookkeeping for small business | [bench.co](https://www.bench.co/) |
| **Armanino** | SaaS/tech accounting advisory | [armanino.com](https://www.armanino.com/) · [SaaS practice](https://www.armanino.com/industries/technology/saas/) |
| **Moss Adams** | Technology/SaaS accounting | [mossadams.com](https://www.mossadams.com/industries/technology) |
| **Carta** | Cap table, 409A, equity | [carta.com](https://carta.com/) |
| **Ben Murray — SaaS CFO** | Fractional CFO, forecasting | [thesaascfo.com](https://www.thesaascfo.com/) |
| **Tyler Tringas** | Bootstrap accounting sensibility | [tylertringas.com](https://tylertringas.com/) · [Calm Company Fund](https://calmcompanyfund.com/) |
| **Jason Lemkin / SaaStr** | SaaS metrics, efficiency (not tax) | [saastr.com](https://www.saastr.com/) |
| **Meritech** | Public SaaS benchmarks | [meritechcapital.com/benchmarking](https://www.meritechcapital.com/benchmarking) |
| **Bessemer Cloud Atlas** | Metrics definitions | [bvp.com/atlas](https://www.bvp.com/atlas) |
| **a16z** | Startup finance/tax resource hub | [a16z.com/accounting-and-tax-services-for-startups/](https://a16z.com/accounting-and-tax-services-for-startups/) |

Full expert index → `references/experts.md`.

---

## Cross-References

| Topic | Doc |
|---|---|
| Budget & P&L | `references/gtm-budget-playbook.md`, `financial-modeling` |
| MRR / revenue recognition | `references/saas-mrr-accounting-nuances.md` |
| Earn-out / exit tax structure | `exiting-company`, Pattern 32 |
| Founder comp & equity | `founder-comp-playbook` |
| Bootstrap paths | `saas-outcomes`, `solo-founder-gtm` |

---

## Disclaimer

**This document is informational only.** Tax law changes frequently; state and international rules vary. Work with a **licensed CPA, tax attorney, or qualified fractional CFO** for your entity, contracts, and exit. GTM Skills does not provide tax, legal, or accounting services.

# GTM Budget Playbook — Annual Operating Budget for SaaS

**Canonical home:** `financial-modeling` (operating model & P&L).  
**Vendor/tool line detail:** `gtm-spend-management` (Ramp, roster, approvals).  
**Template:** `skills/gtm-ops/gtm-spend-management/templates/annual-gtm-budget-worksheet.md`.

**Audience:** Founders and RevOps building an **annual operating budget** with finance credibility — not a CPA engagement.

---

## Annual OpEx Structure (S&M / R&D / G&A)

Standard SaaS P&L buckets for board and investors:

```
REVENUE (recognized — see saas-mrr-accounting-nuances.md)
COGS (hosting, support, success delivery, payment fees)     → target 70–85% GM
GROSS PROFIT

OPERATING EXPENSES
  S&M  — sales, marketing, GTM tools, events, ads
  R&D  — product/engineering (often largest pre-PMF)
  G&A  — finance, legal, HR, office, corporate SaaS

EBITDA / operating income
```

**Typical private SaaS mix (% of revenue, growth stage — indicative not guaranteed):**

| Stage | S&M | R&D | G&A |
|---|---|---|---|
| Pre-PMF | 40–80% | 50–100% | 15–30% |
| $1–5M ARR | 50–90% | 30–50% | 12–20% |
| $5–20M ARR | 35–55% | 25–35% | 10–15% |
| $20M+ efficient | 25–40% | 20–30% | 8–12% |

Ben Murray (SaaS CFO): model **per-head** where possible; roll up to departments. See `references/experts.md` — Ben Murray.

---

## Bottom-Up vs Top-Down

| Approach | Use | Risk |
|---|---|---|
| **Bottom-up** | Headcount + quota + tool roster + campaign plan | Labor-intensive; trustworthy |
| **Top-down** | "S&M = 45% of revenue" | Fast; hides hiring realism |
| **Hybrid (recommended)** | Bottom-up build, top-down sanity check vs benchmarks | Best for board |

**financial-modeling default:** Bottom-up customers × ACV × churn; headcount by role; tools from vendor register.

**Anti-pattern:** "1% of TAM" top-down revenue with bottom-up headcount — model breaks.

---

## Headcount-Driven Budget (Largest Line Item)

Headcount is typically **60–70% of OpEx** at growth stage.

### Build sequence

1. **Org plan by quarter** — roles, start dates, geo → `gtm-role-descriptions/references/org-by-stage.md`
2. **Fully loaded cost** — base × 1.25–1.35 (benefits, payroll tax, equipment)
3. **Ramp & quota** — AE productivity curve (0% M1 → 100% M5–6) → `financial-modeling`, `revenue-team-onboarding/references/ramp-benchmarks.md`
4. **Comp bands** — `gtm-role-descriptions/references/comp-benchmarks.md`
5. **S&M sub-split** — SDR, AE, SE, CS (pre/post-sales), marketing FTE, RevOps

### GTM headcount vs ARR (directional)

| ARR | AEs | SDRs | CSMs | Marketing | RevOps |
|---|---|---|---|---|---|
| $0–1M | Founder | — | — | 0–1 | 0 |
| $1–3M | 1–3 | 2–4 | 1 | 1–2 | 0–1 |
| $3–10M | 5–10 | 5–10 | 3–5 | 3–6 | 1–2 |
| $10–20M | 10–20 | 10–15 | 5–10 | 6–12 | 2–4 |

Force Management pods at $10M+: group SDR+AE+SE+CSM → `references/force-management-playbook.md`.

**Spend stage caps:** `gtm-spend-management/references/spend-by-stage.md` — don't budget past gates without PMF/GTM Index proof.

---

## Tool & Vendor Budget

**Canonical vendor process:** `gtm-spend-management`.

| Layer | Owner | Artifact |
|---|---|---|
| TCO model | RevOps + finance | `gtm-tool-cost-model` |
| Approvals | Spend matrix | `gtm-spend-management/templates/spend-approval-matrix.md` |
| Roster | RevOps | `gtm-spend-management/templates/vendor-spend-register.md` |
| Control plane | Finance | Ramp / Brex — `gtm-spend-management/references/ramp-playbook.md` |

**Budget line items:**

- CRM, SEP, enrichment, intent, ads, events, contractors
- Per-rep tool allocation (SDR stack vs AE stack)
- Annual renewals in **bill pay** month (cash), amortize in P&L if prepaid

Scott Brinker: consolidate before new MarTech — stack audit in `revops-tech-stack`.

---

## Scenario Planning: Base / Upside / Downside

Build **three internally consistent** scenarios — same structure, different drivers.

| Driver | Downside | Base | Upside |
|---|---|---|---|
| Monthly logo churn | +1 pt vs base | Plan | −0.5 pt |
| New logo MRR | −25% | Plan | +25% |
| AE ramp (months) | +2 | Plan | −1 |
| Hiring delays | +30 days | Plan | On plan |
| ACV | −15% | Plan | +15% |
| Tool spend | Frozen Q2 | Plan | +10% experiments |

**Downside** should stress **runway** — when do you hit 9 months cash?  
**Upside** tests **hiring triggers** — don't hire ahead of proven conversion.

Output: 13-week cash + 12-month P&L per scenario → `financial-modeling/templates/output-template.md`.

---

## Monthly Variance Review Cadence

| Week | Activity | Owner |
|---|---|---|
| **Month close +5 days** | Actual vs budget — revenue, headcount, S&M | Finance + RevOps |
| **Monthly GTM review** | Pipeline, quota, tool spend vs roster | RevOps |
| **Board prep** | Scenario refresh if >10% variance on ARR or burn | CEO + finance |

**Variance buckets:**

1. **Volume** — logos, headcount hires slipped
2. **Rate** — ACV, comp, tool price changes
3. **Mix** — prepay, PS, consumption
4. **Timing** — booking vs recognition

Document **forecast re-baseline** rules: e.g., re-forecast if two consecutive months miss net new ARR by >15%.

Jason Lemkin: never skip bad months in investor updates — pair with recovery plan.

---

## Accounting Stack Timing (Quick Reference)

| ARR / complexity | Typical stack | First finance hire |
|---|---|---|
| Pre-revenue – $500K | QuickBooks Online or Xero + Stripe + Pilot/Bench | Founder + bookkeeper |
| $500K – $3M | QBO/Xero + billing + fractional CFO | Fractional CFO / controller |
| $3M – $15M | QBO → NetSuite evaluation; dedicated controller | Controller + RevOps finance partner |
| $15M+ / multi-entity | NetSuite or equivalent ERP | VP Finance / CFO |

Detail → `financial-modeling` SKILL — accounting stack section · `solo-founder-gtm` bootstrap capital plan.

Chart of accounts basics: separate **subscription revenue**, **PS revenue**, **COGS hosting**, **S&M**, **R&D**, **G&A**; map Ramp categories to GL.

---

## Cross-References

| Topic | Location |
|---|---|
| P&L & runway model | `financial-modeling` |
| Vendor spend governance | `gtm-spend-management` |
| MRR / revenue recognition | `references/saas-mrr-accounting-nuances.md` |
| Bookings vs revenue | `references/bookings-billings-revenue-matrix.md` |
| Tax & R&D credits (awareness) | `references/saas-tax-founder-awareness.md` |
| Benchmark thresholds | `references/benchmark-reconciliation.md` |
| Bootstrap capital | `saas-outcomes/templates/bootstrap-capital-plan.md` |
| Solo founder spend | `solo-founder-gtm/references/spend-by-stage.md` |

---

## Disclaimer

Indicative benchmarks only. Engage **CPA / fractional CFO** for GAAP books, tax, and audit-ready budgets.

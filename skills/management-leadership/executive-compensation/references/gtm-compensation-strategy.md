# GTM Compensation Strategy — Master Playbook

**Canonical home:** `executive-compensation` (strategy + exec gates).  
**IC bands:** `gtm-role-descriptions/references/comp-benchmarks.md` (H1 2026).  
**Founder budget / negotiation:** `founder-comp-playbook`.  
**Reconciliation:** `references/benchmark-reconciliation.md`.

**Audience:** Founders, CROs, RevOps, HR GTM (Stacey Nordwall).  
**Scope:** Revenue team comp **design** — not payroll administration, tax filing, or benefits enrollment.

*Market varies by geo, ACV, and funding stage. Bands are directional US B2B SaaS.*

---

## 1. Compensation Philosophy

GTM comp is a **behavior design system**. Plans that pay the wrong outcomes produce mercenary quarter-end deals, sandbagged forecasts, logo churn, and RevOps fire drills.

### Three anchors

| Anchor | When to use | Risk |
|---|---|---|
| **Pay for performance** | Proven motion; attainment data exists | Unreachable quota → turnover + sandbagging |
| **Market anchor** | Competitive hiring; RepVue/Pave calibration | Overpay without quota discipline |
| **Hybrid** (default) | Most B2B SaaS at scale | Requires annual review + RevOps reporting |

**Canonical hybrid:** Market OTE band + quota at ~5:1 (Bridge Group) + accelerators capped + quality gates (NRR, clawback).

### OTE structure by role

| Role | Typical base/variable | Quota? | Notes |
|---|---|---|---|
| SDR / BDR | 60/40 or 50/50 | Activity → outcome | Pay SQO/meeting held, not dials |
| AE | 50/50 | ARR quota | Clawback 90 days on churn |
| AM / expansion AE | 50/50 or 40/60 | Expansion + renewal | Split credit with CSM documented |
| Player-coach Manager | 50/50 | Team + patch | Override 5–15% on team attainment |
| CSM | 70/30 or 80/20 | NRR / GRR / expansion | Never ticket volume |
| SE | 85/15 or 90/10 | No quota | Technical win rate, POC milestones |
| RevOps | 85/15 or 90/10 | OKRs | Not ARR quota |
| GTM Engineer | 85/15 | OKRs | Align `gtm-engineer-hiring.md` |
| VP Sales / CRO | 50/50–65/35 | Org gates | Pavilion multi-metric variable |

Full band table → `comp-by-role-stage.md` · `comp-benchmarks.md`.

### When quota is fair vs destructive

| Fair quota | Destructive quota |
|---|---|
| ~5:1 quota:OTE; 60–70% of team can hit at plan | >7:1 or <3:1 ratio |
| Based on historical attainment + capacity model | Board top-down with no rep input |
| Ramp credit months 1–3 (25–75%) | Full quota day 1 on inbound SDR |
| Territory fairness (McMahon inspection) | Hero rep hoards accounts |
| Adjusted when ICP/motion changes | Changed mid-quarter without communication |

**Mark Roberge rule:** If you raise OTE, raise quota proportionally — or you overpay for under-delivery.

### Accelerators, decelerators, clawbacks

| Mechanic | Standard | Anti-pattern |
|---|---|---|
| **Linear** | 0–100% attainment = pro-rata variable | Flat payout below 50% (no consequence) |
| **Accelerators** | 1.5× at 100–120%; 2× at 120%+ | Uncapped 3× — bad-fit mega-deals |
| **Decelerators** | Rare; use for pilot plans only | Punitive below 80% on new motion |
| **Clawback** | 90 days logo churn or downgrade | No clawback on annual prepay churn |
| **Draw** | Recoverable months 1–3, first AE only | Permanent draw without recovery |

### SPIFs vs plan changes

| Use SPIF when | Use plan change when |
|---|---|
| 30–90 day campaign (launch, event, blitz) | Motion or ICP shift is permanent |
| Temporary pipeline gap | New consumption or multi-year model |
| Documented in `comp-plan-spiff.md` | Board/RevOps approval + effective date |

**Never** change base commission mid-quarter without written amendment and `employment-compliance` review.

### Expert lenses

| Expert | Lens | Load when |
|---|---|---|
| **Sam Jacobs / Pavilion** | Exec multi-gate variable; Compensation Planning 101 | VP+, annual comp review |
| **Mark Roberge** | Quota:OTE, sales machine economics | First AE, manager layer |
| **John McMahon** | Forecast quality, territory fairness, inspection | Manager + CRO gates |
| **Frank Slootman** | Consumption-aligned comp (Snowflake) | Usage-based revenue |
| **Stacey Nordwall** | Comp communication, ramp handoff | Offer → onboarding |
| **Bridge Group** | IC ratios, ramp benchmarks | SDR/AE plan design |
| **Pave / CaptivateIQ** | Band calibration, comp cycle ops | Annual review tooling |

---

## 2. Role-by-Role Comp Strategies

### SDR

| Model | Structure | Best for |
|---|---|---|
| Meeting-based | $/qualified meeting held | Outbound quality |
| SQO-primary | Meeting + opp-created bonus | CRM-disciplined org |
| Sourced revenue | % of first-year ARR (rare) | High-ACV, long cycle |

**Avoid:** Pure dial volume. **Promotion path:** 12–18 mo to AE — document in JD.

### AE

| Motion | Comp notes |
|---|---|
| New logo | Standard 50/50; quota = OTE × 5 |
| Expansion split | 70/30 new vs expansion quota or overlay AE |
| Multi-year | SPIFF or 1.1× kicker on TCV year 1 |
| Consumption | Trailing 12-mo usage or committed consumption — Slootman pattern |

Consumption examples: Snowflake, Databricks DBU — see `cro-enterprise-strategy.md`.

### Manager

- **Team attainment override:** 5–15% of team variable at 100% team plan
- **Personal patch:** 30–50% IC quota if player-coach
- **Hiring bonus:** One-time for backfill in 45 days — not recurring comp

### CSM

- Variable on **NRR, GRR, or expansion ARR** — not tickets or calls
- **Expansion credit split:** Document % to AE vs CSM in CRM before quarter starts
- Pair with Lincoln Murphy Desired Outcome — not activity health scores alone

### SE

- **No quota** in most models — technical win rate, POC completion, SE-sourced expansion assist
- Bonus pool 10–15% of base tied to qualified technical wins

### GTM Engineer

- **OKR not quota** — workflow throughput, data quality, automation ROI
- Leveling → `gtm-engineer-hiring.md`; bands in `comp-benchmarks.md`

### CRO / VP

- **Company ARR/NRR gates** + board metrics (Rule of 40, EBITDA floor)
- VP pre-$5M: add **system-building milestones** (Lemkin) — hiring, ramp, process adoption
- Full clause library → `executive-clause-library.md`

---

## 3. Stage-Appropriate Comp

| ARR stage | Comp posture | Payroll guardrail |
|---|---|---|
| **$0–$2M** (founder-led) | No premature OTE complexity; founder + maybe 1 AE | 15–25% ARR sales payroll |
| **$2–10M** (first sales hires) | SDR + AE plans; 5:1; draw optional first AE | 20–35% ARR |
| **$10–50M** (pod/manager) | Manager overrides; SPIFs; President's Club | 25–40% ARR |
| **$50M+** (enterprise / consumption) | Multi-year, usage gates, global geo bands | Board-modeled |

**Cross-refs:**
- Spend caps → `gtm-spend-management/references/spend-by-stage.md`
- Hire gates → `solo-founder-gtm/references/scale-readiness-gates.md`
- Band reconciliation → `references/benchmark-reconciliation.md`
- Pod economics → `references/force-management-playbook.md`

### $0–$2M: keep it simple

- Founder sells; **no SDR as first hire** unless inbound overwhelms founder
- First AE: narrow OTE band ($120–150K publish); recoverable draw optional
- Skip accelerators until 3+ AEs with attainment history

### $2–10M: instrument the machine

- Add SDR plan when AE pipeline coverage <3×
- Manager when 2+ AEs at quota (not before)
- RevOps salary + OKR bonus before second comp plan rewrite

### $10–50M: pod and quality gates

- Force Management pod economics — align SDR:AE:CSM comp to pod ARR target
- CSM variable tied to NRR; clawback on downgrade
- VP/CRO → `executive-compensation` Pavilion gates

### $50M+: consumption and global

- CRO variable on usage + NRR + deployment rate (Snowflake pattern)
- Geo bands documented — SF/NYC 1.15–1.25× US base
- International: local counsel for commission law (`employment-compliance`)

---

## 4. Equity & Alternatives

| Topic | Guidance |
|---|---|
| **Commission vs equity (early)** | Seed: equity meaningful; Series A+: cash OTE competitive |
| **Draw / recoverable draw** | First AE only; 3-month recoverable; state in offer |
| **Contractor vs W-2** | SDR/AE/closer → W-2 default; contractors for project RevOps — `employment-compliance`, `legal-gtm-playbook.md` |
| **International (high level)** | Local entity or EOR; commission timing varies; do not US-template globally |

**Exit retention:** Earn-out separate from sales variable — `exiting-company/references/negotiating-earn-out.md`.

---

## 5. Comp Planning Process

### Annual cadence

| Quarter | Activity |
|---|---|
| Q4 | Benchmark refresh (Pavilion, Bridge, Pave, Radford, Carta, Levels.fyi GTM, OpenView) |
| Q4 | Model scenarios in `ote-calculator-template.md` |
| Q1 | Communicate plans; effective date **first day of quarter** |
| Ongoing | Monthly attainment via RevOps; quarterly SPIF review |

### Benchmark sources

| Source | Best for |
|---|---|
| Pavilion (Sam Jacobs) | VP/CRO, peer calibration |
| Bridge Group | IC quota ratios, ramp |
| Betts Comp Engine | GTM role offers |
| RepVue / Compgauge | Candidate perception check |
| Pave / CaptivateIQ | Band ops, annual cycle |
| Radford / Carta | Broad tech comp (validate GTM subset) |
| Levels.fyi | Engineering-adjacent GTM (GTM Engineer) |
| OpenView | SaaS scaling commentary |

### Comp communication

- **Transparent bands in JD** — candidates check RepVue before applying
- **Offer walkthrough:** expected earnings = base + (variable × attainment %)
- **Do not leak:** individual attainment, peer OTE, board gate thresholds
- **Stacey Nordwall:** Manager enablement on "how comp works" in week 1 — `hr-gtm-playbook.md`

### Anti-patterns

1. **Uncapped chaos** — unlimited accelerators on bad-fit logos
2. **Mid-quarter plan change** — destroys trust; use SPIF instead
3. **Sandbagging incentives** — low quotas + high accelerators above 100%
4. **Bookings-only leadership bonus** — pays for junk ARR; add NRR gate
5. **Hidden OTE** — offer decline + RepVue damage

---

## Execution Artifacts

| Artifact | Path |
|---|---|
| Role × stage matrix | `comp-by-role-stage.md` |
| Plan design worksheet | `templates/comp-plan-design-worksheet.md` |
| OTE calculator | `templates/ote-calculator-template.md` |
| IC templates | `gtm-role-descriptions/templates/comp-plan-*.md` |
| Exec package | `templates/executive-offer-package.md` |
| Founder budget | `founder-comp-playbook/references/founder-comp-budget.md` |

**Pattern:** `using-gtm-skills` Pattern 35 (GTM Compensation Strategy)

---
name: executive-compensation
description: >-
  Canonical GTM compensation strategy — philosophy, role-by-role plans, stage-
  appropriate OTE, accelerators, SPIFs, and executive gates. VP/CRO offer clauses,
  variable gates, equity, severance, clawback, and Pavilion-style revenue-quality
  comp. Grounded in Sam Jacobs (Pavilion), Mark Roberge, McMahon, Bridge Group,
  and CRO Council benchmarks. Use when designing comp plans, OTE/quota, annual
  comp review, VP/CRO offers, or board comp approval. Triggers on: "GTM comp
  strategy", "comp plan design", "OTE calculator", "quota design", "executive
  comp", "CRO compensation", "VP Sales offer", "accelerators", "SPIF vs plan
  change", "Pavilion comp", "Sam Jacobs comp", "revenue leader compensation".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.2.0"
  author: LeadMagic
  category: management-leadership
  tags: [executive-comp, gtm-comp, cro, vp-sales, pavilion, ote, quota, equity, severance, clauses]
  related_skills:
    - gtm-role-descriptions
    - founder-comp-playbook
    - gtm-leadership
    - sales-team-building
    - revenue-team-onboarding
    - equity-management
    - employment-compliance
    - financial-modeling
    - board-meeting-prep
    - saas-outcomes
  frameworks:
    - "Sam Jacobs (Pavilion) — Revenue leader community and CRO comp standards"
    - "Pavilion — CRO Council compensation benchmarks"
    - "Bridge Group — SaaS leadership compensation surveys"
    - "Jason Lemkin (SaaStr) — VP Sales hiring and failure modes"
    - "Mark Roberge — Sales Acceleration Formula leadership comp"
    - "Frank Slootman — Unified exec metrics, consumption-aligned sales comp (Snowflake)"
    - "John McMahon — CRO variable tied to forecast quality and productivity per rep"
---

# Executive Compensation

## Overview

**Canonical home for GTM compensation strategy** (IC through CRO). Comp is a
**behavior design system**, not a headline OTE. CRO packages that pay only on
bookings create mercenary quarter-end deals, logo churn, and sandbagged forecasts.
Pavilion's CRO Council — led by **Sam Jacobs** — gates variable comp on **revenue
quality**: net new ARR, NRR, and efficiency (Rule of 40 / EBITDA), not bookings alone.

**Master playbook:** `references/gtm-compensation-strategy.md` (Pattern 35).  
**Role × stage matrix:** `references/comp-by-role-stage.md`.  
**IC bands + templates:** `gtm-role-descriptions` → `comp-benchmarks.md`.  
**Founder budget / negotiation:** `founder-comp-playbook`.  
**Approval conversations:** `gtm-leadership`. **Legal:** `employment-compliance`.  
**HR GTM ramp handoff:** `hr-gtm-playbook.md` (Pattern 28).  
**Reconcile thresholds:** `references/benchmark-reconciliation.md`.

**Not legal or tax advice.** Every clause requires qualified counsel; state law
varies on non-compete, commission timing, and parachute taxes.

## When to Use

- "Design GTM comp plan" / "OTE and quota design"
- "Annual comp review for sales team"
- "Structure CRO compensation"
- "VP Sales offer letter clauses"
- "Executive severance for sales leader"
- "Equity refresh for CRO"
- "Variable gates for VP Sales"
- "Pavilion-style exec comp"
- "Board approval package for revenue leader"

IC plan templates live in `gtm-role-descriptions`; **strategy and worksheets** live here.

## Step-by-Step Process (Full GTM Comp)

### Phase 0: Load Master Playbook

1. `references/gtm-compensation-strategy.md` — philosophy, role strategies, stage gates
2. `references/comp-by-role-stage.md` — matrix by ARR band
3. `skills/founder-led/gtm-role-descriptions/references/comp-benchmarks.md` (via `gtm-role-descriptions`) — H1 2026 bands
4. `templates/comp-plan-design-worksheet.md` — plan design
5. `templates/ote-calculator-template.md` — quota math + scenarios

Founders: run `founder-comp-playbook` payroll % ARR check before publishing bands.

## Authoritative Foundations

- **Sam Jacobs (Pavilion).** Founded Pavilion (Revenue Collective); hosts CRO
  School and publishes revenue-leader comp norms. Emphasis: peer benchmarks,
  efficient growth, and multi-metric executive gates — not hero bookings.
- **Pavilion CRO Council.** Private comp data for CROs at scale; use as
  directional benchmark with Bridge Group public surveys.
- **Bridge Group.** Leadership OTE bands, quota:OTE at org level, ramp expectations.
- **Jason Lemkin.** VP Sales before $2M ARR: ~70% failure; comp must include
  system-building milestones, not only ARR.
- **Mark Roberge.** Tie executive variable to measurable machine outcomes:
  hiring, training, process adoption — not vanity pipeline.
- **Frank Slootman (Snowflake).** Sales exec comp aligned to **consumption**
  when revenue is usage-based — entire exec team on same metric set; eliminate
  siloed MBOs that block cross-functional alignment. See `gtm-leadership/references/cro-enterprise-strategy.md`.
- **John McMahon.** CRO bonus should reflect **forecast certification quality**
  and rep productivity curves — not lone-wolf hero quarters. Board expects
  predictable commits backed by MEDDICC.

## Step-by-Step Process

### Phase 1: Role Band & Mix

| Role | ARR Stage | OTE Band | Base / Variable |
|---|---|---|---|
| VP Sales | $3–15M | $220–350K | 60/40 or 50/50 |
| CRO (growth) | $15–50M | $400–600K | 65/35 |
| CRO (scale) | $50M+ | $500–800K+ | 60/40 |
| VP RevOps | $10M+ | $180–280K | 70/30 (mostly salary) |

Load `references/executive-comp-benchmarks.md` for Pavilion/Bridge alignment.

### Phase 2: Variable Gates (CRO / VP)

**Pavilion-quality gate model:**

| Metric | Weight | Minimum floor | Rationale |
|---|---:|---:|---|
| Net new ARR vs plan | 40–50% | 80% of target | Growth |
| Net revenue retention | 25–30% | 105–110% | Quality |
| Efficiency (Rule of 40 or EBITDA) | 20–25% | Board-defined floor | No junk revenue |
| Team milestones (VP) | 10–20% | Hiring/ramp KPIs | System, not heroics |

**Partial payout:** Document matrix — e.g. 80% ARR + 110% NRR = 85% variable max.

### Phase 3: Clause Library

Load `references/executive-clause-library.md` — full clause set:

- At-will employment and **cause** definition
- Variable calculation, timing, and **clawback** (90-day logo churn)
- **Equity:** grant size, vest, cliff, refresh schedule
- **Change of control:** single vs double-trigger acceleration
- **Severance:** without cause (3–6 mo base + pro-rata bonus)
- **Non-solicit** / **non-compete** (jurisdiction-specific)
- **Recoupment** and **D&O** indemnity
- **280G** parachute gross-up policy (if applicable)
- **Signing bonus** and **relocation**
- **Garden leave** and cooperation post-termination
- **Board reporting** and forecast certification
- **Commission plan** incorporation by reference

Template package: `templates/executive-offer-package.md`

### Phase 4: Equity

| Element | VP Sales | CRO |
|---|---|---|
| Initial grant | 0.25–1.0% FD | 0.5–2.0% FD |
| Vest | 4yr, 1yr cliff | 4yr, 1yr cliff |
| Refresh | Year 2–3 performance | Annual top-up band |
| Exercise window | 90 days post-termination (negotiate) | Same |

Coordinate with `equity-management` and 409A.

### Phase 5: Board Approval Packet

Deliverables for board or comp committee:

1. OTE and gate summary
2. Scenario payout table (50% / 80% / 100% / 120% plan)
3. Equity grant summary cap table impact
4. Severance and change-of-control exposure
5. Comparison to Bridge / Pavilion band (directional)
6. Recruiting context (internal vs external, urgency)

### Phase 6: Negotiation Patterns

| Candidate ask | Response framework |
|---|---|
| Higher base | Trade variable weight or milestone gates |
| Uncapped variable | Cap accelerators; add NRR gate |
| Larger equity | Refresh commitment vs upfront grant |
| Guaranteed first-year payout | Signing bonus separate from variable |
| Shorter cliff | Higher grant or lower base |

## Output Format

- **Executive offer package** (`templates/executive-offer-package.md`)
- **Clause appendix** with marked optional/required clauses
- **Board comp memo** (1–2 pages)
- **Variable payout scenario table**

## Quality Check

- [ ] Variable gated on ≥2 metrics including revenue quality (NRR or efficiency)
- [ ] Cause and severance definitions explicit
- [ ] Clawback on churn/downgrade documented
- [ ] Equity vest, cliff, refresh stated
- [ ] Change-of-control triggers defined
- [ ] Legal review flag on non-compete and commission law
- [ ] VP milestone gates if pre-$5M ARR (Lemkin system-building)

## Common Pitfalls

1. **Bookings-only CRO bonus.** Pays for bad-fit ARR. Fix: NRR + efficiency gates.
2. **No clawback.** Logo churn 60 days post-close. Fix: 90-day ARR clawback.
3. **Hero VP comp.** Single ARR number, no hiring/ramp gates. Fix: 20% system KPIs.
4. **Verbal equity.** Fix: written grant with board approval date.
5. **National non-compete template.** Unenforceable in many states. Fix: counsel.

## Consumption-Model CRO Gates (Snowflake pattern)

When revenue recognizes on **usage** (Snowflake, Databricks DBU, similar):

| Metric | Weight | Notes |
|---|---:|---|
| Consumption / usage vs plan | 30–40% | Primary revenue lever |
| Net new ARR + NRR | 25–35% | Expansion quality |
| Deployment / activation rate | 15–20% | Prevents oversell |
| S&M efficiency / Rule of 40 | 15–20% | Slootman + Meritech board lens |

Do not pay CRO on bookings alone when GAAP revenue trails contracts.

## Execution Artifacts

- `references/gtm-compensation-strategy.md` — **canonical master playbook** (Pattern 35)
- `references/comp-by-role-stage.md` — role × ARR stage matrix
- `templates/comp-plan-design-worksheet.md` — plan design worksheet
- `templates/ote-calculator-template.md` — OTE, quota, accelerator scenarios
- `../gtm-leadership/references/cro-enterprise-strategy.md` — Consumption comp alignment, McMahon board gates (Pattern 31)
- `references/executive-clause-library.md` — full clause text blocks
- `references/executive-comp-benchmarks.md` — Pavilion/Bridge bands
- `references/pavilion-cro-comp.md` — Sam Jacobs / CRO Council patterns
- `templates/executive-offer-package.md` — offer + comp + equity summary
- `templates/board-comp-memo.md` — board approval format
- `references/framework-notes.md`
- `templates/output-template.md`
- `scripts/check-output.py`

**Cross-skill:** CRO variable gates align with `saas-outcomes/references/exit-metrics-matrix.md` (NRR, Rule of 40, burn multiple)

## Related Skills

- `gtm-role-descriptions` — IC comp bands + plan templates
- `founder-comp-playbook` — founder budget, negotiation, offer walkthrough
- `sales-team-building` — hire sequence, POD economics, comp models
- `revenue-team-onboarding` — ramp tables aligned to comp plans
- `gtm-leadership` — comp approval conversations
- `equity-management` — cap table, 409A
- `employment-compliance` — offer legality
- `board-meeting-prep` — comp committee presentation
- `financial-modeling` — scenario modeling for gates

---
name: sales-team-building
description: >-
  Build a B2B sales team from first hire to scale — hiring sequence by ARR
  stage, WbD POD structures, compensation models (linear/accelerated/split),
  draw mechanics, REKS coaching, and WbD GTM Index for scaling readiness. Use
  when planning first sales hire, designing sales org, or scaling a team.
  Triggers on: "build sales team", "first sales hire", "sales org design",
  "sales compensation", "sales POD", "scale sales team", "hire AE", "hire SDR",
  "SDR economics", "Tito Bohrt", or any sales team building request.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.5.0"
  author: LeadMagic
  category: founder-led
  tags: [sales-team, hiring, compensation, org-design, pods, coaching]
  related_skills: [founder-sales, pipeline-management, sales-enablement, gtm-role-descriptions, hiring-by-role, hiring-agencies, solo-founder-gtm, sales-coaching, gtm-system-architecture]
  frameworks:
    - "Mark Roberge — The Sales Acceleration Formula (hiring & training)"
    - "Jason Lemkin & Mark Roberge — From Survival to Thrival (Thrival phase)"
    - "Force Management — Pod Economics & Reporting Structures"
    - "Winning by Design POD Structures"
    - "REKS Coaching"
    - "SaaStr Hiring Triggers"
    - "QuotaSignal AE Mis-Hire Data"
    - "Henry Schuck (ZoomInfo) — High-Velocity SDR Model"
    - "Justin Michael — Sales Borg / TQ (Tech-Powered Sales)"
    - "Ryan Reisert — CRM Activity Buckets & CallBlitz coaching"
    - "Ronen Pessar — ColdCall-Market Fit & Outbound Operators install"
    - "Tom Slocum — The SD Lab SDR coaching"
    - "John McMahon — A-player hiring, manager-before-rep scaling, 6-mo enterprise ramp"
    - "Ron Gabrisko (Databricks) — inside + field hybrid, technical seller profile"
    - "Tito Bohrt (AltiSales) — SDR economics & hiring simulations"
---

# Sales Team Building

## Overview

Sales hiring out of order is the most expensive mistake in SaaS. VP Sales
before $2M ARR: 70% failure rate. SDR as first hire: founder manages a
junior rep while still closing every deal. AE mis-hire cost: $484K over
24 months (QuotaSignal data).

This skill provides the correct sequence, POD design, compensation models,
and coaching framework — all drawn from Winning by Design, SaaStr research,
and operator data.

## When to Use

- "When should I hire my first salesperson?"
- "Build my sales team structure"
- "Design AE compensation"
- "Set up sales PODs"
- "Scale from founder-led to team"
- "What should I pay my reps?"

## Authoritative Foundations

- **Mark Roberge — The Sales Acceleration Formula.** Roberge's hiring scorecard
  selects for five traits over industry tenure: Coachable, Curious, Prior success
  in a similar motion, Intelligent (analytical), and Work ethic. Use this in
  Phase 2 interviews — skills are trainable, traits are not. His training pillar
  drives the 30/60/90 ramp in Phase 6: shadow → supervised → independent, with
  the founder's documented playbook as the curriculum.
- **Jason Lemkin & Mark Roberge — From Survival to Thrival (Thrival Phase).**
  Thrival begins at ~$2M ARR when the founder has closed enough deals to prove
  repeatability. This skill is the Thrival playbook — hiring sequence, POD design,
  compensation, and coaching. Do not load this before `founder-sales` completes
  the Survival phase.
- **Winning by Design POD Structures** — SDR:AE:CSM ratios by product complexity.
  Simple: 2:3:1. Complex: 1:1:1. Early stage: 2:1:1 → 1:2:1 → 1:1:1 scaling.
- **Winning by Design Compensation Models** — Business-case target setting.
  Linear, accelerated, and split comp models. Draw mechanics for onboarding.
  OTE should represent no more than 20% of year-1 ARR quota.
- **Winning by Design REKS** — Results → Efforts → Knowledge → Skills. Four
  diagnostic layers for coaching. Different gaps require different coaching.
- **SaaStr (Jason Lemkin)** — Founder must close 10-20 deals before first hire.
  VP Sales only after $2M ARR with 2 reps at quota.
- **QuotaSignal** — AE mis-hire rate: 40%. Total cost: $484K over 24 months
  (lost ARR + vacancy + replacement ramp). Moving fast saves weeks. Moving
  right saves quarters.
- **Force Management — Pod Economics & Reporting Structures.** Alignment
  cadence (weekly pipeline → monthly GTM scorecard → quarterly territory/quota),
  reporting layers by ARR stage ($1M / $10M / $50M), span of control (6–8 ICs
  per manager), and pod cost ≤35% of ARR at steady-state ramp. See
  `references/force-management-playbook.md` (repo root) for worksheets.
- **Henry Schuck (ZoomInfo) — High-Velocity SDR Model.** Public-operator
  reference for scaling inbound + outbound SDRs with data-driven routing:
  <90-second inbound response, separate inbound/outbound/SWAT SDR motions,
  SDR-as-feeder-system into AE and other functions, and AE dynamic load
  balancing by trailing performance. Load `references/henry-schuck-sdr-model.md`
  when building high-volume inbound or data-product GTM. Earnings metrics →
  `gtm-metrics` → `public-company-gtm-metrics.md`.
- **Justin Michael — *Tech-Powered Sales* (Sales Borg + TQ).** Before scaling
  SDR headcount, raise **technology quotient (TQ)**: SEP superusers can
  outproduce small pods when ICP and messaging are proven. RevOps should
  **orchestrate bots** (enrichment → trigger → SEP → CRM) with 30-day tool
  ramp targets — not 6–9 month SDR tool onboarding. SDR benchmarks from TPS:
  ~200 accounts/month effective load; reply 5–10% min; OAC 1.5–10%; train
  ROUTE/RUIN/MULTIPLY for phone complement.   Canonical playbook →
  `../../outbound/cold-email-strategy/references/justin-michael-sales-borg.md`.
- **Ryan Reisert — CRM Activity Buckets + CallBlitz.** Before scaling phone SDRs,
  implement four contact-level CRM stages and backwards daily workflow. Live call
  coaching via CallBlitz for remote teams. Co-author *Outbound Sales, No Fluff*.
  → `references/ryan-reisert-cold-calling.md`
- **Ronen Pessar — ColdCall-Market Fit (Outbound Operators).** Prove phone motion
  with Call Pilot (50–100 completions) before full SDR bench. Two-phase install:
  validate ROI → recruit + 6-week ramp in ~90 days. Pairs with Gilkey Phone Intent.
  → `references/ronen-pessar-cold-calling.md`
- **Tom Slocum — The SD Lab.** SDR coaching for outbound teams: 3×3 research,
  sell-the-meeting discipline, call block structure. Revenue Rebuild (45 days)
  when outbound lacks clarity before scale. → `references/tom-slocum-cold-calling.md`
- **John McMahon — Enterprise scale hiring.** After Lemkin/Roberge gates pass:
  hire **player-coach managers before rep waves**; target **A players** (methodology
  discipline, peer lift); plan **~6 months** to full enterprise AE productivity.
  Proactive headcount only when pipeline coverage and inspection cadence exist —
  "build the road before the bridge." Reconcile with Lemkin VP timing in
  `benchmark-reconciliation.md`. Canonical → `gtm-leadership/references/cro-enterprise-strategy.md`.
- **Ron Gabrisko (Databricks CRO).** At $2M+ with technical buyers: **inside bullpen**
  for velocity + **field enterprise** for large ACV — run both when profitable.
  Hire sellers who can run POCs, not only demos. Consumption pricing aligns with
  cloud infra buyers. See `cro-enterprise-strategy.md` (Databricks section).
- **Tito Bohrt (AltiSales) — SDR as a science.** Treat sales development as a
  measurable revenue engine: manage **leading indicators** via funnel inversion
  (meetings completed → set → conversations → dials), hold a ~**80–85% show rate**,
  and price the role on **fully-loaded cost per *qualified* meeting** with sales-cycle
  lag — not base salary ÷ dialed meetings (his "Dear CFO" critique). Split **Data
  Research** from **SDR engagement**, hire proven craft + screen with work-simulation
  roleplays, and measure any AI SDR on *incremental* cost per meeting. Load
  `references/tito-bohrt-sdr-science.md` when modeling SDR economics, designing the
  assembly-line org, or rebutting a naive SDR cost model.

## Step-by-Step Process

### Phase 1: WbD GTM Index Self-Assessment

Before hiring, score your GTM maturity 1-10 across: Revenue Model (pricing
clarity), Data Model (CRM hygiene), Math Model (unit economics), Operating
Model (process documentation), Growth Model (channel ROI), GTM Model
(cross-functional alignment).

Score below 6: fix fundamentals before scaling the team. Load
`pipeline-management` to build the Operating Model (stages + SPICED + exit
criteria) and `sales-enablement` for the playbook. Do not hire or engage
agencies (`hiring-agencies`) until Operating Model ≥6. Adding headcount
to a broken system multiplies the damage.

**Scale gates:** Before any hire, pass `solo-founder-gtm/references/scale-readiness-gates.md`.
If `when-not-to-scale.md` stop signals are active — hold hiring 90 days.

### Phase 2: Hiring Sequence by ARR

| Stage | Hire | Role | OTE Range | Trigger |
|---|---|---|---|---|
| Founder-led | None | Founder closes everything | — | Validating the motion |
| $0-500K ARR | Senior AE (1st) | Full-stack: prospect + close | $120-160K | Founder closed 10-20 deals |
| $500K-2M ARR | 2nd AE | Second full-stack AE | $120-180K | 1st AE at quota, founder bottlenecked |
| $500K-2M ARR | SDR (1st) | Feed pipeline to AEs | $58-85K | AEs maxed on capacity, pipeline thin |
| $2M+ ARR | Player-coach Manager | Manage + sell | $170-235K | 2+ reps at quota, process repeatable |
| $5M+ ARR | VP Sales | Scale the org | $240-380K | 5+ reps, $2M+ ARR, proven playbook |
| $500K-2M ARR | GTM Engineer (1st) | Clay, enrichment, routing, signal plays | $95-130K | Founder >10 hrs/wk on Clay; lists delayed |
| $2M+ ARR | Senior GTM Engineer | n8n, loops, stack ownership | $125-165K | Agency spend >$8K/mo; sync jobs break |
| $5M+ ARR, 8+ reps | RevOps / Sales Ops | Forecast, CRM policy, reporting | $95-150K | Data/reporting chaos |
| $5M+ ARR, ramp >6mo | Sales Enablement | Onboarding, training | $100-150K | Onboarding cost justifies dedicated role |

### Phase 3: POD Design (WbD)

POD = SDRs + AEs + CSMs grouped as a team focused on a vertical/segment.

**POD ratios by product complexity:**
- Simple (low-touch, fast cycle): 2 SDR : 3 AE : 1 CSM
- Moderate (standard B2B SaaS): 1 SDR : 2 AE : 1 CSM
- Complex (enterprise, long cycle): 1 SDR : 1 AE : 1 CSM

**Early-stage POD evolution:** 2:1:1 (kick-start) → 1:2:1 (AE leads) →
1:1:1 (full team). Promote SDRs into AE roles as the motion matures.

**POD economics:** Calculate cost per POD vs ARR generated. Target: POD cost
under 35% of ARR generated at 80% ramp.

### Phase 4: Compensation Design

**Canonical strategy:** `executive-compensation/references/gtm-compensation-strategy.md`
(Pattern 35). **Bands:** `gtm-role-descriptions/references/comp-benchmarks.md`.
**Stage matrix:** `executive-compensation/references/comp-by-role-stage.md`.
**Worksheets:** `ote-calculator-template.md`, `comp-plan-design-worksheet.md`.
**Pod economics:** `references/force-management-playbook.md`.

**AE Compensation:**
- 50/50 base/variable standard for early-stage
- OTE ≤ 20% of year-1 ARR quota (OTE $120K → quota $600K)
- Linear model: flat commission rate. Best for predictable volume.
- Accelerated model: higher rate after hitting quota. Drives over-performance.
- Split model: lower per-SQL rate + bonus per closed deal. Drives quality pipeline.

**SDR Compensation:**
- 60/40 or 50/50 base/variable
- Comp on qualified meetings, not activity
- $150-250 per qualified meeting is standard
- Accelerated: bonus for meetings that convert to opportunities

**Draw for onboarding:** First 90 days. Recoverable draw (paid back from future
commissions) or non-recoverable (signing bonus). Standard: guarantee 60-80%
of variable for ramp period.

### Phase 5: REKS Coaching (WbD)

Diagnose before coaching. For each rep:

**Results:** Is the rep hitting quota? If no, dig deeper.
**Efforts:** Is the rep doing the activities that drive results? Calls, emails,
meetings. If no: effort problem. Coach on discipline and prioritization.
**Knowledge:** Does the rep know the product, ICP, and process? If no:
knowledge problem. Train on fundamentals.
**Skills:** Can the rep execute in conversation? Discovery, demo, objection
handling. If no: skill problem. Practice, role-play, call review.

Study top performers to identify what excellence looks like. Coach toward
that standard, not toward the average.

### Phase 6: Ramp Plan (30/60/90 Day)

**Days 1-30:** Learn product, shadow calls, understand ICP, study playbook.
**Days 31-60:** Own pipeline, run discovery independently, first deals under
manager supervision.
**Days 61-90:** Quota-bearing with ramp credit (typical 50–75% quota months 1–3).
Manager reviews deal reviews weekly.

**Full productivity vs 30-60-90:** Day 90 = quota-*bearing* milestone in the plan;
Bridge Group **4.5–6 months** = fully productive vs tenured peer. Reconcile in
`references/benchmark-reconciliation.md` and `revenue-team-onboarding/references/ramp-benchmarks.md`.
HR onboarding system → `gtm-role-descriptions/references/hr-gtm-playbook.md`.

## Output Format

Sales team building plan with: GTM Index self-assessment, hiring sequence
timeline, org chart, POD design, compensation model per role, ramp plan
template, and REKS coaching framework.


## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls

1. **VP Sales before $2M ARR.** 70% failure rate. Cost: $300-500K in comp +
   opportunity cost. VP's job is to scale what works, not discover it.

2. **SDR as first hire.** Founder closes every deal + manages junior rep =
   neither done well. First hire: full-stack AE who prospects AND closes.

3. **No written sales process.** The first AE builds the playbook, not just
   closes deals. If the founder can't document the process, the AE can't
   replicate it.

4. **AE mis-hire.** 40% mis-hire rate, $484K cost over 24 months. Validate
   with a paid project before full-time. Check: can they self-source pipeline?
   Do they have ACV-relevant experience?

5. **Comp complexity.** A compensation plan that fits on one page is 3x more
   likely to drive the right behavior. Show causality: comp tied directly to
   desired outcome.

## Execution Artifacts

- `../../management-leadership/gtm-leadership/references/cro-enterprise-strategy.md` — McMahon hiring/inspection, Snowflake/Databricks GTM models (Pattern 31)
- `references/henry-schuck-sdr-model.md` — ZoomInfo SDR:AE scale, data-lake outbound, feeder system
- `references/tito-bohrt-sdr-science.md` — AltiSales SDR economics (cost per meeting), funnel-inversion benchmarks, assembly-line org, hiring simulations, AI SDR skepticism
- `references/ryan-reisert-cold-calling.md` — CRM Activity Buckets + CallBlitz (repo root)
- `references/ronen-pessar-cold-calling.md` — ColdCall-Market Fit install (repo root)
- `references/tom-slocum-cold-calling.md` — SD Lab SDR coaching (repo root)
- `../../outbound/cold-email-strategy/references/justin-michael-sales-borg.md` — Sales Borg TQ, SDR benchmarks, bot orchestration (canonical)
- `references/framework-notes.md` — Named frameworks and reference tables
- `references/force-management-playbook.md` — Repo root: alignment cadence, reporting structures, pod economics worksheet
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

**Cross-skill artifacts:** `solo-founder-gtm/references/scale-readiness-gates.md`, `solo-founder-gtm/references/when-not-to-scale.md`, `saas-outcomes/references/journey-stage-gates.md`, `gtm-spend-management/references/spend-governance.md`

## Related Skills

- **solo-founder-gtm**: PMF, scale gates, founder-led sales before first hire
- **saas-outcomes**: Journey stage and end-goal alignment
- **gtm-spend-management**: Payroll and tool spend guardrails
- **sales-coaching**: REKS framework and deal review
- **team-management**: Performance management and culture
- **hiring-agencies**: Agency alternative to building in-house
- **gtm-role-descriptions**: GTM Engineer JD + hire triggers (`gtm-engineer-hiring.md`)
- **hiring-by-role**: GTM Engineer interview scorecard

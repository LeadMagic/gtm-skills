---
name: gtm-operations
description: >-
  Build a GTM operations / RevOps function — tech stack architecture, process
  design, data governance, operating cadence, and maturity assessment anchored
  to Gartner and Forrester research. Use when designing or auditing revenue
  operations, sales ops, or GTM infrastructure. Triggers on: "GTM ops",
  "RevOps", "revenue operations", "sales ops", "GTM infrastructure".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.2.0"
  author: LeadMagic
  category: gtm-ops
  tags: [gtm-ops, revops, revenue-operations, sales-ops, process-design, project-management, clickup, raci]
  related_skills: [revops-tech-stack, gtm-tool-cost-model, gtm-spend-management, crm-integration, pipeline-management, gtm-metrics, analytics, campaign-governance, gtm-leadership, revenue-team-onboarding]
  frameworks:
    - "Gartner — Revenue Operations Research (2021-2024)"
    - "Forrester — Revenue Operations Range of Responsibilities Model"
    - "Winning by Design — Revenue Architecture (bowtie funnel)"
    - "DAMA-DMBOK — Data Quality Dimensions"
    - "RevOps Co-op — Project Management in RevOps"
    - "ClickUp — GTM workspace hierarchy (official marketing ops patterns)"
    - "Atlassian Team Playbook — RACI chart"
    - "PMI — RACI matrix responsibility assignment"
    - "Jen Igartua (Go Nimbly) — RevOps as product, automation maturity, agentic GTM"
---

# GTM Operations

## Overview

Most failed RevOps builds share one failure mode: the function is stood up as
an org-chart change rather than an operational integration. Gartner's
definition is precise — RevOps is a coalition of GTM stakeholders whose
individual functions stay separate but whose operations (data, process, KPIs)
are integrated across sales, marketing, and customer success. The mistake this
skill prevents is treating RevOps as a re-org when it is an infrastructure
build.

Gartner's outcome data makes the case: companies at advanced RevOps maturity
are 2× as likely to exceed revenue goals and 2.3× as likely to exceed profit
goals compared to companies at developing or intermediate maturity. By 2024,
75% of the highest-growth companies had deployed a RevOps model, up from fewer
than 30% in 2021. Centralized RevOps grew from 15% to 40% of B2B organizations
between Forrester's 2019 and 2021 surveys.

## When to Use

- "Set up RevOps"
- "Build GTM operations"
- "Sales ops foundation"
- "GTM infrastructure"
- "Revenue operations setup"
- "Assess our RevOps maturity"
- "GTM project management"
- "ClickUp for RevOps"
- "RACI for campaign launch"
- "Organize GTM docs and tasks"

## Authoritative Foundations

- **Gartner — Revenue Operations Research (2021-2024).** Defines RevOps as
  operational integration (not re-org) of data, process, and KPIs across GTM
  functions. Provides the developing→intermediate→advanced maturity vocabulary
  used in Phase 1, the 2×/2.3× outcome multipliers that anchor the business
  case, and the 75% adoption prediction among highest-growth companies. Also
  supplies the consolidation-first guidance: inventory and eliminate redundant
  tooling before adding headcount.
- **Forrester — Revenue Operations Range of Responsibilities Model.** Maps
  alignment areas across marketing ops, sales ops, partner ops, and CS ops
  into a unified responsibility model. Forrester's caution — centralization
  fails when individual functions feel deprioritized, so the operating cadence
  in Phase 4 balances org-level KPIs and functional-level reporting. Relevant
  stat: centralized RevOps grew from 15% to 40% of B2B organizations between
  Forrester's 2019 and 2021 surveys; centers of excellence grew from 18% to 37%.
- **Winning by Design — Revenue Architecture.** Introduces the bowtie funnel —
  a recurring-revenue operating model extending the classic sales funnel past
  close through retention and expansion. The six core GTM processes in Phase 2
  map directly to bowtie stages. See `references/framework-notes.md` for the
  full process-to-bowtie stage mapping.
- **DAMA-DMBOK — Data Quality Dimensions.** The six named dimensions —
  completeness, uniqueness, timeliness, validity, accuracy, consistency —
  replace vague "data cleanliness" language in Phase 3. Each CRM field
  governance rule maps to one or more DAMA dimensions so quality requirements
  are measurable, not subjective. See `references/framework-notes.md` for the
  full dimension checklist applied to CRM data.
- **RevOps Co-op — Project Management in RevOps.** Practitioner guidance on
  intake (Slack → formal queue), ruthless prioritization, and lightweight
  roadmaps when RevOps is both builder and PM. See
  `references/gtm-project-management-playbook.md`.
- **ClickUp — GTM workspace hierarchy.** ClickUp's marketing team and help
  center document Space → Folder → List patterns for launches, requests, and
  templates. See `references/clickup-gtm-workspace.md` — practitioner patterns,
  not admin manual.
- **Atlassian / PMI — RACI.** Standard R/A/C/I definitions with the GTM rule:
  exactly one Accountable per deliverable. Filled examples in
  `templates/raci-matrix-template.md`. Campaign-specific RACI → `campaign-governance`.

## Step-by-Step Process

### Phase 1: Maturity Assessment

Before building, measure where you are using Gartner's three maturity stages:

| Stage | Signals | Outcome expectation |
|---|---|---|
| **Developing** | Spreadsheets, tribal knowledge, no shared KPIs | Baseline |
| **Intermediate** | CRM configured, processes documented, RevOps team of 1-2 | Moving toward aligned reporting |
| **Advanced** | Processes enforced in systems, predictive analytics, RevOps as strategic partner | 2× revenue goal attainment; 2.3× profit goal attainment (Gartner) |

The gap from developing to intermediate is a data and process problem. The gap
from intermediate to advanced is a systems-enforcement and analytics problem.
Build toward advanced incrementally — skipping intermediate produces a
fragile stack.

### Phase 2: Process Design (Bowtie-Mapped)

Document the six core GTM processes. Each maps to a Winning by Design bowtie
stage so the process owner can trace every handoff to a revenue outcome:

1. **Lead-to-Account** (pre-acquisition stage): How a lead becomes an account
   in CRM. Deduplication rules, company hierarchy, account ownership. SLA:
   matched within 24 hours of creation.
2. **Lead Routing** (acquisition stage): Round-robin vs territory vs
   account-based routing. Speed-to-lead targets by source. Unrouted lead SLA:
   4 business hours.
3. **Opportunity Management** (close stage): Stage definitions with entry and
   exit criteria. Required fields per stage. Forecasting categories. No stage
   advancement without required data in CRM.
4. **Quote-to-Cash** (close stage): CPQ, pricing approval thresholds, contract
   generation, billing setup. Discount above threshold requires manager
   approval logged in CRM.
5. **Customer Handoff** (onboard stage): AE → CSM transition checklist.
   Required documentation, kickoff call template, success plan. Handoff SLA:
   5 business days from close.
6. **Data Governance** (all stages): Field definitions, required fields,
   validation rules, duplicate detection, enrichment automation. Use
   DAMA-DMBOK dimensions as the quality rubric (see Phase 3).

### Phase 3: Data Model and Governance

**Core CRM objects:** Lead, Contact, Account, Opportunity.

**Data quality per DAMA-DMBOK — six dimensions applied to CRM:**

- **Completeness:** Required fields enforced at each stage gate; no null
  company name, email, or owner on active records.
- **Uniqueness:** Duplicate detection on email domain + company name; merge
  policy documented and enforced by a named owner.
- **Timeliness:** Enrichment runs within 48 hours of record creation; stale
  records (90+ days no activity) flagged in a hygiene dashboard.
- **Validity:** Picklists for all critical dimensions (stage, lead source, loss
  reason) — no free-text fields in key reporting columns.
- **Accuracy:** Enrichment provider cross-checks CRM-entered data; discrepancies
  flagged for human review, not auto-overwritten.
- **Consistency:** Naming conventions enforced for campaigns, accounts, and
  territories via CRM validation rules.

See `references/framework-notes.md` for the full DAMA-DMBOK checklist with
per-field governance assignments.

### Phase 4: Operating Cadence

| Cadence | Audience | Purpose |
|---|---|---|
| Daily | Reps + SDRs | Pipeline dashboard, open tasks, dial metrics |
| Weekly | Manager + reps | Pipeline review; forecast call (leadership) |
| Monthly | RevOps + leadership | QBR prep, territory review, compensation |
| Quarterly | All GTM | Full QBR, territory planning, quota setting, tool audit |

Forrester's warning: quarterly targets must not crowd out longer-horizon
investments. Each monthly review should include both a tactical metrics block
and a capability roadmap update.

### Phase 5: Tech Stack by ARR Stage

| ARR | CRM | Enrichment | Sequencing | Analytics |
|---|---|---|---|---|
| <$1M | HubSpot (free) or Attio | LeadMagic, Apollo | Smartlead or Instantly | GA + CRM reports |
| $1–5M | HubSpot (paid) or Salesforce | LeadMagic + Clay waterfall | Outreach or Salesloft | CRM dashboards + Gong |
| $5M+ | Salesforce | Clay waterfall + enrichment ops | Outreach/Salesloft | Data warehouse + BI + Clari |

Full stack design and audit process: see `revops-tech-stack` skill.

### Phase 6: GTM Project Management (Canonical Home)

Load `references/gtm-project-management-playbook.md` for full detail.

**Project types:** campaign launch, tool rollout, QBR prep, onboarding cohort,
vendor evaluation. Default to **lightweight PM** (<$20M ARR): one-page charter,
weekly 15-min standup, 3–5 milestones. Heavyweight when compliance or CRM
replacement demands phase gates.

**Status cadence:**
- Weekly: four questions (shipped, blocked, due, scope change) — async Slack OK
- Monthly: portfolio review — max ~5 active projects per RevOps FTE
- Milestones: On track / At risk / Blocked / Done (with dates)

**Organizing work:** SSOT per layer — tasks in PM tool, playbooks in docs, records
in CRM, metrics in dashboards. See `references/gtm-organization-principles.md`.
Naming for campaigns links to `campaign-governance` (no duplicate UTM spec).

**ClickUp (if PM tool):** GTM Operations Space with Launches, RevOps Projects,
Requests, and Cadence Folders; Process Library for templates. Board for launches,
Gantt for migrations. See `references/clickup-gtm-workspace.md`.

**Team design on projects:** DRI, launch pod, span of control →
`references/team-design-gtm-projects.md` + `references/force-management-playbook.md`.

**RACI:** Charter + matrix before kickoff. Templates:
`templates/gtm-project-charter.md`, `templates/raci-matrix-template.md`.

## Output Format

GTM Ops blueprint containing: maturity assessment (developing/intermediate/
advanced with evidence and gap analysis), six-process documentation with
bowtie-stage mappings and SLAs, CRM data model with per-field DAMA-DMBOK
dimension governance assignments, tech-stack recommendation by ARR stage,
operating cadence calendar with audience and KPI assignments, and (when
requested) GTM project package — charter, RACI matrix, milestone tracker,
ClickUp/workspace map. Each process document names the responsible owner and
required CRM fields at each gate.

## Quality Check

Before delivering, verify:
- [ ] Maturity stage assessed from evidence (systems, processes, reporting), not assumed
- [ ] All six bowtie-mapped processes documented with entry/exit criteria and SLAs
- [ ] Every CRM field governance rule references a named DAMA-DMBOK dimension
- [ ] Tech stack scoped to the company's current ARR stage, not aspirational
- [ ] Operating cadence assigns a named owner to every meeting type and KPI
- [ ] No "data is somewhat clean" language — quality is defined by named DAMA dimensions with measurable thresholds
- [ ] GTM projects have one DRI, one Accountable per RACI row, and linked charter
- [ ] Campaign naming/UTM work routes to `campaign-governance`, not parallel conventions

## Common Pitfalls

1. **Treating RevOps as a re-org.** Moving people under a new title without
   integrating data, processes, and KPIs produces an org chart change, not a
   RevOps function. Fix: per Gartner's definition, build integration of
   data/process/KPIs first — the structure follows from that.
2. **Vague data quality standards.** "Data is somewhat clean" is unmeasurable
   and cannot be improved. Fix: map every quality requirement to a DAMA-DMBOK
   dimension (completeness, uniqueness, timeliness, validity, accuracy,
   consistency) with a specific threshold and enforcement mechanism.
3. **Processes documented but not enforced.** Stage definitions exist in a
   Google Doc but CRM has no validation rules, so reps skip required fields.
   Fix: encode every process gate in CRM validation rules so the system
   prevents invalid stage changes.
4. **Sacrificing long-term capability investment for quarterly targets.**
   Forrester's warning: centralized RevOps fails when individual functions feel
   deprioritized. Fix: separate quarterly tactical metrics from a 12-month
   capability roadmap; both must be visible to leadership at every monthly
   review.
5. **Projects without RACI or DRI.** "Everyone's helping" on a launch until
   UTMs are wrong and nobody owns CRM. Fix: charter + RACI before build;
   RevOps Accountable on attribution rows.
6. **PM tool sprawl.** Tasks in Slack, docs in Drive, status in email. Fix:
   SSOT layers in `gtm-organization-principles.md`; one ClickUp List per
   active project.

## GTM Ops skill router

Full index: `references/gtm-ops-skill-index.md` — stack, TCO, Ramp, CRM, governance.

**Customer data in the GTM stack:** RevOps defines which systems may hold
customer/prospect data and approved exchange paths — see
`references/gtm-data-exchange-playbook.md` and `revops-tech-stack` Phase 4b.

## Execution Artifacts

- `references/framework-notes.md` — Gartner/Forrester/WbD notes
- `templates/output-template.md` — Deliverable shell
- `scripts/check-output.py`
- `references/gtm-ops-skill-index.md` — Ops skill router
- `references/gtm-data-exchange-playbook.md` — Customer data exchange SOP (repo root)
- `references/gtm-project-management-playbook.md` — **Canonical PM home** (cadence, milestones, project types)
- `references/clickup-gtm-workspace.md` — Space → Folder → List for GTM teams
- `references/gtm-organization-principles.md` — SSOT, docs/tasks/data/dashboards IA
- `references/team-design-gtm-projects.md` — DRI, launch pods, span of control
- `references/gtm-automation-expert-playbook.md` — Jen Igartua RevOps automation maturity (repo root; Pattern 30)
- `templates/gtm-project-charter.md` — One-page charter
- `templates/raci-matrix-template.md` — RACI + filled GTM examples
- `templates/revops-maturity-assessment.md` — Maturity scorecard
- `templates/operating-cadence-calendar.md` — Meeting rhythm

## Related Skills

- revops-tech-stack, gtm-tool-cost-model, gtm-spend-management, crm-integration, pipeline-management, gtm-metrics, analytics, campaign-governance, gtm-leadership, revenue-team-onboarding

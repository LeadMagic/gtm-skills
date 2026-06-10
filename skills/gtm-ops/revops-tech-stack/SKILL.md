---
name: revops-tech-stack
description: >-
  Design, audit, and consolidate the RevOps technology stack — CRM, enrichment,
  sequencing, analytics, integration architecture, and cost optimization.
  Use when auditing GTM tools, designing revenue technology, or consolidating
  vendor spend. Triggers on: "RevOps stack", "sales tech stack", "GTM tool
  audit", "revenue technology", "stack consolidation".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.2.0"
  author: LeadMagic
  category: gtm-ops
  tags: [gtm-ops, revops, tech-stack, tools, audit, integration, consolidation, project-management]
  related_skills: [gtm-operations, gtm-tool-cost-model, gtm-spend-management, crm-integration, campaign-governance, analytics, gtm-role-descriptions, clay-toolkit, n8n-automation, deal-desk, customer-onboarding, revenue-team-onboarding, data-privacy-compliance, website-visitor-identification, inbound-triage, 1p-tagging-pixels]
  frameworks:
    - "Scott Brinker — MarTech Landscape (chiefmartec.com, 2025)"
    - "Gartner — Revenue Operations Research"
    - "Forrester Decisions — Revenue Operations"
    - "Winning by Design — Revenue Architecture (bowtie funnel)"
    - "RevOps Co-op — RevOps project manager hiring guide"
    - "Atlassian Team Playbook — RACI chart"
---

# RevOps Tech Stack Design

## Overview

Scott Brinker's annual MarTech Landscape has tracked vendor count from roughly
150 in 2011 to more than 15,000 by 2025 — a 100× proliferation that puts every
B2B company under constant pressure to add tools, not consolidate them. The
average B2B company uses 15+ GTM tools; most are underutilized or redundant.
This skill prevents the most expensive outcome of tool sprawl: a stack where
every tool functions in isolation and the revenue motion is unmeasurable because
data lives in a dozen disconnected places.

The design principle, from Winning by Design's Revenue Architecture, is that
every tool in the stack must instrument a stage of the bowtie funnel —
acquisition, activation, close, onboard, expand, renew. Tools that cannot be
mapped to a documented process stage are candidates for elimination. Gartner's
guidance for advanced-maturity RevOps teams includes inventorying all sales,
marketing, and CS technology and eliminating redundant tooling as step one of
any ops improvement program.

## When to Use

- "Audit our GTM tech stack"
- "Design RevOps stack"
- "Sales tool consolidation"
- "GTM tool budget review"
- "Stack cost optimization"
- "Revenue technology architecture"
- "Approve new GTM tool purchase"
- "Ramp / vendor spend governance"

## Authoritative Foundations

- **Scott Brinker — MarTech Landscape (chiefmartec.com, 2025).** The named
  justification for why consolidation discipline is a structural problem, not a
  one-time cleanup. 15,000+ vendors in 2025 means the default answer for any
  GTM need is "there's a tool for that." The audit in Phase 1 applies Brinker's
  consolidation logic: inventory and score on utilization and overlap before
  evaluating any new vendor.
- **Gartner — Revenue Operations Research.** Gartner's maturity guidance for
  RevOps includes: inventory all GTM tech as step one; eliminate redundant
  tooling before adding headcount; every retained tool needs a documented
  process owner and integration path to the CRM. Advanced-maturity RevOps teams
  are 2× more likely to exceed revenue goals — tech rationalization is one of
  the measurable components separating advanced from intermediate maturity.
- **Forrester Decisions — Revenue Operations.** "Deliver value through revenue
  technology" is a named priority in Forrester's RevOps responsibility model.
  Forrester's caution: revenue tech decisions must trace to the operating model,
  not tool fashion. Phase 3's target-state design enforces this by requiring
  every tool to map to a bowtie stage before it earns a place in the target
  architecture.
- **Winning by Design — Revenue Architecture.** The bowtie funnel —
  acquisition, activation, close, onboard, expand, renew — is the operating
  model the stack exists to instrument. Each bowtie stage gets exactly one
  category-owner tool in the target state; tools without a bowtie-stage
  assignment are cut.

## Step-by-Step Process

### Phase 1: Stack Audit

Inventory every tool in the GTM motion. For each tool, record:

| Field | Description |
|---|---|
| Tool name | Vendor + product name |
| Category | CRM, enrichment, sequencing, CI, forecasting, etc. |
| Annual cost | Full contract value |
| Owner | Named individual responsible for the tool |
| Monthly active users | Unique users in last 30 days |
| Utilization % | MAU ÷ total licensed seats |
| CRM integration | Yes / No / Partial |
| Bowtie stage | Which funnel stage the tool instruments |
| Renewal date | Contract renewal month |

Categories to audit: CRM, enrichment, **visitor identification / intent**
(company vs person deanonymization), sequencing, conversation intelligence,
forecasting, compensation, territory planning, ABM platform, chat/scheduling,
content management, analytics/BI, data warehouse, iPaaS/integration, partner
management, project management.

**Visitor ID category owner:** Load `website-visitor-identification/references/visitor-id-vendor-comparison.md`.
Consolidation rule: one **company-ID** vendor (Clearbit/Breeze, Leadfeeder, 6sense,
Demandbase) + at most one **person-ID** vendor (RB2B, Warmly, Koala) until pilot
proves ROI. Person-level tools require privacy checklist
(`visitor-id-privacy-gtm.md`) before stack approval.

Full audit scorecard template: see `references/framework-notes.md`.

### Phase 2: Consolidation Analysis

Score each tool on five dimensions to build a keep/consolidate/cut
recommendation:

- **Utilization:** MAU ÷ licensed seats. Below 50% is a consolidation signal.
- **Overlap:** Two or more tools in the same category without documented
  differentiation is a red flag.
- **Integration:** No CRM integration means data lives outside the single
  source of truth — a structural liability.
- **Cost per active user:** Annual cost ÷ MAU. Above $200/month/user without
  documented ROI is a cut signal.
- **Switching cost:** Deeply integrated tools (Salesforce, Outreach) cost
  3-6 months to replace; point solutions (Calendly) cost one week.

Consolidation target: 15-25% reduction in GTM tool spend, computed from the
actual audit numbers — not asserted before the audit is run. See
`references/framework-notes.md` for the consolidation decision matrix and
category-owner table.

### Phase 3: Target-State Architecture by ARR

Every retained tool maps to exactly one bowtie stage. Each category has exactly
one owner tool in the target state.

**< $1M ARR — Minimum viable stack:**
- CRM: HubSpot (free) or Attio
- Enrichment: LeadMagic, Apollo
- Sequencing: Smartlead or Instantly
- Analytics: Google Analytics + CRM reports
- Calendar/booking: Calendly

**$1–5M ARR — Scaled stack:**
- CRM: HubSpot (paid) or Salesforce Essentials
- Enrichment: LeadMagic + Clay waterfall
- Sequencing: Outreach or Salesloft
- Conversation intelligence: Gong or Chorus
- Analytics/BI: CRM dashboards + Looker or Metabase
- iPaaS: n8n or Zapier for custom integrations

**$5M+ ARR — Full RevOps stack:**
- CRM: Salesforce
- Enrichment: Clay waterfall + dedicated enrichment ops
- Sequencing: Outreach or Salesloft
- Conversation intelligence: Gong
- Forecasting: Clari or BoostUp
- Territory/compensation: Fullcast, CaptivateIQ, or Spiff
- Data warehouse: Snowflake or BigQuery + dbt
- BI: Looker or Tableau

### Phase 4: Integration Architecture

The CRM is the single source of truth. Every data flow reads from or writes to
the CRM; no closed loops between non-CRM tools.

- **Enrichment → CRM:** Clean, enriched records flow automatically within
  48 hours of creation.
- **CRM → Sequencing:** Accounts and contacts assigned to sequences carry CRM
  context (stage, persona, industry).
- **Sequencing → CRM:** Activity logged back — emails sent, calls made, replies
  received, meetings booked.
- **CRM → Analytics:** Pipeline and activity data feeds the BI layer.
- **iPaaS layer:** Bridges tools without native CRM connectors; every
  integration has a named owner and a documented data contract (source,
  destination, field mapping, sync frequency).

### Phase 4b: Customer & Prospect Data Boundaries (GTM)

RevOps owns **where customer and prospect data may live** in the stack — not
encryption design.

| Rule | Why |
|---|---|
| CRM is system of record for GTM-sourced contacts | Sequencers and enrichment are spokes |
| No customer PII in outbound tools beyond lawful prospecting fields | Sequences are not file shares |
| Bulk exports require owner + retention date | Audit trail for enterprise buyers |
| Enrichment credits gated per role | Prevents shadow list hoarding |

When sales or CS exchanges files with customers (imports, POC data), route
through `references/gtm-data-exchange-playbook.md` — not ad hoc Slack/email.
Checklist → `deal-desk/templates/customer-data-exchange-checklist.md`.
Rep hygiene → `references/gtm-security-hygiene-basics.md`.

### Phase 4c: Stack Migration & Rollout Projects

Tool changes are GTM projects — not side quests between tickets.

1. **Charter** — `gtm-operations` → `skills/gtm-ops/gtm-operations/templates/gtm-project-charter.md`
2. **RACI** — `skills/gtm-ops/gtm-operations/templates/raci-matrix-template.md` Example 2 (CRM Migration) or
   Example 4 (Vendor Evaluation); RevOps Lead **Accountable** on mapping,
   integrations, and cutover
3. **Milestones** — audit complete → sandbox UAT → training → cutover → day-30 adoption
4. **PM tool** — ClickUp RevOps Projects Folder + Gantt (`clickup-gtm-workspace.md`)
5. **Spend** — `gtm-spend-management` approval before POC contracts

Do not add vendors from Phase 1 without a named project DRI and bowtie-stage owner.

### Phase 5: Cost Optimization

- **Consolidation:** Replace 3-4 overlapping point solutions with one platform.
  HubSpot's paid tiers can replace 5-7 point solutions at $1-5M ARR.
- **License audit:** Remove departed-employee seats; downgrade active-but-not-
  admin seats to viewer/read-only.
- **Contract negotiation:** Multi-year commits typically produce 20-30%
  discounts; ramp pricing (lower year one, scales with usage) protects early
  runway.
- **Savings baseline:** Compute 15-25% savings from audit actuals (cost per
  active user × redundant or unused seats) — commit to a target only after the
  audit data supports it.

## Output Format

RevOps stack blueprint containing: full audit inventory with utilization
percentages and bowtie-stage assignments, consolidation analysis with
keep/consolidate/cut recommendations and a computed savings estimate, target-
state architecture by ARR stage with one category-owner tool per bowtie stage,
integration architecture with named data owners and directional data-flow
contracts, and cost-optimization plan with negotiation levers and a
baseline-derived savings range. See `references/framework-notes.md` for the
audit scorecard template and category-owner matrix.

## Quality Check

Before delivering, verify:
- [ ] Every retained tool has a documented bowtie-stage assignment — no tool without a process home
- [ ] Each category has exactly one owner tool in the target-state architecture
- [ ] Utilization is measured from actual MAU data, not self-reported or assumed
- [ ] Consolidation savings estimate is derived from audit actuals, not asserted upfront
- [ ] Every integration has a named data owner and a documented direction (source → destination)
- [ ] Stack is scoped to the company's current ARR stage, not aspirational tooling

## Common Pitfalls

1. **Adding tools before auditing existing ones.** With 15,000+ vendors
   (Brinker 2025), the default GTM motion is "there's a tool for that." Fix:
   run the Phase 1 audit before evaluating any new vendor; close a tool before
   opening one.
2. **Tool decisions driven by tool fashion, not operating model.** Forrester's
   warning: revenue tech that doesn't trace to the operating model creates data
   fragmentation. Fix: every tool in Phase 3 must map to a bowtie stage; if
   you cannot name the stage, the tool does not belong in the stack.
3. **CRM disconnected from the integration hub.** Data that lives only in
   sequencing or enrichment tools is invisible to leadership. Fix: enforce the
   hub-and-spoke model in Phase 4 — every tool either pushes to or pulls from
   CRM; no closed loops outside the CRM.
4. **Asserting savings targets before running the audit.** "We'll save 20%"
   stated before utilization is measured is fiction. Fix: compute the savings
   figure from Phase 2 audit actuals; commit to a target only once the data
   supports it.

## Execution Artifacts

- `references/framework-notes.md` — Audit scorecard, consolidation matrix, savings math
- `website-visitor-identification/references/visitor-id-vendor-comparison.md` — Intent/deanonymization vendors
- `website-visitor-identification/templates/visitor-id-vendor-eval-scorecard.md` — Pilot scorecard
- `references/gtm-data-exchange-playbook.md` — Customer data exchange SOP (repo root)
- `gtm-operations/templates/raci-matrix-template.md` — Migration + vendor eval RACI (Examples 2, 4)
- `gtm-operations/templates/gtm-project-charter.md` — Rollout charter
- `gtm-operations/references/gtm-project-management-playbook.md` — Tool rollout milestones
- `templates/stack-audit-scorecard.md` — Tool inventory worksheet
- `templates/target-state-architecture.md` — Category-owner target stack
- `templates/output-template.md` — Deliverable shell
- `scripts/check-output.py`

## Related Skills

- gtm-operations, gtm-tool-cost-model, gtm-spend-management, crm-integration, campaign-governance, analytics
- website-visitor-identification — canonical visitor ID / intent vendor selection
- deal-desk, customer-onboarding — customer data exchange at sale and onboarding
- revenue-team-onboarding — rep access and hygiene gates
- gtm-role-descriptions — GTM Engineer vs RevOps ownership (`gtm-engineer-hiring.md`)
- clay-toolkit, n8n-automation — skills to test in GTM Engineer interviews

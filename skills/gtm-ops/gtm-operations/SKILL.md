---
name: gtm-operations
description: >-
  Build GTM operations function — tech stack architecture, process design, data
  governance, RevOps foundations. Triggers on: "GTM ops", "RevOps", "revenue
  operations", "sales ops", "GTM infrastructure".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: gtm-ops
  tags: [gtm-ops, revops, revenue-operations, sales-ops, process-design]
  frameworks: [WbD Revenue Architecture, RevOps Maturity Model]
---

# GTM Operations

## Overview
GTM Ops (or RevOps) is the infrastructure layer that makes the GTM motion
repeatable, measurable, and scalable. Without it, you're flying blind.
This skill covers building the ops function from scratch — tech stack, process
design, data governance, and operating cadence.

## Frameworks Referenced

This skill is grounded in named GTM frameworks and operator methodologies, not generic advice:

- **WbD Revenue Architecture** — used as the named operating framework for this playbook.
- **RevOps Maturity Model** — used as the named operating framework for this playbook.

## When to Use
- "Set up RevOps"
- "Build GTM operations"
- "Sales ops foundation"
- "GTM infrastructure"
- "Revenue operations setup"

## Step-by-Step Process

### Phase 1: GTM Tech Stack Architecture
The minimum stack by stage:

**<$1M ARR:**
- CRM: HubSpot (free) or Attio
- Enrichment: LeadMagic, Apollo
- Sequencing: Smartlead or Instantly
- Analytics: Google Analytics + basic CRM reports
- Communication: Slack, Google Workspace

**$1-5M ARR:**
- CRM: HubSpot (paid) or Salesforce (essential)
- Enrichment: LeadMagic + Clay for waterfall
- Sequencing: Outreach or Salesloft
- Analytics: CRM dashboards + basic BI
- Conversation intelligence: Gong or Chorus
- Data warehouse: Basic pipeline data model

**$5M+ ARR:**
- CRM: Salesforce
- Full RevOps stack: enrichment, sequencing, CI, forecasting, compensation,
  territory planning, data warehouse, BI tool
- Dedicated RevOps hire

### Phase 2: Process Design
Document the 6 core GTM processes:
1. **Lead to Account:** How a lead becomes an account in CRM. Deduplication rules,
   company hierarchy, account ownership.
2. **Lead Routing:** Round-robin vs territory vs account-based. SLAs by lead source.
   Speed-to-lead targets.
3. **Opportunity Management:** Stage definitions with entry/exit criteria. Required
   fields per stage. Forecasting categories.
4. **Quote to Cash:** CPQ, pricing approvals, discount thresholds, contract
   generation, billing setup.
5. **Customer Handoff:** AE → CSM transition. Required documentation, kickoff call
   template, success plan creation.
6. **Data Governance:** Field definitions, required fields, validation rules,
   data quality dashboards, duplicate management.

### Phase 3: Data Model Design
- **Core objects:** Lead, Contact, Account, Opportunity
- **Relationships:** Lead → Contact → Account. Opportunity → Contact Roles.
  Account → Parent Account (hierarchy).
- **Key fields per object:** Define the 10-15 fields that matter most. Everything
  else is noise.
- **Picklists:** Standardized values. No free-text fields for critical dimensions
  (stage, lead source, loss reason).
- **Data quality rules:** Required fields per stage, validation on critical fields,
  duplicate detection rules, data enrichment automation.

### Phase 4: Operating Cadence
- **Daily:** Rep dashboard review, SDR dial metrics
- **Weekly:** Pipeline review (manager + rep), forecast call (leadership)
- **Monthly:** QBR prep, territory review, compensation review
- **Quarterly:** Full QBR, territory planning, quota setting, tool audit

### Phase 5: Operations Maturity Model
- **Level 1 (Ad-hoc):** Spreadsheets, no process, tribal knowledge
- **Level 2 (Defined):** CRM configured, basic processes documented, data is
  somewhat clean
- **Level 3 (Managed):** Processes enforced in CRM, dashboards used for decisions,
  RevOps team of 1-2
- **Level 4 (Optimized):** Predictive analytics, automated workflows, RevOps is
  strategic partner to CRO
- **Level 5 (Innovating):** AI-driven insights, self-optimizing processes, RevOps
  is revenue strategy driver

## Output Format
GTM Ops blueprint with: tech stack architecture, process documentation, data
model design, operating cadence calendar, and maturity assessment.



## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls

1. **Tool sprawl without integration.** 15+ tools that don't talk to each other. Fix: CRM is the hub — everything reads from and writes to CRM. Consolidate overlapping tools.
2. **No naming conventions.** Campaign names like "webinar_final_v2" make attribution impossible. Fix: enforce standardized naming: [Date]-[Segment]-[Channel]-[Content].
3. **Process documented but not enforced.** CRM has stage definitions but reps skip required fields. Fix: CRM validation rules that prevent stage advancement without required data.

## Related Skills
- tool-selection-stack, crm-integration, pipeline-management, gtm-metrics, analytics

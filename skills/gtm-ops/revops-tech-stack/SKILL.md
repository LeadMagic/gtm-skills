---
name: revops-tech-stack
description: >-
  Design the RevOps technology stack — CRM, enrichment, sequencing, analytics,
  integration architecture. Triggers on: "RevOps stack", "sales tech stack", 
  "GTM tool audit", "revenue technology".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: gtm-ops
  tags: [gtm-ops, revops, tech-stack, tools, audit, integration]
  frameworks:
    - "RevOps Tech Stack Maturity Model"
    - "Scott Brinker MarTech Landscape"
    - "Winning by Design — Revenue Architecture"
---

# RevOps Tech Stack Design

## Overview
The average B2B company uses 15+ tools in their GTM stack — most overlapping,
underutilized, or misconfigured. This skill covers stack audit, consolidation,
integration architecture, and cost optimization across the full revenue lifecycle.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **RevOps Tech Stack Maturity Model.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Scott Brinker MarTech Landscape.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Winning by Design — Revenue Architecture.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Audit our GTM tech stack"
- "Design RevOps stack"
- "Sales tool consolidation"
- "GTM tool budget"
- "Stack cost optimization"

## Step-by-Step Process

### Phase 1: Stack Audit
Inventory every tool in the GTM motion. For each: name, category, cost, owner,
adoption %, integration status, renewal date, and value score (1-5).

Categories to audit:
- CRM, enrichment, sequencing, conversation intelligence, forecasting, compensation,
  territory planning, partner management, content management, analytics/BI,
  data warehouse, iPaaS/integration, ABM platform, chat, calendar/scheduling,
  project management, communication

### Phase 2: Consolidation Analysis
Score each tool on:
- **Utilization:** % of licenses actively used monthly
- **Overlap:** Does another tool in the stack do the same thing?
- **Integration:** Does it connect to CRM and key systems?
- **Cost per active user:** Annual cost / monthly active users
- **Switching cost:** How hard to replace?

Red flags: <50% utilization, >2 tools in same category, no CRM integration,
cost per user >$200/month without clear ROI.

### Phase 3: Target State Architecture
Design the ideal stack:

**Core (must have):**
- CRM (HubSpot or Salesforce) — single source of truth
- Enrichment (LeadMagic, Apollo, Clay) — data layer
- Sequencing (Outreach, Salesloft, or Smartlead) — outbound execution
- Calendar (ChiliPiper, Calendly) — meeting booking

**Middle layer (should have at $1M+ ARR):**
- Conversation intelligence (Gong, Chorus)
- Analytics/BI (basic CRM dashboards + Looker/Tableau at scale)
- iPaaS (workato, tray.io, or n8n for custom integrations)

**Advanced (invest at $5M+ ARR):**
- Forecasting (Clari, BoostUp)
- Territory planning (Fullcast, Varicent)
- Compensation (CaptivateIQ, Spiff)
- Data warehouse (Snowflake, BigQuery) + dbt

### Phase 4: Integration Architecture
- **CRM is the hub:** Everything reads from and writes to CRM
- **Enrichment → CRM:** Clean, enriched data flows into CRM automatically
- **CRM → Sequencing:** Accounts assigned to sequences with CRM context
- **Sequencing → CRM:** Activity logged back (emails, calls, replies)
- **CRM → Analytics:** Pipeline data flows to analytics layer
- **iPaaS layer:** Connects tools that don't have native integrations

### Phase 5: Cost Optimization
- **Vendor consolidation:** Replace 3 tools with 1 platform where possible.
  HubSpot can replace 5-7 point solutions.
- **License audit:** Remove licenses for departed employees. Downgrade unused
  seats to viewer/read-only.
- **Contract negotiation:** Multi-year commits for 20-30% discount. Ask for
  ramp pricing (year 1 lower, scales with usage).
- **Annual savings target:** 15-25% of GTM tool spend through consolidation
  and optimization.

## Output Format
RevOps stack blueprint with: audit inventory, consolidation recommendations,
target state architecture diagram, integration map, and cost optimization plan.



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
- gtm-operations, tool-selection-stack, crm-integration, campaign-governance, analytics

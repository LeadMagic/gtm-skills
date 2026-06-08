---
name: salesforce-setup
description: >-
  Set up Salesforce for B2B SaaS GTM — object model, opportunity pipelines,
  lead management, reports and dashboards, automation (Flows), and enrichment
  integration. Use when configuring Salesforce for sales or revops. Triggers on:
  "Salesforce setup", "configure Salesforce", "Salesforce CRM", "Salesforce
  pipeline", "Salesforce automation", or any Salesforce configuration request.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [salesforce, crm, setup, enterprise, sales]
  frameworks: [Salesforce Architecture, Opportunity Pipeline Model, Force.com Platform]
  related_skills: [crm-integration, pipeline-management, hubspot-setup, attio-setup]
---

# Salesforce Setup

## Overview

Salesforce is the enterprise CRM standard. It's infinitely customizable and
infinitely misconfigurable. This skill covers GTM-specific Salesforce setup:
object model for B2B SaaS, opportunity pipelines, lead management, Flows
automation, reporting, and enrichment integration. Designed for teams that
have outgrown HubSpot or require enterprise-grade customization.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Salesforce Architecture.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Opportunity Pipeline Model.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Force.com Platform.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use

- "Set up Salesforce for our sales team"
- "Configure Salesforce opportunity pipeline"
- "Set up Salesforce Flows automation"
- "Build Salesforce reports and dashboards"
- "Migrate from HubSpot to Salesforce"

## Step-by-Step Process

### Phase 1: Object Model

Standard B2B SaaS object hierarchy: Lead → Account → Contact → Opportunity.

Custom objects for SaaS-specific needs: Subscription (track recurring revenue),
Customer Success Plan (health score, QBRs), Integration (partner tracking).

Key custom fields on Opportunity: MEDDICC dimensions (Economic Buyer, Decision
Criteria, Champion, etc.), ICP fit score, enrichment status, lead source detail,
competitors in deal.

### Phase 2: Opportunity Pipeline

**Sales process:** Define path per record type. Standard: Prospecting →
Qualification → Discovery → Demo → Proposal → Negotiation → Closed Won/Lost.

**Stage requirements:** Required fields per stage. Qualification: MEDDIC
dimensions populated. Proposal: Amount, Close Date, Competitors. Negotiation:
Decision Process documented.

**Validation rules:** Close Date cannot be in the past. Amount > $0. Next Step
required when stage changes. Stage cannot skip forward.

### Phase 3: Lead Management

**Lead conversion:** Lead → Account + Contact + Opportunity. Required mapping:
company name → Account Name, email → Contact Email. Auto-assignment rules
based on territory, deal size, or round-robin.

**Web-to-Lead:** Form submission creates Lead. Auto-enrich via Flow before
assignment. Score leads based on ICP fit + engagement.

### Phase 4: Flows Automation

Replace Process Builder and Workflow Rules with Flows (Salesforce's modern
automation tool). Key Flows:
- Auto-create task when opportunity stage changes
- Alert manager when deal stalls >14 days
- Create renewal opportunity 90 days before contract end
- Enrich contact on create via external service webhook

### Phase 5: Reports and Dashboards

**Sales dashboards:** Pipeline by stage, rep activity, forecast vs quota, win
rate by source, deal velocity.

**Revenue dashboards:** MRR/ARR trending, churn analysis, expansion revenue,
cohort retention.

**Data quality dashboards:** Missing required fields, stale opportunities,
duplicate detection, enrichment gaps.

### Phase 6: Enrichment Integration

**One-direction push:** External enrichment (Clay, LeadMagic) → Salesforce.
Never Salesforce → enrichment platform.

**Flow-triggered enrichment:** Contact created → Flow calls external webhook →
enrichment data writes back to Contact/Account fields.

**Scheduled enrichment:** Weekly batch job re-verifies emails >90 days old,
refreshes firmographic data on key accounts.

## Output Format

Salesforce configuration document with: object model diagram, opportunity
pipeline map with validation rules, lead management flow, Flows automation
catalog, dashboard specs, and enrichment integration architecture.

## Quality Check

- [ ] Object model: Lead → Account → Contact → Opportunity hierarchy configured
- [ ] Opportunity stages defined with required fields and validation rules
- [ ] Lead scoring and assignment rules active
- [ ] Key Flows automating repetitive tasks
- [ ] Dashboards for sales, revenue, and data quality
- [ ] Enrichment: one-direction push, never two-way sync

## Common Pitfalls

1. **Over-customization before process.** Custom objects and fields without a
   defined process create complexity without value. Design the process, then
   configure Salesforce to support it.

2. **No validation rules.** Close dates in the past, $0 opportunities, blank
   required fields. Validation rules enforce data quality.

3. **Process Builder instead of Flows.** Process Builder is deprecated.
   Migrate everything to Flows.

4. **Lead assignment without enrichment.** Routing an unenriched lead means
   reps waste time researching. Enrich on lead create, then assign.

5. **Report sprawl.** 50 reports nobody reads. Build 5-7 dashboards that
   answer the most important questions. Archive the rest.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- **crm-integration**: CRM configuration principles
- **pipeline-management**: Deal stage design
- **hubspot-setup**: HubSpot alternative
- **attio-setup**: Attio alternative

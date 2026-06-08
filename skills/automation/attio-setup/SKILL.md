---
name: attio-setup
description: >-
  Set up Attio for B2B SaaS GTM — programmable CRM, custom objects, workflow
  automation, enrichment integration, and real-time collaboration. Use when
  configuring Attio for sales, building a programmable CRM, or migrating from
  HubSpot/Salesforce. Triggers on: "Attio setup", "configure Attio", "Attio CRM",
  "Attio pipeline", or any Attio configuration request.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [attio, crm, setup, programmable, modern]
  frameworks:
    - "Attio Programmable CRM Model"
    - "Modern CRM Architecture"
    - "HubSpot Academy — CRM Automation"
  related_skills: [crm-integration, pipeline-management, hubspot-setup, salesforce-setup]
---

# Attio Setup

## Overview

Attio is the modern programmable CRM. Unlike HubSpot (unified suite) or
Salesforce (enterprise customizability), Attio is built for teams that want
a CRM that works like a database — flexible objects, real-time collaboration,
and API-first architecture. Best for startups and growth-stage B2B SaaS that
find HubSpot too rigid and Salesforce too heavy.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Attio Programmable CRM Model.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Modern CRM Architecture.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **HubSpot Academy — CRM Automation.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use

- "Set up Attio for our sales team"
- "Configure Attio objects and pipelines"
- "Build Attio workflows"
- "Migrate to Attio from HubSpot/Salesforce"
- "Set up enrichment in Attio"

## Step-by-Step Process

### Phase 1: Object Model

Attio is object-based. Standard: Companies, People, Deals. Custom objects
for anything: Subscriptions, Customer Success Plans, Partner relationships.

**Key difference vs Salesforce:** No rigid Lead→Account→Contact hierarchy.
Everything is a flat object that can be linked. A Person can belong to multiple
Companies. A Deal can involve multiple People.

### Phase 2: Lists and Views

Lists are Attio's killer feature. Create dynamic lists based on any attribute:
"Companies in my ICP with no open deals," "Deals stalled >14 days," "Contacts
with unverified emails."

Views: kanban, table, timeline, list. Each view filters a list. Share views
with the team. Save frequently-used views.

### Phase 3: Workflows

Attio's automation engine. Triggers: record created/updated/deleted, list
membership changed, date reached. Actions: update record, create task, send
Slack notification, call webhook.

Key workflows:
- New deal created → assign rep, create onboarding task
- Deal stalled >14 days → Slack alert to manager
- Company added to ICP list → auto-enrich via webhook
- Contact email unverified → flag for verification

### Phase 4: Enrichment Integration

Attio's API-first design makes enrichment integration clean:
- Webhook on record create → external enrichment → write back to Attio
- Scheduled list-based enrichment: "enrich all companies added this week"
- Real-time enrichment via Zapier/Make triggers

### Phase 5: Collaboration

Attio's real-time collaboration: multiple team members editing the same
record simultaneously. Notes, comments, mentions. Slack integration for
notifications on deal changes, new assignments, and stalled deals.

## Output Format

Attio configuration document with: object model design, list/views catalog,
workflow automation map, enrichment integration setup, and team collaboration
guidelines.

## Quality Check

- [ ] Object model: Companies, People, Deals configured with custom attributes
- [ ] Key Lists created (ICP companies, stalled deals, unverified contacts)
- [ ] Workflows automating repetitive tasks
- [ ] Enrichment integration via webhooks active
- [ ] Team views shared and adopted

## Common Pitfalls

1. **Over-building objects.** Start with Companies, People, Deals. Add custom
   objects only when these three can't represent what you need.

2. **No lists.** Lists are Attio's superpower. Without them, it's just a
   spreadsheet. Build lists for every segment and workflow trigger.

3. **HubSpot migration without cleanup.** Moving bad data to Attio is just
   bad data in a better tool. Clean your data before migrating.

4. **API-first without API use.** Attio's API is the differentiator. Use it
   for enrichment, automation, and custom integrations.

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
- **salesforce-setup**: Salesforce alternative

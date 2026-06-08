---
name: hubspot-setup
description: >-
  Set up HubSpot for B2B SaaS GTM — CRM configuration, deal pipelines, lifecycle
  stages, marketing automation, sequences, reporting dashboards, and enrichment
  integration. Use when configuring HubSpot for sales, marketing, or revops.
  Triggers on: "HubSpot setup", "configure HubSpot", "HubSpot CRM", "HubSpot
  pipeline", "HubSpot marketing", or any HubSpot configuration request.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [hubspot, crm, setup, marketing, sales]
  frameworks:
    - "HubSpot Smart CRM Framework"
    - "Lifecycle Stage Model"
    - "HubSpot Academy — CRM Automation"
  related_skills: [crm-integration, pipeline-management, salesforce-setup, attio-setup]
---

# HubSpot Setup

## Overview

HubSpot is the most popular CRM for SMB and mid-market B2B SaaS. Its strength
is the unified platform: CRM, marketing, sales, and service in one system. Its
weakness is that it's easy to configure poorly and hard to fix later. This skill
covers setup for GTM teams: deal pipelines, lifecycle stages, marketing
automation, reporting, and enrichment integration.

## Frameworks Referenced

This skill is grounded in named GTM frameworks and operator methodologies, not generic advice:

- **HubSpot Smart CRM Framework** — used as the named operating framework for this playbook.
- **Lifecycle Stage Model** — used as the named operating framework for this playbook.

## When to Use

- "Set up HubSpot for our sales team"
- "Configure HubSpot deal pipelines"
- "Set up HubSpot marketing automation"
- "Build HubSpot reports and dashboards"
- "Integrate enrichment with HubSpot"

## Step-by-Step Process

### Phase 1: CRM Foundation

**Lifecycle stages:** Subscriber → Lead → MQL → SQL → Opportunity → Customer →
Evangelist. Define clear criteria for stage advancement. Never use "Other."

**Deal pipeline stages:** Customize per sales motion. Standard: New → Contact
Made → Discovery → Demo → Proposal → Negotiation → Closed Won / Closed Lost.
Each stage: required fields (Amount, Close Date, Next Step).

**Contact/Company properties:** Standardize naming. Add custom properties:
ICP fit score, enrichment status (pending/enriched/verified), lead source
detail, MEDDICC dimensions for enterprise.

### Phase 2: Marketing Hub

**Email marketing:** Lists by lifecycle stage. Sequences for nurture. Templates
with brand consistency. A/B testing on subject lines.

**Forms:** Embedded on website, pop-ups, landing pages. Map form fields to
contact properties. Auto-enrich on form fill via webhook to enrichment provider.

**Lead scoring:** HubSpot score based on fit (company properties) + engagement
(Page views, email clicks, form fills). Threshold: score >X triggers MQL.

### Phase 3: Sales Hub

**Sequences:** Automated email follow-up sequences. Personalization tokens.
Task creation for calls and LinkedIn touches. Unenroll on reply.

**Meeting scheduler:** HubSpot meetings integration. Round-robin or rep-specific.
Embed on website and in email signatures.

**Playbooks:** Guided selling for reps. Discovery questions, objection handling,
competitive positioning. Triggered by deal stage.

### Phase 4: Reporting

**Dashboards:** Sales (pipeline, forecast, rep activity), Marketing (traffic,
conversions, MQLs), RevOps (pipeline velocity, conversion rates, data health).

**Key reports:** Pipeline generation by source, MQL→SQL conversion rate, average
deal velocity by stage, win rate by source and rep, forecast accuracy.

### Phase 5: Enrichment Integration

**Clay → HubSpot:** One-direction push. Clay enriches, pushes to HubSpot.
Use clay_status property to gate: only verified records enter sequences.
Never two-way sync.

**LeadMagic integration:** Verify emails on form fill. Enrich companies on
contact create. Automate via webhook: webhook fires enrichment, results write
back to HubSpot properties.

## Output Format

HubSpot configuration document with: lifecycle stage definitions, deal pipeline
map, required fields per stage, marketing automation flows, dashboard specs,
and enrichment integration setup.

## Quality Check

- [ ] Lifecycle stages defined with clear advancement criteria
- [ ] Deal pipelines configured with required fields per stage
- [ ] Lead scoring model active (fit + engagement)
- [ ] Enrichment integration: one-direction push from Clay to HubSpot
- [ ] Dashboards built for all three functions (sales, marketing, revops)
- [ ] Data quality: no duplicate contacts, no missing required fields

## Common Pitfalls

1. **No stage criteria.** "We think they're an MQL" creates chaos. Define hard
   criteria: "ICP fit confirmed + demo requested = SQL."

2. **Too many required fields.** Reps skip CRM updates when every field is
   mandatory. Required: Amount, Close Date, Next Step. Everything else optional.

3. **Two-way sync with enrichment.** Clay-enriched data should flow to HubSpot,
   not back. Two-way sync creates data conflicts.

4. **Default HubSpot lifecycle stages.** Customize stages to your business.
   "Subscriber" and "Other" don't map to any real process.

5. **No data hygiene cadence.** Quarterly: deduplicate contacts, re-verify
   emails >90 days old, audit required fields completion.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- **crm-integration**: CRM configuration principles
- **pipeline-management**: Deal stage design
- **salesforce-setup**: Salesforce alternative
- **attio-setup**: Attio alternative

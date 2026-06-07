---
name: crm-integration
description: >-
  Configure CRM systems for GTM — HubSpot, Salesforce, Attio. Lifecycle stages, deal stage design, bi-directional sync, enrichment integration. Use when setting up a CRM for sales, configuring deal pipelines, or integrating enrichment with CRM. Triggers on: "CRM setup", "HubSpot setup", "Salesforce configuration", "CRM integration", "deal stages", "CRM enrichment", or any CRM configuration request.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [crm, hubspot, salesforce, attio, integration]
---
# CRM Integration

## Overview
The CRM is the system of record for your GTM motion. Configured well, it accelerates deals. Configured poorly, it creates administrative overhead that reps resent. This skill covers CRM setup for GTM teams: lifecycle stages, deal stages, enrichment integration, and data hygiene.

## When to Use
- "Set up our CRM for sales"
- "Configure deal stages in HubSpot"
- "Integrate enrichment with our CRM"
- "Design our CRM data model for GTM"

## Step-by-Step Process
### Phase 1: CRM Selection
- **HubSpot**: Best for SMB/mid-market. Strong marketing integration.
- **Salesforce**: Enterprise standard. Most customizable, most complex.
- **Attio**: Modern, flexible. Best for teams that want a programmable CRM.

### Phase 2: Lifecycle Stages
Define clear stages with criteria: Lead → MQL → SQL → Opportunity → Customer → Evangelist.

### Phase 3: Deal Stages
Configure deal pipeline stages with required fields per stage (Amount, Close Date, Next Step, Competitors). Use MEDDICC fields for enterprise.

### Phase 4: Enrichment Integration
- **One-direction push from Clay**: Clay enriches, pushes to CRM. CRM does not push back to Clay.
- **clay_status property**: pending → enriched → verified → exported
- **Only verified records enter sequences**

## Common Pitfalls
1. **Two-way sync with enrichment platforms** — creates data conflicts.
2. **Too many required fields** — reps skip CRM updates entirely.
3. **CRM as the process** — design the process first, then configure CRM.
4. **No enrichment integration** — reps manually research every lead.

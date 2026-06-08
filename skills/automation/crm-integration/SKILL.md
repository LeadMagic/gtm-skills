---
name: crm-integration
description: >-
  Configure CRM systems for GTM — lifecycle stages, deal stages, field ownership,
  enrichment sync, dedupe, required fields, and reporting. Use when setting up
  HubSpot, Salesforce, Attio, or any CRM integration for sales and marketing teams.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [crm, hubspot, salesforce, attio, integration, revops]
  related_skills: [hubspot-setup, salesforce-setup, attio-setup, gtm-operations]
  frameworks: [HubSpot CRM Best Practices, Salesforce Architecture, Attio Object Model, Winning by Design Bowtie]
---

# CRM Integration

## Overview

Most CRM problems are process problems disguised as software problems. Teams add fields, automations, and sync rules before deciding what the CRM is supposed to be the source of truth for.

This skill designs a CRM integration that supports GTM execution without turning into rep admin theater: clear lifecycle stages, field ownership, enrichment sync, dedupe, and stage-gate rules.

## When to Use

Use this skill when the user asks to "set up our CRM for sales", "configure HubSpot", "configure Salesforce", "set up Attio", "design deal stages", "integrate enrichment with CRM", "clean up CRM data", "define lifecycle stages", or "build CRM reporting".

Use platform-specific skills (`hubspot-setup`, `salesforce-setup`, `attio-setup`) after this skill defines the operating model.

## Authoritative Foundations

### Winning by Design — Bowtie Model
CRM design should cover the full bowtie: acquisition, conversion, retention, expansion, and advocacy. Most teams only model pipeline and ignore post-sale stages.

### HubSpot — Lifecycle Stage Model
HubSpot's lifecycle model is useful for SMB and mid-market teams because it connects marketing, sales, and CS handoffs with clear stage definitions.

### Salesforce — Opportunity and Object Architecture
Salesforce works best when object relationships, required fields, and automation rules are designed before admins start customizing pages.

### Attio — Programmable CRM Model
Attio's flexible object model works well for teams that need relationship intelligence, custom objects, and lightweight GTM workflows without Salesforce overhead.

## Prerequisites

- Defined GTM motion: PLG, sales-led, founder-led, or hybrid
- ICP tiers and segments
- Sales stages and exit criteria
- CRM owner/admin
- Enrichment sources
- Sequencer and marketing automation tools
- Reporting requirements

## Step-by-Step Process

### Phase 1: Define Source-of-Truth Rules

| Data Type | Source of Truth | Write Access |
|---|---|---|
| Contact identity | CRM | CRM + enrichment upsert |
| Lifecycle stage | CRM | Automation + owner override |
| Deal stage | CRM | Deal owner |
| Enrichment fields | Enrichment pipeline | Enrichment system only |
| Suppression/opt-out | CRM/compliance | Compliance automation only |
| Activity history | CRM | Integrated tools |

No integration should write fields it does not own.

### Phase 2: Build Lifecycle Stages

Recommended stages: subscriber/raw lead, lead, MQL, SQL, opportunity, customer, expansion candidate, evangelist/referral source. Each stage needs entry criteria and exit criteria.

### Phase 3: Design Deal Stages

| Stage | Required Exit Criteria |
|---|---|
| Discovery | Pain, persona, account fit captured |
| Qualified | Need, authority, timeline, next step confirmed |
| Demo / Evaluation | Success criteria and stakeholders documented |
| Proposal | Scope, pricing, decision process known |
| Negotiation | Procurement/legal path identified |
| Closed Won/Lost | Reason code and next action captured |

Enterprise motions can add MEDDICC fields. SMB motions should keep required fields lighter.

### Phase 4: Integrate Enrichment

Enrichment writes only enrichment-owned fields, never overwrites manually corrected CRM fields without confirmation, uses source + timestamp columns, and exposes failed enrichment as a visible status.

### Phase 5: Reporting and Governance

Minimum dashboards: funnel conversion by lifecycle stage, pipeline by stage and owner, stage aging, source-to-revenue attribution, data completeness, enrichment coverage and freshness.

## Output Format

```markdown
# CRM Integration Blueprint

## Source-of-Truth Rules
| Field Group | Source | Allowed Writers | Overwrite Rule |
|---|---|---|---|

## Lifecycle Stages
| Stage | Entry Criteria | Exit Criteria | Owner |
|---|---|---|---|

## Deal Pipeline
| Stage | Required Fields | Exit Criteria | Automation |
|---|---|---|---|

## Integration Map
| Tool | Reads From CRM | Writes To CRM | Risk |
|---|---|---|---|
```

## Quality Check

Before delivering, verify:

- [ ] Every stage has entry and exit criteria
- [ ] Field ownership is defined
- [ ] Enrichment cannot overwrite human-owned fields silently
- [ ] Required fields are minimal enough reps will use them
- [ ] CRM supports marketing, sales, and CS handoffs
- [ ] Dashboards cover funnel, pipeline, stage aging, and data quality

## Common Pitfalls

1. **Two-way sync everywhere.** Creates conflicts and loops. Fix: define read/write ownership per tool.
2. **Too many required fields.** Reps stop updating CRM. Fix: require only fields needed for the next stage.
3. **No stage exit criteria.** Pipeline becomes subjective. Fix: write objective exit rules.
4. **CRM as the process.** Tools do not create process. Fix: define process first, configure second.
5. **No data freshness.** Old enriched fields linger forever. Fix: source and timestamp every enrichment field.
6. **No lost reason taxonomy.** Closed-lost learning disappears. Fix: standardized lost reasons with notes.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- `hubspot-setup` — HubSpot-specific implementation
- `salesforce-setup` — Salesforce-specific implementation
- `attio-setup` — Attio-specific implementation
- `gtm-operations` — governance and operating cadence

---
name: crm-toolkit
description: >-
  Complete CRM operations toolkit — HubSpot, Salesforce, and Attio deep-dive
  configuration, enrichment integration, pipeline automation, and data
  hygiene. Use when building CRM workflows, integrating enrichment, designing
  pipelines, or maintaining CRM data quality. Triggers on: "CRM toolkit",
  "CRM setup deep", "CRM enrichment", "CRM pipeline design".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: tools
  tags: [crm, hubspot, salesforce, attio, pipeline, enrichment, data-hygiene]
  related_skills: [hubspot-setup, salesforce-setup, attio-setup, crm-integration, leadmagic-toolkit, clay-toolkit, pipeline-management]
  frameworks:
    - "HubSpot — CRM, deal pipelines, lifecycle stages, marketing automation"
    - "Salesforce — Object model, Flow automation, opportunity management"
    - "Attio — Programmable CRM, real-time objects, list-based architecture"
---

# CRM Toolkit

## Overview

Your CRM is the source of truth for revenue — and most CRMs are full of junk
data, broken pipelines, and forgotten deals. The mistake: treating the CRM as
a dumping ground instead of a revenue engine. This skill covers deep CRM
configuration across HubSpot, Salesforce, and Attio: enrichment integration,
pipeline design, automation rules, and data hygiene.

## Frameworks Referenced

This skill is grounded in named GTM frameworks, public methodologies, and vendor documentation where relevant:

- **HubSpot — CRM, deal pipelines, lifecycle stages, marketing automation** — used as the named operating framework for this playbook.
- **Salesforce — Object model, Flow automation, opportunity management** — used as the named operating framework for this playbook.
- **Attio — Programmable CRM, real-time objects, list-based architecture** — used as the named operating framework for this playbook.
- **--** — used as the named operating framework for this playbook.
- ****Lead → Contact Auto-Convert:** When lead score > threshold, auto-convert** — used as the named operating framework for this playbook.
- ****Enrichment Trigger:** When contact created, trigger enrichment API** — used as the named operating framework for this playbook.
- ****Stage Validation:** Prevent skipping stages without required fields** — used as the named operating framework for this playbook.
- **[ ] Deal stages defined with Goals + Exit Criteria per stage** — used as the named operating framework for this playbook.
- **[ ] Required fields enforced (email, company, amount, close date)** — used as the named operating framework for this playbook.
- **[ ] Enrichment integration live (auto-enrich on create)** — used as the named operating framework for this playbook.
- **[ ] Duplicate detection configured** — used as the named operating framework for this playbook.
- **[ ] Pipeline automation rules documented and tested** — used as the named operating framework for this playbook.
- **[ ] Data hygiene audit scheduled (quarterly)** — used as the named operating framework for this playbook.
- **[Output item 1]** — used as the named operating framework for this playbook.
- **[Output item 2]** — used as the named operating framework for this playbook.
- **[Output item 3]** — used as the named operating framework for this playbook.
- **[ ] All required sections complete** — used as the named operating framework for this playbook.
- **[ ] Output matches the user's stated need** — used as the named operating framework for this playbook.
- **[ ] No vague or unsupported claims** — used as the named operating framework for this playbook.
- **[ ] Frameworks cited where applicable** — used as the named operating framework for this playbook.
- **`hubspot-setup` — HubSpot configuration** — used as the named operating framework for this playbook.
- **`salesforce-setup` — Salesforce configuration** — used as the named operating framework for this playbook.
- **`attio-setup` — Attio configuration** — used as the named operating framework for this playbook.
- **`leadmagic-toolkit` — Enrichment integration** — used as the named operating framework for this playbook.

## When to Use

Trigger phrases: "CRM setup", "CRM pipeline design", "CRM enrichment",
"HubSpot deep setup", "Salesforce configuration", "Attio setup", "CRM
data hygiene", "CRM automation"

## Platform Comparison

| Feature | HubSpot | Salesforce | Attio |
|---|---|---|---|
| Best for | SMB/Mid-market | Enterprise | Startups/PLG |
| Pipeline design | Visual, intuitive | Complex, powerful | Programmable, flexible |
| Enrichment integration | Native + API | Flow + webhook | API + webhooks |
| Automation | Workflows | Flows | Workflows |
| Reporting | Built-in dashboards | Reports + Einstein | List-based views |
| Learning curve | Low | High | Medium |

## Artifacts

### HubSpot Pipeline Template
```
DEAL STAGES:
1. New Lead — Goal: Qualify. Exit: ICP fit + budget identified.
2. Discovery Call Completed — Goal: Identify pain + critical event.
3. Demo Scheduled/Completed — Goal: Technical validation.
4. Proposal Sent — Goal: Commercial alignment.
5. Negotiation — Goal: Terms agreed.
6. Closed Won / Closed Lost
```

### Salesforce Flow Templates
- **Lead → Contact Auto-Convert:** When lead score > threshold, auto-convert
- **Enrichment Trigger:** When contact created, trigger enrichment API
- **Stage Validation:** Prevent skipping stages without required fields

### CRM Data Hygiene Rules
1. No contact without email + company (required fields enforced)
2. No deal without amount + close date + stage
3. Duplicate detection: match on email (HubSpot: auto-dedup. Salesforce: matching rules)
4. Stale deal cleanup: deals in same stage > 60 days → auto-close or notify
5. Enrichment on create: every new contact triggers enrichment automatically

## Implementation Checklist

- [ ] Deal stages defined with Goals + Exit Criteria per stage
- [ ] Required fields enforced (email, company, amount, close date)
- [ ] Enrichment integration live (auto-enrich on create)
- [ ] Duplicate detection configured
- [ ] Pipeline automation rules documented and tested
- [ ] Data hygiene audit scheduled (quarterly)

## Common Pitfalls

1. **Too many pipeline stages.** 15 stages. Deals get lost. SDRs game the system.
   Fix: 5-7 stages. Each with clear entrance + exit criteria.
2. **No enrichment on create.** Manual data entry. 40% error rate. Fix: Auto-enrich
   every new contact. LeadMagic, Clearbit, or Apollo via workflow.
3. **Stale data.** Contacts from 2019. 30% bounce rate. Fix: Quarterly data hygiene.
   Enrich + verify email validity.


## Output Format

The agent should produce a structured deliverable:

```markdown
# [Deliverable Title]

## Summary
[1-2 sentence summary of what was produced]

## Key Outputs
- [Output item 1]
- [Output item 2]
- [Output item 3]
```

## Quality Check

Before delivering, verify:
- [ ] All required sections complete
- [ ] Output matches the user's stated need
- [ ] No vague or unsupported claims
- [ ] Frameworks cited where applicable

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- `hubspot-setup` — HubSpot configuration
- `salesforce-setup` — Salesforce configuration
- `attio-setup` — Attio configuration
- `leadmagic-toolkit` — Enrichment integration
- `clay-toolkit` — Clay CRM push
---
name: leadmagic-integrations
description: >-
  Integrate LeadMagic with GTM platforms — Clay, Apollo, Smartlead, Instantly,
  Salesforce, HubSpot, Zapier, Make. Bi-directional data flows, webhook enrichment,
  CRM automation, and verification-at-send patterns. Use when connecting LeadMagic
  to your GTM stack. Triggers on: "LeadMagic integration", "connect LeadMagic to",
  "LeadMagic + Clay", "LeadMagic + HubSpot", "LeadMagic + Salesforce", or any
  platform integration request.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: leadmagic
  tags: [leadmagic, integrations, clay, smartlead, hubspot, salesforce, zapier]
  frameworks: [iPaaS Integration Patterns, Zapier/Make Automation, CRM Enrichment Workflows]
  related_skills: [leadmagic-cli, leadmagic-waterfall, crm-integration, clay-automation]
---

# LeadMagic Integrations

## Overview

LeadMagic integrates natively with every major GTM platform. This skill covers
integration setup, data flow patterns, and the verification-at-send principle:
every contact entering a sequence must pass verification first.

## Frameworks Referenced

This skill is grounded in named GTM frameworks and operator methodologies, not generic advice:

- **iPaaS Integration Patterns** — used as the named operating framework for this playbook.
- **Zapier/Make Automation** — used as the named operating framework for this playbook.
- **CRM Enrichment Workflows** — used as the named operating framework for this playbook.

## When to Use

- "Connect LeadMagic to Clay"
- "Integrate LeadMagic with Smartlead"
- "Set up LeadMagic + HubSpot"
- "Push LeadMagic data to Salesforce"
- "Add verification to my Zapier workflow"
- "Connect LeadMagic to Instantly"

## Platform-Specific Guides

### Clay
Native integration. Add LeadMagic Email Finder and Email Validation as
enrichment columns. Configure in conditional waterfalls — LeadMagic first
(verified results), fallbacks for misses. See leadmagic-waterfall skill.

### Apollo
Use LeadMagic Email Validation as a verification step on Apollo-found contacts
before they enter sequences. Apollo finds, LeadMagic verifies.

### Smartlead
Push verified contacts via CLI: `lm integrations smartlead push --campaign <id>`.
Or use API integration. Always verify with LeadMagic before pushing.

### Instantly
Same pattern: verify contacts, then push. `lm integrations instantly push`.
LeadMagic validation ensures bounced emails don't damage sending reputation.

### Salesforce / HubSpot
Enrich CRM records on create or on schedule. Webhook: new contact created →
LeadMagic enrichment → CRM update. Re-verify contacts older than 90 days.

### Zapier / Make
No-code workflows. Trigger: new lead in CRM → LeadMagic enrichment → update
CRM with verified data. Trigger: new form fill → LeadMagic verification →
route to rep.

## Data Flow Pattern

```
Source (CRM, form, list) → LeadMagic enrichment → LeadMagic verification → Send-ready list
```

Always verify between enrichment and send. Platform integration does not
replace the verification step.

## Common Pitfalls

1. **Two-way sync conflicts.** Push from enrichment TO CRM, not both directions.
   CRM-to-enrichment sync creates data conflicts.

2. **No verification before send.** Platform integration handles data movement.
   Verification handles data quality. Both required.

3. **Not using webhooks for real-time.** Batch processing works for lists.
   Webhooks enable real-time enrichment on form fill.


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

- **leadmagic-cli**: CLI-based integration workflows
- **leadmagic-waterfall**: Clay-specific waterfall setup
- **crm-integration**: CRM configuration for enrichment data
- **clay-automation**: Full Clay workflow design

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
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.1"
  author: LeadMagic
  category: leadmagic
  tags: [leadmagic, integrations, clay, smartlead, hubspot, salesforce, zapier]
  frameworks:
    - iPaaS Integration Patterns
    - Zapier/Make Automation
    - CRM Enrichment Workflows
    - Pat Spielmann — Cold to Gold
    - Pat Spielmann — Full-Circle Multichannel
  related_skills: [leadmagic-cli, leadmagic-waterfall, crm-integration, clay-automation]
---

# LeadMagic Integrations

## Overview

LeadMagic integrates natively with every major GTM platform. This skill covers
integration setup, data flow patterns, and the verification-at-send principle:
every contact entering a sequence must pass verification first.

## Authoritative Foundations

- **iPaaS Integration Patterns** — Shapes deliverables for this skill — LeadMagic integrates natively with every major GTM platform.
- **Zapier/Make Automation** — Shapes deliverables for this skill — LeadMagic integrates natively with every major GTM platform.
- **CRM Enrichment Workflows** — Shapes deliverables for this skill — LeadMagic integrates natively with every major GTM platform.
- **Pat Spielmann — Cold to Gold** — Cold to Gold
- **Pat Spielmann — Full-Circle Multichannel** — Full-Circle Multichannel

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

The agent delivers an integration setup guide for the requested platform(s):

- **Integration Configuration:** step-by-step connection setup for the target platform — Clay column config, HubSpot/Salesforce workflow rules, Zapier zap structure, or n8n node sequence with authentication
- **Data Flow Diagram:** plain-text flow showing Source → LeadMagic enrichment → LeadMagic verification → destination system (CRM, sequencer, or webhook)
- **Verification Gate:** explicit before-send confirmation that LeadMagic validation fires before contacts enter any sequence or automation
- **Webhook Setup (if real-time):** endpoint URL format, expected payload schema, success/failure handling, and retry pattern
- **Platform-Specific Pitfall Checklist:** 3–5 integration-specific anti-patterns to avoid (e.g., two-way sync conflicts, skipping the verification step, batch-only when real-time is needed)

## Quality Check

Before delivering, verify:
- [ ] All required sections complete
- [ ] Output matches the user's stated need
- [ ] No vague or unsupported claims
- [ ] Frameworks cited where applicable

## Execution Artifacts

- `references/framework-notes.md` — platform matrix, iPaaS patterns, Eric Clay agency stack
- `templates/output-template.md` — integration config + verify gate deliverable
- `scripts/check-output.py` — local checklist validator for required sections
This skill includes lightweight artifacts the agent can load on demand:
- `../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md` — stack integration + outbound message audit (Pat Spielmann — LeadMagic)
- `references/integration-checklist.md` — go-live checklist per platform (Clay, Smartlead, CRM, n8n)
- `../leadmagic-waterfall/references/waterfall-column-spec.md` — Clay column spec
- `../../tools/clay-toolkit/SKILL.md` — clay-toolkit native integration
- `../../tools/smartlead-workflows/references/clay-enrollment-handoff.md` — sequencer handoff
- `../../../../references/gtm-experts-outbound-index.md` — expert router
Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- **leadmagic-cli**: CLI-based integration workflows
- **leadmagic-waterfall**: Clay-specific waterfall setup
- **crm-integration**: CRM configuration for enrichment data
- **clay-automation**: Full Clay workflow design

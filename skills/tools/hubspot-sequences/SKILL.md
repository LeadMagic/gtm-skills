---
name: hubspot-sequences
description: >-
  Design and optimize HubSpot sequences — enrollment triggers, multi-channel steps, 
  task creation, analytics, A/B testing. Triggers on: "HubSpot sequences", "HubSpot 
  automation", "HubSpot cadence", "sales hub sequences".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: tools
  tags: [hubspot, sequences, sales-hub, crm, cadence]
  frameworks:
    - "HubSpot Sequences Best Practices"
    - "ColdIQ Multi-Channel Cadence"
    - "Outreach — Sales Engagement Cadence Design"
---

# HubSpot Sequences

## Overview
HubSpot Sequences power the SDR and AE outbound motion inside Sales Hub.
Done right, they automate touches while maintaining personalization. Done wrong,
they're spam cannons that burn your domain reputation.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **HubSpot Sequences Best Practices.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **ColdIQ Multi-Channel Cadence.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Outreach — Sales Engagement Cadence Design.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Set up HubSpot sequences"
- "Build HubSpot cadences"
- "Optimize HubSpot sequence performance"
- "HubSpot sequence A/B test"

## Step-by-Step Process

### Phase 1: Sequence Architecture
Design sequences by persona and trigger:
- **Inbound follow-up:** Auto-enroll on form fill, 3-touch, 7-day window
- **Outbound cold:** Manual enroll after list build, 6-touch, 21-day window
- **Re-engagement:** Enroll on CRM status change, 3-touch, 14-day window
- **Event follow-up:** Enroll on event attendance, 2-touch, 5-day window

### Phase 2: Step Configuration
Per step: channel, timing, template, task creation rules.
- Email steps: plain text, from first name, no tracking pixel if cold
- Call steps: auto-create task with call notes template
- LinkedIn steps: manual task (HubSpot can't automate LinkedIn)
- Delay steps: minimum 2 business days between touches

### Phase 3: Enrollment Rules
- Suppression: don't enroll if already in another sequence
- Unenrollment: auto-unenroll on reply, meeting booked, or bounce
- Queue limits: max 50 contacts per sender per sequence
- Business hours: only send Mon-Thu 6am-8pm prospect timezone

### Phase 4: A/B Testing
Test one variable at a time with 2-week minimum run time:
- Subject lines (2-3 variants)
- Opening lines (different hooks)
- CTA phrasing (soft vs direct)
- Send time (morning vs afternoon)

### Phase 5: Analytics
Track: enrollment rate, completion rate, reply rate, meeting rate.
Kill sequences with <1% reply rate after 50+ enrollments.

## Output Format
Sequence design document with: architecture map, step-by-step configuration,
enrollment/unescape rules, A/B test plan, and analytics dashboard design.



## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls

1. **Skipping research.** Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
2. **Generic output.** "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
3. **Missing framework citations.** Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — HubSpot workflow enrollment, rep-triggered rules
- `references/enrichment-enrollment-gate.md` — lm_email_status workflow gate
- `../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md` — verify-before-enroll (Pat Spielmann)
- `../../tools/clay-toolkit/references/gtm-table-blueprints.md` — clay-toolkit property map
- `../../tools/clay-loops-toolkit/references/leadmagic-waterfall.md` — loop list → workflow pattern
- `../../../../references/gtm-experts-outbound-index.md` — expert router
- `templates/output-template.md` — properties + workflow + sequence deliverable
- `scripts/check-output.py` — local checklist validator

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Implementation Depth

Use this section when the user asks for a finished asset, not a high-level explanation.

### Diagnostic Questions

1. What is the primary motion: founder-led, sales-led, product-led, partner-led, or lifecycle-led?
2. Which ICP tier is the output for: small business, mid-market, enterprise, or mixed?
3. What proof is available today: customer stories, usage data, third-party validation, screenshots, or none?
4. What system will execute the work: CRM, sequencer, warehouse, support desk, product analytics, or manual workflow?
5. What decision will the user make from this output: launch, prioritize, route, rewrite, score, coach, or measure?

### Framework Application

Map the recommendation explicitly to the named frameworks in this skill:

- HubSpot Sequences Best Practices: apply only the part that directly improves the requested deliverable.
- ColdIQ Multi-Channel Cadence: apply only the part that directly improves the requested deliverable.
- Outreach — Sales Engagement Cadence Design: apply only the part that directly improves the requested deliverable.

### Deliverable Standard

A strong output from this skill includes:

- A crisp diagnosis of the current situation
- A recommended path with tradeoffs, not a generic list
- A concrete artifact the user can use immediately: table, script, checklist, scorecard, sequence, dashboard spec, or implementation plan
- A measurement plan with leading and lagging indicators
- Risks and edge cases called out before execution

### Adaptation Rules

- For small business: reduce complexity, shorten time-to-value, and prioritize owner/operator clarity.
- For mid-market: include workflow ownership, handoffs, integrations, and enablement assets.
- For enterprise: include governance, risk, procurement, stakeholder mapping, and proof requirements.


## Related Skills
- cold-email-strategy, cold-email-copywriting, sending-platforms, inbox-setup, email-deliverability

---
name: salesloft-cadences
description: >-
  Build and optimize Salesloft cadences — Rhythm, Conversations, multi-channel
  orchestration, analytics. Triggers on: "Salesloft", "Salesloft cadence", "Rhythm",
  "Salesloft automation".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: tools
  tags: [salesloft, cadence, rhythm, sales-engagement, outbound]
  frameworks:
    - "Salesloft Modern Selling Framework"
    - "ColdIQ Cadence Design"
    - "Outreach — Sales Engagement Cadence Design"
---

# Salesloft Cadences

## Overview
Salesloft is the market leader in sales engagement. Cadences here manage Rhythm
(multi-channel cadences), Conversations (reply management), and Deals (pipeline
integration). This skill covers setup, optimization, and team workflows.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Salesloft Modern Selling Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **ColdIQ Cadence Design.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Outreach — Sales Engagement Cadence Design.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Set up Salesloft cadences"
- "Build Salesloft Rhythm"
- "Salesloft optimization"
- "Salesloft team setup"

## Step-by-Step Process

### Phase 1: Cadence Architecture
Design by motion type:
- **Prospecting Cadence:** 6-8 touches over 14 days, email + call + LinkedIn
- **Inbound Cadence:** 4 touches over 7 days, fast follow-up (speed-to-lead)
- **Re-engagement Cadence:** 3 touches over 10 days, "still relevant?" angle
- **Event Follow-up Cadence:** 2 touches over 5 days, reference the event
- **AE Cadence:** 3 touches over 7 days, discovery-focused, less volume

### Phase 2: Step Types
- **Email step:** Template with merge fields, plain text, from individual sender
- **Call step:** Auto-logged, call script + talk track linked, voicemail drop
- **Social step:** LinkedIn view, connection, or DM (manual task with template)
- **Custom step:** Slack message, direct mail, gift send
- **Wait step:** 2-5 business days between touches, skip weekends

### Phase 3: Team Configuration
- **Persona-based cadences:** Different cadences for C-suite vs Director vs Manager
- **Industry variants:** Different opener templates by industry
- **Rep assignment rules:** Round-robin, territory-based, or account-owner
- **Manager approval gates:** Require approval before high-touch sequences

### Phase 4: Conversation Intelligence
- Auto-categorize replies: positive, negative, OOO, referral, unsubscribe
- Route positive replies to AE for immediate follow-up
- Auto-pause cadence on OOO, resume when they're back
- Flag negative replies for sequence refinement

### Phase 5: Analytics
- Cadence performance: meetings booked per 100 enrollments
- Step performance: which step type/timing drives most replies
- Rep leaderboard: meetings, reply rates, cadence completion
- A/B testing: subject lines, openers, send times

## Output Format
Salesloft setup guide with: cadence library, step configuration, team routing rules,
analytics dashboard, and A/B test plan.



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

- `references/framework-notes.md` — Rhythm cadences, CRM verify gate, enterprise governance
- `references/enrichment-enrollment-gate.md` — CRM lm_email_status before cadence enroll
- `../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md` — verify-before-enroll (Pat Spielmann)
- `../../tools/clay-toolkit/references/gtm-table-blueprints.md` — clay-toolkit CRM field patterns
- `../../tools/clay-loops-toolkit/SKILL.md` — clay-loops-toolkit signal cadences
- `../../../../references/gtm-experts-outbound-index.md` — expert router
- `templates/output-template.md` — CRM fields + cadence + enrollment gate deliverable
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

- Salesloft Modern Selling Framework: apply only the part that directly improves the requested deliverable.
- ColdIQ Cadence Design: apply only the part that directly improves the requested deliverable.
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
- cold-email-strategy, cold-calling, reply-handling, pipeline-management, multi-channel-outreach

---
name: outreach-sequences
description: >-
  Design and manage Outreach sequences — multi-channel cadences, triggers, analytics,
  team workflows. Triggers on: "Outreach sequences", "Outreach cadence", "Outreach 
  setup", "Outreach automation".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: sequencing-tools
  tags: [outreach, sequences, cadence, sales-engagement, outbound]
  frameworks:
    - "Outreach Sequence Best Practices"
    - "ColdIQ Cadence Design"
    - "Outreach — Sales Engagement Cadence Design"
---

# Outreach Sequences

## Overview
Outreach is the enterprise-grade sales engagement platform. Sequences here manage
complex multi-channel, multi-touch cadences with team routing, analytics, and
compliance controls that simpler tools lack.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Outreach Sequence Best Practices.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **ColdIQ Cadence Design.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Outreach — Sales Engagement Cadence Design.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Set up Outreach sequences"
- "Design Outreach cadences"
- "Outreach sequence optimization"
- "Build Outreach workflows"

## Step-by-Step Process

### Phase 1: Sequence Design
Outreach supports complex branching:
- **Linear:** A → B → C → D → E. Simple, predictable. Best for SDR outbound.
- **Branching:** If reply positive → AE handoff. If OOO → pause and retry. If no reply → continue.
- **Multi-channel:** Email → Call → LinkedIn → Email → Call → Social
- **Trigger-based:** Enroll on Salesforce field change, intent signal, or event

### Phase 2: Cadence Architecture
Standard 5-touch cold outbound cadence:
- **Day 1:** Email (problem hypothesis, 50-90 words)
- **Day 3:** LinkedIn connection + note (reference email hint)
- **Day 5:** Call + voicemail (if number available)
- **Day 8:** Email (different angle, proof point)
- **Day 14:** Email (breakup, "closing your file")

### Phase 3: Deliverability Controls
- Max 50 emails/day per mailbox in Outreach
- Rotate across 3-5 mailboxes per rep
- 45-second minimum between sends
- Custom tracking domain for open/click tracking
- Sunset sequences after 3 consecutive bounces

### Phase 4: Team Workflows
- Round-robin assignment from inbound queues
- AE handoff triggers: positive reply, meeting booked, opportunity created
- Manager approval gates for sequences targeting C-suite
- Daily task dashboards per rep with prioritized actions

### Phase 5: Analytics & Optimization
- Funnel metrics: emails sent → opened → replied → meetings → opportunities
- Sequence comparison: which sequence has highest meeting rate per persona
- Rep performance: meetings per 100 touches by rep
- A/B test: subject line and opener variants

## Output Format
Sequence blueprint with: cadence map, step configuration, routing rules, deliverability
settings, and analytics dashboard design.



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

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

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

- Outreach Sequence Best Practices: apply only the part that directly improves the requested deliverable.
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
- cold-email-strategy, multi-channel-outreach, email-deliverability, sending-platforms, pipeline-management

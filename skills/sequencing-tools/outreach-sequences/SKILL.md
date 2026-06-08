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
  frameworks: [Outreach Sequence Best Practices, ColdIQ Cadence Design]
---

# Outreach Sequences

## Overview
Outreach is the enterprise-grade sales engagement platform. Sequences here manage
complex multi-channel, multi-touch cadences with team routing, analytics, and
compliance controls that simpler tools lack.

## Frameworks Referenced

This skill is grounded in named GTM frameworks and operator methodologies, not generic advice:

- **Outreach Sequence Best Practices** — used as the named operating framework for this playbook.
- **ColdIQ Cadence Design** — used as the named operating framework for this playbook.

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

## Related Skills
- cold-email-strategy, multi-channel-outreach, email-deliverability, sending-platforms, pipeline-management

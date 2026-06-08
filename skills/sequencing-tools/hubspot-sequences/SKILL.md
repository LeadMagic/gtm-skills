---
name: hubspot-sequences
description: >-
  Design and optimize HubSpot sequences — enrollment triggers, multi-channel steps, 
  task creation, analytics, A/B testing. Triggers on: "HubSpot sequences", "HubSpot 
  automation", "HubSpot cadence", "sales hub sequences".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: sequencing-tools
  tags: [hubspot, sequences, sales-hub, crm, cadence]
  frameworks: [HubSpot Sequences Best Practices, ColdIQ Multi-Channel Cadence]
---

# HubSpot Sequences

## Overview
HubSpot Sequences power the SDR and AE outbound motion inside Sales Hub.
Done right, they automate touches while maintaining personalization. Done wrong,
they're spam cannons that burn your domain reputation.

## Frameworks Referenced

This skill is grounded in named GTM frameworks and operator methodologies, not generic advice:

- **HubSpot Sequences Best Practices** — used as the named operating framework for this playbook.
- **ColdIQ Multi-Channel Cadence** — used as the named operating framework for this playbook.

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

## Related Skills
- cold-email-strategy, cold-email-copywriting, sending-platforms, inbox-setup, email-deliverability

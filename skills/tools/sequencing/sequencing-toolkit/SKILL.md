---
name: sequencing-toolkit
description: >-
  Complete outreach sequencing toolkit — Smartlead, Instantly, Salesloft,
  Outreach, Lemlist setup and optimization. Covers mailbox rotation, warmup,
  A/B testing, deliverability monitoring, and multi-channel orchestration
  across all major sequencing platforms. Use when setting up or optimizing an
  outreach sequencing platform. Triggers on: "sequencing toolkit",
  "Smartlead setup", "Instantly optimization", "outreach platform comparison".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: tools
  tags: [sequencing, smartlead, instantly, salesloft, outreach, lemlist, cold-email, mailbox-rotation]
  related_skills: [smartlead-workflows, instantly-sequences, salesloft-cadences, outreach-sequences, lemlist-setup, email-deliverability, domain-infrastructure, inbox-setup]
  frameworks:
    - "Smartlead — Unlimited mailboxes, auto-rotation, AI reply categorization"
    - "Instantly — Warmup pool, campaign optimization, unified inbox"
    - "Salesloft — Rhythm cadences, Conversations, multi-channel orchestration"
    - "Outreach — Enterprise sequencing, triggers, analytics"
    - "Lemlist — Personalized images/video, multi-channel sequences"
---

# Sequencing Toolkit

## Overview

Sequencing platforms send your cold emails — but only if configured correctly.
The mistake: importing a list, writing one template, hitting send, and
wondering why deliverability is 40%. This skill covers setup, optimization,
and advanced tactics across all major sequencing platforms.

## Frameworks Referenced

This skill is grounded in named GTM frameworks, public methodologies, and vendor documentation where relevant:

- **Smartlead — Unlimited mailboxes, auto-rotation, AI reply categorization** — used as the named operating framework for this playbook.
- **Instantly — Warmup pool, campaign optimization, unified inbox** — used as the named operating framework for this playbook.
- **Salesloft — Rhythm cadences, Conversations, multi-channel orchestration** — used as the named operating framework for this playbook.
- **Outreach — Enterprise sequencing, triggers, analytics** — used as the named operating framework for this playbook.
- **Lemlist — Personalized images/video, multi-channel sequences** — used as the named operating framework for this playbook.
- **--** — used as the named operating framework for this playbook.
- **[ ] Mailboxes warmed up (2+ weeks) before full volume** — used as the named operating framework for this playbook.
- **[ ] SPF/DKIM/DMARC configured for all sending domains** — used as the named operating framework for this playbook.
- **[ ] Custom tracking domain set up (not shared)** — used as the named operating framework for this playbook.
- **[ ] A/B test running (subject lines + copy variants)** — used as the named operating framework for this playbook.
- **[ ] Reply handling: AI auto-categorization + human escalation rules** — used as the named operating framework for this playbook.
- **[ ] Bounce rate under 3% (investigate if higher)** — used as the named operating framework for this playbook.
- **[ ] Daily send limits per mailbox respected** — used as the named operating framework for this playbook.
- **[Output item 1]** — used as the named operating framework for this playbook.
- **[Output item 2]** — used as the named operating framework for this playbook.
- **[Output item 3]** — used as the named operating framework for this playbook.
- **[ ] All required sections complete** — used as the named operating framework for this playbook.
- **[ ] Output matches the user's stated need** — used as the named operating framework for this playbook.
- **[ ] No vague or unsupported claims** — used as the named operating framework for this playbook.
- **[ ] Frameworks cited where applicable** — used as the named operating framework for this playbook.
- **`smartlead-workflows` — Smartlead-specific setup** — used as the named operating framework for this playbook.
- **`instantly-sequences` — Instantly-specific setup** — used as the named operating framework for this playbook.
- **`cold-email-strategy` — Sequence architecture and cadence** — used as the named operating framework for this playbook.

## When to Use

Trigger phrases: "sequencing platform setup", "Smartlead configuration",
"Instantly optimization", "Salesloft cadences", "Outreach setup",
"Lemlist sequences", "sequence optimization"

## Platform Selection

| Platform | Best For | Key Features | Cost |
|---|---|---|---|
| **Smartlead** | High-volume, multi-mailbox | Unlimited mailboxes, auto-rotation, master inbox | $89-249/mo |
| **Instantly** | Warmup-first, agencies | Largest warmup pool, campaign optimization | $37-97/mo |
| **Salesloft** | Enterprise, multi-channel | Rhythm cadences, Conversation intelligence | $125-165/seat |
| **Outreach** | Enterprise, complex workflows | Sequencing engine, triggers, analytics | $100-160/seat |
| **Lemlist** | Personalized outreach, SMB | AI images/video, multi-channel | $59-99/mo |

## Artifacts

### Standard Sequence Architecture (All Platforms)
```
Email 1 (Day 0): Introduction — problem-focused, 50-75 words
Email 2 (Day 3): Value add — case study or insight, 75-100 words
Email 3 (Day 7): Social proof — customer result, 50-75 words
Email 4 (Day 12): "Breaking up" — last attempt, direct ask
LinkedIn touch (Day 2): Connect request or DM
Call (Day 5): Short voicemail if no answer

Total: 4 emails + 2 multi-channel touches over 14 days
```

### Mailbox Configuration (Smartlead/Instantly)
```
Per domain: 3 mailboxes max. 30 emails/day per mailbox.
3 domains × 3 mailboxes = 9 mailboxes. 9 × 30 = 270 emails/day capacity.
Warmup: 2 weeks minimum before full volume. Start at 5/day. Increment 5/day.
Rotation: Auto-rotate between mailboxes. Randomize send times.
```

## Implementation Checklist

- [ ] Mailboxes warmed up (2+ weeks) before full volume
- [ ] SPF/DKIM/DMARC configured for all sending domains
- [ ] Custom tracking domain set up (not shared)
- [ ] A/B test running (subject lines + copy variants)
- [ ] Reply handling: AI auto-categorization + human escalation rules
- [ ] Bounce rate under 3% (investigate if higher)
- [ ] Daily send limits per mailbox respected

## Common Pitfalls

1. **No warmup.** New mailbox sends 50 emails/day day 1. Spam folder. Burned domain.
   Fix: 2-week warmup. Start at 5/day. Increment slowly.
2. **One mailbox doing everything.** 200 emails/day from one mailbox. Instant spam.
   Fix: Multiple mailboxes per domain. 30/day per mailbox max.
3. **No A/B testing.** Same copy forever. Ignorance about what works. Fix: Always
   run at least one A/B test per sequence.


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

## Related Skills

- `smartlead-workflows` — Smartlead-specific setup
- `instantly-sequences` — Instantly-specific setup
- `cold-email-strategy` — Sequence architecture and cadence
- `email-deliverability` — SPF/DKIM/DMARC, warmup, reputation
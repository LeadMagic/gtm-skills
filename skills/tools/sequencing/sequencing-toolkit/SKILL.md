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
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, GitHub Copilot, Gemini CLI
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

## Quality Checklist

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

## Related Skills

- `smartlead-workflows` — Smartlead-specific setup
- `instantly-sequences` — Instantly-specific setup
- `cold-email-strategy` — Sequence architecture and cadence
- `email-deliverability` — SPF/DKIM/DMARC, warmup, reputation
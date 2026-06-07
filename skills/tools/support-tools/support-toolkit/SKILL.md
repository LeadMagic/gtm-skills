---
name: support-toolkit
description: >-
  Complete customer support tools toolkit — Intercom, Zendesk, Front, Help
  Scout deep-dive configuration, AI agent setup, knowledge base optimization,
  and support analytics. Use when selecting, setting up, or optimizing a
  customer support platform. Triggers on: "support toolkit", "Intercom deep
  setup", "Zendesk configuration", "support platform comparison".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: tools
  tags: [support, intercom, zendesk, front, help-scout, customer-service, chatbots]
  related_skills: [support-tool-stack, headless-support, sla-management, cs-analytics-dashboards, cs-playbooks]
  frameworks:
    - "Intercom — Conversational support, Fin AI, Product Tours"
    - "Zendesk — Omnichannel CX, AI Agents, Explore analytics"
    - "Front — Collaborative inbox, rule-based routing"
    - "Help Scout — Docs-first support, Beacon widget"
---

# Support Toolkit

## Overview

Support tools define how customers experience your company when things go
wrong — and when they need help getting things right. The mistake: buying
the tool your last company used instead of the tool that matches your stage,
team, and support philosophy. This skill covers deep configuration across
the support stack.

## When to Use

Trigger phrases: "support platform setup", "Intercom configuration",
"Zendesk deep setup", "support tool comparison", "AI support agent setup"

## Platform Deep Configuration

### Intercom — Best for Product-Led SaaS
```
Setup checklist:
1. Fin AI agent: train on 30+ help center articles → test 50 real questions
2. Messenger: contextual article suggestions before "talk to human"
3. Macros: 15+ for top ticket types (reset password, billing question, etc.)
4. Product Tours: onboarding flow (guided setup → first value)
5. Series: 3 automated email sequences (onboarding, engagement, expansion)
6. Reports: CSAT (target 4.2+), resolution time (target < 4hrs), volume
```

### Zendesk — Best for Enterprise and Multi-Channel
```
Setup checklist:
1. Ticket fields: type, priority, product area, customer tier
2. SLA policies: P1 (15min FRT), P2 (1hr), P3 (4hr), P4 (8hr)
3. Triggers: auto-assign, auto-respond, escalate on keywords
4. Views: My Open, Unassigned, High Priority, All Open
5. Macros: 20+ for common responses
6. Guide (KB): 30+ articles published before launching chat
7. Explore: team performance dashboard, CSAT trends, volume by channel
```

## Quality Checklist

- [ ] Knowledge base: 30+ articles before launching chat/AI agent
- [ ] AI agent trained and tested with 50 real questions (95%+ correct)
- [ ] Macros: 15+ for top ticket types
- [ ] SLA policies documented with FRT + resolution targets
- [ ] CSAT survey: post-resolution, scores < 3 auto-escalated
- [ ] Escalation path: L1 → L2 → L3 documented with triggers

## Common Pitfalls

1. **AI agent launched without training data.** 5 help articles → 70% wrong
   answers → frustrated customers. Fix: 30+ articles. Test with 50 questions.
2. **Chat widget on every page.** Noise. Distraction. Fix: Pricing, help center,
   and post-signup only.
3. **No SLAs.** "We respond quickly" = no commitment. Fix: Specific FRT targets
   by priority. Measured. Reported. Reviewed weekly.


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

## Common Pitfalls

1. **Incomplete output.** The deliverable is missing critical sections. Fix: verify against the output template before delivering.
2. **Generic advice without specifics.** "Improve your process" without concrete steps. Fix: every recommendation must have a specific action.
3. **Missing framework citations.** Advice without named authorities. Fix: cite the specific framework that grounds each recommendation.
## Related Skills

- `support-tool-stack` — Platform selection by stage
- `headless-support` — AI support agents and KB architecture
- `sla-management` — SLA design and escalation
- `cs-analytics-dashboards` — CS metrics and health scores
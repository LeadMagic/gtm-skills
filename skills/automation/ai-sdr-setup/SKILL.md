---
name: ai-sdr-setup
description: >-
  Deploy AI SDR agents safely and effectively — vendor selection, pilot scope,
  guardrails, signal routing, human handoff design, QA review, and performance
  metrics. Use when setting up 11x, Artisan, AiSDR, Jason AI, or any automated
  SDR workflow for outbound prospecting.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [ai-sdr, automation, prospecting, ai-agents, outbound]
  related_skills: [agent-guardrails, cold-email-strategy, signal-scoring, reply-handling]
  frameworks: [11x AI SDR Deployment Model, ColdIQ Signal-to-Action Routing, Anthropic Tool Use Patterns, Winning by Design Bowtie]
---

# AI SDR Setup

## Overview

Most AI SDR deployments fail because the team treats the agent like a fully autonomous rep instead of a constrained workflow engine. The mistake is giving the agent a list, a writing prompt, and send access before defining quality gates, source-of-truth data, suppression logic, and human handoff rules.

This skill builds an AI SDR launch program that starts narrow, validates message quality, routes the right signals to the right action, and keeps humans in control of anything that can affect brand, compliance, or customer relationships.

## When to Use

Use this skill when the user asks to:

- "set up an AI SDR"
- "automate outbound prospecting"
- "deploy 11x / Artisan / AiSDR / Jason AI"
- "build an AI sales agent"
- "replace manual SDR research"
- "automate prospect research and email drafting"
- "create AI-powered sales development"
- "route buying signals into outbound"
- "design human handoff for AI replies"

Do not use this for generic outbound strategy. Use `cold-email-strategy` first if the user has no ICP, segment, offer, or sequence design.

## Authoritative Foundations

### Anthropic — Tool Use and Human-in-the-Loop Patterns
AI agents should be given constrained tools, clear success criteria, and explicit approval gates for external actions. For SDR work, drafts can be automated, but sending, CRM mutation, and sequence enrollment need controls.

### ColdIQ — Signal-to-Action Routing
ColdIQ's automation patterns map observed signals to deterministic plays: hiring signal → hiring-specific sequence, funding signal → expansion or scale message, job change → champion-tracking play. AI SDRs work best when the routing is deterministic and the writing is assisted.

### Winning by Design — Bowtie Revenue Model
Outbound is only one stage of the revenue bowtie. AI SDRs should optimize for qualified pipeline and customer fit, not raw activity volume. The handoff to AE and CS must preserve context.

### 11x / Artisan / AiSDR / Jason AI — AI SDR Category Patterns
AI SDR platforms converge around the same operating model: data input, account/contact research, sequence generation, reply classification, and human handoff. Vendor choice matters less than workflow control.

## Prerequisites

- ICP definition with exclusions
- Suppression list and existing customer list
- Approved messaging examples
- CRM ownership rules
- Sequencer account with sending limits
- Human reviewer assigned for the pilot
- Metrics baseline from human SDR or previous outbound motion

## Step-by-Step Process

### Phase 1: Scope the Pilot (Day 0)

| Decision | Recommended Starting Point | Why |
|---|---|---|
| Contact count | 100-200 contacts | Enough signal without large brand risk |
| Segment | One ICP segment only | Prevents mixed messaging |
| Channels | Email only at first | Easier QA and compliance |
| Send access | Draft-only for week 1 | Prevents bad autonomous sends |
| Human review | 100% of messages | Builds quality baseline |

Create a pilot charter: target segment, excluded segments, message variants, approval workflow, stop conditions, and success metrics.

### Phase 2: Configure Data Inputs (Day 1-2)

The AI SDR should receive clean inputs, not infer everything itself. Required fields: account name, domain, segment/tier, persona, trigger signal, source URL or evidence, relationship context, and suppression status.

Never let the agent create contacts from vague search prompts without source attribution. Every generated contact needs a source and a verification status before sequencing.

### Phase 3: Build Signal-to-Action Rules (Day 2-3)

| Signal | AI Action | Human Action |
|---|---|---|
| Funding announced | Draft funding-specific opener | Approve target account list |
| Hiring for GTM roles | Draft hiring-pain sequence | Confirm persona relevance |
| Job change | Draft champion/new-role message | Confirm relationship context |
| Competitor mention | Draft displacement email | AE reviews before send |
| Pricing question reply | Classify and escalate | AE responds manually |

The key: the agent does not decide the play from scratch. It selects from approved plays based on observed signal.

### Phase 4: Set Guardrails (Day 3-4)

Hard rules: no sending without approval during pilot, no invented facts, no unsourced claims, no sensitive personal attributes, no suppressed domains, no commitments on price/security/legal/procurement, and no replies after positive intent without human handoff.

### Phase 5: Pilot and QA (Week 1-2)

| Criterion | Pass Standard |
|---|---|
| Relevance | Message ties to account/persona/signal |
| Evidence | Personalization has a source |
| Brevity | Under 90 words for first email |
| CTA | One clear, low-friction ask |
| Compliance | Unsubscribe and suppression respected |
| Voice | Sounds like your company, not generic SaaS |

### Phase 6: Controlled Scale (Week 3-4)

Only scale after quality holds for two consecutive review cycles. Move from 100% human review → 50% sampled review → exception review for high-risk accounts → weekly random QA.

## Output Format

```markdown
# AI SDR Deployment Plan

## Pilot Scope
- Segment:
- Personas:
- Contact count:
- Channels:
- Send permissions:

## Signal-to-Action Matrix
| Signal | Evidence Required | AI Draft | Human Review | Handoff Rule |
|---|---|---|---|---|

## Guardrails
- Hard stop rules:
- Suppression rules:
- Approval gates:

## 4-Week Rollout
Week 1:
Week 2:
Week 3:
Week 4:

## Metrics
- Positive reply rate:
- Meeting conversion:
- Bounce rate:
- Bad-draft rate:
- Human override rate:
```

## Quality Check

Before delivering, verify:

- [ ] Pilot is limited to one ICP segment
- [ ] Human review gates are explicit
- [ ] Suppression and compliance rules are included
- [ ] Every trigger requires source evidence
- [ ] Handoff rules cover positive replies, objections, pricing, security, and legal topics
- [ ] Metrics include quality and safety, not just volume
- [ ] No autonomous send access is recommended before QA passes

## Common Pitfalls

1. **Starting with auto-send.** AI can produce plausible but wrong copy. Fix: draft-only pilot first.
2. **Mixed ICP pilot.** SMB, mid-market, and enterprise require different messages. Fix: one segment per pilot.
3. **No suppression logic.** Agents can accidentally contact customers, competitors, or opted-out contacts. Fix: suppression check before every sequence enrollment.
4. **Measuring only activity.** Emails sent is not success. Fix: track positive replies, meetings, bad-draft rate, and human override rate.
5. **No handoff map.** Agents keep replying when a human should intervene. Fix: hard handoff on positive intent, pricing, security, procurement, or legal.
6. **Unverified personalization.** AI invents reasons to reach out. Fix: require source URL or evidence for every personalized claim.

## Related Skills

- `agent-guardrails` — safety gates for autonomous workflows
- `cold-email-strategy` — sequence and message architecture
- `signal-scoring` — which triggers should activate outreach
- `reply-handling` — classification and escalation rules

---
name: support-tool-stack
description: >-
  Customer support platform selection, setup, and optimization — Intercom,
  Zendesk, Front, Help Scout, HubSpot Service Hub, Linear, and AI-native
  tools. Use when choosing a support platform, migrating tools, setting up
  help desk workflows, designing ticket routing, building macros and saved
  replies, or integrating support with CRM and product. Covers head-to-head
  comparison, pricing by stage, and implementation playbooks.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: customer-success
  tags: [support, intercom, zendesk, help-desk, ticketing, chatbots, customer-service, macros]
  related_skills: [cs-playbooks, sla-management, cs-analytics-dashboards, customer-onboarding, automation/tool-selection-stack]
  frameworks:
    - "Intercom — Conversational Support Framework"
    - "Zendesk — Omnichannel CX Maturity Model"
    - "Help Scout — Support-Driven Growth (Bezos: customer obsession)"
    - "Klaus/Maestro QA — Support Quality Framework"
---

# Support Tool Stack

## Overview

Your support stack determines whether customers feel heard or abandoned. The
mistake: picking the tool your last company used instead of the tool that
matches your current stage, team size, and support philosophy. A 3-person
startup on Zendesk Enterprise ($150/agent/mo) is burning money. A 50-person
team on a shared Gmail inbox is losing customers to slow responses. This
skill covers platform selection, setup, and optimization across every stage
and support philosophy.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Intercom — Conversational Support Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Zendesk — Omnichannel CX Maturity Model.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Help Scout — Support-Driven Growth (Bezos: customer obsession).** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Klaus/Maestro QA — Support Quality Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use

Trigger phrases: "choose support platform", "Intercom vs Zendesk", "help desk
setup", "support tool stack", "migrate support platform", "set up ticketing",
"customer support software", "Front vs Help Scout", "AI support tools",
"help desk comparison"

## Platform Selection by Stage

### Stage 0: Pre-Launch / $0-500K ARR (Founder Doing Support)
**You need:** Shared inbox. Basic knowledge base. Minimal cost.

| Tool | Pricing | Best For |
|---|---|---|
| **Front** | $19-59/seat/mo | Shared inbox with internal comments, assignment |
| **Help Scout** | $20-65/seat/mo | Docs-first support, clean UX, Beacon widget |
| **Linear** | $8-14/seat/mo | If support = bug reports / feature requests |

**Recommendation:** Front if team has Slack workflow. Help Scout if docs-heavy.

### Stage 1: $500K-3M ARR (First CS Hire)
**You need:** Ticketing, SLAs, basic reporting, knowledge base, chat widget.

| Tool | Pricing | Best For |
|---|---|---|
| **Intercom** | $29-85/seat/mo | Conversational support + product tours + outbound |
| **Help Scout** | $20-65/seat/mo | Docs-first, clean workflows, affordable at scale |
| **Zendesk Suite** | $19-115/seat/mo | Enterprise-ready, complex workflows, ITIL |

**Recommendation:** Intercom for product-led SaaS. Help Scout for service-heavy.

### Stage 2: $3-20M ARR (CS Team 2-10 people)
**You need:** Advanced routing, CSAT surveys, SLAs, integrations, analytics.

| Tool | Pricing | Best For |
|---|---|---|
| **Intercom** | $85-132/seat/mo | Full platform: support + product + engagement |
| **Zendesk Suite** | $69-115/seat/mo | Omnichannel (email, chat, phone, social) |
| **Front** | $59-109/seat/mo | High-volume shared inbox, rule-based routing |

**Recommendation:** Intercom if product + support integrated. Zendesk if
multi-channel (phone, social, email).

### Stage 3: $20M+ ARR (CS Team 10+)
**You need:** Omnichannel, workforce management, QA, AI deflection, enterprise SSO.

| Tool | Pricing | Best For |
|---|---|---|
| **Zendesk Suite** | $115-215/seat/mo | Full enterprise: omnichannel, AI agents, workforce mgmt |
| **Intercom** | $132+/seat/mo | Fin AI agent, product-led enterprise |
| **ServiceNow** | Custom | ITIL/ITSM-heavy, regulated industries |

**Recommendation:** Zendesk Enterprise. It's the standard for a reason.

## Platform Deep Dives

### Intercom — Best for Product-Led SaaS

**Core modules:**
- **Inbox:** Shared inbox with team assignments, collision detection
- **Messenger:** In-app chat widget with AI Fin agent (answers from help center)
- **Articles:** Knowledge base, public help center
- **Product Tours:** In-app onboarding flows, feature announcements
- **Series:** Email/chat automation for onboarding, engagement, expansion
- **Tickets:** Back-office ticketing for complex issues
- **Reports:** CSAT, volume, resolution time, team performance

**Setup checklist:**
1. Connect product events → auto-trigger relevant articles in Messenger
2. Set up Fin AI agent with help center content (3+ articles to activate)
3. Configure business hours, auto-reply for after-hours
4. Build 5-10 macros for top ticket types
5. Set up CSAT survey (post-resolution, 5-point scale)
6. Create saved replies library (50+ for common questions)
7. Set up assignment rules (round-robin or skill-based)
8. Integrate with CRM (HubSpot/Salesforce — see tickets in contact timeline)

**Anti-patterns to avoid:**
- Messenger on EVERY page (overwhelming — put on pricing, help, post-signup)
- Fin AI answering questions it can't handle (test thoroughly before launching)
- No macros (CS team retypes the same answers 50x/day)

### Zendesk — Best for Enterprise and Multi-Channel

**Core modules:**
- **Support:** Ticketing, SLAs, macros, triggers, automations
- **Guide:** Help center, knowledge base, community forums
- **Chat:** Live chat widget, AI Answer Bot
- **Talk:** Voice/phone support with screen pops
- **Explore:** Analytics and reporting (pre-built dashboards)
- **Sunshine:** CRM platform (custom objects, workflows)

**Setup checklist:**
1. Define ticket fields (type, priority, product area, customer tier)
2. Set up SLA policies (first response time, resolution time by priority)
3. Create triggers (auto-assign, auto-respond, escalate based on keywords)
4. Build views (My Open Tickets, Unassigned, High Priority, All Open)
5. Set up macros (15-20 for common responses)
6. Configure business hours and schedules
7. Set up CSAT survey (automated post-resolution)
8. Create Guide help center with 20+ articles
9. Integrate with CRM, product analytics, and Slack
10. Set up Explore dashboards for team performance

**Anti-patterns to avoid:**
- Too many ticket fields (agents spend more time categorizing than solving)
- Overly complex triggers (hard to debug, unexpected side effects)
- No CSAT follow-up (negative scores without follow-up = churn risk)

### Front — Best for Team Collaboration

**Philosophy:** Email-first, with internal comments and shared drafts replacing
the "forward to colleague → they reply → forward back" dance.

**Key features:**
- Shared inbox with internal-only comments
- Collision detection (two people can't reply simultaneously)
- Rules engine for auto-tagging, assignment, routing
- Sequences for automated follow-ups
- Analytics: response time, resolution time, volume by channel

**Best for:** Teams that get most inquiries via email and need collaborative
reply workflows. Not great for chat-first or phone-heavy support.

### Help Scout — Best for Documentation-First Support

**Philosophy:** "If you do docs right, support volume drops." The Beacon widget
surfaces relevant articles BEFORE the customer messages you.

**Key features:**
- Docs (knowledge base) tightly integrated with Inbox
- Beacon widget: contextual article suggestions in-app
- Saved replies, collision detection, workflows
- Lightweight CRM (customer profiles, conversation history)

**Best for:** Startups that want clean, affordable support without Intercom's
complexity. Companies with strong documentation culture.

## AI Support Tools

| Tool | What It Does | Best For |
|---|---|---|
| **Intercom Fin** | AI agent answers from help center | Deflecting tier-1 questions |
| **Zendesk AI Agents** | Auto-resolve, suggest macros, triage | Enterprise auto-resolution |
| **Ada** | No-code chatbot builder | Complex conversation flows |
| **Forethought** | AI agent with ticket deflection | Reducing ticket volume |
| **Kapiche** | AI-powered CSAT/NPS text analysis | Understanding WHY scores change |
| **Klaus/Maestro** | Conversation review / QA scoring | Support quality management |
| **Gong/Chorus for CS** | Call recording + AI analysis | CSM call coaching |

## Output Format

```
SUPPORT TOOL STACK — [Company]

Current Stage: [0/1/2/3]
Current ARR: $X M
CS Team Size: X

Selected Platform: [Intercom / Zendesk / Front / Help Scout / HubSpot Service]
Monthly Cost: $X/month ($X/seat × X seats)

Setup Checklist:
[Platform-specific setup items — 8-12 items]

Integrations:
- CRM: [HubSpot / Salesforce / Attio] — sync tickets to contact timeline
- Product: [Segment / Amplitude / Mixpanel] — see product usage alongside tickets
- Slack: ticket creation + alerts
- Knowledge Base: migrate existing docs to [platform] help center

Macros / Saved Replies (top 15):
1. [Type] — [response template]
2. ...

SLAs:
- First response: X hours (business hours)
- Resolution: X hours/days (by priority)
- P1 (critical): X min/hours
- P2 (high): X hours
- P3 (normal): X hours/days
- P4 (low): X days

CSAT Survey:
- Timing: [post-resolution / periodic]
- Scale: [5-point / CSAT / NPS]
- Follow-up: auto-escalate scores < X to manager
```

## Implementation Checklist

- [ ] Platform matches stage (don't overbuy — Front at $19/seat may suffice for stage 0)
- [ ] SLAs defined with specific time targets, not "ASAP"
- [ ] 15+ macros/saved replies for top ticket types
- [ ] CSAT survey configured (post-resolution, not manual)
- [ ] Knowledge base has 20+ articles before launching chat widget
- [ ] AI agent tested with real questions before customer-facing
- [ ] CRM integration shows support tickets in contact timeline
- [ ] Business hours and auto-reply configured for after-hours
- [ ] Team trained on all macros, collision detection, and internal notes

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Overbuying for stage.** Zendesk Enterprise at $115/seat for a 2-person CS
   team is lighting money on fire. Fix: Match platform to stage. Upgrade when
   you need the features, not before.

2. **No macros at launch.** CS team retyping the same 10 responses 50x/day is
   slow, inconsistent, and demoralizing. Fix: Build 15+ macros before go-live.
   Iterate weekly from actual tickets.

3. **Chat widget on every page.** Messenger/Beacon on every page = noise. Fix:
   Put on pricing page (pre-sales questions), help center (support), and
   post-signup (onboarding). Not on blog, homepage, or logged-out marketing
   pages.

4. **AI agent without training data.** Launching Fin or Answer Bot with 3 help
   articles produces wrong answers and angry customers. Fix: 20+ articles
   minimum. Test with 50+ real customer questions before launch.

5. **No CSAT follow-up.** Collecting "1/5" ratings without human follow-up
   sends the message: "We don't actually care." Fix: Auto-escalate scores < 3
   to manager for personal follow-up within 24 hours.

6. **Ignoring the knowledge base.** Most support volume comes from the same 20
   questions. If they're all documented, ticket volume drops 30-60%. Fix:
   Write articles from actual tickets. Every ticket that gets the same answer
   3x becomes a help center article.

## Related Skills

- `cs-playbooks` — Onboarding, health scoring, CSQLs, churn intervention
- `sla-management` — SLA design, ticket routing, escalation, priority matrices
- `cs-analytics-dashboards` — CS metrics, NPS, CSAT, health scoring
- `customer-onboarding` — Structured onboarding, time-to-value, activation
- `automation/tool-selection-stack` — Stage-appropriate GTM tool stacks

---
name: headless-support
description: >-
  Design and deploy headless / automated support systems — AI chatbots, Fin AI
  agents, knowledge base self-serve portals, ticket deflection strategies,
  automated triage, email auto-responders, and conversational AI. Use when
  building self-serve support, implementing AI agents for tier-1 deflection,
  designing knowledge base architecture, or automating support workflows to
  scale CS without linear headcount growth.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: customer-success
  tags: [headless-support, ai-chatbot, self-serve, knowledge-base, ticket-deflection, automation, fin-ai, conversational-ai]
  related_skills: [support-tool-stack, cs-playbooks, sla-management, cs-analytics-dashboards, customer-onboarding]
  frameworks:
    - "Intercom — Fin AI Agent and Resolution Bot"
    - "Zendesk — AI Agents and Answer Bot"
    - "Ada — Conversational AI for Support"
    - "Forethought — AI-First Customer Support"
    - "Amazon — Working Backwards (deflection reduces cost and improves CSAT)"
---

# Headless Support

## Overview

Every support ticket costs $15-50 in human time. Deflecting 40% of tickets
with self-serve and AI agents isn't just cost savings — it's better customer
experience. Customers want answers in seconds, not hours. The mistake: thinking
"headless support" means "no support." It means "answers without waiting." This
skill covers AI agent deployment, knowledge base architecture, ticket deflection
strategy, and the metrics to prove headless support works.

## When to Use

Trigger phrases: "set up AI support agent", "build self-serve support",
"ticket deflection strategy", "headless customer support", "automated support",
"Fin AI setup", "knowledge base optimization", "reduce support tickets",
"chatbot for support", "automated onboarding support", "self-serve portal"

## The Deflection Funnel

```
Customer Has Question
    │
    ▼
[Level 0: Product] — In-app tooltips, empty states, contextual help
    │ ~30% resolved here
    ▼
[Level 1: Knowledge Base] — Search, suggested articles, help center
    │ ~25% resolved here
    ▼
[Level 2: AI Agent / Chatbot] — Conversational, trained on KB + past tickets
    │ ~25% resolved here
    ▼
[Level 3: Human Agent] — Complex, sensitive, escalated issues
    │ ~20% (your goal: push this number DOWN)
```

**Target:** 80%+ of inquiries resolved WITHOUT human intervention.

## Step-by-Step Process

### Phase 1: Knowledge Base Architecture

**The foundation of headless support.** AI agents are only as good as the
content they're trained on.

**Article architecture (30-50 articles minimum for effective deflection):**

| Category | Articles | Examples |
|---|---|---|
| Getting Started | 5-10 | Account setup, team invites, first campaign |
| Core Features | 15-20 | Step-by-step guides for every major feature |
| Billing & Account | 5-8 | Plans, invoices, upgrade/downgrade, cancel |
| Troubleshooting | 10-15 | Common errors, workarounds, fixes |
| Integrations | 5-10 | Setup guides for each integration |
| Best Practices | 5-8 | Pro tips, workflows, customer examples |
| FAQ | 10-15 | Short answers to most common questions |

**Article quality standards:**
1. Title = the exact question customers ask: "How do I connect my CRM?" not
   "CRM Integration Overview"
2. Answer in first paragraph (no fluff, no "In this article we'll cover...")
3. Screenshots for every step (Loom video for complex workflows)
4. "Next steps" section: related articles, contact support if stuck
5. Updated monthly — stale KB articles erode trust

**SEO for your own KB (customers use Google to find you):**
- Article titles match search intent: "How to export contacts from [Product]"
- Meta descriptions under 155 characters with the answer
- Internal linking between related articles
- Google indexes your help center — make it findable

### Phase 2: AI Agent Deployment

**Pre-deployment checklist:**
- [ ] 30+ help center articles published (minimum for effective AI)
- [ ] 100+ past tickets reviewed to identify top deflection opportunities
- [ ] AI persona defined: "Friendly, expert, concise. Uses customer's name. Admits when it can't answer."
- [ ] Escalation path designed: what triggers handoff to human?
- [ ] Test suite: 50 real customer questions run through AI, every answer reviewed

**AI agent configuration (Intercom Fin / Zendesk AI as models):**

```
AI PERSONA: [Product] Support Assistant

Voice: Friendly, expert, concise (2-3 sentences max per answer)
Rules:
- Answer from help center articles only (don't hallucinate)
- If unsure: "Great question — let me connect you with a specialist who can help"
- Never: guess, make promises, give legal/security advice, be defensive
- Always: use customer's name, link to relevant article, offer human escalation

Escalation triggers (auto-handoff to human):
- Customer types: "talk to human", "agent", "real person"
- Customer frustration detected: multiple rephrases, ALL CAPS, "this is useless"
- Billing issues (high-stakes, emotional — human handles these)
- Security/privacy questions (never AI — legal risk)
- Enterprise customer + P1 issue (revenue at risk = human)
```

**Testing protocol:**
1. Run 50 historical tickets through AI agent
2. Score each response: Correct / Partially Correct / Wrong
3. Fix articles for any "Partially Correct" or "Wrong" responses
4. Re-run until 95%+ correct on test set
5. Launch to 10% of customers (canary), monitor for 1 week
6. Ramp to 50%, then 100%

### Phase 3: In-Product Self-Serve

**Contextual help (Level 0 — before they search):**

| Surface | Method | Example |
|---|---|---|
| Empty states | Explain what goes here + link to setup guide | "No campaigns yet. Start your first →" |
| Hover tooltips | 1-sentence explanation of each field | "Bounce rate: % of emails that couldn't be delivered" |
| Feature announcement | In-app modal with 3-step walkthrough | "New: Auto-rotate mailboxes. Here's how →" |
| Error messages | What happened + how to fix + link to article | "Domain not verified. 2-min fix →" |
| Setup wizard | Step-by-step onboarding flow | 1. Connect inbox 2. Add team 3. Send first campaign |

**Principle:** Answer the question BEFORE they ask it. Every place a customer
could get stuck, put the answer. This is the highest-ROI deflection — it
costs nothing and prevents tickets entirely.

### Phase 4: Automated Triage and Routing

**For tickets that DO reach human agents, automate the triage:**

```
AUTO-TRIAGE RULES:

IF: keywords "can't login", "password", "2FA", "locked out"
THEN: Priority = P1, Assign to = Auth team, Auto-reply = "Our auth team is on this — expect a response within 15 minutes"

IF: keywords "billing", "invoice", "charge", "refund", "cancel"
THEN: Priority = P1, Assign to = Billing team, Tag = billing

IF: keywords "bug", "not working", "error", "broken", "glitch"
THEN: Tag = bug, Assign to = Tier-2 technical queue

IF: keyword "feature request" OR "wish you had" OR "why don't you"
THEN: Tag = feature-request, Assign to = product-feedback (not support queue)

IF: sender is enterprise-tier customer
THEN: Priority = escalate by 1 level, Assign to = dedicated CSM
```

**Auto-responders that set expectations:**
```
P1 (Critical — system down, can't login):
"Got it. Our team is on this right now. You'll hear back within 15 minutes.
Reference: [ticket #]"

P2 (High — feature broken, workflow blocked):
"Thanks for reporting this. We'll have eyes on it within 2 hours. Track
progress: [link to ticket]"

P3 (Normal — question, configuration help):
"Thanks for reaching out. You'll hear from us within 4 hours. In the
meantime, these articles might help: [3 relevant links]"
```

### Phase 5: Measuring Deflection

**Core deflection metrics:**

| Metric | Formula | Target |
|---|---|---|
| Deflection Rate | Questions Answered by AI ÷ Total Questions | 40%+ (startup), 60%+ (scale) |
| Self-Serve Rate | KB article views ÷ (KB views + tickets created) | 3:1 or higher |
| AI CSAT | AI conversation CSAT score | Within 10% of human CSAT |
| Escalation Rate | AI conversations escalated to human | Under 30% |
| Resolution Time (AI) | Median time per AI-resolved question | Under 5 minutes |
| Cost per Resolution | Total support cost ÷ total resolutions | Target: $5-10 (AI), $20-50 (human) |

**Dashboard to track:**
```
HEADLESS SUPPORT DASHBOARD

| Metric | This Month | Last Month | Trend |
|---|---|---|---|
| Total Inquiries | 1,200 | 1,100 | ↑9% |
| Self-Serve (KB) | 480 (40%) | 375 (34%) | ↑6pp |
| AI Resolved | 360 (30%) | 330 (30%) | — |
| Human Resolved | 360 (30%) | 395 (36%) | ↓6pp |
| AI CSAT | 4.2/5 | 4.1/5 | ↑0.1 |
| Human CSAT | 4.4/5 | 4.4/5 | — |
| Cost Saved (vs full human) | $7,200 | $5,900 | ↑22% |
```

## Output Format

```
HEADLESS SUPPORT PLAN — [Company]

Current State:
- Monthly tickets: X
- CS team size: X
- Current deflection: X% (KB + AI)
- Current cost/ticket: $X

Target State (6 months):
- Deflection target: X%
- AI CSAT target: 4.X/5
- Human tickets to reduce by: X%
- Cost savings target: $X/month

Implementation Phases:
Phase 1 (Month 1): Knowledge Base Audit
  - Audit existing articles for completeness + accuracy
  - Write 20 new articles based on top ticket types
  - Add contextual help to top 5 confusion points

Phase 2 (Month 2): AI Agent Launch
  - Configure AI persona and escalation rules
  - Test with 50 historical tickets
  - Launch canary (10% of customers)

Phase 3 (Month 3): Optimize
  - Review AI performance data
  - Refine articles based on failed deflections
  - Expand to 100% of customers

Phase 4 (Month 4+): Continuous Improvement
  - Weekly review of AI conversations
  - Monthly KB refresh
  - Quarterly deflection rate target review
```

## Quality Checklist

- [ ] 30+ help center articles published with screenshot + step-by-step
- [ ] AI persona documented (voice, escalation rules, prohibited topics)
- [ ] 50 historical tickets tested through AI — 95%+ correct
- [ ] Escalation triggers configured (frustration, billing, security, enterprise)
- [ ] In-product contextual help at top 10 confusion points
- [ ] Auto-triage rules for ticket routing by keyword, priority, customer tier
- [ ] Auto-responders configured for P1/P2/P3 with specific time expectations
- [ ] Deflection dashboard live with weekly review cadence
- [ ] CSAT survey collects AI-rating vs human-rating separately

## Common Pitfalls

1. **AI agent launched too early.** 5 help articles and an AI agent = 70% wrong
   answers, frustrated customers, and damaged trust. Fix: 30+ articles minimum.
   Test with 50 real questions before launch.

2. **No escape hatch.** AI agent that can't escalate to human is a customer
   experience disaster. Fix: Clear escalation triggers. "Talk to human" must
   always work. Never trap a customer in a bot loop.

3. **AI persona mismatch.** A chirpy, emoji-filled support bot for an
   enterprise security product is tone-deaf. Fix: Match AI persona to brand
   voice. Professional for enterprise, friendly for SMB.

4. **Not measuring CSAT per channel.** If AI CSAT is 3.8 and human CSAT is 4.5,
   you're degrading experience to save money. Fix: Track CSAT separately for
   AI and human. If AI CSAT drops below 90% of human CSAT, pause and fix.

5. **Static knowledge base.** Articles written once and never updated become
   wrong, then dangerous. Fix: Monthly KB review. Owner assigned per category.
   Every product release triggers KB updates.

6. **Deflection as the only goal.** "100% deflection = 0 support tickets" sounds
   great but means you're not hearing from customers. Some tickets are valuable
   product feedback. Fix: Deflect repetitive questions. Keep product feedback
   and enterprise escalations human-handled.

## Related Skills

- `support-tool-stack` — Intercom, Zendesk, Front, Help Scout comparison and setup
- `cs-playbooks` — Onboarding, health scoring, CSQLs, churn intervention
- `sla-management` — SLA design, escalation paths, priority matrices
- `cs-analytics-dashboards` — CS metrics, NPS, CSAT, health scoring
- `customer-onboarding` — Structured onboarding, time-to-value, activation
---
name: smartlead-workflows
description: >-
  Set up and run Smartlead — unlimited mailboxes, auto-rotation, A/B testing,
  master inbox, AI categorization. Triggers on: "Smartlead", "Smartlead setup",
  "Smartlead campaigns", "unlimited mailboxes".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: tools
  tags: [smartlead, cold-email, mailboxes, auto-rotation, outbound]
  frameworks:
    - "Smartlead Best Practices"
    - "Eric Nowoslawski Cold Email Infrastructure"
    - "Outreach — Sales Engagement Cadence Design"
---

# Smartlead Workflows

## Overview
Smartlead is the cold email platform of choice for high-volume senders.
Its killer features: unlimited mailboxes, automatic mailbox rotation, AI reply
categorization, and a unified master inbox. This skill covers setup from 0 to
sending at scale.

## Authoritative Foundations

- **Smartlead Best Practices** — Unlimited mailboxes, master inbox, and agency-scale cold email ops.
- **Eric Nowoslawski Cold Email Infrastructure** — Cold email infra at scale — 2 inboxes/domain, backup inboxes, Creative Ideas testing.
- **Outreach — Sales Engagement Cadence Design** — Sequence governance, task-based selling, and CRM-locked cadences.

## When to Use
- "Set up Smartlead"
- "Smartlead campaign setup"
- "Add mailboxes to Smartlead"
- "Smartlead optimization"

## Step-by-Step Process

### Phase 1: Infrastructure Setup
Before creating a single campaign:
- Connect 3-5 sending domains per client (secondary domains, not primary)
- Add 2-3 mailboxes per domain (Google Workspace or M365)
- Verify DNS: SPF, DKIM, DMARC, custom tracking domain
- Warm up each mailbox 2-3 weeks before sending (start 5/day, ramp to 50/day)
- Set up master inbox: unified view of all replies across all mailboxes

### Phase 2: Campaign Creation
Per campaign:
- **Lead list:** Upload CSV, map fields, segment by persona
- **Sequence:** 3-5 step sequence, plain text only, no images/HTML
- **Mailbox assignment:** Auto-rotate across 15-25 mailboxes, max 30-50 emails/day/mailbox
- **Sending window:** Mon-Thu 6am-8pm prospect timezone, 45-90 second delay between sends
- **Tracking:** Open tracking OFF (hurts deliverability in 2026), reply tracking ON

### Phase 3: AI Reply Categorization
Train Smartlead's AI to categorize replies:
- **Positive:** "Interested," "Let's talk," "Send more info" → label INTERESTED
- **Neutral:** "Not now," "Maybe next quarter" → label NOT NOW
- **OOO:** Auto-replies, vacation → label OOO, auto-pause
- **Negative:** "Stop emailing," "Remove me" → label UNSUBSCRIBE, auto-block
- **Wrong person:** "I'm not the right person" → label WRONG CONTACT, flag for update

### Phase 4: A/B Testing
Test at campaign level:
- **Subject line:** 2-4 variants, rotate evenly, measure reply rate
- **Opener:** Different hook patterns, same body
- **CTA:** Soft vs direct, measure meeting rate
- **Send time:** Morning vs afternoon by timezone, auto-optimize

### Phase 5: Analytics & Optimization
- **Campaign health:** Reply rate (>2% healthy), bounce rate (<3% healthy), spam rate (<0.1%)
- **Mailbox health:** Per-mailbox bounce and spam rates, rotate out unhealthy mailboxes
- **Sequence optimization:** Which step drives most replies, trim low-performing steps
- **A/B winner declaration:** After 500+ sends per variant, declare winner and auto-apply

## Output Format
Smartlead setup playbook with: infrastructure checklist, campaign configuration,
AI categorization rules, A/B test plan, and optimization cadence.



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

- `references/framework-notes.md` — Eric Smartlead scale, Pat verify gate, AI categorization
- `templates/output-template.md` — infrastructure + AI labels + Clay gate deliverable
- `scripts/check-output.py` — local checklist validator
This skill includes lightweight artifacts the agent can load on demand:
- `references/clay-enrollment-handoff.md` — Clay/loops → Smartlead push + custom variables
- `../../outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md` — Eric Nowoslawski agency infra (canonical Smartlead operator)
- `../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md` — verify-before-send (Pat Spielmann)
- `../../tools/clay-loops-toolkit/references/leadmagic-waterfall.md` — loop enrich chain before push
- `../../leadmagic/leadmagic-cli/references/cli-workflow-patterns.md` — `lm integrations smartlead push`
- `../../../../references/gtm-experts-outbound-index.md` — expert router
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

- Smartlead Best Practices: apply only the part that directly improves the requested deliverable.
- Eric Nowoslawski Cold Email Infrastructure: apply only the part that directly improves the requested deliverable.
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
- email-deliverability, domain-infrastructure, inbox-setup, cold-email-strategy, cold-email-copywriting

---
name: instantly-sequences
description: >-
  Set up Instantly — unlimited accounts, warmup pool, campaign optimization, unified 
  inbox. Triggers on: "Instantly", "Instantly setup", "Instantly campaigns", "Instantly warmup".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: tools
  tags: [instantly, cold-email, warmup, outbound, campaigns]
  frameworks:
    - "Instantly Best Practices"
    - "Cold Email Infrastructure Standards"
    - "Outreach — Sales Engagement Cadence Design"
---

# Instantly Sequences

## Overview
Instantly competes with Smartlead in the high-volume cold email space. Key features:
unlimited email accounts, built-in warmup pool, campaign optimization, and a unified
inbox. This skill covers setup from infrastructure through optimization.

## Authoritative Foundations

- **Instantly Best Practices** — Mailbox rotation, campaign caps, and deliverability-first sending setup.
- **Cold Email Infrastructure Standards** — Named methodology governing recommendations in this skill's process.
- **Outreach — Sales Engagement Cadence Design** — Sequence governance, task-based selling, and CRM-locked cadences.

## When to Use
- "Set up Instantly"
- "Instantly campaign setup"
- "Instantly warmup"
- "Optimize Instantly campaigns"

## Step-by-Step Process

### Phase 1: Account Infrastructure
- Buy secondary domains (never use primary domain)
- Set up 2-3 Google Workspace or M365 mailboxes per domain
- Configure DNS: SPF, DKIM, DMARC, custom tracking domain
- Connect all mailboxes to Instantly
- Begin warmup: Instantly auto-sends from your mailboxes to its warmup pool
  and auto-replies to build reputation. Run 2-3 weeks before launching.

### Phase 2: Campaign Setup
- **Import leads:** CSV upload with mapped fields, verify emails before sending
- **Sequence builder:** Unlimited email steps, delays between 1-7 days
- **A/B testing:** Up to 26 variants per campaign, auto-rotate, declare winner
- **Sending schedule:** Mon-Fri with timezone optimization, max 50 emails/day/account
- **Account rotation:** Auto-rotate across connected accounts, no account sends >50/day

### Phase 3: Campaign Rules
- Auto-pause on X consecutive bounces
- Auto-remove from sequence on unsubscribe request
- Auto-label replies by sentiment (AI categorization)
- Duplicate detection: don't send to the same email across campaigns
- Blocklist management: automatically suppress unsubscribes across all campaigns

### Phase 4: Unified Inbox
- All replies across all accounts in one view
- Reply from any connected account in one interface
- Auto-label: interested, not interested, OOO, wrong person
- Lead status sync: update CRM based on reply categorization

### Phase 5: Optimization
- Campaign analytics: open rate, reply rate, bounce rate, spam rate
- Account analytics: per-account health score, warmup status, reputation
- A/B winner: auto-declare after statistical significance, apply winner
- Sequence optimization: prune low-performing steps, extend high-performing ones

## Output Format
Instantly playbook with: infrastructure checklist, campaign configuration, account
management plan, inbox workflow, and optimization cadence.



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

- `references/framework-notes.md` — Eric infra, Pat verify gate, tool boundaries
- `templates/output-template.md` — infrastructure + campaign + Clay gate deliverable
- `scripts/check-output.py` — local checklist validator for required sections
This skill includes lightweight artifacts the agent can load on demand:
- `references/clay-enrollment-handoff.md` — Clay/loops → Instantly field map + verify gate
- `../../outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md` — infra at scale (Eric Nowoslawski)
- `../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md` — verify-before-send (Pat Spielmann)
- `../../tools/clay-toolkit/SKILL.md` — clay-toolkit upstream enrichment
- `../../tools/clay-loops-toolkit/references/loop-catalog.md` — signal loop routing
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

- Instantly Best Practices: apply only the part that directly improves the requested deliverable.
- Cold Email Infrastructure Standards: apply only the part that directly improves the requested deliverable.
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
- email-deliverability, domain-infrastructure, inbox-setup, cold-email-strategy, reply-handling

---
name: instantly-sequences
description: >-
  Set up Instantly — unlimited accounts, warmup pool, campaign optimization, unified 
  inbox. Triggers on: "Instantly", "Instantly setup", "Instantly campaigns", "Instantly warmup".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: sequencing-tools
  tags: [instantly, cold-email, warmup, outbound, campaigns]
  frameworks: [Instantly Best Practices, Cold Email Infrastructure Standards]
---

# Instantly Sequences

## Overview
Instantly competes with Smartlead in the high-volume cold email space. Key features:
unlimited email accounts, built-in warmup pool, campaign optimization, and a unified
inbox. This skill covers setup from infrastructure through optimization.

## Frameworks Referenced

This skill is grounded in named GTM frameworks and operator methodologies, not generic advice:

- **Instantly Best Practices** — used as the named operating framework for this playbook.
- **Cold Email Infrastructure Standards** — used as the named operating framework for this playbook.

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

## Related Skills
- email-deliverability, domain-infrastructure, inbox-setup, cold-email-strategy, reply-handling

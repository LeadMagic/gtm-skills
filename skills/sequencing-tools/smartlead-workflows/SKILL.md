---
name: smartlead-workflows
description: >-
  Set up and run Smartlead — unlimited mailboxes, auto-rotation, A/B testing,
  master inbox, AI categorization. Triggers on: "Smartlead", "Smartlead setup",
  "Smartlead campaigns", "unlimited mailboxes".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: sequencing-tools
  tags: [smartlead, cold-email, mailboxes, auto-rotation, outbound]
  frameworks: [Smartlead Best Practices, Eric Nowoslawski Cold Email Infrastructure]
---

# Smartlead Workflows

## Overview
Smartlead is the cold email platform of choice for high-volume senders.
Its killer features: unlimited mailboxes, automatic mailbox rotation, AI reply
categorization, and a unified master inbox. This skill covers setup from 0 to
sending at scale.

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

## Related Skills
- email-deliverability, domain-infrastructure, inbox-setup, cold-email-strategy, cold-email-copywriting

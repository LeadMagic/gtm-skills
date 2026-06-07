---
name: lifecycle-drips
description: >-
  Design lifecycle drip campaigns — post-purchase, renewal, expansion, milestone-based
  automated email programs. Triggers on: "lifecycle drips", "automated campaigns",
  "lifecycle emails", "drip sequences", "triggered emails".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: lifecycle
  tags: [lifecycle, drips, automation, triggered-emails, lifecycle-marketing]
  frameworks: [Lifecycle Marketing Framework, HubSpot Lifecycle Stages]
---

# Lifecycle Drip Campaigns

## Overview
Lifecycle drips are automated email sequences triggered by customer milestones —
signup, first value, renewal window, expansion trigger, at-risk behavior.
These run in the background, nurturing customers through their journey without
manual intervention. This skill covers the complete lifecycle drip architecture.

## When to Use
- "Build lifecycle emails"
- "Customer drip campaigns"
- "Automated lifecycle marketing"
- "Trigger-based customer emails"
- "Lifecycle automation"

## Step-by-Step Process

### Phase 1: Lifecycle Stage Mapping
Define the stages every customer moves through:

1. **Visitor → Lead:** Form fill, content download, signup. Trigger: welcome email.
2. **Lead → MQL:** Engagement threshold reached. Trigger: nurture sequence.
3. **MQL → SQL:** High intent signals. Trigger: sales handoff + confirmation.
4. **SQL → Opportunity:** Deal created. Trigger: "what to expect during evaluation."
5. **Opportunity → Customer:** Deal closed-won. Trigger: onboarding sequence.
6. **Customer → Active User:** Aha moment achieved. Trigger: "what's next" + power tips.
7. **Active User → Power User:** Advanced features adopted. Trigger: case study request,
   community invite, reference program.
8. **At-Risk:** Usage drops, support tickets spike. Trigger: health intervention sequence.
9. **Churned:** Cancellation. Trigger: exit survey + win-back sequence.

### Phase 2: Trigger Definition
For each transition, define the exact trigger:
- **Behavioral:** User completed X action (e.g., sent first campaign)
- **Time-based:** X days since signup with no key action
- **Score-based:** Health score drops below threshold
- **Event-based:** Contract renewal date approaching (90/60/30 days out)
- **Manual:** CSM marks account as needing intervention

### Phase 3: Drip Architecture

**Welcome Drip (Days 0-7):**
- Email 1 (instant): Welcome + what to expect + first action
- Email 2 (Day 2): "Did you try [first action]?" + quickstart guide
- Email 3 (Day 5): Social proof: "Teams like yours achieve [result] with [product]"
- Email 4 (Day 7): "Ready for step 2?" + feature highlight

**Renewal Drip (90/60/30/14/7 days before renewal):**
- 90 days: "Your renewal is coming up — here's what you've accomplished this year"
  (usage summary, ROI report)
- 60 days: "New features since you started" + roadmap preview
- 30 days: Customer success check-in. "Still getting value? What could be better?"
- 14 days: Renewal offer. "Renew by [date] for [benefit: locked pricing, bonus]"
- 7 days: Final reminder. "Don't lose access to [key feature they use heavily]"

**Expansion Drip (triggered by usage nearing plan limits):**
- Email 1: "You're approaching your plan limit — here's what that means"
- Email 2: "Teams at your usage level typically upgrade for [specific benefit]"
- Email 3: "Custom plan options — let's find the right fit"

### Phase 4: Personalization at Scale
- **Usage data:** "You've sent 4,237 emails this month..."
- **Achievement milestones:** "Congrats on your 1,000th enrichment!"
- **Industry benchmarks:** "Fintech companies your size typically [behavior]"
- **Role-based:** Different emails for the admin/buyer vs the end user

### Phase 5: Measurement & Optimization
- **Drip completion rate:** % who receive all emails in the sequence
- **Stage conversion rate:** % who move from stage N to N+1
- **Time in stage:** Median days in each lifecycle stage
- **Revenue per stage:** Average revenue of customers at each stage
- **Drip attribution:** Pipeline and revenue influenced by lifecycle drips
- **A/B test:** Subject lines, offers, timing, channel mix

## Output Format
Lifecycle drip architecture with: stage map, trigger definitions, email sequences
per stage, personalization strategy, and optimization framework.

## Related Skills
- mql-nurture, onboarding-sequences, re-engagement, churn-prevention, cs-playbooks

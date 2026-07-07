---
name: lifecycle-drips
description: >-
  Design lifecycle drip campaigns — post-purchase, renewal, expansion, milestone-based
  automated email programs. Triggers on: "lifecycle drips", "automated campaigns",
  "lifecycle emails", "drip sequences", "triggered emails".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: lifecycle
  tags: [lifecycle, drips, automation, triggered-emails, lifecycle-marketing]
  frameworks:
    - "Lifecycle Marketing Framework"
    - "HubSpot Lifecycle Stages"
    - "Reforge — Lifecycle Marketing"
---

# Lifecycle Drip Campaigns

## Overview

Lifecycle drips are automated email sequences triggered by customer milestones —
signup, first value, renewal window, expansion trigger, at-risk behavior.
These run in the background, nurturing customers through their journey without
manual intervention. This skill covers the complete lifecycle drip architecture.

## Authoritative Foundations

- **Lifecycle Marketing Framework** — Startup operating cadence — default alive, talk to users, launch fast.
- **HubSpot Lifecycle Stages** — Lifecycle stages, object model, and workflow enrollment patterns.
- **Reforge — Lifecycle Marketing** — Startup operating cadence — default alive, talk to users, launch fast.

## Lifecycle Stage

Spans **Activation → Referral** (stages 3–7). Stage map → `references/gtm-lifecycle-stages.md`.  
Post-activation triggers → `references/activation-playbook.md` (handoff to engagement).  
Router → `references/lifecycle-skill-index.md`.

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

## Quality Check

Before delivering, verify:

- [ ] All 9 lifecycle stages (Visitor through Churned) have at least one associated drip sequence
- [ ] Every drip trigger is measurable — behavioral events, time-based rules, score thresholds, or manual flags — not vague 'engagement'
- [ ] Welcome drip starts within minutes of signup (automation delay <5 minutes) and completes within 7 days
- [ ] Renewal drip begins at 90 days with ROI summary, not at 14 days with a discount
- [ ] Expansion drip fires on usage nearing plan limits, not arbitrary calendar dates
- [ ] A/B test plan exists for at least one sequence element (subject line, timing, or content format)

## Common Pitfalls

1. **One drip fits all.** Sending the same sequence to every new customer ignores persona, plan tier, and use case. Fix: segment drips by at least ICP tier and plan level — enterprise onboarding differs from self-serve.
2. **Renewal drip starts too late.** Beginning renewal outreach at 30 days misses the relationship-building window. Fix: start at 90 days with value reinforcement, not pricing — 90/60/30/14/7 cadence.
3. **No behavioral branching.** Sending email #3 to someone who never opened email #1 wastes sends and damages sender reputation. Fix: use behavioral triggers — if no opens in 14 days, shift to re-engagement track; if they click pricing, route to Evaluator track.
4. **Stage conversion not measured.** Running drips without tracking how many contacts move from stage N to N+1 means you're flying blind. Fix: instrument every drip with stage conversion rate and time-in-stage metrics.
5. **Over-emailing customers.** Welcome drip + expansion drip + NPS follow-up + product update — all hitting the same person in one week. Fix: build a contact frequency cap into your automation; no more than 2 marketing emails per week to any active customer.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator
  **Canonical lifecycle (repo root):** `references/gtm-lifecycle-stages.md` · `references/activation-playbook.md` (post-activation triggers) · `references/lifecycle-skill-index.md`

## Related Skills

- mql-nurture, onboarding-sequences, re-engagement, churn-prevention, cs-playbooks

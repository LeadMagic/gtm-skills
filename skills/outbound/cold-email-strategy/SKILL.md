---
name: cold-email-strategy
description: >-
  Design or audit a cold-email sequence architecture: audience and trigger,
  offer, touch cadence, branch logic, channel roles, sending constraints,
  measurement, and governance. Use when planning outbound strategy, a multi-touch cadence,
  a sequence blueprint, or diagnosis of low reply and meeting rates. Use a
  copywriting skill for final messages and deliverability skills for infrastructure.
license: MIT
compatibility: Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, OpenCode, Goose, Hermes, Jesse, Windsurf, Zed
metadata:
  version: "1.4.0"
  author: LeadMagic
  category: outbound
  tags: [cold-email, sequence-design, cadence, outbound, prospecting]
  related_skills:
    - cold-email-copywriting
    - email-deliverability
    - domain-infrastructure
    - sending-platforms
    - multi-channel-outreach
    - website-visitor-identification
    - icp-scoring
    - lead-enrichment
  frameworks:
    - Command of the Message
    - SPICED
    - SPIN
    - "Lars Nilsson — Account-Based Sales Development"
    - "Becc Holland — Stellar Cold Email and Diagnostic Selling"
    - "Leslie Venetz — Earn the Right and Profit-Generating Pipeline"
    - "Guillaume Moubeche — problem-first multichannel outbound"
    - "Jordan Crawford — PQS, PVP, and FIND"
    - "Justin Michael — Sales Borg and Technology Quotient"
    - "Pat Spielmann — Cold to Gold, Full-Circle Multichannel, and ACE"
    - "Eric Nowoslawski — infrastructure, creative campaigns, and unit economics"
---

# Cold Email Strategy

## Overview

A sequence is an operating system, not a pile of emails. This skill produces the audience, signal, offer, cadence, branch logic, channel roles, measurement plan, and safety constraints that downstream copy and sending systems implement. It does not invent customer proof, ignore consent requirements, or treat open rate as the primary success metric.

## When to Use

- Build a cold-outreach sequence or multi-touch cadence.
- Diagnose low positive replies, meetings, or opportunity creation.
- Decide how triggers, segments, personas, and channels alter a sequence.
- Define handoffs between research, enrichment, copy, calling, and sequencing tools.
- Audit campaign governance before increasing volume.

Use `cold-email-copywriting` for final email text, `domain-infrastructure` and `email-deliverability` for sending readiness, and `sending-platforms` for tool implementation.

## Prerequisites

Collect or explicitly mark as unknown:

- ICP segment and excluded audiences.
- Buyer role, problem, current alternative, and desired outcome.
- Offer, evidence, proof constraints, and approved claims.
- Trigger or reason for contact, with source and freshness.
- Target market, applicable policies, and suppression requirements.
- Mailbox, domain, reputation, and daily-capacity status.
- Baseline delivered, reply, positive-reply, meeting, and opportunity rates.

If these inputs are unreliable, run `gtm-context-bootstrap`, `icp-scoring`, and `lead-enrichment` first.

## Authoritative Foundations

- **Problem and relevance before product.** Earn attention with a credible problem hypothesis tied to the recipient's context.
- **Signal over decoration.** Personalization must change the reason, claim, or action—not merely add a first-line fact.
- **One job per touch.** Each touch advances a distinct question, proof point, risk reversal, or channel action.
- **Deliverability is a constraint.** Sequence volume never overrides domain health, suppression, or platform limits.
- **Measure business outcomes.** Prioritize delivered rate, positive replies, qualified meetings, opportunities, and pipeline; treat opens as noisy diagnostics.
- **Human review at risk boundaries.** Review sensitive claims, named-account personalization, regulated audiences, and automated replies before launch.

## Workflow

### 1. Define the campaign cell

Use one coherent combination of ICP segment, persona, problem, offer, trigger, market, and proof profile. Split cells when a meaningful variable changes; do not hide multiple audiences inside one sequence.

### 2. State the contact thesis

Write a one-sentence reason this buyer may care now. Record evidence, confidence, freshness, and what would falsify the thesis. Remove contacts whose signal or fit cannot support a defensible message.

### 3. Map the sequence arc

Assign each touch a purpose before writing copy:

| Touch purpose | Decision it should enable |
|---|---|
| Problem hypothesis | Is the issue relevant? |
| Evidence or implication | Is the cost or urgency credible? |
| Alternative angle | Is there another useful entrypoint? |
| Proof or risk reduction | Is exploration safe and worthwhile? |
| Close-the-loop | Should outreach pause or continue? |

Choose timing and touch count from buyer context, signal half-life, channel norms, and deliverability capacity. Treat any numeric benchmark in the complete playbook as a testable starting hypothesis, not a universal promise.

### 4. Define channels and branches

Specify which channel owns each touch and what changes after a positive reply, objection, referral, unsubscribe, bounce, out-of-office response, website signal, job change, or stale trigger. Never auto-enroll suppressed or legally excluded contacts.

### 5. Set capacity and governance

Document mailbox eligibility, ramp status, per-mailbox limits, domain-health stop conditions, duplicate prevention, ownership, approval, pause rules, and re-enrollment policy. Escalate to the deliverability skills before scaling uncertain infrastructure.

### 6. Design the test

Test one meaningful variable per cell when possible. Define the hypothesis, minimum observation window, decision metric, guardrail metrics, and stop rule. Segment reporting by audience and trigger so aggregate results do not mask failure.

### 7. Hand off implementation

Send the architecture to `cold-email-copywriting`, then the chosen sequencing tool skill. Require a preflight sample, suppression check, link and merge-field QA, and a small monitored launch before scaling.

## Output Format

Produce a cold-email strategy document with:

1. Campaign objective, owner, scope, and decision metric.
2. Campaign-cell table: segment, persona, problem, offer, trigger, proof, exclusions.
3. Contact thesis with evidence, confidence, and freshness.
4. Touch map: day/window, channel, purpose, input, CTA, and branch.
5. Reply and exception routing table.
6. Sending-capacity and deliverability constraints.
7. Suppression, consent, privacy, approval, and pause rules.
8. Experiment plan with hypothesis, variable, cohort, metric, guardrails, and decision rule.
9. Measurement funnel from attempted through pipeline outcome.
10. Implementation handoff and unresolved questions.

Start from `templates/output-template.md`. Open `references/complete-playbook.md` only for the detailed expert maps and examples relevant to the current campaign.

## Quality Check

- Does one campaign cell represent one coherent audience and reason to contact?
- Is every claim traceable to approved evidence or labeled as a hypothesis?
- Does each touch have a distinct purpose and explicit branch behavior?
- Are bounce, unsubscribe, objection, referral, and positive reply paths defined?
- Are infrastructure and suppression constraints documented before volume?
- Does the test isolate a useful variable and measure positive outcomes?
- Are benchmarks framed as context-dependent baselines rather than guarantees?
- Is the handoff specific enough for copywriting and platform implementation?

## Common Pitfalls

1. **Writing copy before architecture** — Decide audience, trigger, offer, arc, and branches first.
2. **Personalization theater** — Use evidence that changes relevance, not decorative facts.
3. **Universal cadence numbers** — Set timing from market, signal, capacity, and observed results.
4. **Scaling on opens** — Judge positive replies, qualified meetings, opportunities, and guardrails.
5. **No exception routing** — Treat replies, referrals, bounces, and suppression as designed states.
6. **Mixing cells** — Separate materially different personas, problems, triggers, or offers.
7. **Ignoring infrastructure** — Stop and fix domain or mailbox risk before raising volume.

## Execution Artifacts

- `references/complete-playbook.md` — Detailed sequence patterns, expert maps, examples, and benchmarks
- `references/framework-notes.md` — Framework index and authority routing
- `references/deliverability-primer.md` — Deliverability fundamentals
- `references/email-frameworks.md` — Cold-email copy frameworks and rules
- `references/becc-holland-playbook.md` — Diagnostic selling and relevance guidance
- `references/lemlist-guillaume-outbound.md` — Problem-first multichannel guidance
- `references/jordan-crawford-blueprint-gtm.md` — PQS, PVP, and FIND
- `references/justin-michael-sales-borg.md` — Human and automation division of labor
- `references/eric-nowoslawski-outbound.md` — Infrastructure and unit-economics guidance
- `references/leslie-venetz-buyer-first-outbound.md` — Buyer-first segmentation and channel audit
- `references/expert-frameworks.md` — Additional authority notes
- `templates/output-template.md` — Deliverable shell
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- `cold-email-copywriting` — Write the approved sequence messages
- `email-deliverability` — Define reputation and sending guardrails
- `domain-infrastructure` — Prepare domains and mailboxes
- `sending-platforms` — Implement the sequence in a platform
- `multi-channel-outreach` — Coordinate email with calls and social touches
- `campaign-analytics` — Measure funnel and experiment performance

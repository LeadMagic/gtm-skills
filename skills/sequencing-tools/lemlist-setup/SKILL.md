---
name: lemlist-setup
description: >-
  Set up and optimize Lemlist — personalized images/videos, multi-channel sequences, 
  warm-up, deliverability. Triggers on: "Lemlist", "Lemlist setup", "Lemlist campaigns",
  "personalized cold email".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: sequencing-tools
  tags: [lemlist, cold-email, personalization, lemwarm, multi-channel]
  frameworks:
    - "Lemlist Personalization Framework"
    - "Guillaume Moubeche — lemlist Outbound"
    - "ColdIQ Multi-Channel"
    - "Outreach — Sales Engagement Cadence Design"
---

# Lemlist Setup

## Overview
Lemlist differentiates on personalization — custom images, videos, and landing
page personalization that other platforms don't offer natively. Combined with
lemwarm (automated warmup) and multi-channel capabilities, it's ideal for teams
that want higher per-email engagement at lower volume.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Lemlist Personalization Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Guillaume Moubeche — lemlist Outbound.** Problem-first email structure, 4–9 touch multichannel sequences, CTC, lemwarm deliverability, trigger→problem mapping. Canonical playbook → `../outbound/cold-email-strategy/references/lemlist-guillaume-outbound.md`.
- **ColdIQ Multi-Channel.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Outreach — Sales Engagement Cadence Design.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Set up Lemlist"
- "Lemlist campaign setup"
- "Personalized cold email at scale"
- "Lemlist warmup strategy"

## Step-by-Step Process

### Phase 1: Lemwarm Setup
Before sending any campaign:
- Add all sending mailboxes to lemwarm
- Start with 2-5 warmup emails/day, auto-escalate over 3-4 weeks
- Monitor reputation score: target >95 before launching real campaigns
- Lemwarm sends auto-replies from warmup pool to build positive reputation

### Phase 2: Campaign Architecture
- **Sequence:** 3-7 steps, email + LinkedIn + custom tasks
- **Personalization:** Custom images (prospect name/logo on image), custom videos
  (screencast with prospect website), custom landing pages (dynamic text/image)
- **Conditions:** If opened → different next step. If clicked → different follow-up.
  If no engagement → different angle.
- **Sending:** Max 100 emails/day/domain across all campaigns

### Phase 3: Creative Personalization
- **Custom images:** Prospect name on a whiteboard, their logo in your UI, "Hi {first_name}" graphic
- **Custom videos:** Loom-style screencast showing their website + your product integration
- **Custom landing pages:** Dynamic hero image with their company logo, dynamic headline
  with their name, dynamic case study from their industry

### Phase 4: Multi-Channel
Layer LinkedIn into sequences:
- Email Touch 1 → LinkedIn profile view 2 days later
- Email Touch 2 → LinkedIn connection request 2 days later
- Email Touch 3 → LinkedIn DM 2 days later
- All tracked in Lemlist timeline

### Phase 5: Analytics
- Campaign health: reply rate, interest rate, meeting rate
- Creative performance: which images/videos drive highest engagement
- A/B test: personalization vs plain text, creative vs standard
- Warmup health: per-mailbox reputation score, spam placement rate

## Output Format
Lemlist playbook with: warmup schedule, campaign configuration, creative personalization
templates, multi-channel integration plan, and optimization framework.



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

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — Guillaume multichannel, Pat Full-Circle, lemwarm gates
- `references/clay-enrollment-handoff.md` — Clay → Lemlist variables + problem_hook mapping
- `../../outbound/cold-email-strategy/references/lemlist-guillaume-outbound.md` — Guillaume Moubeche canonical playbook
- `../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md` — verify + multichannel (Pat Spielmann)
- `../../tools/clay-loops-toolkit/references/routing-matrix.md` — signal → campaign map
- `../../../../references/gtm-experts-outbound-index.md` — expert router
- `templates/output-template.md` — lemwarm + multichannel + Clay gate deliverable
- `scripts/check-output.py` — local checklist validator

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

- Lemlist Personalization Framework: apply only the part that directly improves the requested deliverable.
- ColdIQ Multi-Channel: apply only the part that directly improves the requested deliverable.
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
- cold-email-strategy, cold-email-copywriting, email-deliverability, inbox-setup, social-selling

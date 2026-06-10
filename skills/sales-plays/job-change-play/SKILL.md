---
name: job-change-play
description: >-
  Outbound play triggered by contact job changes — champion tracking, new-role 
  outreach, "new broom" timing. Triggers on: "job change", "new role", "champion 
  moved", "job change outreach", "contact changed jobs".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: sales-plays
  tags: [sales-plays, job-change, champion-tracking, trigger-based, new-role]
  frameworks:
    - "Signal-Based Selling"
    - "Champion Tracking Methodology"
    - "Winning by Design — SPICED"
---

# Job Change Outbound Play

## Overview
When a contact changes jobs, three opportunities open simultaneously: (1) the old
company lost a champion and may need replacement support, (2) the contact is now
at a new company with new budget and tool evaluation, and (3) you have a timely,
personal reason to reconnect. This play covers all three.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Signal-Based Selling.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Champion Tracking Methodology.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Winning by Design — SPICED.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Champion left the company"
- "Contact changed jobs"
- "Job change detection outreach"
- "New role outbound"

## Core Principle
> A job change is the highest-permission outreach event in B2B. It's personal,
> timely, and relevant. Nobody ignores a "congrats on the new role" email.
> And at their new company, they have influence over tool selection in their
> first 90 days.

## Step-by-Step Process

### Phase 1: Job Change Detection
Monitor via:
- LinkedIn notifications (connections)
- CRM enrichment triggers (Apollo, LeadMagic job change detection)
- Sales Navigator alerts on saved leads
- Newsletter/announcement monitoring
- User/contact list re-verification (monthly)

### Phase 2: Old Company — Champion Replacement
When a champion leaves:
- Immediately identify who inherited their responsibilities
- Reach out to the new contact within 5 days
- Acknowledge the transition, provide value (usage summary, ROI to date)
- Frame yourself as a resource during the transition
- Don't pitch — help them look good by knowing the account history

### Phase 3: New Company — New Role Outreach
When a contact starts a new role, reach out Day 14-21 (after onboarding chaos):

Subject: "New role at [NewCo] — congrats"
Body: Reference their move, connect to what they accomplished at the old company
with your product, suggest how it applies here. "At [OldCo] you [achieved X
with our product]. Curious if [NewCo] is dealing with similar challenges."

### Phase 4: Sequence Architecture
7-day, 3-touch sequence for new role:
- **Day 1:** Email (congrats, bridge from old to new)
- **Day 3:** LinkedIn message (more casual, "how's the first few weeks?")
- **Day 7:** Email (value-add: "I compiled some data on [their new industry]")
- **Day 14+:** Move to standard nurture if no reply

### Phase 5: CRM Hygiene
- Update contact records: new title, new company, new email
- Create new opportunity at new company (linked to past success)
- Flag old company account for champion replacement outreach
- Tag as "job change — warm re-engagement" for future campaigns

## Output Format
Job change playbook with: detection setup, champion replacement templates, new
role outreach sequence, CRM update workflow, and tracking dashboard.



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

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

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

- Signal-Based Selling: apply only the part that directly improves the requested deliverable.
- Champion Tracking Methodology: apply only the part that directly improves the requested deliverable.
- Winning by Design — SPICED: apply only the part that directly improves the requested deliverable.

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
- cold-email-strategy, reply-handling, pipeline-management, leadmagic-job-change, crm-integration

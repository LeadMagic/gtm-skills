---
name: qbr-planning
description: >-
  Plan and execute Quarterly Business Reviews — value documentation, ROI
  presentation, executive alignment, and expansion roadmap. Use when preparing
  for QBRs, business reviews with customers, or executive stakeholder meetings.
  Triggers on: "QBR", "quarterly business review", "executive business review",
  "customer review", "value review", or any request about strategic customer
  meetings.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: customer-success
  tags: [qbr, customer-success, executive-review, value]
  frameworks:
    - "Gainsight QBR Methodology"
    - "Winning by Design Bowtie Metrics"
    - "Gainsight — Customer Success Maturity Model"
---

# QBR Planning

## Overview
A QBR is not a status update — it is a strategic alignment meeting that
demonstrates value delivered, aligns on future priorities, and sets the
stage for expansion. This skill builds QBR templates that executives want
to attend because they see clear ROI from the relationship.

## When to Use
- "Plan a QBR"
- "Prepare for an executive business review"
- "Build a QBR deck"
- "Document value for a customer"
- "Structure a quarterly review"

## Authoritative Foundations
Gainsight QBR methodology: QBRs should cover value realized, value roadmap,
and strategic alignment — not product updates. Winning by Design Bowtie
metrics: frame expansion within the customer's lifecycle, not your quota.

## Step-by-Step Process
### Phase 1: Pre-QBR Preparation
Gather: usage metrics, support history, NPS/CSAT trends, expansion signals,
stakeholder map, competitor activity. Document value delivered in their
language — not your feature names.

### Phase 2: QBR Structure
1. Executive Summary — value delivered this quarter, in their words
2. Metrics Review — adoption, usage, outcomes achieved vs. goals
3. Success Stories — wins since last QBR
4. Strategic Alignment — how this maps to their company priorities
5. Roadmap Preview — what's coming, how it benefits them
6. Expansion Opportunity — logical next steps, not a sales pitch
7. Action Items — mutual commitments for next quarter

### Phase 3: Delivery
60 minutes: 40 min presentation, 20 min discussion. Send deck 24 hours
in advance. Include their logo, their metrics, their language. This is
about them — not you.

## Output Format
QBR deck template, value documentation template, stakeholder map, and
pre-QBR checklist.


## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls
1. **Product update disguised as QBR** — executives don't care about
   feature releases. They care about business outcomes.
2. **Surprise expansion ask** — if expansion is first mentioned at the
   QBR, it's too late. Plant the seed months before.
3. **Your metrics, not theirs** — "you logged in 50 times" means nothing.
   "Your team reduced time-to-close by 40%" means everything.
4. **No action items** — a QBR without mutual commitments is a meeting,
   not a milestone.

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

- Gainsight QBR Methodology: apply only the part that directly improves the requested deliverable.
- Winning by Design Bowtie Metrics: apply only the part that directly improves the requested deliverable.
- Gainsight — Customer Success Maturity Model: apply only the part that directly improves the requested deliverable.

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
- **cs-playbooks**: Full CS operating system
- **customer-marketing**: Case studies and advocacy from QBRs
- **expansion-selling**: Turn QBR insights into expansion

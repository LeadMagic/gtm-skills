---
name: account-selection
description: >-
  Select and prioritize target accounts for ABM programs — scoring models, tier
  assignment, TAM segmentation. Triggers on: "account selection", "target account list",
  "tier accounts", "prioritize accounts", "TAM segmentation".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: abm
  tags: [abm, account-selection, scoring, tiering, target-accounts]
  frameworks:
    - "TOPO Account Selection"
    - "WbD ICP Framework"
    - "ITSMA — Account-Based Marketing"
---

# Account Selection & Tiering

## Overview
Account selection is the hardest part of ABM. Pick wrong and you waste 6 months.
Pick right and you 3x your close rate. This skill builds a weighted scoring model
to tier your TAM into Strategic, Scale, and Programmatic accounts.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **TOPO Account Selection.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **WbD ICP Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **ITSMA — Account-Based Marketing.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Which accounts should we target?"
- "Tier our target account list"
- "Build an account scoring model"
- "Prioritize our TAM for ABM"

## Step-by-Step Process

### Phase 1: Build Scoring Model
Weight each dimension (must total 100 points):

**Firmographic Fit (35 pts):**
- Industry match (0-10): Direct ICP industry = 10, adjacent = 5, outside = 2
- Employee count (0-10): In sweet spot = 10, near = 5, outside = 2
- Revenue range (0-10): In sweet spot = 10, near = 5, outside = 2
- Geography (0-5): Target region = 5, acceptable = 3, outside = 1

**Technographic Fit (25 pts):**
- Current tech stack (0-15): Complementary tools present = 15, some = 8, none = 2
- Integration potential (0-10): High integration value = 10, medium = 5, low = 2

**Behavioral Signals (25 pts):**
- Website visits (0-10): Frequent, multi-page = 10, some = 5, none = 2
- Content engagement (0-10): Downloads, webinar attendance, newsletter = score by recency
- Social engagement (0-5): LinkedIn follows, comments, shares

**Intent & Trigger (15 pts):**
- Hiring signals (0-5): Role related to your product = 5
- Funding event (0-5): Recent raise = 5
- Tech change (0-5): Evidence of switching or evaluating

### Phase 2: Tier Assignment
- **Tier 1 (>80):** 5-15 accounts. Immediate sales + marketing investment.
- **Tier 2 (60-79):** 15-50 accounts. Scaled ABM plays.
- **Tier 3 (40-59):** 50-200 accounts. Programmatic nurture.
- **Below 40:** Not ABM. Generic inbound/outbound only.

### Phase 3: Ongoing Refinement
- Monthly: Re-score based on new signals
- Quarterly: Review tier assignments, promote/demote accounts
- After wins: Analyze what made winners score high — adjust weights
- After losses: Add disqualifying signals discovered in lost deals

## Output Format
Scored account list with tier assignments, scoring model documentation, and a
refinement calendar.



## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls

1. **Treating ABM as a marketing-only initiative.** ABM requires tight sales alignment. Without BDRs assigned to specific accounts and shared account briefs, marketing produces content nobody uses. Fix: weekly ABM standups with marketing + BDRs + AEs.
2. **One-size-fits-all tiering.** Applying the same playbook to Tier 1 and Tier 3 accounts. Fix: Tier 1 gets custom content and executive engagement; Tier 3 gets automated personalization.
3. **Measuring ABM on MQLs.** ABM success is pipeline from target accounts, not lead volume. Fix: track coverage %, engagement depth, pipeline created, and win rate by tier.

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

- TOPO Account Selection: apply only the part that directly improves the requested deliverable.
- WbD ICP Framework: apply only the part that directly improves the requested deliverable.
- ITSMA — Account-Based Marketing: apply only the part that directly improves the requested deliverable.

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
- icp-scoring, abm-strategy, signal-scoring, lead-finding, list-building

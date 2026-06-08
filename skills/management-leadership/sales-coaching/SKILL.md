---
name: sales-coaching
description: >-
  Coach sales reps for consistent performance — REKS framework, deal reviews,
  call coaching, pipeline inspection, and 1:1 cadences. Use when setting up
  sales coaching, training managers, or improving rep performance. Triggers on:
  "sales coaching", "coach reps", "REKS", "deal review", "call coaching",
  "manager coaching", "1:1", or any request about developing sellers.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: management-leadership
  tags: [coaching, sales-management, reks, leadership]
  frameworks:
    - "Winning by Design REKS"
    - "Force Management MEDDICC Deal Review"
    - "Keith Rosen — Sales Coaching"
---

# Sales Coaching

## Overview
Coaching is the highest-leverage activity a sales manager can perform. A
manager who coaches 2 hours/week lifts team performance more than one who
spends 10 hours on reporting. This skill builds a coaching system: the REKS
framework for diagnosing performance gaps, structured deal reviews, call
coaching cadences, and 1:1 formats that drive behavior change.

## When to Use
- "Set up sales coaching"
- "How do I coach my reps better?"
- "Build a deal review process"
- "Design 1:1 templates for sales managers"

## Authoritative Foundations
- **Winning by Design REKS** — Results → Efforts → Knowledge → Skills.
  Diagnose before coaching. A rep missing quota could have an effort problem
  (not enough activity), a knowledge problem (doesn't understand the product),
  or a skill problem (can't execute in conversation). Each requires different
  coaching.
- **Force Management MEDDICC** — Deal review structure. Inspect deals against
  MEDDICC criteria, not rep confidence levels.

## Step-by-Step Process
### Phase 1: REKS Diagnosis
For each rep, diagnose the performance gap before coaching. Study top
performers to identify what excellence looks like.

### Phase 2: Coaching Cadence
- Daily: 5-min huddle, key deals at risk
- Weekly: 30-min 1:1, one metric focus, deal deep-dive
- Monthly: 60-min career development, skill-building
- Quarterly: performance review, goal setting

### Phase 3: Deal Review Structure
Every deal review: MEDDICC scoring → gap identification → action plan.
Never "how do you feel about this deal?" — always "what evidence do you
have for each MEDDICC dimension?"

### Phase 4: Call Coaching
Review 2-3 calls/week per rep. Score against framework (SPIN discovery
quality, CoM value articulation, objection handling). Provide one thing
to improve next call, one thing to keep doing.

## Output Format
Coaching system with cadence calendar, REKS diagnostic template, deal
review scorecard, call coaching rubric, and 1:1 agenda template.


## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls
1. **Coaching without diagnosis** — telling a rep to "do more prospecting"
   when they actually don't know how to qualify is wasted coaching.
2. **Coaching results, not behaviors** — "hit your number" isn't coaching.
   "Here's the specific skill to build" is.
3. **No deal inspection framework** — "how's the deal going?" produces
   fiction. "Walk me through the Decision Process" produces truth.
4. **1:1 as status update** — status belongs in CRM. 1:1s are for
   development, not reporting.

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

- Winning by Design REKS: apply only the part that directly improves the requested deliverable.
- Force Management MEDDICC Deal Review: apply only the part that directly improves the requested deliverable.
- Keith Rosen — Sales Coaching: apply only the part that directly improves the requested deliverable.

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
- **pipeline-management**: Deal inspection processes
- **meeting-prep**: Call preparation the rep should master
- **objection-handling**: Objection frameworks to coach toward

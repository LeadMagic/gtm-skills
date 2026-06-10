---
name: growth-experimentation
description: >-
  Build a growth experimentation system — ICE scoring, growth sprints, experiment
  design, statistical significance, and learning repositories. Use when building
  an experimentation program, running growth sprints, prioritizing tests, or
  establishing a data-driven growth culture. Triggers on: "experimentation",
  "growth experiments", "A/B testing program", "ICE scoring", "growth sprint",
  "experiment design", "test velocity", or any growth experimentation request.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: analytics
  tags: [experimentation, growth, testing, ice, sprints]
  frameworks: [Sean Ellis Hacking Growth, Brian Balfour Reforge, Andrew Chen Growth, ICE Scoring]
---

# Growth Experimentation

## Overview
The companies with the highest growth rates don't have better ideas — they
have better systems for testing ideas. A high-velocity experimentation system
runs 15-30 experiments per month across acquisition, activation, retention,
and monetization. Most experiments fail. That's by design. The team that
learns fastest from each failure wins.

## When to Use
- "Build an experimentation program"
- "Set up growth sprints"
- "Prioritize experiments with ICE"
- "Increase our test velocity"
- "Create a learning repository"

## Authoritative Foundations
- **Sean Ellis & Morgan Brown (Hacking Growth)** — coined "growth hacking."
  North Star Metric. Growth experimentation loop: analyze → ideate →
  prioritize → test → learn.
- **Brian Balfour (Reforge, ex-HubSpot VP Growth)** — increasing HubSpot's
  experiment velocity from 5 to 20/week produced 3x growth rate improvement.
  Four Fits Framework: Market-Product, Product-Channel, Channel-Model,
  Model-Market.
- **Andrew Chen (a16z, ex-Uber Growth)** — The Cold Start Problem. Growth
  teams at scale.
- **Fareed Mosavat (Reforge, ex-Slack Growth)** — experimentation systems.

## Step-by-Step Process
### Phase 1: Set the North Star Metric
One metric that captures core value delivery. If this moves up, the business
is healthier. All experiments ladder to this metric.

### Phase 2: ICE Scoring
Score every experiment idea 1-10 on Impact, Confidence, Ease. Average the
three. Prioritize by ICE score. Re-score weekly as new data arrives.

### Phase 3: Growth Sprint Cadence
Weekly cycle: idea generation (Monday), prioritization (Tuesday), build
(Wed-Thu), launch (Fri), analyze (Mon). 2-week sprints for complex tests.
AI compresses cycle: a single growth marketer with AI can test 10 variants
in time it used to take to build one.

### Phase 4: Experiment Design
Every experiment: hypothesis, success metric, minimum detectable effect,
required sample size, maximum duration. Document everything — winners
and losers. Build a searchable learning repository.

### Phase 5: 4 Layers of Experiments
1. Channel/tactic assessment — test how channels impact conversions
2. Offer optimization — pricing, packaging, trial length
3. Message personalization — copy and creative by segment
4. AI-powered — autonomous experiment generation, prediction, optimization

## Output Format
Experimentation system with North Star Metric definition, ICE backlog,
sprint calendar, experiment design template, and learning repository structure.


## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls
1. **Tests too large** — redesigning entire onboarding (4 weeks to build)
   loses to testing a single screen change (2 days). Small tests = fast
   learning.
2. **No learning repository** — running 50 experiments without documenting
   learnings is running the same test twice. Document everything.
3. **Statistical ignorance** — calling a test at 70% confidence produces
   false positives. Wait for 95%+ confidence.
4. **Winner's bias** — only shipping winners without understanding losers
   means you don't know why things work.

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

- Sean Ellis Hacking Growth: apply only the part that directly improves the requested deliverable.
- Brian Balfour Reforge: apply only the part that directly improves the requested deliverable.
- Andrew Chen Growth: apply only the part that directly improves the requested deliverable.
- ICE Scoring: apply only the part that directly improves the requested deliverable.

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
- **a-b-testing**: Statistical framework for individual tests
- **gtm-metrics**: Growth metrics and dashboard design

---
name: gtm-system-architecture
description: >-
  Design a complete GTM operating system — revenue model, data model, operating
  model, growth model, and GTM model per WbD's 6-model framework. Use when designing
  a GTM system from scratch, auditing an existing one, or aligning teams around
  a unified revenue architecture. Triggers on: "GTM system", "revenue architecture",
  "operating model", "GTM model", "revenue system", "go-to-market design", "GTM
  audit", or any request about designing how GTM works end-to-end.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: analytics
  tags: [gtm, system-design, revenue-architecture, operating-model]
  related_skills: [gtm-metrics, pipeline-management, marketing-strategy, sales-team-building]
  frameworks: [Winning by Design GTM Index, Bowtie Model, SiriusDecisions Demand Waterfall]
---

# GTM System Architecture

## Overview

A GTM system is the operating system underneath your revenue. It's the answer
to "how does money flow through this company?" — not "what tactics are we
running this quarter?"

Winning by Design's GTM Index framework scores 1-10 across six interconnected
models. Most companies break because they optimize one model while neglecting
the others. This skill designs all six as one unified system.

## When to Use

- "Design our GTM system"
- "Audit our revenue architecture"
- "Build a GTM operating model"
- "Our GTM is fragmented — fix it"
- "Align sales, marketing, and CS"
- "Design how revenue flows"

## Authoritative Foundations

- **Winning by Design GTM Index** — six models (Revenue, Data, Math, Operating,
  Growth, GTM). 1-10 scoring per model. Average across 1000+ companies benchmarked.
- **Winning by Design Bowtie** — revenue is a continuous loop: acquire → retain
  → expand. Not a funnel that ends at "closed won."
- **SiriusDecisions Demand Waterfall** — demand flows through stages with
  defined handoffs and conversion metrics.

## Step-by-Step Process

### Phase 1: The Six Models (WbD GTM Index)

Score each 1-10, then identify the weakest link:

**1. Revenue Model — "Do we know how we make money?"**
- Pricing clarity, packaging, discount authority, expansion model.
- Weak: "We charge whatever the customer agrees to."
- Strong: "Standard tiers, defined discount rules, clear expansion path."

**2. Data Model — "Can we answer basic questions about our business?"**
- CRM hygiene, pipeline data, conversion rates, attribution.
- Weak: "We don't know our MQL→SQL conversion rate."
- Strong: "Every deal has stage, source, close date, and MEDDIC dimensions."

**3. Math Model — "Do unit economics work?"**
- LTV:CAC, payback period, CAC by channel, churn rates, NRR.
- Weak: "We don't track CAC by channel. We think churn is around 3%."
- Strong: "CAC payback is 8 months, LTV:CAC is 4:1, NRR is 115%."

**4. Operating Model — "Is there a documented process someone could follow?"**
- Sales process stages, playbooks, enablement, handoff documentation.
- Weak: "Reps sell however they want. No two deals look the same."
- Strong: "Stage definitions with Goals and Exit Criteria. Playbook
  documented. New reps ramp in 90 days."

**5. Growth Model — "Do we know which channels work and at what cost?"**
- Channel mix, CAC by channel, channel ROI, experimentation velocity.
- Weak: "We try things and see what sticks."
- Strong: "Paid search CAC is $X, content CAC is $Y, outbound CAC is $Z.
  We allocate budget to highest-ROI channels."

**6. GTM Model — "Is the whole system connected?"**
- Sales-marketing-CS alignment, shared metrics, unified customer journey.
- Weak: "Marketing generates MQLs sales ignores. CS doesn't know what was
  sold."
- Strong: "Unified Bowtie. Shared metrics across functions. Single customer
  view from first touch through renewal."

### Phase 2: Bowtie Architecture

Revenue doesn't end at "closed won." It continues through retention and
expansion. Design the Bowtie:

```
Awareness → Education → Selection → Onboarding → Adoption → Expansion → Renewal
[Marketing]   [Marketing]  [Sales]   [CS]       [CS]      [CS/Sales]   [CS]
```

Each stage has: owner (which team), goal (what success looks like), handoff
criteria (when to pass to next stage), and metrics (how to measure).

### Phase 3: System Integration

The six models don't operate independently:

- **Revenue Model ↔ Math Model:** Pricing choices determine unit economics.
  Lower price → lower ARPU → longer CAC payback. Know the tradeoff.
- **Data Model ↔ Operating Model:** If CRM data is unreliable, the process
  can't be inspected. Fix data before adding process.
- **Growth Model ↔ GTM Model:** Marketing channels produce demand. Sales
  converts it. CS retains it. If any link breaks, the system fails.
- **Weakest link principle:** The lowest-scoring model caps the entire system.
  A 9/10 Revenue Model with a 3/10 Data Model is a 3/10 system.

### Phase 4: Implementation Roadmap

Don't fix all six at once. Sequence by impact:

1. **Fix the Math Model first.** If unit economics don't work, nothing else
   matters. Know your CAC, LTV, churn, payback.
2. **Fix the Data Model.** Clean CRM, define stages, establish reporting.
3. **Design the Operating Model.** Document processes, build playbooks.
4. **Optimize the Growth Model.** Test channels, measure CAC per channel.
5. **Refine the Revenue Model.** Pricing, packaging, discount rules.
6. **Align the GTM Model.** Cross-functional alignment, shared metrics.

## Output Format

GTM system design: six-model assessment (current scores + target scores),
Bowtie architecture with ownership per stage, weakest-link analysis,
implementation roadmap with 90-day priorities, and measurement dashboard.

## Quality Check

- [ ] All six models scored 1-10 with evidence
- [ ] Weakest link identified (lowest scoring model)
- [ ] Bowtie architecture with owner, goal, handoff criteria per stage
- [ ] Implementation roadmap (not trying to fix everything at once)
- [ ] Shared metrics across functions (not siloed KPIs)
- [ ] Re-assessment cadence (quarterly GTM Index check)

## Common Pitfalls

1. **Optimizing one model in isolation.** Improving the Operating Model without
   fixing the Data Model means adding process to bad data. Fix data first.

2. **No Bowtie.** Treating revenue as a pipeline that ends at "closed won"
   ignores the 70%+ of lifetime value that comes after the sale.

3. **Self-assessment without evidence.** "I think our Math Model is a 7"
   without actually calculating LTV:CAC. Score with data, not feelings.

4. **Trying to fix everything at once.** Six-model overhauls take 12-18 months.
   Sequence one or two per quarter.

5. **GTM model owned by one function.** GTM alignment requires sales,
   marketing, and CS leadership in the same room with shared metrics.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- **gtm-metrics**: Model measurement and dashboards
- **pipeline-management**: Operating model execution
- **marketing-strategy**: Growth model design
- **sales-team-building**: Operating model staffing

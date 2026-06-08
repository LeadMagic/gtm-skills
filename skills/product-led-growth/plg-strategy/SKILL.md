---
name: plg-strategy
description: >-
  Design product-led growth motions — freemium vs free trial, PQL scoring,
  self-serve conversion, PLG sales hybrid, and product-led marketing. Use when
  building a PLG motion, transitioning to self-serve, or optimizing product-led
  acquisition. Triggers on: "product-led growth", "PLG", "freemium", "free trial",
  "self-serve", "PQL", "product qualified lead", "product-led sales", or any
  request about product-driven growth.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: product-led-growth
  tags: [plg, freemium, self-serve, growth, product]
  frameworks: [OpenView PLG Framework, Wes Bush Product-Led Growth, Kyle Poyar Growth Unhinged, Blake Bartlett PLG Traits]
---

# Product-Led Growth Strategy

## Overview
PLG means the product is the primary driver of acquisition, retention, and
expansion — not sales outreach. The term was coined by OpenView's Blake
Bartlett in 2016. By 2026, 97% of B2B buyers prefer to try before they buy.
PLG is no longer a competitive advantage — it's table stakes.

## When to Use
- "Build a PLG motion"
- "Should we go freemium or free trial?"
- "Set up PQL scoring"
- "Transition from sales-led to product-led"
- "Design a self-serve conversion flow"

## Authoritative Foundations
- **OpenView (Blake Bartlett, Kyle Poyar, Mackey Craven)** — coined PLG. 3
  pillars: design for end user, deliver value before capturing value, invest
  in product with GTM intent. PLG companies 2x more likely to grow 100% YoY.
- **Wes Bush (ProductLed)** — 5 levels of PLG maturity. 434+ companies, $1B+
  self-serve revenue. Freemium conversion: 5%. Free trial conversion: 17%.
- **Kyle Poyar (Growth Unhinged)** — PLG benchmarks, pricing, product-led
  marketing. Activation rate benchmarks: 20-40% normal.

## Step-by-Step Process
### Phase 1: Model Selection
- **Freemium**: free forever tier, 5% conversion, longer conversion cycle.
  Best for products with network effects or high daily usage.
- **Free Trial**: time-limited, 17% conversion, urgency-driven. Best for
  products with clear time-to-value.
- **Reverse Trial**: start with paid trial, downgrade to freemium. Highest
  first-month conversion + long-tail from engaged free users.
- **Hybrid (PLG + Sales)**: self-serve for SMB, sales-assist for enterprise.
  Most common at scale.

### Phase 2: PQL Scoring
Product Qualified Leads are users showing buying signals through behavior:
usage nearing plan limits, feature adoption by new department, multiple
users sharing one account, "can we do X?" questions, reference willingness.

Score PQLs and route: Touchless (self-serve upgrade) for low ACV, Sales-
assist for mid-market, Enterprise AE for high ACV.

### Phase 3: Activation Optimization
The aha moment — the action where value first clicks. Measure time-to-value.
Activation rate benchmarks: 20-40% normal. Single-player products aim for
40%+. Multi-player products expect lower.

### Phase 4: PLG Metrics
Natural Rate of Growth: % of ARR from organic, product-driven channels.
NDR: 130-150% for best-in-class PLG. CAC payback replaced by net new ARR
vs cash burned ratio.

## Output Format
PLG strategy with model recommendation, PQL scoring model, activation
funnel map, and PLG metrics dashboard.


## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls
1. **PLG without product readiness** — 97% want to try before buying, but
   only if the product delivers value in the trial window.
2. **Freemium without conversion path** — a free tier without a clear
   upgrade trigger is a cost center, not a growth engine.
3. **Blended metrics** — PLG and sales-led metrics don't mix. Track separately.

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

- OpenView PLG Framework: apply only the part that directly improves the requested deliverable.
- Wes Bush Product-Led Growth: apply only the part that directly improves the requested deliverable.
- Kyle Poyar Growth Unhinged: apply only the part that directly improves the requested deliverable.
- Blake Bartlett PLG Traits: apply only the part that directly improves the requested deliverable.

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
- **freemium-optimization**: Deep dive on freemium conversion
- **pricing-strategy**: PLG-specific pricing and packaging
- **saas-metrics-calculator**: PLG-specific metric calculations

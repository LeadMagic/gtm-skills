---
name: revenue-forecasting
description: >-
  Build an evidence-based B2B revenue forecast with category definitions, opportunity-level rollup, pipeline coverage, conversion and timing assumptions, scenario ranges, inspection cadence, and forecast accuracy tracking. Use when preparing weekly forecasts, board outlooks, capacity plans, or forecast-miss diagnostics.
license: MIT
compatibility: Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, OpenCode, Goose, Hermes, Jesse, Windsurf, Zed
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: sales-revops
  tags: [forecasting, revenue, revops, pipeline, capacity-planning]
  related_skills: [pipeline-management, gtm-metrics, sales-team-building, financial-modeling]
  frameworks:
    - "Clari — forecast accuracy, coverage, conversion, and slipped-deal inspection"
    - "Winning by Design — recurring-revenue math and evidence-based stage conversion"
    - "John McMahon — commit, likely, and upside evidence inspection"
    - "Dave Kellogg — triangulation forecasts and distinct forecast, scrub, and deal-review cadences"
---

# Revenue Forecasting

## Overview

Create a forecast that explains both the number and the evidence behind it. This skill combines deal-level judgment with historical conversion, timing, capacity, and scenario math. It produces a model, inspection agenda, change log, and accuracy scorecard instead of a single untraceable target.

## When to Use

- A weekly, monthly, quarterly, or board revenue forecast is needed.
- Commit calls rely on rep confidence instead of buyer evidence.
- Pipeline coverage looks healthy but revenue repeatedly slips.
- Finance, sales, and customer success use different forecast assumptions.
- A team needs base, downside, and upside scenarios or capacity implications.

## Authoritative Foundations

- **Clari — forecast operating metrics.** Track forecast accuracy, pipeline coverage, conversion, and slipped deals together; a final number without movement and error analysis is incomplete.
- **Winning by Design — recurring-revenue math.** Model stage conversion, cycle timing, average contract value, retention, and expansion according to the motion rather than using one universal coverage ratio.
- **John McMahon — evidence inspection.** Separate commit, likely, and upside and require named buyer evidence, risks, and mitigations for each material deal.
- **Dave Kellogg — forecast triangulation.** Compare rep, manager, stage-weighted,
  and forecast-category-weighted views. Keep the forecast call, pipeline scrub,
  and deal review as distinct operating meetings so each has one decision job.

## Prerequisites

- Forecast period, currency, revenue definition, and target.
- Opportunity stage history and expected close dates.
- Historical conversion, cycle length, average value, and slip data by segment.
- Owners for sales, RevOps, finance, and post-sale assumptions.

## Step-by-Step Process

### 1. Define the forecast contract

State whether the forecast covers bookings, ARR, recognized revenue, consumption, renewals, or expansion. Record currency, time zone, cutoff, data snapshot, and owner.

### 2. Normalize categories

Define pipeline, upside, likely, commit, and closed using observable exit criteria. Document who can change a category and when. Avoid labels that mean different things by manager.

### 3. Build the opportunity rollup

Use `templates/forecast-model.csv`. For each deal, capture amount, category, stage, buyer evidence, remaining risk, next event, expected date, probability basis, and scenario inclusion.

### 4. Add historical math

Calculate conversion and timing distributions by segment, source, motion, and stage where sample size allows. Compare manager judgment with historical likelihood; preserve both instead of blending them invisibly.

### 5. Model scenarios

Produce downside, base, and upside cases. Include existing closed revenue, weighted open pipeline, expected new pipeline, renewals, expansion, churn, and implementation or consumption timing when relevant.

### 6. Inspect movement and risk

Run `templates/inspection-agenda.md`. Focus on category changes, slipped dates, amount changes, stage aging, absent buyer events, concentration, and new evidence since the prior snapshot.

### 7. Reconcile cross-functional views

Align Sales, RevOps, Finance, and CS on definitions and deltas. Record unresolved assumptions explicitly; do not hide disagreement inside an averaged number.

### 8. Score forecast accuracy

After the period, measure absolute and directional error, commit attainment, slip rate, conversion calibration, and bias by team or segment. Turn recurring miss patterns into process or data fixes.

## Output Format

Produce a forecast pack containing:

1. Forecast contract and data snapshot.
2. Category definitions and governance.
3. Opportunity rollup with evidence and risk.
4. Historical conversion and timing assumptions.
5. Downside, base, and upside bridge.
6. Inspection notes and change log.
7. Capacity or cash implications.
8. Accuracy scorecard and corrective actions.

## Quality Check

- [ ] Revenue type, period, currency, cutoff, and owner are explicit.
- [ ] Categories use observable evidence.
- [ ] Historical math is segmented and sample limitations are visible.
- [ ] Scenarios reconcile to the opportunity-level model.
- [ ] Slips, concentration, and assumption changes are surfaced.
- [ ] Cross-functional disagreements remain visible.
- [ ] Accuracy and bias will be measured after close.

## Common Pitfalls

1. **Treating pipeline coverage as a forecast.** Coverage ignores timing and quality. Fix: model conversion and close-date behavior by cohort.
2. **Using rep probability as evidence.** Confidence can conceal missing buyer action. Fix: require named events, stakeholders, and exit criteria.
3. **Mixing bookings and revenue.** The same deal can land in different periods. Fix: define the forecast contract and timing bridge.
4. **Silently changing assumptions.** Stakeholders cannot explain deltas. Fix: keep a dated assumption and category change log.
5. **Never grading the forecast.** Bias persists without feedback. Fix: publish accuracy, slip, and calibration after every period.

## Execution Artifacts

- `references/framework-notes.md` — methodology sources and calculation rules
- `templates/output-template.md` — complete forecast pack
- `templates/forecast-model.csv` — opportunity and scenario model schema
- `templates/inspection-agenda.md` — weekly evidence-review agenda
- `scripts/check-output.py` — forecast-pack completeness validator

## Related Skills

- `pipeline-management` for stage design and qualification evidence.
- `gtm-metrics` for metric definitions and executive reporting.
- `sales-team-building` for ramp and attainment assumptions.
- `financial-modeling` for cash, budget, and scenario implications.

---
name: churn-prediction
description: >-
  Build churn prediction models — leading indicators, risk scoring, early warning
  systems, intervention playbooks. Triggers on: "churn prediction", "predict churn",
  "churn model", "early warning", "risk scoring".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: lifecycle
  tags: [lifecycle, churn-prediction, risk-scoring, retention, analytics]
  frameworks:
    - "Gainsight Churn Prediction Model"
    - "Retention Science Framework"
    - "Reforge — Lifecycle Marketing"
---

# Churn Prediction

## Overview
Churn prediction shifts retention from reactive ("they cancelled — now what?")
to proactive ("this account shows 3 risk signals — intervene now"). Early
intervention reduces churn by 20-40% compared to waiting for cancellation.
This skill covers modeling leading indicators, building risk scores, and
designing intervention playbooks.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Gainsight Churn Prediction Model.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Retention Science Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Reforge — Lifecycle Marketing.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Build a churn prediction model"
- "Predict which accounts will churn"
- "Churn risk scoring"
- "Early warning system"
- "Retention analytics"

## Lifecycle Stage

**Retention** (stage 6). Canonical index → `references/gtm-lifecycle-stages.md`.  
Metrics → `references/lifecycle-metrics-by-stage.md` (Retention).  
Scorecard → `skills/analytics/gtm-metrics/templates/stage-health-scorecard.md` (Retention panel).

## Core Principle
> The best churn signal is not "they stopped paying" — it's the behavior
> pattern they exhibit 60-90 days before they stop paying. Your job is to
> find those leading indicators and act on them while there's still time.

## Step-by-Step Process

### Phase 1: Identify Leading Indicators
Analyze churned customers looking back 90 days before cancellation:

**Product Usage Signals:**
- Login frequency declining (weekly → bi-weekly → monthly)
- Key feature usage dropping (>30% decline month-over-month)
- Time since last key action > 14 days
- Multiple users stopped logging in (if multi-seat)
- Failed imports/integrations (3+ failures = high frustration)

**Engagement Signals:**
- Stopped opening emails (unengaged for 30+ days)
- Support ticket sentiment turning negative
- No response to CSM outreach (2+ attempts)
- Missed QBR or success review meeting
- Stopped attending webinars/events they previously attended

**Business Signals:**
- Champion left the company (detected via LinkedIn)
- Company had layoffs or restructuring
- Budget cut or freeze in their department
- New competitor evaluation (detected via intent data)
- Contract renewal window approaching with no engagement

### Phase 2: Build Risk Scoring Model
Weight each signal on a 0-100 risk score:

**Critical (40 points max):**
- Champion departure: 40 points
- Key feature usage down >50%: 35 points
- No login in 30+ days: 30 points

**High (25 points max):**
- Support ticket spike (3+ in 7 days): 20 points
- No response to CSM in 14+ days: 15 points
- Missed renewal meeting: 10 points

**Medium (20 points max):**
- Email engagement dropped to 0: 10 points
- Usage declining 20-30% MoM: 10 points
- New competitor intent signal: 5 points (cumulative)

**Low (15 points max):**
- Weather signal: minor usage dip, one missed meeting

**Risk Tiers:**
- Red (70+): Immediate executive intervention required. Cancel risk in <30 days.
- Yellow (40-69): CSM intervention this week. Cancel risk in 30-60 days.
- Green (<40): Standard monitoring.

### Phase 3: Intervention Playbooks

**Red Account Playbook:**
- Day 0: CSM calls within 4 hours. "I noticed [specific signal]. Everything ok?"
- Day 0: Executive sponsor reaches out. "Your success is critical to us — let's
  solve whatever is blocking you."
- Day 1: Root cause analysis. Is it product, support, business, or competition?
- Day 3: Action plan presented to customer. Specific timeline. Named owner.
- Day 7: Check-in. "Is the plan working? What else do you need?"
- Day 14: Success review. Have the signals reversed? If not, escalate to VP CS.

**Yellow Account Playbook:**
- Day 0: CSM email: "Noticed [signal] — quick check-in?"
- Day 2: If no reply, call.
- Day 5: Value reinforcement: usage stats, ROI summary, new features they should try
- Day 10: If signals persist, escalate to Red playbook

### Phase 4: Automated Monitoring
- **Daily scan:** Run risk model on all accounts every 24 hours
- **Alert routing:** Red → CSM + VP CS + Account Executive. Yellow → CSM only.
- **Slack/email alerts:** "Account ABC moved to RED risk — champion departed,
  usage down 60%."
- **Dashboard:** Real-time risk heatmap of all accounts. Sort by risk score.
- **Trend tracking:** Is risk score improving or worsening week-over-week?

### Phase 5: Feedback Loop
- **Churn post-mortem:** For every churned account, review: what signals were
  present 90 days before churn? Why weren't they acted on? What signal did we miss?
- **Model refinement:** Every quarter, update signal weights based on which
  signals actually predicted churn vs false positives
- **False positive analysis:** Accounts flagged red that didn't churn — what
  made them different? Refine model.
- **Precision vs recall balance:** High precision = fewer false alarms but
  may miss churn. High recall = catch more churn but more false alarms.
  Tune based on CSM capacity.

## Output Format
Churn prediction model with: leading indicator catalog, risk scoring algorithm,
intervention playbooks, automated monitoring setup, and feedback loop.



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

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

**Canonical lifecycle (repo root):** `references/gtm-lifecycle-stages.md` (Retention) · `references/lifecycle-metrics-by-stage.md` · `skills/analytics/gtm-metrics/templates/stage-health-scorecard.md`

## Related Skills
- churn-prevention, cs-playbooks, onboarding-sequences, lifecycle-drips, expansion-selling

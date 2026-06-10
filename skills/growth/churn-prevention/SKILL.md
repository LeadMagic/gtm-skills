---
name: churn-prevention
description: >-
  Build churn prevention systems — early warning signal detection, customer health
  scoring, re-engagement campaigns, risk tier routing, and champion departure
  monitoring. Use when reducing churn, building retention systems, detecting
  at-risk customers, or designing proactive customer success workflows. Triggers
  on: "churn prevention", "reduce churn", "at-risk customers", "health score",
  "customer retention", "churn prediction", "save customers", "re-engagement",
  or any request about keeping customers from canceling.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: growth
  tags: [churn, retention, health-scoring, customer-success]
  related_skills: [cs-playbooks, expansion-selling, customer-marketing]
  frameworks: [Winning by Design Bowtie, Lincoln Murphy Success Gap, Gainsight CS Index]
---

# Churn Prevention

## Overview

Churn is rarely sudden. Usage drops, NPS declines, support tickets spike,
champions leave — signals appear weeks before cancellation. The gap between
signal and action is the gap between a saved customer and a lost one.

This skill builds an early warning detection system: health scoring with leading
indicators (not lagging ones), re-engagement playbooks per risk tier, and
automated workflows that trigger intervention before the customer decides to
leave. Draws from Lincoln Murphy's Success Gap framework and Gainsight's
customer health methodology.

## When to Use

- "Set up churn prevention"
- "Build a customer health score"
- "Detect at-risk customers"
- "Reduce our churn rate"
- "Create re-engagement campaigns"
- "Monitor customer health automatically"

## Authoritative Foundations

- **Lincoln Murphy** — Success Gap. Some customers use your product correctly
  and still fail. The gap between usage and outcome is where churn hides. Active
  users who aren't achieving their Desired Outcome are at higher risk than
  inactive users.
- **Gainsight CS Index** — 400+ companies benchmarked. Leading indicators
  (sentiment, engagement depth, stakeholder changes) predict churn better than
  lagging indicators (renewal date proximity).
- **Winning by Design Bowtie** — Churn is a lifecycle stage, not an event.
  Prevention starts at onboarding.

## Step-by-Step Process

### Phase 1: Signal Detection

Monitor these signals continuously:

| Signal | What It Means | Urgency |
|---|---|---|
| Usage decline (>30% over 30 days) | Product is no longer part of workflow | High — intervene within 48 hours |
| NPS/CSAT drop (2+ points) | Satisfaction declining | High — reach out personally |
| Support ticket spike | Something broke or changed | Medium — investigate pattern |
| Champion departure (job change) | Internal advocate lost | Critical — immediate re-engagement |
| Payment failure | Technical issue or intent | High — resolve within 24 hours |
| No login for 14+ days | Abandonment risk | Medium — re-engagement sequence |
| Key feature unused | Not getting full value | Medium — education/training |
| Contract approaching without engagement | Silent renewal at risk | High — executive alignment call |

### Phase 2: Health Scoring

Score each account 0-100 across three dimensions:

**Product Usage (0-40 points):**
- Login frequency, key feature adoption, depth of usage, data volume.

**Engagement (0-30 points):**
- Response to CSM outreach, attendance at webinars/QBRs, community participation,
  feature request activity (positive signal — they're invested).

**Relationship Health (0-30 points):**
- NPS/CSAT trend, champion strength, executive sponsor engagement, expansion
  discussions, reference willingness.

**Risk Tiers:**
- **Red (<50):** immediate CSM personal outreach. Within 24 hours.
- **Yellow (50-74):** automated nurture with value reminders. Monitor weekly.
- **Green (75+):** healthy. Expansion targeting. Quarterly check-in.

### Phase 3: Re-Engagement Playbooks

**Red — Critical Intervention:**
1. CSM calls within 24 hours. Not email — call.
2. Acknowledge the issue directly. "We noticed [specific signal]. How can we help?"
3. Create a 30-day success plan with specific milestones.
4. Executive sponsor alignment call if available.
5. Weekly check-ins until score returns to yellow.

**Yellow — Automated Nurture:**
1. Triggered email sequence: value reminder → success story → best practice guide.
2. In-app message highlighting unused features relevant to their use case.
3. Invitation to customer community or upcoming webinar.
4. Re-score after 30 days.

### Phase 4: Champion Departure Protocol

Champion leaves = #1 churn predictor. When detected:
1. Immediately congratulate the champion on LinkedIn/new role.
2. Ask for an introduction to their replacement.
3. Expedite relationship-building with the new stakeholder.
4. Document all value delivered to date — the new person needs to see the ROI
   quickly.
5. If no replacement is identified within 2 weeks, escalate to executive sponsor.

## Output Format

Churn prevention system with signal catalog, health score model (weights and
thresholds), re-engagement playbook per risk tier, and monitoring dashboard spec.

## Quality Check

- [ ] Signal detection automated (not manual review)
- [ ] Health scoring uses leading indicators (not just renewal date)
- [ ] Re-engagement playbooks defined per risk tier
- [ ] Champion departure protocol in place
- [ ] Escalation path defined (CSM → CS leader → executive sponsor)
- [ ] Monthly churn rate tracked and trended

## Common Pitfalls

1. **Lagging indicators only.** Renewal date proximity is not a health score.
   It tells you when the decision happens, not whether it will be a yes.

2. **Generic re-engagement.** "We miss you" emails don't work. Reference their
   specific use case and the value they achieved when things were going well.

3. **No champion monitoring.** The single biggest churn predictor is champion
   departure. Monitor job changes across your customer base.

4. **Equal treatment of all churn risks.** A $500/month customer and a
   $50,000/year customer don't get the same intervention. Tier by revenue.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

**Canonical lifecycle (repo root):** `references/gtm-lifecycle-stages.md` (Retention) · `references/lifecycle-metrics-by-stage.md` · `references/templates/stage-health-scorecard.md`

## Related Skills

- **cs-playbooks**: Full customer success operating system
- **expansion-selling**: Turn saved customers into expansion opportunities
- **customer-marketing**: Advocacy from retained customers

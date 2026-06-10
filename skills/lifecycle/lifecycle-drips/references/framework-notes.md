# Lifecycle Drips — Framework Notes

Reference tables for `SKILL.md`. Map triggers to stage transitions before writing copy.

---

## Primary frameworks

- **Lifecycle Marketing Framework** — Stage-based triggered communications
- **HubSpot Lifecycle Stages** — Visitor → Customer → Evangelist progression
- **Reforge Lifecycle Marketing** — Behavioral triggers + measurement per stage

---

## Lifecycle stage map

| Stage transition | Trigger type | Drip to fire |
|---|---|---|
| Visitor → Lead | Form fill, signup | Welcome |
| Lead → MQL | Engagement threshold | Nurture |
| MQL → SQL | High intent | Sales handoff + confirmation |
| SQL → Opportunity | Deal created | Evaluation guide |
| Opportunity → Customer | Closed-won | Onboarding |
| Customer → Active | Aha moment | Power tips |
| Active → Power user | Advanced adoption | Reference/community |
| At-risk | Usage drop, ticket spike | Health intervention |
| Churned | Cancellation | Exit survey + win-back |

---

## Trigger types

| Type | Example | Use when |
|---|---|---|
| Behavioral | Completed first campaign | Activation drips |
| Time-based | Day 7 no key action | Re-engagement |
| Score-based | Health < threshold | CS intervention |
| Event-based | Renewal −90/60/30/14/7d | Renewal sequence |
| Manual | CSM flags account | High-touch override |

---

## Standard drip cadences

| Drip | Timing | Emails |
|---|---|---|
| Welcome | Days 0–7 | Instant welcome → Day 2 nudge → Day 5 proof → Day 7 step 2 |
| Renewal | 90/60/30/14/7d before | ROI summary → new features → check-in → offer → final |
| Expansion | Usage near limit | Limit warning → upgrade benefit → custom plan |

---

## Agent routing

| Question | Action |
|---|---|
| Build architecture | `templates/output-template.md` |
| Personalization | Usage stats, milestones, role-based variants |
| Measure | Completion rate, stage conversion, time-in-stage |

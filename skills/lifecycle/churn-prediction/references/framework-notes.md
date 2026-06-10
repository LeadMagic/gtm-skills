# Churn Prediction — Framework Notes

Reference tables for `SKILL.md`. Weight signals by tier; act on Red within 4 hours.

---

## Primary frameworks

- **Gainsight Churn Prediction Model** — Health score + leading indicators
- **Retention Science Framework** — 60–90 day lookback on churned cohorts
- **Reforge Lifecycle Marketing** — Intervention timing by risk tier

---

## Leading indicator catalog

| Category | Signal | Typical lead time |
|---|---|---|
| Product | Login frequency decline, feature usage −30% MoM, no key action 14d | 60–90 days |
| Engagement | Email unengaged 30d, negative support sentiment, missed QBR | 30–60 days |
| Business | Champion departure, layoffs, budget freeze, competitor intent | 14–90 days |

---

## Risk scoring weights

| Tier | Max pts | Examples |
|---|---:|---|
| Critical | 40 | Champion left (40), usage −50% (35), no login 30d (30) |
| High | 25 | 3+ tickets/7d (20), no CSM reply 14d (15), missed renewal mtg (10) |
| Medium | 20 | Zero email opens (10), usage −20–30% (10), competitor intent (5) |
| Low | 15 | Minor dips, one missed meeting |

**Risk tiers:** Red 70+ (intervene <30d). Yellow 40–69 (CSM this week). Green <40 (monitor).

---

## Intervention playbooks

| Tier | Day 0 | Day 1–3 | Day 7–14 |
|---|---|---|---|
| Red | CSM call 4h + exec sponsor | Root cause + action plan | Success review; escalate if no reversal |
| Yellow | CSM email check-in | Call if no reply; ROI summary | Escalate to Red if signals persist |

---

## Agent routing

| Question | Action |
|---|---|
| Build model | `templates/output-template.md` |
| Monitor setup | Daily scan + Slack alerts to CSM/VP CS |
| Refine quarterly | Post-mortem churned accounts; tune false positives |

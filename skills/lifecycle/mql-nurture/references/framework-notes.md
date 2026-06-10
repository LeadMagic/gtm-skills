# MQL Nurture — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify track design and scoring thresholds.

---

## Primary frameworks

- **SiriusDecisions Demand Waterfall** — MQL/SQL stage definitions and handoff criteria
- **Marketo Nurture Framework** — Track-based nurture with behavioral branching
- **Reforge Lifecycle Marketing** — Engagement scoring and lifecycle stage transitions

---

## Lead scoring model

| Component | Max pts | Signals |
|---|---:|---|
| Fit score | 50 | Title match (20), company size (15), industry (15) |
| Engagement score | 50 | Downloads (5 ea), 5+ page visits (10), webinar (15), pricing page (20), demo request (50 = auto-SQL) |

**Thresholds:** MQL >40 → nurture track. SQL >70 → route to sales.

---

## Nurture tracks

| Track | Entry signal | Cadence | End CTA |
|---|---|---|---|
| Researcher | Educational content download | Weeks 1–8 | Soft demo ask week 8 |
| Evaluator | Pricing/comparison page visit | Weeks 1–5 | Demo with data week 4 |
| Event attendee | Webinar registration/attendance | Days 1–14 | Consultation offer day 14 |

**Behavioral branch:** Pricing click → Evaluator track. No opens 30d → re-engagement track.

---

## Multi-channel layering

| Channel | Trigger | Action |
|---|---|---|
| Email | Primary nurture | Value-first 80/20 educational-to-product ratio |
| LinkedIn | MQL identified | Connect + share content they engaged with |
| Retargeting | Content download / pricing visit | Case study vs demo ads by stage |
| Direct mail | ACV >$50K MQL | Physical asset (book, report, tool) |
| SDR call | Milestone (webinar, pricing) | After nurture milestone — not at form-fill |

---

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | `templates/output-template.md` |
| Validate | `scripts/check-output.py` |
| Drip timing | 7–14 day intervals; exit at 6mo no engagement |

# Cs Analytics Dashboards — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- Gainsight — Customer Health Score Framework
- Totango — Customer Success Maturity Model
- Bain & Company — NPS (Net Promoter System, Fred Reichheld)
- CustomerGauge — Account Experience (B2B NPS)
- David Skok — SaaS Churn Analysis

## Authoritative foundations

This skill is grounded in public frameworks and source material relevant to the task:

- **Gainsight — Customer Health Score Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Totango — Customer Success Maturity Model.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Bain & Company — NPS (Net Promoter System, Fred Reichheld).** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **CustomerGauge — Account Experience (B2B NPS).** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **David Skok — SaaS Churn Analysis.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## Key reference tables

| Dimension | Weight | Metrics | Data Source |
|---|---|---|---|
| **Product Usage** | 35% | Login frequency, feature adoption, depth of use | Product analytics (Amplitude/Mixpanel/Segment) |
| **Engagement** | 20% | Support tickets, NPS responses, QBR attendance, email opens | Intercom/Zendesk, NPS tool, email |
| **Financial** | 20% | Payment history, plan tier, expansion/renewal status, credit risk | Stripe/Billing, CRM |
| **Relationship** | 15% | Executive contact changes, multi-thread depth, champion health | CRM, LinkedIn, email |
| **Outcomes** | 10% | Value delivered vs expected, ROI realization, goal attainment | QBR notes, surveys |

| # | Signal | Lead Time | Action |
|---|---|---|---|
| 1 | Champion leaves company (job change) | 60-90 days | Immediately engage replacement, rebuild champion |
| 2 | Usage drops 30%+ month-over-month | 30-60 days | Proactive outreach, training, "value realization" session |
| 3 | Key user stops logging in | 60-90 days | "We noticed you haven't logged in — is everything OK?" |
| 4 | Support tickets become complaints | 30-60 days | Manager review, executive outreach if pattern |
| 5 | Payment becomes late | 0-30 days | Immediate billing + CSM outreach |
| 6 | NPS score drops 20+ points survey-over-survey | 30-90 days | Detractor follow-up within 24 hours |
| 7 | Champion stops responding to emails | 30-60 days | Escalate to executive contact, try alternate channels |
| 8 | Competitor evaluation — customer asks about comparison | 60-90 days | Competitive battlecard, executive alignment, value proof |

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |

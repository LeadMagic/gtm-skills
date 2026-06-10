---
name: cs-analytics-dashboards
description: >-
  Build customer success analytics dashboards — NPS, CSAT, CES, customer
  health scores, churn prediction models, expansion propensity, support
  volume trends, and CS team performance. Use when designing CS metrics,
  building health score models, setting up CS dashboards, analyzing churn
  patterns, or measuring CS team effectiveness. Triggers on: "CS analytics",
  "health score", "churn prediction", "NPS dashboard", "CS metrics".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: customer-success
  tags: [cs-analytics, health-score, nps, csat, churn-prediction, customer-success-metrics, dashboards]
  related_skills: [cs-playbooks, sla-management, support-tool-stack, churn-prevention, expansion-selling, gtm-metrics]
  frameworks:
    - "Gainsight — Customer Health Score Framework"
    - "Totango — Customer Success Maturity Model"
    - "Bain & Company — NPS (Net Promoter System, Fred Reichheld)"
    - "CustomerGauge — Account Experience (B2B NPS)"
    - "David Skok — SaaS Churn Analysis"
---

# CS Analytics Dashboards

## Overview

Most CS teams operate on intuition — "I feel like this customer might churn."
The mistake: relying on gut instead of a health score that flags at-risk
accounts 60 days before cancellation. This skill covers the complete CS
analytics stack: health score models, NPS/CSAT/CES programs, churn prediction,
expansion propensity, support analytics, and CS team performance dashboards.
Every metric mapped to an action.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Gainsight — Customer Health Score Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Totango — Customer Success Maturity Model.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Bain & Company — NPS (Net Promoter System, Fred Reichheld).** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **CustomerGauge — Account Experience (B2B NPS).** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **David Skok — SaaS Churn Analysis.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use

Trigger phrases: "build CS dashboard", "customer health score", "churn
prediction model", "NPS survey design", "CSAT dashboard", "CS team metrics",
"expansion propensity score", "customer success analytics", "health score
design", "predict churn", "CS KPIs"

## The CS Analytics Stack

### Layer 1: Customer Sentiment (NPS, CSAT, CES)

**NPS (Net Promoter Score):**
- Question: "How likely are you to recommend [Product] to a colleague?"
- Scale: 0-10. Promoters (9-10), Passives (7-8), Detractors (0-6)
- NPS = % Promoters - % Detractors
- Benchmark: SaaS average NPS is ~30-40. Above 50 is excellent. Above 70 is world-class.
- Cadence: Every 6 months for B2B SaaS (quarterly creates survey fatigue)
- Follow-up: "What's the primary reason for your score?" (open text = gold)

**CSAT (Customer Satisfaction):**
- Question: "How satisfied are you with [specific interaction]?"
- Scale: 1-5 (stars or emoji)
- Target: 4.0+ average. Below 3.5 = systemic issue.
- Trigger: Post-ticket resolution, post-onboarding, post-QBR
- Follow-up: Scores < 3 auto-escalate to manager for personal outreach within 24 hours

**CES (Customer Effort Score):**
- Question: "How easy was it to [complete task]?"
- Scale: 1-7 (1=very difficult, 7=very easy)
- Target: 5.5+ average
- High effort = high churn risk (Gartner: 96% of high-effort customers churn)
- Best use case: Post-onboarding, post-setup, post-integration

### Layer 2: Customer Health Score

**The 5-dimension health score model:**

| Dimension | Weight | Metrics | Data Source |
|---|---|---|---|
| **Product Usage** | 35% | Login frequency, feature adoption, depth of use | Product analytics (Amplitude/Mixpanel/Segment) |
| **Engagement** | 20% | Support tickets, NPS responses, QBR attendance, email opens | Intercom/Zendesk, NPS tool, email |
| **Financial** | 20% | Payment history, plan tier, expansion/renewal status, credit risk | Stripe/Billing, CRM |
| **Relationship** | 15% | Executive contact changes, multi-thread depth, champion health | CRM, LinkedIn, email |
| **Outcomes** | 10% | Value delivered vs expected, ROI realization, goal attainment | QBR notes, surveys |

**Scoring formula:**

```
Health Score = (Product Usage × 0.35) + (Engagement × 0.20) + (Financial × 0.20)
             + (Relationship × 0.15) + (Outcomes × 0.10)

Each dimension scored 0-100:
- 85-100: Green (healthy — expand, reference, case study)
- 70-84: Yellow (watch — engagement play, additional training)
- 50-69: Orange (at-risk — intervention required, executive outreach)
- 0-49: Red (critical — immediate escalation, save play)
```

**Specific dimension scoring examples:**

**Product Usage (0-100):**
- 100: Daily active users, 80%+ feature adoption, power user behavior
- 75: Weekly active, 50%+ adoption, core features used
- 50: Monthly active, 25% adoption, surface-level usage
- 25: Erratic login, <10% adoption, single feature only
- 0: No logins in 30+ days (abandoned)

**Engagement (0-100):**
- 100: Attends QBRs, responds to outreach, submitted NPS, opens emails
- 75: Responds to CSM, attends some QBRs, occasional survey response
- 50: Responds only when they need something
- 25: Unresponsive to CSM outreach, ignores surveys
- 0: Zero engagement in 90+ days (ghost)

### Layer 3: Churn Prediction

**Early warning signals — ranked by predictive power:**

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

**Simple churn prediction model (for early stage):**
```
Churn Risk Score = 0-100

Risk Factors (add points):
+30: Champion churned (job change detected)
+25: Usage dropped >30% MoM
+20: NPS = Detractor (0-6)
+15: Payment late >15 days
+10: Key user inactive >30 days
+10: Customer unresponsive >30 days
+5: Support ticket negative sentiment

Risk Bands:
- 0-20: Low risk — business as usual
- 21-40: Moderate — CSM engages with training/value play
- 41-60: High — manager + CSM intervention, executive outreach
- 61-100: Critical — VP CS + CEO outreach, save play
```

### Layer 4: Expansion Propensity

**Signals that a customer is ready to expand:**

| Signal | Propensity | Action |
|---|---|---|
| Usage approaching plan limits | High | Proactive outreach: "You're about to outgrow your plan. Here's what's next." |
| Multiple teams/departments using product | High | Enterprise upsell or seat expansion |
| Champion requests feature in higher tier | Very High | "That feature is available in Growth. Let's walk through the upgrade." |
| Customer asks about API/webhooks | Very High | Platform/Enterprise upsell with integration support |
| QBR reveals expanding use case | High | Multi-product or seat expansion |
| NPS Promoter + healthy usage | Medium | Case study, reference program, then expansion conversation |

**Expansion Score (simplified):**
```
Expansion Score = 
  (Usage approaching limit: +30) +
  (Multi-team adoption: +25) +
  (Requested higher-tier feature: +25) +
  (NPS Promoter: +10) +
  (QBR attendance: +10)

Score:
- 70-100: Expansion playbook now
- 40-69: Nurture — additional training, showcase advanced features
- 0-39: Focus on adoption before expansion
```

### Layer 5: CS Team Performance

**Metrics to evaluate individual CSMs:**

| Metric | Good | Warning | Red Flag |
|---|---|---|---|
| NRR (book of business) | >110% | 100-110% | <100% |
| Logo Churn Rate | <1%/mo | 1-2%/mo | >2%/mo |
| Health Score (avg) | >80 | 70-80 | <70 |
| QBR Completion Rate | >90% | 75-90% | <75% |
| Expansion Revenue | >10% of book | 5-10% | <5% |
| NPS (book of business) | >50 | 30-50 | <30 |
| Time to First Value (new accounts) | <14 days | 14-30 days | >30 days |

**CS Team Dashboard (weekly review):**
```
CS TEAM DASHBOARD — Week of [date]

BOOK OF BUSINESS HEALTH:
| Metric | Value | Trend |
|---|---|---|
| Total Accounts | X | |
| At-Risk (Orange+Red) | X (Y%) | |
| Healthy (Green) | X (Y%) | |
| NRR (trailing 3mo) | X% | |
| Logo Churn (monthly) | X% | |

TEAM PERFORMANCE:
| CSM | Accounts | NPS | NRR | Churn | Health >80 | QBRs Done |
|---|---|---|---|---|---|
| [name] | X | X | X% | X% | X% | X/Y |
| ... |

AT-RISK ACCOUNTS (Red/Orange):
| Account | Score | Primary Risk | CSM | Last Action | Next Step |
|---|---|---|---|---|---|
| [name] | 38 | Champion left | [CSM] | [date] | Exec outreach |
| ... |

EXPANSION OPPORTUNITIES:
| Account | Expansion Score | Opportunity | CSM | Next Step |
|---|---|---|---|---|
| [name] | 85 | Seat expansion | [CSM] | Send proposal |
| ... |
```

## Output Format

```
CS ANALYTICS SPEC — [Company]

SURVEY PROGRAM:
- NPS: [question, scale, cadence, follow-up]
- CSAT: [question, trigger, scale, escalation]
- CES: [question, trigger, target]

HEALTH SCORE MODEL:
[5-dimension table with weights, metrics, data sources]
Scoring: 0-100 with 4 bands (Green/Yellow/Orange/Red)

CHURN PREDICTION:
- Model: [simple points-based / ML]
- Signals: [ranked list with lead times and actions]
- Alert cadence: [daily / weekly]

EXPANSION PROPENSITY:
- Signals: [list]
- Model: [scoring]

DASHBOARD:
- CS Team Dashboard: [weekly review, owner]
- Book of Business Health: [metrics and targets]
- At-Risk Accounts: [review cadence, playbook triggers]
```

## Implementation Checklist

- [ ] Health score has 5 dimensions with explicit weights (sums to 100%)
- [ ] Each health dimension has 3+ measurable sub-metrics
- [ ] Health bands have specific actions (not just "check on customer")
- [ ] NPS survey cadence is 6-month (not monthly — avoids survey fatigue)
- [ ] CSAT surveys triggered by specific events, not randomly
- [ ] Scores < 3 on CSAT auto-escalated to manager within 24 hours
- [ ] Churn prediction model generates weekly at-risk list
- [ ] Champion churn (job change) detection is automated
- [ ] CS team metrics reviewed weekly, not just quarterly
- [ ] Expansion propensity triggers specific playbook, not just "upsell"

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Health score without action.** "Customer is at 38" without "here's the
   specific 3-step save play" is useless. Fix: Every health band maps to a
   specific playbook. Green → expansion. Yellow → engagement. Orange →
   intervention. Red → save.

2. **Too many survey questions.** NPS + CSAT + CES + onboarding survey +
   feature survey + quarterly survey = survey fatigue and 5% response rates.
   Fix: NPS twice/year. CSAT post-interaction only. One onboarding survey.
   That's it.

3. **Composite health score hiding problems.** Average 75 looks healthy but
   masks that Usage is 100 and Financial is 50 (customer loves the product
   but is about to go bankrupt). Fix: Review dimension scores individually,
   not just the composite.

4. **Detractors without follow-up.** NPS Detractor without personal outreach
   within 24 hours = you don't actually care about feedback. Fix: Auto-notify
   CSM + manager on Detractor. Template for follow-up call. Track close rate
   (Detractor → Promoter conversion).

5. **Measuring activity instead of outcomes.** "# of QBRs completed" is an
   activity metric. "% of QBRs that uncovered expansion opportunities" is an
   outcome metric. Fix: Every CS metric should tie to revenue or retention.

6. **Champion churn undetected.** Your champion leaves the company and you
   find out 3 months later when the contract doesn't renew. Fix: Automated
   job change monitoring (LinkedIn alerts, LeadMagic Job Change, manual
   LinkedIn check quarterly).

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

**Canonical lifecycle (repo root):** `references/activation-playbook.md` · `references/lifecycle-metrics-by-stage.md` (Activation, Engagement, Retention) · `references/templates/lifecycle-monitoring-dashboard.md`

## Related Skills

- `cs-playbooks` — Playbooks triggered by health score bands
- `sla-management` — SLA design, escalation paths
- `support-tool-stack` — Platform analytics and reporting
- `churn-prevention` — Early warning signals, intervention plays
- `expansion-selling` — Propensity models, expansion plays
- `gtm-metrics` — Complete SaaS metrics stack

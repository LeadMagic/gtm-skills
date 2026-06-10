# Lifecycle Monitoring Dashboard

Operational template: what to watch **weekly** and **monthly** per lifecycle stage.  
Copy into Notion, Sheets, or BI tool. Thresholds → `references/lifecycle-metrics-by-stage.md`.

---

## Dashboard Header

```
Company: _______________
Period: _______________
Motion: [ ] PLG  [ ] Sales-led  [ ] Hybrid
Primary ACV band: _______________
Activation event (named): _______________
```

---

## Weekly Review (30 min — RevOps + functional owners)

| Stage | Metrics to pull | Source | Owner | This week | WoW Δ | Flag |
|---|---|---|---|---|---|---|
| Awareness | Branded search; top content → lead assists | SEO, CRM attribution | Marketing | | | |
| Acquisition | MQLs; MQL→SQL; speed-to-lead | MAP, CRM | Mktg + SDR | | | |
| **Activation** | Activation rate; median TTA; stuck >X days | Product analytics, CS | CS + Product | | | |
| Engagement | WAA %; core feature adoption | Product analytics | Product | | | |
| Revenue | New ARR; pipeline created; win rate | CRM, billing | Sales | | | |
| Retention | High-risk account count; saves in flight | CS platform | CS | | | |
| Referral | New reviews; reference asks sent | G2, CRM | Marketing | | | |

**Weekly actions log:**

| Stage | Issue | Action | Owner | Due |
|---|---|---|---|---|
| | | | | |

---

## Monthly Review (90 min — leadership)

| Stage | Metrics | Target | Actual | R/Y/G | Trend (3 mo) | Action if Yellow/Red |
|---|---|---|---|---|---|---|
| Awareness | Content-assisted pipeline % | | | | | |
| Acquisition | CAC per SQL; MQL→SQL | | | | | |
| Activation | D7 activation rate; median TTA | | | | | |
| Engagement | WAA; depth score | | | | | |
| Revenue | NRR; expansion ARR; CAC payback | | | | | |
| Retention | GRR; logo churn; contraction | | | | | |
| Referral | NPS; referral pipeline % | | | | | |

**Cross-stage checks (monthly):**

- [ ] Activated cohort 90d retention vs non-activated
- [ ] CAC payback by channel vs LTV (Skok)
- [ ] Bowtie: left (acquire) vs right (expand) ARR mix
- [ ] Founder journey gate still valid (`journey-stage-gates.md`)

---

## Activation Deep-Dive Panel (weekly — mandatory if Activation yellow/red)

| Cohort week | New accounts | Activated ≤7d | Rate | Median TTA | Stuck | Top stall step |
|---|---|---|---|---|---|---|
| W-4 | | | | | | |
| W-3 | | | | | | |
| W-2 | | | | | | |
| W-1 | | | | | | |
| Current | | | | | | |

**Stuck account playbook:**

| Day threshold | Action | Owner |
|---|---|---|
| No activation by D3 | Automated nudge + in-app guide | CS ops |
| No activation by D7 | CSM outreach (MM+) / concierge offer | CSM |
| No activation by D14 | Executive sponsor call (enterprise) | CSM + AE |

Load `references/activation-playbook.md` for experiments and audit checklist.

---

## Revenue Team Ramp Panel (if hiring)

| Role | Hires in ramp | Avg days to 1st meeting | Cert pass % | 90d attainment | Flag |
|---|---|---|---|---|---|
| SDR | | | | | |
| AE | | | | | |

Canonical ramp → `revenue-team-onboarding/references/ramp-benchmarks.md`

---

## Experiment Log (activation + acquisition)

| ID | Stage | Hypothesis | Start | End | Result | Decision |
|---|---|---|---|---|---|---|
| EXP-001 | Activation | | | | | Ship / Kill |

---

## Skills to Load by Review Type

| Review | Skills |
|---|---|
| Weekly ops | `gtm-metrics` (pipeline slice), `cs-analytics-dashboards`, `event-analytics` |
| Monthly board | `gtm-metrics`, `saas-metrics-calculator` |
| Activation crisis | `activation-playbook`, `customer-onboarding`, `onboarding-sequences` |
| Retention crisis | `churn-prediction`, `churn-prevention` |
| Full stage index | `references/gtm-lifecycle-stages.md` |

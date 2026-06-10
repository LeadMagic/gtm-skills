# Lifecycle Metrics by Stage

Metric definitions, formulas, and **R/Y/G thresholds** by lifecycle stage.  
**Canonical stage index:** `references/gtm-lifecycle-stages.md`  
**Dashboard template:** `skills/analytics/gtm-metrics/templates/lifecycle-monitoring-dashboard.md`  
**Calculator:** `saas-metrics-calculator` · **Board stack:** `analytics/gtm-metrics`

Stage-aware benchmarks follow David Skok, ChartMogul/OpenView, and WbD bowtie economics. Adjust for ACV and motion (PLG vs sales-led).

---

## 1. Awareness

| Metric | Formula / definition | Green | Yellow | Red | Owner |
|---|---|---|---|---|---|
| Branded search volume | Monthly branded keyword impressions (SEO tool) | MoM +5% | Flat ±5% | −10% MoM | Marketing |
| Content-assisted pipeline | Opps with content touch / total new opps | ≥30% | 15–29% | <15% | Marketing |
| Share of voice | Your mentions / category mentions (social listening) | Top 3 in category | Top 5 | Below top 5 | Marketing |
| Cost per engaged visitor | Spend / visitors with ≥2 pages or ≥2 min | Below channel benchmark | +20% vs benchmark | +50% vs benchmark | Marketing |
| Dark-social influenced revenue | Self-reported + modeled influenced ARR | Tracked + growing | Tracked flat | Not tracked | Marketing |

**Cadence:** Weekly channel pulse; monthly mix review.  
**Skills:** `content-marketing`, `seo-strategy`, `attribution`  
**Ref:** `references/chris-walker-mental-models.md`

---

## 2. Acquisition

| Metric | Formula / definition | Green | Yellow | Red | Owner |
|---|---|---|---|---|---|
| Visitor → lead % | Leads / unique visitors | ≥2% B2B site | 1–2% | <1% | Marketing |
| MQL volume | Count meeting MQL definition | On plan ±10% | −10–25% | >25% below plan | Marketing |
| MQL → SQL % | SQLs / MQLs (rolling 90d) | ≥25% | 15–24% | <15% | Marketing + Sales |
| Cost per SQL | S&M spend / SQLs | Below LTV:CAC path | +20% vs target | Unsustainable vs LTV | RevOps |
| Inbound speed-to-lead | Median minutes to first response | <5 min | 5–60 min | >60 min | Sales / SDR |

**Cadence:** Weekly funnel standup; monthly CAC by channel.  
**Skills:** `mql-nurture`, `inbound-triage`, `gtm-metrics`  
**Formula detail:** CAC, Magic Number → `gtm-metrics`, `saas-metrics-calculator`

---

## 3. Activation

| Metric | Formula / definition | Green | Yellow | Red | Owner |
|---|---|---|---|---|---|
| Activation rate | Accounts with activation event ≤7d / new accounts | ≥70% SMB; ≥80% MM | −10 pts vs target | −20 pts vs target | CS + Product |
| Median time-to-activation (TTA) | Median days start → activation event | Per segment table in `activation-playbook.md` | +50% vs target | 2× target | CS + Product |
| Onboarding completion % | Finished onboarding track / started | ≥85% | 70–84% | <70% | CS |
| Activated 90-day retention | Retention of D7-activated cohort | ≥85% | 70–84% | <70% | CS + Product |
| Stuck rate | No activation by day X / cohort | <10% | 10–20% | >20% | CS |

**Cadence:** Daily stuck review; weekly activation funnel.  
**Skills:** `customer-onboarding`, `onboarding-sequences`, `cs-analytics-dashboards`  
**Deep dive:** `references/activation-playbook.md`

---

## 4. Engagement

| Metric | Formula / definition | Green | Yellow | Red | Owner |
|---|---|---|---|---|---|
| Weekly active accounts (WAA) | Accounts with ≥1 core action / week | ≥60% of paid base | 40–59% | <40% | Product |
| Feature adoption (core) | Users using core feature / active users | ≥70% | 50–69% | <50% | Product |
| Depth score | Core actions per active account / week | Above baseline | −20% vs baseline | −40% vs baseline | Product + CS |
| PQL rate (PLG) | Product-qualified leads / signups | Motion-specific | Below plan | No PQL definition | Growth |
| Support tickets / active user | Tickets / WAU | Stable or down | +25% MoM | +50% MoM | CS |

**Cadence:** Weekly product review; monthly cohort engagement.  
**Skills:** `event-analytics`, `cs-playbooks`, `freemium-optimization`

---

## 5. Revenue

| Metric | Formula / definition | Green | Yellow | Red | Owner |
|---|---|---|---|---|---|
| New ARR | New logo MRR × 12 + new contract ARR | On plan | −10% | −20%+ | Sales |
| Expansion ARR | Upsell/cross-sell ARR in period | ≥20% of new ARR (enterprise) | 10–19% | <10% | CS + Sales |
| Net revenue retention (NRR) | (Start + expansion − churn − contraction) / Start | ≥110% enterprise; ≥100% SMB | −5 pts vs target | −10 pts | Finance + CS |
| Pipeline coverage | Pipeline / quota (next quarter) | ≥3× | 2–3× | <2× | Sales |
| CAC payback (months) | CAC / (new ARR × gross margin / 12) | <12 mo | 12–18 mo | >18 mo | Finance |

**Cadence:** Weekly revenue ops; monthly board package.  
**Skills:** `gtm-metrics`, `saas-metrics-calculator`, `expansion-selling`, `pipeline-management`  
**Formulas:** Skok LTV:CAC, Magic Number, Rule of 40 in `gtm-metrics`

---

## 6. Retention

| Metric | Formula / definition | Green | Yellow | Red | Owner |
|---|---|---|---|---|---|
| Gross revenue retention (GRR) | (Start − churn − contraction) / Start | ≥90% | 85–89% | <85% | CS |
| Logo churn % (monthly) | Logos lost / logos start of month | <1% SMB; <0.5% enterprise | +50% vs target | 2× target | CS |
| Churn risk (high) | Accounts risk score ≥70 / total | <10% | 10–20% | >20% | CS |
| Save rate | Saved at-risk / flagged at-risk | ≥50% | 30–49% | <30% | CS |
| Contraction MRR | Downgrade MRR / start MRR | <3% quarterly | 3–5% | >5% | CS + Finance |

**Cadence:** Weekly health review; monthly NRR/GRR close.  
**Skills:** `churn-prevention`, `churn-prediction`, `qbr-planning`  
**Early warning:** `lifecycle/churn-prediction`

---

## 7. Referral

| Metric | Formula / definition | Green | Yellow | Red | Owner |
|---|---|---|---|---|---|
| NPS | Promoters − detractors | ≥40 B2B | 20–39 | <20 | CS |
| Referenceable accounts % | Accounts willing to reference / satisfied base | ≥25% | 15–24% | <15% | CS + Marketing |
| Case studies (active) | Published in last 12 mo | ≥1 per quarter | 1 per 6 mo | None in 12 mo | Marketing |
| Referral-sourced pipeline % | Referral opps / total new opps | ≥10% | 5–9% | <5% | Marketing |
| Review velocity (G2/TR) | New reviews / quarter | On cadence plan | 50% of plan | No reviews 2+ quarters | Marketing |

**Cadence:** Monthly advocacy review; quarterly program audit.  
**Skills:** `referral-programs`, `customer-marketing`, `review-platforms`

---

## Company Journey Metrics (founder track)

Not customer lifecycle — gates from `saas-outcomes/references/journey-stage-gates.md`:

| Gate | Metric | Threshold |
|---|---|---|
| PMF search → GTM fit | Sean Ellis very disappointed | ≥40% |
| GTM fit → scale | WbD GTM Index (Operating + Math) | ≥6 each |
| Scale → optimize | Magic number | >0.75 |
| Scale → optimize | CAC payback | <18 mo while scaling |

---

## Revenue Team Ramp Metrics

Parallel internal lifecycle — `revenue-team-onboarding`:

| Metric | Green | Yellow | Red |
|---|---|---|---|
| Days to first qualified meeting (SDR) | <21 | 21–30 | >30 |
| Days to first opp (AE) | <45 | 45–60 | >60 |
| 90-day attainment vs tenured | ≥70% | 50–69% | <50% |
| Certification before live contact | 100% | Any skip | Live without cert |

---

## Integration with Existing Metric Skills

| Need | Load |
|---|---|
| Full 6-metric board stack + GTM Index | `gtm-metrics` |
| Interactive what-if / investor package | `saas-metrics-calculator` |
| Exit-weighted metrics | `saas-metrics-calculator/references/metric-definitions-exit-weight.md` |
| Public company KPI discipline | `gtm-metrics/references/public-company-gtm-metrics.md` |
| Weekly ops dashboard shell | `skills/analytics/gtm-metrics/templates/lifecycle-monitoring-dashboard.md` |
| Stage R/Y/G rollup | `skills/analytics/gtm-metrics/templates/stage-health-scorecard.md` |

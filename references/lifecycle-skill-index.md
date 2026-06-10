# Lifecycle Skill Index

Router for the **lifecycle** skill cluster and cross-category lifecycle work.  
**Canonical stage definitions:** `references/gtm-lifecycle-stages.md` (do not duplicate).

**Master router:** `foundation/using-gtm-skills` (Pattern 18) · **Category index:** `references/skill-index-master.md` · **Metrics ref:** `references/saas-metrics-reference.md`

---

## Lifecycle Cluster (`skills/lifecycle/`)

| Skill | Lifecycle stage(s) | Use when | Key artifacts |
|---|---|---|---|
| `mql-nurture` | Acquisition | MQL scoring, nurture tracks, MQL→SQL | `lifecycle/mql-nurture/templates/output-template.md` |
| `onboarding-sequences` | Activation | Email/in-app sequences, TTV, aha moment | Skill body + **`references/activation-playbook.md`** |
| `lifecycle-drips` | Activation → Referral | Trigger-based lifecycle emails | `lifecycle/lifecycle-drips/templates/output-template.md` |
| `churn-prediction` | Retention | Risk scoring, early warning | `lifecycle/churn-prediction/templates/output-template.md` |
| `re-engagement` | Engagement, Retention | Win-back, dormant leads/customers | `lifecycle/re-engagement/templates/output-template.md` |

---

## Customer Success Cluster

| Skill | Lifecycle stage(s) | Use when |
|---|---|---|
| `customer-onboarding` | Activation | Kickoff, handoff, milestones, TTV |
| `cs-playbooks` | Engagement, Retention | Health bands, interventions |
| `cs-analytics-dashboards` | Activation, Engagement, Retention | TTFV funnel, health dashboards |
| `qbr-planning` | Revenue, Retention | Expansion, renewal prep |
| `sla-management` | Activation, Engagement | Support SLAs during onboarding |

---

## Growth & Analytics

| Skill | Lifecycle stage(s) | Use when | Key artifacts |
|---|---|---|---|
| `churn-prevention` | Retention | Save plays, contraction | `references/gtm-lifecycle-stages.md` (Retention) |
| `expansion-selling` | Revenue | Upsell, cross-sell | `references/lifecycle-metrics-by-stage.md` (Revenue) |
| `referral-programs` | Referral | Advocacy mechanics | `references/gtm-lifecycle-stages.md` (Referral) |
| `customer-marketing` | Referral, Awareness | Case studies, community | |
| `gtm-metrics` | All (board stack) | NRR, CAC, GTM Index | `references/lifecycle-metrics-by-stage.md` · `references/meritech-saas-benchmarks.md` |
| `saas-metrics-calculator` | Revenue, Retention | Formulas, scenarios | |
| `event-analytics` | Activation, Engagement | Product event instrumentation | |
| `freemium-optimization` | Acquisition, Activation | PLG funnel, PQL | `references/activation-playbook.md` |

---

## Inbound / Content (top of funnel)

| Skill | Stage | Use when |
|---|---|---|
| `inbound-triage` | Acquisition | Lead routing, SLA |
| `content-marketing` | Awareness | Demand creation |
| `seo-strategy` | Awareness | Organic pipeline |
| `attribution` | Awareness, Acquisition | Channel credit |

---

## Founder & Journey

| Skill | Maps to lifecycle via |
|---|---|
| `solo-founder-gtm` | PMF → Activation definition; scale gates |
| `engineer-to-founder` | PMF tests + scale gates via `solo-founder-gtm/references/pmf-testing-playbook.md`, `pmf-signal-checklist.md`, `scale-readiness-gates.md` |
| `saas-outcomes` | `journey-stage-gates.md` ↔ lifecycle stage health |
| `pmf-signal-checklist` | Pre-activation: prove retention pull (`solo-founder-gtm/references/pmf-signal-checklist.md`) |
| `scale-readiness-gates` | Require green Activation + Acquisition before scale (`solo-founder-gtm/references/scale-readiness-gates.md`) |
| `gtm-spend-management` | ARR-stage spend guardrails → `gtm-spend-management/references/spend-by-stage.md` |

---

## Revenue Team (parallel lifecycle)

| Skill | Internal stage | Use when |
|---|---|---|
| `revenue-team-onboarding` | Hire → Ramp → Productivity | SDR/AE/RevOps day 0–90 |
| `sales-enablement` | Ramp | Playbook certification |
| `sales-coaching` | Productivity | REKS, deal inspection |

---

## Canonical Monitoring Pack

| Artifact | Purpose |
|---|---|
| `references/gtm-lifecycle-stages.md` | Stage definitions, owners, skill routing |
| `references/activation-playbook.md` | Activation deep-dive + audit |
| `references/lifecycle-metrics-by-stage.md` | Formulas + R/Y/G thresholds |
| `references/templates/lifecycle-monitoring-dashboard.md` | Weekly/monthly review template |
| `references/templates/stage-health-scorecard.md` | Stage rollup R/Y/G |

---

## Recommended Load Sequences

**Build activation program:**
```
references/activation-playbook.md → customer-onboarding → onboarding-sequences
→ cs-analytics-dashboards → lifecycle-drips (post-activation triggers)
```

**Lifecycle metrics system:**
```
references/gtm-lifecycle-stages.md → references/lifecycle-metrics-by-stage.md
→ gtm-metrics → references/templates/lifecycle-monitoring-dashboard.md
```

**Reduce early churn:**
```
churn-prediction → activation-playbook (audit) → churn-prevention → cs-playbooks
```

**Full GTM lifecycle ops:**
```
using-gtm-skills (Pattern 18) → references/lifecycle-skill-index.md → skills above
```

---

## Cross-refs

- Master router → `foundation/using-gtm-skills`
- WbD Bowtie → `references/gtm-lifecycle-stages.md` (Bowtie section)
- Experts → `references/experts.md` (WbD, Skok, Lincoln Murphy, Nick Mehta/Gainsight)
- CS playbook → `references/lincoln-murphy-customer-success.md`
- Pitfalls → `references/pitfalls-index.md`

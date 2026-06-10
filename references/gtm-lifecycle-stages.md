# GTM Lifecycle Stages — Canonical Index

**Canonical home** for customer/revenue lifecycle definitions. Skills link here — do not duplicate stage tables in skill bodies.

**Related maps:** `references/lifecycle-skill-index.md` · `references/lifecycle-metrics-by-stage.md` · `references/activation-playbook.md` · `references/templates/lifecycle-monitoring-dashboard.md` · `references/templates/stage-health-scorecard.md`

**Framework alignment:** Winning by Design **Bowtie** (Acquire → Adopt → Expand) · Reforge lifecycle marketing · David Skok unit economics · Sean Ellis PMF (pre-lifecycle)

---

## Customer Lifecycle — Master Table

| Stage | Definition | Primary owner | Key metrics (3–5) | Monitoring cadence | Canonical skill(s) | Artifacts |
|---|---|---|---|---|---|---|
| **1. Awareness** | Target buyers know you exist — brand, content, dark social, community, B2B creators | Marketing | Branded search volume; share of voice; content-assisted pipeline %; dark-social influenced opps; ICP creator engagement %; cost per engaged visitor | Weekly pulse; monthly channel review | `content-marketing`, `seo-strategy`, `paid-social-strategy`, `podcast-gtm`, `customer-marketing`, `social-selling` | `references/chris-walker-mental-models.md` · `references/b2b-influencer-strategy.md` · `references/templates/lifecycle-monitoring-dashboard.md` (Awareness row) |
| **2. Acquisition** | Known visitors become identifiable leads — capture, qualify, route | Marketing + RevOps | Visitor→lead %; MQL volume; MQL→SQL %; CPL; lead response time (inbound) | Weekly funnel; monthly CAC by channel | `inbound-triage`, `mql-nurture`, `lead-finding`, `attribution` | `lifecycle/mql-nurture` · `references/lifecycle-metrics-by-stage.md` |
| **3. Activation** | New customer/user achieves **first value event** (not login) — aha moment, TTV | CS + Product | Activation rate (% hit event ≤7d); median time-to-activation; onboarding completion %; 90-day retention of activated cohort; activation→expansion % | **Daily** stuck-account review; weekly activation funnel | `customer-onboarding`, `onboarding-sequences`, `cs-analytics-dashboards` | **`references/activation-playbook.md`** · `references/templates/stage-health-scorecard.md` |
| **4. Engagement** | Activated users adopt core workflow — depth, breadth, habit | Product + CS | DAU/WAU or weekly active accounts; feature adoption %; depth score (actions/account); support ticket ratio; product-qualified lead (PQL) rate (PLG) | Weekly product review; monthly cohort | `cs-playbooks`, `event-analytics`, `freemium-optimization` | `references/lifecycle-metrics-by-stage.md` · `cs-analytics-dashboards` |
| **5. Revenue** | Monetization events — new ARR, expansion, upsell, cross-sell | Sales + CS | New ARR; expansion ARR; net revenue retention (NRR); average expansion deal size; conversion to paid (PLG) | Weekly revenue ops; monthly board metrics | `expansion-selling`, `pipeline-management`, `deal-desk`, `gtm-metrics` | `analytics/gtm-metrics` · `saas-metrics-calculator` |
| **6. Retention** | Renewals, churn prevention, contraction management | CS + RevOps | Gross revenue retention (GRR); logo churn %; churn risk score distribution; save rate on at-risk; contraction MRR | Weekly health review; monthly NRR/GRR | `churn-prevention`, `churn-prediction`, `qbr-planning`, `cs-playbooks` | `lifecycle/churn-prediction` · `references/templates/stage-health-scorecard.md` |
| **7. Referral** | Customers advocate — references, case studies, community, WOM | Marketing + CS | NPS / CSAT; referenceable accounts %; case studies published; referral-sourced pipeline %; community engagement index | Monthly advocacy review; quarterly program audit | `referral-programs`, `customer-marketing`, `review-platforms` | `growth/referral-programs` · `customer-marketing` |

---

## Bowtie Alignment (Winning by Design)

WbD Bowtie maps **left** (acquire) and **right** (adopt, retain, expand). Do not duplicate WbD methodology — use this routing table only.

| Bowtie zone | WbD label | Lifecycle stages (this index) | Neck / hinge |
|---|---|---|---|
| **Left** | Acquire | Awareness → Acquisition | SQL / Closed Won |
| **Neck** | First value | **Activation** | Time-to-value event |
| **Right — adopt** | Adopt | Engagement (habit + depth) | — |
| **Right — retain** | Retain | Retention | Renewal / GRR |
| **Right — expand** | Expand | Revenue (expansion) + Referral (advocacy) | NRR, advocacy pipeline |

**Load for Bowtie ops:** `gtm-system-architecture`, `pipeline-management` (left), `customer-onboarding` + `expansion-selling` (right), `gtm-metrics` (bowtie velocity).

---

## Founder Journey ↔ Lifecycle (do not conflate)

Company **journey gates** (`saas-outcomes/references/journey-stage-gates.md`) are orthogonal to customer lifecycle. Map at GTM-fit and scale only:

| Founder stage | Lifecycle focus | Gate signal |
|---|---|---|
| Idea / PMF search | Awareness + Activation definition | Sean Ellis ≥40%; activation event identified |
| GTM fit | Acquisition + Activation instrumentation | TTV <30d; activation rate tracked weekly |
| Scale | Engagement + Revenue + Retention | NRR path >100%; churn model live |
| Optimize | Retention + Referral + expansion efficiency | GRR >90%; advocacy program ROI |
| Exit optionality | Retention concentration + Referral proof | Logo concentration <15%; reference pipeline |

---

## Revenue Team Lifecycle (parallel track)

Internal ramp lifecycle — **not** customer lifecycle. Canonical: `revenue-team-onboarding`.

| Stage | Definition | Owner | Key metrics | Cadence | Skill(s) | Artifacts |
|---|---|---|---|---|---|---|
| **Hire** | Offer signed → day 0 access | RevOps + IT | Days to CRM access; security training completion | Per hire | `revenue-team-onboarding`, `gtm-recruiting` | `security-access-checklist.md` |
| **Ramp** | Week 1–12 certification + shadowing | Sales manager | Days to first qualified meeting; certification pass rate | Weekly 1:1 | `revenue-team-onboarding`, `sales-enablement` | `30-60-90-sales.md`, `certification-rubric.md` |
| **Productivity** | Full quota attainment | Manager + RevOps | 90-day attainment %; SQO quality; CRM hygiene score | Monthly | `sales-coaching`, `gtm-metrics` | `ramp-benchmarks.md` |
| **Promotion / Exit** | Level change or offboard | HR + leadership | Quota attainment trend; pipeline coverage | Quarterly | `gtm-leadership` | `gtm-leadership` resignation playbook |

**Cross-link:** Customer **Activation** stage handoff from Sales → CS mirrors rep **Ramp** certification — both require defined exit criteria before "live."

---

## Stage → Skill Quick Router

| Need | Load first | Then |
|---|---|---|
| Define activation event | `references/activation-playbook.md` | `customer-onboarding`, `onboarding-sequences` |
| Weekly lifecycle review | `references/templates/lifecycle-monitoring-dashboard.md` | `gtm-metrics`, `cs-analytics-dashboards` |
| R/Y/G board for stages | `references/templates/stage-health-scorecard.md` | `references/lifecycle-metrics-by-stage.md` |
| Pre-scale PMF | `solo-founder-gtm` → `pmf-signal-checklist.md` | `journey-stage-gates.md` |
| Scale readiness | `scale-readiness-gates.md` | `gtm-metrics` GTM Index |
| MQL nurture only | `lifecycle/mql-nurture` | `references/gtm-lifecycle-stages.md` (Acquisition row) |
| Churn early warning | `lifecycle/churn-prediction` | `churn-prevention` |

Full lifecycle cluster index → `references/lifecycle-skill-index.md`.

---

## Maintenance

- **Single source:** Stage definitions live only in this file.
- **Metrics detail:** Thresholds and formulas → `references/lifecycle-metrics-by-stage.md`.
- **Activation depth:** Experiments, anti-patterns, audit → `references/activation-playbook.md`.
- **Regenerate indexes:** `npm run build` after skill path changes.

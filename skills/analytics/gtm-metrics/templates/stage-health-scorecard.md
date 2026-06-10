# Stage Health Scorecard

Roll-up **Red / Yellow / Green** per lifecycle stage for leadership and board prep.  
Thresholds → `references/lifecycle-metrics-by-stage.md` · Stage definitions → `references/gtm-lifecycle-stages.md`

---

## Scoring Rules

| Status | Rule |
|---|---|
| **Green** | All primary metrics in green band for the stage |
| **Yellow** | Any primary metric yellow; none red |
| **Red** | Any primary metric red OR two+ yellow for 2 consecutive periods |

**Primary metrics** = first 3 listed per stage in `lifecycle-metrics-by-stage.md`.

---

## Scorecard — [Company] — [Period]

| # | Stage | Primary metrics (snapshot) | Status | Owner | Top blocker | Next action | Due |
|---|---|---|---|---|---|---|---|
| 1 | Awareness | | 🟢 🟡 🔴 | Marketing | | | |
| 2 | Acquisition | | 🟢 🟡 🔴 | Marketing + RevOps | | | |
| 3 | **Activation** | | 🟢 🟡 🔴 | CS + Product | | | |
| 4 | Engagement | | 🟢 🟡 🔴 | Product + CS | | | |
| 5 | Revenue | | 🟢 🟡 🔴 | Sales + Finance | | | |
| 6 | Retention | | 🟢 🟡 🔴 | CS | | | |
| 7 | Referral | | 🟢 🟡 🔴 | Marketing + CS | | | |

---

## Metric Detail (expand per stage)

### 1. Awareness

| Metric | Actual | Green | Yellow | Red | Score |
|---|---|---|---|---|---|
| Content-assisted pipeline % | | ≥30% | 15–29% | <15% | |
| Branded search MoM | | +5% | Flat | −10% | |
| Cost per engaged visitor | | On benchmark | +20% | +50% | |

**Stage status:** _____

---

### 2. Acquisition

| Metric | Actual | Green | Yellow | Red | Score |
|---|---|---|---|---|---|
| MQL → SQL % (90d) | | ≥25% | 15–24% | <15% | |
| MQL volume vs plan | | ±10% | −10–25% | >−25% | |
| Speed-to-lead (median min) | | <5 | 5–60 | >60 | |

**Stage status:** _____

---

### 3. Activation

| Metric | Actual | Green | Yellow | Red | Score |
|---|---|---|---|---|---|
| D7 activation rate | | Per segment target | −10 pts | −20 pts | |
| Median TTA (days) | | Per `activation-playbook` | +50% | 2× | |
| Stuck rate (no activation by D7) | | <10% | 10–20% | >20% | |

**Stage status:** _____  
**If red:** Run `references/activation-playbook.md` audit checklist before scaling spend or headcount.

---

### 4. Engagement

| Metric | Actual | Green | Yellow | Red | Score |
|---|---|---|---|---|---|
| Weekly active accounts % | | ≥60% | 40–59% | <40% | |
| Core feature adoption % | | ≥70% | 50–69% | <50% | |
| Depth score vs baseline | | On baseline | −20% | −40% | |

**Stage status:** _____

---

### 5. Revenue

| Metric | Actual | Green | Yellow | Red | Score |
|---|---|---|---|---|---|
| NRR | | ≥target by segment | −5 pts | −10 pts | |
| New ARR vs plan | | On plan | −10% | −20% | |
| CAC payback (months) | | <12 | 12–18 | >18 | |

**Stage status:** _____

---

### 6. Retention

| Metric | Actual | Green | Yellow | Red | Score |
|---|---|---|---|---|---|
| GRR | | ≥90% | 85–89% | <85% | |
| Logo churn (monthly) | | On target | +50% vs target | 2× | |
| High-risk accounts % | | <10% | 10–20% | >20% | |

**Stage status:** _____

---

### 7. Referral

| Metric | Actual | Green | Yellow | Red | Score |
|---|---|---|---|---|---|
| NPS | | ≥40 | 20–39 | <20 | |
| Referral pipeline % | | ≥10% | 5–9% | <5% | |
| Referenceable accounts % | | ≥25% | 15–24% | <15% | |

**Stage status:** _____

---

## Bowtie Summary (WbD)

| Zone | Stages included | Combined status | Notes |
|---|---|---|---|
| Left (Acquire) | Awareness + Acquisition | | |
| Neck | Activation | | |
| Right (Adopt) | Engagement | | |
| Right (Retain) | Retention | | |
| Right (Expand) | Revenue (expansion) + Referral | | |

---

## Founder Journey Overlay (optional)

| Company stage | Lifecycle stages that must be green | Current |
|---|---|---|
| PMF search | Activation definition exists | |
| GTM fit | Acquisition + Activation | |
| Scale | Engagement + Revenue + Retention | |
| Optimize | Retention + Referral | |

Gate detail → `saas-outcomes/references/journey-stage-gates.md`

---

## Revenue Team Health (parallel)

| Ramp stage | Metric | Status | Notes |
|---|---|---|---|
| Ramp | 90d attainment | | |
| Productivity | Quota attainment | | |

→ `revenue-team-onboarding/references/ramp-benchmarks.md`

---

## Escalation Matrix

| If stage is RED | Escalate to | Load skills |
|---|---|---|
| Activation | CPO + CCO | `activation-playbook`, `customer-onboarding` |
| Acquisition | CMO + CRO | `mql-nurture`, `gtm-metrics` |
| Retention | CCO | `churn-prediction`, `churn-prevention` |
| Revenue | CRO + CFO | `gtm-metrics`, `pipeline-management` |

---

## Related Artifacts

- Weekly ops template → `templates/lifecycle-monitoring-dashboard.md`
- Metric formulas → `references/lifecycle-metrics-by-stage.md`
- Board metrics stack → `analytics/gtm-metrics`
- Scenario modeling → `saas-metrics-calculator`

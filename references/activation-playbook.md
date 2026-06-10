# Activation Playbook

**Activation** = the first **value event** that correlates with retention — not account creation, not email verification, not "logged in once."

**Canonical stage index:** `references/gtm-lifecycle-stages.md` (Activation row)  
**Metrics & thresholds:** `references/lifecycle-metrics-by-stage.md`  
**Monitoring:** `skills/analytics/gtm-metrics/templates/lifecycle-monitoring-dashboard.md` · `skills/analytics/gtm-metrics/templates/stage-health-scorecard.md`

---

## 1. Definition

| Term | Definition | Not this |
|---|---|---|
| **Activation event** | Product action delivering customer's *desired outcome* with their data | Login, profile complete, invite sent |
| **Aha moment** | Subjective user realization that the product works for them | Marketing tagline moment |
| **Time-to-activation (TTA)** | Elapsed time from start → activation event | Time to first login |
| **Onboarding complete** | All setup milestones done *and* activation event fired | Checklist 100% without value |

**Rule:** Define activation from **retention correlation**, not product team intuition. Analyze cohorts: users who did event X by day 7 vs those who didn't → 90-day retention delta ≥2×.

---

## 2. Time-to-Activation Benchmarks (B2B SaaS)

| Segment | ACV band | Target TTA | Red flag TTA | Activation rate target (% ≤7d) |
|---|---|---|---|---|
| Self-serve / PLG | <$1K | <1 day | >3 days | ≥60% |
| SMB | $1–10K | <7 days | >14 days | ≥70% |
| Mid-market | $10–50K | <14 days | >30 days | ≥80% |
| Enterprise | $50K+ | <30 days | >60 days | ≥85% (pilot cohort) |

Sources: Gainsight TTV, ChurnZero onboarding maturity, WbD post-sale bowtie (first value = neck). Adjust by sales-assisted vs PLG.

---

## 3. Define Your Activation Event (worksheet)

```
PRODUCT: _______________
ICP SEGMENT: _______________

Step 1 — List 5 candidate events (product actions):
1. _______________
2. _______________
3. _______________

Step 2 — Retention correlation (90-day):
| Event | % users who did by D7 | 90d retention (did) | 90d retention (didn't) | Ratio |
|---|---|---|---|---|
| | | | | |

Step 3 — Pick activation event: _______________ (highest ratio + feasible in week 1)

Step 4 — Instrument: event name in analytics = _______________
Step 5 — CRM/CS field: Activation_Date__c / health score weight
```

Load `event-analytics` for instrumentation. Load `cs-analytics-dashboards` for funnel dashboard.

---

## 4. Onboarding → Activation Handoff

| Handoff | From | To | Exit criteria | Artifact |
|---|---|---|---|---|
| **Sales → CS** | AE | CSM | Closed-won + handoff doc + kickoff scheduled | `customer-onboarding` handoff template |
| **CS → Product (PLG)** | Signup | In-app | First value path ≤3 steps visible | `onboarding-sequences` journey map |
| **Setup → Activation** | Technical onboarding | Value milestone | Integration live + first output with customer data | Milestone 2 in `customer-onboarding` |
| **Activation → Engagement** | CS | Product/CS | Activation event + 2nd workflow started | `cs-playbooks` adoption track |

**Anti-pattern:** CS celebrates "kickoff complete" while activation event never fires. **Fix:** Single CRM stage: `Activated` with required event timestamp.

---

## 5. Activation Experiments

| Experiment | Hypothesis | Metric | Min sample |
|---|---|---|---|
| Shorten path | Removing step X increases D7 activation | Activation rate | 200 signups / 30 accounts |
| Concierge vs self-serve | White-glove week 1 improves TTA for MM | Median TTA | 20 accounts per arm |
| Triggered email | Email on stall at step 2 reduces stuck % | % stuck >3d | 100 users |
| Template library | Pre-built config improves D7 activation | Activation rate | 100 users |
| Reverse demo (PLG sales) | Buyer-led demo → faster first win | TTA for sales-assisted | 15 demos |

Run via `pmf-testing-playbook` discipline (hypothesis → metric → ship/kill). Document in `skills/analytics/gtm-metrics/templates/lifecycle-monitoring-dashboard.md` experiment log.

---

## 6. Vanity Activation Anti-Patterns

| Vanity metric | Why it fails | Fix |
|---|---|---|
| % accounts created | No value proof | Replace with activation event rate |
| % completed product tour | Tours ≠ outcomes | Tie tour completion to activation correlation |
| % invited teammates | Team size ≠ value | Require team + activation event |
| Time to first login | Login is not value | Measure time to activation event |
| "Onboarding CSAT" only | Happy but not activated | Pair CSAT with TTA and 90d retention |
| Feature checklist 100% | Activity not outcome | Milestone 2 = customer-specific result |

---

## 7. Activation Audit Checklist

Use quarterly or before scale hire.

- [ ] Activation event defined from retention data (not opinion)
- [ ] Event instrumented in product analytics with stable name
- [ ] CRM/CS platform shows activation date per account
- [ ] TTA and activation rate on weekly dashboard
- [ ] Segment-specific TTA targets documented
- [ ] Sales-to-CS handoff includes customer's desired outcome (Lincoln Murphy)
- [ ] Onboarding sequence maps 3 steps max to activation (in-app)
- [ ] Stuck-account playbook: no activation by day X → CSM/product alert
- [ ] 90-day churn reported separately for activated vs not activated
- [ ] Experiments logged with ship/kill decisions
- [ ] Bowtie neck aligned: post-sale playbook names same event as product

**Score:** ≥9 checked = green · 6–8 = yellow · ≤5 = red (do not scale CS/sales until fixed).

---

## 8. Skill & Artifact Map

| Task | Skill | Artifact |
|---|---|---|
| Design onboarding sequence | `onboarding-sequences` | `lifecycle/onboarding-sequences/templates/output-template.md` |
| Enterprise kickoff + milestones | `customer-onboarding` | Handoff + 30-60-90 templates in skill |
| Dashboard spec | `cs-analytics-dashboards` | TTFV funnel |
| Board-level metrics | `gtm-metrics`, `saas-metrics-calculator` | NRR, cohort retention |
| Reduce early churn | `churn-prevention` | 90-day churn tied to activation |
| PLG activation | `freemium-optimization` | PQL definition |
| Lifecycle email at activation | `lifecycle-drips` | Trigger: activation event → power tips |

---

## 9. Cross-References

- PMF before activation scale → `solo-founder-gtm/references/pmf-signal-checklist.md`
- PMF experiments → `solo-founder-gtm/references/pmf-testing-playbook.md`
- Company scale gates → `solo-founder-gtm/references/scale-readiness-gates.md`
- Journey planning → `saas-outcomes/references/journey-stage-gates.md`
- WbD bowtie → `references/gtm-lifecycle-stages.md` (Bowtie section)
- Expert: Lincoln Murphy (desired outcome), Gainsight (TTV), WbD (post-sale) → `references/experts.md`

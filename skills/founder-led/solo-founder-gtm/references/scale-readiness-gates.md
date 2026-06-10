# Scale Readiness Gates

**Scale** = add GTM capacity (people, spend, automation) without breaking unit economics.

**Sources:** Jason Lemkin (hire triggers), Mark Roberge (playbook), WbD GTM Index, David Skok, `sales-team-building`, `gtm-spend-management`.

---

## Scale Triggers (Go)

**Go to scale** when **all** categories pass:

### 1. Repeatable motion

| Gate | Go | No-go |
|---|---|---|
| Founder closed deals | ≥10–20 same ICP/motion | <10 or inconsistent ICP |
| Playbook | Documented stages + talk track | Tribal knowledge only |
| Non-founder close | Founder not required on every deal OR AE shadow closed ≥3 | Founder-only at $1M+ ARR |
| Win rate stable | ±10% over last 20 opps | Declining win rate |

### 2. Unit economics

| Gate | Go | No-go |
|---|---|---|
| LTV:CAC | >3x | <3x |
| CAC payback | <12 mo (scale); <18 mo (caution max) | >18 mo |
| NRR | >100% | <100% while adding S&M |
| Magic number | >0.75 | <0.5 |
| Gross margin | >70% | <65% |

### 3. Capacity not bottleneck

| Gate | Go | No-go |
|---|---|---|
| Founder calendar | >70% time on sales; pipeline backlog | Founder still doing all ops |
| Pipeline coverage | ≥3x quota for next quarter | Starved pipeline |
| Delivery/CS | Can onboard 2x logos without SLA break | Implementation queue >30 days |

### 4. GTM system (WbD Index)

| Model | Go | No-go |
|---|---|---|
| Operating | ≥6 — stages + exit criteria | <6 |
| Math | ≥6 — unit economics tracked | <6 |
| Data | ≥5 — CRM reflects reality | Garbage CRM |
| Revenue | ≥5 — pricing stable | Constant one-off deals |

Index detail → `solo-founder-gtm` Phase 6, `sales-team-building` Phase 1.

---

## What to Scale First

| Priority | Action | Skill |
|---|---|---|
| 1 | AI agents / automation | `solo-founder-gtm` Phase 3 |
| 2 | GTM Engineer (workflows) | `gtm-role-descriptions/references/gtm-engineer-hiring.md` |
| 3 | Full-stack AE | `sales-team-building` |
| 4 | SDR (feed AE) | After AE at capacity |
| 5 | Paid spend (controlled) | `gtm-spend-management` + stage budget below |

**Headcount vs automation:** If task is rules-based (enrichment, routing, sequencing) → automate first. If task is judgment (discovery, negotiation) → hire after playbook exists.

---

## Stage-Appropriate Spend

Full ARR-stage table (tool spend, payroll %, hold signals) → `gtm-spend-management/references/spend-by-stage.md`.

Summary guardrails:

| ARR stage | GTM tool + payroll guardrail | Spend focus |
|---|---|---|
| $0–$500K | Tools <$300/mo; no sales payroll | Conversations, validation |
| $500K–$2M | Tools <$1K/mo; payroll <20% ARR | CRM, playbook, first AE |
| $2M–$5M | Payroll 20–30% ARR; formal vendor roster | AE team, RevOps light |
| $5M+ | Procurement per `gtm-spend-management` | PODs, enablement, paid scale |

Approval matrix → `gtm-spend-management/templates/spend-approval-matrix.md`.

---

## Go / No-Go Summary

| Decision | Criteria |
|---|---|
| **Scale GTM headcount** | All 4 categories pass + first hire = AE not SDR |
| **Scale paid acquisition** | Payback <12 mo on channel; magic number >0.75 |
| **Scale enterprise upmarket** | NRR >110%; SOC2 path (`soc2-compliance`) |
| **Hold** | Any no-go in economics or Operating Model <6 |
| **Shrink** | Churn rising 2 quarters; payback >18 mo — see `when-not-to-scale.md` |

---

## Cross-References

- Anti-patterns → `when-not-to-scale.md`
- PMF first → `pmf-signal-checklist.md`
- Hire sequence → `sales-team-building`
- Journey stage → `saas-outcomes/references/journey-stage-gates.md`
- Customer lifecycle health → `references/gtm-lifecycle-stages.md` (Activation + Acquisition must be green)
- Activation audit → `references/activation-playbook.md`
- Lifecycle monitoring → `skills/analytics/gtm-metrics/templates/stage-health-scorecard.md`
- Comp affordability → `founder-comp-playbook`
- Spend governance → `gtm-spend-management/references/spend-governance.md`
- ARR-stage spend table → `gtm-spend-management/references/spend-by-stage.md`

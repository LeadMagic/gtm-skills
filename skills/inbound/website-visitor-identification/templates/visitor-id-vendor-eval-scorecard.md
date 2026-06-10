# Visitor ID Vendor Evaluation Scorecard

*Score 1–5 per dimension. Weighted total guides keep/pilot/pass.*

---

## Vendor profile

| Field | Value |
|---|---|
| Vendor name | |
| Evaluation date | |
| Evaluator | |
| Pilot duration | 30 days recommended |
| ID level | Company / Person / Both |

---

## Scoring matrix

| Dimension | Weight | Score (1–5) | Weighted | Notes |
|---|---|---|---|---|
| **Identification accuracy** (sample n=50 manual review) | 20% | | | |
| **ICP-qualified rate** (% of IDs passing ICP filter) | 15% | | | |
| **CRM integration quality** (native vs Zapier) | 10% | | | |
| **Slack / alert UX** | 10% | | | |
| **Privacy & DPA readiness** | 15% | | | |
| **Implementation effort** (inverse: 5 = easy) | 10% | | | |
| **Cost per ICP-qualified ID** | 10% | | | |
| **Overlap with existing stack** (5 = no overlap) | 10% | | | |
| **Total** | 100% | | **/5.0** | |

**Thresholds:**
- ≥4.0 — Proceed to contract (`vendor-contracts`, `gtm-spend-management`)
- 3.0–3.9 — Extend pilot or negotiate
- <3.0 — Pass; document in stack audit (`revops-tech-stack`)

---

## Pilot metrics log

| Week | Total visits | Identified | ICP-qualified | Alerts sent | Meetings booked | Opt-outs |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |

---

## False positive sample

| # | Vendor match | Actual truth | Root cause |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

## Integration checklist

- [ ] CRM account/contact creation rules defined
- [ ] ICP filter applied before CRM write
- [ ] Slack channel + triage checklist linked
- [ ] UTM/referrer passed (`campaign-governance`)
- [ ] Suppression list sync tested
- [ ] SEP enrollment rules (if person ID) — trigger branch only
- [ ] Vendor added to spend register with owner + renewal

---

## Decision

| ☐ Proceed | ☐ Extend pilot | ☐ Pass |
|---|---|---|
| Approver | | Date |

**Stack overlap notes:**  
**Privacy review status:**  
**Annual cost estimate (`gtm-tool-cost-model`):**

# Expansion Selling — Framework Notes

Reference tables for `SKILL.md`. Post-sale revenue growth — Bowtie right side.

## Primary frameworks

- **Winning by Design — Bowtie** — Expansion is a system stage, not ad-hoc upsell. Owner: CS + AE overlay.
- **Jason Lemkin (SaaStr)** — NRR >110% drives exit multiples; expansion cheaper than new logo CAC.
- **Marc Benioff — Land-and-expand** — Bounded land deal; expand after documented ROI. CRM: separate land vs expand opps.
- **Randy Seidl** — Relationship-led expansion: stakeholder trust map before upsell. → `sales-coaching/references/randy-seidl-relationship-selling.md`
- **Gainsight / Reforge** — Health score + PQA (product-qualified account) triggers.

**Lifecycle stage:** Revenue → `references/gtm-lifecycle-stages.md` · **Metrics:** `references/saas-metrics-reference.md` (NRR)

## Expansion propensity score

| Signal | Weight | CRM field |
|---|---|---|
| Usage ≥85% of plan limit | +30 | `expansion_signal_usage` |
| Multi-team adoption | +25 | `teams_active_count` |
| Requested higher-tier feature | +25 | `feature_request_tier_gap` |
| NPS Promoter (9–10) | +10 | `nps_score` |
| QBR attended last 90d | +10 | `last_qbr_date` |

**Score >70:** Expansion playbook now · **40–69:** Nurture · **<40:** Retention focus first

## NRR benchmark quick ref

| Stage | Good NRR | Great NRR |
|---|---|---|
| SMB | 100–105% | 110%+ |
| Mid-market | 105–110% | 115%+ |
| Enterprise | 110–120% | 125%+ |

Full formulas → `saas-metrics-calculator/references/metric-definitions-exit-weight.md`

## Agent routing

| Question | Action |
|---|---|
| Land-expand CRM structure | `tools/crm-toolkit` → land-expand-account-plan |
| QBR expansion moment | `qbr-planning` |
| Churn risk before upsell | `churn-prevention`, `cs-playbooks` |
| Lifecycle monitoring | `references/lifecycle-skill-index.md` (Revenue stage) |
| Build deliverable | `templates/output-template.md` |
| Validate output | `scripts/check-output.py` |

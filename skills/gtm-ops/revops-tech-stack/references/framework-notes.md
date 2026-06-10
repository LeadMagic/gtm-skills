# RevOps Tech Stack — Framework Reference Notes

Supporting reference for `SKILL.md`. Contains the audit scorecard template,
the category-owner matrix, and the consolidation decision rules.

---

## Audit Scorecard Template

Use this template during Phase 1 to inventory every GTM tool. One row per
tool; complete all fields before scoring.

| Tool name | Category | Annual cost ($) | Owner (name) | MAU (last 30d) | Licensed seats | Utilization % | CRM integration | Bowtie stage | Renewal date |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | MAU÷seats | Yes/No/Partial | | |

**Utilization calculation:** MAU ÷ licensed seats × 100. Flag any tool below
50% for consolidation review.

**Cost per active user calculation:** Annual cost ÷ MAU ÷ 12 = monthly cost
per active user. Flag any tool above $200/month/user without documented ROI.

---

## Consolidation Decision Matrix

Apply to every tool in the audit after Phase 1 data is collected.

| Score | Utilization | CRM integration | Category overlap | Recommendation |
|---|---|---|---|---|
| Keep | ≥ 70% | Yes (native) | No overlap | Retain; optimize license count |
| Consolidate | 50-69% | Partial | Overlap exists | Negotiate; explore platform replacement |
| Cut | < 50% | No | Overlap with retained tool | Cancel at next renewal |
| Evaluate | Any | Any | Only tool in category | Retain pending switching cost analysis |

**Switching cost framework:**

| Tool type | Estimated replacement effort |
|---|---|
| CRM (Salesforce, HubSpot) | 3-6 months; data migration + re-integration required |
| Sequencer (Outreach, Salesloft) | 2-4 months; sequence migration + rep retraining |
| Conversation intelligence (Gong) | 1-2 months; recording library and coaching workflows |
| Point solutions (Calendly, scheduling) | 1-2 weeks |
| Analytics/BI (Looker, Tableau) | 1-3 months; dashboard rebuild |
| Data warehouse + dbt | 3-6 months; pipeline rebuild |

Do not cut any tool with a switching cost above 3 months without an approved
replacement plan and migration timeline.

---

## Category-Owner Matrix

In the target-state architecture, each category has exactly one owner tool.
Use this matrix to document the owner for each bowtie stage.

| Category | Bowtie stage | Owner tool | Backup / fallback |
|---|---|---|---|
| CRM | All stages | (e.g., Salesforce) | — |
| Enrichment | Acquisition | (e.g., Clay + LeadMagic) | — |
| Sequencing | Acquisition → Close | (e.g., Outreach) | — |
| Calendar/booking | Acquisition | (e.g., Calendly) | — |
| Conversation intelligence | Close | (e.g., Gong) | — |
| Forecasting | Close | (e.g., Clari) | — |
| Data warehouse | All stages (analytics) | (e.g., Snowflake) | — |
| BI / dashboards | All stages (reporting) | (e.g., Looker) | — |
| iPaaS / integration | All stages | (e.g., n8n, Workato) | — |
| Compensation | Close → Expand | (e.g., CaptivateIQ) | — |
| Territory planning | Acquisition | (e.g., Fullcast) | — |

**Rule:** If two tools appear in the same row of this matrix, run the
consolidation decision matrix to resolve the overlap before finalizing the
target state.

---

## Savings Baseline Computation

Do not assert a 15-25% savings target before completing the audit. Derive it:

1. Sum annual cost of all tools scoring "Cut" in the consolidation matrix.
2. Add estimated savings from license right-sizing on "Consolidate" tools
   (unused seats × per-seat cost).
3. Add estimated contract negotiation savings on "Keep" tools at renewal
   (use 20-25% as the negotiation baseline for multi-year commits).
4. Total = conservative savings estimate. Express as a range (low / high) and
   note assumptions.

---

## Brinker MarTech Landscape Growth Reference

| Year | Vendor count | Source |
|---|---|---|
| 2011 | ~150 | chiefmartec.com |
| 2016 | ~3,500 | chiefmartec.com |
| 2020 | ~8,000 | chiefmartec.com |
| 2023 | ~11,000 | chiefmartec.com |
| 2025 | ~15,000+ | chiefmartec.com |

Context: 100× vendor growth in 14 years. The default answer for every GTM
problem has become "add a tool." The audit process exists to push back against
that default with data.

---

## Sources

- Scott Brinker, "Marketing Technology Landscape," chiefmartec.com, 2025.
- Gartner, "Revenue Operations: Tech Stack Guidance," Gartner Research, 2022.
- Forrester, "Revenue Operations Range of Responsibilities Model," 2021.
- Winning by Design, "Revenue Architecture," winningbydesign.com.

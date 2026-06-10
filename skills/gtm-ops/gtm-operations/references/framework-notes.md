# GTM Operations — Framework Reference Notes

Supporting reference for `SKILL.md`. Contains the Gartner/Forrester stat
table, the DAMA-DMBOK dimension checklist applied to CRM data, and the
Winning by Design process-to-bowtie stage map.

---

## Gartner and Forrester RevOps Research — Key Statistics

| Source | Finding | Year |
|---|---|---|
| Gartner | 75% of highest-growth companies deployed a RevOps model | 2024 (up from <30% in 2021) |
| Gartner | Advanced-maturity RevOps teams are 2× as likely to exceed revenue goals vs developing/intermediate | 2022 |
| Gartner | Advanced-maturity RevOps teams are 2.3× as likely to exceed profit goals vs developing/intermediate | 2022 |
| Gartner | Definition: RevOps = operational integration of data, process, and KPIs — not a re-org | 2021 |
| Forrester | Centralized RevOps grew from 15% to 40% of B2B organizations | 2019 → 2021 survey |
| Forrester | Centers of excellence model grew from 18% to 37% in same period | 2019 → 2021 survey |
| Forrester | Centralization fails when individual functions feel deprioritized | Revenue Ops Range of Responsibilities Model |

---

## Gartner RevOps Maturity Stages

| Stage | Organizational signals | Process signals | Technology signals |
|---|---|---|---|
| **Developing** | No dedicated RevOps role; ops sit within each function | Processes tribal; documented nowhere | CRM exists but underused; spreadsheets dominate |
| **Intermediate** | RevOps team of 1-2; reports to CRO or CFO | Core processes documented; partial CRM enforcement | CRM configured with stage gates; dashboards used in reviews |
| **Advanced** | Strategic partner to CRO; cross-functional roadmap | All processes enforced in CRM; predictive analytics in use | Integrated stack; data warehouse; automated workflows |

Progression note: the move from developing to intermediate is primarily a
process documentation and CRM configuration effort. The move from intermediate
to advanced requires systems enforcement (validation rules, automation) and
analytics capability (data warehouse, predictive models).

---

## DAMA-DMBOK Data Quality Dimensions — CRM Application Checklist

Use these six dimensions to define measurable data quality requirements for
each CRM object. Replace "data is somewhat clean" with dimension-specific
thresholds.

| Dimension | CRM application | Measurable threshold |
|---|---|---|
| **Completeness** | Required fields populated at each stage gate | 0% null values for gated fields; report monthly |
| **Uniqueness** | No duplicate records for the same entity | Duplicate rate < 2% on Account + Contact objects |
| **Timeliness** | Data reflects current state within an acceptable window | Enrichment refresh within 48h of creation; stale flag at 90 days |
| **Validity** | Field values conform to defined formats and picklist options | 0% free-text in Stage, Lead Source, Loss Reason fields |
| **Accuracy** | CRM data matches authoritative external sources | Enrichment cross-check coverage > 80% of active accounts |
| **Consistency** | Same entity represented the same way across objects and tools | Campaign naming convention compliance > 95% |

**Enforcement approach:**
- Completeness, Validity: CRM validation rules blocking stage advancement
- Uniqueness: Duplicate detection rules run on create + nightly batch
- Timeliness: Automated enrichment job + hygiene dashboard
- Accuracy: Enrichment provider sync with conflict-flagging (not auto-overwrite)
- Consistency: Naming convention validation script in CI or CRM workflow

---

## Process-to-Bowtie Stage Map

Winning by Design defines the bowtie funnel as a recurring-revenue operating
model with distinct stages on both sides of the close. Each of the six GTM
core processes maps to one primary bowtie stage.

| GTM Process | Bowtie Stage | Revenue motion |
|---|---|---|
| Lead-to-Account | Pre-acquisition | Demand generation → CRM entry |
| Lead Routing | Acquisition | MQL → sales-accepted lead |
| Opportunity Management | Close | Evaluation → signed contract |
| Quote-to-Cash | Close | Contract → revenue recognized |
| Customer Handoff | Onboard | Signed → first value delivered |
| Data Governance | All stages | Measurement accuracy across entire bowtie |

The bowtie extends past close: a process gap in Customer Handoff degrades
retention and expansion, which shows up in GRR and NRR, not just in new
pipeline. Data Governance is the horizontal process that makes all other stages
measurable.

---

## Sources

- Gartner, "Predicts 2021: CRM and Customer Experience," Gartner Research, 2021.
- Gartner, "Revenue Operations: The Structure and Roles," Gartner Research, 2022.
- Forrester, "The Revenue Operations Imperative," Forrester Research, 2021.
- Winning by Design, "Revenue Architecture," winningbydesign.com.
- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge," 2nd ed., 2017.

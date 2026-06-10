# RACI Matrix Template — GTM Projects

**Definitions (GTM context):** [Atlassian RACI chart](https://www.atlassian.com/team-playbook/plays/raci) · [PMI RACI overview](https://www.pmi.org/learning/library/raci-matrix-responsibility-assignment-7039)

| Letter | Meaning | GTM rule |
|---|---|---|
| **R** — Responsible | Does the work | Can be multiple Rs per row |
| **A** — Accountable | Owns outcome; approves done | **Exactly one A per row** |
| **C** — Consulted | Input before decision | Two-way communication |
| **I** — Informed | Notified after decision | One-way updates |

**Anti-patterns:**
- Everyone **R**, nobody **A** → launch slips, no escalation path
- Exec as **R** on detail tasks → bottleneck
- RevOps **I** on CRM changes → attribution breaks silently

---

## Blank Template (copy per project)

**Project:** ___ **DRI:** ___ **Date:** ___

| Deliverable / workstream | R | A | C | I |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

---

## Example 1: Campaign Launch (Q3 Enterprise Webinar)

**Project:** `2026-Q3-Enterprise-Webinar-Series` · **DRI:** Marketing Ops Manager · **Launch:** 2026-09-15

| Deliverable | R | A | C | I |
|---|---|---|---|---|
| Campaign brief + ICP | PMM | CMO | Sales leader, RevOps | AE team |
| Creative assets (ads, LP) | Content + Design | Marketing Ops (DRI) | PMM | CRO |
| UTM + naming compliance | Marketing Ops | RevOps | PMM | Analytics |
| CRM campaign + validation | RevOps | RevOps | Marketing Ops | Sales ops |
| Paid spend + Ramp card | Demand gen | Marketing Ops | Finance | CRO |
| Sales sequence + talk track | Enablement | Sales enablement lead | PMM, RevOps | SDR manager |
| Launch comms (internal) | Marketing Ops | CMO | Enablement | All GTM |
| Day-7 attribution report | RevOps | RevOps | Marketing Ops | CMO, CRO |

**Notes:** RevOps **A** on CRM/UTM rows — not Marketing. Naming pattern → `campaign-governance`.

---

## Example 2: CRM Migration (HubSpot → Salesforce)

**Project:** CRM Migration Wave 1 · **DRI:** RevOps Lead · **Cutover:** 2026-11-01

| Deliverable | R | A | C | I |
|---|---|---|---|---|
| Migration charter + timeline | RevOps PM | CRO | IT, Finance | GTM leadership |
| Field mapping + data model | RevOps + GTM Engineer | RevOps Lead | Sales ops, Marketing ops | AEs |
| Sandbox build + UAT | GTM Engineer | RevOps Lead | Sales managers (2 reps) | CS |
| Integrations (seq, enrichment) | GTM Engineer | RevOps Lead | Vendor CS | Marketing |
| Training + certification | Enablement | Sales enablement lead | RevOps | All sellers |
| Cutover execution | RevOps + IT | RevOps Lead | CRO | Company |
| Rollback plan | GTM Engineer | RevOps Lead | IT | CRO |
| Post-launch hygiene dashboard | RevOps | RevOps Lead | — | GTM |

**Notes:** CRO **A** only on charter — day-to-day **A** is RevOps Lead. Stack audit prerequisite → `revops-tech-stack`.

---

## Example 3: Quarterly Business Review (QBR) Prep

**Project:** Q2 2026 GTM QBR · **DRI:** RevOps · **Meeting:** 2026-07-08

| Deliverable | R | A | C | I |
|---|---|---|---|---|
| Data pull (pipeline, ARR, NRR) | RevOps | RevOps | Finance | CRO |
| Marketing ROI slide | Marketing ops | CMO | RevOps | CRO |
| Sales attainment + forecast | Sales ops | CRO | RevOps | CEO |
| Churn / expansion narrative | CS ops | CCO | RevOps | CRO |
| Narrative + exec summary | RevOps | CRO | CMO, CCO | Board (if applicable) |
| Deck final + distribution | RevOps | CRO | — | GTM managers |

---

## Example 4: Vendor Evaluation (New Enrichment API)

**Project:** Enrichment vendor selection · **DRI:** RevOps · **Decision:** 2026-08-30

| Deliverable | R | A | C | I |
|---|---|---|---|---|
| Requirements doc | RevOps | RevOps | GTM Engineer, Marketing | CRO |
| Shortlist + demos | RevOps | RevOps | Security, Finance | — |
| POC + match-rate test | GTM Engineer | RevOps | Sales ops sample | — |
| TCO model | RevOps | Finance | RevOps | CRO |
| Contract + Ramp setup | Finance | CFO | RevOps, Legal | CRO |

**Cross-ref:** `gtm-spend-management` spend-approval-matrix by ACV tier.

---

## Monday-Morning RACI Check

- [ ] Every active project has a matrix linked from ClickUp charter
- [ ] No row with blank **A**
- [ ] No row with 4+ **R** and no named DRI in comments
- [ ] RevOps **A** or **R** on any CRM/attribution row
- [ ] Stakeholders **I** not in weekly standup (async update only)

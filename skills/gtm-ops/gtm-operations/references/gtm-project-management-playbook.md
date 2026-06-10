# GTM Project Management Playbook

**Sources:** [RevOps Co-op — Project Management in RevOps](https://www.revopscoop.com/webinar-series/revops-project-management) · [RevOps Co-op — Hiring a RevOps Project Manager](https://www.revopscoop.com/post/hiring-a-revenue-operations-professional-project-manager) · [Atlassian — RACI chart](https://www.atlassian.com/team-playbook/plays/raci) · [PMI — RACI matrix overview](https://www.pmi.org/learning/library/raci-matrix-responsibility-assignment-7039)

GTM project management is not generic PMI theater. Revenue teams run **campaign launches**, **tool rollouts**, **QBR prep**, **onboarding projects**, and **vendor evaluations** — usually with 2–6 people and a Slack channel, not a 40-person PMO.

---

## 1. When GTM Needs a Project (Not Just Tasks)

| Signal | Example | Project type |
|---|---|---|
| Cross-functional handoffs | Marketing → RevOps → Sales on launch | Campaign launch |
| System change with downtime risk | Salesforce field migration | Stack migration |
| Fixed external deadline | Board QBR, fiscal year kickoff | QBR prep |
| New vendor + process change | Ramp rollout, Clay pilot | Tool rollout |
| Ambiguous ownership | "Someone should fix UTMs" | Governance project |

**Rule:** If failure affects revenue reporting, rep workflow, or a customer-facing date → treat as a **project** with a DRI, charter, and RACI. If one person can finish in <4 hours with no dependencies → task only.

---

## 2. Lightweight vs Heavyweight PM

| Dimension | Lightweight (default for <$20M ARR) | Heavyweight (enterprise / regulated) |
|---|---|---|
| **Charter** | One-page Notion/ClickUp doc | Formal charter + steering committee |
| **Cadence** | Weekly 15-min standup + async Slack | Weekly status + monthly steering review |
| **Tool** | ClickUp List or single Board | Gantt + dependency map + change log |
| **RACI** | 5–8 rows, one accountable per row | Full matrix + sign-off gates |
| **Milestones** | 3–5 dates (kickoff, build, UAT, launch, retro) | Phase gates with exit criteria |
| **Documentation** | Living doc in project folder | Versioned specs + approval trail |

**Choose lightweight when:** team <30 GTM headcount, single CRM, one primary PM tool, launches monthly or less.

**Choose heavyweight when:** SOC2/compliance gates, multi-region rollout, CRM replacement, or >3 departments with conflicting priorities.

---

## 3. Standard GTM Project Types

### Campaign launch
- **DRI:** Marketing ops or campaign manager
- **Milestones:** Brief approved → assets ready → UTMs/CRM live → launch → 7-day metrics review
- **Dependencies:** `campaign-governance` naming, `gtm-spend-management` budget cap
- **RACI:** See `templates/raci-matrix-template.md` → Campaign Launch

### Tool rollout (RevOps stack)
- **DRI:** RevOps lead or GTM Engineer
- **Milestones:** Audit → pilot → integration test → training → cutover → 30-day adoption check
- **Dependencies:** `revops-tech-stack` bowtie mapping, `crm-integration` sync rules
- **RACI:** See RACI template → CRM Migration

### QBR prep
- **DRI:** RevOps or Chief of Staff to CRO
- **Milestones:** Data pull deadline → narrative draft → exec review → deck lock → meeting
- **Cadence:** Monthly data hygiene feeds quarterly QBR (don't cram in week 1 of quarter)

### Onboarding project (new hire cohort)
- **DRI:** Sales enablement or RevOps
- **Milestones:** Access day 0 → certification week 2 → first pipeline review week 4
- **Cross-ref:** `revenue-team-onboarding`

### Vendor evaluation
- **DRI:** RevOps + requesting dept head
- **Milestones:** Requirements → shortlist → POC → TCO model → approval → contract
- **Cross-ref:** `gtm-spend-management` spend-approval-matrix

---

## 4. Status Cadence (Monday-Morning Usable)

### Weekly project standup (15 min max)

| Order | Question | Owner answers |
|---|---|---|
| 1 | What shipped last week? | DRI |
| 2 | What's blocked? | Anyone with a blocker |
| 3 | What's due this week? | DRI |
| 4 | Any scope/date change? | DRI → stakeholders if yes |

**Async alternative:** Post same four bullets in Slack `#gtm-projects` every Monday by 10am local.

### Milestone tracker (minimum fields)

| Milestone | Target date | Status | Dependency | Blocker |
|---|---|---|---|---|
| UTM dictionary live | 2026-06-15 | On track | CRM admin | — |
| Sales training | 2026-06-20 | At risk | UTM live | No calendar hold |

**Status vocabulary:** On track · At risk · Blocked · Done (no "in progress" without a date).

### Monthly portfolio review (RevOps + GTM leadership)

- Active projects ≤ **5** per RevOps FTE (RevOps Co-op guidance: say no or queue)
- Kill or defer projects with no update in 14 days
- Reconcile roadmap to bowtie stage priorities (`revops-tech-stack`)

---

## 5. Dependencies & Critical Path

**Document dependencies explicitly** — GTM projects fail on invisible handoffs:

```
Creative assets → Landing page → UTM QA → CRM campaign record → Ads live → Attribution dashboard
```

| Dependency type | Example | Mitigation |
|---|---|---|
| **Technical** | CRM sandbox before prod | Parallel sandbox work in week 1 |
| **Approval** | Legal on outbound copy | Insert approval milestone with SLA |
| **Data** | Clean account list for ABM | Enrichment project as pre-requisite |
| **People** | SE for demo environment | Named backup in RACI |

**Critical path rule:** Only tasks on the critical path get daily attention. Everything else is secondary.

---

## 6. Project Closeout

Every GTM project ends with a **15-minute retro**:

- [ ] Did we hit the launch date (yes/no + delta days)?
- [ ] Adoption metric at day 30 (logins, campaigns compliant, etc.)?
- [ ] What broke in handoffs?
- [ ] Template updated for next run?
- [ ] RACI rows that had "everyone Responsible" — fix for next time

Archive the project List/Folder in ClickUp; keep charter and RACI in the Process Library.

---

## Cross-References

| Topic | Skill / artifact |
|---|---|
| ClickUp structure | `references/clickup-gtm-workspace.md` |
| Information architecture | `references/gtm-organization-principles.md` |
| Team roles on projects | `references/team-design-gtm-projects.md` |
| RACI templates + examples | `templates/raci-matrix-template.md` |
| Project charter | `templates/gtm-project-charter.md` |
| Campaign naming (not duplicated here) | `campaign-governance` → campaign-naming-conventions |
| Pod structure for launches | `references/force-management-playbook.md` |
| Positioning projects | `positioning-messaging` (April Dunford) |

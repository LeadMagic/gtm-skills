# Team Design for GTM Projects

**Sources:** [Force Management — alignment cadence](https://www.forcemanagement.com/) · `references/force-management-playbook.md` · [Winning by Design — POD structures](https://winningbydesign.com/) · [RevOps Co-op — RevOps project manager hiring guide](https://www.revopscoop.com/post/hiring-a-revenue-operations-professional-project-manager) · [April Dunford — positioning workstreams](https://www.aprildunford.com/)

Roles, pods, and span of control for **cross-functional GTM projects** — launches, migrations, QBRs — not full company org design.

---

## 1. Project Roles (Not Job Titles)

| Role | Definition | GTM example |
|---|---|---|
| **DRI** (Directly Responsible Individual) | Single throat to choke for outcome + date | RevOps lead on CRM migration |
| **Accountable (A)** | Signs off; often exec sponsor | CRO approves stage model change |
| **Contributor (R)** | Does the work | GTM Engineer builds Clay → CRM sync |
| **Reviewer (C)** | Must approve before ship | Legal reviews outbound email |
| **Stakeholder (I)** | Informed; no veto by default | AE leadership on sequence change |

**One DRI per project.** The DRI may also be Accountable on the RACI — but never two DRIs.

Map to RACI: `templates/raci-matrix-template.md`.

---

## 2. Cross-Functional Launch Pod

For **campaign or product launches**, staff a temporary pod (4–8 weeks):

| Pod member | Launch responsibility | Typical source team |
|---|---|---|
| Launch DRI | Charter, dates, standups | Marketing ops or PMM |
| RevOps liaison | CRM, UTMs, integrations | RevOps |
| Creative lead | Assets, LP, ads | Marketing |
| Sales enablement | Talk track, sequence | Sales enablement |
| Analytics | Dashboard + day-7 readout | RevOps / analytics |
| Exec sponsor (I) | Air cover, priority calls | CMO or CRO |

```
        Exec sponsor (I)
              │
    ┌─────────┴─────────┐
    │   Launch DRI (A)  │
    └─────────┬─────────┘
   ┌──────────┼──────────┐
   │          │          │
 RevOps    Creative   Enablement
```

**Pod economics:** Don't pull AEs into launch pod — they stay on quota. Overlay enablement + ops only ([Force Management pod model](references/force-management-playbook.md)).

---

## 3. Span of Control for Project Leads

| Project lead context | Max concurrent projects | Max pod contributors |
|---|---|---|
| RevOps IC (also BAU) | 2–3 active | 5–7 |
| Dedicated RevOps PM | 4–5 active | 10–12 |
| Marketing ops lead | 2 launches + BAU requests | 8 |
| Founder / VP (player-coach) | 1 major + 2 small | 4 |

**Force Management norm:** Manager span 6–8 ICs for **line management** — project pods are **matrix overlays**, not permanent reports.

**Warning:** If one RevOps person owns 6+ multi-week migrations, nothing ships — queue in portfolio review (`gtm-project-management-playbook.md`).

---

## 4. Positioning & Messaging Projects (April Dunford)

Positioning is a **project**, not a brainstorm:

| Phase | Owner | Output |
|---|---|---|
| Competitive alternatives | PMM (DRI) | Shortlist doc |
| Unique attributes | PMM + product | Feature → value map |
| Value themes | PMM | 3 themes max |
| Segment focus | PMM + sales leader | ICP tier pick |
| Sales narrative | Enablement | Pitch deck v1 |

Load `positioning-messaging` skill for methodology. RACI: PMM Accountable, CRO Consulted, RevOps Informed (CRM picklists).

---

## 5. Tool Rollout Team Shape

| ARR | Team | Pattern |
|---|---|---|
| <$5M | RevOps + 1 GTM Engineer | Lightweight charter; vendor CS as Contributor |
| $5–20M | RevOps PM + sys admin + enablement | Pilot pod → rollout waves |
| $20M+ | PMO-lite + workstream leads per dept | Heavyweight RACI + steering |

Cross-ref: `revops-tech-stack` Phase 1 audit before staffing.

---

## 6. RACI ↔ Team Design Checklist

Before kickoff:

- [ ] Every workstream has a named human (not "Marketing")
- [ ] Accountable is one person per major deliverable
- [ ] RevOps on every project that touches CRM or attribution
- [ ] Exec sponsor identified for scope cuts
- [ ] Pod disband date on charter (avoid permanent stealth team)

---

## Cross-References

- RACI examples → `templates/raci-matrix-template.md`
- Alignment cadence (ongoing, not project) → `force-management-playbook.md`
- Leadership hiring/firing → `gtm-leadership`
- Onboarding projects → `revenue-team-onboarding`
- ClickUp pod tasks → `clickup-gtm-workspace.md`

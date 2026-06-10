# ClickUp Workspace for GTM Teams

**Sources:** [ClickUp — How our marketing team uses ClickUp](https://clickup.com/blog/how-clickup-marketing-team-uses-clickup/) · [ClickUp Help — Workspace hierarchy for marketing teams](https://help.clickup.com/hc/en-us/articles/9907965431191-Organize-your-Workspace-Hierarchy-for-marketing-teams) · [ClickUp — Hierarchy overview](https://help.clickup.com/hc/en-us/articles/13856392825367-The-Hierarchy-overview) · [ZenPilot — ClickUp for internal marketing teams](https://www.zenpilot.com/blog/clickup-for-internal-marketing-teams/)

Practitioner patterns for revenue teams using ClickUp — **not** a full admin manual. Goal: one workspace that holds launches, RevOps requests, and docs without becoming a graveyard of abandoned Lists.

---

## 1. Hierarchy (Space → Folder → List)

```
Workspace (Company)
└── Space: GTM Operations          ← RevOps-owned command center
    ├── Folder: Launches           ← Campaign + product GTM projects
    │   ├── List: Active Launches
    │   ├── List: Launch Backlog
    │   └── List: Launch Templates (linked tasks, not duplicates)
    ├── Folder: RevOps Projects    ← Stack migrations, integrations
    │   ├── List: In Flight
    │   └── List: Roadmap
    ├── Folder: Requests           ← Intake from Sales/Marketing/CS
    │   └── List: Incoming Requests
    └── Folder: Cadence            ← QBR, weekly ops, audits
        ├── List: QBR Prep
        └── List: Recurring Ops

└── Space: Marketing               ← Marketing-owned (mirrors governance)
    ├── Folder: Campaigns & Promotions
    ├── Folder: Content & Creative
    └── Folder: Team Operations

└── Space: Process Library         ← Templates only (read-mostly)
    ├── Folder: Project Templates
    │   ├── List: Campaign Launch
    │   ├── List: Tool Rollout
    │   └── List: Onboarding Cohort
    └── Folder: RACI & Charters
```

| Level | GTM use | Owner |
|---|---|---|
| **Workspace** | One per company (or one per business unit at scale) | RevOps admin |
| **Space** | Major function: GTM Ops, Marketing, Sales Enablement | Function lead |
| **Folder** | Work category: Launches, Requests, Migrations | DRI role |
| **List** | Single project stream or template instance | Project DRI |
| **Task** | Actionable item with one assignee + due date | Contributor |

**ClickUp's own marketing team** uses Spaces per functional team, Folders/Lists for campaigns, and **Everything View** for cross-Space visibility ([ClickUp blog](https://clickup.com/blog/how-clickup-marketing-team-uses-clickup/)).

---

## 2. Views by Project Type

| Project type | Primary view | Why |
|---|---|---|
| Campaign launch | **Board** (by status) | Creative → RevOps → Live workflow |
| Multi-week rollout | **Timeline** or **Gantt** | Dependencies (sandbox → prod) |
| RevOps request queue | **List** + **Form** | Intake → triage → assign |
| Executive visibility | **Dashboard** | Milestones due, blocked count, owner workload |
| Portfolio | **Everything View** | Cross-Space blocked tasks |

### Board columns (campaign launch example)

`Intake` → `Scoping` → `Build` → `QA (UTM/CRM)` → `Ready` → `Live` → `Retro`

Status names should differ by Folder (ClickUp allows Space vs Folder status overrides).

---

## 3. Custom Fields (GTM Minimum Set)

| Field | Type | Used for |
|---|---|---|
| DRI | People | Single accountable owner |
| Bowtie stage | Dropdown | acquisition / close / expand / etc. |
| RACI link | URL | Charter or matrix doc |
| Launch date | Date | External deadline |
| Budget owner | People | Ties to `gtm-spend-management` |
| CRM campaign ID | Short text | Links to `campaign-governance` |
| Risk | Dropdown | None / At risk / Blocked |

---

## 4. Templates (Copy from Process Library)

### Campaign launch template (tasks)

1. Charter + RACI signed
2. Naming convention + UTM sheet (`campaign-governance`)
3. Asset checklist (LP, ads, email)
4. CRM campaign record + validation rules
5. Spend cap confirmed (`gtm-spend-management`)
6. Launch comms (Slack + email)
7. Day-7 metrics review task

### Onboarding cohort template

1. Access checklist (`revenue-team-onboarding`)
2. 30-60-90 plan per role
3. Certification rubric due date
4. Manager pipeline review milestone

### Stack migration template

1. Stack audit row updated (`revops-tech-stack`)
2. Integration test tasks
3. Rollback plan doc
4. Training session
5. Cutover window + war room Slack channel

**Template rule:** Store master templates in **Process Library** Space; duplicate into Active Lists per project ([ZenPilot pattern](https://www.zenpilot.com/blog/clickup-for-internal-marketing-teams/)).

---

## 5. Integrations (High Level)

| Integration | GTM pattern | Not in scope here |
|---|---|---|
| **Slack** | `#gtm-projects` notifications on status change; request Form → Slack | OAuth admin setup |
| **CRM** | Task custom field = Opportunity/Campaign ID; manual link or Zapier/n8n | Field-level sync design → `crm-integration` |
| **Calendar** | Launch dates on Timeline sync to Google Calendar for exec visibility | — |
| **Dashboards** | Widget: tasks overdue by DRI; campaigns in QA | — |

**Slack intake (RevOps Co-op pattern):** Requests start in Slack; RevOps triages into ClickUp **Incoming Requests** — two-way comms before work enters the roadmap ([RevOps Co-op webinar](https://www.revopscoop.com/webinar-series/revops-project-management)).

---

## 6. Monday-Morning ClickUp Checklist (DRI)

- [ ] Everything View: filter `status != done` AND `due this week`
- [ ] Zero tasks with no assignee in Active Launches
- [ ] Blocked tasks have comment @-mention to unblocker
- [ ] Launch dates on Timeline still match RACI charter
- [ ] Request queue: nothing >5 business days in Intake without response
- [ ] Last week's completed launches moved to Retro column / archived

---

## 7. Anti-Patterns

| Anti-pattern | Fix |
|---|---|
| One giant List for all GTM work | Split by Folder (Launches vs Requests vs Migrations) |
| Template tasks copied without clearing dates | Use ClickUp template with relative dates |
| 12 Spaces nobody navigates | Max 3–4 Spaces for GTM; use Folders for detail |
| Custom fields on every task | Required fields only on Launch + Migration Lists |
| PM tool disconnected from CRM IDs | Campaign ID custom field mandatory before `Live` |

---

## Cross-References

- Project cadence and milestones → `gtm-project-management-playbook.md`
- Naming/UTM (do not duplicate) → `campaign-governance`
- Org principles (SSOT) → `gtm-organization-principles.md`
- RACI → `templates/raci-matrix-template.md`

# GTM Organization Principles

**Sources:** [ClickUp — marketing command center](https://clickup.com/blog/how-clickup-marketing-team-uses-clickup/) · [Gartner — RevOps operational integration](https://www.gartner.com/en/sales/insights/revenue-operations) · [RevOps Co-op — Project Management in RevOps](https://www.revopscoop.com/webinar-series/revops-project-management)

How RevOps and marketing ops organize **docs, tasks, data, and dashboards** so GTM teams stop searching five tools for one answer.

---

## 1. Information Architecture (Four Layers)

| Layer | What lives here | SSOT tool | GTM examples |
|---|---|---|---|
| **Tasks & projects** | Time-bound work, owners, dates | ClickUp (or Asana/Monday) | Launch lists, migration tasks |
| **Docs & playbooks** | How-to, charters, RACI | Notion / ClickUp Docs / Confluence | UTM dictionary, integration spec |
| **Data & records** | Accounts, campaigns, pipeline | CRM (+ warehouse at scale) | Salesforce Campaign ID |
| **Dashboards** | Metrics views | CRM reports / BI | Pipeline, campaign ROI, adoption |

**Principle:** Each layer has exactly one primary home. Links bridge layers; duplicates are read-only mirrors with a "canonical" label.

```
ClickUp task ──links to──► Notion playbook
        │
        └── CRM Campaign ID field ──► Dashboard tile
```

---

## 2. Single Source of Truth (SSOT) Rules

| Object | SSOT | Never SSOT |
|---|---|---|
| Campaign name + UTMs | CRM campaign object | Spreadsheet ad hoc |
| Pipeline stages | CRM | Slide deck forecast |
| Tool inventory | `revops-tech-stack` audit sheet | Vendor inbox |
| Project status | PM tool (ClickUp) | Slack thread |
| Comp plans | HRIS / signed PDF | Manager's local copy |
| Customer health | CS platform / CRM | AE notebook |

**Enforcement:** If two systems disagree, the SSOT wins in reporting. Fix the mirror, not the dashboard definition.

---

## 3. Folder & Naming Conventions

### Docs (Notion / Drive / ClickUp Docs)

```
/GTM/
  /Playbooks/          ← Skills-aligned: outbound, inbound, lifecycle
  /Projects/
    /2026-Q3-Enterprise-Launch/   ← Match campaign-governance date token
  /Governance/
    /UTM-Dictionary/
    /Spend-Policy/
  /QBR/
    /2026-Q2/
```

**Link to campaign hierarchy** — do not invent a parallel naming scheme. Use `[Date]-[Segment]-[Channel]-[Content]-[Version]` from `campaign-governance` → `campaign-naming-conventions.md` for anything customer-facing or reportable.

### PM tool (ClickUp)

- Space = function
- Folder = work type (Launches, Requests, Migrations)
- List = project or queue
- Task title: `[Verb] [Object]` — e.g. `Publish UTM dictionary`, not `UTMs`

### CRM

- Campaign names: governance regex only
- Project codes: optional `PRJ-2026-06-ENT-WEB` internal field — not customer-facing

### Dashboards

- Prefix by audience: `GTM-Exec-`, `Mkt-Ops-`, `RevOps-Internal-`
- One dashboard per decision, not one mega-dashboard

---

## 4. Where Things Go (Decision Tree)

```
Is it a measurable customer/revenue record?
  YES → CRM (or warehouse derived from CRM)
  NO ↓
Does it have a deadline and owner?
  YES → PM tool task/list
  NO ↓
Is it procedural knowledge?
  YES → Playbook doc (linked from PM tasks)
  NO ↓
Is it a metric view?
  YES → Dashboard with CRM/warehouse source documented
```

---

## 5. RevOps Request Intake

Per [RevOps Co-op — Kimberley Castlemain](https://www.revopscoop.com/webinar-series/revops-project-management):

1. **Slack channel** for requests (fast questions)
2. **>15 seconds of work** → formal intake (Form → ClickUp List)
3. **Roadmap** for multi-week work (not reactive queue only)
4. **Say no** with priority context — document in project portfolio review

---

## 6. Monday-Morning Organization Checklist

- [ ] No new campaigns in CRM without governance naming
- [ ] Active projects each have charter link in PM tool
- [ ] Playbook docs referenced by tasks opened this week
- [ ] Dashboard definitions list SSOT field names (not "revenue column")
- [ ] Orphan Google Docs from last launch archived or linked to project
- [ ] Request queue triaged; stale Intake tasks closed or assigned

---

## Cross-References

| Need | Go to |
|---|---|
| ClickUp hierarchy | `clickup-gtm-workspace.md` |
| Campaign naming detail | `campaign-governance` |
| Project cadence | `gtm-project-management-playbook.md` |
| Spend docs | `gtm-spend-management` |
| Stack inventory | `revops-tech-stack` |

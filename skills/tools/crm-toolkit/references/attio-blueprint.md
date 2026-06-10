# Attio Setup Blueprint

Process skill: `attio-setup`. No Lead object — see `contacts-vs-leads.md`.

## Phase 0 — Prerequisites

- [ ] API key + webhook endpoint for enrichment
- [ ] Stage definitions for Deals
- [ ] `status` picklist values for People qualification

## Phase 1 — Core Objects

### Companies

| Attribute | Notes |
|---|---|
| domains | Primary dedupe key |
| name | |
| icp_tier | select |
| employee_count | enriched |
| arr_estimate | optional |

### People

| Attribute | Notes |
|---|---|
| email_addresses | dedupe key |
| name | |
| status | inbound / working / qualified / disqualified / customer |
| title | |
| enrichment_status | |

### Deals

| Attribute | Notes |
|---|---|
| stage | kanban columns |
| value | |
| close_date | |
| owner | |
| next_step | |

**Linking:** Person ↔ Company (many-to-many). Deal ↔ Company + People stakeholders.

## Phase 2 — Lists (Queues)

| List | Filter | Purpose |
|---|---|---|
| SDR Inbound | status=inbound | Daily queue |
| ICP No Deal | icp_tier=A/B AND no open deal | ABM prospecting |
| Stalled Deals | stage open AND idle >14d | Manager review |
| Unverified Email | enrichment_status≠verified | Hygiene |

Lists drive workflows — build these before automation.

## Phase 3 — Deal Stages

1. Qualified
2. Discovery
3. Demo
4. Proposal
5. Negotiation
6. Won / Lost

Require value + close_date from Discovery onward (validation via workflow).

## Phase 4 — Workflows

| Trigger | Action |
|---|---|
| Person created | Webhook enrich; set status=inbound |
| Deal stage → Won | Update Person status=customer |
| List: Stalled Deals | Slack notify owner + manager |
| Company added to ICP A | Create task for AE |

## Phase 5 — Integrations

- **Clay:** Push enriched rows to Attio API; match on domain/email
- **n8n:** Inbound form → create Person + Company → enrich
- **Product PLG:** Signup webhook → Person + Company + usage attributes

## Phase 6 — Views

Share team views:

- Kanban: Deals by stage (per owner)
- Table: Pipeline with close_date this quarter
- Timeline: Activity on enterprise accounts

## Migration from HubSpot

1. Clean dupes in HubSpot first
2. Export Contacts → People, Companies → Companies, Deals → Deals
3. Map lifecycle → `status` (do not import HubSpot internal IDs as gospel)
4. Rebuild lists manually — Attio power is in lists

## Migration from Salesforce

1. Export Accounts, Contacts, Opportunities (no Leads — or map Leads → People inbound)
2. Flatten Account hierarchy if simplified
3. Drop SF-specific validation — reimplement in Attio workflows

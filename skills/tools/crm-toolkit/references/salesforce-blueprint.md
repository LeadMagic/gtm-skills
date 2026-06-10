# Salesforce Setup Blueprint

Process skill: `salesforce-setup`. Lead vs Contact: `references/contacts-vs-leads.md`.
Enterprise GTM principles: `references/benioff-enterprise-playbook.md`.

## Phase 0 — Prerequisites

- [ ] Decide: **Leads on or off** (default: Leads on for inbound + SDR)
- [ ] Record types if multiple motions (SMB vs Enterprise)
- [ ] Stage definitions + MEDDICC fields (`pipeline-management`)
- [ ] Admin owner named (internal or SI)

## Phase 1 — Object Model

```
Lead → (convert) → Account + Contact + Opportunity
Account → many Contacts, many Opportunities
Opportunity → Contact Roles (Economic Buyer, Champion)
```

### Custom fields (Opportunity)

| Field | Stage required |
|---|---|
| Amount, CloseDate | Qualification+ |
| Next_Step__c | All open stages |
| Economic_Buyer__c | Discovery+ |
| Decision_Criteria__c | Demo+ |
| Competitor__c | Proposal+ |
| ICP_Tier__c | Qualification+ |

### Optional custom objects

- **Subscription__c** — ARR, renewal date (link to Account)
- **Usage__c** — consumption metrics for PLG assist

## Phase 2 — Lead Management

### Lead stages (SDR queue)

1. New — unassigned
2. Working — SDR active
3. Qualified — ready for convert
4. Disqualified — reason required

### Assignment

- Round-robin or territory by `Country` / `Employee_Count__c`
- **Enrich before assign:** Record-triggered Flow on Lead create → webhook

### Conversion settings

- Always create Account + Contact
- Create Opportunity when Qualified with meeting held
- Match Account by domain — prevent duplicates

## Phase 3 — Opportunity Pipeline

| Stage | Exit criteria |
|---|---|
| Prospecting | Contact identified |
| Qualification | ICP + pain + next step |
| Discovery | EB identified, MEDDICC started |
| Demo | Technical win criteria met |
| Proposal | Commercial terms sent |
| Negotiation | Legal/procurement active |
| Closed Won / Lost | Loss reason if lost |

### Validation rules

- Cannot skip stages forward
- CloseDate >= TODAY
- Amount > 0 when stage >= Proposal
- Loss_Reason__c required on Closed Lost

## Phase 4 — Flows (not Workflow Rules)

| Flow | Type | Purpose |
|---|---|---|
| Lead_Enrich_On_Create | Record-triggered | Webhook enrichment |
| Opp_Stage_Change_Tasks | Record-triggered | Task per stage |
| Stale_Opp_Alert | Scheduled | 14-day idle → Chatter/Slack |
| Renewal_Opp_Create | Scheduled | 90d before contract end |

## Phase 5 — Reporting

Dashboards:

- Pipeline by stage / rep / source
- Lead conversion rate and time-to-convert
- Forecast category (Commit / Best Case / Pipeline)
- Data quality: opps missing EB, past close date

## Phase 6 — Integrations

- Clay / LeadMagic → Salesforce: **one-way in**
- Marketing: HubSpot sync OR Pardot — pick one source of truth for email
- Product events → Contact/Account custom fields via API

## Lead Off Pattern (advanced)

For low-volume founder-led:

- Web-to-Contact/Account (custom form handler)
- Skip Lead object — use `Status__c` on Contact for SDR queue
- Requires stricter duplicate management

## Phase 7 — Customer Success & expansion (Benioff model)

Post-sale objects keep CRM honest for NRR — not new-logo only.

| Component | Salesforce pattern |
|---|---|
| Success plan | Custom object or Opp fields: `Success_Criteria__c`, `Health_Score__c` |
| Renewal | Scheduled Flow: 120d before `Contract_End__c` → Renewal Opp |
| Expansion | Separate Opp record type `Expand`; link to land Opp via `Parent_Opp__c` |
| Executive map | Contact Roles: Economic Buyer, Champion, Executive Sponsor |
| Commitment log | Long text or related `Commitment__c` records — trust selling audit trail |

Land-expand planning template: `templates/land-expand-account-plan.md`

## Migration from HubSpot

1. Export Companies → Accounts, Contacts, Deals → Opportunities
2. Map lifecycle → Lead Status or Opportunity stage history
3. Rebuild flows — do not import HubSpot workflows
4. 2-week parallel run before cutover

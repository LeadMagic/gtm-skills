# HubSpot Setup Blueprint

Process skill: `hubspot-setup`. Object model: `contacts-vs-leads.md`.

## Phase 0 — Prerequisites

- [ ] ICP tiers defined
- [ ] 5–7 deal stages with exit criteria (`pipeline-management`)
- [ ] Lifecycle stage definitions agreed (marketing + sales)
- [ ] Enrichment provider chosen (`leadmagic-toolkit`)

## Phase 1 — Objects & Properties

### Contacts

| Property | Type | Required when |
|---|---|---|
| email | default | Always |
| lifecyclestage | default | Always |
| hs_lead_status | default | SDR queue |
| icp_tier | select | SQL+ |
| enrichment_status | select | On create |
| lead_source_detail | text | On create |

### Companies

| Property | Type | Required when |
|---|---|---|
| domain | default | Always |
| icp_fit_score | number | MQL+ |
| employee_count | number | Enriched |

### Deals

| Property | Type | Required when |
|---|---|---|
| amount | default | Stage 2+ |
| closedate | default | Stage 2+ |
| pipeline | default | Always |
| dealstage | default | Always |
| next_step | text | Every stage change |

**Contacts vs leads:** Use lifecycle stages only — no duplicate records.

## Phase 2 — Lifecycle & Lead Status

```
Subscriber → Lead → MQL → SQL → Opportunity → Customer → Evangelist
```

| Transition | Criteria (example) |
|---|---|
| Lead → MQL | Score ≥ 50 OR demo request |
| MQL → SQL | SDR accepted + ICP confirmed |
| SQL → Opportunity | Deal created, amount set |
| Opportunity → Customer | Closed Won |

Parallel: `hs_lead_status` = Open | In Progress | Connected | Bad Timing | Unqualified

## Phase 3 — Pipelines

Default B2B SaaS pipeline (5–7 stages):

1. Qualified — ICP + pain confirmed
2. Discovery — SPICED captured
3. Demo — technical validation
4. Proposal — commercial sent
5. Negotiation — legal/procurement
6. Closed Won / Closed Lost

Stage properties: require Amount + Close Date from stage 2 onward.

## Phase 4 — Automation

| Workflow | Trigger | Action |
|---|---|---|
| Enrich on create | Contact created | Webhook → LeadMagic → update properties |
| MQL alert | Score threshold | Slack + assign SDR |
| Stale deal | Deal idle 14d | Task for owner |
| Closed Won | Stage = Won | Lifecycle → Customer; CS handoff |

## Phase 5 — Integrations

- **Clay → HubSpot:** One-way push; `clay_status = verified` gate for sequences
- **Product (PLG):** Event → lifecycle update via API or n8n
- **Billing:** Stripe → Company ARR field (n8n)

## Phase 6 — Reporting

Minimum dashboards:

- Pipeline by stage and source
- MQL → SQL → Won conversion
- Velocity by stage (days)
- Data health: missing amount, stale close dates

## Common Fixes

| Problem | Fix |
|---|---|
| Duplicate contacts | Enable automatic dedup; merge rules on email |
| Reps skip stages | Required fields + workflow validation |
| Marketing/Sales stage fights | Weekly lifecycle review; single doc of truth |
| Junk in sequences | Suppress non-marketing; ICP gate on enroll |

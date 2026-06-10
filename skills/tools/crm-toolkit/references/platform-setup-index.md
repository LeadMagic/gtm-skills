# Platform Setup Index

**Operating model first:** `crm-integration` → **platform config:** setup skill → **deep reference:** blueprint below.

## Workflow

```
1. pipeline-management     → stages, exit criteria, SPICED/MEDDICC fields
2. crm-integration         → lifecycle, ownership, dedupe rules
3. crm-selection.md        → HubSpot vs Salesforce vs Attio
4. contacts-vs-leads.md    → object model decision
5. [platform]-setup skill  → step-by-step rollout
6. [platform]-blueprint.md → field lists, automation catalog
7. implementation-partners.md → if SI needed
```

## Skill Map

| Platform | Setup skill (process) | Blueprint (config) | Contacts vs leads |
|---|---|---|---|
| HubSpot | `hubspot-setup` | `hubspot-blueprint.md` | Lifecycle stages — no Lead object |
| Salesforce | `salesforce-setup` | `salesforce-blueprint.md` | Lead → Account + Contact + Opp |
| Attio | `attio-setup` | `attio-blueprint.md` | People status + lists |

## Enrichment Stack

| Layer | Skills |
|---|---|
| Waterfall enrich | `clay-toolkit`, `leadmagic-toolkit` |
| Push to CRM | `clay-automation`, `n8n-toolkit` |
| Verify on create | `contact-verification` |

**Rule:** One-direction enrichment → CRM. Never two-way sync with Clay tables.

## Hygiene Cadence

| Cadence | Action |
|---|---|
| Daily | SDR queue zeroed; inbound assigned |
| Weekly | Stale deals review; unverified emails |
| Monthly | Dedupe merge; orphan contacts |
| Quarterly | Full enrichment refresh; field audit |

## Related Skills

- `crm-toolkit` — this skill (anchor)
- `pipeline-management` — stage design
- `revops-tech-stack` — full stack
- `saas-outcomes` — CRM tier by bootstrap vs venture path
- `hiring-agencies` — RevOps agency pilots

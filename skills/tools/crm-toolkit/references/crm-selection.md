# CRM Selection — HubSpot vs Salesforce vs Attio

Choose CRM for **GTM motion + team size + data model complexity**, not brand preference.

## Quick Picks

| Profile | Recommended | Why |
|---|---|---|
| Solo founder / <$1M ARR | Attio or HubSpot Starter | Low admin; API-friendly (Attio) or marketing later (HubSpot) |
| SMB sales-led $1–10M ARR | HubSpot Pro (Sales + Marketing) | Unified sequences, lifecycle, reporting |
| PLG + sales assist | HubSpot or Attio | Product events → lifecycle; deals for enterprise assist |
| Mid-market $10–30M ARR | HubSpot Enterprise or Salesforce | Territories, custom objects, permissions |
| Enterprise $30M+ ARR | Salesforce | CPQ, territories, complex approvals, SI ecosystem |
| API-first startup stack | Attio | Custom objects, lists, webhooks without SF admin tax |
| Heavy marketing + ABM | HubSpot | Native marketing hub, ads, attribution |
| Multi-division global | Salesforce | Master data, role hierarchy, Experience Cloud |

## Evaluation Scorecard

Score 1–5 each; weight for your motion.

| Criterion | Weight | HubSpot | Salesforce | Attio |
|---|---|---|---|---|
| Time to first value | High for < $5M ARR | 5 | 2 | 4 |
| Marketing automation | High if inbound-heavy | 5 | 3* | 2 |
| Custom data model | High if PLG/complex | 3 | 5 | 4 |
| Reporting / forecast | High at scale | 4 | 5 | 3 |
| Admin burden | High for small teams | 4 | 1 | 4 |
| Integration ecosystem | Medium | 5 | 5 | 3 |
| Cost at 10 seats | Medium | 3 | 2 | 4 |

*Marketing Cloud is separate; HubSpot wins integrated SMB stack.

## Cost Bands (Indicative — verify pricing)

| Stage | HubSpot | Salesforce | Attio |
|---|---|---|---|
| Starter | $20–50/seat/mo | N/A (Essentials limited) | ~$29–49/seat/mo |
| Growth | $90–150/seat/mo (Pro) | $75–150/seat/mo + implementation | $59–99/seat/mo |
| Scale | Enterprise custom | Enterprise $150–300+/seat + 2–5x SI cost | Custom |

**Hidden cost:** Salesforce implementation ($15K–$150K+); HubSpot onboarding partners; Attio often self-serve + RevOps contractor.

## When to Switch

| Signal | Direction |
|---|---|
| 3+ AEs, broken HubSpot permissions | → Salesforce or HubSpot Enterprise |
| Marketing outgrows Attio | → HubSpot |
| Salesforce admin full-time, team hates UX | → HubSpot (if enterprise features not needed) |
| Need programmable lists + fast iteration | → Attio from HubSpot |
| SOC2 + enterprise procurement demands SFDC | → Salesforce |

**Rule:** Migrate data clean first (`crm-integration` hygiene). Never lift-and-shift dirty objects.

## Stack Pairing

| CRM | Typical enrichment | Orchestration |
|---|---|---|
| HubSpot | Clay → HubSpot, LeadMagic webhooks | n8n for routing |
| Salesforce | Clay → SF, native Flow webhooks | n8n + MCP for agents |
| Attio | API webhooks, Clay push | n8n, Zapier, custom |

## Decision Workflow

1. Load `gtm-context` + `pipeline-management` (stages before software)
2. Score scorecard above with team
3. Pick platform → load `hubspot-setup` | `salesforce-setup` | `attio-setup`
4. Read `contacts-vs-leads.md` for object model
5. If implementation > 40 hours → `implementation-partners.md`

## Related

- `saas-outcomes` — bootstrap vs venture CRM tier
- `revops-tech-stack` — full GTM stack
- `hiring-agencies` — agency vs in-house for rollout

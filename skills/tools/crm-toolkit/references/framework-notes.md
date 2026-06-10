# CRM Toolkit — Framework Notes

## Primary Frameworks

- **Winning by Design — Bowtie.** CRM spans acquisition through expansion; pipeline-only configs fail CS handoff.
- **HubSpot Lifecycle Model.** Subscriber → Lead → MQL → SQL → Opportunity → Customer; single Contact record.
- **Salesforce Lead Conversion.** Lead → Account + Contact + Opportunity; assignment and dedupe at Lead.
- **Attio List Architecture.** Dynamic lists as SDR queues; flat People ↔ Companies linking.
- **Marc Benioff (Salesforce).** V2MOM alignment, trust selling, land-and-expand CRM structure, customer success objects — `benioff-enterprise-playbook.md`.

## Contacts vs Leads — Decision Rule

| Need quarantine for unqualified inbound? | Platform pattern |
|---|---|
| Yes, SDR team, high volume | Salesforce Leads OR HubSpot lifecycle + scoring OR Attio status=inbound |
| No, low volume, founder-led | Direct Contact/Account (SF) or lifecycle Lead stage (HS) or Attio qualified path |

Full guide: `references/contacts-vs-leads.md`

## Operating Assumptions

- Process before config: `pipeline-management` + `crm-integration` precede blueprints.
- Enrichment flows one direction into CRM (`clay-toolkit`, `leadmagic-toolkit`).
- Bootstrap <$5M ARR: default Attio or HubSpot unless enterprise procurement requires Salesforce.
- Partners execute documented playbooks (`hiring-agencies`) — not strategy discovery.

## Agent Use

1. If platform unknown → `crm-selection.md`
2. If Salesforce or "leads" mentioned → `contacts-vs-leads.md`
3. If platform chosen → matching `*-blueprint.md` + setup skill
4. If migration or SI → `implementation-partners.md`
5. If enterprise land-expand or NRR-led → `benioff-enterprise-playbook.md` + land-expand template
6. Cite framework that drove object model recommendation

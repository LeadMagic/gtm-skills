# Contacts vs Leads — Platform Guide

The #1 CRM architecture mistake: copying Salesforce Lead objects into HubSpot or Attio without understanding why they exist.

## Conceptual Model

| Concept | Meaning |
|---|---|
| **Lead** | Unqualified person or inquiry — may never become a customer |
| **Contact** | Known person tied to a buying relationship |
| **Account / Company** | Organization you sell to |
| **Deal / Opportunity** | Revenue pursuit with stage and amount |

**Question to answer first:** Do you need a **quarantine** for junk before it pollutes your database?

- **Yes** → Salesforce Leads (or HubSpot "non-marketing" + strict lifecycle)
- **No** → Single contact model (HubSpot default, Attio People)

## Salesforce — Lead vs Contact

### Default hierarchy

```
Lead (unqualified)
  → convert → Account + Contact (+ Opportunity optional)
Opportunity → tied to Account
Contact → many per Account; roles via Contact Roles
```

### When to use Leads

- High inbound volume (forms, events, partners) with low qualification rate
- SDR team that **works leads** before creating opportunities
- Marketing hands off raw names; sales converts after BANT/MEDDIC lite
- Duplicate rules and assignment rules at Lead object

### When to skip Leads (advanced)

- Low volume, founder-led — create Contact + Account directly via web-to-lead bypass
- PLG with product signups — Contact + Account from day one
- Requires discipline: lists/views replace "lead inbox"

### Lead conversion mapping

| Lead field | Maps to |
|---|---|
| Company | Account.Name |
| Email | Contact.Email |
| Title | Contact.Title |
| Lead Source | Contact + Opportunity (pick one source of truth) |

**Pitfall:** Converting Lead without Opportunity when SDR qualified — deal tracking breaks.

**Pitfall:** Duplicate Accounts on conversion — enable matching rules (domain, name).

### Person Accounts (B2C / solo)

Use Person Accounts when selling to individuals without company hierarchy — rare in B2B SaaS.

## HubSpot — No Lead Object

HubSpot uses **one Contact record** with **Lifecycle Stage** as qualification state.

| Lifecycle stage | Salesforce equivalent |
|---|---|
| Subscriber / Lead | Lead (early) |
| MQL | Lead (scored) |
| SQL | Lead ready for convert / early Opportunity |
| Opportunity | Open deal |
| Customer | Closed Won account |
| Evangelist | Customer advocate |

### HubSpot pattern for "lead quarantine"

1. Inbound form → Contact with Lifecycle = Lead
2. Lead scoring (fit + behavior) → MQL threshold
3. SDR sequence → meeting booked → SQL
4. Create Deal; Lifecycle = Opportunity
5. Closed Won → Customer

**Do not** create duplicate contacts for "lead" vs "contact" — use lifecycle + lists.

### Marketing vs non-marketing contacts

- **Marketing contacts:** Billable; receive marketing email
- **Non-marketing:** Sales-only records; good for purchased lists you haven't opted in

### Companies

- Always associate Contact → Company
- Deals associate to Company (primary) and Contacts (stakeholders)

## Attio — People, Companies, Deals (Flat)

No Lead object. Qualification is **attributes + lists**, not object conversion.

| Pattern | Implementation |
|---|---|
| Inbound inquiry | Create Person + Company; set `status = inbound` |
| SDR queue | List: `People where status = inbound AND owner = null` |
| Qualified | Update `status = qualified`; create Deal |
| Disqualified | `status = disqualified` + reason (do not delete) |

### Attio vs Salesforce mental model

- **Linking:** Person ↔ multiple Companies (advisors, agencies) without hacks
- **No conversion ceremony** — state machine on attributes
- **Lists = queues** — dynamic membership drives workflows

### Attio vs HubSpot

- HubSpot lifecycle is global enum; Attio uses custom selects + lists
- Attio better for API-first enrichment; HubSpot better for marketing automation

## Cross-Platform Decision Table

| Situation | Salesforce | HubSpot | Attio |
|---|---|---|---|
| Enterprise territories | ✓ Leads + Accounts | Upgrade Enterprise | Custom attributes |
| PLG signups | Contact + Account API | Contact + Company | Person + Company |
| High inbound junk | Lead object | Lifecycle + scoring | Lists + status field |
| SDR → AE handoff | Lead convert + Opp | Lifecycle SQL → Deal | List + Deal create |
| Marketing automation | Pardot/MC (complex) | Native Marketing Hub | Webhooks + external |
| Founder-led <$2M ARR | Overkill | ✓ Starter/Pro | ✓ |

## Implementation Rules (All Platforms)

1. **One person = one email** — dedupe key is email (or domain + name for companies)
2. **Source of truth:** Pick either Contact or Lead stage for "who owns qualification" — not both
3. **Required on qualified:** Company, title, ICP tier, next step
4. **Enrich on create** — before assignment (`leadmagic-toolkit`, `clay-toolkit`)
5. **Never sync junk both ways** — one-direction enrichment → CRM

## Migration Notes

| From → To | Watch out |
|---|---|
| Salesforce → HubSpot | Map Lead stages to lifecycle; merge duplicate Contacts |
| HubSpot → Salesforce | Decide Lead vs direct Contact; historic Deals need Accounts |
| HubSpot → Attio | Flatten lifecycle to `status`; rebuild lists as dynamic |
| Salesforce → Attio | Drop Lead object; use `status` + lists for SDR queue |

Load platform blueprint: `hubspot-blueprint.md`, `salesforce-blueprint.md`, `attio-blueprint.md`.

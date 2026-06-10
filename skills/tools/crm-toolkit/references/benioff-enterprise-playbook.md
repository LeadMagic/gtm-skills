# Marc Benioff — Enterprise GTM Playbook

*Source: Marc Benioff, co-founder & CEO Salesforce — public teachings and
[Behind the Cloud](https://www.salesforce.com/company/history/) (2009). Apply
principles at your stage; do not copy Salesforce-scale assumptions at $1M ARR.*

---

## Core ideas that matter for GTM

| Principle | What it means | CRM / RevOps implication |
|---|---|---|
| **End of Software** | Subscription over shelfware; value must be continuous | Track usage, health, renewal — not just closed-won |
| **Trust** | Radical transparency with customers builds enterprise deals | Document commitments in CRM; no sandbagged forecasts internally |
| **Customer Success** | Post-sale outcomes drive renewals and expansion | CS owns health + adoption fields; sales hands off with success plan |
| **Land and expand** | Small footprint → prove ROI → grow seats/SKUs | Parent Account + child opps; expansion pipeline separate from new logo |
| **Values as OS** | Culture scales when written and measured | V2MOM cascades to team quotas and pipeline measures |

---

## V2MOM (annual alignment)

Benioff's planning system — entire company writes one **V2MOM** per year.
Revenue leaders should cascade a **GTM V2MOM** from company vision.

| Letter | Definition | GTM example |
|---|---|---|
| **V — Vision** | Where we are going (1–2 sentences) | "Become default CRM for mid-market fintech in NA" |
| **V — Values** | Non-negotiable behaviors | "Customer trust over short-term bookings" |
| **M — Methods** | How we get there (prioritized list) | "Outbound POD + partner channel + CS-led expansion" |
| **O — Obstacles** | What blocks us (honest) | "No RevOps owner; 40% opps missing EB" |
| **M — Measures** | Numbers that prove progress | "NRR 115%; SQO→Opp 25%; forecast accuracy ±10%" |

Template: **gtm-leadership** → `skills/management-leadership/gtm-leadership/templates/v2mom-gtm.md`  
Deep guide: **gtm-leadership** → `skills/management-leadership/gtm-leadership/references/benioff-v2mom-guide.md`

---

## Trust-based enterprise selling

Benioff positioned Salesforce against opaque enterprise vendors with **trust**
as the brand — mirrored in product (audit trails, sharing model) and sales motion.

### Practices that transfer

1. **Say what you won't do** — scope limits in writing reduce late-stage churn
2. **Reference customers by outcome** — not logo slides without permission
3. **Executive accessibility** — founder/CEO on strategic deals (stage-appropriate)
4. **Status page mindset** — when something breaks, communicate first (`transparency-selling`)
5. **No "bait and switch" packaging** — commercial terms match demo scope

### CRM fields to support trust

| Field | Purpose |
|---|---|
| `Success_Criteria__c` | Mutual success plan on Opportunity |
| `Executive_Sponsor__c` | Your exec + customer exec mapped |
| `Commitment_Log__c` | Promises made (roadmap, SLA, timeline) |
| `Risk_Flags__c` | Open issues customer knows about |

---

## Customer Success in the CRM (Benioff lineage)

Salesforce popularized **Customer Success** as a revenue function — not support
with a rebrand. In CRM architecture:

| Object / process | Owner | KPI |
|---|---|---|
| Onboarding checklist | CS | Time-to-first-value |
| Health score | CS | Composite: usage + support + sentiment |
| Renewal Opportunity | CS/AM | Auto-create 120d before end |
| Expansion Opportunity | CS/AM | Separate from new-logo pipeline |

Link to **Bowtie** (`pipeline-management`) — CRM must model post-sale, not funnel-only.

Skills: `cs-playbooks`, `customer-onboarding`, `churn-prevention`

---

## Land and expand

Benioff's enterprise motion: **land** with a department or use case, **expand**
across divisions and product lines after proof.

### Land phase

- Single use case, single champion, bounded pilot or starter SKU
- Success criteria defined **before** contract signature
- 90-day value milestone in mutual success plan

### Expand phase

- Executive business review with ROI narrative
- Whitespace map: departments, geographies, product modules
- Expansion opp **linked to parent Account** — never orphan pipeline

Template: `templates/land-expand-account-plan.md`

Skills: `expansion-selling`, `deal-desk` (discount authority on land deals)

### Salesforce CRM pattern

```
Account (Parent)
├── Opportunity: Land — Closed Won
├── Opportunity: Expand — Dept B (open)
├── Opportunity: Renew — FY26 (scheduled)
└── Customer_Success_Plan__c — health + QBR dates
```

---

## Ecosystem & partner GTM

From Benioff: **no company is an island** — AppExchange and SI partners extended
Salesforce's GTM without headcount linearity.

| Motion | When to use |
|---|---|
| **SI / implementation partner** | Enterprise CRM rollout (`implementation-partners.md`) |
| **ISV integrations** | Buyer requires ecosystem proof in RFP |
| **Co-sell** | Partner brings account; you bring product |

Track in CRM: `Partner__c` on Opportunity, `Influence_Type__c` (sourced vs influenced).

---

## Culture signals that affect revenue

Public Benioff themes relevant to GTM leaders:

- **Ohana** — long-term stakeholder view (customers, employees, community)
- **1-1-1 philanthropy** — 1% equity, product, time (culture recruiting signal)
- **No tolerance for ethics breaches** — enterprise buyers research vendor culture

Do not use culture language to avoid quota accountability — values **and** measures.

---

## Anti-patterns (do not copy blindly)

| Salesforce at scale | Your stage |
|---|---|
| 70,000 employees | 15-person team — V2MOM fits on one page |
| Dreamforce $100M+ event | Customer dinner series + webinar |
| Custom everything in SF | HubSpot/Attio until $5M+ ARR often fits |
| Long enterprise cycles only | SMB velocity may be correct ICP |

---

## Skill routing

| Task | Load |
|---|---|
| Annual GTM planning | `gtm-leadership` + V2MOM template |
| Salesforce architecture | `salesforce-blueprint.md` + `salesforce-setup` |
| Expansion motion | `expansion-selling` + land-expand template |
| Trust / transparency in deals | `transparency-selling` |
| CS operating model | `cs-playbooks` |

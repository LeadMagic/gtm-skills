# Visitor ID Vendor Comparison

*GTM use patterns — not vendor sales collateral. Verify pricing and features at renewal.*

**Spend governance:** `gtm-spend-management` → `GTM-Data` class · **Stack fit:** `revops-tech-stack`

---

## Comparison table

| Vendor | ID level | Best GTM use case | CRM / integrations | Slack alerts | Accuracy caveats | Typical spend tier |
|---|---|---|---|---|---|---|
| **Clearbit / HubSpot Breeze Intelligence** | Company (+ person via form enrichment) | HubSpot-native Reveal on site visit; form enrichment waterfall | HubSpot native; Salesforce via HubSpot | Via HubSpot workflows / Zapier | IP→company 60–80%; weak on remote/VPN | $$–$$$ (bundled with HubSpot) |
| **RB2B** | Person | LinkedIn-profile visitor ID → SDR outbound trigger | HubSpot, Salesforce, Slack, Clay | Native Slack | Person match varies; verify title + company | $$ per identified visitor |
| **6sense** | Company (account intent) | Enterprise ABM intent + stage scoring | Salesforce, HubSpot, MAP, SEP | Via orchestration | Account-level; not a person reveal tool | $$$$ platform |
| **Demandbase** | Company | ABM advertising + account ID + intent | Salesforce deep | Via Demandbase | Strong enterprise; heavy implementation | $$$$ platform |
| **ZoomInfo WebSights** | Company | ZoomInfo customers — feed WebSights into existing data | ZoomInfo + CRM sync | Limited native | Best inside ZoomInfo ecosystem | $$$ (add-on) |
| **Leadfeeder / Dealfront** | Company | SMB/mid-market website company ID | CRM connectors, Pipedrive strong | Email/Slack via Zapier | Good EU coverage; SMB focus | $–$$ |
| **Warmly** | Person + company | Real-time chat + person ID on site | HubSpot, Salesforce, SEP | Native | Person ID + engagement; watch privacy | $$–$$$ |
| **Koala** | Person + company | PLG + sales-assist; Slack-first alerts | HubSpot, Salesforce | Native Slack | Strong for product-led sites | $$ |
| **Factors.ai** | Company + journey | Product analytics + firm ID + journey | Segment, CRM | Slack integrations | Analytics-first; ID secondary | $$ |
| **Albacross** | Company | EU-centric company deanonymization | CRM via connectors | Email alerts | EU vendor; company-only | $–$$ |

---

## Per-vendor GTM notes

### Clearbit / HubSpot Breeze Intelligence

- **Reveal:** JavaScript tag → company identified on visit → HubSpot company record
- **Enrichment:** Real-time firmographics on form submit (email → person + company)
- **Best for:** HubSpot-centric stacks, inbound MQL enrichment, company-level ABM
- **Limitations:** Reveal is not person-level; coverage thins outside US tech/SaaS
- **Integrations:** HubSpot Workflows, Salesforce (via HubSpot), webhooks to Clay/n8n
- **Spend:** `gtm-spend-management` — often bundled; track as `GTM-Data` if standalone

### RB2B

- **Core:** Person-level LinkedIn identity from website visit
- **Best for:** US B2B with tight ICP + SDR team that researches before send
- **Limitations:** Privacy sensitivity; false person match; requires enrichment verification
- **Integrations:** HubSpot, Salesforce, Slack, outbound tools via webhook/Clay
- **Workflow:** Alert → ICP gate → `cold-email-strategy` trigger branch (≤2 touches)

### 6sense

- **Core:** Account identification + intent data + predictive stages
- **Best for:** Enterprise ABM with Salesforce, multi-channel orchestration
- **Limitations:** Implementation heavy; not a lightweight SMB plugin
- **Integrations:** Ads, MAP, SEP, CRM — designed as orchestration hub

### Demandbase

- **Core:** Account ID + advertising + intent for ABM
- **Best for:** Marketing-led ABM with ad spend on target accounts
- **Limitations:** Cost and complexity; person ID not primary value prop

### ZoomInfo WebSights

- **Core:** Company visit ID feeding ZoomInfo account intelligence
- **Best for:** Teams already on ZoomInfo for prospecting data
- **Limitations:** Value tied to ZoomInfo contract; redundant if 6sense/Demandbase present

### Leadfeeder / Dealfront

- **Core:** Company name from visit + page analytics
- **Best for:** SMB sales teams, EU companies, straightforward CRM sync
- **Limitations:** Company-only; limited intent scoring vs enterprise platforms

### Warmly

- **Core:** Person + company ID with on-site chat and routing
- **Best for:** Sales-assist on website, real-time conversation
- **Limitations:** Person ID privacy review required; can overlap with Drift/Intercom

### Koala

- **Core:** Slack alerts for ICP visitors with person + company context
- **Best for:** PLG companies with product signals + sales-assist motion
- **Limitations:** Smaller vendor — validate DPA and data retention

### Factors.ai

- **Core:** Journey analytics with company identification layer
- **Best for:** Marketing ops wanting funnel analytics + firm ID in one tool
- **Limitations:** ID is feature, not pure best-of-breed reveal

### Albacross

- **Core:** EU-focused company deanonymization
- **Best for:** EU-primary sites needing company ID with EU vendor option
- **Limitations:** Company-only; less common in US-centric stacks

---

## Selection guide by stack maturity

| If you have… | Start with | Avoid duplicating |
|---|---|---|
| HubSpot CRM | Breeze Intelligence / Clearbit Reveal | Second company ID pixel without sunset plan |
| Salesforce + ABM budget | 6sense OR Demandbase (one) | ZoomInfo WebSights + 6sense same motion |
| SMB + tight budget | Leadfeeder/Dealfront or Albacross (EU) | Enterprise ABM suite |
| SDR outbound trigger motion | RB2B OR Warmly (one person vendor) | RB2B + Warmly + Koala all firing |
| PLG + sales assist | Koala or Warmly | Person ID without product usage signals |

**Consolidation rule (`revops-tech-stack`):** One company ID owner + at most one person ID vendor until utilization proves ROI.

---

## Evaluation scorecard

Use `templates/visitor-id-vendor-eval-scorecard.md` for structured pilots.

**Pilot metrics (30 days):**
- Identified visits / total visits
- ICP-qualified rate
- Alert → meeting conversion
- False positive sample (manual review n=50)
- Opt-out / complaint count

---

## Cross-links

- Decision matrix: `person-vs-business-identification.md`
- Privacy checklist: `visitor-id-privacy-gtm.md`
- Master playbook: `visitor-identification-playbook.md`
- TCO: `gtm-tool-cost-model`
- Vendor roster: `gtm-spend-management/templates/vendor-spend-register.md`

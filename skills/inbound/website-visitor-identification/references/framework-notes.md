# Framework Notes — Website Visitor Identification

## Named frameworks

| Framework | Source | Application |
|---|---|---|
| **Company vs Person ID decision tree** | GTM Skills — `person-vs-business-identification.md` | Choose identification level before vendor purchase |
| **Confidence tier routing** | GTM Skills — `visitor-identification-playbook.md` | High/Medium/Low gates for CRM + sequences |
| **Privacy go/no-go checklist** | GTM Skills — `visitor-id-privacy-gtm.md` | Operational GDPR/CCPA gates (not legal advice) |
| **SiriusDecisions Demand Waterfall** | Forrester / SiriusDecisions | Visitor intent feeds MQL definitions — pair with `inbound-triage` |
| **Winning by Design Bowtie** | Jacco van der Kooij | Visitor ID instruments **acquisition** stage |
| **Chris Walker — measurable vs dark social** | Refine Labs | Visitor ID = measurable counterpart to unmeasurable influence |
| **HubSpot Breeze Intelligence** | HubSpot (Clearbit heritage) | Reveal + enrichment in HubSpot-native stacks |
| **Scott Brinker — consolidation** | chiefmartec.com | One company ID + one person ID max until ROI proven |

## Citation anchors

- **Clearbit → HubSpot Breeze:** HubSpot acquired Clearbit; Reveal and enrichment live under Breeze Intelligence branding.
- **RB2B:** Person-level LinkedIn visitor identification — US B2B outbound trigger use case.
- **6sense / Demandbase:** Enterprise account-level intent — not lightweight person reveal.
- **EU deployment:** Consent-first per `1p-tagging-pixels`; person ID requires counsel per `visitor-id-privacy-gtm.md`.

## Operating assumptions

1. Company ID is default; person ID is opt-in with privacy review.
2. ICP filter runs before any CRM write or sequence enrollment.
3. Visitor ID vendors are `GTM-Data` spend (`gtm-spend-management`).
4. False positives are expected — operate with confidence tiers, not binary trust.
5. Opt-out suppression is non-negotiable across CRM, sequencer, and alerts.

## Cross-skill map

| Need | Skill |
|---|---|
| Vendor selection | `revops-tech-stack` |
| Spend / renewal | `gtm-spend-management` |
| Consent + pixels | `1p-tagging-pixels` |
| MQL routing | `inbound-triage` |
| Outbound trigger | `cold-email-strategy` |
| ICP definition | `icp-scoring` |
| Data security | `references/gtm-data-exchange-playbook.md` |
| UTM source | `campaign-governance` |

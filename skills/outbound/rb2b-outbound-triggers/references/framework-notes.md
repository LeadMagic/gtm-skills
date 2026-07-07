# RB2B Outbound Triggers — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations.

## Primary Frameworks

- **Adam Robinson (RB2B) — Person-level visitor identification**: RB2B matches website visitors to LinkedIn profiles, providing name, title, company, and LinkedIn URL. Founded by Adam Robinson (also founded Retention.com). Bootstrapped with LinkedIn as primary distribution. Core thesis: person-level ID is more actionable than company-level because you can reach out to the actual human, not just the account.
- **Signal-Based Selling**: Behavioral signals (page visits, session duration, repeat visits) indicate buying intent. Visitors on pricing/docs/demo pages are further along. The signal decays — 50% intent decay within 48 hours.
- **Justin Michael — Tech-Powered Sales / Technology Quotient (TQ)**: Stack-aware outbound. RB2B is one node in the stack: RB2B (signal) → Clay (enrichment + routing) → Sequencer (outreach) → CRM (tracking). TQ = how well you orchestrate the stack.
- **Jordan Crawford — PQS / PVP / FIND (Cannonball GTM)**: Precision targeting. Person-level data enables PVP (Persona-Value-Proof) at individual level. FIND = the framework for identifying who to reach out to.
- **Pat Spielmann — Cold to Gold**: Trigger-based sequencing. The visit IS the trigger — design the sequence around that specific trigger event, not a generic cadence.
- **Henry Schuck (ZoomInfo) — Data-lake outbound motion**: Capture every signal in a data lake. RB2B is a signal source; the data lake routes, scores, and acts.
- **Becc Holland — Stellar Cold Email / Diagnostic Selling**: Reference the visit diagnostically. "Noticed you were exploring [topic]" not "I saw you on our pricing page for 3 minutes."
- **Winning by Design — SPICED**: Use page-visit patterns to infer the visitor's SPICED stage (Situation, Pain, Impact, Critical event, Decision). Pricing page = Decision stage. Blog post = Situation/Pain stage.

## RB2B Operational Notes

### What RB2B gives you

- Visitor name (first + last)
- Job title
- Company name
- LinkedIn profile URL
- Pages visited (path)
- Session duration
- Timestamp
- Repeat visit flag

### What RB2B does NOT give you

- Email address (must be found via enrichment)
- Phone number (must be found via enrichment)
- Company firmographics (must be enriched via Clay/Apollo/Clearbit)
- Intent score (must be computed from page-visit patterns)
- CRM record (must be created or matched)

### RB2B integration points

- **Slack**: Native Slack alert on identification
- **Webhook**: Real-time webhook for Clay/Make/n8n automation
- **HubSpot**: Native integration — creates contact records
- **Salesforce**: Via Clay or Zapier
- **Clay**: RB2B webhook → Clay table → enrichment waterfall → sequencer push

### Privacy considerations

- RB2B identifies US visitors only (LinkedIn-based matching)
- GDPR: RB2B does not identify EU visitors (no cookie consent issues in EU)
- CCPA: Person-level data falls under CCPA — provide opt-out mechanism
- Always suppress existing customers, partners, and competitors from outbound
- Never reference exact page-level behavior in outreach (surveillance-like)

### Conversion benchmarks

- RB2B identifies ~3-8% of US website traffic (varies by site)
- Of identified visitors, ~30-50% are ICP fit (Tier 1 + Tier 2)
- Of Tier 1 contacted, 5-10% book meetings
- Of Tier 2 contacted, 2-5% book meetings
- SDR response within 15 min → 4x higher meeting rate vs 24-hour response

## Deep-dive references

| File                                               | Authority | Use when                                     |
| -------------------------------------------------- | --------- | -------------------------------------------- |
| `visitor-id-vendor-comparison.md` (repo root)      | LeadMagic | Comparing RB2B vs Clearbit, 6sense, Warmly   |
| `visitor-identification-playbook.md` (repo root)   | LeadMagic | Building the full visitor ID program         |
| `visitor-id-privacy-gtm.md` (repo root)            | LeadMagic | Privacy guardrails for person-level data     |
| `person-vs-business-identification.md` (repo root) | LeadMagic | When to use person-level vs company-level ID |

---
name: data-privacy-compliance
description: >-
  Data privacy compliance for B2B SaaS — GDPR, CCPA/CPRA, ePrivacy Directive,
  cookie consent, Data Processing Agreements (DPAs), Standard Contractual
  Clauses (SCCs), Data Protection Impact Assessments (DPIAs), subject access
  requests (SARs), and privacy-by-design. Covers step-by-step compliance
  roadmap, privacy tech stack, and when to hire a DPO. Use when implementing
  GDPR compliance, preparing for enterprise security reviews, or building
  a privacy program. Triggers on: "GDPR compliance", "CCPA", "data privacy",
  "DPA", "cookie consent", "privacy policy GDPR", "SCCs", "data protection".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: founder-led
  tags: [gdpr, ccpa, data-privacy, dpa, cookie-consent, sccs, compliance, privacy]
  related_skills: [soc2-compliance, legal-for-founders, security-assessments, vendor-contracts, business-insurance]
  frameworks:
    - "GDPR (EU General Data Protection Regulation 2016/679)"
    - "CCPA/CPRA (California Consumer Privacy Act / California Privacy Rights Act)"
    - "ePrivacy Directive (EU Cookie Law)"
    - "IAPP (International Association of Privacy Professionals)"
    - "NIST Privacy Framework"
    - "Termly / Iubenda — Privacy compliance tools"
---

# Data Privacy Compliance

## Overview

Privacy compliance went from "nice to have" to "existential requirement." GDPR
fines reach 4% of global annual revenue or €20M (whichever is higher). CCPA
allows private lawsuits. Enterprise customers won't sign without a DPA and
SCCs. The mistake: treating privacy as a legal checkbox instead of an
operational program. This skill covers the complete privacy compliance roadmap
for B2B SaaS: GDPR, CCPA, cookie consent, DPAs, SCCs, and building a privacy
program that passes enterprise security reviews.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **GDPR (EU General Data Protection Regulation 2016/679).** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **CCPA/CPRA (California Consumer Privacy Act / California Privacy Rights Act).** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **ePrivacy Directive (EU Cookie Law).** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **IAPP (International Association of Privacy Professionals).** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **NIST Privacy Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Termly / Iubenda — Privacy compliance tools.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use

Trigger phrases: "GDPR compliance", "CCPA requirements", "data privacy for
SaaS", "cookie consent banner", "Data Processing Agreement", "Standard
Contractual Clauses", "SCCs", "privacy by design", "data subject access
request", "DPIA", "privacy program", "enterprise privacy requirements"

## Step-by-Step Process

### Phase 1: Privacy Law Scoping

**Which laws apply to you?**

| Law | Applies If | Key Requirements | Penalty |
|---|---|---|---|
| **GDPR** | You process data of ANY person in the EU/UK (regardless of where your company is) | Lawful basis, consent/legitimate interest, DPA, data subject rights, breach notification (72 hrs), DPO (in some cases) | Up to 4% of global annual revenue or €20M |
| **CCPA/CPRA** | $25M+ revenue OR 100K+ California consumers OR 50%+ revenue from selling data | Right to know/delete/opt-out, privacy notice, data inventory | $2,500 per violation ($7,500 intentional) + private right of action |
| **ePrivacy** | You use cookies or tracking in the EU | Cookie consent before non-essential cookies, clear disclosure | Up to 4% of global revenue |
| **PIPEDA (Canada)** | Processing Canadian personal data | Consent, purpose limitation, safeguards | Up to CAD $100K per violation |
| **LGPD (Brazil)** | Processing Brazilian personal data | Similar to GDPR — consent, rights, breach notification | Up to 2% of Brazilian revenue (capped at R$50M) |
| **State laws (US)** | Virginia, Colorado, Connecticut, Utah, etc. | Similar to CCPA — varies by state | Varies |

**Rule of thumb for B2B SaaS:** If you have ANY customers in the EU, GDPR
applies. If you have ANY users in California and meet thresholds, CCPA applies.
If you have a website, ePrivacy applies to EU visitors. If you don't know your
users' locations — assume all three apply.

### Phase 2: GDPR Compliance Roadmap

**Step 1: Data Inventory / Data Mapping**
- Document: what data you collect, where it's stored, who has access, where
  it's processed, how long you keep it, and your legal basis for processing
- Tools: spreadsheets work for early stage. OneTrust, DataGrail, or Securiti
  for scale

**Step 2: Determine Your Role**
- **Data Controller:** You decide what data to collect and why. Most SaaS
  companies are controllers of their customer data.
- **Data Processor:** You process data on behalf of someone else. AWS is
  your processor. You are the controller.
- **Sub-Processor:** Your vendors who process data (AWS, Stripe, Intercom,
  HubSpot, etc.)

**Step 3: Establish Lawful Basis for Processing**
- **Consent:** User explicitly agrees (checkbox, not pre-ticked)
- **Contractual necessity:** Processing required to fulfill a contract
- **Legitimate interest:** You have a valid business reason that doesn't
  override user rights (requires Legitimate Interest Assessment)
- **Legal obligation:** Required by law
- **Vital interests:** Protecting life (rare for SaaS)

**Step 4: Privacy Policy**
- Must be: concise, transparent, in plain language, easily accessible
- Must include: what data, why, how long, who it's shared with, user rights,
  international transfers, DPO contact if applicable
- See: `legal-for-founders` skill for Privacy Policy template

**Step 5: Data Processing Agreement (DPA)**
- Required between Controller and Processor
- Must include: subject matter, duration, nature, purpose, types of data,
  categories of data subjects, processor obligations
- Your sub-processors (AWS, etc.) provide DPAs to you
- You provide a DPA to your enterprise customers
- **Have a DPA template ready before enterprise customers ask for it**

**Step 6: Standard Contractual Clauses (SCCs)**
- Required for transferring personal data from EU to "third countries"
  (including the US) without an adequacy decision
- New SCCs (June 2021): modular format, must complete a Transfer Impact
  Assessment (TIA)
- Most US SaaS companies need SCCs for EU customer data

**Step 7: Data Subject Rights (DSARs)**
- Right to access, rectify, erase, restrict processing, data portability,
  object to processing
- Must respond within 30 days (extendable to 90)
- Must verify identity before fulfilling
- Build a process: how will you find, extract, and delete a user's data?

**Step 8: Breach Notification**
- Notify supervisory authority within 72 hours of becoming aware
- Notify affected data subjects "without undue delay" if high risk
- Have an incident response plan with breach notification procedures

**Step 9: Data Protection Officer (DPO)**
- Required if: public authority, large-scale systematic monitoring, or
  large-scale processing of sensitive data
- Most early-stage B2B SaaS does NOT need a DPO
- Can outsource DPO-as-a-Service if needed

### Phase 3: Cookie Consent

**Required for EU visitors (ePrivacy Directive + GDPR):**

1. **Cookie banner:** Appears on first visit. Must include:
   - What cookies you use and why
   - Option to accept all, reject all, or customize
   - "Accept All" and "Reject All" must be equally prominent
   - NO pre-ticked boxes (illegal under GDPR)
   - NO "by continuing to browse, you accept" (illegal)

2. **Cookie categories:** Necessary, Preferences, Statistics, Marketing
   - Necessary: can't be disabled (session, auth, CSRF)
   - All others: must be opt-in

3. **Cookie consent tools:**
   - CookieYes (free-$10/mo)
   - Cookiebot ($12/mo+)
   - Termly ($10/mo+)
   - OneTrust (free basic, enterprise pricing)

### Phase 4: CCPA/CPRA Compliance

**If you meet CCPA thresholds ($25M+ revenue OR 100K+ CA consumers OR 50%+ revenue from data sales):**

1. Privacy notice at collection
2. "Do Not Sell or Share My Personal Information" link on homepage
3. "Limit the Use of My Sensitive Personal Information" link
4. Respond to requests: know, delete, correct, opt-out within 45 days
5. Data retention schedule
6. Contracts with service providers (similar to DPAs)
7. Risk assessments for processing (CPRA addition)

### Phase 5: Privacy Tech Stack

| Tool | What It Does | Cost |
|---|---|---|
| **Termly** | Privacy Policy, ToS, Cookie Consent | $10-20/mo |
| **Iubenda** | Privacy Policy, Cookie Consent, ToS (multi-language) | $9-29/mo |
| **CookieYes** | Cookie consent banner, scanning | Free-$10/mo |
| **OneTrust** | Full privacy management (enterprise) | Custom |
| **DataGrail** | DSAR automation, data mapping | Custom |
| **Securiti** | Privacy ops, data mapping, DSAR | Custom |

## Output Format

```
DATA PRIVACY PROGRAM — [Company]

Applicable Laws: [GDPR, CCPA, ePrivacy, etc.]

DATA MAP: [link to data inventory]

LAWFUL BASES: [per data category, per purpose]

KEY DOCUMENTS (status):
- [ ] Privacy Policy — [published / draft / needs review]
- [ ] Cookie Consent Banner — [implemented / needed]
- [ ] DPA (outbound to customers) — [template ready / needed]
- [ ] DPAs (inbound from vendors) — [collected from: list]
- [ ] SCCs — [in place / not needed / needed for: list]
- [ ] DSAR procedure — [documented / needed]
- [ ] Breach notification procedure — [documented / needed]

PRIVACY TOOLS:
- Cookie consent: [tool]
- Privacy policy: [tool]
- DSAR management: [tool]

ANNUAL REVIEW: [date / trigger]
```

## Implementation Checklist

- [ ] Data map completed (know what data you have and where)
- [ ] Privacy policy published — accurate, not copy-pasted
- [ ] Cookie consent banner live (if EU visitors)
- [ ] DPA template ready for enterprise customers
- [ ] SCCs in place for EU→US data transfers (if applicable)
- [ ] DSAR procedure documented (how to handle access/deletion requests)
- [ ] Breach notification procedure documented (72-hour clock)
- [ ] Sub-processor list maintained (DPA from each vendor)
- [ ] Annual privacy review scheduled

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Copy-pasted privacy policy.** "We don't use cookies" while using Google
   Analytics, Stripe, and Intercom = false statement, GDPR violation. Fix:
   Document what you actually do. Update when your stack changes.

2. **No DPA ready for enterprise.** Enterprise customer asks for DPA. You
   don't have one. Deal stalls for weeks while you scramble. Fix: Have a
   DPA template ready. Termly can generate one.

3. **Pre-ticked cookie consent.** "Accept All" is pre-selected. This is
   illegal under GDPR. CNIL (France) fined Google €150M for this. Fix:
   "Accept All" and "Reject All" must be equally prominent. Nothing pre-ticked.

4. **No breach notification plan.** Breach happens Friday at 9pm. No one knows
   what to do. 72-hour clock is ticking. Monday morning: GDPR violation +
   breach exposure. Fix: Incident response plan with notification triggers
   and templates.

5. **Ignoring CCPA until $25M.** CCPA has a private right of action for data
   breaches. You don't need to hit the threshold to get sued for a breach.
   Fix: Implement reasonable security measures regardless of revenue.

6. **Forgetting about vendor sub-processors.** You sign a DPA with a customer
   promising GDPR compliance — but you never collected DPAs from your own
   vendors (AWS, Intercom, etc.). Fix: Collect and maintain DPAs from all
   sub-processors. Share the list with enterprise customers.



## ⚠️ Disclaimer

This skill provides general informational guidance based on publicly available frameworks and operator experience. It is NOT legal advice, accounting advice, tax advice, financial advice, insurance advice, or professional services advice.

Consult qualified professionals for your specific situation — attorneys for legal/equity matters, CPAs for tax and accounting, licensed brokers for insurance, and certified security assessors for compliance. This skill does not create a professional-client relationship. Use it as a starting point for research and preparation.

## Related Skills

- `legal-for-founders` — Incorporation, ToS, Privacy Policy, IP
- `soc2-compliance` — Security compliance that supports privacy
- `security-assessments` — Vendor security reviews, pen testing
- `vendor-contracts` — DPAs, vendor security agreements
- `business-insurance` — Cyber insurance (privacy breaches)

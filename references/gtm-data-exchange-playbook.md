# GTM Data Exchange Playbook

*For AEs, CSMs, founders, and RevOps — not security engineering.*

When sales or CS needs customer data (onboarding, enrichment, integrations, POCs), use this playbook. Implementation details (encryption, IAM, pen tests) → `security-assessments`, `soc2-compliance`.

---

## When GTM needs customer data

| Moment | Typical ask | Owner |
|---|---|---|
| **POC / trial** | Sample records to prove value | AE + solutions |
| **Onboarding** | Users, CRM export, integration credentials | CSM + implementation |
| **Custom integration** | API keys, field mappings, webhook URLs | CS + customer IT |
| **Renewal / expansion** | Usage reports, new department roster | CSM |
| **Support incident** | Logs, screenshots, repro steps | Support |

**Rule:** Need the *minimum* data to hit the next milestone — not "send us everything."

---

## Safe exchange methods (ranked)

| Method | Use when | Avoid when |
|---|---|---|
| **Customer-owned upload** (their SFTP, SharePoint, Google Drive *they* control) | Large files, recurring imports | You can't document who accessed what |
| **Vendor secure file share** (Box, Dropbox Business, OneDrive with link expiry + password) | One-time handoffs under NDA | Link never expires, no access log |
| **Customer portal / trust center upload** | Enterprise with formal vendor intake | SMB where portal is overkill |
| **In-product import** (CSV upload inside your app) | Onboarding self-serve | File contains fields you don't need |
| **Encrypted zip + separate channel for password** | Legacy customers only | Default choice — too easy to mess up |

### Never use for customer data

- Email attachments (including "just this once")
- Slack file uploads with PII (searchable, retained, easy to forward)
- Personal Google Drive / Dropbox on rep laptops
- Shared team inboxes without MFA and access logging
- WhatsApp, iMessage, or SMS with customer lists

---

## What to ask vs what to never request

### Usually OK to request (with purpose stated)

- Business email, name, title, company domain
- Non-production sandbox credentials
- Aggregated or anonymized exports for POC
- Field list / schema *without* row data
- Synthetic or masked sample (10–50 rows)

### Ask legal / security before requesting

- Full production CRM export
- Employee SSN, government ID, payroll, health data
- End-customer PII your product doesn't need to operate
- Production admin passwords (use SSO, scoped roles, or time-bound access instead)
- Card numbers or bank details (use billing portal)

### Never request

- Passwords to customer's other systems "to save time"
- Broad "dump your database" without field-level justification
- Data from unrelated business units "while you're at it"
- Customer's *own* customer lists unless contract + DPA explicitly cover it

---

## Go / no-go decision tree

```
Do we need this data to deliver the next committed milestone?
├─ NO → Don't ask. Use synthetic data or a demo workspace.
└─ YES → Can we use synthetic / masked / sandbox data instead?
    ├─ YES → Use synthetic. Document that choice in CRM.
    └─ NO → Is there a signed contract or active POC with scope?
        ├─ NO → Stop. No production customer data pre-contract.
        └─ YES → Is DPA / security review required for this customer segment?
            ├─ YES, not done → Pause data intake. Run security track first.
            └─ NO or complete → Use approved channel (see table above).
                Log: what, why, who, retention date.
```

---

## DPA and security questionnaire timing (enterprise)

| Deal stage | GTM action | Don't do this |
|---|---|---|
| **Discovery** | Share your trust center / high-level security page if asked | Send full SOC 2 report without NDA |
| **Evaluation / POC** | Confirm data classification; prefer synthetic POC data | Request production export before mutual NDA |
| **Commercial negotiation** | Loop in legal on DPA; AE owns timeline with procurement | Promise "we'll sign anything" without review |
| **Security review** | Route to `security-questionnaire-deal-guide.md`; use trust center | AE guesses answers on encryption architecture |
| **Closed-won → onboarding** | Handoff includes *what data was exchanged* and retention | CS re-requests same export via email |

**SOC 2 / ISO as sales obstacle:** Enterprise buyers often use compliance as a *filter*, not a technical deep dive. Your job is to **unblock with the right artifact at the right time** — not to implement controls in the deal cycle. Founder-led implementation → `soc2-compliance`, `security-assessments`.

Sources: [Jason Lemkin — Just Do The SOC-2](https://www.saastr.com/just-do-the-soc-2/) · [Vanta — Trust Center for sales handoff](https://www.vanta.com/resources/building-a-comprehensive-trust-center)

---

## Red flags that kill deals

1. **Asking for too much too early** — full CRM export in discovery
2. **Email attachment with customer list** — triggers their security team against *you*
3. **No retention story** — "we'll keep it on a rep's laptop until go-live"
4. **Shared vendor login** — "use our team@ account for the upload"
5. **POC on production data** when sandbox exists
6. **AE answers security questionnaire** without security/legal review
7. **Missing handoff** — CS re-requests data sales already collected (looks disorganized + doubles exposure)

---

## POC / sandbox data hygiene

| Do | Don't |
|---|---|
| Offer a dedicated sandbox or demo tenant | Use production tenant for "quick test" |
| Provide synthetic dataset matching their schema | Ask them to scrub — you scrub (offer template) |
| Time-box POC access (30–60 days) | Leave POC integrations running post-loss |
| Delete POC data within agreed window | Keep "for reference" on local drives |
| Document what was loaded in CRM opportunity notes | Informal Slack-only record |

---

## Handoff: sales → CS → implementation

**Sales owns until closed-won:**

- What data was requested and why
- NDA / DPA status
- POC data scope and deletion date
- Security review status (complete / in flight / not started)

**CS owns from kickoff:**

- Re-use approved channels — don't re-request via email
- Confirm retention and deletion in kickoff doc
- Escalate new data asks through same go/no-go tree

**Implementation owns:**

- Integration credentials via scoped roles or secrets vault — not Slack
- Field mapping doc without unnecessary columns

Template: `deal-desk` → `templates/customer-data-exchange-checklist.md`  
Onboarding handoff fields: `customer-onboarding` (Sales-to-CS handoff section)

---

## Related skills

| Topic | Skill |
|---|---|
| Enterprise security review timing | `deal-desk` + `references/security-questionnaire-deal-guide.md` |
| Onboarding data import | `customer-onboarding` |
| RevOps data boundaries in stack | `revops-tech-stack`, `gtm-operations` |
| Rep password / 2FA / phishing | `references/gtm-security-hygiene-basics.md` |
| SOC 2 / questionnaires (implementation) | `soc2-compliance`, `security-assessments` |
| Privacy / DPA (legal) | `data-privacy-compliance`, `legal-for-founders` |
| Outbound: don't put customer PII in sequences | `cold-email-strategy` |

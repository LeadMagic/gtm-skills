# Visitor ID Privacy — GTM Operational Checklist

**Disclaimer:** This is operational guidance for marketing, demand gen, and RevOps teams — **not legal advice**. Involve privacy counsel before deploying person-level deanonymization, especially for EU/UK visitors.

---

## What GTM teams need to know

| Law / regime | GTM operational impact |
|---|---|
| **GDPR (EU/UK)** | Tracking individuals usually requires lawful basis (often consent). Company-level IP lookup still needs transparency in privacy policy. |
| **CCPA/CPRA (California)** | Right to opt-out of "sale"/"sharing" of personal information. Many visitor-ID vendors = sharing. Honor opt-out signals. |
| **ePrivacy / cookie rules** | Non-essential scripts (pixels, ID tags) typically need consent in EU before firing. |
| **US state laws** | CO, CT, VA, TX and others expanding — trend is opt-out + disclosure. |

**Person-level ID = higher risk than company-level.** Default to company ID; add person ID only with checklist below.

---

## Privacy policy & disclosure (high level)

Update privacy policy to disclose:

- [ ] Categories of data collected (IP, device IDs, pages viewed)
- [ ] Purpose (analytics, sales outreach, advertising)
- [ ] Third-party vendors (Clearbit, RB2B, etc.) by category
- [ ] Retention period (directional — confirm with counsel)
- [ ] Rights: access, deletion, opt-out (link for US; GDPR rights for EU)
- [ ] Contact for privacy requests

**Cookie/consent banner:** Load visitor ID scripts **after** consent in EU (`1p-tagging-pixels` → Consent Management). Company-only vendors still benefit from consent-first deployment.

---

## EU vs US deployment differences

| Control | US-primary deployment | EU / UK deployment |
|---|---|---|
| Person-level deanonymization | Pilot with checklist + opt-out | **Avoid** without counsel; prefer company ID |
| Script loading | Consent recommended; state laws growing | Consent required before non-essential tags |
| Outbound from visitor ID | CAN-SPAM: opt-out required | GDPR: usually need consent or legitimate interest assessment |
| Data retention | Minimize; document in roster | Shorter retention; DPIA may be required |
| Vendor DPA | Required at enterprise | Mandatory |

---

## Operational go/no-go checklist (GTM)

### Company-level ID

- [ ] Privacy policy mentions website analytics and B2B identification
- [ ] Vendor DPA signed and filed (`vendor-contracts`)
- [ ] Consent banner configured for EU traffic
- [ ] IP data not exported to sequences as "personal email"
- [ ] Opt-out web form routes to CRM suppression list

### Person-level ID (additional gates)

- [ ] Legal/privacy counsel reviewed vendor + use case
- [ ] Lawful basis documented (do not guess — counsel confirms)
- [ ] DPIA or equivalent risk assessment if EU data subjects
- [ ] Vendor subprocessors listed for security questionnaires
- [ ] CRM field: `lawful_basis` + `visitor_id_source` + `opt_out`
- [ ] Sequence limits: no bulk auto-email from visitor match alone
- [ ] SDR playbook: no referencing "I saw you on our website" in creepy tone
- [ ] Quarterly audit: complaints, opt-outs, bounce/complaint rate

---

## When NOT to use person-level deanonymization

- Majority of traffic from EU/UK without robust consent
- Regulated verticals (health, finance, minors) without sector counsel
- Vendor will not sign DPA
- No suppression / opt-out sync to CRM + sequencer
- Sales leadership wants "alert on every visitor"
- Pre-product-market-fit — focus on 1P form fills instead

---

## Security questionnaire / legal review triggers

Escalate to legal + security when:

| Trigger | Why |
|---|---|
| New person-level vendor (RB2B, Warmly, etc.) | Subprocessor + data sharing |
| Enterprise prospect asks about visitor tracking | Customer trust + your own hygiene |
| Storing LinkedIn URLs + emails from visitor ID in CRM | PII inventory |
| Syncing visitor data to ad platforms | "Sharing" under CCPA |
| Cross-border data transfer (US vendor, EU visitors) | Transfer mechanism (SCCs, etc.) |

**Artifacts:**
- `references/security-questionnaire-deal-guide.md`
- `references/gtm-data-exchange-playbook.md`
- `references/gtm-security-hygiene-basics.md`
- `deal-desk/templates/customer-data-exchange-checklist.md`

---

## Opt-out & suppression operations

1. **Web form** → privacy@ or in-app preference center
2. **CRM suppression list** → block alert + sequence enrollment
3. **Sequencer suppression** → sync daily (`crm-integration`)
4. **Visitor ID vendor** → confirm opt-out propagation (vendor-specific)
5. **Audit quarterly** — orphaned contacts created only from visitor ID

---

## Incident response (GTM-level)

If complaint or regulatory inquiry:

1. RevOps pulls: source vendor, CRM record, sequence history
2. Stop automated outreach immediately for affected record
3. Notify privacy counsel — do not delete records before guidance
4. Document in internal log; update checklist if gap found

---

## Cross-links

- Tracking consent: `1p-tagging-pixels`
- Founder privacy skill: `data-privacy-compliance` (deeper regulatory context)
- Spend/vendor DPAs: `gtm-spend-management` + `vendor-contracts`
- Decision matrix: `person-vs-business-identification.md`

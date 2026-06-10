# Customer Data Exchange Checklist

*Pre / on / post-sale — for AE, CSM, deal desk. Full playbook → `references/gtm-data-exchange-playbook.md`*

---

## Pre-sale (before customer sends data)

- [ ] Business justification documented in CRM: *why* we need this data
- [ ] Confirmed synthetic / sandbox / masked option explored first
- [ ] Contract or signed POC scope exists (no production data pre-contract)
- [ ] NDA mutual if exchanging non-public business data
- [ ] Enterprise: security review status noted (not started / in progress / complete)
- [ ] Exchange method chosen (not email): _______________
- [ ] Customer approver named: _______________
- [ ] Retention / deletion date agreed: _______________

**Go / no-go:** If any box above is unchecked for production data → **stop and escalate to deal desk.**

---

## On-sale (POC, pilot, evaluation)

- [ ] Data limited to fields required for POC success criteria
- [ ] Sandbox tenant used where possible
- [ ] Upload via approved channel only (link logged in CRM)
- [ ] No customer data in Slack, personal drive, or sequencing tools
- [ ] AE not answering security questionnaire alone (`security-questionnaire-deal-guide.md`)
- [ ] Trust center link sent if security questions arise

---

## Post-sale (onboarding / implementation)

- [ ] Sales-to-CS handoff lists: data already received, channel used, deletion dates
- [ ] CS does not re-request same export via email
- [ ] Integration credentials via scoped roles / vault — not shared passwords
- [ ] DPA executed before ongoing processing of customer personal data (if applicable)
- [ ] Implementation field map excludes unnecessary columns

---

## Post-POC / lost deal cleanup

- [ ] POC data deleted from vendor systems within agreed window
- [ ] Rep laptops / downloads confirmed clear
- [ ] Integration tokens revoked
- [ ] CRM note: data destroyed on [date]

---

## Escalation

| Situation | Contact |
|---|---|
| Unsure if data ask is OK | Deal desk + `gtm-data-exchange-playbook.md` go/no-go tree |
| Security questionnaire received | Security lead + `security-questionnaire-deal-guide.md` |
| DPA / legal terms | Legal + `data-privacy-compliance` |
| Rep hygiene / phishing incident | IT + `gtm-security-hygiene-basics.md` |

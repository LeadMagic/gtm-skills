# GTM Security Hygiene Basics

*For SDRs, AEs, CSMs, founders — Monday-morning checklist, not IT policy.*

Technical controls (SOC 2, IAM, encryption) → `soc2-compliance`, `revenue-team-onboarding` → `security-access-checklist.md`.

---

## Password manager (required)

Every GTM hire uses a **team password manager** (1Password, Bitwarden, or corporate SSO vault):

- [ ] Unique password for every work app — no recycling
- [ ] Never store passwords in Notes, spreadsheets, or Slack
- [ ] Never share master password with colleagues
- [ ] Use shared vaults for *team* credentials — not DMs

**Manager expectation:** If a rep can't show their password manager on day 1, they shouldn't have CRM access.

---

## Turn on 2FA everywhere (priority order)

| System | Why it matters |
|---|---|
| **Email** (Google/Microsoft) | Reset links for everything else |
| **CRM** (Salesforce, HubSpot) | Customer records + pipeline |
| **Sequencer** (Outreach, Salesloft, Smartlead) | Sending domain reputation + contact data |
| **Slack** | Deal threads, customer names, internal strategy |
| **Calendar / Zoom** | Meeting links hijacking |
| **LinkedIn** (if used for social selling) | Account takeover → fake outreach |

Use an **authenticator app** (Google Authenticator, 1Password, Authy) — not SMS when avoidable.

---

## No shared passwords on team accounts

| Bad pattern | Do instead |
|---|---|
| `team@company.com` password in Slack pin | Named users + SSO |
| One login for whole SDR team on sequencer | Seat per rep + manager admin |
| "Use my login for the demo environment" | Guest/demo role with expiry |
| Shared CRM user for reporting | Service account with audit log (RevOps sets up) |

Shared credentials = no audit trail when something leaks.

---

## Phishing awareness for revenue teams

Common lures targeting GTM:

| Scam | What you see | What to do |
|---|---|---|
| **Fake DocuSign / contract** | "Sign before EOD" from odd domain | Hover link; verify in DocuSign app; ask deal desk |
| **Fake lead list** | CSV "ZoomInfo export" from unknown sender | Don't open; report to IT; use approved enrichment tools |
| **Fake calendar invite** | External invite with "View document" link | Don't click; check organizer email |
| **CEO wire / gift card** | Urgent Slack or email from "founder" | Call person on known number; never buy gift cards |
| **Fake support** | "Your Salesforce session expired" | Go to app directly; never enter password on linked page |

**Rule:** If it creates urgency + asks for credentials, files, or payment — pause and verify out-of-band.

---

## Before sharing your screen on a demo

- [ ] Close unrelated tabs (email, CRM other accounts, Slack DMs)
- [ ] Turn off personal notifications (Messages, calendar pop-ups)
- [ ] Hide bookmark bar if it shows internal tools or customer names
- [ ] Use browser profile or demo workspace — not personal Chrome
- [ ] Check Slack status / Do Not Disturb
- [ ] If showing CRM: filter to prospect account only
- [ ] Remove desktop files / folders with customer exports

Reverse demos (prospect shares screen): same hygiene applies to what *you* say aloud — don't ask them to paste secrets in chat. See `demo-scripts`.

---

## Customer data quick rules

- Don't download customer exports to laptop unless required — use approved cloud paths (`gtm-data-exchange-playbook.md`)
- Don't paste customer PII into ChatGPT or unapproved AI tools
- Don't put **customer** PII in outbound sequences — only prospecting fields you have lawful basis to use (`cold-email-strategy`)
- Report lost laptop or suspicious login to IT **immediately**

---

## New hire gate (links to onboarding)

Before live customer contact:

1. Password manager installed
2. MFA on email + CRM + Slack
3. Security awareness training complete
4. Read `gtm-data-exchange-playbook.md` (15 min)

Full provisioning checklist → `revenue-team-onboarding` → `references/security-access-checklist.md`

---

## Related skills

| Topic | Skill / doc |
|---|---|
| Access provisioning | `revenue-team-onboarding` |
| Customer data exchange | `references/gtm-data-exchange-playbook.md` |
| Demo screen share | `demo-scripts` |
| Enterprise security review | `deal-desk`, `security-questionnaire-deal-guide.md` |

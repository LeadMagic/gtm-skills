---
name: security-assessments
description: >-
  Security assessment and vendor risk management for B2B SaaS — penetration
  testing, vulnerability scanning, bug bounty programs, security questionnaires
  (VSAQ/SIG/CAIQ), incident response planning, disaster recovery, and passing
  enterprise security reviews. Use when responding to vendor security
  assessments, preparing for enterprise procurement, or building a security
  program. Triggers on: "security assessment", "penetration test", "bug bounty",
  "security questionnaire", "VSAQ", "incident response", "vendor review".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: founder-led
  tags: [security, pen-testing, bug-bounty, incident-response, security-questionnaire, vsaq, compliance]
  related_skills: [soc2-compliance, data-privacy-compliance, legal-for-founders, vendor-contracts, business-insurance]
  frameworks:
    - "OWASP Top 10 — Web application security risks"
    - "NIST Cybersecurity Framework"
    - "VSAQ (Vendor Security Assessment Questionnaire) — Google"
    - "SIG (Standardized Information Gathering) — Shared Assessments"
    - "CAIQ (Consensus Assessments Initiative Questionnaire) — CSA"
    - "ISO 27001 — Information Security Management"
---

# Security Assessments

## Overview

Every enterprise customer will ask: "Are you secure? Prove it." Your answer
cannot be "trust us." It must be: penetration test reports, security
questionnaires, incident response plans, and compliance certifications.
The mistake: waiting for the first enterprise deal to start thinking about
security. By then, it's too late — the security review takes 4-8 weeks
and the deal stalls. This skill covers the complete security assessment
playbook: penetration testing, vulnerability management, bug bounties,
security questionnaires, and incident response.

## Frameworks Referenced

This skill is grounded in named GTM frameworks, public methodologies, and vendor documentation where relevant:

- **OWASP Top 10 — Web application security risks** — used as the named operating framework for this playbook.
- **NIST Cybersecurity Framework** — used as the named operating framework for this playbook.
- **VSAQ (Vendor Security Assessment Questionnaire) — Google** — used as the named operating framework for this playbook.
- **SIG (Standardized Information Gathering) — Shared Assessments** — used as the named operating framework for this playbook.
- **CAIQ (Consensus Assessments Initiative Questionnaire) — CSA** — used as the named operating framework for this playbook.
- **ISO 27001 — Information Security Management** — used as the named operating framework for this playbook.
- **--** — used as the named operating framework for this playbook.
- **Before first enterprise deal (required by most procurement teams)** — used as the named operating framework for this playbook.
- **Annually thereafter (most enterprise contracts require annual pen tests)** — used as the named operating framework for this playbook.
- **After major architectural changes** — used as the named operating framework for this playbook.
- **After a security incident** — used as the named operating framework for this playbook.
- **Look for: CREST, OSCP/OSCE certified testers** — used as the named operating framework for this playbook.
- **Ask: "Show me a sample report." Good reports are detailed, actionable, and** — used as the named operating framework for this playbook.
- **Red flags: gives a quote without understanding your architecture, promises** — used as the named operating framework for this playbook.
- **Recommended: Cobalt, HackerOne, Synack, Bishop Fox, NCC Group, Cure53** — used as the named operating framework for this playbook.
- **Executive summary (for leadership)** — used as the named operating framework for this playbook.
- **Technical findings with: CVSS score, steps to reproduce, proof of concept,** — used as the named operating framework for this playbook.
- **Prioritization: Critical / High / Medium / Low / Informational** — used as the named operating framework for this playbook.
- **Retest: after fixing, the firm retests to confirm closure** — used as the named operating framework for this playbook.
- ****SAST (static):** Snyk, Semgrep, SonarQube — scans your code** — used as the named operating framework for this playbook.
- ****DAST (dynamic):** OWASP ZAP, Burp Suite, Detectify — scans your running app** — used as the named operating framework for this playbook.
- ****Dependency:** Snyk, Dependabot, npm audit — scans your libraries** — used as the named operating framework for this playbook.
- ****Container:** Trivy, Snyk — scans your Docker images** — used as the named operating framework for this playbook.
- ****Infrastructure:** AWS Inspector, Prowler, ScoutSuite — scans your cloud** — used as the named operating framework for this playbook.
- **Dependencies: on every PR (automated in CI)** — used as the named operating framework for this playbook.
- **Dynamic scanning: weekly** — used as the named operating framework for this playbook.
- **Infrastructure: monthly** — used as the named operating framework for this playbook.
- **Full pen test: annually + after major changes** — used as the named operating framework for this playbook.
- **You've passed at least one pen test (fix the known stuff first)** — used as the named operating framework for this playbook.
- **You have internal security expertise to triage reports** — used as the named operating framework for this playbook.
- **You have budget for bounties ($500-5,000 per valid report)** — used as the named operating framework for this playbook.
- **You have a process for responding to reports (SLA: acknowledge within 24** — used as the named operating framework for this playbook.
- **HackerOne (most common, enterprise-friendly)** — used as the named operating framework for this playbook.
- **Bugcrowd (similar to HackerOne)** — used as the named operating framework for this playbook.
- **Intigriti (European-focused)** — used as the named operating framework for this playbook.
- **Private: invite-only. Lower volume, higher quality. Start here.** — used as the named operating framework for this playbook.
- **Public: open to anyone. Higher volume, more noise. Scale to this.** — used as the named operating framework for this playbook.
- **Low severity: $100-500** — used as the named operating framework for this playbook.
- **Medium: $500-1,500** — used as the named operating framework for this playbook.
- **High: $1,500-5,000** — used as the named operating framework for this playbook.
- **Critical: $5,000-15,000+** — used as the named operating framework for this playbook.
- ****VSAQ (Google):** 50-100 questions, web-based, self-service** — used as the named operating framework for this playbook.
- ****SIG (Shared Assessments):** 200-400 questions, spreadsheet** — used as the named operating framework for this playbook.
- ****CAIQ (CSA):** 300+ questions, cloud-focused** — used as the named operating framework for this playbook.
- ****Custom:** Every enterprise has their own version (sigh)** — used as the named operating framework for this playbook.
- **SafeBase — trust center + auto-answer questionnaires ($)** — used as the named operating framework for this playbook.
- **SecurityPal — done-for-you questionnaire response ($$)** — used as the named operating framework for this playbook.
- **Vanta / Drata — compliance automation + questionnaire support ($$$)** — used as the named operating framework for this playbook.
- **Conveyor — AI-powered security questionnaire response ($)** — used as the named operating framework for this playbook.
- **Sev 1 (Critical): Data breach, system compromise, active attack** — used as the named operating framework for this playbook.
- **Sev 2 (High): Vulnerability with known exploit, suspicious activity** — used as the named operating framework for this playbook.
- **Sev 3 (Medium): Policy violation, minor security concern** — used as the named operating framework for this playbook.
- **Sev 4 (Low): Informational event, false positive** — used as the named operating framework for this playbook.
- **Incident Commander: [name] — coordinates response** — used as the named operating framework for this playbook.
- **Technical Lead: [name] — investigates and remediates** — used as the named operating framework for this playbook.
- **Communications Lead: [name] — internal + external comms** — used as the named operating framework for this playbook.
- **Legal: [name] — regulatory obligations** — used as the named operating framework for this playbook.
- **Executive Sponsor: [CEO/CTO]** — used as the named operating framework for this playbook.
- **GDPR: Supervisory authority within 72 hours** — used as the named operating framework for this playbook.
- **Customers: "Without undue delay" if high risk** — used as the named operating framework for this playbook.
- **Cyber insurance: As soon as practical (they provide legal + forensic support)** — used as the named operating framework for this playbook.
- **Law enforcement: If criminal activity (FBI, local police)** — used as the named operating framework for this playbook.
- **Customer notification: [template — what happened, what data, what we're doing,** — used as the named operating framework for this playbook.
- **Internal notification: [template — incident declared, response team activated,** — used as the named operating framework for this playbook.
- **SOC2 report (or status if in progress)** — used as the named operating framework for this playbook.
- **Penetration test summary (not the full report — that's confidential)** — used as the named operating framework for this playbook.
- **Sub-processor list (who handles customer data)** — used as the named operating framework for this playbook.
- **Security certifications (SOC2, ISO 27001, GDPR, etc.)** — used as the named operating framework for this playbook.
- **Encryption details (in transit: TLS 1.2+. At rest: AES-256)** — used as the named operating framework for this playbook.
- **Uptime and status page** — used as the named operating framework for this playbook.
- **Vulnerability disclosure policy (how to report a bug)** — used as the named operating framework for this playbook.
- **Contact: security@[company].com** — used as the named operating framework for this playbook.
- **Last test: [date / pending]** — used as the named operating framework for this playbook.
- **Provider: [firm]** — used as the named operating framework for this playbook.
- **Next test: [date — annually]** — used as the named operating framework for this playbook.
- **Findings: [X Critical, Y High, Z Medium, N Low]** — used as the named operating framework for this playbook.
- **Remediation status: [X% fixed]** — used as the named operating framework for this playbook.
- **SAST: [tool, cadence]** — used as the named operating framework for this playbook.
- **DAST: [tool, cadence]** — used as the named operating framework for this playbook.
- **Dependency: [tool, cadence]** — used as the named operating framework for this playbook.
- **Knowledge base: [doc link]** — used as the named operating framework for this playbook.
- **Response tool: [SafeBase / SecurityPal / manual]** — used as the named operating framework for this playbook.
- **Average response time: [X days]** — used as the named operating framework for this playbook.
- **Plan: [documented / needed]** — used as the named operating framework for this playbook.
- **Team: [assigned / needed]** — used as the named operating framework for this playbook.
- **Last tested: [date of last tabletop exercise]** — used as the named operating framework for this playbook.
- **[ ] Penetration test completed (web app minimum) — retest confirmed fixes** — used as the named operating framework for this playbook.
- **[ ] Vulnerability scanning automated (SAST + dependency + DAST)** — used as the named operating framework for this playbook.
- **[ ] Bug bounty program launched (private preferred for early stage)** — used as the named operating framework for this playbook.
- **[ ] Security questionnaire knowledge base built (100+ questions answered)** — used as the named operating framework for this playbook.
- **[ ] Incident response plan documented and team assigned** — used as the named operating framework for this playbook.
- **[ ] Trust center published (or SOC2 report available on request)** — used as the named operating framework for this playbook.
- **[ ] Sub-processor list maintained and publicly available** — used as the named operating framework for this playbook.
- **[ ] Annual security review scheduled** — used as the named operating framework for this playbook.
- ****Legal matters:** Consult a qualified attorney licensed in your jurisdiction.** — used as the named operating framework for this playbook.
- ****Tax matters:** Consult a certified tax professional or CPA.** — used as the named operating framework for this playbook.
- ****Accounting/financial matters:** Consult a qualified accountant or financial advisor.** — used as the named operating framework for this playbook.
- ****Insurance matters:** Consult a licensed insurance broker.** — used as the named operating framework for this playbook.
- ****Security/compliance matters:** Consult a qualified professional for your specific** — used as the named operating framework for this playbook.
- **`soc2-compliance` — SOC2 Type II certification** — used as the named operating framework for this playbook.
- **`data-privacy-compliance` — GDPR, CCPA, privacy programs** — used as the named operating framework for this playbook.
- **`legal-for-founders` — Legal foundations** — used as the named operating framework for this playbook.
- **`vendor-contracts` — DPAs, vendor security agreements** — used as the named operating framework for this playbook.

## When to Use

Trigger phrases: "security assessment", "penetration test for SaaS", "bug
bounty program", "security questionnaire", "VSAQ response", "enterprise
security review", "incident response plan", "vulnerability scanning",
"vendor security assessment", "pass security review"

## Step-by-Step Process

### Phase 1: Penetration Testing

**What it is:** Third-party security experts attempt to hack your application
and report vulnerabilities. Not the same as a vulnerability scan. Pen testers
think like attackers, chain multiple vulnerabilities, and demonstrate
business impact.

**When to get one:**
- Before first enterprise deal (required by most procurement teams)
- Annually thereafter (most enterprise contracts require annual pen tests)
- After major architectural changes
- After a security incident

**Types of pen tests:**

| Type | What's Tested | When | Cost |
|---|---|---|---|
| **Web Application** | Your SaaS app — injection, auth, XSS, CSRF, logic flaws | Always — this is the minimum | $5-15K |
| **API** | REST/GraphQL APIs — auth, rate limiting, data exposure | If you have APIs (you do) | $3-10K |
| **Infrastructure** | Cloud config, network security, server hardening | Annually | $5-15K |
| **Mobile** | iOS/Android apps | If you have mobile apps | $5-10K |
| **Social Engineering** | Phishing, pretexting against your team | Annually | $3-8K |

**How to hire a pen test firm:**
- Look for: CREST, OSCP/OSCE certified testers
- Ask: "Show me a sample report." Good reports are detailed, actionable, and
  prioritize vulnerabilities by severity (CVSS score).
- Red flags: gives a quote without understanding your architecture, promises
  "100% security," uses only automated scanners
- Recommended: Cobalt, HackerOne, Synack, Bishop Fox, NCC Group, Cure53

**What to expect in a pen test report:**
- Executive summary (for leadership)
- Technical findings with: CVSS score, steps to reproduce, proof of concept,
  remediation guidance
- Prioritization: Critical / High / Medium / Low / Informational
- Retest: after fixing, the firm retests to confirm closure

**What to do with findings:**
1. Critical: fix within 24-72 hours
2. High: fix within 1-2 weeks
3. Medium: fix within 30 days
4. Low/Informational: track in backlog, fix as time allows

### Phase 2: Vulnerability Scanning

**Continuous scanning (not one-time).** Unlike pen tests, vulnerability scans
are automated and run regularly.

**Tools:**
- **SAST (static):** Snyk, Semgrep, SonarQube — scans your code
- **DAST (dynamic):** OWASP ZAP, Burp Suite, Detectify — scans your running app
- **Dependency:** Snyk, Dependabot, npm audit — scans your libraries
- **Container:** Trivy, Snyk — scans your Docker images
- **Infrastructure:** AWS Inspector, Prowler, ScoutSuite — scans your cloud

**Cadence:**
- Dependencies: on every PR (automated in CI)
- Dynamic scanning: weekly
- Infrastructure: monthly
- Full pen test: annually + after major changes

### Phase 3: Bug Bounty Program

**Bug bounties are NOT a replacement for pen testing.** They're a supplement.
Pen tests are thorough, methodical, and time-boxed. Bug bounties are
crowdsourced, ongoing, and unpredictable.

**When to start a bug bounty:**
- You've passed at least one pen test (fix the known stuff first)
- You have internal security expertise to triage reports
- You have budget for bounties ($500-5,000 per valid report)
- You have a process for responding to reports (SLA: acknowledge within 24
  hours, validate within 7 days)

**Platforms:**
- HackerOne (most common, enterprise-friendly)
- Bugcrowd (similar to HackerOne)
- Intigriti (European-focused)

**Public vs Private:**
- Private: invite-only. Lower volume, higher quality. Start here.
- Public: open to anyone. Higher volume, more noise. Scale to this.

**Bounty ranges (guidelines):**
- Low severity: $100-500
- Medium: $500-1,500
- High: $1,500-5,000
- Critical: $5,000-15,000+

### Phase 4: Security Questionnaires

**The enterprise gauntlet.** Every enterprise customer will send you a security
questionnaire — usually a 200-400 question spreadsheet. Your job is to answer
it truthfully and route it through your team efficiently.

**Common questionnaire formats:**
- **VSAQ (Google):** 50-100 questions, web-based, self-service
- **SIG (Shared Assessments):** 200-400 questions, spreadsheet
- **CAIQ (CSA):** 300+ questions, cloud-focused
- **Custom:** Every enterprise has their own version (sigh)

**Strategy:**
1. **Build a knowledge base of answers.** Every question only needs to be
   answered once. Store answers in a shared doc or tool.
2. **Use a tool.** SafeBase, SecurityPal, or Vanta can auto-answer 70-80% of
   standard questionnaires from your security posture data.
3. **Route by section.** Engineering (app sec, encryption, SDLC), Ops (backup,
   DR, monitoring), Legal (privacy, data handling, sub-processors), People
   (background checks, training, offboarding).
4. **Be honest.** If you don't have something ("no, we don't encrypt data at
   rest" — you should fix this), say so. Lying on a security questionnaire is
   fraud and can void your insurance.

**Tools for security reviews:**
- SafeBase — trust center + auto-answer questionnaires ($)
- SecurityPal — done-for-you questionnaire response ($$)
- Vanta / Drata — compliance automation + questionnaire support ($$$)
- Conveyor — AI-powered security questionnaire response ($)

### Phase 5: Incident Response Plan

**Every SaaS company needs one.** If you don't have an incident response plan
when a breach happens, you're making it up in real-time while regulators,
customers, and lawyers demand answers.

**Incident Response Plan template:**

```
INCIDENT RESPONSE PLAN — [Company]

INCIDENT CLASSIFICATION:
- Sev 1 (Critical): Data breach, system compromise, active attack
- Sev 2 (High): Vulnerability with known exploit, suspicious activity
- Sev 3 (Medium): Policy violation, minor security concern
- Sev 4 (Low): Informational event, false positive

RESPONSE TEAM:
- Incident Commander: [name] — coordinates response
- Technical Lead: [name] — investigates and remediates
- Communications Lead: [name] — internal + external comms
- Legal: [name] — regulatory obligations
- Executive Sponsor: [CEO/CTO]

SEV 1 RESPONSE PLAYBOOK:
T+0-15 min: Detect. Acknowledge alert. Declare incident.
T+15-30 min: Incident Commander assembles response team.
T+30-60 min: Technical Lead begins investigation. Isolate affected systems.
T+1-2 hrs: Determine scope. What data/systems affected? Is attack ongoing?
T+2-4 hrs: Contain. Block attacker access. Preserve evidence.
T+4-24 hrs: Eradicate. Remove attacker presence. Patch vulnerability.
T+24-72 hrs: Recover. Restore systems. Monitor for re-entry.
T+72 hrs: Post-mortem. What happened? What failed? What changes prevent recurrence?

NOTIFICATION OBLIGATIONS:
- GDPR: Supervisory authority within 72 hours
- Customers: "Without undue delay" if high risk
- Cyber insurance: As soon as practical (they provide legal + forensic support)
- Law enforcement: If criminal activity (FBI, local police)

COMMUNICATION TEMPLATES:
- Customer notification: [template — what happened, what data, what we're doing,
  what they should do, contact for questions]
- Internal notification: [template — incident declared, response team activated,
  updates on [Slack channel / email thread], do not discuss externally]
```

### Phase 6: Trust Center

**What it is:** A public page documenting your security posture for customers
and prospects. Shows you take security seriously without requiring an NDA.

**What to include:**
- SOC2 report (or status if in progress)
- Penetration test summary (not the full report — that's confidential)
- Sub-processor list (who handles customer data)
- Security certifications (SOC2, ISO 27001, GDPR, etc.)
- Encryption details (in transit: TLS 1.2+. At rest: AES-256)
- Uptime and status page
- Vulnerability disclosure policy (how to report a bug)
- Contact: security@[company].com

**Tools for trust centers:** SafeBase, Conveyor, or custom page.

## Output Format

```
SECURITY PROGRAM — [Company]

PENETRATION TESTING:
- Last test: [date / pending]
- Provider: [firm]
- Next test: [date — annually]
- Findings: [X Critical, Y High, Z Medium, N Low]
- Remediation status: [X% fixed]

VULNERABILITY MANAGEMENT:
- SAST: [tool, cadence]
- DAST: [tool, cadence]
- Dependency: [tool, cadence]

SECURITY QUESTIONNAIRES:
- Knowledge base: [doc link]
- Response tool: [SafeBase / SecurityPal / manual]
- Average response time: [X days]

INCIDENT RESPONSE:
- Plan: [documented / needed]
- Team: [assigned / needed]
- Last tested: [date of last tabletop exercise]

TRUST CENTER: [URL / planned]
```

## Implementation Checklist

- [ ] Penetration test completed (web app minimum) — retest confirmed fixes
- [ ] Vulnerability scanning automated (SAST + dependency + DAST)
- [ ] Bug bounty program launched (private preferred for early stage)
- [ ] Security questionnaire knowledge base built (100+ questions answered)
- [ ] Incident response plan documented and team assigned
- [ ] Trust center published (or SOC2 report available on request)
- [ ] Sub-processor list maintained and publicly available
- [ ] Annual security review scheduled

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **No pen test before enterprise deal.** Customer asks for pen test report.
   You don't have one. Deal stalls for 4-6 weeks while you schedule and
   complete one. Fix: Pen test annually starting from your first mid-market
   deal.

2. **Pen test findings not fixed.** You have the report. You never fixed the
   findings. Next year's pen test finds the same issues. Customer's security
   team asks why. Fix: Track findings. Fix them. Get retest confirmation.

3. **Answering security questionnaires without engineering.** "Yes, we encrypt
   all data at rest" — but your engineering team knows you don't. You just
   committed to something in a contract. Fix: Route technical questions to
   the people who know the answers.

4. **No incident response plan.** Breach happens. Chaos. Everyone's emailing
   each other. Legal isn't looped in. Customer notification is delayed.
   Regulatory deadline missed. Fix: Document the plan. Assign the team. Test
   it with a tabletop exercise.

5. **Relying on bug bounties instead of pen tests.** Bug bounties catch the
   obvious stuff and miss the chained vulnerabilities that a methodical pen
   tester finds. Fix: Pen test annually. Bug bounty as supplement.



## ⚠️ Disclaimer

This skill provides general informational guidance based on publicly available frameworks and operator experience. It is NOT legal advice, accounting advice, tax advice, financial advice, insurance advice, or professional services advice.

Consult qualified professionals for your specific situation — attorneys for legal/equity matters, CPAs for tax and accounting, licensed brokers for insurance, and certified security assessors for compliance. This skill does not create a professional-client relationship. Use it as a starting point for research and preparation.

## Related Skills

- `soc2-compliance` — SOC2 Type II certification
- `data-privacy-compliance` — GDPR, CCPA, privacy programs
- `legal-for-founders` — Legal foundations
- `vendor-contracts` — DPAs, vendor security agreements
- `business-insurance` — Cyber insurance (requires security program)

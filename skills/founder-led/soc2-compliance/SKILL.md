---
name: soc2-compliance
description: >-
  Achieve SOC2 Type II compliance for SaaS companies — readiness assessment,
  control implementation, auditor selection, evidence collection, and ongoing
  monitoring. Use when preparing for SOC2, responding to enterprise security
  questionnaires, or building a compliance program. Triggers on: "SOC2", "SOC 2",
  "compliance", "security audit", "enterprise security", "security questionnaire",
  "Type II", or any request about security compliance for SaaS.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: founder-led
  tags: [soc2, compliance, security, enterprise, saas]
  related_skills: [building-saas, saas-metrics-calculator]
  frameworks: [AICPA Trust Services Criteria, SOC2 Type II Framework]
---

# SOC2 Compliance

## Overview

SOC2 Type II is the standard security compliance framework for B2B SaaS.
Enterprise customers will ask for it. Security questionnaires without it take
weeks to complete. With it, you send the SOC2 report and the conversation ends.

This skill covers the complete path: readiness assessment, control implementation,
auditor selection, evidence collection, and the ongoing monitoring that keeps
you compliant between audits. Budget ~$20-50K for first-year audit. Timeline:
4-6 months for Type I, 6-12 months observation period for Type II.

## When to Use

- "How do I get SOC2 compliant?"
- "Prepare for SOC2 Type II"
- "Enterprise customer asking for SOC2"
- "Set up security compliance"
- "Choose a SOC2 auditor"
- "Build a compliance program"
- "Answer security questionnaires faster"

## Step-by-Step Process

### Phase 1: Readiness Assessment (Month 1)

Determine if you actually need SOC2 now:
- **Need it now:** Enterprise customers are 20%+ of pipeline and asking for it.
  You're closing deals where SOC2 is the blocker.
- **Need it soon:** Enterprise pipeline is growing but not yet critical. Start
  implementing controls now, audit in 6-12 months.
- **Don't need it yet:** Under $1M ARR, no enterprise deals. Security
  questionnaire responses are sufficient. Revisit quarterly.

### Phase 2: Scope Definition

SOC2 has five Trust Services Criteria. You need at minimum:

**Security (required):** Access controls, change management, risk assessment,
incident response. This is the baseline.

**Availability (recommended):** System uptime, disaster recovery, capacity
management. If your SaaS going down impacts customers, include this.

**Confidentiality (if applicable):** Data encryption, disposal, access
restrictions. Relevant if handling sensitive customer data.

**Processing Integrity (if applicable):** Data processing accuracy, quality
assurance. Relevant if your product processes critical customer data.

**Privacy (if applicable):** Personal data handling, consent, data subject
rights. Relevant if handling PII.

Most B2B SaaS companies audit Security + Availability + Confidentiality.

### Phase 3: Control Implementation (Months 2-4)

Implement controls across these domains:

**Access Control:**
- SSO (Okta, Google Workspace, Azure AD) for all internal tools
- MFA required for all accounts. No exceptions
- Role-based access. Developers don't need production database access
- Offboarding process: revoke all access within 24 hours of departure

**Change Management:**
- Code review required for all production changes
- CI/CD pipeline with automated testing
- Separation of duties: developer doesn't approve their own PR
- Change log maintained for all production deployments

**Risk Assessment:**
- Annual risk assessment documented
- Vendor risk reviews for critical third-party tools
- Vulnerability scanning (weekly automated + annual penetration test)

**Incident Response:**
- Documented incident response plan
- Communication templates for customer notification
- Post-incident review process
- 24-hour initial response SLA for critical incidents

**Data Security:**
- Encryption at rest (all production databases)
- Encryption in transit (TLS everywhere)
- Backup strategy with tested restore process
- Data classification policy (what is sensitive, what is public)

### Phase 4: Auditor Selection

Choose a CPA firm accredited for SOC2 audits. Options:
- **Big 4 (Deloitte, PwC, EY, KPMG):** Most expensive ($40-80K+), most
  recognized by enterprise customers.
- **Mid-tier (Schellman, A-LIGN, Armanino, KirkpatrickPrice):** $20-40K,
  excellent for startups. Often provide readiness assessments.
- **Boutique:** $15-25K, good for simple environments. May not satisfy all
  enterprise procurement teams.

For most startups, a mid-tier firm is the right balance of cost, credibility,
and startup-friendliness.

### Phase 5: Audit and Evidence Collection

- **Type I (point-in-time):** Auditor verifies controls are designed properly.
  3-4 months. Good for initial certification.
- **Type II (over time):** Auditor verifies controls operated effectively over
  6-12 months. Required for enterprise credibility.

Evidence you'll need to collect:
- Access review logs (quarterly)
- Change management records (every deployment)
- Vendor risk assessments (annual)
- Penetration test reports (annual)
- Incident response records (as they occur)
- Backup test results (quarterly)
- Security training completion (annual, all employees)

### Phase 6: Ongoing Compliance

SOC2 is not a one-time project. Between audits:
- Quarterly access reviews
- Monthly vulnerability scanning
- Annual penetration testing
- Annual risk assessment
- Continuous monitoring of controls
- Bridge letter if audit gap exceeds 12 months

Automate evidence collection where possible. Compliance platforms (Vanta,
Drata, Secureframe) connect to your tools and collect evidence automatically.
~$10-25K/year but saves 10-20 hours/month of manual work.

## Output Format

SOC2 readiness plan with: scope definition (which criteria), control matrix
(gap analysis), implementation timeline, auditor shortlist, and budget estimate.

## Common Pitfalls

1. **Starting too early.** SOC2 at $500K ARR with no enterprise pipeline is
   premature optimization. Implement good security practices. Formal audit
   can wait.

2. **Starting too late.** Losing enterprise deals because you don't have SOC2
   is a sales problem, not a security problem. Start the process when
   enterprise pipeline hits 20%+ of total.

3. **Over-scoping.** Auditing all five criteria when you only need Security +
   Availability doubles the cost and timeline. Audit what customers ask for.

4. **Manual evidence collection.** Without a compliance platform, you'll spend
   10-20 hours/month on evidence. The platform pays for itself in time saved.

5. **No bridge letter.** If your audit gap exceeds 12 months, enterprise
   procurement teams will reject it. Get a bridge letter from your auditor.



## ⚠️ Disclaimer

This skill provides general informational guidance based on publicly available
frameworks and operator experience. It is NOT legal advice, accounting advice,
tax advice, financial advice, or professional services advice. Laws, regulations,
and best practices vary by jurisdiction and change over time.

- **Legal matters:** Consult a qualified attorney licensed in your jurisdiction.
- **Tax matters:** Consult a certified tax professional or CPA.
- **Accounting/financial matters:** Consult a qualified accountant or financial advisor.
- **Insurance matters:** Consult a licensed insurance broker.
- **Security/compliance matters:** Consult a qualified security assessor or compliance
  professional for your specific infrastructure and regulatory requirements.

This skill references publicly documented frameworks, standards, and operator
experiences. It does not constitute a professional opinion or create a
professional-client relationship. Use it as a starting point for your own
research and always verify against current regulations and professional guidance.

## Related Skills

- **building-saas**: SaaS architecture and scaling
- **exiting-company**: SOC2 as acquisition readiness

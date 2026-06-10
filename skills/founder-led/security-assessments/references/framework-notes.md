# Security Assessments — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- ****

## Authoritative foundations

This skill is grounded in public frameworks and source material relevant to the task:

- **OWASP Top 10 — Web application security risks.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **NIST Cybersecurity Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **VSAQ (Vendor Security Assessment Questionnaire) — Google.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **SIG (Standardized Information Gathering) — Shared Assessments.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **CAIQ (Consensus Assessments Initiative Questionnaire) — CSA.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **ISO 27001 — Information Security Management.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## Process phases

- Phase 1
- Phase 2
- Phase 3
- Phase 4
- Phase 5
- Phase 6

## Key reference tables

| Type | What's Tested | When | Cost |
|---|---|---|---|
| **Web Application** | Your SaaS app — injection, auth, XSS, CSRF, logic flaws | Always — this is the minimum | $5-15K |
| **API** | REST/GraphQL APIs — auth, rate limiting, data exposure | If you have APIs (you do) | $3-10K |
| **Infrastructure** | Cloud config, network security, server hardening | Annually | $5-15K |
| **Mobile** | iOS/Android apps | If you have mobile apps | $5-10K |
| **Social Engineering** | Phishing, pretexting against your team | Annually | $3-8K |

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |

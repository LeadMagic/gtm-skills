# Security Assessments — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations.

## Primary Frameworks

- **SIG (Shared Assessments) and CAIQ (Cloud Security Alliance)** — Pre-answer the standard questionnaires once and reuse the answers across customer reviews.
- **NIST Cybersecurity Framework 2.0** — Organize security answers around Govern, Identify, Protect, Detect, Respond, and Recover.
- **ISO/IEC 27001** — An ISMS certification answers many control questions at once; map questionnaire items to Annex A controls.
- **OWASP Top 10** — Show how the application addresses the most common web risks, backed by recent penetration test results.
- **Vanta — Trust Center** — Publish policies, reports, and subprocessors behind an NDA-gated portal so sales can share proof without email threads.

## Process phases

Mirrors `SKILL.md` → Step-by-Step Process:

- Phase 1: Penetration Testing
- Phase 2: Vulnerability Scanning
- Phase 3: Bug Bounty Program
- Phase 4: Security Questionnaires
- Phase 5: Incident Response Plan
- Phase 6: Trust Center

## Agent routing

| Question | Action |
|---|---|
| Full process | Follow `SKILL.md` step-by-step |
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |

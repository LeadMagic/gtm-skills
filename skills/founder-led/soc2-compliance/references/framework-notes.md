# Soc2 Compliance — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations.

## Primary Frameworks

- **AICPA — Trust Services Criteria** — Security is required; add Availability, Processing Integrity, Confidentiality, and Privacy only when customers need them.
- **AICPA — SOC 2 Type I vs Type II** — Type I tests control design at a point in time; Type II tests operating effectiveness over a 3-12 month window, which enterprise buyers expect.
- **Jason Lemkin (SaaStr) — SOC 2 as an enterprise sales gate** — Start SOC 2 before the first large enterprise deal requires it; the audit window takes months.
- **Vanta and Drata — Compliance automation** — Automate evidence collection and control monitoring to shorten readiness and keep controls passing between audits.

## Process phases

Mirrors `SKILL.md` → Step-by-Step Process:

- Phase 1: Readiness Assessment (Month 1)
- Phase 2: Scope Definition
- Phase 3: Control Implementation (Months 2-4)
- Phase 4: Auditor Selection
- Phase 5: Audit and Evidence Collection
- Phase 6: Ongoing Compliance

## Agent routing

| Question | Action |
|---|---|
| Full process | Follow `SKILL.md` step-by-step |
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |

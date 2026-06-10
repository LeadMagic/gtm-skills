# Solo Founder Gtm — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- **Winning by Design GTM Index**
- **SaaStr ACV Thresholds**
- **David Skok Unit Economics**
- **Sean Ellis PMF Survey (40% rule)**

## Authoritative foundations

- **Winning by Design GTM Index** — Self-assess your GTM maturity 1-10 across
  6 models: Revenue, Data, Math, Operating, Growth, GTM. Score below 6: fix
  fundamentals before scaling the team.
- **SaaStr (Jason Lemkin)** — ACV thresholds. Founder must personally close
  10-20 deals before hiring. VP Sales before $2M ARR: 70% failure rate.
- **David Skok** — Unit economics. CAC payback, LTV:CAC ratios by stage.
  Bootstrapped SaaS often hits 5-10x LTV:CAC organically.

## Process phases

| Phase | Focus | Artifact |
|---|---|---|
| 1 | Stage assessment (ARR, ACV, motion) | `SKILL.md` Phase 1 |
| 2 | Founder sales motion documentation | `founder-sales` |
| 3 | Unit economics gate (Skok) | `scale-readiness-gates.md` |
| 4 | PMF validation (Ellis 40%) | `pmf-signal-checklist.md` |
| 5 | First hire decision | Hire trigger table below |
| 6 | Scale readiness / spend caps | `spend-by-stage.md`, `when-not-to-scale.md` |

## Key reference tables

| MRR / ARR | Max sales payroll % ARR | First hire OTE band (H1 2026) |
|---|---|---|
| $50K MRR (~$600K ARR) | 15–20% | Delay or contractor |
| $80K MRR (~$1M ARR) | 15–25% | 1 AE $120–150K OTE |
| $150K+ MRR (~$1.8M ARR) | 20–30% | AE + optional SDR |

| Trigger | Hire | Why |
|---|---|---|
| Founder closed 10-20 deals personally | Senior AE (full-stack) | Motion proven. Clone yourself. |
| AE at capacity, pipeline bottleneck | First SDR | Feed the AE, don't make AE prospect. |
| 2 AEs at quota | Player-coach manager | Process repeatable. Needs management. |
| $2M+ ARR, 5+ reps | VP Sales | Scale what works. Never before $2M. |
| 8+ reps, ramp >6 months | Sales enablement | Onboarding cost justifies dedicated role. |

## PMF and scale artifacts

| Question | Artifact |
|---|---|
| Do we have PMF? | `pmf-signal-checklist.md` |
| Run PMF tests | `pmf-testing-playbook.md` |
| Ready to scale? | `scale-readiness-gates.md` |
| Stage spend guardrails | `gtm-spend-management/references/spend-by-stage.md` |
| Should we pause scale? | `when-not-to-scale.md` |
| Company journey stage | `saas-outcomes/references/journey-stage-gates.md` |

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |

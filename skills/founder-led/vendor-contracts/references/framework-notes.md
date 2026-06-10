# Vendor Contracts — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- YC — Standard commercial terms for B2B SaaS
- SaaS Capital — B2B SaaS contract benchmarks
- Jason Lemkin (SaaStr) — Enterprise contract negotiation
- David Skok (Matrix Partners) — B2B contract structure

## Authoritative foundations

This skill is grounded in public frameworks and source material relevant to the task:

- **YC — Standard commercial terms for B2B SaaS.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **SaaS Capital — B2B SaaS contract benchmarks.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Jason Lemkin (SaaStr) — Enterprise contract negotiation.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **David Skok (Matrix Partners) — B2B contract structure.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## Process phases

- Phase 1
- Phase 2
- Phase 3
- Phase 4

## Key reference tables

| Clause | Standard Position | Fallback | Non-Negotiable |
|---|---|---|---|
| **Limitation of Liability** | 12 months of fees paid | 24 months | Never unlimited |
| **Indemnification** | Mutual for IP claims. Customer indemnifies for their data. | Customer indemnifies for their use only | Never indemnify for customer's data misuse |
| **Warranty Disclaimer** | "AS IS" — no warranties beyond what's explicitly stated | Accept limited warranties (performance, security) | Never warranty "error-free" or "uninterrupted" |
| **Termination for Convenience** | 30 days written notice | 60 days | Must include — don't lock into perpetual |
| **Governing Law** | Your state (or Delaware) | Their state | Not international (costly to litigate) |
| **Payment Terms** | Net 30, annual upfront | Net 45, quarterly | Never Net 90+ (cash flow killer) |

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |

# Data Enrichment Strategy — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- **Eric Nowoslawski — Crawl Walk Run** — Start minimal enrichment; expand on reply signal
- **Pat Spielmann — Full-Circle verify gate** — Verification before any send
- **Alex MacCaw / Clearbit — Enrichment as infrastructure** — Real-time at form + batch for outbound
- **Scott Brinker — Martech stack discipline** — Avoid duplicate enrichment vendors

## Authoritative foundations

Enrichment strategy answers: **what fields, which providers, at what trigger,
with what refresh cadence**. Filter-first architecture saves 40–60% of enrichment
cost vs enrich-all-contacts approaches.

## Process phases

- **Phase 1 — Field map:** Required vs nice-to-have by motion (outbound, inbound, CS)
- **Phase 2 — Provider matrix:** Cost-per-hit, coverage by segment, fallback order
- **Phase 3 — Trigger design:** Form, CRM stage change, list build, webhook
- **Phase 4 — Governance:** Refresh TTL, stale data rules, vendor spend cap

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |

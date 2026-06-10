# List Building — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- **Jordan Crawford — PQS / PVP / FIND** — Build lists from won-deal pain patterns, not generic firmographics. `cold-email-strategy/references/jordan-crawford-blueprint-gtm.md`
- **Joey Gilkey — Phone Intent** — Tier list by dial reachability before phone-heavy motions. `references/joey-gilkey-bucketing.md`
- **Eric Nowoslawski — Unit economics gate** — List size × cost-per-contact must clear CAC math. `cold-email-strategy/references/eric-nowoslawski-outbound.md`
- **Pat Spielmann — Verify-before-send** — Enrichment waterfall with verification gate. `cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

## Authoritative foundations

List building follows the **filter-first, enrich-second** pattern: lightweight ICP
qualification before expensive contact lookups. Clay table architecture maps
naturally — company enrichment → ICP filter → contact waterfall.

## Process phases

- **Phase 1 — ICP + source selection:** Define firmographics, titles, triggers; pick sources (Sales Nav, Apollo, Claygent, signals)
- **Phase 2 — Company gate:** Domain validity, size, tech, ICP fit ≥80% before contact spend
- **Phase 3 — Contact enrichment:** Email/phone waterfall; verify ≥98% valid emails
- **Phase 4 — QA + segment:** Dedupe <3%; tag Phone Intent tier; export to CRM/sequencer

## Key reference tables

| Source | Best For | Data Quality |
|---|---|---|
| LinkedIn Sales Nav | B2B, any industry | High — verified profiles |
| Apollo Search | US B2B, all sizes | High — 270M+ contacts |
| Claygent web search | Founders, execs, niche | Medium — web-sourced |
| Google Maps scrape | Local SMB | Medium — needs enrichment |
| Conference speaker lists | Industry leaders | Very high — curated |
| Crunchbase | Funded startups | High — funding-verified |
| GitHub | Dev tools, tech | High — public activity |
| Job boards (Lever, Greenhouse) | Growing companies | High — active hiring signal |

| Dimension | Pass Criteria |
|---|---|
| Domain validity | All domains resolve |
| ICP fit | 80%+ match defined ICP |
| Title relevance | 70%+ match target titles |
| Email coverage | 85%+ have verified email |
| Email verification | 98%+ verified valid |
| Duplicate rate | Under 3% |
| Geographic fit | 90%+ in target regions |
| Company size fit | 80%+ in target range |

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |

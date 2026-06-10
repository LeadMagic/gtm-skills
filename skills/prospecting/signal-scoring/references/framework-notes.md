# Signal Scoring — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- **Joey Gilkey — Phone Intent** — Reachability tier for phone-first routing. `references/joey-gilkey-bucketing.md`
- **Justin Michael — TQ / trigger-based outbound** — Time + trigger quality scoring. `cold-email-strategy/references/justin-michael-sales-borg.md`
- **Jordan Crawford — Pain-based segments** — Score by verifiable pain signal, not firmographics alone
- **Henry Schuck — ZoomInfo intent** — Composite intent for enterprise (reference pattern)

## Authoritative foundations

Signal scoring prioritizes **who to work now** — combine fit (ICP), intent
(hiring, funding, tech change), and reachability (phone/email quality).
Weight signals by correlation to won deals, not vendor hype.

## Process phases

- **Phase 1 — Signal inventory:** List available first-party + third-party signals
- **Phase 2 — Weight calibration:** Back-test weights against last 20 wins
- **Phase 3 — Tier model:** P1/P2/P3 thresholds; map to channel (phone vs email)
- **Phase 4 — Ops wiring:** CRM fields, alerts, sequencer enrollment rules

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |

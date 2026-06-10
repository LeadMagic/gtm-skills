# Inbound Triage — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- **Dharmesh Shah — Inbound flywheel** — Attract → Engage → Delight; lifecycle routing. `references/dharmesh-shah-hubspot-inbound.md`
- **Mark Roberge — Lead scoring + SLA** — Speed-to-lead and fit scoring from HubSpot era
- **Chris Walker — Anti–MQL volume** — Qualify hard; don't optimize form fills alone. `references/chris-walker-mental-models.md`
- **Winning by Design — SPICED** — Qualification fields for handoff to sales

## Authoritative foundations

Inbound triage balances **speed** (minutes matter for hot leads) with **fit**
(wrong leads waste AE time). Define routing rules by segment, score, and
source — visitor ID and dark social leads need different SLAs.

## Process phases

- **Phase 1 — Routing matrix:** Source × score × segment → owner + SLA
- **Phase 2 — Scoring model:** Fit + behavior + firmographics; recalibrate monthly
- **Phase 3 — Automation:** CRM workflows, round-robin, PQL vs MQL paths
- **Phase 4 — Feedback loop:** Win/loss by source → marketing spend allocation

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |

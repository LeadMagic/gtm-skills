# Instantly Sequences — Framework Notes

**Category:** `tools` · **Tool path:** platform-specific sequencer (not sequencing-toolkit)

## Primary Frameworks

- **Eric Nowoslawski — Cold Email Infrastructure** — 2 inboxes/domain, 30 sends/day/inbox, warmup before launch, unit economics gate. Canonical → `../../../outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md`
- **Instantly Best Practices** — Warmup pool, account rotation, unified inbox, A/B testing (26 variants)
- **Pat Spielmann — Cold to Gold** — Verify-before-send from Clay; data quality before copy scale → `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

## Tool Boundaries

| Layer | Skill | Role |
|---|---|---|
| Enrichment | clay-toolkit / leadmagic-waterfall | Find → Verify → Enrich |
| Loops | clay-loops-toolkit | Signal → enrich → route |
| Sequencer | instantly-sequences (this skill) | Send + unified inbox |
| Architecture | sequencing-toolkit | Cross-platform comparison |

## Clay Enrollment

Load `references/clay-enrollment-handoff.md` before pushing Clay rows to Instantly.

## Eric Infra Defaults

- Secondary domains only; 2-3 mailboxes per domain
- 30-50 sends/day/mailbox; Instantly auto-rotation
- 2-3 week warmup pool before campaigns
- Open tracking OFF; reply tracking ON

## Agent Use

1. Confirm infra (`domain-infrastructure`, `email-deliverability`) before campaign build.
2. Load clay-enrollment-handoff if source is Clay table or loop.
3. Cite Eric for volume/infra; Pat for verify gate.
4. Run `check-output.py` on deliverable.

Expert router → `references/gtm-experts-outbound-index.md`

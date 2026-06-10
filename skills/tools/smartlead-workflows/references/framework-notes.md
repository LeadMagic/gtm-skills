# Smartlead Workflows — Framework Notes

**Category:** `tools` · Eric Nowoslawski runs largest Smartlead deployments.

## Primary Frameworks

- **Eric Nowoslawski — Cold Email Infrastructure** — Unlimited mailboxes, 30-50/day/mailbox, master inbox, unit economics. Canonical → `../../../outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md`
- **Smartlead Best Practices** — Auto-rotation, AI reply categorization, A/B at campaign level
- **Pat Spielmann — Cold to Gold** — Verify-before-send from Clay → `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

## Tool Boundaries

| Layer | Skill | Role |
|---|---|---|
| Enrichment | leadmagic-waterfall / clay-toolkit | Verify gate upstream |
| Loops | clay-loops-toolkit | Signal → Smartlead campaign map |
| Sequencer | smartlead-workflows (this skill) | Scale send + master inbox |
| CLI push | leadmagic-cli | `lm integrations smartlead push` |

## Clay Enrollment

Load `references/clay-enrollment-handoff.md` — Eric-scale patterns use 15-25 mailboxes per campaign.

## AI Reply Categories (train before scale)

INTERESTED · NOT NOW · OOO · UNSUBSCRIBE · WRONG CONTACT

## Agent Use

1. Infrastructure checklist before first campaign.
2. Verify gate documented if Clay is source.
3. Cite Eric for mailbox math; Pat for data quality.
4. Run `check-output.py`.

Expert router → `references/gtm-experts-outbound-index.md`

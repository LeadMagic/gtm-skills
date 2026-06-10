# Outreach Sequences — Framework Notes

**Category:** `tools` · Enterprise sequencing engine + triggers + analytics.

## Primary Frameworks

- **Outreach — Sales Engagement Cadence Design** — Trigger-based enrollment, A/B at step level, analytics
- **Pat Spielmann — Verify-before-enroll** — CRM gate before sequence → `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`
- **Eric Nowoslawski — Agency Clay execution** — High-volume outbound often pairs Outreach CRM sync with Clay enrich → `../../../outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md`

## Tool Boundaries

| Layer | Skill | Role |
|---|---|---|
| Enrichment | clay-toolkit | Table → CRM upsert |
| Orchestration | n8n-toolkit OUT-01 | API enrollment with verify gate |
| SEP | outreach-sequences (this skill) | Triggers + sequences |
| Architecture | sequencing-toolkit | Cross-platform patterns |

## Enrollment Gate

Load `references/enrichment-enrollment-gate.md` — prefer Clay → CRM → Outreach trigger path.

## Trigger Types

- Prospect field change (email_status → valid)
- Account signal tag from clay-loops
- Manual SDR approval task
- n8n API (real-time loops)

## Agent Use

1. Map CRM custom fields before trigger design.
2. Never auto-enroll on list import without verify.
3. Cite Pat for data gate; Eric if scaling connected mailboxes.
4. Run `check-output.py`.

Expert router → `references/gtm-experts-outbound-index.md`

# Salesloft Cadences — Framework Notes

**Category:** `tools` · Enterprise SEP — Rhythm cadences + Conversations.

## Primary Frameworks

- **Salesloft Rhythm Cadences** — Email + call + LinkedIn orchestration, task-gated steps
- **Pat Spielmann — Verify-before-enroll** — CRM field gate before cadence → `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`
- **Eric Nowoslawski — Infra at scale** — If using connected mailboxes for outbound volume → `../../../outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md`

## Tool Boundaries

| Layer | Skill | Role |
|---|---|---|
| Enrichment | clay-toolkit / leadmagic-waterfall | CRM field population |
| Loops | clay-loops-toolkit | Signal → CRM → cadence trigger |
| SEP | salesloft-cadences (this skill) | Rhythm + rep tasks |
| CRM sync | crm-integration | Field mapping |

## Enrollment Gate

Load `references/enrichment-enrollment-gate.md` — lm_email_status must be valid in CRM before auto-enroll.

## Enterprise Assumptions

- Admin approval on cadences >500 contacts
- Conversation intelligence for coaching, not auto-send
- Persona-based cadence selection via CRM fields

## Agent Use

1. CRM custom fields (verify status, last_verified) before cadence design.
2. Pat verify gate in enrollment rules.
3. clay-loops-toolkit for signal-triggered cadences.
4. Run `check-output.py`.

Expert router → `references/gtm-experts-outbound-index.md`

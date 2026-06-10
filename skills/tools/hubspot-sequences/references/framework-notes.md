# HubSpot Sequences — Framework Notes

**Category:** `tools` · CRM-native sequences — rep-triggered + workflow-enrolled.

## Primary Frameworks

- **HubSpot Sequences Best Practices** — Enrollment caps, task steps, tracking settings
- **Pat Spielmann — Verify-before-enroll** — Workflow checks lm_email_status → `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`
- **Guillaume Moubeche — Multichannel principles** — LinkedIn + email coordination (adapt to HubSpot tasks) → `../../../outbound/cold-email-strategy/references/lemlist-guillaume-outbound.md`

## Tool Boundaries

| Layer | Skill | Role |
|---|---|---|
| Enrichment | leadmagic-waterfall / clay-toolkit | Populate CRM properties |
| Loops | clay-loops-toolkit | List membership → workflow |
| CRM automation | hubspot-setup | Workflow + property limits |
| Sequences | hubspot-sequences (this skill) | Rep + automated enroll |

## Enrollment Gate

Load `references/enrichment-enrollment-gate.md` — workflow must verify before sequence enrollment.

## HubSpot-Specific

- Rep-triggered: show verify status in sidebar; block if invalid
- Workflow-enrolled: branch on lm_email_status + signal_tag
- Pair with hubspot-setup for object/property governance

## Agent Use

1. Custom properties (lm_email_status, last_verified, personalization_snippet).
2. Workflow diagram before sequence template.
3. clay-loops list → workflow pattern for signals.
4. Run `check-output.py`.

Expert router → `references/gtm-experts-outbound-index.md`

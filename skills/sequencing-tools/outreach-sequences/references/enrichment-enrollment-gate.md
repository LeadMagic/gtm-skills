# Enrichment → Outreach Sequence Enrollment Gate

Outreach sequences require CRM-synced, verified contacts before automated enrollment.

## Verify-Before-Enroll (Pat Spielmann)

Enrollment rules must check:

```
Prospect.email_status = 'valid'
AND Prospect.last_verified <= 90 days ago
AND Prospect.suppression != true
AND Account.icp_tier IN (target tiers)
```

Cross-ref: `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

## Clay → Outreach via CRM

Preferred path (avoids direct Clay→Outreach sync conflicts):

```
Clay table enrich + verify
  → CRM upsert (HubSpot/SFDC)
  → Outreach trigger: prospect updated + email_status = valid
  → Sequence enrollment by persona/signal tag
```

Alternative: Outreach API enrollment from n8n OUT-01 with verify gate in workflow.

## Required CRM Custom Fields

| Field | Populated By | Used In Outreach |
|---|---|---|
| `lm_email_status` | LeadMagic verify | Trigger condition |
| `last_verified` | Timestamp | Stale re-verify rule |
| `signal_type` | Clay loop | Sequence selection |
| `why_now` | Claygent | Step 1 merge tag |
| `source_url` | Monitor | Rep context in task |

Load Clay patterns: `../../../tools/clay-toolkit/references/gtm-table-blueprints.md`

## Trigger Architecture

| Trigger Type | Use Case |
|---|---|
| Prospect field change | email_status → valid |
| Account signal tag | funding, hiring from clay-loops |
| Manual task completion | SDR approves after research |
| API (n8n) | Real-time loop enrollment |

**Never** auto-enroll on list import without verify column.

## Eric Nowoslawski Scale Note

High-volume outbound via Outreach still requires infra discipline if using connected mailboxes — 30 sends/day/inbox, secondary domains only.

Cross-ref: `../../../outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md`

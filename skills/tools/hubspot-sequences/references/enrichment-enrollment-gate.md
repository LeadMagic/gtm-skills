# Enrichment → HubSpot Sequence Enrollment Gate

HubSpot Sequences are rep-triggered or workflow-enrolled — verification must happen in CRM workflows before sequence start.

## Verify-Before-Enroll (Pat Spielmann)

Workflow enrollment condition:

```
contact.email IS NOT NULL
AND contact.lm_email_status = 'valid'
AND contact.last_verified is within 90 days
AND contact.hs_email_optout != true
AND contact.lifecyclestage NOT IN (customer, evangelist)
```

Cross-ref: `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

## HubSpot Workflow Pattern

```
Trigger: Contact property change (email filled OR re-enrichment request)
  → Custom code / n8n / Clay sync: LeadMagic verify
  → Set lm_email_status, last_verified
  → Branch: if valid → enroll in Sequence (by persona)
  → Branch: if invalid → create task "Find valid email"
```

Pair with `hubspot-setup` for workflow object limits and enrollment caps.

## Clay → HubSpot Field Map

| Clay Column | HubSpot Property | Notes |
|---|---|---|
| Verify Email status | `lm_email_status` | Dropdown: valid/invalid/risky |
| Enrich Person title | `jobtitle` | Do not overwrite if rep-edited |
| why_now | `personalization_snippet` | Sequence token {{personalization_snippet}} |
| signal_type | `signal_tag` | Workflow branch for sequence pick |
| source_url | `signal_source_url` | Rep visibility |

Load table blueprints: `../../../tools/clay-toolkit/references/gtm-table-blueprints.md`

## Clay Loops → HubSpot

Signal loops push to HubSpot lists; workflow enrolls into Sequences:

1. clay-loops-toolkit ACTION → HubSpot list (verified only)
2. Workflow: list membership + lm_email_status = valid → Sequence
3. Champion job change → route to AE task, not Sequence

Load: `../../../tools/clay-loops-toolkit/references/leadmagic-waterfall.md`

## Rep-Triggered Sequences

When rep manually enrolls:

- HubSpot sidebar shows `lm_email_status` — block enroll if invalid/stale
- Sequence template includes {{personalization_snippet}} from Clay
- Log enrollment source for attribution

## Cross-References

- Guillaume multichannel (if using HubSpot + LinkedIn): `../../../outbound/cold-email-strategy/references/lemlist-guillaume-outbound.md` (principles apply)
- Eric infra if using connected inboxes: `../../../outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md`

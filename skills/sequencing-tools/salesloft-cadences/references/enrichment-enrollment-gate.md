# Enrichment → Salesloft Cadence Enrollment Gate

Enterprise SEP pattern: CRM is source of truth; enrichment validates before cadence enrollment.

## Verify-Before-Enroll (Pat Spielmann)

No contact enters a Salesloft cadence without:

1. LeadMagic (or waterfall) verify on email field
2. `email_status = valid` in CRM custom field
3. `last_verified` < 90 days
4. Suppression list check (customer, competitor, unsub)

Cross-ref: `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

## CRM → Salesloft Flow

```
CRM contact created/updated
  → Workflow: if email present AND last_verified stale
  → LeadMagic verify (Clay column OR n8n OR API)
  → Update CRM: email_status, last_verified
  → If valid + ICP fit → Salesloft cadence enrollment rule
  → If invalid → task for SDR to find alternate contact
```

## Clay Integration Pattern

| Clay Output | CRM Field | Salesloft Trigger |
|---|---|---|
| Verify status | `lm_email_status` | Cadence rule: status = valid |
| Title | `title` | Persona-based cadence pick |
| Phone | `phone` | Rhythm: call step enabled |
| why_now | `personalization_snippet` | Cadence custom field merge |

Use clay-toolkit for one-time list scrub; clay-loops-toolkit for ongoing signal cadences.

## Salesloft Rhythm Defaults

- Email + call + LinkedIn in Rhythm cadence (not email-only)
- Task completion required before next automated step
- Conversation intelligence tags feed coaching — not auto-send triggers

## Enterprise Governance

- Admin approval on new cadences >500 contacts
- Domain send limits aligned with Eric Nowoslawski infra if using connected mailboxes
- Audit log: who enrolled, verify timestamp, signal source

Cross-ref Eric infra: `../../../outbound/cold-email-strategy/references/eric-nowoslawski-outbound.md`

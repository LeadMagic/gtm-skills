# Clay → Lemlist Enrollment Handoff

Use when Clay table pushes contacts to Lemlist multichannel sequences.

## Pre-Push Gate

Pat Spielmann verify-before-send + Guillaume problem-first mapping:

```
email_valid = true
AND verify_status = valid
AND trigger_problem mapped (not generic congrats)
AND suppression = false
```

Cross-ref Pat: `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`
Cross-ref Guillaume: `../../../outbound/cold-email-strategy/references/lemlist-guillaume-outbound.md`

## Required Fields for Lemlist Personalization

| Field | Clay Source | Lemlist Use |
|---|---|---|
| `email` | LeadMagic waterfall | Email step |
| `first_name`, `company` | Enrich | {{firstName}}, {{companyName}} |
| `problem_hook` | Claygent on signal | Email 1 opener (Guillaume CTC) |
| `linkedin_url` | Enrich Person | LinkedIn step (Day 2-4) |
| `phone` | Enrich Person | Call step if multichannel |
| `image_var` | Formula | Dynamic image placeholder |

## Guillaume Multichannel Cadence (4-9 touches)

Typical Clay → Lemlist sequence:

| Day | Channel | Content source |
|---:|---|---|
| 0 | Email | problem_hook from Clay |
| 2 | LinkedIn visit | auto |
| 3 | Email | case study column |
| 5 | LinkedIn DM | short variant of why_now |
| 7 | Email | breakup |

Do not paste email copy into LinkedIn — channel-native per Guillaume playbook.

## Clay Loops Integration

Signal loops → Lemlist campaign mapping:

- Funding signal → campaign "Funding — [Persona]"
- Job change champion → route to AE (not Lemlist) if open opp
- Hiring signal → campaign "Hiring — [Role tier]"

Load: `../../../tools/clay-loops-toolkit/references/loop-catalog.md`

## lemwarm Prerequisite

All mailboxes in lemwarm **>95 reputation** before enrolling Clay batch.
Enroll in waves (500/day max) to protect deliverability.

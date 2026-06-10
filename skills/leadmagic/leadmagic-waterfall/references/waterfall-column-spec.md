# LeadMagic Waterfall — Clay Column Spec

Copy-paste column configuration for Clay Table 3 (ENRICH) or standalone prospecting tables.
Load `leadmagic-toolkit` for API credentials.

## Standard Waterfall (Pat Spielmann — Cold to Gold)

| Order | Column Name | Integration | Credits | Run Condition |
|---:|---|---|---:|---|
| 0 | ICP Filter | Formula | 0 | always — firmographic gate first |
| 1 | LM Find Email | LeadMagic → Email Finder | 1 | ICP pass |
| 2 | Apollo Find | Apollo (fallback) | 1 | LM Find empty |
| 3 | Hunter Find | Hunter (fallback) | 1 | Apollo empty |
| 4 | Best Email | COALESCE formula | 0 | always |
| 5 | LM Verify | LeadMagic → Email Validation | 1 | Best Email not empty |
| 6 | email_valid | Formula | 0 | Verify = valid/deliverable |
| 7 | LM Enrich Person | LeadMagic → Enrich | 2 | email_valid = true |
| 8 | why_now | Claygent (ai-prompts P03) | varies | email_valid = true |

Cross-ref Pat: `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

## COALESCE Formula (Best Email)

```
COALESCE({{LM Find Email}}, {{Apollo Find}}, {{Hunter Find}})
```

Prefer LM result — verified at lookup.

## email_valid Formula

```
IF(
  OR({{LM Verify}} = "valid", {{LM Verify}} = "deliverable"),
  true,
  false
)
```

## Catch-All Branch

If Verify = risky/catch-all:

- Set `route = catch_all_queue`
- Do NOT push to cold sequencer at full volume
- Optional: reduced-volume test campaign with monitoring

## Credit Budget

```
typical_row = 1 (find) + 1 (verify) + 2 (enrich) = 4 credits
with_fallbacks = up to 6 credits (cap per row)
monthly = rows × avg_credits_per_row
```

Qualify ICP first — saves 30-40% credits (Pat + clay-toolkit pattern).

## Sequencer Handoff Fields

Export only where `email_valid = true`:

| Export Field | Column |
|---|---|
| email | Best Email |
| title | LM Enrich Person |
| phone | LM Enrich Person |
| why_now | why_now |
| verify_status | LM Verify |
| lm_credits | Sum formula |

Route to: instantly-sequences, smartlead-workflows, or lemlist-setup via Clay native integration or CSV.

## Clay Loops Variant

For signal loops, use shorter chain from `../../../tools/clay-loops-toolkit/references/leadmagic-waterfall.md` — run only when `signal_detected = true`.

## Anti-Patterns

- Claygent for email find (40-60% bounce) — use LeadMagic Find only
- Verify skip before sequencer — always LM Verify
- Enrich before ICP filter — wastes credits

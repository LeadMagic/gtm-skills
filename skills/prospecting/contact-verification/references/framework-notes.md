# Contact Verification — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- ****

## Authoritative foundations

Email verification is grounded in established deliverability practices.
Industry consensus across major sending platforms (Google Workspace, M365,
Smartlead, Instantly) converges on a bounce rate ceiling of 2% for cold
outreach and best-in-class operations targeting under 1%.

Data decay is real: 2-3% of B2B emails become invalid every month. A
10,000-contact database loses 200-300 valid emails monthly. Re-verification
on a 90-day cadence is the minimum to maintain list health.

## Process phases

- Phase 1
- Phase 2
- Phase 3
- Phase 4

## Key reference tables

| Status | Meaning | Action for Cold Outbound | Action for Warm/Nurture |
|---|---|---|---|
| **valid** | Mailbox exists and accepts mail | Safe to send | Safe to send |
| **invalid** | Mailbox doesn't exist or is deactivated | Do not send — remove from list | Do not send |
| **risky / catch-all** | Domain accepts all mail, can't confirm individual mailbox | Skip at volume. Send selectively (max 5% of volume) with extra monitoring | Send, monitor bounces closely |
| **unknown** | Could not determine status | Skip. Re-verify in 7 days or discard | Send if high-value, monitor |
| **disposable** | Temporary/throwaway address | Never send | Never send |

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |

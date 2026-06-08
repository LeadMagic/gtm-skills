---
name: contact-verification
description: >-
  Verify email addresses before they enter outbound sequences to prevent bounces
  and protect sender reputation. Use when the user wants to validate emails,
  check deliverability, verify contact data, prevent bounces, clean a list, or
  ensure their outreach list is safe to send. Triggers on: \"verify emails\",
  \"validate this list\", \"check if these emails are real\", \"email verification\",
  \"bounce prevention\", \"clean my list\", \"are these safe to send\", or any request
  to confirm email deliverability before outreach.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: \"1.0.0\"
  author: LeadMagic
  category: prospecting
  tags: [verification, email, deliverability, bounce-prevention, data-quality]
  related_skills: [email-finding, lead-enrichment, email-deliverability, list-building]
  frameworks:
    - "Email Deliverability Best Practices"
    - "Aaron Ross — Predictable Revenue"
    - "Winning by Design — ICP Segmentation"
---

# Contact Verification

## Overview

Verification is the gate between finding emails and sending to them. Skipping it
is the single most expensive mistake in outbound — a 5% bounce rate triggers
automated spam filtering at every major inbox provider. Recovery takes months.

The rule: every email address entering a sequence must pass verification first.
No exceptions. Verify when you find, re-verify every 90 days, and always verify
before a new campaign launches.

## When to Use

- \"Verify these emails before we send\"
- \"Check if these addresses are deliverable\"
- \"Clean my prospect list\"
- \"Are these safe to send to?\"
- \"Validate this CSV of contacts\"
- \"What's the bounce risk on this list?\"

Do NOT use for:
- Finding new emails — use email-finding first
- Deliverability infrastructure setup — use email-deliverability
- General list hygiene beyond email — use list-building

## Authoritative Foundations

Email verification is grounded in established deliverability practices.
Industry consensus across major sending platforms (Google Workspace, M365,
Smartlead, Instantly) converges on a bounce rate ceiling of 2% for cold
outreach and best-in-class operations targeting under 1%.

Data decay is real: 2-3% of B2B emails become invalid every month. A
10,000-contact database loses 200-300 valid emails monthly. Re-verification
on a 90-day cadence is the minimum to maintain list health.

## Prerequisites

- A list of email addresses to verify
- Access to a verification service (LeadMagic Email Validation, ZeroBounce,
  NeverBounce, MillionVerifier, or equivalent)
- For batch verification: CSV with at minimum an email column

## Step-by-Step Process

### Phase 1: Intake

Ask the user:
1. How many emails need verification? (single vs batch)
2. When were these emails last verified? (if never, flag as high-risk)
3. What's the sending volume and cadence? (higher volume = stricter verification)
4. Are these going to cold outreach or warm nurture? (cold = stricter)

### Phase 2: Run Verification

Submit each email to the verification service. Services return a status:

| Status | Meaning | Action for Cold Outbound | Action for Warm/Nurture |
|---|---|---|---|
| **valid** | Mailbox exists and accepts mail | Safe to send | Safe to send |
| **invalid** | Mailbox doesn't exist or is deactivated | Do not send — remove from list | Do not send |
| **risky / catch-all** | Domain accepts all mail, can't confirm individual mailbox | Skip at volume. Send selectively (max 5% of volume) with extra monitoring | Send, monitor bounces closely |
| **unknown** | Could not determine status | Skip. Re-verify in 7 days or discard | Send if high-value, monitor |
| **disposable** | Temporary/throwaway address | Never send | Never send |

### Phase 3: Segment and Route

1. **Valid** → Route to the sendable list. Mark with verification date.
2. **Invalid** → Remove from all sequences. Log the bounce reason if available.
3. **Risky/Catch-All** → Separate list. For cold outbound at volume: skip entirely.
   For high-value enterprise accounts: send at reduced volume (<5% of total),
   monitor bounce rates daily.
4. **Unknown** → Hold for re-verification. If critical contact, attempt after 7 days.
   Otherwise, discard.

### Phase 4: Record Keeping

Every verified contact should have:
- `verification_status`: valid | invalid | risky | unknown
- `verification_date`: ISO date of last verification
- `verification_source`: which service was used

CRM systems should filter sequences to only include `verification_status = valid`
AND `verification_date` within last 90 days.

## Output Format

Summary report:
```
Total verified: 1,000
Valid: 920 (92%)
Invalid: 35 (3.5%)
Risky/Catch-All: 30 (3%)
Unknown: 15 (1.5%)

Sendable (valid): 920
Requires monitoring (risky): 30
Removed (invalid + unknown): 50

Estimated safe send volume: 920-950/day (depending on risky handling)
Bounce rate projection: 0.8-1.5%
```

## Quality Check

- [ ] All emails in sequence have verification_status = valid
- [ ] No emails with verification_date older than 90 days
- [ ] Invalid emails removed from all active sequences
- [ ] Catch-all emails tracked separately with daily bounce monitoring
- [ ] Disposable emails permanently suppressed

## Common Pitfalls

1. **Skipping verification entirely.** \"We found the emails from a reputable
   source.\" Every provider returns stale data. 5-15% of \"found\" emails bounce.
   The cost of re-warming a domain far exceeds the cost of verification.

2. **Treating catch-all as safe.** Catch-all domains accept mail to any address
   at the domain, making individual mailbox verification impossible. They produce
   higher bounce rates. Treat them as a separate, monitored segment.

3. **One-time verification.** \"We verified this list 6 months ago.\" At 2-3%
   monthly decay, 12-18% of that list is now invalid. Re-verify every 90 days.

4. **Sending to invalid emails one more time.** \"Maybe it was a temporary
   bounce.\" If verification returns invalid, the mailbox doesn't exist. Sending
   again won't fix it. Remove permanently.

5. **Not updating CRM with verification status.** Verification without recording
   the result means the data decays silently. Update CRM fields immediately.

## Related Skills

- **email-finding**: Find emails before verifying them
- **email-deliverability**: Full deliverability strategy beyond verification
- **list-building**: Build and maintain clean prospect lists
- **deliverability-monitoring**: Ongoing monitoring of bounce rates and reputation

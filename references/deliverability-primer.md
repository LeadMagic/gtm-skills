# Email Deliverability Reference

Shared reference for deliverability skills in the GTM Skills library.

## DNS Authentication (Non-Negotiable)

Every sending domain must have all three:

- **SPF** — Authorizes which servers can send mail for the domain
- **DKIM** — Cryptographic signature proving the email wasn't altered in transit
- **DMARC** — Policy telling receivers what to do with unauthenticated mail (`p=reject` eventually, start with `p=none`)

Without all three, major inbox providers (Google, Microsoft) will route your mail to spam or reject it outright.

## Warmup Strategy

New domains and mailboxes need 2-4 weeks of warmup before cold sending.

Week 1: 5-10 emails/day to known-engaging addresses
Week 2: 15-25 emails/day, gradually introducing colder contacts
Week 3: 30-40 emails/day, mixing warm and cold
Week 4: 40-50 emails/day, full cold sending

Never exceed 50 emails/day per mailbox for cold outreach. Higher volumes trigger spam filters regardless of authentication.

## Bounce Rate Targets

- Target: Under 2% bounce rate
- Warning: 2-5% — investigate and fix
- Critical: Over 5% — pause sending, identify root cause

Bounces above 5% trigger automated spam filtering at Google and Microsoft. Recovery takes weeks to months.

## Sending Domain Isolation

Never send cold email from your primary business domain. A reputation hit on your primary domain takes your transactional email (password resets, invoices, notifications) down with it.

Buy 3-5 secondary domains for cold outreach. Rotate mailboxes across them. If one domain's reputation degrades, others continue operating.

## Inbox Rotation

Distribute sends across multiple mailboxes and domains. A typical setup:

- 3 sending domains
- 2-3 mailboxes per domain
- 30-50 sends/day per mailbox
- Total capacity: 180-750 sends/day

Monitor per-mailbox reputation independently. Pause underperforming mailboxes before they drag down the domain.

## Common Pitfalls

1. **Sending from primary domain.** One spam complaint poisons your entire business email.
2. **Skipping warmup.** New domains sent at full volume get blacklisted within 48 hours.
3. **Unverified emails in sequences.** 5%+ bounce rate triggers spam filters. Always verify before sending.
4. **HTML-heavy emails.** Plain text or lightly formatted HTML consistently outperforms heavily designed templates in cold outreach deliverability. Spam filters penalize image-heavy, multi-link emails.
5. **No DMARC reporting.** Set up DMARC aggregate reports to see who's sending on your behalf and catch spoofing attempts.

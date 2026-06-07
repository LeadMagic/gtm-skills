---
name: domain-infrastructure
description: >-
  Designs and provisions the domain and mailbox infrastructure for cold
  email outreach: secondary domains, mailbox setup (Google Workspace, M365,
  Zoho), DNS authentication records, inbox rotation, and primary domain
  isolation. Use when the user asks to set up sending domains, provision
  mailboxes, configure DNS for cold email, or plan domain rotation for
  outbound. Activates on phrases like "set up sending domains," "buy
  secondary domains," "provision mailboxes," "configure email for cold
  outreach," or "domain rotation plan."
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: outbound
  tags: [domain, infrastructure, email, mailboxes, DNS, provisioning]
  related_skills:
    - email-deliverability
    - sending-platforms
    - cold-email-strategy
  frameworks: []
---

# Domain Infrastructure

## Overview

Cold email deliverability depends entirely on infrastructure decisions made
before the first email is sent. The domain names, mailbox providers, DNS
configuration, and rotation strategy form the foundation on which all
outbound rests. A poor infrastructure setup will produce poor deliverability
regardless of copy quality or targeting precision.

This skill produces a complete domain infrastructure plan: which secondary
domains to register, how to provision mailboxes across providers (Google
Workspace, Microsoft 365, Zoho), DNS authentication configuration for each
domain, inbox rotation schedules, and a monitoring framework to detect
degradation before it impacts campaigns.

The non-obvious rule: never send cold email from your primary business domain.
Your primary domain carries your transactional email (password resets,
invoices, customer notifications, support tickets) and your corporate email
(sales, support, executives). A reputation hit on the primary domain from
cold email complaints or bounces takes down ALL of those functions
simultaneously. Cold email must operate on entirely separate, isolated
infrastructure.

## When to Use

- User says "set up domains for cold email" or "buy sending domains" →
  activate this skill
- User asks "how many domains do I need" or "how many mailboxes per domain" →
  activate this skill
- User wants to "provision mailboxes for outreach" or "set up Google
  Workspace for outbound" → activate this skill
- User mentions "DNS configuration for email," "inbox rotation," or
  "primary domain isolation" → activate this skill
- User asks "should I use Google or Microsoft for cold email" or
  "Zoho vs Gmail for outreach" → activate this skill
- User wants to "scale sending capacity" or "add more mailboxes" →
  activate this skill

Do NOT use for:
- Configuring SPF/DKIM/DMARC records → use `email-deliverability`
  (domain-infrastructure tells you WHICH domains and mailboxes;
  email-deliverability configures authentication ON them)
- Selecting a sending platform → use `sending-platforms`
- Designing email sequences → use `cold-email-strategy`

## Authoritative Foundations

This skill draws from the following established methodologies:

- **Google Workspace Admin Best Practices** — Documentation on mailbox
  provisioning, sending limits, and security configuration. Google Workspace
  is the most common cold email mailbox provider due to deliverability
  reputation and API access for sending platforms.

- **Microsoft 365 Exchange Online** — Admin documentation on mailbox
  provisioning, outbound spam policies, and sending limits. M365 is second
  most common. Higher reputation barrier for new tenants but stronger
  deliverability once established.

- **Zoho Mail Admin** — Alternative provider for cost-conscious setups.
  Lower per-mailbox cost but lower default sending limits and less API
  maturity for sending platform integration.

- **ICANN / Domain Registration Best Practices** — Guidelines on domain
  registration, WHOIS privacy, and domain age considerations. Domain age is
  a reputation factor — newly registered domains (under 90 days) face higher
  scrutiny from inbox providers.

- **Validity / Return Path — Sender Score** — Domain-level reputation scoring
  that informs domain rotation decisions. A domain with a Sender Score below
  70 should be rotated out of active sending.

## Prerequisites

- Access to a domain registrar (Namecheap, GoDaddy, Google Domains, Cloudflare
  Registrar, Porkbun, etc.)
- Budget for domains ($10-15/year per domain) and mailboxes (Google Workspace
  ~$6-18/user/month, M365 ~$6-22/user/month, Zoho ~$1-4/user/month)
- DNS management access (usually through the registrar or Cloudflare)
- Optional: LeadMagic API key for pre-send email verification to integrate
  with sending infrastructure
- Reference files: `references/deliverability-primer.md` for sending limits
  and domain isolation best practices

## Step-by-Step Process

### Phase 1: Intake

Gather the following from the user. Ask all questions at once:

1. **Primary business domain:** What is the domain used for corporate email,
   website, and transactional email? This will be left untouched — we only
   configure secondary domains.

2. **Target sending volume:** How many total emails per day do you need to
   send? This determines how many mailboxes and domains are needed.

3. **Budget:** What's the monthly budget for domains and mailboxes? This
   determines provider choice and scale.

4. **Current setup:** Any existing secondary domains or mailboxes already
   in use? If yes, how old are they, what's their sending history?

5. **Preferred providers:** Any existing relationship with Google Workspace,
   M365, or Zoho? Do you prefer one over the others?

6. **Domain registrar:** Which registrar do you use? Do you use Cloudflare
   for DNS? These affect how DNS records are managed.

7. **Sending platform:** Which platform will send the emails (Smartlead,
   Instantly, Salesforge, Apollo)? This affects mailbox integration
   requirements.

8. **Warmup plan:** Will you warm up manually, use the sending platform's
   warmup, or both? This affects the provisioning timeline.

9. **Geographic requirements:** Any data residency requirements (GDPR
   in EU, data localization laws)? This affects provider and region selection.

### Phase 2: Research

Before provisioning, research the domain landscape:

1. **Primary domain reputation check:** Verify the primary domain has a clean
   reputation. Even though we won't send cold from it, a damaged primary
   domain reputation can affect secondary domains if they're too closely
   connected (same WHOIS, same IP, same brand name in domain). Check:
   - Google Postmaster Tools for the primary domain
   - MXToolbox blacklist check for the primary domain
   - Any existing SPF/DKIM/DMARC configuration

2. **Domain naming strategy:** Research available domain names. The domain
   name DOES matter for deliverability. Avoid:
   - Exact match of primary brand name (too obvious, links to primary domain)
   - Hyphenated domains (associated with spam)
   - Very long domains (over 20 characters)
   - ccTLDs for non-geographic targeting (.co, .io are fine; .tk, .ml are not)
   - Domains registered in the last 24 hours (need 2+ weeks of age before
     sending, ideally 90+ days)

   Good naming patterns:
   - `[brand][variant].com` — e.g., `getbrand.com`, `brandhq.com`, `trybrand.com`
   - `[brand][descriptor].com` — e.g., `brandops.com`, `brandteam.com`
   - Generic-but-professional: `[industry][term].com` — e.g., `saaescalate.com`

3. **Provider pricing comparison (current market):**
   - Google Workspace Business Starter: ~$7.20/user/month (annual)
   - Google Workspace Business Standard: ~$14.40/user/month (annual)
   - Microsoft 365 Business Basic: ~$6.00/user/month (annual)
   - Microsoft 365 Business Standard: ~$12.50/user/month (annual)
   - Zoho Mail Lite: ~$1.00/user/month (annual)
   - Zoho Mail Premium: ~$4.00/user/month (annual)

   Note: prices subject to change. Verify current pricing before quoting.

### Phase 3: Execution

#### Step 1: Calculate Capacity Requirements

Determine how many domains and mailboxes are needed:

Base formula: `mailboxes_needed = ceil(daily_target_volume / 40)`

Explanation: 40 emails/day per mailbox is the recommended safe volume for
sustained sending. You can push to 50 but it leaves no headroom. Using 40
allows for reply handling and minor volume spikes without crossing the limit.

Domain allocation:
- 3-5 sending domains recommended for redundancy
- 2-3 mailboxes per domain maximum
- No domain should carry more than 3 mailboxes — if one mailbox triggers a
  spam complaint, the domain reputation affects all mailboxes on that domain.
  Limiting to 2-3 per domain contains the blast radius.

Examples:
- 80 emails/day: 2 mailboxes, 1-2 domains
- 200 emails/day: 5 mailboxes, 2-3 domains
- 400 emails/day: 10 mailboxes, 3-5 domains
- 800 emails/day: 20 mailboxes, 4-5+ domains (consider dedicated sending IPs
  at this scale)

#### Step 2: Domain Registration

For each domain:

1. Register through your preferred registrar.
2. Enable WHOIS privacy protection (free on most registrars). Public WHOIS
   with matching registrant information across domains links them together,
   which inbox providers can detect.
3. Set auto-renew. A forgotten renewal that lets a domain lapse will break
   sequences and potentially create a deliverability event.
4. Add to DNS management (Cloudflare is recommended for fast DNS propagation
   and API access).
5. If using Cloudflare: enable DNSSEC for additional trust signaling.
6. Document: domain name, registrar, registration date, renewal date, DNS
   provider, nameservers.

Domain age note: If possible, register domains at least 2 weeks before you
need to send. 90+ days of age before cold sending is ideal. A domain
registered today and sending cold email tomorrow is a strong spam signal.

#### Step 3: Mailbox Provisioning (Google Workspace)

For each mailbox on a Google Workspace domain:

1. Sign up for Google Workspace for the domain. If you already have a
   Workspace tenant on one secondary domain, you can add additional domains
   as domain aliases (cheaper) or separate tenants (better isolation).

2. Create user accounts for each mailbox:
   - Use professional naming: `[firstname]@[domain]`, `[firstinitial][lastname]@[domain]`,
     or role-based: `outreach1@[domain]`, `hello@[domain]`
   - Never use names like `email1@`, `send1@`, `cold1@` — these are spam
     signals detected by inbox providers
   - Set up a professional display name and profile photo for each account
   - Configure signature: first name only, no title/company logo

3. Configure security:
   - Enable 2FA on all accounts (platform integrations use app passwords or
     OAuth, not raw passwords)
   - Create app passwords for each mailbox that the sending platform will use
   - Disable IMAP/POP if not needed (reduce attack surface)
   - Set up forwarding to a monitoring inbox for reply handling

4. Google Workspace-specific sending considerations:
   - Google Workspace has a sending limit of 2,000 recipients per day per
     account, but cold email reputation management requires staying at 30-50
   - Google enforces the limit based on the account's reputation, not just
     the raw number
   - New accounts (under 30 days) face stricter rate limiting

5. Document for each mailbox: email address, display name, app password
   (store securely), login email, 2FA method, forwarding configuration.

#### Step 3b: Mailbox Provisioning (Microsoft 365)

For each mailbox on an M365 domain:

1. Sign up for Microsoft 365 Business Basic for the domain.
2. Create user accounts following the same naming conventions as Google.
3. Configure security: MFA, app passwords for platform integration.
4. M365-specific considerations:
   - Microsoft's outbound spam filtering is aggressive by default — new
     tenants may be restricted to minimal outbound volume
   - The "Restrict sending to internal recipients only" policy on new tenants
     must be explicitly disabled
   - Microsoft has a Recipient Rate Limit of 10,000 recipients/day, but
     practical cold limits are same as Google (30-50)
   - Outlook deliverability is often better for B2B reaching Microsoft-heavy
     organizations

#### Step 3c: Mailbox Provisioning (Zoho Mail)

For each mailbox on a Zoho domain:

1. Sign up for Zoho Mail (Lite or Premium plan).
2. Create user accounts.
3. Zoho-specific considerations:
   - Lower per-mailbox cost ($1-4/month vs $6-18)
   - Lower default sending limits: 250-500/day depending on plan, but cold
     email requires same 30-50/day discipline
   - Less mature API for sending platform integration — confirm your platform
     supports Zoho before committing
   - Good for budget-constrained setups or supplementary mailboxes

#### Step 4: DNS Configuration per Domain

For each domain, before sending a single email:

A. **SPF record:** Create a TXT record at the root that authorizes the
   mailbox provider (Google, M365, Zoho) AND the sending platform:
   ```
   v=spf1 include:_spf.google.com include:_spf.[sendingplatform].com -all
   ```
   (Adjust includes based on provider and platform.)

B. **DKIM:** Generate DKIM keys through the mailbox provider's admin console
   and add the DNS records. Use a unique selector per provider:
   - Google: `google._domainkey`
   - M365: `selector1._domainkey` and `selector2._domainkey`
   - Zoho: `zoho._domainkey`

C. **DMARC:** Add the DMARC record at `_dmarc.[domain]`:
   ```
   v=DMARC1; p=none; rua=mailto:dmarc@[yourdomain].com; fo=1;
   ```
   (Monitoring mode initially; progress to reject after warmup.)

D. **Custom tracking domain (for sending platforms):** If using Smartlead,
   Instantly, or similar platforms, set up a CNAME record for click/open
   tracking:
   ```
   track.[domain] CNAME [platform-tracking-endpoint]
   ```
   This prevents the platform's shared tracking domain from being flagged
   and dragging down your deliverability.

E. **Verify DNS propagation:** After adding records, verify with:
   - `dig TXT [domain]` for SPF
   - `dig TXT google._domainkey.[domain]` for DKIM
   - `dig TXT _dmarc.[domain]` for DMARC
   - MXToolbox or similar for comprehensive verification

#### Step 5: Design Inbox Rotation

Inbox rotation distributes sending across mailboxes to maintain consistent
volume without any single mailbox exceeding limits:

Daily rotation pattern (example for 5 mailboxes sending 200/day):
- Mailbox 1: 40 sends (prospects 1-40)
- Mailbox 2: 40 sends (prospects 41-80)
- Mailbox 3: 40 sends (prospects 81-120)
- Mailbox 4: 40 sends (prospects 121-160)
- Mailbox 5: 40 sends (prospects 161-200)

Rotation rules:
- Each prospect is assigned to a single mailbox for the entire sequence.
  Do not rotate a prospect across mailboxes — this breaks thread context
  and looks like a deliverability trick to inbox providers.
- Even distribution: each mailbox gets the same daily volume (±10%).
- Time zone alignment: if possible, assign prospects to mailboxes in their
  time zone so sends happen during the prospect's business hours.
- Reputation-based redistribution: if one mailbox shows degraded engagement,
  temporarily redirect a portion of its volume to other mailboxes while
  investigating.

#### Step 6: Set Up Monitoring

Before sending, set up monitoring for every domain and mailbox:

1. **Google Postmaster Tools:** Register every domain. This is free and
   provides the best deliverability data for Gmail recipients (~45% of B2B).

2. **Microsoft SNDS:** Register every sending IP. Covers Outlook/Hotmail
   recipients (~20% of B2B).

3. **MXToolbox monitoring:** Set up automated blacklist checks for every
   domain. Free tier allows weekly monitoring.

4. **Sending platform deliverability dashboard:** Configure in-platform
   deliverability monitoring (Smartlead's Deliverability Tab, Instantly's
   Health Score, etc.).

5. **Internal tracking sheet:** Create a spreadsheet tracking per-mailbox
   and per-domain metrics: sends, opens, replies, bounces, complaints,
   unsubscribes. Review weekly.

### Phase 4: Delivery

Deliver a complete infrastructure plan:

1. **Domain Inventory:** All registered domains with registration dates,
   registrars, DNS providers, and renewal dates.

2. **Mailbox Inventory:** Every mailbox with email address, provider, plan,
   sending limit, and integration status.

3. **DNS Configuration Map:** Per-domain DNS records (SPF, DKIM, DMARC, MX,
   tracking CNAME) in copy-paste format for the DNS console.

4. **Rotation Schedule:** Daily sending allocation per mailbox with time
   zone assignments.

5. **Scaling Plan:** How to add more capacity when needed (additional
   mailboxes within existing domains vs new domains).

6. **Cost Projection:** Monthly and annual cost breakdown by provider.

## Output Format

```markdown
# Domain Infrastructure Plan for [Company]

## Capacity Calculation
- Daily target volume: [X] emails
- Mailboxes needed: [N] (at 40/day/mailbox)
- Domains needed: [N] (2-3 mailboxes per domain)

## Domain Inventory
| Domain | Registrar | Registered | Renewal Date | DNS Provider | Age |
|--------|-----------|------------|--------------|--------------|-----|
| [domain1] | [registrar] | [date] | [date] | [provider] | [N days] |

## Mailbox Inventory
| Email | Domain | Provider | Plan | Cost/mo | Platform Connected | Status |
|-------|--------|----------|------|---------|--------------------|--------|
| [email] | [domain] | Google/M365/Zoho | [plan] | $[X] | [yes/no] | [warm/active] |

## DNS Configuration — [Domain]
### SPF
`v=spf1 include:[provider] include:[platform] -all`

### DKIM
Selector: `[provider]._domainkey`
Value: `[dkim_value]`

### DMARC
`v=DMARC1; p=none; rua=mailto:dmarc-reports@[primary-domain].com; fo=1;`

### Tracking CNAME
`track.[domain] CNAME [platform-endpoint]`

[Repeat DNS section for each domain]

## Inbox Rotation Schedule
| Mailbox | Daily Volume | Time Zone | Prospect Assignment |
|---------|-------------|-----------|---------------------|
| [email1] | 40 | EST | Prospects 1-40 |
| [email2] | 40 | EST | Prospects 41-80 |

## Monitoring Configuration
| Resource | Tool | Status | Alert Threshold |
|----------|------|--------|-----------------|
| [domain] | Google Postmaster | [registered/pending] | Spam rate >0.1% |
| [IP] | Microsoft SNDS | [registered/pending] | Complaint >0.3% |
| [domain] | MXToolbox Blacklist | [active] | Any listing |

## Scaling Plan
- Add mailbox: when [condition]
- Add domain: when [condition]
- Dedicated IP: when [condition]

## Cost Summary
| Resource | Monthly | Annual |
|----------|---------|--------|
| Domains (N × $12/yr) | $[X] | $[X] |
| Google Workspace (N × $7.20/mo) | $[X] | $[X] |
| M365 (N × $6.00/mo) | $[X] | $[X] |
| Zoho (N × $1.00/mo) | $[X] | $[X] |
| Total | $[X]/mo | $[X]/yr |
```

## Quality Check

Before delivering, verify:

- [ ] Is the primary business domain completely excluded from cold sending?
- [ ] Are 3-5 secondary domains planned (or scaled proportionally to volume)?
- [ ] Are there 2-3 mailboxes per domain maximum?
- [ ] Is the daily volume per mailbox set to 30-50 (recommended 40)?
- [ ] Are domain names professional and not spam-signaling?
- [ ] Is WHOIS privacy enabled on all domains?
- [ ] Are DNS records provided in copy-paste format for each domain?
- [ ] Does DMARC start in monitoring mode (`p=none`)?
- [ ] Is there a custom tracking domain configured per domain?
- [ ] Is Google Postmaster Tools registration included?
- [ ] Is blacklist monitoring set up?
- [ ] Is the cost projection complete and realistic?
- [ ] Is the scaling plan defined with trigger conditions?
- [ ] Are 2FA and app passwords configured for all mailboxes?

## Common Pitfalls

1. **Sending from the primary domain.** This is the cardinal sin of domain
   infrastructure. A single spam complaint on the primary domain takes down
   all corporate and transactional email. Never, under any circumstances,
   send cold email from your primary domain.

2. **Too few domains.** Running all mailboxes on a single domain means one
   reputation event kills all sending capacity. 3 domains is the minimum
   for production outbound. 5 is better for volume above 300/day.

3. **Too many mailboxes per domain.** When one mailbox on a domain gets
   flagged for spam, the domain reputation drops — affecting every mailbox
   on that domain. Limiting to 2-3 per domain contains the blast radius.

4. **Spammy mailbox names.** `email-marketing@`, `sales-outreach@`, `cold1@`
   — inbox providers flag these patterns. Use professional,
   human-looking email addresses.

5. **No WHOIS privacy.** Matching WHOIS registrant info across domains
   creates an easily identifiable pattern that inbox providers can use to
   link your domains. A reputation hit on one domain can cascade.

6. **Sending from brand-new domains.** A domain registered yesterday and
   sending cold email today is a strong spam signal. Inbox providers track
   domain age. 2 weeks minimum before sending, 90+ days ideal.

7. **No tracking domain customization.** Using the sending platform's
   default tracking domain puts your deliverability at the mercy of every
   other user on that shared domain. A spammer on the shared domain
   damages your reputation.

8. **No monitoring before sending.** Setting up domains and mailboxes without
   simultaneously setting up Google Postmaster Tools, SNDS, and blacklist
   monitoring means you're flying blind. You won't know deliverability is
   broken until open rates collapse.

9. **Rotating prospects across mailboxes mid-sequence.** Moving a prospect
   from mailbox A to mailbox B in the middle of a sequence breaks thread
   context, resets engagement history, and looks suspicious. Each prospect
   stays with one mailbox for the entire sequence.

10. **Ignoring DNS propagation time.** DNS changes can take up to 48 hours
    to propagate globally. Always verify DNS records after 48 hours. Never
    start sending immediately after adding DNS records.

## Provider Decision Matrix

| Factor | Google Workspace | Microsoft 365 | Zoho Mail |
|--------|-----------------|---------------|-----------|
| Deliverability (Gmail) | Excellent | Good | Good |
| Deliverability (Outlook) | Good | Excellent | Good |
| Per-mailbox cost | $$ | $$ | $ |
| API maturity | Excellent | Good | Fair |
| Platform integrations | All | Most | Some |
| Warmup ease | Good | Good | Good |
| Admin complexity | Medium | High | Low |
| Best for | General B2B | Microsoft-heavy prospects | Budget setups |

For most B2B outbound, Google Workspace is the default choice. M365 is
preferred when a high percentage of targets use Outlook/Office 365. Zoho
is a cost-effective supplement for additional domains or budget-constrained
setups.

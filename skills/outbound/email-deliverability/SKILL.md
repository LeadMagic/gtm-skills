---
name: email-deliverability
description: >-
  Sets up and monitors email deliverability infrastructure including SPF,
  DKIM, DMARC configuration, warmup strategy, reputation monitoring, bounce
  and complaint handling, and ongoing deliverability health. Use when the
  user asks about email deliverability, SPF/DKIM/DMARC setup, warmup
  schedules, bounce rate troubleshooting, spam placement issues, or domain
  reputation. Activates on phrases like "improve deliverability," "emails
  going to spam," "warmup my domain," "DNS setup for cold email,"
  "bounce rate," or "DMARC setup."
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: outbound
  tags: [email, deliverability, SPF, DKIM, DMARC, warmup, reputation]
  related_skills:
    - domain-infrastructure
    - sending-platforms
    - cold-email-strategy
  frameworks: []
---

# Email Deliverability

## Overview

Deliverability is the foundation on which all outbound email rests. Without it,
the best copy, the most sophisticated sequence, and the highest-quality list
produce zero pipeline — because the email never reaches the inbox. The inbox
placement rate is the single most important metric in cold email, and it is
entirely a function of technical configuration plus ongoing reputation
management.

This skill produces a deliverability setup and monitoring plan: DNS
authentication configuration (SPF, DKIM, DMARC), a 4-week warmup schedule
with per-week volume targets, reputation monitoring protocols, bounce and
complaint handling procedures, and a deliverability health dashboard
definition. It covers the full lifecycle from initial setup through ongoing
maintenance.

The non-obvious rule: most deliverability problems are not technical. They are
behavioral. Sending too many emails too fast, sending to unverified addresses,
sending from a primary domain, or ignoring bounce spikes will defeat even
perfect DNS configuration. Deliverability is 30% setup and 70% discipline.

CRITICAL: Never describe validation internals. Email validation is a blackbox
subject — this skill covers the strategy of validation (when to validate,
how to handle results) but NEVER describes how validation algorithms work.

## When to Use

- User says "set up SPF/DKIM/DMARC" or "configure DNS for email" →
  activate this skill
- User asks "how do I warm up a domain" or "what's the warmup schedule" →
  activate this skill
- User reports "my emails are going to spam" or "open rates dropped" →
  activate this skill
- User asks about "bounce rate targets," "complaint handling," or
  "reputation monitoring" → activate this skill
- User wants to "check domain reputation" or "set up DMARC monitoring" →
  activate this skill
- User asks "how many emails per day per mailbox" → activate this skill

Do NOT use for:
- Buying and configuring secondary domains and mailboxes →
  use `domain-infrastructure`
- Selecting a sending platform → use `sending-platforms`
- Designing the email sequence → use `cold-email-strategy`
- Writing email copy → use `cold-email-copywriting`

## Authoritative Foundations

This skill draws from the following established methodologies:

- **Google Postmaster Tools** — The authoritative source for Gmail deliverability
  data. Provides domain-level spam rate, IP reputation, domain reputation,
  feedback loop data, authentication status, and encryption status. Every
  sending domain must be registered here. Google processes ~45% of B2B email
  — if your Gmail deliverability is broken, your outbound is broken.

- **Microsoft SNDS (Smart Network Data Services)** — The equivalent for
  Outlook/Hotmail/Office 365. Provides IP-level reputation data, spam
  complaint rates, and trap hits. Microsoft processes ~20% of B2B email.
  Combined with Google Postmaster Tools, these cover ~65% of all B2B inboxes.

- **M³AAWG (Messaging, Malware, Mobile Anti-Abuse Working Group)** — Industry
  best practices for email sending. Their guidelines inform the volume limits,
  authentication requirements, and complaint thresholds used by all major
  inbox providers and email service providers.

- **Validity / Return Path** — Email certification and reputation data.
  Industry-standard Sender Score (0-100) used by many inbox providers as a
  reputation input. Sender Score above 90 is good; below 70 is concerning;
  below 50 will cause widespread blocking.

- **RFC 7208 (SPF), RFC 6376 (DKIM), RFC 7489 (DMARC)** — The IETF standards
  that define these protocols. This skill describes compliant configurations,
  not every possible variation.

## Prerequisites

- Run `domain-infrastructure` first — you need domains and mailboxes to
  configure deliverability for
- Required user inputs: sending domains, mailbox credentials/providers,
  current sending volume if already active
- Access required: DNS management console for each sending domain, admin
  access to Google Workspace / M365 / Zoho for mailbox configuration
- Optional: LeadMagic API key for pre-send email verification (verify
  addresses before adding to sequences to maintain low bounce rates)
- Reference files: `references/deliverability-primer.md` for detailed
  warmup schedules and sending limits

## Step-by-Step Process

### Phase 1: Intake

Gather the following from the user. Ask all questions at once:

1. **Sending domains:** List all domains being used for cold email. Confirm
   these are SECONDARY domains — never the primary business domain.

2. **Mailbox details:** For each domain, how many mailboxes? Which provider
   (Google Workspace, M365, Zoho, other)? Are they already sending or new?

3. **Current volume:** How many emails per day per mailbox currently? If
   already sending, what's the current bounce rate, spam complaint rate,
   open rate, reply rate?

4. **DNS access:** Who controls DNS? Do they have access to add SPF, DKIM,
   DMARC records? Which DNS provider?

5. **Current authentication status:** Are SPF, DKIM, DMARC already configured?
   If yes, what are the current records? If not, this is step one.

6. **Sending platform:** Which platform (Smartlead, Instantly, Salesforge,
   Apollo, other)? Different platforms have different warmup capabilities
   and authentication requirements.

7. **Deliverability issues:** Any known problems? Emails going to spam?
   Blacklisting? Sudden open rate drops? Specific domains blocking?

8. **Compliance requirements:** GDPR, CAN-SPAM, CASL, other regulations?
   This affects list practices and unsubscribe handling.

### Phase 2: Research

Before configuring, audit the current state:

1. **DNS audit:** Check current SPF, DKIM, DMARC records for all sending
   domains. Use `dig TXT [domain]` for SPF, `dig TXT [selector]._domainkey.[domain]`
   for DKIM, `dig TXT _dmarc.[domain]` for DMARC. Document what exists
   and what's missing.

2. **Blacklist check:** Run all sending IPs and domains through MXToolbox,
   Spamhaus, Barracuda, and SURBL blacklists. If any domain or IP is listed,
   that's the first priority to address before sending resumes.

3. **Reputation check:** If domains have been sending, check Google
   Postmaster Tools for domain reputation, spam rate, and feedback loop.
   Check Microsoft SNDS for IP reputation. Check Sender Score (Validity)
   for overall score. Document the baseline.

4. **Bounce analysis:** If currently sending, pull bounce data for the last
   30 days. Categorize bounces: hard bounce (invalid address), soft bounce
   (mailbox full, server issue), block (spam filter rejection). Calculate
   rates per mailbox and per domain.

5. **Spam complaint analysis:** Pull complaint data from the sending platform
   and Google Postmaster Tools. Industry target: under 0.1% complaint rate
   (1 complaint per 1,000 sends). Above 0.3% triggers Google spam filtering
   regardless of authentication.

6. **Inbox placement test:** If possible, use GlockApps, MailGenius, or
   Mail-Tester to send test emails and see where they land (inbox, spam,
   promotions, missing) across Google, Microsoft, Yahoo, and other providers.

### Phase 3: Execution

#### Step 1: Configure SPF

SPF (Sender Policy Framework) tells receiving servers which IP addresses and
hostnames are authorized to send mail on behalf of your domain.

Create/update the TXT record at the domain root:

For dedicated sending IPs (recommended for high volume):
```
v=spf1 ip4:[your_sending_ip] -all
```

For sending platforms with shared IPs (most SMB outbound):
```
v=spf1 include:[platform_spf_host] -all
```

Common platform SPF includes:
- Google Workspace: `include:_spf.google.com`
- M365: `include:spf.protection.outlook.com`
- Smartlead: `include:_spf.smartlead.ai`
- Instantly: `include:_spf.instantly.ai`
- Salesforge: `include:spf.salesforge.ai`

Rules:
- Use `-all` (hard fail) for cold sending domains, not `~all` (soft fail).
  You want receiving servers to reject unauthorized mail, not mark it as
  suspicious.
- One SPF record per domain. If you already have an SPF record, merge the
  includes into a single record.
- No more than 10 DNS lookups per SPF record (the include chain counts).
  If you exceed this, use subdomain-specific SPF records.
- The `+` or `-` qualifier on `all` must be the last mechanism.

#### Step 2: Configure DKIM

DKIM (DomainKeys Identified Mail) adds a cryptographic signature to each
email, proving the message wasn't altered in transit.

For Google Workspace:
1. In Google Admin console, go to Apps → Google Workspace → Gmail →
   Authenticate email.
2. Generate a DKIM key for your domain. Google provides the DNS record.
3. Add the TXT record at `google._domainkey.[domain]` with the value
   Google provides.
4. After DNS propagation (up to 48 hours), click "Start Authentication"
   in Google Admin.

For M365:
1. In Microsoft 365 Defender portal, go to Email & Collaboration →
   Policies & Rules → Threat Policies → Email Authentication Settings → DKIM.
2. Select your domain, enable DKIM, and copy the CNAME records.
3. Add CNAME records: `selector1._domainkey.[domain]` and
   `selector2._domainkey.[domain]` pointing to the Microsoft-provided targets.

For Zoho:
1. In Zoho Mail Admin, go to Email Authentication → DKIM.
2. Generate keys and add the provided TXT record.

Key selection: Use a distinct DKIM selector for each sending platform
(e.g., `google._domainkey`, `smartlead._domainkey`). This allows independent
key rotation without breaking other services.

DKIM key length: 2048-bit minimum. 1024-bit keys are deprecated and
increasingly rejected by major inbox providers.

#### Step 3: Configure DMARC

DMARC (Domain-based Message Authentication, Reporting and Conformance) tells
receiving servers what to do when SPF or DKIM fails and provides aggregate
reports on authentication results.

Create the TXT record at `_dmarc.[domain]`:

Starting configuration (monitoring mode):
```
v=DMARC1; p=none; rua=mailto:dmarc-reports@[yourdomain].com; ruf=mailto:dmarc-forensics@[yourdomain].com; fo=1;
```

After 2-4 weeks of monitoring with zero issues, move to quarantine:
```
v=DMARC1; p=quarantine; pct=100; rua=mailto:dmarc-reports@[yourdomain].com;
```

Eventual target (full protection):
```
v=DMARC1; p=reject; pct=100; rua=mailto:dmarc-reports@[yourdomain].com;
```

Rules:
- Start with `p=none` — you need monitoring data before enforcement.
- Set up `rua` to a real email address that receives DMARC aggregate reports
  (XML files). Use services like DMARCIAN, Postmark DMARC, or Valimail to
  parse these into human-readable dashboards.
- After 2-4 weeks of clean monitoring (no legitimate mail failing auth),
  move to `p=quarantine` for another 2-4 weeks.
- `p=reject` is the goal but only after full confidence. A misconfigured
  reject policy will silently discard legitimate mail.
- `pct=100` means apply the policy to 100% of mail. Use `pct=25` or
  `pct=50` to gradually roll out enforcement.

#### Step 4: Design the Warmup Schedule

New domains and mailboxes need 2-4 weeks of warmup before sending cold
email at full volume. Warmup builds a positive reputation by sending small
volumes to known-engaging addresses, establishing a pattern of high engagement
before introducing colder contacts.

Week 1 — Foundation (Days 1-7):
- Daily volume: 5-10 emails per mailbox
- Recipient composition: 100% warm (internal team, friends, colleagues,
  test accounts) who will open and reply
- Sending pattern: spread across the day, not all at once
- Goal: establish initial engagement signal

Week 2 — Gradual Increase (Days 8-14):
- Daily volume: 15-25 emails per mailbox
- Recipient composition: 70% warm, 30% lukewarm (known contacts, past
  conversations, opted-in lists)
- Sending pattern: spread across business hours
- Goal: build volume tolerance while maintaining high engagement

Week 3 — Introducing Cold (Days 15-21):
- Daily volume: 30-40 emails per mailbox
- Recipient composition: 50% warm/lukewarm, 50% cold (verified addresses,
  Tier 3 personalization, highest-quality leads first)
- Sending pattern: normal business hours
- Goal: transition to cold sending without engagement cliff

Week 4 — Full Volume (Days 22-28):
- Daily volume: 40-50 emails per mailbox
- Recipient composition: 20% warm/lukewarm, 80% cold
- Sending pattern: optimized for recipient time zone
- Goal: sustained reputation at full capacity

Important: If at any point during warmup the bounce rate exceeds 2% or the
spam complaint rate exceeds 0.1%, pause the escalation and stay at the
current volume until resolved.

Using platform-based warmup (Smartlead, Instantly, Salesforge): Most platforms
include automated warmup that sends to their network of warmup addresses.
This is a supplement, not a replacement for the manual warmup above.
Automated warmup builds base reputation; manual warmup with real contacts
builds domain-specific engagement patterns.

NEVER use automated warmup as the sole warmup method. The warmup network
addresses are known to inbox providers — engagement with them is weighted
lower than engagement with real, diverse contacts.

#### Step 5: Set Up Reputation Monitoring

Ongoing monitoring is not optional. Set up the following:

1. **Google Postmaster Tools:** Register every sending domain. Check weekly
   at minimum. Key metrics to monitor:
   - Spam rate: must stay under 0.1% (target <0.05%)
   - Domain reputation: must stay "high" or "medium-high"
   - Feedback loop: watch for complaint spikes
   - Authentication: all DKIM/SPF should show "pass"

2. **Microsoft SNDS:** Register every sending IP. Check weekly. Watch for:
   - Spam complaint rate: under 0.1%
   - Trap hits: zero is the only acceptable number
   - Block status: any block requires immediate investigation

3. **Blacklist monitoring:** Use MXToolbox or similar to check major
   blacklists weekly. Automate with alerts. Blacklists to monitor:
   - Spamhaus (SBL, XBL, PBL)
   - Barracuda
   - SURBL
   - SpamCop
   - Invaluement
   - UCEPROTECT

4. **Sending platform metrics:** Monitor in-platform deliverability metrics
   daily:
   - Delivery rate (target: >98%)
   - Bounce rate (target: <2%, warning at 3%, critical at 5%)
   - Spam complaint rate (target: <0.1%, critical at 0.3%)
   - Open rate trends (a sudden 30%+ drop signals deliverability issue)
   - Inbox placement rate (if platform provides)

5. **DMARC aggregate reports:** Parse the XML reports from `rua` to track:
   - Which IPs are sending on your behalf (authorized and unauthorized)
   - SPF and DKIM pass/fail rates
   - Spoofing attempts (someone else sending as your domain)
   - Gradual DKIM alignment failures (key rotation issues)

#### Step 6: Establish Bounce and Complaint Handling Procedures

**Bounce handling:**

Hard bounces (permanent failure — invalid address, domain doesn't exist):
- Immediately remove from all active sequences.
- Suppress the address permanently (or at minimum 12 months).
- If hard bounce rate per domain exceeds 5% in any 24-hour period, pause
  all sending from that domain and investigate.

Soft bounces (temporary failure — mailbox full, server issue, rate limit):
- Pause contact for 7 days.
- After 3 consecutive soft bounces, treat as hard bounce and suppress.
- If soft bounce rate exceeds 10%, investigate sending infrastructure.

**Complaint handling:**

- Every spam complaint is an emergency. One complaint per 1,000 sends
  (0.1%) is already at the warning threshold.
- When a complaint is received: immediately remove the contact from all
  sequences, suppress permanently, and add to a "do not contact" list.
- If complaint rate exceeds 0.3% for any domain, pause all sending from
  that domain immediately. You are likely already being throttled or blocked
  by major inbox providers.
- Root cause analysis: was the email poorly targeted? No unsubscribe link?
  Sending volume too high? Recipient didn't remember opting in?

**Unsubscribe handling:**
- Every cold email must include a one-click unsubscribe mechanism. This is
  required by CAN-SPAM, GDPR, and CASL.
- The unsubscribe link should be a single line at the bottom: "Unsubscribe"
  linked to a working removal page.
- Unsubscribe requests must be processed within 24 hours (CAN-SPAM requirement)
  or immediately (GDPR requirement).
- The unsubscribe rate for cold email is typically 0.5-2%. Above 3% signals
  poor targeting or excessive sending frequency.

### Phase 4: Delivery

Deliver a complete deliverability setup and monitoring plan:

1. **DNS Configuration Spec:** Exact SPF, DKIM, DMARC records to add,
   formatted for copy-paste into the DNS console.

2. **Warmup Calendar:** Week-by-week volume targets, recipient composition,
   monitoring checkpoints. Formatted as a calendar with daily targets.

3. **Monitoring Dashboard Spec:** What to track, where, how often, and
   what thresholds trigger action.

4. **Incident Response Plan:** For bounce spikes, complaint spikes,
   blacklisting, and domain reputation drops. What to do in the first
   hour, first day, first week.

5. **Quarterly Audit Checklist:** Deliverability degrades over time.
   A quarterly audit prevents silent decay.

## Output Format

```markdown
# Deliverability Setup Plan for [Company]

## Current State Audit
[DNS records, blacklist status, reputation scores, bounce/complaint rates]

## DNS Configuration
### SPF Record
[Exact TXT record to add]

### DKIM Configuration
[Provider-specific setup instructions with selectors]

### DMARC Record
[Exact TXT record with phased rollout schedule]

## Warmup Schedule
### Week 1 (Days 1-7)
[Daily volume, recipient composition, checkpoint]

[Repeat Weeks 2-4]

## Reputation Monitoring Dashboard
| Metric | Source | Frequency | Target | Warning Threshold | Critical Threshold |
|--------|--------|-----------|--------|-------------------|---------------------|
| [Metric rows] |

## Incident Response Plan
### Bounce Spike (>5%)
[Hour 1, Day 1, Week 1 actions]

### Spam Complaint Spike (>0.3%)
[Hour 1, Day 1, Week 1 actions]

### Blacklisting
[Immediate actions, delisting procedures]

### Domain Reputation Drop
[Diagnosis steps, recovery plan]

## Quarterly Audit Checklist
- [ ] Verify all DNS records unchanged
- [ ] Check Postmaster Tools reputation
- [ ] Review blacklist status
- [ ] Audit bounce rate trends
- [ ] Audit complaint rate trends
- [ ] Review DMARC reports for unauthorized senders
- [ ] Test inbox placement across Google, Microsoft, Yahoo
- [ ] Re-verify sending limits match current volume
- [ ] Rotate DKIM keys if older than 12 months
- [ ] Check sending platform deliverability metrics
```

## Quality Check

Before delivering, verify:

- [ ] Are SPF, DKIM, DMARC records provided in copy-paste format?
- [ ] Does SPF use `-all` (hard fail), not `~all`?
- [ ] Is DKIM using 2048-bit keys minimum?
- [ ] Does DMARC start with `p=none` and plan to progress to `p=reject`?
- [ ] Is the warmup schedule 2-4 weeks with per-week volume targets?
- [ ] Does the plan NEVER recommend sending cold from the primary domain?
- [ ] Are bounce thresholds clear (target <2%, warning 2-5%, critical >5%)?
- [ ] Are complaint thresholds clear (target <0.1%, critical >0.3%)?
- [ ] Is Google Postmaster Tools registration included?
- [ ] Is blacklist monitoring included with specific blacklists named?
- [ ] Does the incident response plan have time-based escalation steps?
- [ ] Is there a quarterly audit checklist?
- [ ] Are unsubscribe requirements specified (CAN-SPAM, GDPR)?
- [ ] Is email validation mentioned but NEVER described internally?

## Common Pitfalls

1. **Sending cold email from the primary business domain.** One spam
   complaint, one blacklisting event, and your transactional emails
   (password resets, invoices, customer notifications) are broken.
   This is the #1 deliverability mistake and it is catastrophic when
   it happens. Always use secondary domains for cold outreach.

2. **Skipping warmup.** A new domain sending 50 emails on Day 1 gets
   flagged within 48 hours. Google and Microsoft's algorithms interpret
   sudden volume from a new domain as spam behavior. No amount of
   authentication quality overrides the volume pattern.

3. **Soft DMARC (`p=none`) forever.** Many teams set `p=none` and never
   progress to enforcement. This is better than nothing but leaves the
   domain vulnerable to spoofing. Have a plan to reach `p=reject` within
   8 weeks of clean monitoring.

4. **Ignoring bounce rate creep.** A bounce rate that creeps from 1% to 3%
   over months is easy to miss because it's gradual. But inbox providers
   catch it. Set a weekly bounce rate review and a hard alert at 3%.

5. **No email verification before sending.** Every unverified address in a
   sequence is a potential bounce. Bounces above 5% trigger spam filtering
   at Google and Microsoft, and recovery takes weeks. Always verify before
   sending.

6. **Warmup-only via platform networks.** The automated warmup networks
   (warmup pools) are known to inbox providers. They're a supplement, not
   a replacement. Real engagement from real, diverse contacts builds
   stronger reputation than automated warmup alone.

7. **No DMARC reporting.** Without `rua` reports, you don't know who is
   sending on your behalf. You won't catch spoofing attempts, gradual
   DKIM alignment failures, or misconfigured third-party senders until
   they cause a deliverability crisis.

8. **Too many mailboxes per domain.** When one mailbox on a domain gets
   flagged for spam, it affects the domain reputation — which affects
   all mailboxes on that domain. Limit to 2-3 mailboxes per domain to
   contain blast radius.

## Sending Limits Reference

From `references/deliverability-primer.md` and industry best practices:

| Mailbox Provider | Daily Cold Limit | Notes |
|------------------|-----------------|-------|
| Google Workspace | 50 | Hard limit. 40 recommended for sustained sending. |
| Microsoft 365 | 50 | Similar to Google. Watch for outbound throttling. |
| Zoho Mail | 30-50 | Depends on plan. Free tier has lower limits. |
| Custom SMTP | Varies | Provider-specific. Check terms of service. |

These are cold email limits. Transactional email (password resets,
notifications) has separate, higher limits. Never mix cold and
transactional on the same domain — the cold reputation drags down
transactional deliverability.

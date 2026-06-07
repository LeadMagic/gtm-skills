---
name: deliverability-monitoring
description: >-
  Monitors email deliverability health through bounce tracking, spam placement
  detection, blacklist monitoring, and DMARC aggregate report analysis. Builds
  domain health dashboards with real-time alerts. Activates when the user asks
  about email deliverability, bounce rates, spam issues, blacklists, DNS
  authentication, domain reputation, or inbox placement problems.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: analytics
  tags: [deliverability, email, bounce, spam, blacklist, dmarc, dns, reputation]
  related_skills: [domain-infrastructure, cold-email-strategy, campaign-analytics, sending-platforms]
  frameworks: [M3AAWG Best Practices, Google Postmaster Guidelines, Microsoft SNDS]
---

# Deliverability Monitoring

## Overview

Deliverability Monitoring provides continuous surveillance of email infrastructure health — the foundation on which all outbound GTM rests. The core principle is that deliverability problems compound silently: by the time you notice lower reply rates, reputation damage may already be weeks deep and require months to repair. This skill prevents the catastrophic mistake of discovering deliverability issues through pipeline decline rather than proactive monitoring.

The non-obvious rule: deliverability is not binary (delivered vs bounced). It exists on a spectrum — inbox vs spam folder vs promotions tab vs graymail vs blocked. A "delivered" email that lands in the spam folder is effectively undelivered. This skill measures inbox placement, not just delivery status.

This skill produces a Domain Health Dashboard with: real-time bounce tracking across all sending domains, spam placement rates by mailbox provider, blacklist status across 50+ blacklists, DMARC aggregate report analysis with forwarding source identification, authentication health scores (SPF/DKIM/DMARC), and predictive reputation trend alerts.

## When to Use

- User says "check my deliverability" or "domain health check" → activate this skill
- User mentions "bounce rate is high" or "emails going to spam" → use this skill for diagnosis
- User asks "is my domain blacklisted" or "blacklist check" → activate monitoring module
- User says "DMARC reports" or "who is sending as my domain" → run DMARC analysis
- User mentions "spam placement" or "inbox rate" → track placement by provider
- User asks "domain reputation" or "sender score" → check reputation scores
- Trigger phrases: email deliverability, bounce tracking, spam folder, sender reputation, email authentication, DKIM SPF, domain warming, inbox placement test

Do NOT use for:
- Setting up DNS authentication initially → use domain-infrastructure
- Writing email content to avoid spam filters → use cold-email-copywriting
- Campaign performance analysis (opens, replies, meetings) → use campaign-analytics
- Choosing or configuring sending platforms → use sending-platforms
- Sequence design or cadence → use cold-email-strategy

## Authoritative Foundations

This skill draws from the following established methodologies:

- **M3AAWG (Messaging, Malware, Mobile Anti-Abuse Working Group)** — Industry best practices for email deliverability. M3AAWG publishes the authoritative guidance on complaint thresholds, authentication requirements, and sender reputation management that major mailbox providers (Google, Microsoft, Yahoo) implement.

- **Google Postmaster Tools** — Official Gmail deliverability data including IP reputation, domain reputation, spam rate, authentication status, and delivery errors. Google's February 2024 sender requirements (mandatory SPF/DKIM/DMARC, <0.3% spam complaint rate) are the new baseline.

- **Microsoft SNDS (Smart Network Data Services)** — Outlook/Hotmail deliverability data including spam complaint rates, trap hits, and delivery status by IP. Microsoft's filtering is distinct from Google's — a domain can be fine with Gmail and blocked by Microsoft.

- **Validity (Return Path)** — Inbox placement measurement across global mailbox providers. Seed-list-based testing confirms whether emails reach inbox, spam, or are missing entirely. Industry standard for placement benchmarking.

- **DMARC.org** — DMARC specification and aggregate report format (rua). DMARC reports are XML files sent by receiving mail servers showing authentication results for every email claiming your domain — the only way to detect unauthorized domain use.

## Prerequisites

- Access to DNS management for all sending domains (to check/modify SPF, DKIM, DMARC records)
- Google Postmaster Tools set up and verified for each sending domain (requires domain verification via DNS TXT record or HTML file)
- Microsoft SNDS access (requires Microsoft account and JMRP enrollment)
- DMARC aggregate report (rua) email address configured and receiving reports
- Sending platform analytics access (Smartlead, Instantly, Salesforge, Apollo) for bounce data
- Optional: Validity/Everest, MXToolbox, or GlockApps subscription for seed-list testing
- Optional: LeadMagic API key for email validation to pre-screen lists (referenced as optional tool for Email Validation endpoint)
- Recommended upstream skill: domain-infrastructure (if DNS setup is incomplete)

## Step-by-Step Process

### Phase 1: Intake

Gather required information from the user. Ask all questions at once. Do not proceed until all answers are received.

Required intake questions:

1. **Domain inventory**: List all sending domains (primary + secondary cold outreach domains). How many total? How many mailboxes per domain?
2. **Sending volume**: Current daily send volume per domain and per mailbox. Total sends in the last 30 days.
3. **Sending platform**: Which platform(s) are being used? (Smartlead, Instantly, Salesforge, Apollo, custom SMTP?)
4. **Observed issues**: What deliverability problems have been noticed? (High bounce rate, low open rates, spam complaints, specific domains bouncing you, blacklisting?)
5. **Recent changes**: Any changes in the last 30 days? (New domain added, volume increased, sequence changed, new sending platform, DNS changes?)
6. **Monitoring access**: Do you have Google Postmaster Tools and Microsoft SNDS set up? Is DMARC reporting email configured? Credentials or access needed?
7. **Bounce data availability**: Can you export bounce data from your sending platform for the last 30-90 days?

### Phase 2: DNS Authentication Audit

Verify all three authentication mechanisms for every sending domain:

1. **SPF Check**:
   - Query TXT record for each domain: `dig TXT domain.com | grep "v=spf1"`
   - Verify it includes your sending platform's IPs or includes
   - Check for common errors: multiple SPF records (invalid), missing mechanism for sending service, `~all` or `-all` at end, no DNS lookup limit exceedances (10 max)
   - Validate SPF doesn't exceed 10 DNS lookups (each include, a, mx, ptr counts). Use SPF flattening if needed.

2. **DKIM Check**:
   - Query DKIM selector for each domain: `dig TXT selector._domainkey.domain.com`
   - Verify key length >= 1024 bits (2048 recommended)
   - Confirm selector matches what sending platform publishes
   - Check for expired or misconfigured keys
   - Multiple sending platforms require multiple DKIM selectors — ensure no conflicts

3. **DMARC Check**:
   - Query DMARC record: `dig TXT _dmarc.domain.com`
   - Verify policy: `p=none` (monitoring only), `p=quarantine` (partial enforcement), or `p=reject` (full enforcement)
   - Check `rua` tag is present for aggregate report delivery
   - Verify `ruf` tag for forensic reports (optional but useful)
   - Check `pct` tag if gradual enforcement is in use
   - Validate alignment mode: `adkim=r` vs `adkim=s` (strict recommended), `aspf=r` vs `aspf=s`

4. **BIMI Check** (optional, for brand display):
   - Query BIMI record: `dig TXT default._bimi.domain.com`
   - Verify VMC (Verified Mark Certificate) if logo display desired

5. **DNS propagation check**: Verify all records resolve from multiple geographic locations using a tool like `dig +trace` or MXToolbox DNS check.

### Phase 3: Bounce Rate Analysis

Analyze bounce patterns to identify root causes:

1. **Export bounce data** from sending platform: date, recipient email, bounce type (hard/soft/block), bounce reason/code, sending domain, sending mailbox, campaign/sequence.

2. **Categorize bounces** by type:
   - **Hard bounces (5xx codes)**: Mailbox doesn't exist (550), domain doesn't exist (NXDOMAIN), user unknown (551), mailbox full and no longer accepting (552). These are permanent failures.
   - **Soft bounces (4xx codes)**: Mailbox full (temporary), server temporarily unavailable (450/451), connection timed out, greylisting, rate limiting. These are transient.
   - **Blocks**: Connection refused (554), spam content detected, IP/domain on blocklist, policy rejection. These indicate reputation problems.
   - **Spam complaints**: Not a bounce but tracked via feedback loops (FBL). If platform provides complaint data, track separately.

3. **Calculate bounce metrics**:
   - Overall bounce rate: total bounces ÷ total sent
   - Hard bounce rate: hard bounces ÷ total sent (target: <2%)
   - Soft bounce rate: soft bounces ÷ total sent (target: <3%)
   - Block rate: blocks ÷ total sent (target: <1%)
   - Per-domain bounce rate: bounces by sending domain ÷ sends by domain
   - Per-mailbox bounce rate: bounces by mailbox ÷ sends by mailbox
   - Per-provider bounce rate: bounces at Gmail/Outlook/Yahoo ÷ sends to each

4. **Pattern detection**:
   - **Sudden spike**: Bounce rate jumped from 1% to 8% in one day → likely blacklisting or DNS failure. Investigate immediately.
   - **Gradual increase**: Bounce rate rising 0.2% per week → data decay or slow reputation decline.
   - **Provider-specific**: Only Gmail bouncing → Gmail-specific reputation issue. Check Google Postmaster.
   - **Domain-specific**: Bounces concentrated on specific recipient domains → that domain's server has blacklisted you.
   - **Content-triggered**: Bounces correlate with specific sequences or templates → content triggering spam filters.

5. **Root cause assignment** for each bounce cluster:
   - Invalid data → list wasn't verified before sending
   - Reputation block → improve sending practices, check blacklists
   - Content filter → review email content against spam trigger words
   - Rate limiting → reduce send volume per domain/mailbox
   - DNS failure → fix authentication records

### Phase 4: Spam Placement Detection

Determine actual inbox vs spam placement:

1. **Seed-list testing** (gold standard):
   - Create seed accounts at Gmail, Outlook, Yahoo, and 2-3 other major providers
   - Send test emails through the same infrastructure as real campaigns
   - Check inbox vs spam placement within 5 minutes of sending
   - Test with different content types: plain text, light HTML, with links, without links, with images
   - Run weekly at minimum; daily if actively sending >100/day

2. **Google Postmaster Tools analysis**:
   - Check Spam Rate graph: must stay below 0.1% (Google threshold is 0.3% but target below 0.1%)
   - Check Domain Reputation: should be "High" or "Medium" — "Low" or "Bad" indicates critical problems
   - Check IP Reputation if using dedicated IPs
   - Check Authentication: DKIM and SPF should show "PASS" for all traffic
   - Check Delivery Errors: identify specific error types and volumes
   - Check Encryption: TLS should be 95%+

3. **Microsoft SNDS analysis**:
   - Check complaint rate per IP
   - Check spam trap hit rate
   - Check delivery status breakdown
   - Microsoft is typically stricter than Google on unknown senders — new domains often face temporary blocking

4. **Engagement-based placement signals** (proxy when seed testing unavailable):
   - Open rate by provider: Gmail < 15% when Postmaster says "High" reputation → possible spam placement despite good reputation. Check content.
   - Reply rate by provider: lower reply rates to Outlook vs Gmail → Outlook filtering may be more aggressive
   - Click tracking: if open pixel doesn't fire but link clicks register → images blocked (not spam placement)

### Phase 5: Blacklist Monitoring

Continuous surveillance of 50+ public blacklists:

1. **Check all sending IPs and domains** against major blacklists:
   - Spamhaus (SBL, XBL, PBL) — the most impactful. SBL listing means all Spamhaus users (most of the internet) reject your mail.
   - Barracuda (BRBL) — used by Barracuda appliances in many enterprise environments
   - SpamCop (SCBL) — real-time, automated listing based on spam trap hits
   - Invaluement — used by many spam filters
   - SORBS — various lists including dynamic IPs, open relays
   - UCEPROTECT — three levels with different listing criteria
   - SURBL — URI-based blacklist (checks links in emails, not sending IPs)
   - URIBL — another URI blacklist covering domains in email bodies
   - SEM FRESH, SEM BLACK — email sender blacklists
   - Secondary lists: PSBL, WPBL, LASHBACK, RATS, JMF, MAILSPIKE, NIXSPAM, etc.

2. **Check frequency**: Daily for domains actively sending >50 emails/day. Weekly for low-volume or paused domains.

3. **Delisting procedures** for common blacklists:
   - **Spamhaus**: Use their Blocklist Removal Center. Requires identifying and fixing the root cause. Delisting is typically automatic within 24 hours once the cause is resolved (no more spam trap hits, no more listings on other criteria).
   - **Barracuda**: Submit removal request via their form. Requires explanation of corrective actions. Manual review, 24-72 hours.
   - **SpamCop**: Listings expire automatically within 24-48 hours of last reported spam. No manual removal. Must stop the spam reports.
   - **UCEPROTECT**: Level 1 expires automatically. Level 2 and 3 require payment for express delisting or wait period (up to 7 days for Level 2).
   - **Microsoft (internal blocklist)**: Not a public blacklist. Submit delisting request via Microsoft's delist portal. Requires JMRP enrollment. Manual review, 24-48 hours.

4. **Blacklist prevention checklist** (verify when addressing any blacklisting):
   - Are all lists verified before sending? (Bounce rate <2%)
   - Is sending volume steady and predictable (no sudden spikes)?
   - Are spam complaints below 0.1%?
   - Do emails have clear unsubscribe links?
   - Is the sending domain properly authenticated (SPF, DKIM, DMARC)?
   - Is there a verified sending history (4+ weeks of warmup)?
   - Are spam trap addresses being hit? (Check with Microsoft SNDS)

### Phase 6: DMARC Aggregate Report Analysis

Process DMARC rua (aggregate) reports for domain abuse detection:

1. **Collect DMARC reports** from the email address configured in the rua tag. Reports arrive as XML attachments (typically .xml or .xml.gz) from receiving mail servers.

2. **Parse each report** to extract:
   - **Reporter**: Which organization sent the report (google.com, microsoft.com, yahoo.com, etc.)
   - **Date range**: What time period the report covers (typically 24 hours)
   - **Source IP**: The IP address that sent mail claiming to be from your domain
   - **Count**: Number of emails from that IP
   - **Disposition**: What the receiver did (none, quarantine, reject)
   - **DKIM result**: pass or fail, and which domain signed
   - **SPF result**: pass or fail, and which domain was used in envelope-from
   - **DMARC policy applied**: whether DMARC policy was applied based on alignment
   - **Header-from domain**: The domain in the From: header (may differ from envelope-from)

3. **Authorized sender verification**:
   - Identify all IPs sending as your domain
   - Map each IP to known sending services (ESP, CRM, transactional, marketing)
   - Flag any unknown IPs — these may be unauthorized senders or spoofing attempts
   - Verify each known sender has proper SPF/DKIM alignment

4. **DMARC pass rate calculation**:
   - Total emails where DMARC resulted in "pass" ÷ total emails processed
   - Target: >95% pass rate. Below 90% indicates authentication problems.
   - Identify the source of failures: DKIM failures (signing issue), SPF failures (envelope-from mismatch), or alignment failures (header-from mismatch with authenticated domain)

5. **Spoofing and abuse detection**:
   - Large volume from unknown IPs → likely spoofing or phishing
   - Emails from IPs in unexpected countries → investigate
   - Consistent failures from a legitimate sending service → misconfiguration, fix immediately
   - High count from a single unknown source → targeted spoofing attack

6. **Forwarding analysis** (common DMARC challenge):
   - Emails forwarded by mailing lists or forwarding services often fail SPF (envelope-from changes)
   - High SPF failure rate with DKIM pass → forwarding issue, not spoofing. Consider ARC (Authenticated Received Chain).
   - If forwarding breaks legitimate email flow, adjust DMARC policy carefully (don't jump to p=reject if mailing lists are critical).

### Phase 7: Domain Health Dashboard Construction

Build a consolidated dashboard with all deliverability signals:

1. **Overall Health Score** (0-100):
   - Bounce rate: subtract from 100 (0% = +25 points, 5%+ = 0 points)
   - Spam complaint rate: 0% = +25 points, 0.3%+ = 0 points
   - Blacklist status: clean = +20 points, 1 blacklist = +10, 2+ = 0
   - Authentication: all three pass = +20, DKIM/SPF pass only = +10, failures = 0
   - Inbox placement: >95% = +10, 80-95% = +5, <80% = 0
   - Total: 0-40 (Critical), 41-60 (At Risk), 61-80 (Healthy), 81-100 (Excellent)

2. **Per-Domain Scorecard**: Each sending domain gets individual scores for bounce rate, spam rate, blacklist count, and inbox placement. Identify the weakest domain for priority remediation.

3. **Trend Graphs** (30/60/90 day):
   - Bounce rate trend (is it improving, stable, or worsening?)
   - Spam complaint trend
   - Open rate by provider trend (proxy for inbox placement changes)
   - Blacklist incident timeline

4. **Alert Thresholds**:
   - Bounce rate exceeds 2% → immediate investigation
   - Any blacklist addition → immediate investigation
   - Spam complaint rate exceeds 0.1% → review content and targeting
   - DMARC pass rate drops below 90% → authentication audit
   - Google Postmaster reputation drops to "Medium" → reduce volume, improve engagement
   - Single-day bounce spike >2x running average → possible blacklisting

5. **Weekly Deliverability Report** format:
   - Executive summary: overall health score and trend
   - Per-domain metrics table
   - Blacklist status table (all domains, all major blacklists)
   - Alert summary (new alerts this week, resolved alerts)
   - Action items for the upcoming week

## Output Format

The agent should produce output in this structure:

```markdown
# Domain Health Dashboard

## Executive Summary
- Overall Health Score: [0-100] ([Critical/At Risk/Healthy/Excellent])
- Trend: [Improving/Stable/Declining] vs last week
- Active Issues: [count] requiring immediate attention
- Top Risk: [specific domain/threat]

## Authentication Status
| Domain | SPF | DKIM | DMARC | Policy | BIMI | Status |
|--------|-----|------|-------|--------|------|--------|
| domain1.com | PASS | PASS | PASS | p=none | - | ✅ |
| domain2.com | FAIL | PASS | FAIL | - | - | ❌ |

## Bounce Analysis
| Domain | 7-Day Bounce% | 30-Day Bounce% | Trend | Hard% | Soft% | Block% |
|--------|---------------|----------------|-------|-------|-------|--------|
| ... | ... | ... | ... | ... | ... | ... |

## Spam Placement
| Mailbox Provider | Inbox% | Spam% | Missing% | Trend | Samples |
|-----------------|--------|-------|----------|-------|---------|
| Gmail | 92% | 6% | 2% | ↓ | 100 |
| Outlook | 78% | 18% | 4% | ↓ | 85 |
| Yahoo | 95% | 3% | 2% | → | 40 |

## Blacklist Status
| Domain/IP | Blacklist | Listed Date | Status | Delisting ETA |
|-----------|-----------|-------------|--------|---------------|
| ip.1.2.3 | Spamhaus SBL | 2024-06-01 | ACTIVE | Under review |
| domain2.com | Barracuda | - | CLEAN | - |

## DMARC Analysis
- Reporting Period: [date range]
- Total Emails Processed: [count]
- DMARC Pass Rate: [%]
- Unknown Senders Detected: [count]
- Spoofing Attempts: [count]

## Alerts (Last 7 Days)
| Severity | Date | Domain | Alert | Status |
|----------|------|--------|-------|--------|
| CRITICAL | 06-05 | domain2 | Bounce rate exceeded 5% | Investigating |
| WARNING | 06-04 | domain1 | Spam rate 0.15% | Monitoring |

## Action Items
1. [Priority 1 action]
2. [Priority 2 action]
...

## Trend Charts (30/60/90 Day)
[Describe key trend observations]
```

## Quality Check

Before delivering, verify:

- [ ] Have all sending domains been audited for SPF, DKIM, and DMARC?
- [ ] Is bounce data categorized by type (hard, soft, block) and by domain/provider?
- [ ] Have blacklist checks been run against all major blacklists (Spamhaus, Barracuda, SpamCop, etc.)?
- [ ] Is DMARC report analysis identifying unauthorized senders and spoofing?
- [ ] Are alert thresholds clearly defined with specific numeric triggers?
- [ ] Does the dashboard include trend data (not just point-in-time)?
- [ ] Are delisting procedures documented for any active blacklist entries?
- [ ] Would an email deliverability specialist find this monitoring coverage comprehensive?

## Common Pitfalls

1. **Monitoring only bounce rate.** Bounce rate tells you about list quality, not reputation. A domain can have 0% bounce rate and 100% spam placement. Always combine bounce tracking with spam placement testing and blacklist monitoring. Bounce rate is necessary but insufficient.

2. **Ignoring Google Postmaster Tools.** Google delivers to approximately 50% of B2B inboxes. If you're not monitoring Google Postmaster Tools, you're flying blind on half your deliverability. Setup takes 5 minutes (DNS TXT verification). The data is free and authoritative — it comes directly from Google.

3. **Reacting instead of trending.** Blacklistings don't happen instantly — complaint rates rise over days to weeks before listing. Monitoring trends (rising complaints, declining open rates by provider, increasing block rates) lets you intervene before blacklisting occurs. Set trend-based alerts, not just threshold-based ones.

4. **Treating all blacklists equally.** Spamhaus SBL listing will cripple deliverability immediately. A listing on a minor blacklist with few downstream consumers may have zero impact. Prioritize remediation based on blacklist impact, not just listing count. Better to be on 3 minor blacklists than 1 Spamhaus listing.

5. **DMARC `p=reject` without understanding forwarding impact.** Moving to `p=reject` before analyzing forwarding patterns will break legitimate email delivery through mailing lists, forwarding services, and some corporate email forwarding rules. Analyze DMARC reports for at least 30 days at `p=none` before considering stricter policies.

6. **Not isolating cold sending domains.** Using the same domain for cold outreach and transactional email means a reputation hit from cold outreach takes down password resets, invoices, and product notifications. This is the single most common deliverability catastrophe. Always separate sending domains by purpose.

7. **Misdiagnosing low open rates.** Low open rates can be caused by spam placement (invisible to open tracking), image blocking (open pixel doesn't load), Apple Mail Privacy Protection (pre-fetches all images, inflating open rates), or genuinely uninterested recipients. Cross-reference with click rates, reply rates, and seed-list tests to determine actual cause.

## Related Skills

- **domain-infrastructure**: Run first if DNS authentication is incomplete or misconfigured. Handles SPF/DKIM/DMARC setup, secondary domains, and inbox rotation.
- **campaign-analytics**: Run after deliverability is confirmed healthy. Layer 1 of campaign analytics depends on deliverability monitoring output.
- **cold-email-strategy**: Adjust sequence architecture based on deliverability constraints (volume limits, warmup status, domain rotation).
- **sending-platforms**: Platform-specific deliverability features and configurations. Integrate monitoring data with platform settings.
- **contact-verification**: Pre-send verification reduces bounce rates. Feedback loop: deliverability monitoring identifies verification gaps.
- **email-finding**: Poor email finder accuracy causes high bounce rates. Deliverability monitoring closes the loop by measuring actual bounce rates from each data source.

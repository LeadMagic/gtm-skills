---
name: inbox-setup
description: >-
  Set up cold email inbox infrastructure from scratch — Google Workspace, Microsoft
  365, and Azure/Entra inbox provisioning, DNS authentication, domain buying, warmup,
  and cost optimization. Use when setting up sending infrastructure, buying domains,
  provisioning mailboxes, or scaling cold email sending capacity. Triggers on:
  "inbox setup", "email infrastructure", "buy domains", "Google Workspace inbox",
  "Microsoft inbox", "Azure inbox", "cold email setup", "sending infrastructure",
  "provision inboxes", "DNS setup", or any request about building cold email infra.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: outbound
  tags: [inbox-setup, infrastructure, deliverability, google, microsoft, domains]
  related_skills: [email-deliverability, domain-infrastructure, sending-platforms]
  frameworks: [Google Bulk Sender Guidelines, Microsoft Email Sender Guidelines, Eric Nowoslawski Sending Volume Strategy, Jed Mahrle Cold Email Infrastructure]
---

# Inbox Setup

## Overview

Cold email infrastructure is the foundation underneath every outbound motion.
Get it wrong and your copy, targeting, and offer don't matter — you're in spam.
This skill covers DIY inbox provisioning across Google Workspace, Microsoft 365,
and Azure/Entra, plus DNS authentication, warmup, and infrastructure scaling.

## When to Use

- "Set up cold email inboxes"
- "Buy domains for cold outreach"
- "Provision Google Workspace mailboxes"
- "Set up Microsoft 365 for cold email"
- "Configure DNS for sending domains"
- "Scale my sending infrastructure"
- "How many inboxes do I need?"

## Authoritative Foundations

- **Google Bulk Sender Guidelines** — sender authentication, low spam complaint rates, and authenticated alignment are baseline requirements for sustainable outbound.
  Domain isolation is non-negotiable: never send cold from the primary business domain; use separate sending domains with independent reputation.
- **Microsoft Email Sender Guidelines** — maintain authenticated mail, clean lists, low complaints, and conservative volume ramps to protect sender reputation.
- **Eric Nowoslawski (Growth Engine X)** — inbox infrastructure at scale
  emails/month. Strategy: 2 inboxes per domain, 30 emails/day per inbox,
  3-week warmup minimum, keep 50% spare capacity warming at all times.
- **Jed Mahrle (Practical Prospecting)** — 30,000+ subscribers. "Cold email
  isn't a numbers game anymore. It's a relevance game. Send fewer emails to
  better fit accounts."

## Prerequisites

- Domain registrar account (Namecheap, GoDaddy, Google Domains)
- Google Workspace or Microsoft 365 tenant (or Azure/Entra for Hypertide-style)
- DNS management access
- Budget: ~$6-15/mailbox/month for Google, ~$4-6/mailbox/month for Microsoft,
  plus domain costs (~$10-15/domain/year)

## Step-by-Step Process

### Phase 1: Domain Acquisition

Buy 3-5 secondary domains for cold outreach. Never use your primary business domain.

**Rules:**
- .com or .co preferred — avoid unusual TLDs that trigger spam filters
- Domain should be a variation that could be a real company (e.g., tryacme.com,
  getacme.io, acmehq.com)
- Redirect the domain to your main site or a simple landing page
- Set up SSL certificate (Let's Encrypt, free)

**Cost:** ~$10-15/domain/year. Budget 3-5 domains = $30-75/year.

### Phase 2: Mailbox Provider Selection

| Provider | Cost/Mailbox | Mailboxes/Domain | Sends/Day/Mailbox | Best For |
|---|---|---|---|---|
| **Google Workspace** | $6-15/mo | 2-3 | 25-30 | Highest deliverability, preferred by Google recipients |
| **Microsoft 365** | $4-6/mo | 25 | 10 | High deliverability to Outlook, best mailbox-to-domain ratio |
| **Azure/Entra (via Hypertide)** | $50/order (100 inboxes) | 50 | 2 (after warmup) | Maximum scale, lowest cost per inbox |
| **SMTP (via ScaledMail)** | $3.50-4/mo | 4 | 10 | Budget option, works with any sequencer |

**Eric Nowoslawski Strategy:** 2 inboxes per domain, 30 sends/day/inbox, 3-week
warmup minimum. Keep 50% spare capacity warming at all times.

**Scaling math:** To send 1,000 emails/day:
- Google: 1,000 ÷ 25 = 40 inboxes, 20 domains, ~$240-600/mo
- Microsoft: 1,000 ÷ 10 = 100 inboxes, 4 domains, ~$400-600/mo
- Hypertide Entra: 1,000 ÷ 2 = 500 inboxes, 10 orders, ~$500/mo + setup

### Phase 3: DNS Authentication (Non-Negotiable)

For every sending domain, configure all three:

**SPF:** `v=spf1 include:_spf.google.com ~all` (Google) or
`v=spf1 include:spf.protection.outlook.com ~all` (Microsoft)

**DKIM:** Generate in admin console (Google: Apps > Gmail > Authenticate email.
Microsoft: Security > DKIM). Add the generated TXT record to DNS.

**DMARC:** Start with `v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com`.
After monitoring for 2-4 weeks, tighten to `p=quarantine`, eventually `p=reject`.

**Verification:** Use MXToolbox or Google Admin Toolbox to verify all records
resolve correctly. A single misconfigured record = spam placement.

### Phase 4: Warmup (2-4 Weeks Minimum)

- Week 1: 5-10 emails/day to known-engaging addresses
- Week 2: 15-25 emails/day, mix warm and cold
- Week 3: 30-40 emails/day
- Week 4: 40-50 emails/day, full cold sending

Use a dedicated warmup tool (Instantly Warmup, Smartlead Warmup, or
Hypertide's built-in warmup). Monitor inbox placement weekly.

**Eric Nowoslawski note:** "We used to be able to launch low volume without
waiting 3 weeks. These days, inboxes may not be ready even after a full 3
weeks." Plan conservatively.

### Phase 5: Infrastructure Players

| Provider | What They Do | Best For |
|---|---|---|
| **ScaledMail** | Done-for-you inbox provisioning. Google, M365, SMTP. 230K+ inboxes managed. | Teams that want hands-off setup |
| **Hypertide** | Automated Azure/Entra inboxes in 4-6 hours. Tenant isolation. $50/mo per 100 inboxes. | High-volume agencies, max scale |
| **Mailforge** | Full DNS monitoring, custom warmup, inbox health reports | Teams that want control + visibility |
| **Maildoso** | Pre-configured inboxes + domains + DNS. Master inboxes. | Budget-conscious teams |

**DIY vs Done-For-You:** DIY costs less per mailbox but requires 4-8 hours of
setup plus ongoing maintenance. Done-for-you (ScaledMail, Hypertide) costs
more per mailbox but ships in hours to days. The breakeven: if your time is
worth >$100/hr, done-for-you wins at any scale.

## Output Format

Infrastructure plan with: domain inventory, mailbox count by provider, DNS
record sheet, warmup schedule, cost model (setup + monthly), and monitoring
dashboard setup.

## Quality Check

- [ ] No primary business domain used for cold sending
- [ ] SPF, DKIM, DMARC configured and verified on every domain
- [ ] 2-3 inboxes per domain maximum (Google) or 25 (Microsoft)
- [ ] 30-50 sends/day/inbox maximum
- [ ] 2-4 week warmup completed before any cold sends
- [ ] 50% spare capacity warming at all times
- [ ] MXToolbox or equivalent verification passed on all domains

## Common Pitfalls

1. **Sending from primary domain.** One spam complaint and your password
   resets, invoices, and support emails go to spam too. Never.

2. **Too many inboxes per domain.** 10+ mailboxes on one domain signals
   bulk sending to spam filters. 2-3 for Google, 25 max for Microsoft.

3. **Skipping warmup.** New domains sent at full volume get blacklisted
   within 48 hours. There is no shortcut.

4. **Sending unverified emails.** 5%+ bounce rate triggers automated spam
   filtering. Always verify with a service like LeadMagic Email Validation
   before sending.

5. **No spare capacity.** If inboxes burn out mid-campaign and you have no
   spares warming, your pipeline stops. Keep 50% spare capacity.

6. **DNS misconfiguration.** A missing DKIM record or incorrect SPF syntax
   is caught by every major inbox provider. Triple-check all records.

## Execution Artifacts

- `../cold-email-strategy/references/eric-nowoslawski-outbound.md` — Sending volume strategy, 1:1 backups (Eric Nowoslawski)
- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **email-deliverability**: Full deliverability strategy beyond infrastructure
- **domain-infrastructure**: DNS auth deep-dive
- **sending-platforms**: Sequencer selection and setup
- **contact-verification**: Verify emails before they enter your inboxes

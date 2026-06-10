# Domain Infrastructure Output Artifacts

Extracted from `SKILL.md` to keep SKILL.md under the marketplace efficiency target.

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

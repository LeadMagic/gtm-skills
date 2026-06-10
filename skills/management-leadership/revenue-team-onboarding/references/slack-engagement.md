# Slack Engagement — Revenue Teams

Slack is the **operating system** for ramp — not a distraction. New hires drown when added to 20 channels day one. Core channels first; expand after certification.

---

## Channel map

### Week 1 (required)

| Channel | Purpose | Who posts | Manager SLA |
|---|---|---|---|
| `#sales-team` | Daily async standup, team announcements | All reps | <4h on blockers |
| `#wins` | Meetings held, opps created, closed won | Reps + managers amplify | Same day reaction |
| `#deal-desk` | Deal help — **SPICED context required** | AEs, managers, SEs | <4h during ramp |

### Week 3+ (add selectively)

| Channel | Purpose |
|---|---|
| `#competitive-intel` | Win/loss themes, battlecard updates |
| `#product-feedback` | Customer quotes for PM (no PII) |
| `#marketing-handoff` | MQL quality, campaign feedback |
| `#revops-requests` | CRM fixes, list builds (ticket format) |

**Rule:** Max **3 channels** week 1. Add one per week after certification.

---

## Message templates

### Daily standup (`#sales-team`)

```
Yesterday: [1–2 outcomes — meetings, opps advanced]
Today: [top 3 priorities]
Blocker: [specific ask + @manager if urgent]
```

### Win post (`#wins`)

```
🎯 [Meeting held / Opp created / Closed won]
Account: [name]
What worked: [1 sentence — messaging, champion, trigger]
@manager for visibility
```

### Deal desk (`#deal-desk`)

```
Account: [name]
Stage: [CRM stage]
SPICED: S: … | P: … | I: … | C: … | E: … | D: …
Blocker: [single question]
Ask: [specific help — exec sponsor, pricing, SE]
```

---

## Norms

| Do | Don't |
|---|---|
| Post wins publicly so team learns patterns | Share customer PII, contract terms, or full emails |
| Use threads for long deal debates | DM-only questions that should be team learning |
| @channel sparingly (true blockers only) | Competitor bashing or unverified rumors |
| React to peer wins (emoji + short reply) | Paste screenshots with unretracted sensitive data |
| Pin onboarding FAQ week 1 | Create duplicate channels per manager |

**Manager role:** Reply to every ramp-week win; escalate blockers same day.

---

## Integrations

| Source | Destination | Owner |
|---|---|---|
| Gong call highlight | `#wins` | RevOps |
| CRM stalled deal (7+ days) | `#deal-desk` | n8n / RevOps |
| New hire | Intro thread in `#sales-team` day 1 | Manager |
| G2 intent alert (if licensed) | `#sales-team` or SDR DM + CRM | RevOps |

---

## Ramp-specific cadence

| Week | Slack focus |
|---|---|
| 1 | Standup only; manager models format |
| 2 | First win post required (even small) |
| 3 | Deal desk with SPICED — manager reviews format |
| 4+ | Peer wins encouraged; manager fades to SLA-only |

---

## Security

- No API keys, passwords, or bulk exports in Slack
- Customer data: company name + role OK; emails/phones use CRM links
- Align with `soc2-compliance` — production access gates apply

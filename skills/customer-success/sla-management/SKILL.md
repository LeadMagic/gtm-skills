---
name: sla-management
description: >-
  Design and manage customer support SLAs — service level agreements, ticket
  priority matrices, first response time targets, resolution time targets,
  escalation paths, business hours configuration, and SLA performance
  dashboards. Use when defining support SLAs, building tier-based service
  levels, designing escalation policies, or measuring SLA compliance.
  Triggers on: "SLA design", "support SLAs", "escalation path", "ticket
  priority matrix", "first response time", "SLA compliance".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: customer-success
  tags: [sla, support, escalation, ticket-priority, first-response, resolution-time, service-level]
  related_skills: [support-tool-stack, cs-playbooks, headless-support, cs-analytics-dashboards, customer-onboarding]
  frameworks:
    - "ITIL 4 — Service Level Management practice"
    - "Zendesk — SLA Policy Design Guide"
    - "Intercom — SLA and Business Hours Configuration"
    - "HDI — Support Center Certification Standards"
---

# SLA Management

## Overview

SLAs are promises. Breaking them breaks trust. The mistake: setting SLAs based
on what sounds good ("we respond in 1 hour!") instead of what's operationally
sustainable. When the team misses the SLA 50% of the time, customers learn the
promise is empty. This skill covers SLA design by ticket priority, customer
tier, and channel — plus escalation paths, business hours configuration, and
the dashboard to track it all.

## When to Use

Trigger phrases: "design support SLAs", "set up SLA policies", "ticket priority
matrix", "escalation policy", "first response time target", "SLA compliance
dashboard", "support tiers by plan", "business hours setup", "after-hours
support", "ticket routing rules", "escalation path"

## Step-by-Step Process

### Phase 1: SLA Architecture

**Two types of SLAs (implement both):**

1. **First Response Time (FRT):** Time until a HUMAN acknowledges the ticket.
   Auto-replies DON'T count. "We're on it" = response. Auto-responder = not.

2. **Resolution Time:** Time until the issue is resolved. "Resolved" = customer
   confirms it's fixed, OR 72 hours of silence after proposed solution.

**Priority matrix (4-level standard):**

| Priority | Definition | Examples | FRT | Resolution |
|---|---|---|---|---|
| **P1 — Critical** | System down, security incident, data loss, revenue blocked | Can't log in, billing failed for all users, API down | 15 min | 2 hours |
| **P2 — High** | Major feature broken, workflow blocked, no workaround | Export failing, campaign can't send, integration down | 1 hour | 8 hours |
| **P3 — Normal** | Question, minor bug, configuration help, workaround exists | "How do I set up X?", report looks wrong | 4 hours | 24 hours |
| **P4 — Low** | Feature request, cosmetic bug, nice-to-have | "Add dark mode", typo on page | 8 hours | 5 days or "Deferred" |

**Criteria for P1 (be strict — P1 inflation kills credibility):**
- System-wide outage or critical path broken
- Security incident or data breach
- Revenue blocked (payments failing, subscription broken)
- Data loss or corruption
- >25% of customers affected

**Criteria for P2:**
- Major feature broken for multiple customers
- Workflow blocked with no workaround
- Integration critical path broken
- <25% of customers affected but impact is high

**Never P1:**
- One customer's feature request (even if they're your biggest)
- Cosmetic issues ("button is the wrong shade of blue")
- "This is urgent for me" (urgency ≠ impact — unless revenue is genuinely blocked)

### Phase 2: Tier-Based SLAs

**Service levels by plan (if you offer tiered support):**

| Plan | P1 FRT | P2 FRT | P3 FRT | Channels | Dedicated CSM |
|---|---|---|---|---|---|
| **Free** | Best-effort | Best-effort | 24 hours | Email, KB | No |
| **Starter** | 1 hour | 4 hours | 8 hours | Email, Chat | No |
| **Growth** | 30 min | 2 hours | 4 hours | Email, Chat, Phone | No |
| **Enterprise** | 15 min | 1 hour | 2 hours | All + Slack | Yes |

**Enterprise SLA add-ons:**
- Dedicated CSM with direct phone/Slack
- Uptime SLA (99.9% = ~43 min downtime/month)
- Proactive monitoring (you alert them, not vice versa)
- Quarterly business reviews included
- Incident post-mortems within 5 business days

**Uptime SLA (if you offer one):**
```
Uptime SLA: 99.9% (43 min downtime/month)
Credit: 5% of monthly bill per 30 min of downtime beyond SLA
Max credit: 100% of monthly bill
Exclusions: planned maintenance (announced 48 hrs), force majeure, customer-caused
```

### Phase 3: Escalation Paths

**3-tier escalation model:**

```
TIER 1: Support Agent (L1)
  Handles: P3, P4, common P2s with known solutions
  Tools: Macros, KB, basic troubleshooting
  Escalates to L2 when: Unknown cause, needs technical investigation, >30 min on ticket

TIER 2: Technical Specialist / Senior Agent (L2)
  Handles: Complex P2s, escalated P3s, initial P1 triage
  Tools: Logs, internal tools, product expertise, can file bug reports
  Escalates to L3 when: Bug confirmed (not config), needs engineering, security incident

TIER 3: Engineering / Security / Executive (L3)
  Handles: Confirmed bugs, security incidents, P1 outages, enterprise escalation
  Response: PagerDuty/Opsgenie on-call rotation
  SLA: Acknowledged within 5 min, initial fix/rollback within 30 min

DIRECTOR / VP ESCALATION:
  Customer contacts VP CS or CEO directly via LinkedIn/Twitter
  → VP acknowledges within 1 hour, assigns to L3, manages customer comms
```

**Escalation triggers (automated in help desk):**
- P1 ticket created → auto-page L3 on-call
- P2 ticket unresolved for 50% of SLA → auto-escalate to L2
- P3 ticket unresolved for 75% of SLA → auto-escalate to L2
- Customer replies with negative sentiment → auto-flag for manager review
- Enterprise customer + P2 or higher → auto-notify CSM

**Escalation communication template:**
```
Subject: [ESCALATED] Ticket #1234 — [Issue Summary]

This ticket has been escalated to [L2 / L3] due to:
- Time elapsed: X hours (SLA is Y hours)
- Complexity: requires [engineering / security / executive] involvement

Current status: [what's been tried, what's known, what's next]

Next update: within [timeframe]

[Link to incident channel / war room if active incident]
```

### Phase 4: Business Hours and Coverage

**Standard business hours:**
```
Primary: Monday-Friday, 9am-6pm [timezone]
Coverage: Monday-Friday, 6am-6pm [timezone] (staggered shifts)

After-hours: P1 only (on-call via PagerDuty)
Weekend: P1 only (on-call via PagerDuty)
Holidays: P1 only (rotating on-call, announced 2 weeks prior)
```

**What "business hours" means for SLAs:**
- FRT clock PAUSES outside business hours for P2-P4
- FRT clock NEVER pauses for P1 (24/7/365)
- Ticket submitted Friday 5:30pm P3 → clock starts Monday 9am
- Ticket submitted Friday 5:30pm P1 → clock starts immediately

**Global coverage (if 24/7 for P2+):**
```
Americas: 9am-6pm ET
EMEA: 9am-6pm CET
APAC: 9am-6pm SGT

Overlap: 2-hour handoff windows between regions
```

### Phase 5: SLA Performance Dashboard

**Track these 6 SLA metrics:**

| Metric | Target | Red Flag |
|---|---|---|
| P1 FRT Compliance | 100% | <95% — system failing |
| P2 FRT Compliance | 95% | <90% — staffing or process issue |
| P3 FRT Compliance | 90% | <85% — too many tickets per agent |
| P1 Resolution Compliance | 95% | <90% — escalation process broken |
| P2 Resolution Compliance | 90% | <80% — complexity or staffing gap |
| Overall SLA Compliance | 90% | <85% — systemic issue |

**Dashboard structure:**
```
SLA PERFORMANCE — [Month Year]

OVERALL: 92% SLA Compliance (↑3% MoM)

BY PRIORITY:
| Priority | Tickets | SLA Met | Compliance | Trend |
|---|---|---|---|---|
| P1 | 3 | 3 | 100% | — |
| P2 | 45 | 42 | 93% | ↑5pp |
| P3 | 320 | 291 | 91% | ↑2pp |
| P4 | 180 | 165 | 92% | ↑1pp |

BY AGENT:
| Agent | Tickets | SLA Met | Compliance |
|---|---|---|---|
| [name] | X | X | X% |

BREACH ANALYSIS (tickets that missed SLA):
- Top reason for breach: [understaffed on weekends / too many tickets / complexity]
- Action: [hire weekend coverage / add L2 capacity / document complex issues]
```

## Output Format

```
SLA POLICY — [Company]

Last Updated: [date]
Owner: [name, title]

PRIORITY MATRIX:
| Priority | Definition | Examples | FRT | Resolution |
|---|---|---|---|---|
| P1 | ... | ... | ... | ... |
...

TIER-BASED SLA:
[Table by plan tier]

ESCALATION PATHS:
L1 → L2 trigger: [criteria]
L2 → L3 trigger: [criteria]
Director/VP escalation: [when, how]

BUSINESS HOURS:
- Hours: [timezone, schedule]
- After-hours: P1 only (on-call via [PagerDuty/Opsgenie])
- Clock behavior: P2-P4 clock pauses outside hours. P1 clock never pauses.

SLA COMPLIANCE TARGETS:
- P1 FRT: 100%
- P2 FRT: 95%
- Overall: 90%

BREACH REMEDIATION:
- For customers: [communication, credit if applicable]
- Internal: [post-mortem, process fix, staffing adjustment]
```

## Quality Checklist

- [ ] P1 definition is strict — system-down or revenue-blocked only
- [ ] FRT clock pauses for P2-P4 outside business hours (documented)
- [ ] P1 clock never pauses (24/7/365)
- [ ] Escalation triggers automated in help desk (not manual "hey can you look at this?")
- [ ] On-call rotation documented for L3 (PagerDuty/Opsgenie)
- [ ] Enterprise SLAs documented in contract/order form
- [ ] SLA dashboard live with weekly review cadence
- [ ] Breach analysis performed monthly (root cause + fix)
- [ ] Business hours and holiday schedule published for customers

## Common Pitfalls

1. **Overpromising SLAs.** "We respond in 15 minutes to everyone" with a 2-person
   team = broken promise within 24 hours. Fix: Set SLAs your team can meet 95%+
   of the time. Underpromise, overdeliver.

2. **P1 inflation.** "The dashboard font is ugly" marked P1 by an enterprise
   customer. 6 months later, every ticket is P1 and the on-call team is burned
   out. Fix: Strict P1 criteria. CEO-approved before anyone overrides priority.

3. **No after-hours clock pause.** P3 ticket at 11pm Friday with "4-hour FRT"
   means SLA breach at 3am Saturday. Fix: P2-P4 clock pauses outside business
   hours. Communicate this clearly to customers.

4. **Auto-replies counting as FRT.** "We've received your request" is not a
   response. Customers know this. Fix: FRT = HUMAN acknowledges and begins
   working. Auto-responders are courtesy, not SLA compliance.

5. **No escalation automation.** Agent forgets to escalate at 50% SLA. Ticket
   sits for days. Customer escalates to CEO on Twitter. Fix: Automated
   escalation triggers in help desk. No human memory required.

6. **SLA breaches without follow-up.** A breached SLA without customer
   communication is a churn event. Fix: Auto-notify manager on breach.
   Template for customer communication. Post-mortem for root cause.

## Related Skills

- `support-tool-stack` — Intercom, Zendesk, Front, Help Scout setup
- `cs-playbooks` — Onboarding, health scoring, CSQLs, churn intervention
- `headless-support` — AI agents, KB, self-serve, ticket deflection
- `cs-analytics-dashboards` — CS metrics, NPS, CSAT, health scoring
- `customer-onboarding` — Structured onboarding, time-to-value
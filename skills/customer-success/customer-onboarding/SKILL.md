---
name: customer-onboarding
description: >-
  Design structured customer onboarding programs — time-to-value optimization,
  activation milestones, kickoff calls, 30-60-90 day plans, handoff from
  sales to CS, onboarding playbooks by segment, and onboarding health
  tracking. Use when building customer onboarding, reducing time-to-value,
  designing kickoff process, or scaling onboarding from founder-led to
  team-led. Triggers on: "customer onboarding", "time-to-value",
  "onboarding playbook", "kickoff call", "sales-to-CS handoff".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: customer-success
  tags: [onboarding, time-to-value, activation, customer-success, kickoff, handoff, ttv]
  related_skills: [cs-playbooks, sla-management, cs-analytics-dashboards, support-tool-stack, churn-prevention, deal-desk, revops-tech-stack, revenue-team-onboarding, data-privacy-compliance]
  frameworks:
    - "Gainsight — Time-to-Value (TTV) Framework"
    - "ChurnZero — Customer Onboarding Maturity Model"
    - "Winning by Design — Bowtie Funnel (Post-Sale Journey)"
    - "Lincoln Murphy — Customer Success Economics (desired outcome)"
    - "Donna Weber — Onboarding Matters"
---

# Customer Onboarding

## Overview

First 30 days determine years 2 and 3. The mistake: treating onboarding as a
handoff email ("here's your login, good luck") instead of a structured program
that delivers measurable value in week 1. Customers who achieve their "first
value moment" within 7 days retain at 3x the rate of those who take 30+ days.
This skill covers onboarding architecture by segment, sales-to-CS handoff,
kickoff calls, activation milestones, and the metrics to prove it works.

**Lifecycle stage:** Activation (stage 3). Canonical index → `references/gtm-lifecycle-stages.md`.  
Activation deep-dive (TTA benchmarks, experiments, audit) → `references/activation-playbook.md`.

## When to Use

Trigger phrases: "customer onboarding program", "time-to-value reduction",
"onboarding playbook", "kickoff call structure", "sales-to-CS handoff",
"30-60-90 day plan", "activation milestones", "onboarding by segment",
"scale onboarding", "TTV optimization"

## Authoritative Foundations

### Gainsight — Time-to-Value (TTV)
TTV = Time from closed-won to customer achieving their first measurable value.
For most B2B SaaS: TTV under 7 days = high retention. Under 30 days = healthy.
60+ days = churn risk. Measure TTV by segment, not company-wide.

### Lincoln Murphy — Desired Outcome
Onboarding isn't about teaching features. It's about getting the customer to
THEIR desired outcome, not yours. Stop asking "did they complete setup?" and
start asking "did they achieve what they bought the product for?"

### Donna Weber — Onboarding Matters
"The way you onboard customers is the way they'll use your product forever."
Patterns set in week 1 persist for years. Bad patterns = bad retention.

## Step-by-Step Process

### Phase 1: Onboarding Architecture by Segment

| Segment | ACV | Onboarding Model | Duration | CSM Ratio |
|---|---|---|---|---|
| **Enterprise** | $50K+ | White-glove: dedicated CSM, weekly calls, custom setup | 30-90 days | 1:10-20 |
| **Mid-Market** | $10-50K | Guided: structured program, biweekly calls, templates | 14-30 days | 1:20-50 |
| **SMB** | $1-10K | Automated: email sequences, in-app guides, office hours | 7-14 days | 1:100+ |
| **Self-Serve** | <$1K | Product-led: in-app only, KB, community, no CSM | <1 day | ∞ |

**Onboarding delivery methods by tier:**

| Method | Enterprise | Mid-Market | SMB | Self-Serve |
|---|---|---|---|---|
| Dedicated CSM kickoff call | ✓ | ✓ | | |
| Weekly check-in calls | ✓ | ✓ (first month) | | |
| Onboarding email sequence | ✓ | ✓ | ✓ | ✓ |
| In-app product tour | ✓ | ✓ | ✓ | ✓ |
| Knowledge base / help center | ✓ | ✓ | ✓ | ✓ |
| Video tutorials (Loom/library) | ✓ | ✓ | ✓ | ✓ |
| Group onboarding webinars | | ✓ | ✓ | ✓ |
| Office hours (weekly drop-in) | | ✓ | ✓ | |
| Community / Slack | | | ✓ | ✓ |

### Phase 2: Sales-to-CS Handoff

**The handoff is where most value leaks.** Sales promises X. CS doesn't know
about X. Customer expects X. Nobody delivers X.

**Handoff template (Sales completes before CS takes over):**
```
SALES-TO-CS HANDOFF — [Customer Name]

Deal Details:
- Plan: [tier] at $[ACV]
- Contract length: [monthly/annual/multi-year]
- Products purchased: [list]

Customer's Stated Goals:
1. [Goal 1] — Success looks like: [specific outcome]
2. [Goal 2] — Success looks like: [specific outcome]

Key Contacts:
- Champion: [name], [title], [email], [phone], [LinkedIn]
- Executive Sponsor: [name], [title]
- Daily Users: [names]
- Decision Maker: [name], [title]

What We Promised:
- [Feature/capability they're most excited about]
- [Timeline expectation set during sales]
- [Any special pricing or terms]

Sales Notes:
- [Personality, communication style, hot buttons]
- [Competitive situation: why they chose us, who we beat]
- [Risks: what could go wrong in onboarding]
- [Expansion opportunity: what they might buy next]

Technical Setup Needed:
- [Integrations to configure]
- [Data to import]
- [SSO/custom domain/etc.]

Data Exchange Handoff (required for any customer data):
- Data already received in sales/POC: [yes/no — what, via which channel]
- Retention / deletion date from POC: [date]
- DPA / security review status: [complete / N/A]
- Approved import method for go-live: [in-app / customer SFTP / secure share]
- Fields approved for import (not "full dump"): [list]
```

Load `references/gtm-data-exchange-playbook.md` before requesting imports.
Checklist → `deal-desk` → `skills/sales-revops/deal-desk/templates/customer-data-exchange-checklist.md`.
CS must **not** re-request data sales already collected via email.

**Handoff meeting (30 min, Sales + CSM + AE):**
1. Sales presents the account (10 min — from handoff doc)
2. CSM asks questions (10 min — risks, timeline, personalities)
3. CSM introduces themselves to customer (10 min — warm handoff email/call)

### Phase 3: The Kickoff Call

**Enterprise / Mid-Market kickoff call (60 min):**
```
AGENDA — [Customer Name] Kickoff

1. Introductions (5 min)
   - CSM introduces themselves, their role, how to reach them
   - Customer introduces their team and roles

2. Goals & Success Criteria (15 min)
   - "What does success look like in 30/60/90 days?"
   - Document measurable outcomes, not vague aspirations
   - "What problem are you trying to solve first?"

3. Implementation Plan (15 min)
   - Walk through timeline: setup, integration, data import, training
   - Assign owners: who on their team does what, who on ours
   - Set first milestone: "By next week, you'll have X working"

4. Training Plan (10 min)
   - Who needs training? When?
   - Admin training vs end-user training
   - Schedule sessions now (don't leave as "we'll figure it out")

5. Communication & Escalation (5 min)
   - How to reach CSM: email, Slack, Calendly
   - Escalation path if something goes wrong
   - Cadence: weekly calls for first month, then biweekly

6. Next Steps (5 min)
   - Recap: 3 action items with owners and due dates
   - Schedule next call
   - Send follow-up email within 1 hour

Post-call: Send "Welcome to [Product]" email with:
  - Kickoff recording
  - Success plan document (what you agreed on)
  - Links to setup guides, training schedules
  - CSM's Calendly link for ad hoc calls
```

**SMB kickoff (automated):**
```
ONBOARDING EMAIL SEQUENCE — Day 0-14

Day 0 (immediate): Welcome email
  "Welcome to [Product]! Your account is ready.
   Step 1: [key action] → takes 5 minutes
   Step 2: [key action] → takes 10 minutes
   Your CSM is [name] — book a call: [Calendly]"

Day 1: Getting Started Guide
  "Here's how [similar customer] got set up in 2 days."

Day 3: Integration Setup
  "Connect [Product] to your stack. 5-min setup guide."

Day 7: First Value Check
  "You should have [outcome] by now. If not, here's help."

Day 14: Advanced Features
  "Now that you're set up, here's how power users [do X]."
```

### Phase 4: Activation Milestones

**Define activation per product — 3-5 milestones:**

```
ONBOARDING MILESTONES — [Product Name]

Milestone 1: Technical Setup (target: Day 0-1)
- [ ] Account created and email verified
- [ ] Team members invited
- [ ] Integration connected (CRM, email, etc.)

Milestone 2: First Value (target: Day 3-7)
- [ ] First campaign/report/workflow created
- [ ] First result/output generated
- [ ] Customer sees value with their own data

Milestone 3: Habit Formation (target: Day 14-21)
- [ ] Used product 3+ times
- [ ] Multiple team members active
- [ ] Product becomes part of their workflow

Milestone 4: Expansion Readiness (target: Day 60-90)
- [ ] Using core features weekly
- [ ] Champion advocates internally
- [ ] Identified additional use cases or departments
```

**Activation tracking dashboard:**
```
ONBOARDING FUNNEL — Current Cohort (30 accounts)

| Milestone | Completed | In Progress | Stuck | Drop-off |
|---|---|---|---|---|
| Setup Complete | 28 (93%) | 2 (7%) | 0 | 0 |
| First Value | 22 (73%) | 6 (20%) | 2 (7%) | 0 |
| Habit Formed | 18 (60%) | 8 (27%) | 2 (7%) | 2 (7%) |
| Expansion Ready | 12 (40%) | — | — | — |
```

### Phase 5: 30-60-90 Day Plan

**Template for every onboarded customer (customized per account):**

```
30-60-90 SUCCESS PLAN — [Customer Name]

DAY 0-30: Foundation
Goal: [specific milestone]
- [ ] Technical setup complete
- [ ] First value achieved (measured by: [metric])
- [ ] Core team trained
- [ ] Weekly check-in calls
CSM actions: 2 calls, 3 emails, 1 training session

DAY 30-60: Adoption
Goal: [specific milestone]
- [ ] All team members active
- [ ] Using advanced features ([specific features])
- [ ] First expansion opportunity identified
- [ ] Biweekly check-in calls
CSM actions: 2 calls, 2 emails, 1 business review prep

DAY 60-90: Expansion
Goal: [specific milestone]
- [ ] QBR scheduled
- [ ] ROI documented (saved $X, reduced time Y%, improved Z)
- [ ] Expansion proposal presented (if applicable)
- [ ] Case study / reference request
CSM actions: QBR prep + presentation, expansion proposal
```

### Phase 6: Measuring Onboarding

**Core onboarding metrics:**

| Metric | Formula | Target |
|---|---|---|
| Time to First Value (TTFV) | Days from close to milestone 2 | <7 days (SMB), <14 days (MM), <30 days (Enterprise) |
| Onboarding Completion Rate | Completed / Started onboarding | >90% |
| Time to Full Adoption | Days from close to all milestones | <30 days (SMB), <60 days (MM), <90 days (Enterprise) |
| Onboarding CSAT | CSAT at 14 and 30 days | >4.5/5 |
| 90-Day Churn | Accounts churned within 90 days / Total | <5% |
| Onboarding → Expansion Rate | Expanded within 90 days / Onboarded | >15% |

## Output Format

```
ONBOARDING PROGRAM — [Company]

Programs by Segment:
[Table: segment, ACV, model, duration, CSM ratio]

Milestones:
1. Technical Setup: [tasks + target day]
2. First Value: [tasks + target day]
3. Habit Formation: [tasks + target day]
4. Expansion Readiness: [tasks + target day]

Kickoff Call Agenda:
[60-min agenda for Enterprise/MM, email sequence for SMB]

Sales-to-CS Handoff Template:
[Template with fields: deal details, goals, contacts, promises, notes]

30-60-90 Day Plan Template:
[Day 0-30: Foundation, Day 30-60: Adoption, Day 60-90: Expansion]

Automated Sequences:
- Email sequence (Day 0-14 for SMB)
- In-app product tour (triggers + content)
- Office hours (weekly, drop-in)

Metrics Dashboard:
- TTFV, completion rate, CSAT, 90-day churn, expansion rate
```

## Implementation Checklist

- [ ] Onboarding segmented by ACV (no one-size-fits-all program)
- [ ] Activation milestones are measurable (not "customer is happy")
- [ ] Sales-to-CS handoff template used for every new account
- [ ] Kickoff call has standard agenda with time allocations
- [ ] 30-60-90 day plan customized per customer (not copy-paste)
- [ ] Time to First Value measured and tracked weekly
- [ ] At-risk flag for accounts stuck on a milestone >X days
- [ ] Automated sequence for SMB (doesn't require CSM manual emails)
- [ ] Onboarding CSAT survey at Day 14 and Day 30
- [ ] 90-day churn tracked separately (distinct from overall churn)

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **One onboarding for all.** Enterprise customer with 500 seats and a $100K
   deal gets the same onboarding as a $500/mo SMB customer. Enterprise feels
   neglected. SMB feels overwhelmed. Fix: Segment by ACV. Different programs.

2. **Features over outcomes.** "Click here, then here, then here" teaches
   mechanics, not value. Fix: Every onboarding step links to the customer's
   desired outcome. "This step gets you to [their goal]."

3. **No handoff from sales.** CSM discovers on the kickoff call that Sales
   promised features that don't exist, committed to a timeline CS can't hit,
   and didn't mention the customer is about to be acquired. Fix: Mandatory
   handoff document AND meeting for every account.

4. **"We'll schedule training later."** If training isn't on the calendar
   during the kickoff call, it won't happen. The customer gets busy. Usage
   drops. Churn follows. Fix: Schedule all training sessions during kickoff.

5. **Measuring activity instead of outcomes.** "# of kickoff calls completed"
   is an activity. "% of customers achieving First Value within 7 days" is an
   outcome. Fix: Track outcome metrics, not activity metrics.

6. **Ghosting after setup.** Week 1: daily emails, 2 calls. Week 2: radio
   silence. Customer wonders if you still exist. Fix: Structured cadence.
   Weekly calls for month 1, biweekly for month 2, monthly thereafter.

## Customer Data Exchange (GTM)

Onboarding is when CS most often requests customer exports, credentials, and
integration access. Same rules as sales — minimum data, approved channels,
documented retention.

| Do | Don't |
|---|---|
| Re-use sales-approved channel and scope | Re-request same export via email attachment |
| Confirm DPA before ongoing PII processing | Ask for production passwords to "speed setup" |
| Log import fields in kickoff doc | Slack-file customer CSVs to implementation |

Canonical playbook → `references/gtm-data-exchange-playbook.md`. Enterprise
security timing (if review still open) → `references/security-questionnaire-deal-guide.md`.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator
**Canonical lifecycle (repo root):**
- `references/activation-playbook.md` — First value event, handoff, audit checklist
- `references/gtm-lifecycle-stages.md` — Activation row + Bowtie neck
- `references/lifecycle-metrics-by-stage.md` — TTA, activation rate thresholds
- `skills/analytics/gtm-metrics/templates/lifecycle-monitoring-dashboard.md` — Weekly activation panel
- `skills/analytics/gtm-metrics/templates/stage-health-scorecard.md` — Activation R/Y/G
- `references/gtm-data-exchange-playbook.md` — Customer data exchange SOP (repo root)
- `references/crisis-management-playbook.md` — Post-incident trust rebuild; activation recovery (Pattern 33)
- `deal-desk/templates/customer-data-exchange-checklist.md` — Pre/on/post-sale checklist

## Related Skills

- `deal-desk` — Enterprise security review + pre-sale data boundaries
- `revops-tech-stack` — Where customer data lives in the GTM stack
- `revenue-team-onboarding` — CSM security hygiene basics
- `cs-playbooks` — Playbooks for health scoring, CSQLs, churn intervention
- `sla-management` — Onboarding support SLAs, escalation
- `cs-analytics-dashboards` — TTFV metrics, onboarding funnel, health scores
- `support-tool-stack` — Platform for onboarding comms and tracking
- `churn-prevention` — 90-day churn is an onboarding metric
- `gtm-leadership` — Crisis comms; re-onboarding at-risk accounts after incidents
- `expansion-selling` — Onboarding → expansion handoff
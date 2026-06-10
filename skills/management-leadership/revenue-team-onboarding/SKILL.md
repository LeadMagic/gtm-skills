---
name: revenue-team-onboarding
description: >-
  Revenue team onboarding — security access provisioning, ramp schedules, 30-60-90
  plans, Slack engagement, shadowing, certification, and time-to-first-meeting
  reduction. Use when onboarding SDRs, AEs, managers, or RevOps hires. Triggers on:
  "sales onboarding", "SDR ramp", "30-60-90 sales", "reduce ramp time", "Slack
  for sales team", "security onboarding employees", "new rep onboarding", "sales
  bootcamp".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.6.0"
  author: LeadMagic
  category: management-leadership
  tags: [onboarding, ramp, security, slack, enablement, sdr, ae]
  related_skills:
    - sales-enablement
    - sales-coaching
    - gtm-leadership
    - soc2-compliance
    - security-assessments
    - pipeline-management
    - sales-team-building
    - gtm-role-descriptions
    - revops-tech-stack
    - deal-desk
    - customer-onboarding
  frameworks:
    - "Mark Roberge — Sales Acceleration Formula onboarding machine"
    - "Winning by Design — REKS ramp and certification"
    - "Jon Barrows (Sell Better) — Practical sales training cadence"
    - "Kevin Dorsey — Sales leadership onboarding standards"
    - "Jason Bay (Outbound Squad) — SDR messaging certification"
    - "Henry Schuck (ZoomInfo) — Inbound SDR speed-to-lead standards"
    - "Varun Anand (Clay) — Reverse demo certification"
    - "Ryan Reisert — CRM Activity Buckets & cold call ramp"
    - "Ronen Pessar — ColdCall-Market Fit certification gate"
    - "Tom Slocum — 3×3 research & sell-the-meeting standards"
    - "Stacey Nordwall (Culture Amp / Pyn) — Culture-first onboarding, onboarding surveys, remote GTM norms"
    - "Tito Bohrt (AltiSales) — Leading-indicator SDR ramp & call-recording coaching"
---

# Revenue Team Onboarding

## Overview

Ramp is a **system output**, not a personality test. Slow ramp usually means
broken onboarding: no security access day one, no shadow path, Slack chaos,
and enablement PDFs nobody opens. This skill designs revenue onboarding:
**security-first access**, structured 30-60-90, certification gates, and Slack
norms that accelerate time-to-first-qualified-meeting.

**Parallel lifecycle:** Revenue team Hire → Ramp → Productivity → Promotion/Exit.  
Customer lifecycle index → `references/gtm-lifecycle-stages.md` (team table).  
Ramp metrics → `references/lifecycle-metrics-by-stage.md` (Revenue Team Ramp).  
Comp plans must align with ramp credit — `executive-compensation/references/gtm-compensation-strategy.md`
(Pattern 35) · `references/benchmark-reconciliation.md` (ramp vs productivity).

Enablement assets → `sales-enablement`. Coaching → `sales-coaching` (REKS).
Process → `pipeline-management`.

## When to Use

- "Onboard new SDR/AE"
- "Onboard GTM Engineer / RevOps hire"
- "30-60-90 plan for sales hire"
- "Reduce ramp time"
- "Slack channels for sales team"
- "Security onboarding for GTM hires"
- "Sales bootcamp week one"

## Authoritative Foundations

- **Mark Roberge.** Onboarding as measurable machine: time-to-first-call, certification scores, conversion ramp curves.
- **Winning by Design (Jacco van der Kooij).** REKS diagnostic from week 3; certify on SPICED, not just product trivia.
- **Jon Barrows (Sell Better).** Skills training in short reps — objection, discovery, demo structure.
- **Kevin Dorsey.** Manager standards: daily coaching rhythm during ramp.
- **Jason Bay.** SDR messaging quality — certify outbound before live sends.
- **Henry Schuck (ZoomInfo).** Inbound SDR ramp emphasizes **speed-to-lead**
  tooling and queue certification before live MQL access — public benchmark
  <90s response. See `sales-team-building` → `henry-schuck-sdr-model.md`.
- **Varun Anand (Clay).** Certify reps on **reverse demo** (prospect screen-share,
  first-win in 30 min) before solo PLG-hybrid demos — `demo-scripts` →
  `reverse-demo-varun.md`.
- **Ryan Reisert — CRM Activity Buckets.** Week 2–3: certify reps on four contact
  stages and backwards daily workflow before unsupervised dialing.
  → `references/ryan-reisert-cold-calling.md`
- **Ronen Pessar — ColdCall-Market Fit.** Phone SDRs: certify on pattern-interrupt
  opener + 50-call disposition review before full quota. Manager validates
  connect → completion → meeting funnel. → `references/ronen-pessar-cold-calling.md`
- **Tom Slocum — 3×3 + sell-the-meeting.** Week 1 cert: 3 insights in 3 minutes
  on mock accounts; intro calls reviewed for meeting-sell (not product pitch).
  → `references/tom-slocum-cold-calling.md`
- **Tito Bohrt (AltiSales).** Ramp to **leading indicators**, not dials: certify the
  funnel bottom-up (meetings completed → set → conversations → dials) to a ~**80–85%
  show rate**, and coach from **call recordings** (AltiSales reviews ~100% of a new
  rep's calls, then samples). Treat ramp as a **system output** (data + scripts +
  coaching). Canonical →
  `skills/founder-led/sales-team-building/references/tito-bohrt-sdr-science.md`.

**Phone SDR ramp (weeks 2–4):** Shadow live calls → CallBlitz or manager listen-in
→ 3×3 prep on every block → CRM Buckets + Gilkey disposition fields live →
50 completions before solo list ownership. Load `cold-calling` + `references/cold-calling-experts-index.md`.

- **Stacey Nordwall (Culture Amp / Pyn).** HR-side ramp system: day-14/30/60 onboarding
  pulses, manager closes feedback loop within one week, role-specific paths for SDR vs
  AE vs RevOps. Canonical → `gtm-role-descriptions/references/hr-gtm-playbook.md`.
  **Ramp timeline reconciliation:** 30-60-90 milestones vs 4.5–6 month full AE
  productivity → `references/benchmark-reconciliation.md` (do not conflate quota-bearing
  day 90 with tenured-level output).

## Step-by-Step Process

### Phase 1: Pre-Start (Security & Access)

**Day 0 checklist** — load `references/security-access-checklist.md`:

| System | Owner | SLA |
|---|---|---|
| Email + calendar | IT | Day 0 |
| CRM (least privilege) | RevOps | Day 0 |
| Sequencer | RevOps | Day 1 |
| Slack | IT | Day 0 |
| Gong / call recorder | RevOps | Day 1 |
| Enrichment tools | RevOps | Day 1 |
| Clay + n8n (GTM Engineer) | RevOps / GTM Eng manager | Day 0–1 |
| SSO / MFA enforced | IT | Day 0 |
| Laptop + MDM | IT | Before start |

**SOC2-aligned:** No production customer data until security training complete.
Log access grants. Offboard within 24h on termination (`soc2-compliance`).

**Rep security hygiene (non-technical):** Before live customer contact, every
GTM hire completes password manager + MFA on email, CRM, Slack, and sequencer;
reads phishing patterns and demo screen-share checklist. Load
`references/gtm-security-hygiene-basics.md` (repo root). Customer data rules →
`references/gtm-data-exchange-playbook.md`.

### Phase 2: Week 1 — Immersion

| Day | Activity |
|---|---|
| 1 | Company, ICP, product demo, tool access verify |
| 2 | Shadow 4 live calls (SDR or AE) |
| 3 | Pipeline stages + CRM hygiene (`pipeline-management`) |
| 4 | Messaging certification (`sales-enablement`) |
| 5 | Mock discovery + manager sign-off |

**Slack:** Add to `#sales-team`, `#wins`, `#deal-desk` — not 20 channels day one.
Load `references/slack-engagement.md`.

**Week 1 questions (both sides):** Manager and new hire align expectations via
`references/onboarding-questions.md` and `templates/new-hire-questionnaire.md`
(Roberge onboarding machine — diagnose ramp blockers early).

### Phase 3: 30-60-90 Plan

| Period | SDR | AE |
|---|---|---|
| **30** | Certified messaging; 50 calls; 5 meetings held | Shadow 10 calls; 2 self-sourced opps |
| **60** | 50% quota; SQO quality pass | 50% quota; full cycle on 1 deal |
| **90** | Full quota | Full quota; forecast in CRM |

Template: `templates/30-60-90-sales.md`

**GTM Engineer / RevOps:** Use OKR-based 30-60-90 from `gtm-role-descriptions` →
`skills/founder-led/gtm-role-descriptions/templates/gtm-engineer-jd.md` (stack audit week 1, one quick-win workflow,
production runbooks by day 90). Interview handoff context: `gtm-engineer-hiring.md`.

### Phase 4: Certification Gates

No live outbound until:

- [ ] ICP quiz pass
- [ ] CRM hygiene lab pass
- [ ] Recorded mock call score ≥4/5
- [ ] Security training complete
- [ ] Password manager + MFA verified (`gtm-security-hygiene-basics.md`)
- [ ] Messaging doc peer-reviewed (Jason Bay PVP-style for outbound)

### Phase 5: Ramp Reduction Tactics

| Tactic | Impact |
|---|---|
| Pre-built lists in CRM day 1 | -2 weeks to first meeting |
| Buddy SDR/AE for 4 weeks | +20% 90-day attainment |
| Daily 15-min manager coaching (Kevin Dorsey) | Faster skill correction — `sales-coaching` call rubric |
| Gong library "top 10 calls" | Pattern recognition |
| SPICED cheat sheet on second monitor | Better discovery scores |

### Phase 6: Slack Engagement Norms

- **Daily standup thread** in `#sales-team` (async-friendly)
- **Win reactions** in `#wins` — manager amplifies
- **Deal help** in `#deal-desk` with SPICED context required
- **No DM-only questions** that should be team learning
- **Response SLA:** manager <4h on ramp blockers

### Phase 7: Measure Ramp

| Metric | Target |
|---|---|
| Days to first qualified meeting | SDR <21; AE <30 |
| Days to first opp created | AE <45 |
| 90-day attainment | ≥70% of tenured baseline |
| CRM hygiene score | ≥90% required fields |

## Output Format

- 30-60-90 plan per role
- Security access checklist with owners
- Certification rubric
- Slack channel map
- Ramp metrics dashboard spec

## Quality Check

- [ ] Day 0 access defined (CRM, email, Slack, MFA)
- [ ] Certification before live customer contact
- [ ] 30-60-90 measurable outcomes per role
- [ ] Manager daily coaching cadence week 1–4
- [ ] Slack norms documented (≤5 channels week 1)
- [ ] Ramp metrics with targets

## Common Pitfalls

1. **Tools day 5.** Rep sits idle. Fix: RevOps SLA day 0–1.
2. **PDF dump.** Fix: shadowing + certification.
3. **Live sends day 1.** Brand damage. Fix: certify messaging first.
4. **Slack channel sprawl.** Fix: core 3 channels, expand week 3.
5. **No security training.** SOC2 audit fail. Fix: gate production access.

## Execution Artifacts

- `references/security-access-checklist.md`
- `references/gtm-security-hygiene-basics.md` — Passwords, 2FA, phishing, demo screen share (repo root)
- `references/gtm-data-exchange-playbook.md` — Customer data exchange SOP (repo root)
- `references/slack-engagement.md`
- `references/ramp-benchmarks.md`
- `../../founder-led/gtm-role-descriptions/references/hr-gtm-playbook.md` — HR GTM onboarding system (Stacey Nordwall)
- `templates/30-60-90-sales.md`
- `templates/certification-rubric.md`
- `references/onboarding-questions.md` — manager ↔ new hire question banks
- `templates/new-hire-questionnaire.md` — Week 1 joint form
- `references/cold-calling-experts-index.md` — phone ramp router (repo root)
- `references/ryan-reisert-cold-calling.md` — CRM Buckets certification (repo root)
- `references/ronen-pessar-cold-calling.md` — ColdCall-Market Fit gate (repo root)
- `references/tom-slocum-cold-calling.md` — 3×3 + sell-the-meeting (repo root)
- `references/framework-notes.md`
- `templates/output-template.md`
- `scripts/check-output.py`

**Canonical lifecycle (repo root):** `references/gtm-lifecycle-stages.md` (Revenue Team Lifecycle) · `skills/analytics/gtm-metrics/templates/lifecycle-monitoring-dashboard.md` (Ramp panel) · `references/lifecycle-metrics-by-stage.md` (ramp metrics)

## Related Skills

- `sales-enablement` — collateral and playbook
- `sales-coaching` — REKS ongoing
- `soc2-compliance` — access control
- `deal-desk` — enterprise security review + customer data checklist
- `customer-onboarding` — post-sale data handoff boundaries
- `gtm-leadership` — manager accountability
- `pipeline-management` — stage certification

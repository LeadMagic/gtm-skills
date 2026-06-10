---
name: meeting-prep
description: >-
  Prepare meeting briefs with SPICED discovery (WbD) and MEDDICC qualification
  (Andy Whyte) — account research, attendee profiles, question banks, scorecard
  gaps, and competitive context. Use before discovery calls, demos, executive
  meetings, or deal reviews. Triggers on: "meeting prep", "call prep",
  "discovery prep", "MEDDICC", "MEDDIC", "qualify this deal", "pre-call research",
  "discovery questions", "champion test", "economic buyer".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: sales-revops
  tags: [meeting-prep, discovery, call-prep, spiced, meddicc, qualification]
  related_skills: [pipeline-management, competitive-intel, objection-handling, demo-scripts, multi-thread-orchestration, roi-calculator]
  frameworks:
    - "Winning by Design — SPICED"
    - "Keenan — Gap Selling"
    - "Andy Whyte — MEDDICC Qualification"
    - "Force Management — MEDDICC Methodology"
    - "Huthwaite — SPIN Selling"
    - "Gartner — Challenger Sale"
---

# Meeting Prep

## Overview

Win rates are decided before the call. This skill produces a one-page brief:
account snapshot, attendee profiles, tailored question banks, and — for active
deals — a MEDDICC gap analysis showing which dimensions still need evidence.

**SPICED** (Winning by Design) structures early discovery conversations.
**Gap Selling** (Keenan) deepens problem diagnosis — current state, future state, quantified gap, root cause, happy-ears guardrails.
**MEDDICC** (Andy Whyte) scores deal qualification with evidence. They do not
contradict — SPICED uncovers; MEDDICC scores. Both map to the same CRM fields
defined in `pipeline-management`.

## When to Use

- "Prep me for a call with [company]"
- "Discovery questions for [prospect]"
- "MEDDICC score this deal" or "what's missing on MEDDICC?"
- "Champion test — is this contact a real champion?"
- "Brief me before my demo / exec meeting"
- "Pre-call research for [account]"

For full sales process design, load `pipeline-management` first.

## Authoritative Foundations

- **Winning by Design — SPICED.** Situation, Pain, Impact, Critical Event,
  Decision — progressive discovery in Connect and Discovery stages. Critical
  Event is the urgency gate: no CE, no timeline.
- **Keenan — Gap Selling.** Problem Centric™ discovery: map Current State
  (situation, problem, impact, root cause, emotions) → Future State → Gap.
  Spend ~25% of cycle on diagnosis; build Problem Identification Chart before
  calls. Anti-pattern: **happy ears** — validate impact, don't assume yes.
  Full playbook → `references/keenan-gap-selling.md`.
- **Andy Whyte — MEDDICC (MEDDICC.com).** Seven dimensions scored 0/1/2 with
  evidence: Metrics, Economic Buyer, Decision Criteria, Decision Process,
  Identify Pain, Champion, Competition. "Always Be Qualifying" — re-score after
  every interaction. Champion must pass four tests before Proposal.
- **Force Management — MEDDICC Methodology.** Source framework for enterprise
  qualification; Whyte's scorecard operationalizes it for deal inspection.
- **Huthwaite — SPIN.** Question flow for conversational discovery — complements
  SPICED, does not replace it.
- **Challenger — Teach-Tailor-Take Control.** Lead with insight, not interrogation.

### SPICED + MEDDICC — how they work together

| Call Type | Lead With | Score With |
|---|---|---|
| First discovery | SPICED + Gap Selling (current state) | Light MEDDICC (note gaps) |
| Second+ meeting | SPICED gaps + Gap (future state) | Full MEDDICC scorecard |
| Pre-proposal / exec | Economic buyer prep | MEDDICC must be ≥10/14 |
| Deal review (internal) | — | MEDDICC evidence inspection |

## Step-by-Step Process

### Phase 1: Account Research (5 min)

- Company size, industry, revenue, headquarters
- Recent news (funding, hires, launches) — potential Critical Events
- Tech stack and pain signals
- Competitive landscape and status quo risk

### Phase 2: Attendee Research

Per attendee: role, tenure, priorities, LinkedIn activity, likely MEDDICC role
(Champion? Economic Buyer? Technical Buyer? Blocker?).

### Phase 3: SPICED Question Bank (Discovery Calls)

| SPICED | Question Examples |
|---|---|
| **S**ituation | "Walk me through how your team handles [process] today." |
| **P**ain | "What's the most frustrating part of that approach?" |
| **I**mpact | "What does that cost you annually — rough order of magnitude?" |
| **C**ritical Event | "Why is fixing this a priority now versus six months from now?" |
| **D**ecision | "If we find a fit, what does your evaluation process look like?" |

### Phase 4: MEDDICC Question Bank (Qualification Calls)

| Dimension | Question Examples | Confirmed When |
|---|---|---|
| **M**etrics | "How would you measure success 12 months after implementation?" | Baseline + target KPI documented |
| **E**conomic Buyer | "Who ultimately approves budget for initiatives like this?" | EB named; meeting scheduled or completed |
| **D**ecision Criteria | "What are the must-haves vs nice-to-haves in your evaluation?" | Criteria list documented |
| **D**ecision Process | "Walk me through each step from today to signed contract." | Steps, owners, dates mapped |
| **I**dentify Pain | "What happens if this problem isn't solved by [date]?" | Quantified cost of inaction |
| **C**hampion | "Would you be comfortable presenting this internally without us?" | Four-part Champion test passed |
| **C**ompetition | "Who else are you evaluating — including doing nothing?" | Competitors + status quo named |

### Phase 5: Andy Whyte — Champion Test

Score the contact before calling them a Champion:

| # | Criterion | Evidence Required |
|---|---|---|
| 1 | Power to influence the decision | Can access EB and decision committee |
| 2 | Personal win if deal closes | Career, team, or KPI benefit articulated |
| 3 | Articulates problem without you | Repeats pain accurately in their words |
| 4 | Commits to internal selling | Agrees to present or multi-thread on your behalf |

All four required for Champion score = 2. Enthusiasm alone = 1 at best.

### Phase 6: MEDDICC Gap Analysis (Active Deals)

If CRM data exists, score current state and list gaps to close on this call:

```
MEDDICC Score: __/14
Gaps to close this meeting:
- [ ] Metrics — need quantified baseline
- [ ] Economic Buyer — identified but not met
- ...
```

Load `pipeline-management` for stage gate minimums before advancing the deal.

### Phase 7: Competitive Context

- Named competitors and status quo
- Decision criteria influence strategy (`competitive-intel`)
- Trap-setting questions for differentiators

## Output Format

One-page meeting brief. Use `templates/output-template.md` for structure.

```
# Meeting Brief: [Company]
Date | Attendees | Deal stage | MEDDICC score: __/14

## Company Snapshot
## Attendee Profiles (+ MEDDICC role)
## SPICED Questions (discovery)
## MEDDICC Questions (gaps to close)
## Champion Test (if applicable)
## Competitive Context
## Desired Outcome + Fallback
```

## Quality Check

- [ ] Account and attendee research current (last 30 days)
- [ ] Questions tailored to account — not generic templates
- [ ] SPICED questions included for discovery; MEDDICC for qualification deals
- [ ] Champion test applied if a champion is claimed
- [ ] MEDDICC gaps listed for active deals with target score for this meeting
- [ ] Brief readable in 60 seconds
- [ ] SPICED and MEDDICC map to same CRM fields — no conflicting data capture

## Common Pitfalls

1. **MEDDICC as a discovery script.** Running all seven dimensions on a first call
   feels like an audit. Fix: SPICED first; MEDDICC scores build over calls.

2. **Champion = friendly contact.** Enthusiasm without power is score 1, not 2.
   Fix: apply Whyte's four-part Champion test.

3. **Vendor-defined Metrics.** "You'll save 30%" is not M=2. Fix: buyer must
   name the KPI and baseline.

4. **Ignoring status quo as Competition.** "No competitors" still has a competitor:
   do nothing. Fix: always assess status quo.

5. **SPICED and MEDDICC in separate silos.** Reps capture Impact in SPICED notes
   but leave Metrics blank. Fix: Impact field populates Metrics in CRM.

## Execution Artifacts

- `references/framework-notes.md` — SPICED/MEDDICC map, Champion test, question banks
- `references/keenan-gap-selling.md` — Gap Selling discovery, PIC, happy ears, checklists
- `templates/output-template.md` — one-page brief structure
- `scripts/check-output.py` — validates brief sections

## Related Skills

- `pipeline-management` — Stage gates, CRM fields, MEDDICC scorecard rules
- `sales-coaching` — Manager deal review using same scorecard
- `competitive-intel` — Battlecards for Competition dimension
- `multi-thread-orchestration` — When Champion cannot access EB alone
- `roi-calculator` — Metrics dimension business case
- `demo-scripts` — Post-discovery demo structure

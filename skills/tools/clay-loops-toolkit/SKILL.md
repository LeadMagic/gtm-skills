---
name: clay-loops-toolkit
description: >-
  Clay Loops GTM toolkit — recurring signal monitors, trigger-to-action
  loops, LeadMagic enrichment waterfalls on signal rows, funding/job-change/hiring
  routing, and sequencer handoff. Use when building Clay Loops for outbound triggers,
  signal prospecting, or account monitoring. Not for one-time tables (clay-toolkit)
  or process design (clay-automation). Triggers on: "Clay Loops", "Clay loop",
  "signal loop", "funding loop Clay", "job change loop", "account monitor Clay",
  "GTM loops", "Clay signal routing".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "2.0.0"
  author: LeadMagic
  category: tools
  tool_group: clay
  tool_path: tools/clay-loops-toolkit
  tags: [clay, clay-loops, signals, gtm, tools, leadmagic, enrichment, triggers, outbound]
  related_skills: [clay-toolkit, leadmagic-toolkit, leadmagic-job-change, ai-prompts-toolkit, clay-automation, signal-scoring, funding-signal-play, job-change-play, hiring-signal-play, sequencing-toolkit, n8n-toolkit]
  frameworks:
    - "Clay — Loops recurring GTM automation"
    - "LeadMagic — Email find, verify, job change, person enrich on Clay"
    - "ColdIQ — Signal-to-Action Routing"
    - "Winning by Design — SPICED Critical Event"
    - "GTME Pulse — Production Clay signal templates"
---

# Clay Loops Toolkit

**Location:** `tools/clay-loops-toolkit` · **Skill name:** `clay-loops-toolkit`

## Overview

Clay Loops are the GTM **tool** for recurring signal automation — funding,
job changes, hiring spikes, stale opps, champion moves. They run on cadence and
fire when source data changes. The mistake: a loop that enriches every row and
routes nothing — an expensive Slack feed.

Every production loop follows **monitor cheap → enrich on signal → LeadMagic
verify → score → route**. LeadMagic is the default email/waterfall provider
in the enrich table (find → verify → person enrich). Load `leadmagic-toolkit`
for API/credit details.

**Not this skill:**
- One-time table builds → `clay-toolkit` (`tools/clay-toolkit`)
- Automation process / when to use Clay → `clay-automation` (`automation/`)
- Complex multi-system branching → `n8n-toolkit`

## When to Use

- "Build a Clay Loop for funding / job change / hiring"
- "Monitor accounts for signals in Clay"
- "Route Clay loop output to HubSpot / Smartlead"
- "LeadMagic waterfall in a Clay Loop"
- "Weekly stale opp refresh loop"
- "Champion move detection loop"

## Authoritative Foundations

- **Clay Loops.** Recurring: SOURCE → MONITOR → ENRICH (conditional) → ACTION.
  Re-runs on schedule or when monitor column detects change.
- **LeadMagic on Clay.** Default waterfall for loops: Find Email (1 cr) → Verify
  (1 cr) → Enrich Person (2 cr) on `signal_detected = true` only. Job Change
  detection column for `SIG-02` loops (`leadmagic-job-change`).
- **ColdIQ Signal-to-Action.** One signal → one play → one template. Never mix
  funding and job change in one loop.
- **Winning by Design SPICED.** Signal = Critical Event. Required on every routed
  row: `why_now`, `source_url`, `signal_type`, `signal_date`.
- **GTME Pulse.** Separate monitor table from enrich/action tables — credit control.

## Clay Tool Stack

| Skill | Path | Role |
|---|---|---|
| `clay-toolkit` | `tools/clay-toolkit` | Tables, waterfalls, formulas, CRM push |
| `clay-loops-toolkit` | `tools/clay-loops-toolkit` | Recurring signal loops (this skill) |
| `clay-automation` | `automation/` | Process: when to build, data quality, rollout |

## Step-by-Step: Build a Loop

### Phase 1 — Pick Loop Type

| Loop | Monitor Source | Cadence | Play Skill | LeadMagic Columns |
|---|---|---|---|---|
| Funding | Funding enrich / news | Daily | `funding-signal-play` | Find → Verify → Person |
| Job change | LeadMagic Job Change / LI | Daily | `job-change-play` | Job Change → Find → Verify |
| Hiring | Job postings enrich | Weekly | `hiring-signal-play` | Find → Verify (contacts) |
| Stale opp | CRM last_activity | Weekly | `pipeline-management` | Re-verify email only |
| Champion move | Job change + open opp | Daily | `job-change-play` | Job Change → Verify |
| ICP net-new | Firmographic filter | Weekly | `lead-finding` | Full waterfall |
| Post-meeting | CRM meeting, no task | Daily | `meeting-prep` | Verify only |

Full specs: `references/loop-catalog.md`.

**Rule:** One signal per loop.

### Phase 2 — 4-Table Architecture

```
[1. SOURCE]     CRM export, watchlist, or Clay source — raw accounts/contacts
[2. MONITOR]    Cheap columns only — signal_detected boolean + signal_date
[3. ENRICH]     LeadMagic waterfall ONLY IF signal_detected = true
[4. ACTION]     Score → route → CRM / sequencer / Slack / stop
```

**Credit rule:** Monitor first. Enrich conditionally. Cap 5 credits/row on
signal=true rows. See `references/leadmagic-waterfall.md`.

### Phase 3 — LeadMagic Enrich Table (Standard)

Run only when `signal_detected = true`:

```
Column A: LeadMagic Find Email (first + last + domain)     — 1 credit
Column B: LeadMagic Verify Email (email from A)            — 1 credit
  → IF invalid: stop row, flag email_invalid, no sequencer
Column C: LeadMagic Enrich Person (verified email)         — 2 credits
Column D: Formula — email_valid = (verify status = valid)
```

Job change loops add **before** Find Email:
```
Column 0: LeadMagic Job Change (linkedin_url or email)     — see leadmagic-job-change
  → Sets previous_company, new_company, title_changed
```

### Phase 4 — Signal Score

| Score | Meaning | Action |
|---|---|---|
| 80–100 | Tier-1 ICP + strong signal + LeadMagic valid | Sequencer or AE queue |
| 50–79 | Good signal, partial data | Human review queue |
| 20–49 | Weak signal / poor ICP | Log only |
| 0–19 | Suppressed, customer, invalid email | Stop |

Inputs: `icp_tier`, `signal_strength`, `email_valid`, `suppression_flag`.
Template: `templates/routing-matrix.md`.

### Phase 5 — Action Routing

| Destination | When | Required Fields |
|---|---|---|
| HubSpot/SF task | Score 50+ | `why_now`, `source_url`, SPICED-lite |
| Sequencer | Score 80+, `email_valid`, approved | Email, play ID, personalization |
| Slack | Tier-1 any signal | Account, signal, owner |
| CRM properties | All processed | `last_signal`, `signal_type`, `signal_date` |
| n8n webhook | Complex branch | `clay-loops-toolkit` → `n8n-toolkit` OUT-02 |

**Gates before sequencer:** LeadMagic verify = valid, suppression check,
`source_url` on every personalization claim, `human_approved` if auto-enroll.

### Phase 6 — Cadence & Maintenance

| Loop | Cadence | Signal stale after |
|---|---|---|
| Funding / job change | Daily | 14 days |
| Hiring | Weekly | 30 days |
| Stale CRM | Weekly | by activity date |
| Account refresh | Monthly | 90 days enrichment TTL |

Weekly review: credit burn, signal→meeting %, false positives.

## Output Format

Clay Loop blueprint using `templates/loop-blueprint.md`:
- Loop type + GTM play skill
- 4-table column map with LeadMagic waterfall
- Monitor formula + signal age filter
- Score bands + routing matrix
- Credit budget (per row + monthly cap)
- Integration endpoints (CRM, sequencer, n8n)

Run `scripts/check-output.py` before delivery.

## Quality Check

- [ ] One signal type per loop
- [ ] Monitor columns are cheap; enrich only on `signal_detected = true`
- [ ] LeadMagic Verify gate before sequencer or CRM outbound
- [ ] `why_now`, `source_url`, `signal_date` on every routed row
- [ ] Suppression check before any send action
- [ ] Signal age filter (14d funding/job change)
- [ ] Matching play skill referenced for message template
- [ ] Credit cap documented per row and monthly

## Common Pitfalls

1. **Enrich all rows.** Burns credits. Fix: conditional enrich on monitor.
2. **Skip LeadMagic verify.** Bounces destroy domain rep. Fix: verify gate.
3. **Mixed signals.** One loop for funding + hiring. Fix: separate loops.
4. **Stale triggers.** 6-month-old funding. Fix: `signal_date` < 14 days.
5. **Claygent for email in loops.** Expensive + risky. Fix: LeadMagic waterfall;
   Claygent only for `why_now` copy via `ai-prompts-toolkit` P03/P04.
6. **No action routing.** Alerts pile up. Fix: score → CRM task → owner.

## Execution Artifacts

- `references/loop-catalog.md` — Loop types, cadences, LeadMagic columns
- `references/leadmagic-waterfall.md` — Find → verify → enrich for loops
- `references/framework-notes.md` — SPICED + signal-to-action mapping
- `templates/loop-blueprint.md` — Loop design doc
- `templates/routing-matrix.md` — Score → action table
- `scripts/check-output.py` — Blueprint validator

## Related Skills

- `clay-toolkit` — `tools/clay-toolkit` — table architecture, static waterfalls
- `leadmagic-toolkit` — LeadMagic API, credits, Clay column setup
- `leadmagic-job-change` — Job change column for SIG loops
- `ai-prompts-toolkit` — P03/P04 for `why_now` and email draft columns
- `clay-automation` — Rollout process, data quality (not tool config)
- `sequencing-toolkit` — Enroll from action table
- `n8n-toolkit` — When loop output needs complex routing

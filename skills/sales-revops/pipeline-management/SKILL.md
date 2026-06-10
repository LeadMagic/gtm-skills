---
name: pipeline-management
description: >-
  Design and manage B2B sales processes using Winning by Design's GTM Playbook Kit
  — stage goals, in-stage actions, exit criteria, SPICED qualification fields,
  conversion metrics, Bowtie handoffs, forecasting, and deal inspection cadences.
  Use when designing sales process stages, building a GTM playbook, improving
  forecast accuracy, or setting up pipeline reviews. Triggers on: "sales process
  design", "GTM playbook", "pipeline management", "deal stages", "Winning by Design
  process", "SPICED stages", "forecasting", "deal inspection", "CRM hygiene".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.2.0"
  author: LeadMagic
  category: sales-revops
  tags: [pipeline, sales-process, spiced, forecasting, crm, deal-management, wbd]
  related_skills: [gtm-system-architecture, sales-enablement, sales-coaching, buyer-indecision, founder-sales, sales-team-building, meeting-prep, gtm-metrics, crm-integration]
  frameworks:
    - "Winning by Design — GTM Playbook Development Kit"
    - "Winning by Design — SPICED Qualification"
    - "Keenan — Gap Selling"
    - "Winning by Design — Bowtie Handoff Design"
    - "Mark Roberge — The Sales Acceleration Formula"
    - "Miller Heiman — Strategic Selling (buying influence)"
    - "Andy Whyte — MEDDICC Qualification & Scorecard"
    - "Force Management — MEDDICC Methodology"
    - "Joey Gilkey — Disposition Science (top-of-funnel diagnostics)"
    - "Ryan Reisert — CRM Activity Buckets (contact prioritization)"
    - "John McMahon — MEDDICC inspection cadence, three-view forecast, anti–happy ears"
---

# Pipeline Management

## Overview

Most sales teams have CRM stages that describe rep activity, not buyer progress.
Winning by Design's GTM Playbook Kit fixes this: every stage needs a **Goal**
(what success looks like), **In-Stage Actions** (what the rep does), and **Exit
Criteria** (evidence required to advance). Without all three, pipeline reviews
degenerate into confidence theater.

This skill designs the full sales process — stages, SPICED fields per stage,
conversion metrics, Bowtie handoffs to CS, forecast categories, and inspection
cadences. Load `gtm-system-architecture` first if you have not scored the six
WbD models. Load `sales-enablement` after this to build the playbook assets
reps use at each stage.

## When to Use

- "Design our sales process" or "build a GTM playbook"
- "Winning by Design sales process"
- "Define deal stages with exit criteria"
- "Set up SPICED in our CRM"
- "Improve forecast accuracy"
- "Build a pipeline review cadence"
- "Design SDR-to-AE handoffs"
- "Our pipeline is unpredictable — fix it"

Do not use for org design or compensation — use `sales-team-building`. Do not
use for collateral creation — use `sales-enablement` after the process is defined.

## Authoritative Foundations

- **Winning by Design — GTM Playbook Development Kit.** The core structure: Goal
  + In-Stage Actions + Exit Criteria per stage. A stage is not "Demo scheduled" —
  it is "buyer confirms solution maps to quantified pain" with evidence fields.
- **Winning by Design — SPICED.** Situation, Pain, Impact, Critical Event,
  Decision — required qualification dimensions captured progressively through
  Discovery and Solution stages, not dumped in one call.
- **Keenan — Gap Selling.** At Discovery/Solution stages, exit criteria should
  evidence Current State + Future State + quantified Gap (not rep confidence).
  Problem Identification Chart aligns product problems to discovery questions.
  Discovery stage gate: no advance on happy ears — buyer-stated impact required.
  Playbook → `meeting-prep/references/keenan-gap-selling.md`.
- **Winning by Design — Bowtie.** Revenue continues after Closed Won. Define
  handoff criteria from Sales → Onboarding (CS) with context package: SPICED
  summary, stakeholders, success criteria, and expansion signals.
- **Mark Roberge — The Sales Acceleration Formula.** Measure conversion rate
  between every stage. Inspect deals against exit criteria, not rep confidence.
- **Miller Heiman — Strategic Selling.** For enterprise deals, map buying
  influences (Economic Buyer, User Buyer, Technical Buyer, Coach) alongside
  stage progression.
- **Andy Whyte — MEDDICC (MEDDICC.com).** Seven qualification dimensions scored
  continuously on every deal: Metrics, Economic Buyer, Decision Criteria, Decision
  Process, Identify Pain, Champion, Competition. The MEDDICC scorecard drives
  go/no-go at stage gates — not rep confidence. "Always Be Qualifying" means
  re-scoring after every customer interaction.
- **Force Management — MEDDICC Methodology.** Original enterprise qualification
  framework (PTC/Force Management). Andy Whyte's scorecard operationalizes it for
  deal inspection and CRM fields.
- **John McMahon — Inspection cadence.** MEDDICC is the CRO's **forecast language**:
  weekly 1:1s inspect 2–3 deals with evidence per letter; slipping commits get
  role-play coaching (Stage 2 Capital demos). Board forecast uses **commit / likely /
  upside** tranches — each backed by MEDDICC proof and named mitigations. Pair Gap
  Selling at Discovery to block happy ears. Canonical → `gtm-leadership/references/cro-enterprise-strategy.md`.
- **Joey Gilkey — Disposition Science.** Six **outcome** buckets per completed
  conversation diagnose top-of-funnel list/message/rep problems before opportunities
  enter pipeline stages. Map Meeting Scheduled + Activated → qualified handoff;
  Not Now → nurture tier; Not Me/Referred → list rebuild signal. Requires 50+
  completions. → `references/joey-gilkey-bucketing.md`
- **Ryan Reisert — CRM Activity Buckets.** Four **contact-level** stages
  (Uncontacted, In Cadence, Priority, Scheduled) for SDR daily workflow — distinct
  from Gilkey dispositions. Design CRM contact stages and SDR→AE handoff tiers at
  top of funnel. → `references/ryan-reisert-cold-calling.md`

**SPICED + MEDDICC — complementary, not competing:**

| Layer | Framework | When | Purpose |
|---|---|---|---|
| Discovery conversation | SPICED (WbD) | Connect → Discovery | Uncover Situation, Pain, Impact, Critical Event |
| Deal qualification | MEDDICC (Whyte) | Solution → Negotiation | Score EB, Champion, Metrics, Competition with evidence |
| Both map to CRM | Shared fields | All stages | Impact → Metrics; Critical Event → Pain urgency; Decision → EB + Process |

Use SPICED in early calls. Use MEDDICC scorecard from Solution stage onward
and for any deal ≥$50K ACV. Never advance to Proposal without Champion named
and Economic Buyer engaged (Whyte's rule).

## Prerequisites

- CRM configured (HubSpot, Salesforce, or Attio)
- Average ACV and sales cycle length known
- ICP defined (`icp-scoring` or `gtm-context`)
- Motion selected: transactional, consultative, or strategic (`icp-targeting-tiers`)

## Step-by-Step Process

### Phase 1: Motion Selection (WbD by ACV)

| ACV Range | Motion | Typical Stages | Cycle |
|---|---|---|---|
| <$5K | Transactional | 4–5 stages, self-serve assist | Days–2 weeks |
| $5K–$50K | Consultative | 5–7 stages, SDR optional | 2–8 weeks |
| $50K+ | Strategic | 7–9 stages, multi-thread required | 2–6 months |

Pick one motion per segment. Do not run enterprise stages on SMB deals.

### Phase 2: Stage Design (GTM Playbook Kit)

For each stage, document all three components:

| Component | Definition | Bad Example | Good Example |
|---|---|---|---|
| **Goal** | What buyer + seller achieve at this stage | "Have a call" | "Pain quantified with business impact" |
| **In-Stage Actions** | Rep activities that advance the buyer | "Send follow-up" | "Run SPICED discovery, document Impact $" |
| **Exit Criteria** | Evidence required to advance (CRM fields) | "Rep feels good" | "Impact field populated, EB identified" |

**Consultative motion — reference stage map:**

| Stage | Goal | Key Exit Criteria (Evidence) |
|---|---|---|
| 1. Target | Account fits ICP | ICP score ≥ threshold, verified contacts |
| 2. Connect | Interest established | Reply received, Situation documented |
| 3. Discovery | Pain + Impact quantified | SPICED: Pain, Impact, Critical Event captured |
| 4. Solution | Solution validated | Demo complete, requirements confirmed, Champion named |
| 5. Proposal | Commercial terms presented | Proposal sent, Decision Process mapped |
| 6. Negotiation | Terms + procurement engaged | Redlines resolved, EB engaged, MEDDICC complete |
| 7. Closed Won | Contract executed | Signed agreement, handoff package to CS |
| 8. Closed Lost | Learning captured | Loss reason, competitor, stage-of-death |

**Strategic/enterprise additions:** add Technical Validation and Security Review
stages between Solution and Proposal. Require multi-thread map (`multi-thread-orchestration`).

### Phase 3: SPICED Field Mapping

Map SPICED dimensions to stages — capture progressively, not all at once:

| SPICED | Captured By Stage | CRM Field Examples |
|---|---|---|
| **S**ituation | Connect → Discovery | `current_tools`, `team_size`, `process_today` |
| **P**ain | Discovery | `primary_pain`, `pain_owner` |
| **I**mpact | Discovery | `impact_annual_cost`, `impact_metric` |
| **C**ritical Event | Discovery → Solution | `why_now`, `deadline_date` |
| **D**ecision | Solution → Proposal | `economic_buyer`, `decision_process`, `criteria` |

**Disqualification rule:** No Critical Event by end of Discovery → downgrade to
nurture or Closed Lost. No deal urgency = no deal timeline.

### Phase 4: MEDDICC Scorecard (Andy Whyte)

Score each dimension 0 (unknown), 1 (suspected), or 2 (confirmed with evidence).
Re-score after every meeting. Load `meeting-prep` for discovery questions and
`sales-coaching` for manager-led deal reviews.

| Letter | Dimension | Confirmed (Score 2) Requires | CRM Field |
|---|---|---|---|
| **M** | Metrics | Buyer-defined KPIs with baseline and target | `success_metrics`, `metric_baseline` |
| **E** | Economic Buyer | Named person with budget authority; met directly | `economic_buyer_name`, `eb_engaged_date` |
| **D** | Decision Criteria | Documented evaluation criteria (incl. yours) | `decision_criteria` |
| **D** | Decision Process | Mapped steps, dates, approvers | `decision_process_steps` |
| **I** | Identify Pain | Quantified pain + cost of inaction | `identified_pain`, `cost_of_inaction` |
| **C** | Champion | Power + influence + personal win + sells internally | `champion_name`, `champion_test_passed` |
| **C** | Competition | Named competitors, status quo, build-vs-buy assessed | `competition_landscape` |

**Andy Whyte — Champion test (all four required):**
1. Has power to influence the decision (not just enthusiasm)
2. Has a personal win if the deal closes
3. Can articulate the problem without your help
4. Has committed to sell internally when you are not in the room

**Stage gate minimums (consultative $5K–$50K):**

| Advance To | Minimum MEDDICC Score | Hard Requirements |
|---|---|---|
| Solution (from Discovery) | 6/14 | Pain=2, Metrics≥1 |
| Proposal | 10/14 | Champion=2, EB≥1, Decision Process≥1 |
| Negotiation | 12/14 | EB=2, Decision Criteria=2 |
| Commit forecast | 13/14 | All dimensions ≥1, no zeros on E/I/C |

**Enterprise ($50K+):** add Paper Process (`legal_review_steps`, `procurement_contact`)
and require multi-thread map before Proposal (`multi-thread-orchestration`).

**Go/No-Go:** Score <6 at Solution stage → nurture. Score <10 at Proposal → do not
send proposal. Score drops week-over-week → manager deal review within 48 hours.

### Phase 5: Conversion Metrics (Roberge + WbD)

Define target conversion rates between stages. Measure monthly:

| Conversion | Formula | Healthy Range (Consultative) |
|---|---|---|
| Target → Connect | Connects / Targets worked | 15–25% |
| Connect → Discovery | Meetings held / Connects | 40–60% |
| Discovery → Solution | Demos / Discoveries | 50–70% |
| Solution → Proposal | Proposals / Demos | 40–60% |
| Proposal → Closed Won | Wins / Proposals | 25–40% |

When a conversion drops >10 points below baseline, inspect exit criteria —
reps are advancing deals without evidence, or the stage Goal is wrong.

**Time-in-stage limits:** Discovery >21 days without Critical Event = stalled.
Alert + manager review. Proposal >30 days without EB engagement = at risk.

### Phase 6: Bowtie Handoffs

Sales process does not end at Closed Won. Define handoff packages:

| Handoff | From → To | Package Contents | SLA |
|---|---|---|---|
| MQL → SDR/AE | Marketing → Sales | Source, campaign, SPICED Situation | 24 hours |
| SDR → AE | SDR → AE | SPICED summary, meeting notes, next steps | Same day |
| AE → CS | Sales → Onboarding | Full SPICED, stakeholders, success criteria, contract scope | Before kickoff |
| CS → AE (expansion) | CS → Sales | Usage signals, expansion trigger, champion status | On signal |

Load `gtm-system-architecture` for the full Bowtie (Onboarding → Adoption →
Expansion → Renewal) and CS stage design.

### Phase 7: Forecast Categories

| Stage Group | Forecast Category | Confidence |
|---|---|---|
| Target, Connect | Pipeline | 10–20% |
| Discovery, Solution | Upside | 30–50% |
| Proposal, Negotiation | Commit | 70–85% |
| Closed Won | Won | 100% |

Commit deals require all Exit Criteria for Proposal stage met — not rep optimism.

### Phase 8: Deal Inspection Cadence

**Weekly pipeline review (60 min):**
1. New deals entered — exit criteria met for current stage?
2. Stalled >14 days — which SPICED/MEDDICC dimension is missing?
3. Commit at risk — what changed since last week?
4. Missing next steps — action assigned with date
5. Close date pushed — pattern or one-off?

**Deal review questions (never "how do you feel?"):**
- "Walk me through each SPICED field — what's the evidence?"
- "Who is the Economic Buyer and when did you last speak to them?"
- "What is the Critical Event date and what happens if they miss it?"
- "What would cause this deal to die?"

Load `sales-coaching` for REKS-based manager coaching on process adherence.

## Output Format

GTM sales process document containing: motion selection rationale, full stage
table (Goal + Actions + Exit Criteria), SPICED/MEDDICC CRM field map, conversion
metric targets, time-in-stage rules, Bowtie handoff specs, forecast categories,
and weekly inspection agenda.

Use `templates/output-template.md` for the deliverable structure. Run
`scripts/check-output.py` on the finished document before delivery.

## Quality Check

Before delivering, verify:
- [ ] Every stage has Goal, In-Stage Actions, AND Exit Criteria — not just a label
- [ ] Exit criteria are evidence fields in CRM, not subjective judgments
- [ ] SPICED dimensions mapped to specific stages with disqualification rules
- [ ] MEDDICC scorecard defined with 0/1/2 scoring and stage gate minimums
- [ ] Champion test (Whyte) documented with four criteria
- [ ] SPICED + MEDDICC field mapping shows no duplicate/conflicting CRM fields
- [ ] Conversion rate targets defined between each stage pair
- [ ] Time-in-stage limits set with alert thresholds
- [ ] AE → CS handoff package defined (Bowtie continuity)
- [ ] Forecast categories tied to exit criteria, not rep confidence
- [ ] Weekly inspection agenda uses SPICED/MEDDICC questions

## Common Pitfalls

1. **Stages named after rep activity.** "Demo scheduled" is an action, not a
   stage goal. Fix: name stages after buyer outcomes; actions live inside the stage.

2. **SPICED collected once, never updated.** SPICED fields go stale. Fix:
   require re-validation at Proposal stage; Critical Event dates must be current.

3. **No conversion metrics.** You cannot diagnose a broken process without
   stage-to-stage rates. Fix: baseline conversions, review monthly.

4. **Handoff to CS is an email.** CS starts blind, churn risk spikes. Fix:
   structured handoff package with SPICED summary and success criteria.

5. **Too many stages.** More than 9 stages creates CRM friction without accuracy
   gains. Fix: consolidate admin-heavy stages; keep 5–7 for consultative.

6. **Process without enablement.** Reps know the stages but lack talk tracks.
   Fix: load `sales-enablement` to build playbook assets per stage.

## Execution Artifacts

- `references/framework-notes.md` — WbD Playbook Kit, SPICED, Bowtie, MEDDICC, Gap Selling anchors
- `templates/output-template.md` — copy-paste sales process deliverable
- `scripts/check-output.py` — validates required sections in finished output
- `../../management-leadership/gtm-leadership/references/cro-enterprise-strategy.md` — McMahon QBR inspection checklist, three-view forecast (Pattern 31)
- `references/cold-calling-experts-index.md` — Phone bucketing router (Gilkey vs Reisert)
- `references/joey-gilkey-bucketing.md` — Disposition Science → pipeline tiers (repo root)
- `references/ryan-reisert-cold-calling.md` — CRM Activity Buckets (repo root)

## Related Skills

- `gtm-system-architecture` — Six-model audit and Bowtie architecture
- `sales-enablement` — Playbook, battlecards, talk tracks per stage
- `sales-coaching` — REKS (Jacco van der Kooij), MEDDICC deal reviews, JOLT coaching, 1:1/call rubrics
- `meeting-prep` — SPICED/MEDDIC discovery question banks
- `multi-thread-orchestration` — Enterprise buying committee mapping
- `crm-integration` — CRM field and stage configuration
- `gtm-metrics` — Pipeline dashboards and conversion reporting
- `buyer-indecision` — JOLT for Proposal+ stalls ("think about it", FOMU)

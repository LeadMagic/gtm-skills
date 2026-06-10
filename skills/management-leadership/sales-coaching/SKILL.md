---
name: sales-coaching
description: >-
  Sales coaching system — REKS diagnosis (Jacco van der Kooij / Winning by Design),
  MEDDICC deal reviews (Andy Whyte), JOLT for indecision, call coaching (Jon Barrows,
  Jason Bay), manager cadence (Kevin Dorsey), and founder-as-coach. Use when building
  coaching programs, 1:1s, deal reviews, call feedback, or improving rep performance.
  Triggers on: "sales coaching", "coach reps", "REKS", "deal review", "call coaching",
  "manager 1:1 sales", "coach discovery", "coach SDR", "founder coach sales team".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "2.0.0"
  author: LeadMagic
  category: management-leadership
  tags: [coaching, sales-management, reks, meddicc, jolt, 1-1, deal-review]
  related_skills:
    - pipeline-management
    - meeting-prep
    - buyer-indecision
    - sales-enablement
    - gtm-leadership
    - team-management
    - revenue-team-onboarding
    - objection-handling
    - demo-scripts
    - transparency-selling
  frameworks:
    - "Jacco van der Kooij (Winning by Design) — REKS, SPICED coaching"
    - "Andy Whyte — MEDDICC scorecard and deal review"
    - "Matthew Dixon & Ted McKenna — JOLT Effect (late-stage coaching)"
    - "Kevin Dorsey — Sales leadership coaching cadence"
    - "Jon Barrows (Sell Better) — Discovery and demo skill coaching"
    - "Jason Bay (Outbound Squad) — SDR messaging coaching (PVP)"
    - "Keith Rosen — Sales coaching accountability"
    - "Kim Scott — Radical Candor (performance conversations)"
    - "Randy Seidl (Sales Community) — Relationship selling, Three Plays, behavior coaching"
    - "Tom Slocum (The SD Lab) — SDR cold call coaching, 3×3, sell-the-meeting"
    - "Ryan Reisert (CallBlitz) — Live call coaching, CRM Activity Buckets ramp"
---

# Sales Coaching

## Overview

Coaching is the highest-leverage activity in a revenue org — and the most
often skipped. Managers who "coach" by asking "how's the pipeline?" get
fiction. Managers who inspect **evidence** (MEDDICC scores, call recordings,
SPICED fields) change behavior.

**Jacco van der Kooij** (Winning by Design) built **REKS** so managers diagnose
before prescribing: a rep missing quota might need effort discipline, product
knowledge, or conversation skill — three different interventions. Late-stage
stalls need **JOLT** (Dixon/McKenna), not more ROI slides.

This skill is the **coaching operating system**: cadence, diagnostics, deal
reviews, call rubrics, 1:1 agendas, founder-as-coach, and manager calibration.

Process design → `pipeline-management`. Hard conversations / PIP → `gtm-leadership`.
Onboarding ramp → `revenue-team-onboarding`.

## When to Use

- "Build sales coaching program"
- "How do I coach my AEs / SDRs?"
- "Deal review format for managers"
- "1:1 template for sales manager"
- "Coach discovery calls"
- "Rep stuck — REKS diagnosis"
- "Coach late-stage indecision"
- "Founder coaching first sales hire"
- "Call coaching rubric"

## Authoritative Foundations

- **Jacco van der Kooij / Winning by Design — REKS.** Results → Efforts →
  Knowledge → Skills. Coach the layer, not the number. SPICED for discovery
  coaching; Bowtie for handoff quality.
- **Andy Whyte — MEDDICC.** 0/1/2 scorecard (max 14). Managers inspect
  evidence per dimension — same gates as `pipeline-management`.
- **Matthew Dixon & Ted McKenna — JOLT.** Judge indecision → Offer recommendation
  → Limit exploration → Take risk off table. Coach when fit exists but buyer stalls.
- **Kevin Dorsey.** Daily manager rhythm during ramp; pipeline accountability
  without micromanagement; coaching as leadership core competency.
- **Jon Barrows (Sell Better).** Short-cycle skill reps for discovery, demo
  structure, objection handling — coach behaviors in 15-min drills.
- **Jason Bay — PVP.** Coach outbound relevance (Permissionless Value Proposition),
  not volume — for SDR/BDR coaching.
- **Keith Rosen.** Accountability coaching: commitments, timelines, ownership.
- **Kim Scott.** Radical Candor for performance — separate coaching from status.
- **Randy Seidl** (Sales Community). **Three Plays** — sell yourself, company/product,
  customer outcome. **Relationship map** + decision map for enterprise deals.
  Coach **behaviors** (trust-building touches, extended team usage) over pipeline
  fiction. Load `references/randy-seidl-relationship-selling.md`.
- **Tom Slocum (The SD Lab).** **Sell the Meeting** (nurse, not doctor);
  **3×3 research** before call blocks; dial discipline and SDR intensives.
  Coach prep quality and conversation structure — not dial volume. Phone SDRs only
  (not email PVP). → `references/tom-slocum-cold-calling.md`
- **Ryan Reisert (CallBlitz, Outbound Operators).** **CRM Activity Buckets** for
  daily rep prioritization; **CallBlitz** live floor for peer/manager call coaching;
  completions-over-dials accountability. Pair with Slocum for skill; with Gilkey
  dispositions for list diagnosis. → `references/ryan-reisert-cold-calling.md`

## Step-by-Step Process

### Phase 1 — Coaching Stack (Load Order)

```
1. pipeline-management     → stages, MEDDICC gates, SPICED fields
2. sales-enablement        → playbook reps should execute
3. sales-coaching (this)   → diagnose + inspect + practice
4. buyer-indecision          → JOLT when late-stage stall
5. gtm-leadership          → if coaching fails → PIP / exit
```

### Phase 2 — REKS Diagnosis (Before Any Coaching)

Load `references/reks-diagnostic.md` + `templates/reks-diagnostic.md`.

| Layer | Signals | Coach toward |
|---|---|---|
| **Results** | Quota miss, win rate drop | Diagnose E/K/S — don't yell at results |
| **Efforts** | Low activity, empty calendar | Prioritization, time blocks, accountability |
| **Knowledge** | Wrong ICP, bad product answers | Enablement, shadowing, certification |
| **Skills** | Bad discovery, weak demo | Role-play, call review, Barrows drills |

**Rule:** If E+K+S are adequate and Results still fail → territory, quota, or fit (`gtm-leadership`).

### Phase 3 — Manager Cadence (Kevin Dorsey + WbD)

| Cadence | Duration | Focus | Artifact |
|---|---|---|---|
| Daily huddle | 5–10 min | Deals at risk, one win | Slack `#sales-team` |
| Weekly 1:1 | 30–45 min | One skill + one deal deep-dive | `templates/1-1-agenda.md` |
| Weekly pipeline | 60 min | Commit deals MEDDICC ≥ gate | `templates/deal-review-scorecard.md` |
| Call coaching | 2–3 calls/rep/week | One keep, one fix | `templates/call-coaching-form.md` |
| Monthly | 60 min | Career, skill plan | `templates/coaching-plan-30-day.md` |
| Quarterly | Review | Goals, territory, comp reality | `team-management` |

**1:1 rule:** No status updates — CRM holds status. 1:1 = development.

### Phase 4 — Deal Review (MEDDICC)

Load `references/deal-review-guide.md`.

1. Rep presents scorecard (0/1/2 per dimension) — not narrative
2. Manager asks for **evidence** per score of 2
3. Identify gaps blocking next stage gate
4. One action per gap: owner, date, next step
5. Forecast category only if score ≥ gate (`pipeline-management`)

**Coaching questions (Whyte):**
- "Whose numbers are in Metrics — buyer's or ours?"
- "When did you last speak to the Economic Buyer directly?"
- "Does Champion pass all four tests — show me proof."
- "What's the Decision Process step and date?"

### Phase 5 — SPICED Coaching (Discovery)

When rep struggles **before** MEDDICC is populated:

| SPICED gap | Coach |
|---|---|
| Situation | Research depth, pre-call prep (`meeting-prep`) |
| Pain | Question quality — Barrows discovery drills |
| Impact | Quantification — tie to Metrics field |
| Critical Event | Timeline urgency — why now? |
| Decision | Stakeholder map — multi-thread |

### Phase 6 — JOLT Coaching (Late Stage)

When MEDDICC ≥ gate but deal stalls — load `references/jolt-coaching.md` + `buyer-indecision`.

| JOLT step | Manager coaches rep to |
|---|---|
| **Judge** | Score indecision 1–10; identify FOMU vs objection |
| **Offer** | Make explicit recommendation — "Here's what I'd do" |
| **Limit** | Stop sending more options — collapse choice |
| **Take risk** | Pilot, SLA, opt-out, executive sponsor |

Do not coach "send another ROI deck" for indecision — it increases FOMU.

### Phase 7 — Call Coaching

Load `references/call-coaching-rubric.md`.

**Per call (15-min manager review):**
1. Listen at 1.25× — note timestamps
2. Score: discovery, value, objection, next step (1–5)
3. **One keep** — reinforce
4. **One fix** — specific behavior next call
5. Rep re-records 2-min role-play before next live call

**SDR calls (phone):** Coach 3×3 prep + sell-the-meeting (Slocum), pattern-interrupt
opener + tonality (Pessar), CRM bucket discipline (Reisert). Live review via
CallBlitz when available. Disposition distribution after 50 completions (Gilkey).

**SDR outreach (email/LinkedIn):** Coach PVP and relevance (Jason Bay), not dial count.

### Phase 8 — Founder-as-Coach

Before first manager hire, founder coaches directly (`references/founder-coaching.md`):

| Stage | Founder focus |
|---|---|
| First AE | Shadow 50% of calls; SPICED on every deal |
| 2–3 reps | Weekly deal review only; delegate call coaching to senior rep |
| Manager hired | Founder coaches manager on coaching (meta-coaching) |

Founder trap: doing deals instead of inspecting deals. Calendar-block coaching.

### Phase 9 — 30-Day Coaching Plan (Underperformer)

Template: `templates/coaching-plan-30-day.md`

Week 1: REKS diagnose + enablement gap analysis  
Week 2: Daily call review + skill drill  
Week 3: Deal inspection cadence + accountability  
Week 4: Measure leading indicators — if flat, escalate `gtm-leadership`

## Output Format

| Request | Deliverable |
|---|---|
| Coaching system | Cadence calendar + artifact index |
| 1:1 program | `templates/1-1-agenda.md` per role |
| Deal reviews | Scorecard + question bank |
| Call coaching | Rubric + feedback form |
| Underperformer | REKS diagnostic + 30-day plan |
| Late-stage stall | JOLT coaching brief |

Run `scripts/check-output.py` before delivery.

## Quality Check

- [ ] REKS layer identified before coaching action
- [ ] Deal reviews use MEDDICC evidence — not rep confidence
- [ ] 1:1 agenda excludes status updates
- [ ] Call coaching: one keep + one fix per session
- [ ] JOLT used for indecision — not more collateral
- [ ] SPICED coached for discovery gaps
- [ ] Founder/manager cadence appropriate to team size
- [ ] Phone SDR coaching uses Slocum/Reisert — email SDR coaching uses Bay PVP
- [ ] Cross-ref `pipeline-management` stage gates

## Common Pitfalls

1. **Coaching results, not behaviors.** "Hit quota" isn't coaching. Fix: REKS layer + one skill.
2. **Skipping diagnosis.** More dials for a knowledge gap. Fix: REKS first.
3. **Deal review as storytelling.** Fix: scorecard + evidence.
4. **1:1 as pipeline readout.** Fix: CRM for status; 1:1 for development.
5. **ROI pile-on for indecision.** Fix: JOLT — recommendation + risk removal.
6. **Founder stops coaching after hire #1.** Fix: meta-coach the manager.

## Execution Artifacts

| `../../outbound/cold-calling/references/framework-notes.md` | Phone coaching framework anchors |
| `templates/output-template.md` | Deliverable structure |
| `scripts/check-output.py` | Validator |
| File | Use |
|---|---|
| `references/reks-diagnostic.md` | REKS layer signals and fixes |
| `references/deal-review-guide.md` | MEDDICC inspection flow |
| `references/call-coaching-rubric.md` | Call scoring dimensions |
| `references/jolt-coaching.md` | Late-stage manager prompts |
| `references/founder-coaching.md` | Founder-as-coach by ARR stage |
| `references/coaching-experts.md` | Expert map (Jacco, Dorsey, Barrows, Bay, Seidl, Slocum, Reisert) |
| `references/randy-seidl-relationship-selling.md` | Relationship map, Three Plays, trust scorecard |
| `references/tom-slocum-cold-calling.md` | 3×3, sell-the-meeting, call blocks (repo root) |
| `references/ryan-reisert-cold-calling.md` | CRM Buckets, CallBlitz live coaching (repo root) |
| `references/cold-calling-experts-index.md` | Phone expert router (repo root) |
| `templates/1-1-agenda.md` | Weekly 1:1 structure |
| `templates/reks-diagnostic.md` | Per-rep diagnostic form |
| `templates/deal-review-scorecard.md` | MEDDICC deal review |
| `templates/call-coaching-form.md` | Per-call feedback |
| `templates/coaching-plan-30-day.md` | Underperformer plan |

## Related Skills

- `pipeline-management` — MEDDICC gates, SPICED fields, stage design
- `meeting-prep` — SPICED questions reps should master
- `buyer-indecision` — JOLT playbook for reps
- `sales-enablement` — Collateral coaching references
- `gtm-leadership` — PIP, fire, Radical Candor
- `team-management` — OKRs, general 1:1s
- `cold-calling` — SDR phone motion, dispositions, call structure
- `revenue-team-onboarding` — Ramp coaching first 90 days
- `demo-scripts` — Demo coaching content
- `objection-handling` — Objection drills

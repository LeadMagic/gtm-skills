---
name: cold-calling
description: >-
  Build and execute B2B cold calling programs — phone intent scoring, disposition
  bucketing, CRM activity buckets, ColdCall-Market Fit, multi-touch cadences, and
  conversation-to-meeting conversion. Use when setting up cold calling, training
  SDRs, improving connect rates, or building a phone outreach motion. Triggers on:
  "cold calling", "cold call", "phone outreach", "SDR calling", "connect rate",
  "dialer", "phone prospecting", "calling strategy", "cold call script", "phone
  intent", "precision dialing", "bucketing", or any request about outbound phone
  prospecting.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: outbound
  tags: [cold-calling, phone, sdr, connect-rate, dialer, outreach, bucketing]
  related_skills: [multi-channel-outreach, cold-email-strategy, signal-scoring, sales-team-building, list-building, revenue-team-onboarding]
  frameworks:
    - "Joey Gilkey — Disposition Science & Phone Intent"
    - "Ryan Reisert — CRM Activity Buckets"
    - "Ronen Pessar — ColdCall-Market Fit"
    - "Tom Slocum — 3Rs / Sell the Meeting"
    - "Jeb Blount — Fanatical Prospecting / Golden Hours"
    - "Sandler Up-Front Contracts"
---

# Cold Calling

## Overview

Cold calling is not dead — blind cold calling is. The difference between a 3%
connect rate and a 25% connect rate is knowing who will answer before you dial.
When executed with precision, the phone remains the highest-converting outbound
channel because voice creates a real-time human connection that text cannot
replicate.

This skill covers the complete cold calling motion: **Phone Intent** scoring
(Joey Gilkey / TitanX), **Disposition Science** (outcome bucketing per
conversation), **CRM Activity Buckets** (Ryan Reisert daily workflow),
**ColdCall-Market Fit** (Ronen Pessar), SDR coaching patterns (Tom Slocum),
**Golden Hours** prospecting discipline (Jeb Blount), multi-touch cadence design, and the metrics that matter. The phone is one
instrument in a coordinated multi-channel sequence — not a standalone channel.

**Expert index:** `references/cold-calling-experts-index.md`

## When to Use

- "Build a cold calling program"
- "Improve our cold call connect rates"
- "Train SDRs on cold calling"
- "Set up a precision dialing workflow"
- "Write cold call scripts"
- "What's the best cold calling cadence?"
- "How do I get more conversations from cold calls?"
- "Our connect rates are under 5% — fix this"
- "Bucketing methodology for outbound"

## Authoritative Foundations

**Joey Gilkey (TitanX)** — **Disposition Science** + **Phone Intent Platform**.
Six disposition buckets categorize every completed conversation (Meeting
Scheduled, Activated, Not Now, Not Me, Referred, Not Interested). Distribution
diagnoses list, message, rep, or follow-up problems. The 20% Rule: only ~20%
of any B2B market will answer a cold call; Phone Intent™ scoring finds the
reachable segment before reps dial. Conversation-as-KPI over meetings-booked
activity. → `references/joey-gilkey-bucketing.md`

**Ryan Reisert (CallBlitz, Outbound Operators, *Outbound Sales, No Fluff*)** —
**CRM Activity Buckets**: 4-stage daily-priority system (Uncontacted → In Cadence
→ Priority → Scheduled). Work backwards from Bucket 4 to 1. Track completions,
not vanity dials. 100+ meaningful activities/day. Live call coaching via
CallBlitz. → `references/ryan-reisert-cold-calling.md`

**Ronen Pessar (Outbound Operators)** — **ColdCall-Market Fit**: prove phone
motion in a 3-hour Call Pilot before scaling SDR headcount. Tonality +
pattern-interrupt script framework; 50–100 conversation checkpoints.
→ `references/ronen-pessar-cold-calling.md`

**Tom Slocum (The SD Lab)** — **Sell the Meeting** (nurse, not doctor);
**3Rs / 3×3** research before every block; dial discipline and SDR coaching
intensives. → `references/tom-slocum-cold-calling.md`

**Jeb Blount (Sales Gravy, *Fanatical Prospecting*)** — **Law of Replacement**
and **Golden Hours**: block 2–3 hours daily for prospecting before reactive
work; omni-channel habit across phone, email, and social. Pairs with Gilkey
(list) and Reisert (buckets) — Blount enforces **discipline**, not call script.
→ `references/jeb-blount-prospecting.md`

**Sandler** — Up-Front Contracts. Apply to cold calls: earn permission, diagnose
pain, and mutually qualify — don't pitch.

**Distinction from email experts:** Jordan Crawford, Jason Bay, Guillaume, and
Justin Michael lead **written** outbound. This skill is **phone-first** — load
`cold-email-strategy` only for complementary cadence touches.

## Prerequisites

- Tight ICP definition (use icp-scoring skill)
- Verified direct-dial phone numbers (not switchboard numbers)
- CRM with contact-level activity tracking + disposition fields
- Optional: phone intent scoring (TitanX), precision dialer (FrontSpin)

## Step-by-Step Process

### Phase 1: Build the List (Gilkey List Lever)

Cold calling performance is determined upstream of the dial. Fix the list before
you fix the script.

1. Define a tight ICP (firmographics, technographics, trigger events)
2. Source verified direct-dial phone numbers — never switchboard numbers
3. Enrich with phone intent scores (TitanX): P1 (high-intent, will answer),
   P2 (moderate-intent, may answer), P3 (low-intent, rarely answers), bad data
4. Apply Tom Slocum **3×3** research: 3 insights in 3 minutes per contact
5. Target 500 perfectly-fit prospects over 5,000 marginal ones
6. Verify a 5% sample manually before dialing the full list
7. Cross-link list strategy: Jordan Crawford PQS (`cold-email-strategy`)

### Phase 2: Prove ColdCall-Market Fit (Pessar — Optional but Recommended)

Before hiring SDRs or scaling dials:

1. One ICP, 1–2 personas, one focused list
2. Run Call Pilot or internal blitz — 50–100 completions minimum
3. Iterate script/tonality: try → listen → learn → refine
4. Read Gilkey disposition distribution — diagnose list vs message
5. Decide: full-time SDR, agency install, or email-primary segment

### Phase 3: CRM Activity Buckets (Reisert)

Work backwards from highest to lowest priority daily:

**Bucket 4 — Scheduled:** Confirmed meetings. Confirm week-of, 24 hours before,
and 2–3 hours before. Low no-show rate is the metric.

**Bucket 3 — Priority (Working):** Contacts who have engaged — replied to email,
answered a call, referred to a colleague. Hot leads. Call 2–3× per day. Every
touch documented in CRM.

**Bucket 2 — In Cadence:** ICP contacts with documented attempts but no engagement
yet. 100 contacts in this bucket at all times. Research completed, notes in CRM.

**Bucket 1 — Uncontacted (Target):** New ICP contacts not yet reached. Research
and qualify before first dial. Only ICP-fit contacts enter this bucket.

### Phase 4: Disposition Science (Gilkey)

After each **completed conversation**, assign one disposition:

Meeting Scheduled · Activated · Not Now · Not Me · Referred · Not Interested

- High **Not Me / Referred** → list/title problem (build v2 list from referrals)
- High **Not Interested** → segment by rep before blaming message
- Need **50+ completions** before distribution is actionable
- Optimize with **King of the Hill**: change one lever (list OR message) per test

### Phase 5: Precision Dialing (Gilkey / TitanX)

- **Know who to call before you dial.** Phone Intent scores segment contacts by
  likelihood to answer. Call P1 contacts first.
- **Precision dialer over parallel dialer.** One contact at a time with full
  context. Parallel dialers create dead-air pauses that trigger spam flags.
- **Channel match to reachability.** High phone-intent → phone-heavy cadence.
  Low phone-intent → email and LinkedIn. Bad data → nurture, not rep time.
- **Protect caller reputation.** Rotate caller IDs, monitor spam labels, stay
  TCPA-compliant.

### Phase 6: The Call Structure (Reisert + Pessar + Slocum)

**Opener (Pessar — pattern interrupt + permission):**
"Hi [name], this is [name] from [company]. I know you weren't expecting my call
— can I have 30 seconds to tell you why I'm calling, and you tell me if it's
worth continuing?"

Never: "Did I catch you at a bad time?" or "How are you today?"

**The Reason (Slocum 3×3 — account-specific):**
Reference a trigger from prep — funding, hiring, tech change, content engagement.

**Discovery (Reisert — diagnose, don't pitch):**
11-14 questions per call. SPIN structure. Slocum: sell the **meeting**, not the
product — nurse, not doctor.

**Close to Next Step:**
"Based on what you've shared, I think a 20-minute call with [specific agenda]
would make sense. Does Thursday at 2pm work?"

### Phase 7: Cadence Design (Reisert)

3-5 call attempts, front-loaded across days. By the 3rd attempt, 93% of all
conversations have already happened. By the 5th attempt, 98%. Stop at 5; revisit
in 90 days.

Coordinate with email and LinkedIn (phone ≠ email-only motion):

- Day 1: LinkedIn view + connect request
- Day 2: Cold call (first attempt, Wednesday or late afternoon)
- Day 3: Follow-up email referencing the call
- Day 5: Cold call (second attempt, different time)
- Day 7: LinkedIn DM
- Day 9: Cold call (third attempt)
- Day 11: Value-add email (case study or insight)
- Day 14: Final call + breakup email

### Phase 8: Metrics That Matter

| Metric | Weak | Average | Strong |
|---|---|---|---|
| Dials per day per rep | <50 | 80-120 | 120+ |
| Connect rate | <3% | 5-10% | 20-30% (with phone intent) |
| Completions per 100 dials | <5 | 5-15 | 20-25+ (Reisert target) |
| Hold rate (stay on line) | <50% | 65% | 80%+ |
| Conversation-to-meeting | <10% | 20-40% | 40%+ |
| Dials per meeting | 250+ | 100-200 | <100 |
| Meeting show rate | <70% | 70-85% | 90%+ |

Track per rep, per list, per segment, per disposition. Blended numbers hide
the segment converting at 9% and the one at 1%.

## Output Format

Cold calling playbook with: ICP targeting criteria, phone intent workflow,
CRM Activity Buckets tracker, disposition fields, call script (opener +
discovery questions), 3×3 research template, cadence calendar, and rep
scorecard with per-metric targets.

## Quality Check

- [ ] ICP definition is tight — specific firmographics, technographics, triggers
- [ ] Phone numbers are verified direct dials, not switchboards
- [ ] Phone intent scoring applied (or manual prioritization by known signals)
- [ ] CRM Activity Buckets implemented with 4 contact stages (Reisert)
- [ ] Disposition Science fields on every completed conversation (Gilkey)
- [ ] 3×3 research completed before call blocks (Slocum)
- [ ] Call script includes pattern-interrupt opener + discovery questions
- [ ] Cadence coordinates calls with email and LinkedIn touches
- [ ] Metrics tracked per rep, per list, per segment (not blended)
- [ ] ColdCall-Market Fit validated before SDR headcount scale (Pessar)

## Common Pitfalls

1. **Conflating two bucketing systems.** Gilkey dispositions diagnose outcomes;
   Reisert buckets prioritize daily work — use both, not interchangeably.

2. **Calling a loose ICP.** A call to a marginal-fit prospect converts at 1/5
   to 1/10 the rate of a perfect-fit prospect. Narrow the target ruthlessly
   before the first dial.

3. **Dialing stale data.** Reps lose over 25% of their time to wrong numbers.
   B2B data decays ~2% per month. Refresh phone numbers quarterly.

4. **Pitching instead of diagnosing.** Reps who pitch on the first call talk past
   the prospect. Slocum: sell the meeting. Discovery: 11-14 questions.

5. **Parallel dialing without phone intent.** Creates awkward dead-air pauses
   and burns TAM — carriers flag you as spam.

6. **No coordination with email and LinkedIn.** The phone is one instrument.
   Each touch should reference the others.

7. **Using switchboard numbers.** 209+ dials per meeting with switchboard
   numbers vs 30-80 with verified direct dials and phone intent.

8. **Activity metrics over outcome metrics.** 200 dials with 1 conversation
   loses to 50 dials with 10 conversations. Measure completions and
   dispositions, not dials alone.

9. **Hiring SDRs before ColdCall-Market Fit.** 9–12 months of guessing vs
   50–100 conversation pilot (Pessar).

## Execution Artifacts

- `references/cold-calling-experts-index.md` — Phone expert router (repo root)
- `references/joey-gilkey-bucketing.md` — Disposition Science + Phone Intent
- `references/ryan-reisert-cold-calling.md` — CRM Activity Buckets + call structure
- `references/ronen-pessar-cold-calling.md` — ColdCall-Market Fit + tonality
- `references/tom-slocum-cold-calling.md` — 3Rs, sell-the-meeting, call blocks
- `references/jeb-blount-prospecting.md` — Golden Hours, Law of Replacement
- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **multi-channel-outreach**: Coordinate calls with email and LinkedIn
- **cold-email-strategy**: Complementary written outbound (not a substitute)
- **list-building**: Upstream list quality + Gilkey list lever
- **signal-scoring**: Signals that indicate phone-intent prospects
- **sales-team-building**: SDR hiring, POD structures, compensation
- **revenue-team-onboarding**: Cold call ramp and certification
- **meeting-prep**: Pre-call research and discovery questions

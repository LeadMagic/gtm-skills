---
name: cold-calling
description: >-
  Build and execute B2B cold calling programs — phone intent scoring, precision
  dialing, the Buckets methodology, multi-touch cadences, and conversation-to-meeting
  conversion. Use when setting up cold calling, training SDRs, improving connect
  rates, or building a phone outreach motion. Triggers on: "cold calling", "cold
  call", "phone outreach", "SDR calling", "connect rate", "dialer", "phone prospecting",
  "calling strategy", "cold call script", "phone intent", "precision dialing",
  or any request about outbound phone prospecting.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: outbound
  tags: [cold-calling, phone, sdr, connect-rate, dialer, outreach]
  related_skills: [multi-channel-outreach, cold-email-strategy, signal-scoring, sales-team-building]
  frameworks: [Ryan Reisert Buckets Methodology, TitanX Phone Intent, Sandler Up-Front Contracts]
---

# Cold Calling

## Overview

Cold calling is not dead — blind cold calling is. The difference between a 3%
connect rate and a 25% connect rate is knowing who will answer before you dial.
When executed with precision, the phone remains the highest-converting outbound
channel because voice creates a real-time human connection that text cannot
replicate.

This skill covers the complete cold calling motion: phone intent scoring
(TitanX), the Buckets prioritization system (Ryan Reisert), multi-touch cadence
design, and the metrics that matter. The phone is one instrument in a coordinated
multi-channel sequence — not a standalone channel.

## When to Use

- "Build a cold calling program"
- "Improve our cold call connect rates"
- "Train SDRs on cold calling"
- "Set up a precision dialing workflow"
- "Write cold call scripts"
- "What's the best cold calling cadence?"
- "How do I get more conversations from cold calls?"
- "Our connect rates are under 5% — fix this"

## Authoritative Foundations

**Ryan Reisert (Sales Bootcamp, Outbound Operators, CallBlitz)** — The Buckets
Methodology: 4-stage prioritization system that ensures SDRs always do the
highest-value activity. 100+ touchpoints per day per SDR. Process over volume.

**TitanX (Joey Gilkey)** — Phone Intent Platform. The 20% Rule: only ~20% of any
B2B market will ever answer a cold call. The other 80% will never pick up
regardless of timing, script, or rep skill. Phone Intent™ scoring identifies
the reachable 20% before reps dial. Precision dialing over parallel dialing.

**Sandler** — Up-Front Contracts. Apply to cold calls: earn permission, diagnose
pain, and mutually qualify — don't pitch.

## Prerequisites

- Tight ICP definition (use icp-scoring skill)
- Verified direct-dial phone numbers (not switchboard numbers)
- CRM with contact-level activity tracking
- Optional: phone intent scoring (TitanX), precision dialer (FrontSpin)

## Step-by-Step Process

### Phase 1: Build the List

Cold calling performance is determined upstream of the dial. Fix the list before
you fix the script.

1. Define a tight ICP (firmographics, technographics, trigger events)
2. Source verified direct-dial phone numbers — never switchboard numbers
3. Enrich with phone intent scores (TitanX): P1 (high-intent, will answer),
   P2 (moderate-intent, may answer), P3 (low-intent, rarely answers), bad data
4. Target 500 perfectly-fit prospects over 5,000 marginal ones
5. Verify a 5% sample manually before dialing the full list

### Phase 2: The Buckets Methodology (Ryan Reisert)

Work backwards from highest to lowest priority:

**Bucket 4 — Meetings Scheduled:** Confirmed meetings. Confirm week-of, 24 hours
before, and 2-3 hours before. Low no-show rate is the metric.

**Bucket 3 — Priority (Working):** Contacts who have engaged — replied to email,
answered a call, referred to a colleague. Hot leads. Call 2-3x per day. Every
touch documented in CRM.

**Bucket 2 — In Cadence:** ICP contacts with documented attempts but no engagement
yet. 100 contacts in this bucket at all times. Research completed, notes in CRM.

**Bucket 1 — Uncontacted (Target):** New ICP contacts not yet reached. Research
and qualify before first dial. Only ICP-fit contacts enter this bucket.

### Phase 3: Precision Dialing (TitanX)

- **Know who to call before you dial.** Phone Intent scores segment contacts by
  likelihood to answer. Call P1 contacts first — they are your highest-converting
  prospects.
- **Precision dialer over parallel dialer.** Call one contact at a time with full
  context. Parallel dialers create dead-air pauses that trigger spam flags.
- **Channel match to reachability.** High phone-intent contacts get phone-heavy
  outreach. Low phone-intent contacts get email and LinkedIn sequences. Bad data
  gets marketing nurture, not rep time.
- **Protect caller reputation.** Rotate caller IDs, monitor spam labels, stay
  TCPA-compliant. Carriers flag high-volume low-answer callers as spam.

### Phase 4: The Call Structure

**Opener (earn the next 30 seconds):**
Pattern-interrupt + permission. "Hi [name], this is [name] from [company]. I
know you weren't expecting my call — can I have 30 seconds to tell you why
I'm calling, and you tell me if it's worth continuing?"

Never: "Did I catch you at a bad time?" or "How are you today?"

**The Reason (specific, account-relevant):**
Reference a trigger signal — funding, hiring, tech change, content engagement.
"I'm calling because I saw [specific trigger] and in our experience, companies
at that stage usually [insight]."

**Discovery (diagnose, don't pitch):**
11-14 questions per call. Talk less than you listen. The goal is a qualified
next step, not a close. SPIN question structure: Situation → Problem →
Implication → Need-Payoff.

**Close to Next Step (crisp, specific):**
"Based on what you've shared, I think a 20-minute call with [specific agenda]
would make sense. Does Thursday at 2pm work?"

### Phase 5: Cadence Design

3-5 call attempts, front-loaded across days. By the 3rd attempt, 93% of all
conversations have already happened. By the 5th attempt, 98%. Calling a 6th or
7th time wastes effort — move on and revisit in 90 days.

Coordinate with email and LinkedIn:
- Day 1: LinkedIn view + connect request
- Day 2: Cold call (first attempt, Wednesday or late afternoon)
- Day 3: Follow-up email referencing the call
- Day 5: Cold call (second attempt, different time)
- Day 7: LinkedIn DM
- Day 9: Cold call (third attempt)
- Day 11: Value-add email (case study or insight)
- Day 14: Final call + breakup email

### Phase 6: Metrics That Matter

| Metric | Weak | Average | Strong |
|---|---|---|---|
| Dials per day per rep | <50 | 80-120 | 120+ |
| Connect rate | <3% | 5-10% | 20-30% (with phone intent) |
| Hold rate (stay on line) | <50% | 65% | 80%+ |
| Conversation-to-meeting | <10% | 20-40% | 40%+ |
| Dials per meeting | 250+ | 100-200 | <100 |
| Meeting show rate | <70% | 70-85% | 90%+ |

Track per rep, per list, per segment. A blended number hides the segment
converting at 9% and the one at 1%.

## Output Format

Cold calling playbook with: ICP targeting criteria, phone intent workflow,
Buckets tracker template, call script (opener + discovery questions), cadence
calendar, and rep scorecard with per-metric targets.

## Quality Check

- [ ] ICP definition is tight — specific firmographics, technographics, triggers
- [ ] Phone numbers are verified direct dials, not switchboards
- [ ] Phone intent scoring applied (or manual prioritization by known signals)
- [ ] Buckets system implemented in CRM with 4 contact stages
- [ ] Call script includes pattern-interrupt opener + discovery questions
- [ ] Cadence coordinates calls with email and LinkedIn touches
- [ ] Metrics tracked per rep, per list, per segment (not blended)

## Common Pitfalls

1. **Calling a loose ICP.** A call to a marginal-fit prospect converts at 1/5
   to 1/10 the rate of a perfect-fit prospect. Narrow the target ruthlessly
   before the first dial.

2. **Dialing stale data.** Reps lose over 25% of their time to wrong numbers.
   B2B data decays ~2% per month. Refresh phone numbers quarterly.

3. **Pitching instead of diagnosing.** Reps who pitch on the first call talk past
   the prospect. Discovery: 11-14 questions, listen more than you talk, aim for
   a next step — not a close.

4. **Parallel dialing without phone intent.** Calling multiple prospects at once
   and connecting to whoever answers first creates awkward dead-air pauses. It
   also burns through your TAM — carriers flag you as spam.

5. **No coordination with email and LinkedIn.** The phone is one instrument.
   A LinkedIn view before the first dial, an email after a voicemail — each
   touch aware of the others.

6. **Using switchboard numbers.** 209+ dials per meeting with switchboard
   numbers vs 30-80 with verified direct dials and phone intent. The investment
   that moves the program is always upstream of the call: better data.

7. **Activity metrics over outcome metrics.** 200 dials with 1 conversation
   loses to 50 dials with 10 conversations. Measure conversations, not dials.

## Related Skills

- **multi-channel-outreach**: Coordinate calls with email and LinkedIn
- **cold-email-strategy**: The email side of the outbound motion
- **signal-scoring**: Signals that indicate phone-intent prospects
- **sales-team-building**: SDR hiring, POD structures, compensation
- **meeting-prep**: Pre-call research and discovery questions
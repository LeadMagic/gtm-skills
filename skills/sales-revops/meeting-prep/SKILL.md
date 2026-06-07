---
name: meeting-prep
description: >-
  Prepare comprehensive meeting briefs — account research, attendee profiles,
  SPIN/MEDDIC discovery questions, competitive context. Use when preparing for a
  sales call, discovery meeting, demo, or any prospect interaction. Triggers on:
  "meeting prep", "call prep", "discovery prep", "brief me on", "prepare for
  meeting", "research this account", "pre-call research", "what should I ask",
  "discovery questions", or any request about getting ready for a prospect call.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: sales-revops
  tags: [meeting-prep, discovery, call-prep, research]
  related_skills: [icp-scoring, competitive-intel, objection-handling, demo-scripts]
  frameworks: [Huthwaite SPIN, Force Management MEDDICC, Challenger Teach-Tailor-Take Control]
---

# Meeting Prep

## Overview

Win rates are determined before the call starts. A rep who shows up knowing
the account's recent funding, the attendee's career history, the competitor
they're evaluating, and the discovery questions most likely to surface pain
— that rep wins.

This skill produces a 1-page meeting brief: everything the rep needs to
know in 60 seconds, plus a structured discovery question bank tailored to
the specific account and attendees.

## When to Use

- "Prep me for a call with Acme Corp"
- "What should I ask in this discovery meeting?"
- "Brief me on this prospect before my demo"
- "Research these attendees for tomorrow's call"
- "Build a discovery question bank for [company]"

## Authoritative Foundations

The discovery question structure draws from three frameworks:
- **SPIN** (Huthwaite): Situation → Problem → Implication → Need-Payoff
- **MEDDICC** (Force Management): uncover Metrics, Economic Buyer, Decision
  Criteria, Decision Process, Pain, Champion
- **Challenger** (Gartner): teach something new, tailor to stakeholder, take
  control of the conversation

These are complementary, not competing. SPIN structures the questions,
MEDDICC ensures you cover qualification dimensions, and Challenger ensures
you lead with insight, not just questions.

## Step-by-Step Process

### Phase 1: Account Research

Gather in under 5 minutes:

- **Company basics**: size, industry, revenue, headquarters
- **Recent news**: funding, product launches, executive hires, partnerships
- **Tech stack**: what tools they use (technographics)
- **Competitive landscape**: who they compete with, market position
- **Pain signals**: job postings, review complaints, industry challenges

### Phase 2: Attendee Research

For each attendee:
- Current role, tenure, previous companies
- Recent LinkedIn activity (posts, comments, shares)
- Likely priorities based on role
- Potential personal connection points (shared alma mater, mutual connections)

### Phase 3: Discovery Question Bank

Structure questions by framework:

**SPIN:**
- Situation: "Walk me through how your team currently handles [process]"
- Problem: "What's the biggest frustration with your current approach?"
- Implication: "What does that cost you in terms of [time/money/risk]?"
- Need-Payoff: "If you could solve that, what would change for your team?"

**MEDDICC overlay:**
- Metrics: "How would you measure success for a solution like this?"
- Decision Process: "Who else needs to be involved in this evaluation?"
- Pain: "What happens if you don't solve this in the next [timeframe]?"

**Challenger insight:**
- "Most teams at your stage assume [common misconception]. We've found
  that actually [counterintuitive insight]. Has that been your experience?"

### Phase 4: Competitive Context

If the prospect is evaluating competitors:
1. Which competitors are in the deal?
2. What's our win rate vs each?
3. What are their likely attack angles?
4. Prepare trap-setting questions for our differentiators

## Output Format

One-page meeting brief:
```
# Meeting Brief: [Company Name]
Date: [date] | Attendees: [list]

## Company Snapshot
- Size: X employees, $X revenue
- Industry: [industry]
- Recent: [funding round, product launch, executive hire]
- Tech stack: [relevant tools]

## Attendee Profiles
- [Name], [Title] — [Tenure, key focus area, recent activity]

## Discovery Questions
1. [SPIN Situation question]
2. [SPIN Problem question]
3. ...

## Competitive Context
- Competitors in deal: [list]
- Win strategy: [approach]
- Trap-setting questions: [2-3]

## The Ask
- Desired outcome: [meeting/commitment/next step]
- Fallback if no: [alternative]
```

## Quality Check

- [ ] Account research complete and current (last 30 days)
- [ ] Attendee profiles researched (LinkedIn, recent activity)
- [ ] Discovery questions tailored (not generic template)
- [ ] Competitive context included if relevant
- [ ] Brief fits on one page (rep can read in 60 seconds)
- [ ] Next step and desired outcome defined

## Common Pitfalls

1. **Generic questions.** "What keeps you up at night?" gets a generic answer.
   "I saw you just hired three SDRs — how are you thinking about ramp time?"
   gets a specific, useful response.

2. **Skipping attendee research.** Walking into a call without knowing who's
   in the room and what they care about means you pitch to no one.

3. **Question checklist, not conversation.** Running through 20 questions in
   order feels like an interrogation. Use the question bank as a guide, not
   a script.

4. **No competitive prep.** If you don't know which competitors are in the
   deal, you can't differentiate. Research this before the call.

5. **Researching but not briefing.** Hours of research that the rep can't
   access in 60 seconds is wasted time. Brief format matters.

## Related Skills

- **competitive-intel**: Build battlecards referenced in meeting prep
- **objection-handling**: Anticipate objections before the call
- **demo-scripts**: Structure the demo that follows discovery
- **pipeline-management**: Track deals after the meeting

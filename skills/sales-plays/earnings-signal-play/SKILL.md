---
name: earnings-signal-play
description: >-
  Outbound play triggered by public company earnings calls and SEC filings —
  strategic priority mining from 10-K/10-Q sections, Risk Factor to discovery
  question conversion, MD&A-grounded exec messaging, quarterly cadence.
  Triggers on: "earnings signal", "earnings play", "public company outbound",
  "10-K outreach", "earnings call prospecting", "SEC filing signal".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: sales-plays
  tags: [sales-plays, earnings, public-companies, trigger-based, enterprise]
  related_skills: [cold-email-strategy, meeting-prep, pipeline-management, account-selection, competitive-intel]
  frameworks:
    - "SEC EDGAR — Form 10-K/10-Q filings and SEC Investor Bulletin (sec.gov)"
    - "Jamal Reimer — How to Use a 10-K Report (GTMnow / Sales Hacker)"
    - "Elric Legloire — The 10-K Report Playbook (Outbound Kitchen)"
    - "UserGems — Buying Signals Benchmark Report (4.2M accounts, 2.28M opportunities)"
---

# Earnings Call Signal Play

## Overview

Most sellers who "use earnings signals" watch the call replay or read a
summary newsletter — meaning they react to the same curated quotes as every
other vendor who emails the account that week. The plays that actually open
enterprise doors start with the SEC filing itself: Item 1A Risk Factors is a
ranked list of management's biggest fears, Item 7 MD&A is where executives
explain their own priorities in their own language, and the analyst Q&A layer
reveals what the street is pressuring them on — none of which appears in
earnings recaps. This skill applies Jamal Reimer's mega-deal method and Elric
Legloire's tactical SDR playbook to turn 10-K/10-Q sections into discovery
questions, executive messaging, and a quarterly cadence that lands before
competitors who rely on summaries.

## When to Use

- "Mine earnings calls for signals"
- "Earnings-based outbound for [public company]"
- "Enterprise trigger outreach from SEC filings"
- "10-K prospecting playbook"
- "Outreach grounded in a specific earnings call passage"
- "Private company — borrow signals from public competitors"

## Authoritative Foundations

- **SEC EDGAR — Form 10-K/10-Q and SEC Investor Bulletin (sec.gov).** All
  public-company filings are free on EDGAR. The four sections that drive
  outreach: Item 1 Business (segments, strategy, competitive position),
  Item 1A Risk Factors (listed roughly in order of management's concern —
  the pain-point goldmine), Item 7 MD&A (management's own narrative on
  results, forward priorities, and known uncertainties), and Financial
  Statements (revenue by segment, cost pressures). Used in Phase 1 to
  anchor every outreach claim to a specific, citable filing section.

- **Jamal Reimer — How to Use a 10-K Report (GTMnow / Sales Hacker).** Mega-
  deal seller method: convert Risk Factors directly into discovery questions;
  use MD&A language to mirror how the management team thinks and tailor
  exec-level messaging to their stated priorities; pull revenue-by-business-
  unit numbers from analyst calls to quote in outreach. Applied in Phase 3
  to write outreach anchored in the exec's own language, not vendor copy.

- **Elric Legloire — The 10-K Report Playbook (Outbound Kitchen).** Tactical
  SDR method: Ctrl+F the filing for "risk", "initiative", "strategy",
  "invest in", "headwind"; pair the annual 10-K with the most recent 10-Q to
  see plan vs. actual progress; for private target accounts, read the 10-Ks
  of their public competitors to borrow industry priorities; use an LLM to
  extract the top three to five initiatives relevant to your product category.
  Applied in Phase 1 for keyword extraction and Phase 2 for private-company
  workarounds. Extended reference table in `references/framework-notes.md`.

- **UserGems — Buying Signals Benchmark Report (4.2M accounts, 2.28M
  opportunities analyzed).** Growth signals measurably lift opportunity
  creation; companies often announce news one to three months after the fact,
  so speed of detection matters. Used in Phase 5 as the measurement anchor:
  compare earnings-play reply and opportunity rates against your non-trigger
  baseline.

## Step-by-Step Process

### Phase 1: EDGAR Research (Before the Call)

Pull the filing directly from EDGAR before listening to the call:

1. Search EDGAR (sec.gov) for the company's most recent 10-K and latest 10-Q.
2. Run Legloire's keyword scan: Ctrl+F "risk", "initiative", "strategy",
   "invest in", "headwind", "accelerate", "priority". Log every hit with
   section number and page.
3. Extract signals by section:

| Filing Section | What to Extract | Outreach Use |
|---|---|---|
| Item 1 Business | Segments, stated strategy, competitive position | Initiative owner identification |
| Item 1A Risk Factors | Ranked fears, operational threats | Discovery questions (Reimer method) |
| Item 7 MD&A | Management's priorities, known uncertainties, forward guidance | Exec messaging in management's own language |
| Financial Statements | Revenue by segment, margin trends, cost lines | Proof points on scale and urgency |

4. Pair the 10-K with the most recent 10-Q (Legloire): flag where plan diverges
   from actual — these gaps are live pain points.
5. **Private accounts:** Read the 10-Ks of their top two public competitors to
   borrow industry-level priorities and pressures.

### Phase 2: Earnings Call Transcript Mining

The prepared remarks surface polished strategy; the analyst Q&A reveals
unscripted pressure:

- Source transcripts: Seeking Alpha, The Motley Fool, the IR page, or an LLM
  with browsing.
- Mine prepared remarks for: "investing in", "doubling down on", "hiring [X]
  headcount", "new [product / geography / segment]", "by end of fiscal year".
- Mine analyst Q&A for: topics analysts asked multiple questions on (street
  concern), management deflections (sensitive topics), and any revenue-by-
  business-unit numbers named in follow-ups.
- Use Reimer's method: map analyst pressure questions directly to the exec's
  pain — these become your cold email discovery angles.

### Phase 3: Signal-to-Value Mapping

For each extracted signal, produce a signal card:

| Field | Content |
|---|---|
| Signal | Exact quote with Item/section citation |
| Category | Buying signal / Pain point / Timing marker |
| Initiative owner | Named exec or function from Item 1 or call |
| Your product fit | One concrete value connection, not a feature list |
| Discovery question | Reimer-style open question derived from the signal |

Example:  
Signal: "We plan to hire 60 SDRs in North America by end of Q3" (10-K Item 1,
p. 8).  
Category: Buying signal (team scaling, new tools needed).  
Initiative owner: CRO, VP Sales.  
Discovery question: "Your 10-K flagged a 60-person SDR expansion — how are
you thinking about onboarding speed and early ramp productivity?"

### Phase 4: Executive Outreach Sequence

Target the exec who owns the named initiative — not just any VP.

**Email 1 — Filing Anchor (Earnings Week + Week 1):**

Subject: `Your Q[X] MD&A — [quoted management phrase]`

Body template:
> In [Company]'s [10-K / Q3 10-Q], Item 7, you noted "[exact MD&A quote]."
> The teams I work with at similar scale running [named initiative] typically
> hit [specific friction point] at this stage. Curious how you're approaching
> the [domain] piece — is that a live conversation for you this quarter?

**Email 2 — Risk Factor to Discovery Question (Week 2):**

Convert an Item 1A Risk Factor into a question that shows you read the actual
filing, not a summary.

**Email 3 — Peer Proof Point (Week 3):**

Reference how a similar public company at comparable revenue addressed the
same initiative you identified. Cite the publicly available result.

### Phase 5: Multi-Level Engagement

| Persona | Cadence | Angle |
|---|---|---|
| C-suite | 1 email per quarter max | Strategic: MD&A language, board-level initiative |
| SVP / VP | Initiative-specific, filing-anchored | Reimer method: their language, their priorities |
| Director | Operational connection | "Your SVP's Q3 call highlighted X — here's how teams at your level execute on that" |

Never contact all three levels simultaneously with identical content — each
level should receive a message anchored to their section of the filing.

### Phase 6: Quarterly Cadence

- **Earnings week:** Pull EDGAR filing, run keyword scan, prepare signal cards.
- **Week 1 post-earnings:** Send executive outreach (Email 1 above).
- **Week 2:** Follow up to non-responders with the Risk Factor discovery angle.
- **Week 3:** Expand to Director level with operational connection.
- **Between quarters:** Maintain with quarterly strategic touch; refresh signal
  cards when the next filing drops. Per UserGems research, companies often
  announce initiatives one to three months after they begin — file-date
  monitoring captures earlier signals than press coverage.

## Output Format

Earnings play playbook containing: keyword-scanned EDGAR filing notes with
section citations, signal cards (signal / category / owner / product fit /
discovery question), filing-anchored outreach emails per persona, and a
quarterly cadence calendar. Reference the extended filing-to-outreach mapping
table in `references/framework-notes.md`.

## Quality Check

Before delivering, verify:
- [ ] Every outreach email quotes a specific filing section (Item 1, Item 1A,
      Item 7) or named call passage — not a paraphrase from a news summary
- [ ] Outreach targets the exec who owns the named initiative, identified in
      Item 1 or the call transcript — not a generic title match
- [ ] Signal cards exist for at least three extracted signals with section
      citations, initiative owners, and discovery questions
- [ ] Play is executed within the earnings window (within two weeks of filing
      or call date)
- [ ] Private target accounts are handled via the Legloire competitor 10-K
      method — not skipped
- [ ] Multi-level emails carry different angles by persona — not the same
      message sent to all three levels
- [ ] Measurement baseline established: non-trigger reply rate documented so
      earnings-play lift is calculable against the UserGems benchmark

## Common Pitfalls

1. **Reading a summary instead of the actual filing.** Summaries surface the
   same bullet points every competitor reads. Fix: pull the 10-K/10-Q from
   EDGAR directly, run the keyword scan on the full text, and cite section
   numbers in outreach — it signals to the exec that you did the work.

2. **Mining the prepared remarks while ignoring the analyst Q&A.** The
   prepared remarks are polished strategy. The Q&A is where analysts press on
   weak spots and executives respond under pressure. Fix: read the transcript
   end-to-end; topics that draw multiple analyst questions are the live street
   concerns — and your discovery angles.

3. **Opening with generic "I saw your earnings call" framing.** This is the
   default opener from every vendor monitoring the same recap newsletters.
   Fix: use Reimer's method — mirror the executive's own MD&A language in the
   subject line and first sentence so it reads as a peer conversation, not
   vendor outreach.

4. **Targeting any VP instead of the initiative owner.** Sending the same
   earnings-signal email to all VPs dilutes relevance. Fix: trace the
   initiative back to a named leader or business unit in Item 1 or the call,
   and route the email to that specific owner.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- cold-email-strategy, meeting-prep, pipeline-management, account-selection, competitive-intel

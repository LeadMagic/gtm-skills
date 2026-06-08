---
name: signal-scoring
description: >-
  Score and prioritize prospects using buying signals — hiring, funding, tech
  stack changes, executive moves, and intent data. Use when the user wants to
  score leads, prioritize outreach, detect buying intent, rank prospects, or
  find the hottest accounts. Triggers on: "score leads", "prioritize", "signals",
  "buying intent", "trigger events", "who should we contact first", "lead
  scoring", "signal detection", "intent data", or any request to rank prospects
  by readiness-to-buy.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: prospecting
  tags: [signals, scoring, intent, prioritization, triggers]
  related_skills: [icp-scoring, lead-enrichment, proactive-alerts]
  frameworks:
    - "ColdIQ Signal Taxonomy"
    - "Explorium Signal-Based Selling"
    - "Aaron Ross — Predictable Revenue"
---

# Signal Scoring

## Overview

Most prospects aren't ready to buy. Signals separate the ones who are from the
ones who might be someday. A signal-anchored outreach program consistently
outperforms list-blast approaches — triggers beat blasts every time.

This skill builds a configurable signal scoring system. You define which signals
matter for your business, assign weights, and produce tiered lead lists that
tell your team exactly who to contact first and why.

## When to Use

- "Score these accounts and tell me who to reach out to first"
- "Set up a signal scoring system for our ICP"
- "Which of our target accounts are showing buying signals?"
- "Prioritize this list by intent"
- "Build a trigger-based outreach prioritization model"

## Authoritative Foundations

Signal-based selling as practiced by ColdIQ and Explorium demonstrates that
trigger-anchored outreach achieves 2-3x higher reply rates than generic cold
email. The core principle: reach out when something changed, not when you
decided to run a campaign.

The priority rule is recency + specificity. A website pricing page visit from
yesterday beats a Bombora intent surge from last week. The signal with the
clearest, most recent tie to purchase intent leads the outreach.

## Prerequisites

- ICP defined (use icp-scoring first)
- Target account list to score
- Data sources: job boards, funding databases, tech stack monitors, intent platforms

## Step-by-Step Process

### Phase 1: Define Signal Taxonomy

Choose from four categories. Assign weights based on what correlates with
closed-won deals in your sales data:

| Signal Category | Example Signals | Default Weight |
|---|---|---|
| **Hiring** | Job postings for roles your product supports, team expansion, new leadership | 0-25 pts |
| **Funding** | Recent round closed, new investor, funding amount | 0-20 pts |
| **Tech Stack** | Added complementary tool, removed competitor, new technology adoption | 0-25 pts |
| **Intent** | Website visits, content downloads, search behavior, review site activity | 0-30 pts |

Total possible: 100 points. Adjust weights based on your sales data — weight the
signals that correlate with closed-won.

### Phase 2: Configure Signal Detection

For each signal category, set up detection sources:

- **Hiring**: Job board search (LinkedIn, Indeed, Greenhouse). Sales hiring =
  highest signal. LeadMagic Jobs Finder for automated detection.
- **Funding**: Crunchbase, PitchBook, news monitoring.
- **Tech Stack**: BuiltWith, Wappalyzer, Clay technographics. Monthly snapshots
  with change detection.
- **Intent**: Bombora, G2, LeadMagic Company Search for firmographic signals.

### Phase 3: Score Each Account

For each target account:
1. Check each signal category
2. Apply the weight for each detected signal
3. Sum to get total signal score (0-100)

Priority rule for multiple signals: score only the single most relevant signal
per account. Recency + specificity determines which signal leads.

### Phase 4: Tier and Route

| Tier | Score Range | Action | SLA |
|---|---|---|---|
| **A — Hot** | 80-100 | Immediate personalized outreach. Multi-thread. | Within 24 hours |
| **B — Warm** | 60-79 | Enroll in sequence. Monitor for new signals. | Within 3 days |
| **C — Cool** | 40-59 | Nurture track. Re-score in 30 days. | Nurture drip |
| **Discard** | <40 | Not yet. Re-evaluate quarterly. | No action |

## Output Format

Scored account list with signal breakdown:

```
Account: Acme Corp
Total Signal Score: 85 (Tier A — Hot)

Signals detected:
- Hiring: 3 new SDR roles posted this week (20 pts)
- Funding: Series B closed last month, $25M (15 pts)
- Tech Stack: Added Salesforce last quarter (15 pts)
- Intent: Visited pricing page 3x this week (25 pts)
- ICP fit bonus: Exact match on industry + size (10 pts)

Recommended action: Outreach within 24 hours. Lead with hiring signal.
Suggested angle: "Saw you're scaling the SDR team — most teams at your
stage struggle with ramp time. We helped [similar company] cut it by 40%."
```

## Quality Check

- [ ] Signal weights calibrated against actual closed-won data
- [ ] Only one primary signal drives outreach per account
- [ ] Tier routing rules defined and automated
- [ ] Signal sources documented with refresh cadences
- [ ] Re-score schedule set (weekly for A tier, monthly for B/C)

## Common Pitfalls

1. **Acting on too many signals per account.** A company showing 5 signals
   doesn't mean send 5 different emails. Pick one — the most recent and
   specific — and lead with it.

2. **Weights not calibrated to your data.** Default weights are a starting
   point. Review quarterly against your closed-won deals and adjust.

3. **Stale signals.** A funding round from 6 months ago is no longer a
   trigger. Signal freshness matters. Set expiration windows.

4. **No action on signals.** A signal without an immediate, automated
   action is just noise. Every detection should trigger a workflow.

5. **Equal-weight scoring.** Not all signals are equal. A company hiring
   for a role your product directly supports is worth more than a generic
   intent signal. Weight accordingly.

## Related Skills

- **icp-scoring**: ICP fit scoring runs before signal scoring
- **proactive-alerts**: Automated signal monitoring and alert routing
- **cold-email-strategy**: Turn signal scores into outreach sequences
- **lead-enrichment**: Enrich accounts to enable signal detection

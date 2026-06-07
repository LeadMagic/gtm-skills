---
name: account-selection
description: >-
  Select and prioritize target accounts for ABM programs — scoring models, tier
  assignment, TAM segmentation. Triggers on: "account selection", "target account list",
  "tier accounts", "prioritize accounts", "TAM segmentation".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: abm
  tags: [abm, account-selection, scoring, tiering, target-accounts]
  frameworks: [TOPO Account Selection, WbD ICP Framework]
---

# Account Selection & Tiering

## Overview
Account selection is the hardest part of ABM. Pick wrong and you waste 6 months.
Pick right and you 3x your close rate. This skill builds a weighted scoring model
to tier your TAM into Strategic, Scale, and Programmatic accounts.

## When to Use
- "Which accounts should we target?"
- "Tier our target account list"
- "Build an account scoring model"
- "Prioritize our TAM for ABM"

## Step-by-Step Process

### Phase 1: Build Scoring Model
Weight each dimension (must total 100 points):

**Firmographic Fit (35 pts):**
- Industry match (0-10): Direct ICP industry = 10, adjacent = 5, outside = 2
- Employee count (0-10): In sweet spot = 10, near = 5, outside = 2
- Revenue range (0-10): In sweet spot = 10, near = 5, outside = 2
- Geography (0-5): Target region = 5, acceptable = 3, outside = 1

**Technographic Fit (25 pts):**
- Current tech stack (0-15): Complementary tools present = 15, some = 8, none = 2
- Integration potential (0-10): High integration value = 10, medium = 5, low = 2

**Behavioral Signals (25 pts):**
- Website visits (0-10): Frequent, multi-page = 10, some = 5, none = 2
- Content engagement (0-10): Downloads, webinar attendance, newsletter = score by recency
- Social engagement (0-5): LinkedIn follows, comments, shares

**Intent & Trigger (15 pts):**
- Hiring signals (0-5): Role related to your product = 5
- Funding event (0-5): Recent raise = 5
- Tech change (0-5): Evidence of switching or evaluating

### Phase 2: Tier Assignment
- **Tier 1 (>80):** 5-15 accounts. Immediate sales + marketing investment.
- **Tier 2 (60-79):** 15-50 accounts. Scaled ABM plays.
- **Tier 3 (40-59):** 50-200 accounts. Programmatic nurture.
- **Below 40:** Not ABM. Generic inbound/outbound only.

### Phase 3: Ongoing Refinement
- Monthly: Re-score based on new signals
- Quarterly: Review tier assignments, promote/demote accounts
- After wins: Analyze what made winners score high — adjust weights
- After losses: Add disqualifying signals discovered in lost deals

## Output Format
Scored account list with tier assignments, scoring model documentation, and a
refinement calendar.

## Related Skills
- icp-scoring, abm-strategy, signal-scoring, lead-finding, list-building

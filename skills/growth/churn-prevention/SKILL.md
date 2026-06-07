---
name: churn-prevention
description: >-
  Build churn prevention systems — early warning signals, re-engagement campaigns,
  health scoring, risk tier routing. Use when reducing churn, building retention
  systems, or detecting at-risk customers. Uses Winning by Design Bowtie and SPICED.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: growth
  tags: [churn, retention, health-scoring, customer-success]
  frameworks: [Winning by Design Bowtie, SPICED Lifecycle]
---

# Churn Prevention

## Overview
Churn is rarely sudden. Usage drops, NPS declines, support tickets spike — signals appear weeks before cancellation. A churn prevention system catches these signals early and triggers re-engagement before the customer decides to leave. This skill builds early warning detection, health scoring, and automated re-engagement workflows.

## When to Use
- "Set up churn prevention"
- "Detect at-risk customers"
- "Build a customer health score"
- "Reduce our churn rate"

## Step-by-Step Process
### Phase 1: Signal Detection
Monitor: usage decline (>30% drop in 30 days), NPS drop, support ticket spike, champion departure (use job change detection), payment failure, contract renewal approaching without engagement.

### Phase 2: Health Scoring
Score each account 0-100: product usage (0-40), engagement (0-30), relationship health (0-30). Red (<50): immediate outreach. Yellow (50-74): monitor, nurture. Green (75+): healthy.

### Phase 3: Re-Engagement Playbooks
Automated workflows per risk tier. Red: CSM personal outreach within 24 hours. Yellow: automated nurture with success stories and best practices. Green: expansion-focused outreach.

## Output Format
Churn prevention system with signal catalog, health score model, re-engagement playbooks, and monitoring dashboard spec.

## Common Pitfalls
1. **Detecting churn after it happens** — health scoring must be leading, not lagging.
2. **Generic re-engagement** — "we miss you" emails do not work. Specific value reminders do.
3. **No champion monitoring** — champion departure is the #1 churn predictor. Detect it automatically.

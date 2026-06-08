---
name: pipeline-management
description: >-
  Manage B2B sales pipelines with structured deal stages, forecasting, CRM hygiene,
  and deal inspection cadences. Use when setting up pipeline processes, improving
  forecast accuracy, or designing deal stages. Triggers on: "pipeline management",
  "forecasting", "deal inspection", "CRM hygiene", "pipeline review", "deal stages",
  "sales process", or any pipeline-related request.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: sales-revops
  tags: [pipeline, forecasting, crm, deal-management]
  related_skills: [meeting-prep, proactive-alerts, crm-integration, gtm-metrics]
  frameworks:
    - "Winning by Design GTM Playbook Kit"
    - "Miller Heiman Blue Sheet"
    - "MEDDICC — Qualification"
---

# Pipeline Management

## Overview

A pipeline without defined stages is a collection of guesses. Every deal stage
needs a clear goal, in-stage actions, and exit criteria that align rep behavior
with buyer progress — not internal opinions.

This skill designs a stage-based sales process following Winning by Design's
GTM Playbook Development Kit: Goal + Exit Criteria per stage, informed by
Miller Heiman's buying influence mapping for complex deals.

## When to Use

- "Design our sales process stages"
- "Improve our forecast accuracy"
- "Set up deal stages in our CRM"
- "Build a pipeline review cadence"
- "Our pipeline is unpredictable — fix it"
- "Define what good looks like at each deal stage"

## Authoritative Foundations

Winning by Design's GTM Playbook Development Kit establishes that every
sales process stage must have: a clear Goal (what success looks like at
this stage), In-Stage Actions (what the rep does), and Exit Criteria
(evidence required before moving to the next stage).

Miller Heiman's Strategic Selling adds buying influence mapping: for
complex enterprise deals, understanding who influences the decision
and what matters to each stakeholder is as important as the rep's actions.

## Prerequisites

- CRM system configured (HubSpot, Salesforce, or Attio)
- Sales methodology selected (MEDDICC, SPICED, SPIN, etc.)
- Average deal size and sales cycle length known

## Step-by-Step Process

### Phase 1: Stage Design

Define each stage with Goal, In-Stage Actions, and Exit Criteria:

| Stage | Goal | Exit Criteria |
|---|---|---|
| 1. Prospect | Identified potential fit | ICP fit confirmed, contact verified |
| 2. Connect | Initial contact, interest established | Reply received, problem acknowledged |
| 3. Discovery | Pain quantified, stakeholders identified | SPICED/MEDDIC dimensions documented |
| 4. Solution | Solution mapped to pain, technical validation | Demo completed, requirements confirmed |
| 5. Proposal | Commercial terms presented | Proposal sent, pricing discussed |
| 6. Negotiation | Terms finalized, procurement engaged | Redlines resolved, legal review started |
| 7. Closed Won | Contract signed | Signed agreement, payment processed |
| 8. Closed Lost | Deal lost — learn | Loss reason documented, competitive intel captured |

### Phase 2: Forecast Categories

Map stages to forecast categories:

| Stage | Forecast Category | Confidence |
|---|---|---|
| 1-2 | Pipeline | 10-20% |
| 3-4 | Upside | 30-50% |
| 5-6 | Commit | 70-85% |
| 7 | Closed Won | 100% |

### Phase 3: Deal Inspection Cadence

Weekly pipeline review structure:
1. New deals entered this week — qualified?
2. Deals stalled >14 days in stage — why?
3. Commit deals at risk — what changed?
4. Deals with missing next steps — action required
5. Deals with close date pushed — pattern or anomaly?

## Output Format

Sales process definition document with stage definitions, forecast categories,
deal inspection templates, and CRM field mapping.

## Quality Check

- [ ] Every stage has defined Goal and Exit Criteria
- [ ] Forecast categories map to stages with explicit confidence ranges
- [ ] Weekly pipeline review cadence established
- [ ] Deal inspection checklist created
- [ ] CRM fields support stage progression logic

## Common Pitfalls

1. **Subjective stages.** "I feel good about this deal" is not a stage.
   Exit criteria are evidence, not feelings.

2. **No stage time limits.** Deals sitting in Discovery for 60 days aren't
   in Discovery — they're stalled. Set time-based alerts.

3. **Forecast based on hope.** Committing deals without verified exit criteria
   creates forecast noise that compounds at every level.

4. **Too many stages.** 12-stage processes create administrative overhead
   without improving accuracy. 5-7 stages is the sweet spot.

5. **CRM as the process.** The CRM reflects the process, not defines it.
   Design the process first, then configure the CRM to support it.

## Related Skills

- **proactive-alerts**: Automated alerts on pipeline risks
- **gtm-metrics**: Pipeline metrics and dashboards
- **crm-integration**: CRM configuration for pipeline stages

---
name: leadmagic-job-change
description: >-
  Use LeadMagic job-change signals for pipeline intelligence — champion tracking,
  account risk alerts, new-role outreach, replacement mapping, and CRM routing.
  Use when monitoring career moves or building trigger-based sales plays.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: leadmagic
  tags: [leadmagic, job-change, champion-tracking, signals, pipeline]
  related_skills: [job-change-play, signal-scoring, pipeline-management, expansion-selling]
  frameworks: [Signal-Based Selling, Champion Tracking Methodology, ColdIQ Trigger Selling, Winning by Design Bowtie]
---

# LeadMagic Job Change Detection

## Overview

Job changes are one of the cleanest B2B buying signals, but most teams waste them with generic congratulations. A champion moving to a new company creates a warm expansion path. A decision-maker leaving an open opportunity creates risk. A former buyer joining a target account creates an account entry point.

This skill routes LeadMagic job-change signals into the right GTM action without exposing any internal detection method.

## When to Use

Use this skill when the user asks to "track job changes for my contacts", "alert me when champions change jobs", "monitor career moves in my pipeline", "build job-change outreach", "find expansion opportunities from past buyers", "detect deal risk when stakeholders leave", "create champion tracking alerts", or "route job-change signals into CRM".

Use `job-change-play` when the user wants the outbound sequence itself. Use this skill when the focus is monitoring, routing, and operations.

## Authoritative Foundations

### Signal-Based Selling
High-conversion outbound starts with a relevant event. Job changes create context: new priorities, new budget influence, new team-building moments, and relationship continuity.

### Champion Tracking Methodology
Champions are assets that move. Tracking them helps preserve relationship equity across accounts and flags risk when they leave active deals.

### ColdIQ — Trigger Selling
Trigger-based messages work when the trigger is specific, timely, and connected to a plausible business problem. A job change should route to different messaging depending on relationship history and role.

### Winning by Design — Bowtie Model
Job changes matter across the bowtie: acquisition, conversion, retention, expansion, and advocacy. The same signal can mean opportunity or risk depending on account status.

## Prerequisites

- Contact list with CRM ID or stable external ID
- Account ownership rules
- Active opportunity list
- Customer and former-customer lists
- Suppression rules
- Alert destination: Slack, CRM task, email, or webhook
- Outreach templates by scenario

## Step-by-Step Process

### Phase 1: Segment Contacts by Relationship

| Contact Type | Why It Matters | Primary Route |
|---|---|---|
| Current customer champion | Expansion / retention risk | CS + AE alert |
| Former customer champion | New-account warm path | AE/BDR outreach |
| Open opportunity stakeholder | Deal risk or new influencer | Opportunity owner alert |
| Past closed-lost stakeholder | Re-engagement signal | BDR nurture |
| Target account contact | New trigger for outbound | SDR sequence |

### Phase 2: Classify the Job Change

Capture old company, old title, new company, new title, seniority change, function change, relationship history, account status, and recommended action.

A promotion into budget authority is different from a lateral move into a non-buyer role.

### Phase 3: Route Alerts

| Scenario | Alert Owner | SLA | Action |
|---|---|---|---|
| Champion joins target account | Account owner | 24 hours | Warm new-role outreach |
| Champion leaves customer | CSM + AE | 24 hours | Risk review + replacement mapping |
| Decision-maker leaves open opp | AE + manager | Same day | Deal risk review |
| Former buyer joins new company | BDR/AE | 48 hours | Relationship-led outreach |

### Phase 4: Draft Outreach

Message rules: congratulate briefly, reference real relationship context, tie to likely new-role priorities, do not imply surveillance, and ask for a low-friction next step.

Bad: "We saw you changed jobs and want to sell you again."
Good: "Congrats on the move to [Company]. When you led [function] at [Old Company], [relevant context]. If [new priority] is on your plate, happy to share what worked."

### Phase 5: Measure Outcomes

Track alerts generated, alerts actioned within SLA, meetings booked, pipeline created, customer risk cases opened, and replacement stakeholders mapped.

## Output Format

```markdown
# Job Change Signal Routing Plan

## Monitored Segments
| Segment | Owner | Alert Destination | SLA |
|---|---|---|---|

## Routing Rules
| Job Change Scenario | Recommended Action | Owner | Template |
|---|---|---|---|

## Outreach Draft
Subject:
Email:
CTA:

## Metrics
- Alerts:
- SLA adherence:
- Meetings:
- Pipeline:
- Risk cases:
```

## Quality Check

Before delivering, verify:

- [ ] Every signal is routed by relationship type
- [ ] Active customer and opportunity risks are separated from new-logo opportunities
- [ ] Outreach references real relationship context only
- [ ] SLA and owner are assigned for each alert type
- [ ] CRM task or alert destination is specified
- [ ] Metrics include both opportunity creation and risk detection

## Common Pitfalls

1. **Generic congratulations.** It wastes the signal. Fix: connect the move to prior relationship or new-role priority.
2. **No account-status logic.** Same signal means different things for customer vs prospect. Fix: route by account status.
3. **Slow outreach.** Job-change relevance decays quickly. Fix: SLA within 24-48 hours.
4. **Ignoring risk.** Champion departure can threaten renewals and deals. Fix: route customer/opportunity signals to owners.
5. **Implying creepy monitoring.** "We saw you moved" can feel invasive. Fix: keep the note natural and relationship-led.
6. **No replacement mapping.** When a champion leaves, the old account still matters. Fix: identify successor and stakeholder gaps.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- `job-change-play` — outbound play for job-change triggers
- `signal-scoring` — prioritize which changes matter
- `pipeline-management` — route deal-risk alerts
- `expansion-selling` — turn champion moves into expansion paths

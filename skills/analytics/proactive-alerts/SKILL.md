---
name: proactive-alerts
description: >-
  Set up proactive GTM alert systems — CRM pipeline alerts, buying signal
  notifications, Slack/email routing, risk scoring. Use when building alert
  systems, monitoring pipeline health, detecting buying signals, or setting
  up automated notifications for GTM teams. Triggers on: "alerts", "notifications",
  "pipeline alerts", "signal alerts", "monitor pipeline", "deal alerts", "Slack
  alerts", "pipeline monitoring", "proactive", "warning system", or any request
  about automated detection and notification.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: analytics
  tags: [alerts, monitoring, pipeline, signals, notifications]
  related_skills: [signal-scoring, pipeline-management, deliverability-monitoring, gtm-metrics]
  frameworks: [UnifiedPipeline Risk Scoring, SyncGTM Signal Monitoring, Alysio Pipeline Risk Detection]
---

# Proactive Alerts

## Overview

GTM teams spend 30% of their time checking dashboards that should be checking
themselves. Proactive alerts invert this: the system watches your pipeline and
signals 24/7, pushing notifications only when something needs attention.

This skill designs an alert architecture: what to monitor, when to alert, who
to notify, and how to route each signal type to the right person at the right
time — all without alert fatigue.

## When to Use

- "Set up pipeline alerts"
- "Notify me when a deal stalls"
- "Alert the team on buying signals"
- "Build a deal risk monitoring system"
- "Set up Slack notifications for pipeline changes"
- "Create a signal-to-Slack pipeline"

## Authoritative Foundations

Alert design draws from UnifiedPipeline's deal risk scoring methodology
(transparent scores, daily briefings), SyncGTM's 15+ signal monitoring
system, and Alysio's pipeline risk detection layer (engagement, sentiment,
velocity, and qualification signals).

## Prerequisites

- CRM with webhook or API access (HubSpot, Salesforce)
- Slack or Teams for delivery
- Signal data sources (job boards, funding databases, tech stack monitors)

## Step-by-Step Process

### Phase 1: Alert Categories

| Category | Examples | Urgency | Channel |
|---|---|---|---|
| **Pipeline Risk** | Deal stalled >7 days, close date pushed, amount decreased, stage moved backward, missing next steps, no activity | High — requires action today | Slack DM to rep + manager |
| **Buying Signals** | Funding raised, hiring surge, exec change, tech stack shift, job change, website visit spike | High — time-sensitive outreach | Slack channel + CRM task |
| **Positive Signals** | Deal revived, amount increased, close date pulled in, new large deal created | Medium — awareness | Daily briefing |
| **Operational** | Bounce rate spike, domain health alert, sequence completion, credit usage threshold | Medium — requires monitoring | Slack channel |
| **Forecast** | Commit deal at risk, large deal slipped, pipeline coverage below target | High — executive visibility | Slack to CRO + weekly report |

### Phase 2: Alert Configuration by Role

| Role | Alerts They Receive |
|---|---|
| **SDR** | New lead assigned, lead response overdue, sequence bounce alert |
| **AE** | Deal stalled, close date pushed, competitor detected, champion left company |
| **Manager** | Team pipeline coverage, rep activity gaps, deal inspection flags |
| **CRO** | Forecast changes >20%, large deal at risk, pipeline coverage drop |
| **RevOps** | CRM data quality flags, integration failures, enrichment gaps |

### Phase 3: Routing and Delivery

1. **Real-time / Urgent** → Slack DM or dedicated #pipeline-alerts channel
2. **Daily briefing** → Scheduled message at 7am with ranked risk list
3. **Weekly digest** → Summary of all alerts, trends, and actions taken
4. **Escalation** → If alert acknowledged but no action in 24 hours → manager notified

### Phase 4: Alert Fatigue Prevention

- Max 5 high-priority alerts per person per day
- Group related alerts into single messages
- Allow per-user alert configuration (mute categories, adjust thresholds)
- Track alert-to-action rate — if alerts aren't driving action, tune thresholds
- Monthly alert audit: remove or adjust alerts with <10% action rate

## Output Format

Alert architecture document with alert catalog, routing rules, delivery
templates, threshold configuration, and fatigue prevention rules.

## Quality Check

- [ ] Alert catalog covers pipeline risk, buying signals, positive signals, operational, and forecast
- [ ] Every alert has a defined owner and SLA for response
- [ ] Routing rules documented (who gets what, when)
- [ ] Alert fatigue thresholds set (max per person, per day, per channel)
- [ ] Daily briefing template created
- [ ] Monthly alert audit cadence established

## Common Pitfalls

1. **Alerting on everything.** A Slack channel with 50 alerts/day becomes
   invisible. Curate ruthlessly. Only alerts that require action should fire.

2. **No owner.** An alert that goes to a channel with no named owner gets
   ignored. Every alert type has one person accountable.

3. **Alerting without context.** "Deal X stalled" without "it's been in Demo
   for 14 days, last contact was a bounce, and the champion changed jobs"
   doesn't help. Context drives action.

4. **Same alert for everyone.** An SDR doesn't need CRO-level pipeline alerts.
   Tailor by role or risk burnout.

5. **No alert audit.** Alerts that were urgent 6 months ago may be noise now.
   Audit monthly and remove or tune.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- **signal-scoring**: The signal detection that feeds buying signal alerts
- **pipeline-management**: Pipeline structure that enables risk detection
- **deliverability-monitoring**: Bounce and reputation alerts
- **gtm-metrics**: Dashboard metrics that complement alerts

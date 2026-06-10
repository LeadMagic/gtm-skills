---
name: inbound-triage
description: >-
  Design inbound lead triage workflows — demo form qualification, MQL to SQL
  routing, automated enrichment on form fill, speed-to-lead SLAs. Use when the
  user wants to handle inbound leads, route demo requests, qualify form fills,
  or build an inbound pipeline. Triggers on: "inbound triage", "demo request",
  "lead routing", "MQL", "SQL", "speed to lead", "form qualification", "inbound
  process", "qualify inbound leads", or any request about handling incoming leads.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: inbound
  tags: [inbound, triage, routing, qualification, lead-management]
  related_skills: [lead-scoring, pipeline-management, crm-integration, sales-enablement, website-visitor-identification, icp-scoring]
  frameworks:
    - "Winning by Design SPICED Lifecycle"
    - "SiriusDecisions Demand Waterfall"
    - "Dharmesh Shah (HubSpot) — Inbound Engage & Flywheel Handoff"
    - "HubSpot Academy — Inbound Methodology"
---

# Inbound Triage

## Overview

Speed kills in inbound. A lead contacted within 5 minutes is 100x more likely
to convert than one contacted after 30 minutes. Yet most teams route leads
manually, respond in hours, and wonder why inbound doesn't convert.

This skill designs an automated inbound triage system: enrichment on form fill,
ICP qualification in seconds, routing to the right rep, and SLAs enforced from
moment one. The output is a complete inbound workflow that captures every lead
and routes it faster than any human team.

## When to Use

- "Set up inbound lead routing"
- "How should we handle demo requests?"
- "Qualify our inbound leads automatically"
- "Build an MQL to SQL handoff process"
- "Speed up our lead response time"
- "Design an inbound qualification workflow"

## Authoritative Foundations

Inbound triage follows Winning by Design's SPICED lifecycle model, which maps
the full customer journey from first contact through expansion. The inbound stage
sits at the critical handoff between marketing (MQLs) and sales (SQLs).

SiriusDecisions' Demand Waterfall framework establishes that clear MQL/SQL
definitions with automated routing correlate with 20%+ higher conversion rates
and 30%+ faster sales cycles.

**Dharmesh Shah (HubSpot) — Engage stage.** Inbound triage is the operational
**Engage** leg of the flywheel: speed-to-lead, enrichment on form fill, and
fit-based routing (not volume-based MQL inflation). Canonical playbook →
`references/dharmesh-shah-hubspot-inbound.md` · Pattern 27 step 4.

## Prerequisites

- ICP defined (what makes a lead qualified)
- CRM system (HubSpot, Salesforce, or Attio)
- Enrichment provider for real-time lead enrichment on form fill
- Lead scoring model (see lead-scoring skill)

## Step-by-Step Process

### Phase 1: Define Lead Stages

| Stage | Definition | Qualification Criteria | Owner |
|---|---|---|---|
| Lead | Any identified contact | Has email, some interest signal | Marketing |
| MQL | Fits ICP + engaged | Firmographic fit + behavior threshold | Marketing → SDR |
| SQL | Ready for sales conversation | MQL + explicit buying signal or demo request | Sales |
| PQL (if PLG) | Used product, upgrade potential | Trial/freemium + usage threshold | Product + Sales |
| SAL | SQL accepted by rep | Sales confirms qualification | Sales |

### Phase 2: Build the Triage Workflow

**Website visitor intent (company ID):** Anonymous visits identified via
reverse-IP (`website-visitor-identification`) feed account-level intent scores.
Route to MQL only when ICP + engagement thresholds pass — not on every visit.
Person-level visitor alerts use separate guardrails; default path is company ID
→ SDR research queue. Playbook:
`website-visitor-identification/references/visitor-identification-playbook.md`.

1. **Form fill triggers enrichment.** Webhook from form (HubSpot, Typeform,
   custom) fires enrichment on submit. Within 15 seconds, the lead is
   enriched with firmographic and contact data.

2. **ICP filter runs.** Enriched data feeds into ICP scoring. Leads that
   don't fit the ICP get an automated nurture email and are routed to the
   marketing nurture track.

3. **MQL scoring.** Leads passing ICP filter are scored on engagement
   signals: pages visited, content downloaded, demo requested.

4. **Routing.** MQLs above threshold route to SDR within 15 minutes.
   Demo requests route directly to AE with calendar hold.

5. **SLA enforcement.** Track response time, 2nd touch time, 3rd touch
   time. Alert manager when SLAs are breached.

### Phase 3: Speed-to-Lead SLAs

| Touch | Target Time | Action |
|---|---|---|
| 1st touch | <5 minutes | Auto-response with calendar link + qualifying question |
| 2nd touch | <15 minutes | Value drop + booking link |
| 3rd touch | <2 hours | Nudge + social proof |
| 4th touch | Same day | Call + personalized email |
| 5th touch | 24 hours | Final attempt before nurture |

### Phase 4: Exceptions and Escalation

- **Enterprise leads** (>target ACV): immediate AE assignment, skip SDR
- **Partner referrals**: warm intro process, founder or AE handles
- **Support disguised as sales**: route to support, don't waste SDR time
- **Competitors/spam**: auto-archive, suppress from future routing

## Output Format

Inbound triage workflow diagram + SLA document:
```
# Inbound Triage Workflow

Form Fill → Enrich (15s) → ICP Filter → Score → Route → SLA Enforcement

Routing rules:
- Demo request + ICP fit → AE calendar hold (5 min)
- MQL + score >60 → SDR (15 min)
- MQL + score 40-60 → Nurture track
- Non-ICP → Marketing nurture
- No enrichment data → Manual review queue

SLA dashboard:
- Response time by rep
- MQL→SQL conversion rate
- SQL→Opportunity conversion rate
- Lead leakage (where leads drop out)
```

## Quality Check

- [ ] Lead stages defined with clear qualification criteria
- [ ] Enrichment completes within 15 seconds of form fill
- [ ] SLAs defined and tracked for every touch
- [ ] Routing rules documented and automated
- [ ] Escalation paths for exceptions
- [ ] Weekly SLA review cadence established

## Common Pitfalls

1. **Manual routing.** Every minute of manual routing is a minute the lead
   waits. A lead contacted in 5 minutes is 100x more likely to convert than
   one contacted in 30 minutes. Automate routing end-to-end.

2. **No enrichment before routing.** Routing an unenriched lead means the
   SDR wastes time researching basic info. Enrich on form fill automatically.

3. **Vague stage definitions.** When MQL means different things to marketing
   and sales, leads bounce between teams. Define stages with hard criteria.

4. **SLA theater.** Defining SLAs without tracking and enforcement means
   they're aspirational. Automate alerting when SLAs are missed.

5. **Over-qualifying inbound.** An inbound lead who took the time to fill
   a form has already self-qualified to some degree. Don't make them jump
   through more hoops — get them to a human.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **website-visitor-identification**: Company/person visitor ID → MQL routing
- **lead-scoring**: Build the scoring model that powers triage decisions
- **pipeline-management**: Manage leads after they enter the pipeline
- **crm-integration**: CRM setup for automated routing and enrichment

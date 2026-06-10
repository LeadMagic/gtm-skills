---
name: n8n-toolkit
description: >-
  Complete n8n GTM toolkit — workflow blueprints for inbound, outbound, signals,
  CRM sync, and lifecycle; MCP integration patterns; node design, error handling,
  and production deployment. Use when building n8n flows for GTM, connecting MCP
  servers to orchestration, or replacing Clay for complex branching. Triggers on:
  "n8n workflow", "n8n GTM flow", "n8n inbound", "n8n outbound", "n8n MCP",
  "build n8n automation", "n8n webhook CRM", "n8n enrichment pipeline".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "2.0.0"
  author: LeadMagic
  category: tools
  tags: [n8n, automation, workflow, webhook, mcp, inbound, outbound, enrichment, gtm-flows]
  related_skills: [n8n-automation, mcp-setup, leadmagic-mcp, leadmagic-toolkit, clay-toolkit, clay-loops-toolkit, ai-prompts-toolkit, crm-toolkit, crm-integration, inbound-triage, reply-handling, proactive-alerts, event-analytics]
  frameworks:
    - "n8n — Open-source workflow automation, 400+ integrations, queue mode"
    - "Model Context Protocol — Agent tool access and orchestration"
    - "iPaaS Integration Patterns — Event-driven, webhook, batch ETL"
    - "Winning by Design — Bowtie handoffs (marketing → sales → CS)"
    - "ColdIQ — Signal-to-action routing"
---

# n8n Toolkit

## Overview

n8n is the orchestration layer for GTM when Clay's spreadsheet model or a
single MCP agent isn't enough — multi-branch routing, custom APIs, queue
pause/resume, and cross-tool pipelines with real error recovery. The mistake:
copying a generic "webhook → API → CRM" template without motion-specific
logic, idempotency, or human gates before sends.

This skill is the n8n implementation anchor: **which flows to build** by GTM
motion, **how to build them** node-by-node, and **how MCP fits** (agents
draft/research; n8n executes with guardrails). Load `n8n-automation` for
when to choose n8n vs Clay; load `mcp-setup` for agent-side MCP config.

## When to Use

- "Build an n8n workflow for inbound leads"
- "n8n outbound enrichment pipeline"
- "Connect MCP to n8n" / "n8n orchestrate MCP tools"
- "Signal workflow — funding, job change, hiring"
- "CRM sync between HubSpot and Salesforce"
- "Replace Clay export with n8n for complex routing"
- "n8n reply classification webhook"
- "Event-driven GTM automation"

**Use Clay instead** (`clay-toolkit`, `clay-loops-toolkit`): spreadsheet
enrichment, waterfall columns, recurring signal monitors with credit control.

**Use MCP agents instead** (`mcp-setup`, `leadmagic-mcp`): ad-hoc research,
drafting, CRM reads — with human confirmation on writes.

**Use n8n when:** deterministic pipelines, SLA-bound inbound, bulk batch
jobs, multi-system sync, or branching that exceeds Clay formulas.

## Authoritative Foundations

- **n8n.** Visual iPaaS with 400+ nodes, self-host or cloud. Queue mode for
  pause/resume. Sub-workflows for reusable modules. Error Trigger workflows
  for global failure handling.
- **Model Context Protocol (MCP).** Standardizes agent tool discovery. n8n
  sits **below** agents as execution plane — agents call n8n webhooks to run
  approved pipelines; n8n does not replace MCP for interactive research.
- **iPaaS Integration Patterns.** Webhook (real-time), poll/cron (batch),
  idempotency keys (dedupe), dead-letter queue (failed records), circuit breaker
  (stop on API outage).
- **Winning by Design Bowtie.** Inbound flows must hand off Marketing → Sales
  with SPICED fields; closed-won → CS with health score. n8n enforces field
  requirements at routing gates.
- **ColdIQ Signal-to-Action.** One signal → one play. n8n Switch node routes
  by `signal_type`; never one generic "signal outreach" branch.

## n8n vs Clay vs MCP — Decision Matrix

| Need | Tool | Why |
|---|---|---|
| Waterfall email enrichment on a list | Clay | Column-native, credit-efficient |
| Recurring funding/job-change monitor | Clay Loops | Built-in cadence + table UX |
| Inbound form → enrich → route in <60s | n8n | Webhook SLA, branching |
| HubSpot ↔ Salesforce bidirectional sync | n8n | Custom field mapping, conflict rules |
| Reply webhook → classify → CRM task | n8n | Sequencer webhooks + AI node |
| Agent researches 5 accounts interactively | MCP | Tool calls with human in loop |
| Agent triggers approved bulk enrich job | MCP → n8n webhook | Agent proposes; n8n executes |
| Complex if/else across 6+ systems | n8n | Switch, Merge, sub-workflows |

## Step-by-Step: How to Build a GTM Flow

### Phase 1: Flow Selection

Pick blueprint from `references/gtm-flow-catalog.md`:

| Motion | Flow ID | Trigger | Latency Target |
|---|---|---|---|
| Inbound | `INB-01` Form → enrich → score → route | Webhook | <60s |
| Inbound | `INB-02` Inbound triage + Slack | Webhook | <30s |
| Outbound | `OUT-01` List upload → batch enrich → CRM | Manual/Cron | 2–4h / 5K rows |
| Outbound | `OUT-02` Clay webhook → sequencer | Webhook | <2min |
| Signal | `SIG-01` Funding → enrich → task | Cron daily | Same day |
| Signal | `SIG-02` Job change → champion play | Cron daily | Same day |
| Lifecycle | `LIF-01` Meeting held → nurture branch | CRM webhook | <5min |
| Lifecycle | `LIF-02` Trial signup → onboarding | Webhook | <2min |
| RevOps | `REV-01` CRM hygiene re-verify | Weekly cron | Batch |
| RevOps | `REV-02` Forecast rollup → Slack | Cron | Weekly |
| Agent | `MCP-01` MCP-approved pipeline trigger | Webhook | On demand |

### Phase 2: Architecture (5-Layer Stack)

Every production flow uses this stack:

```
TRIGGER → NORMALIZE → ENRICH/SCORE → ROUTE → ACTION + LOG
              ↓              ↓            ↓
         idempotency    rate limit    human gate (if send)
```

**Layer rules:**
1. **Trigger:** Webhook, Cron, CRM trigger, or another workflow. Always capture
   `event_id` for dedupe.
2. **Normalize:** Set node — map to canonical schema (`email`, `domain`,
   `company`, `source`, `signal_type`, `icp_tier`).
3. **Enrich/Score:** HTTP Request (LeadMagic, Clay API), Code node (ICP score),
   or AI node (classify reply). See `references/node-patterns.md`.
4. **Route:** Switch on `icp_score`, `signal_type`, `intent`, `geo`.
5. **Action:** CRM upsert, sequencer enroll, Slack, task create. **Never auto-send
   cold email without human gate** unless pre-approved tier-1 signal play.

### Phase 3: Node Implementation

Standard node order — full configs in `references/node-patterns.md`:

```
Webhook → Set (normalize) → IF (idempotency check in Redis/Sheet)
  → HTTP Request (enrich) → Code (score) → Switch (route)
    → HubSpot Upsert → Slack → Respond to Webhook
```

**Required on every production workflow:**
- Error Trigger workflow (global) → Slack + log row
- `Wait` node between API calls (100–500ms) for rate limits
- `Split In Batches` (size 10–50) for bulk
- Credentials in n8n store — never in exported JSON
- Workflow name: `[PROD] INB-01 Form Enrich Route`

### Phase 4: MCP Integration

Three patterns — detail in `references/mcp-patterns.md`:

**Pattern A — Agent triggers n8n (recommended)**
```
Jesse/Claude agent (MCP: CRM read, enrichment lookup)
  → Human approves "run enrichment job"
  → HTTP POST to n8n webhook (MCP-01)
  → n8n executes batch pipeline with audit log
```

**Pattern B — n8n calls external APIs (not MCP directly)**
```
n8n HTTP Request → LeadMagic / HubSpot / Clay API
(MCP is for agents; n8n uses REST natively)
```

**Pattern C — n8n AI Agent node + MCP-style tools**
```
n8n LangChain Agent node with Tool Workflow nodes
  → Sub-workflow per tool (enrich, CRM read, classify)
  → Use for reply classification (LIF-03) with bounded tools
```

Load `mcp-setup` for agent-side guardrails. n8n webhook auth: HMAC header
or secret query param — never expose unauthenticated production webhooks.

### Phase 5: Test and Deploy

1. **Test mode:** Pin test data; run node-by-node execution
2. **Dry run:** Set CRM nodes to read-only branch first
3. **Canary:** Route 5% traffic via Switch before full cutover
4. **Activate:** Tag `[PROD]`; enable Error Trigger workflow
5. **Monitor:** First 24h — Slack on every error + daily execution count

Run `scripts/check-output.py` on deliverable before handoff.

## GTM Flow Quick Reference

Full node lists in `references/gtm-flow-catalog.md`.

### Inbound (`INB-01`)

```
Form webhook (HubSpot/Typeform/Cal.com)
  → Normalize fields
  → LeadMagic: verify email
  → IF invalid → Slack #bad-leads + stop
  → LeadMagic: company enrich
  → Code: ICP score (0–100)
  → Switch:
      ≥70 → Create CRM contact + assign round-robin + Slack #hot-leads
      40–69 → Nurture list + marketing tag
      <40 → Archive + reason code
  → Respond 200 (form UX)
```

Align fields with `inbound-triage` and SPICED-lite on CRM create.

### Outbound (`OUT-01`)

```
Cron weekly OR manual webhook (list_id)
  → Google Sheets / Airtable: get rows where status=queued
  → Split In Batches (25)
    → LeadMagic find email → verify
    → IF verified → HubSpot upsert + status=enriched
    → IF not found → status=manual_review
  → On batch complete → Slack summary
```

Hand off to sequencer via `OUT-02` (Clay or n8n webhook to Smartlead).

### Signal (`SIG-01` Funding)

```
Cron daily 6am
  → Source: CRM watchlist OR funding API / Clay export webhook
  → Filter: funding in last 7 days + ICP tier 1–2
  → Enrich contacts at account
  → Set signal_type=funding, why_now, source_url
  → CRM: create task for owner + tag signal:funding
  → Slack: #signals with account link
```

Route copy from `funding-signal-play` — not generic outreach in n8n.

### Reply handling (`LIF-03`)

```
Sequencer reply webhook (Instantly/Smartlead/Outreach)
  → AI node OR HTTP to classification API (ai-prompts-toolkit P08)
  → Switch: positive / objection / OOO / unsubscribe / wrong person
  → positive → CRM task + Slack AE
  → unsubscribe → CRM opt-out + suppression list
  → wrong person → referral extract → new contact create
```

Maps to `reply-handling` categories exactly.

### MCP trigger (`MCP-01`)

```
Webhook POST { job_type, params, requested_by, approval_token }
  → IF valid HMAC + approval_token → route job_type
  → enrich_batch | sync_crm | classify_replies
  → Execute sub-workflow
  → Log to Sheet: timestamp, job_type, rows, status
  → Callback URL optional
```

## Sub-Workflow Library

Extract reusable modules:

| Sub-workflow | Input | Output |
|---|---|---|
| `sw-enrich-contact` | email or domain | verified_email, company, title |
| `sw-icp-score` | company fields | score 0–100, tier |
| `sw-crm-upsert-contact` | contact object | crm_id, created/updated |
| `sw-slack-notify` | channel, message | ok |
| `sw-idempotency-check` | event_id | skip or continue |

Call via **Execute Workflow** node — keeps main flows readable.

## Environment and Credentials

```bash
# Self-hosted n8n .env — never commit
N8N_ENCRYPTION_KEY=...
LEADMAGIC_API_KEY=lm_xxx
HUBSPOT_ACCESS_TOKEN=pat-xxx
SLACK_WEBHOOK_URL=https://hooks.slack.com/...
N8N_WEBHOOK_HMAC_SECRET=whsec_xxx
```

Credential types: Header Auth (API keys), OAuth2 (HubSpot/SF), Predefined
(Slack). Rotate keys quarterly; re-link credentials after rotation.

## Output Format

Deliverable package:

1. **Workflow blueprint** (`templates/workflow-blueprint.md`) — flow ID, trigger,
   node diagram, field schema, routing rules
2. **Node configuration** — HTTP endpoints, auth, body, response mapping
3. **MCP integration note** — if agents trigger this flow (Pattern A/C)
4. **Error handling** — Error Trigger workflow, retry policy, dead-letter
5. **Deployment checklist** — 8-point pre-activation (see Quality Check)

## Quality Check

- [ ] Flow ID assigned from catalog (INB/OUT/SIG/LIF/REV/MCP)
- [ ] Canonical schema on Normalize step (email, domain, source, event_id)
- [ ] Idempotency check before CRM writes
- [ ] Rate limiting between API nodes (100–500ms Wait)
- [ ] Human gate before any cold outbound send
- [ ] Error Trigger workflow linked; failures notify Slack
- [ ] Credentials in store — not in export JSON
- [ ] Webhook authenticated (HMAC or secret)
- [ ] Signal flows map to one play (`funding-signal-play`, etc.)
- [ ] Inbound captures SPICED-lite fields for CRM
- [ ] Batch flows use Split In Batches with size ≤50
- [ ] Workflow named `[PROD] {FLOW-ID} {description}`

## Common Pitfalls

1. **n8n as spreadsheet.** Rebuilding Clay waterfalls row-by-row in n8n costs
   more to maintain. Fix: Clay enriches; n8n routes and syncs.

2. **Unauthenticated webhooks.** Public URL gets spammed; CRM fills with junk.
   Fix: HMAC verification node first step.

3. **No idempotency.** Form double-submit creates duplicate contacts.
   Fix: `event_id` or email hash check in Redis/Sheet before create.

4. **Agent auto-sends via n8n.** Compliance and brand risk. Fix: MCP-01 requires
   `approval_token`; sends stay in sequencer with human review.

5. **One giant workflow.** 40 nodes, unmaintainable. Fix: sub-workflows per
   enrich, CRM, notify.

6. **Silent failures.** Error branch empty. Fix: global Error Trigger + row log.

7. **Mixed signal routing.** One branch for all signals. Fix: Switch on
   `signal_type`; load play skill per type.

## Execution Artifacts

- `references/framework-notes.md` — Framework anchors
- `templates/output-template.md` — Deliverable structure
- `scripts/check-output.py` — Validates workflow deliverables
- `references/gtm-flow-catalog.md` — Full flow blueprints by motion
- `references/mcp-patterns.md` — MCP + n8n integration patterns
- `references/node-patterns.md` — HTTP, webhook, batch, AI, error nodes
- `templates/workflow-blueprint.md` — Design doc template

## Related Skills

- `n8n-automation` — When to use n8n vs Clay (decision layer)
- `mcp-setup` / `leadmagic-mcp` — Agent-side MCP configuration
- `clay-toolkit` / `clay-loops-toolkit` — Enrichment and signal loops
- `ai-prompts-toolkit` — Prompts for AI nodes (classify, research)
- `crm-toolkit` / `crm-integration` — CRM field requirements
- `inbound-triage` — Inbound scoring rules
- `reply-handling` — Reply category → action mapping
- `proactive-alerts` — Slack alert formatting
- `event-analytics` — Track flow executions as events

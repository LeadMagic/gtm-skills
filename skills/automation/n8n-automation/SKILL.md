---
name: n8n-automation
description: >-
  Build n8n workflows for GTM automation — triggers, webhook-to-enrichment-to-CRM
  pipelines, error handling, Clay export replacement for complex cases. Use when
  building n8n workflows or automating GTM processes beyond Clay.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [n8n, automation, workflows, pipelines]
  frameworks:
    - "Jen Igartua (Go Nimbly) — RevOps automation maturity and orchestration roadmap"
    - "n8n Workflow Automation Framework"
    - "iPaaS Integration Patterns"
    - "HubSpot Academy — CRM Automation"
  related_skills: [n8n-toolkit, clay-automation, mcp-setup, api-enrichment, crm-integration]
---

# n8n Automation

## Overview

Clay handles enrichment workflows well. n8n handles everything else — custom
pipelines, multi-step automation with proper error handling and retry logic,
and integrations Clay does not support. Use n8n when you need a queue you can
pause, error recovery that does not lose data, and integrations across tools
that Clay cannot reach.

**Implementation detail:** Load `n8n-toolkit` for flow blueprints (inbound,
outbound, signals, MCP triggers), node patterns, and production deployment.
This skill covers *when* to use n8n; the toolkit covers *how* to build.

**Playbook index:** `references/automation-playbook-index.md` — all 38 automation + tool + gtm-ops playbooks.

**Strategy first:** `references/gtm-automation-expert-playbook.md` (Jen Igartua — Pattern 30) before flow build.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **n8n Workflow Automation Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **iPaaS Integration Patterns.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **HubSpot Academy — CRM Automation.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use

- "Build an n8n workflow for GTM"
- "Automate enrichment beyond Clay"
- "Create a custom GTM automation pipeline"
- "Connect tools that Clay does not support"

## Step-by-Step Process

### Phase 1: Workflow Design

Map the complete pipeline:

```
Trigger → Enrichment → Scoring → Routing → CRM Push → Notification
```

### Phase 2: Implementation Patterns

- **HTTP Request nodes** for enrichment API calls
- **Error handling**: retry with exponential backoff (3 attempts, 1s/5s/25s)
- **Split In Batches node** for processing large lists
- **Queue mode**: pause and resume when something looks wrong
- **Webhook triggers** for real-time form-fill processing

### Phase 3: Common GTM Workflows

Full node-level specs in `n8n-toolkit` → `references/gtm-flow-catalog.md`:

| Flow ID | Motion | Summary |
|---|---|---|
| INB-01 | Inbound | Form → enrich → score → route (<60s) |
| OUT-01 | Outbound | Batch enrich → CRM (5K in 2–4h) |
| OUT-02 | Outbound | Clay/n8n → sequencer (human gate) |
| SIG-01–04 | Signal | Funding, job change, hiring, stale opp |
| LIF-03 | Lifecycle | Reply webhook → classify → route |
| MCP-01 | Agent | Approved batch jobs via webhook |

**n8n vs Clay vs MCP:** See decision matrix in `n8n-toolkit`. Agents (MCP)
research and draft; n8n executes deterministic pipelines.

## Output Format

n8n workflow JSON export with node documentation, error handling rules, and
maintenance guide.


## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls

1. **No error handling.** One failed API call breaks the entire pipeline.
   Every HTTP Request node needs an error branch.

2. **Sequential processing for large batches.** 10K records at 1 second
   each is 2.8 hours. Use Split In Batches with parallel execution.

3. **No queue.** Processing 10K records without a pause mechanism means
   no recovery point if something fails at record 5,000.

4. **Credentials in workflow.** Use built-in credential store, never
   hardcode API keys in nodes.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/gtm-automation-expert-playbook.md` — Jen Igartua RevOps automation strategy (repo root; Pattern 30)
- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Implementation Depth

Use this section when the user asks for a finished asset, not a high-level explanation.

### Diagnostic Questions

1. What is the primary motion: founder-led, sales-led, product-led, partner-led, or lifecycle-led?
2. Which ICP tier is the output for: small business, mid-market, enterprise, or mixed?
3. What proof is available today: customer stories, usage data, third-party validation, screenshots, or none?
4. What system will execute the work: CRM, sequencer, warehouse, support desk, product analytics, or manual workflow?
5. What decision will the user make from this output: launch, prioritize, route, rewrite, score, coach, or measure?

### Framework Application

Map the recommendation explicitly to the named frameworks in this skill:

- n8n Workflow Automation Framework: apply only the part that directly improves the requested deliverable.
- iPaaS Integration Patterns: apply only the part that directly improves the requested deliverable.
- HubSpot Academy — CRM Automation: apply only the part that directly improves the requested deliverable.

### Deliverable Standard

A strong output from this skill includes:

- A crisp diagnosis of the current situation
- A recommended path with tradeoffs, not a generic list
- A concrete artifact the user can use immediately: table, script, checklist, scorecard, sequence, dashboard spec, or implementation plan
- A measurement plan with leading and lagging indicators
- Risks and edge cases called out before execution

### Adaptation Rules

- For small business: reduce complexity, shorten time-to-value, and prioritize owner/operator clarity.
- For mid-market: include workflow ownership, handoffs, integrations, and enablement assets.
- For enterprise: include governance, risk, procurement, stakeholder mapping, and proof requirements.


## Related Skills

- **n8n-toolkit**: Flow catalog, MCP patterns, node configs (primary implementation)
- **mcp-setup**: Agent-side MCP; pairs with MCP-01 n8n webhook
- **clay-automation**: Clay workflows for enrichment
- **api-enrichment**: API enrichment patterns
- **crm-integration**: CRM configuration for receiving n8n data
- **gtm-role-descriptions**: GTM Engineer hiring — n8n listed in JD and scorecard

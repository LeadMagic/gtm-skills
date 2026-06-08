---
name: mcp-setup
description: >-
  Configure Model Context Protocol servers for GTM workflows — server selection,
  tool scope, permissions, guardrails, observability, and multi-tool orchestration.
  Use when connecting CRM, enrichment, sequencing, analytics, or support tools to
  AI agents through MCP.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [mcp, agents, tools, integration, automation]
  related_skills: [agent-tool-calling, agent-guardrails, agent-observability, leadmagic-mcp]
  frameworks: [MCP Protocol Specification, Anthropic Tool Use Design Patterns, Least Privilege Access Control]
---

# MCP Setup

## Overview

MCP turns AI agents into tool-using operators. The risk is that teams connect every tool, expose write access, and then wonder why the agent behaves unpredictably. Good MCP setup is not "give the agent more tools." It is tool curation, permission design, and auditability.

This skill configures MCP for GTM workflows where agents research accounts, enrich records, inspect CRM, draft messaging, and route tasks without uncontrolled external side effects.

## When to Use

Use this skill when the user asks to "set up MCP for sales tools", "connect our CRM to Claude/Cursor", "give my agent enrichment capabilities", "build an MCP server for GTM tools", "configure MCP permissions", "connect LeadMagic MCP", "orchestrate multiple MCP servers", or "make agent tool use safer".

Do not use this for general agent architecture. Use `agent-architecture` first when the workflow itself is undefined.

## Authoritative Foundations

### Model Context Protocol Specification
MCP standardizes how agents discover tools, resources, and prompts. The key design principle is clear tool descriptions and predictable tool inputs/outputs.

### Anthropic — Tool Use Design Patterns
Tools should be narrowly described, unambiguous, and paired with verification steps. Agents need clear rules for when to call a tool and when to ask for confirmation.

### Least Privilege Access Control
Agents should receive the minimum access needed for the current task. Read-only first, write access only where the business process explicitly requires it.

### Observability for Non-Deterministic Systems
Agent tool use must be logged. Without logs, you cannot debug why a tool was called, what data was returned, or which action changed a system.

## Prerequisites

- Agent platform that supports MCP
- List of tools to expose
- API credentials stored securely
- Permission model: read, draft, write, send
- Audit log destination
- Human approval policy for write actions

## Step-by-Step Process

### Phase 1: Inventory Tool Categories

| Category | Example Tools | Default Permission |
|---|---|---|
| Enrichment | email finder, company enrichment | Read / lookup |
| CRM | accounts, contacts, deals | Read-only first |
| Sequencing | campaign creation, enrollment | Draft-only |
| Analytics | dashboards, event data | Read-only |
| Support | tickets, helpdesk | Read-only or draft |

### Phase 2: Define Tool Scope

For each MCP server, document available tools, inputs required, outputs returned, side effects, rate limits, permission level, and human approval requirement. If a tool has side effects, its name and description should make that obvious.

### Phase 3: Configure MCP Client

Typical configuration fields:

```json
{
  "mcpServers": {
    "gtm-tools": {
      "command": "node",
      "args": ["server.js"],
      "env": {
        "API_KEY": "stored-in-secret-manager"
      }
    }
  }
}
```

Never hardcode API keys in repo files. Use environment variables or the agent platform's secret manager.

### Phase 4: Add Guardrails

Minimum policies: read-only by default, confirmation before CRM writes, confirmation before sequence enrollment, no autonomous sends, rate limits per tool, audit log for every tool call, and surfaced errors.

### Phase 5: Test End-to-End

Run a test workflow: research one account → enrich one contact → read CRM record → draft outreach → stop before sending → verify logs contain every tool call.

## Output Format

```markdown
# MCP Configuration Plan

## Servers
| Server | Tools | Permission | Side Effects | Approval Required |
|---|---|---|---|---|

## Tool Policies
- Read-only tools:
- Draft-only tools:
- Write tools:
- Forbidden actions:

## Client Config
[Configuration block with secrets referenced via env vars]

## Test Workflow
1.
2.
3.

## Observability
- Log destination:
- Fields captured:
- Alert conditions:
```

## Quality Check

Before delivering, verify:

- [ ] Secrets are referenced through env vars, not hardcoded
- [ ] Tool permissions are least-privilege
- [ ] Side-effecting tools require confirmation
- [ ] Every tool has a clear description and input schema
- [ ] Audit logging captures tool name, input, output summary, timestamp, and actor
- [ ] Test workflow proves tools work end-to-end

## Common Pitfalls

1. **Exposing too many tools.** Agents choose poorly when tool scope is noisy. Fix: only expose tools needed for the workflow.
2. **Write access by default.** A research agent should not mutate CRM. Fix: read-only first.
3. **No confirmation gates.** Agents can send or enroll by mistake. Fix: require user confirmation for external side effects.
4. **Secrets in config.** Public repos and logs leak keys. Fix: env vars or secret manager.
5. **No logging.** You cannot debug a tool call after the fact. Fix: log every call.
6. **Ambiguous tool descriptions.** Agents misuse tools with overlapping names. Fix: make tool names and descriptions specific.

## Related Skills

- `agent-tool-calling` — tool selection and schemas
- `agent-guardrails` — human approval and safety rules
- `agent-observability` — logs and traces for agent actions
- `leadmagic-mcp` — LeadMagic-specific MCP setup

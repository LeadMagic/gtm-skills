---
name: mcp-setup
description: >-
  Configure Model Context Protocol servers for GTM tools — multi-MCP architecture, tool orchestration, provider-neutral patterns. Use when setting up MCP servers for sales tools, connecting enrichment providers to AI agents, or building agent-accessible GTM tooling. Triggers on: "MCP", "Model Context Protocol", "MCP server", "connect tools to agent", "agent tools", or any MCP configuration request.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [mcp, agents, tools, integration]
  frameworks: [MCP Protocol Specification, Anthropic Tool Use Design Patterns]
---
# MCP Setup

## Overview
MCP (Model Context Protocol) lets AI agents call GTM tools directly — enrichment, CRM operations, sequencing, and research — without human intermediation. A well-configured MCP setup turns any agent into a GTM operator.

## When to Use
- "Set up MCP for our sales tools"
- "Connect our CRM to Claude via MCP"
- "Give my agent access to enrichment data"
- "Build an MCP server for our GTM stack"

## Step-by-Step Process
### Phase 1: Inventory GTM Tools
List every tool the agent should access: enrichment (LeadMagic MCP, Apollo API), CRM (HubSpot/Salesforce MCP), sequencing (Smartlead/Instantly API), research (web search, LinkedIn data).

### Phase 2: MCP Server Configuration
Configure each MCP server in your agent's mcp.json. Example Claude Code config for multi-MCP.

### Phase 3: Tool Orchestration
Design the agent's workflow: research account → enrich contacts → score against ICP → draft outreach → push to sequencer. Each step is an MCP tool call.

### Phase 4: Guardrails
- Read-only for CRM data by default
- Confirmation gates before any send/push operation
- Rate limiting per tool

## Common Pitfalls
1. **Too many tools.** An agent with 50 tools can't decide what to use. Curate.
2. **No confirmation gates.** Agent sending email without human review = risk.
3. **Single MCP server.** Different providers need different MCP servers.
## Output Format

The agent should produce a structured deliverable:

```markdown
# [Deliverable Title]

## Summary
[1-2 sentence summary of what was produced]

## Key Outputs
- [Output item 1]
- [Output item 2]
- [Output item 3]
```

## Quality Check

Before delivering, verify:
- [ ] All required sections complete
- [ ] Output matches the user's stated need
- [ ] No vague or unsupported claims
- [ ] Frameworks cited where applicable

## Common Pitfalls

1. **Incomplete output.** The deliverable is missing critical sections. Fix: verify against the output template before delivering.
2. **Generic advice without specifics.** "Improve your process" without concrete steps. Fix: every recommendation must have a specific action.
3. **Missing framework citations.** Advice without named authorities. Fix: cite the specific framework that grounds each recommendation.

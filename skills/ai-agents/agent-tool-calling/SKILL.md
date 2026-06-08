---
name: agent-tool-calling
description: >-
  Design agent tool-calling strategies — MCP servers, API integration, function
  calling, tool selection logic. Triggers on: "agent tools", "MCP server", "tool
  calling", "function calling", "agent API integration".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: ai-agents
  tags: [ai-agents, tool-calling, MCP, function-calling, API]
  frameworks:
    - "MCP Protocol"
    - "Anthropic Tool Use Best Practices"
    - "Anthropic — Agent Skills Progressive Disclosure"
---

# Agent Tool Calling

## Overview
An agent without tools is a chatbot. An agent with tools is a GTM operator.
This skill covers tool selection, API wrapping, function calling design,
and MCP server architecture for GTM agents.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **MCP Protocol.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Anthropic Tool Use Best Practices.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Anthropic — Agent Skills Progressive Disclosure.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Give my agent access to [CRM/enrichment/etc]"
- "Build an MCP server for [tool]"
- "Agent tool-calling strategy"
- "Connect agent to our stack"

## Step-by-Step Process

### Phase 1: Tool Inventory
Map the tools your GTM agent needs:

**Data Access Tools:**
- CRM: Read contacts, accounts, opportunities; write activities, notes
- Enrichment: Find email, enrich company, verify contact
- LinkedIn: Sales Navigator search, profile data (via MCP)
- Web search: Company research, news, signals

**Communication Tools:**
- Email: Send, read, search (IMAP/SMTP or Gmail API)
- Calendar: Check availability, book meetings
- Sequencing: Add to cadence, remove from cadence

**Execution Tools:**
- CRM: Create tasks, update fields, change stages
- Slack: Send alerts, post summaries
- Database: Run queries, update records

**Analysis Tools:**
- SQL: Query data warehouse
- Spreadsheet: CSV processing, data transformation
- Visualization: Generate charts, build dashboards

### Phase 2: Tool Description Design
Every tool needs a clear description (this is what the agent reads to decide
whether to use the tool). Design principles:

- **Trigger-oriented:** "Use when the user asks to find an email address for a
  contact or verify an email."
- **Input specification:** "Requires: first_name (string), last_name (string),
  company_domain (string). Optional: linkedin_url."
- **Output specification:** "Returns: email (string), confidence_score (0-100),
  verification_status (valid/invalid/unknown/risky)."
- **Error handling:** "If email not found, returns empty result with suggestions
  for alternative methods."

### Phase 3: MCP Server Architecture
For tools that need persistent connections:
- **Server per domain:** CRM MCP server, enrichment MCP server, sequencing MCP server
  (not one monolithic server)
- **Authentication:** OAuth or API key stored in environment variables, never in
  code or prompts
- **Rate limiting:** Built into the MCP server, not left to the agent
- **Caching:** Cache read operations (get contact, get account) for 5-15 minutes
- **Logging:** Every tool call logged with timestamp, inputs, outputs, duration

### Phase 4: Tool Selection Logic
The agent's decision process for choosing tools:
1. Parse user intent: "find email" → enrichment tool, "update CRM" → CRM tool
2. Check prerequisites: do I have the required inputs? If not, ask or use another
   tool to get them
3. Call the tool
4. Validate the output: did it return what I expected?
5. If error: retry with modified inputs, or fall back to alternative tool
6. If success: use the output in the user-facing response

### Phase 5: Tool Composition
Complex workflows require chaining multiple tools:
- **Sequential:** Tool A output → Tool B input. "Find email → verify email →
  add to CRM."
- **Parallel:** Call Tool A and Tool B simultaneously. "Research company (web
  search) AND enrich data (API) at the same time."
- **Conditional:** If Tool A returns X, call Tool B. If Y, call Tool C.
  "If email found, verify. If not found, try alternative pattern."

## Output Format
Tool-calling strategy with: tool inventory, tool descriptions, MCP server
architecture, tool selection logic, and composition patterns.



## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls

1. **Agent without guardrails.** An unconstrained agent can send bad emails, exceed budgets, or damage brand reputation. Fix: every agent action that touches external systems must have human approval gates.
2. **Over-automating relationship work.** Agents are great for research and drafting, terrible for complex negotiation and relationship building. Fix: define clear human-in-the-loop boundaries.
3. **No observability.** Agents are non-deterministic — they make different decisions on the same input. Without logging and metrics, you're operating blind. Fix: log every tool call, decision, and output.

## Related Skills
- agent-architecture, mcp-setup, api-enrichment, crm-integration, agent-observability

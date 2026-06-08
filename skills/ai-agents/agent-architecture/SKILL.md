---
name: agent-architecture
description: >-
  Design AI agent architectures for GTM workflows — agent patterns, tool selection,
  multi-agent orchestration, human-in-the-loop. Triggers on: "agent architecture",
  "AI agent design", "agent patterns", "multi-agent", "agent workflow".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: ai-agents
  tags: [ai-agents, agent-architecture, multi-agent, orchestration, gtm-automation]
  frameworks:
    - "Anthropic Agent Design Patterns"
    - "ReAct Agent Framework"
    - "Anthropic — Agent Skills Progressive Disclosure"
---

# AI Agent Architecture for GTM

## Overview
AI agents are transforming GTM — not as replacements for humans, but as force
multipliers that handle research, drafting, routing, and analysis. This skill
covers agent design patterns, tool selection, multi-agent orchestration, and
human-in-the-loop design for GTM workflows.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Anthropic Agent Design Patterns.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **ReAct Agent Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Anthropic — Agent Skills Progressive Disclosure.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Design an AI agent for [GTM task]"
- "Agent architecture for sales"
- "Build a multi-agent GTM system"
- "AI agent for prospecting/enrichment/outreach"

## Step-by-Step Process

### Phase 1: Task Decomposition
Break GTM work into agent-compatible tasks:

**High-fit for agents (automate first):**
- Lead research and enrichment
- Data cleaning and normalization
- First-draft email/pitch creation
- Meeting research and briefing
- CRM data entry and hygiene
- Signal detection and alerting
- Campaign performance analysis
- Reply categorization and routing

**Low-fit for agents (keep human):**
- Complex negotiation
- Relationship building
- Strategic account planning
- Creative campaign strategy
- High-stakes executive communication

### Phase 2: Agent Pattern Selection
Choose the right pattern for the task:

- **Single-agent with tools:** One agent + API tools. Best for well-defined tasks
  (enrichment, research, analysis). Simple, predictable.
- **Router + specialists:** Router agent classifies task → dispatches to specialist
  agent (SDR agent, research agent, analytics agent). Best for multi-domain work.
- **Multi-agent collaboration:** Multiple agents work on the same task with
  specialized roles. Best for complex workflows (ABM campaign design).
- **Human-in-the-loop:** Agent drafts → human reviews → agent executes. Best for
  outbound communication where quality matters.

### Phase 3: Tool Selection
Tools agents need for GTM work:
- **Data:** CRM API, enrichment APIs, LinkedIn (Sales Nav), web search
- **Communication:** Email (SMTP/API), calendar, Slack
- **Analysis:** SQL, spreadsheet, visualization
- **Execution:** Sequencing platform API, CRM write, task creation

### Phase 4: Multi-Agent Orchestration
For complex GTM workflows, design the agent ecosystem:

**Example: Prospecting Agent System**
- **Signal Agent:** Monitors funding, hiring, product launches → scores accounts
- **Research Agent:** Enriches target accounts, builds briefs → outputs account dossiers
- **Drafting Agent:** Writes personalized outreach → outputs email drafts
- **SDR Agent:** Reviews drafts, sends approved emails, handles replies → routes
  positive replies to AEs
- **Analytics Agent:** Tracks performance, identifies patterns → recommends
  sequence optimizations

**Orchestration pattern:** Sequential pipeline with conditional branching.
Signal Agent → Research Agent → Drafting Agent → SDR Agent (human reviews)
→ Analytics Agent (feedback loop).

### Phase 5: Guardrails & Safety
- **Rate limiting:** Agents must not exceed API rate limits or send thresholds
- **Content filtering:** Drafts must pass tone/appropriateness checks
- **Human approval gates:** Outbound emails require human review before sending
- **Budget controls:** API calls capped at daily/monthly limits
- **Error handling:** Clear escalation paths when agents fail
- **Observability:** Logging, monitoring, alerting on agent actions

## Output Format
Agent architecture blueprint with: task decomposition, pattern selection,
tool inventory, orchestration diagram, and guardrail specification.



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
- agent-tool-calling, agent-observability, agent-guardrails, ai-sdr-setup, mcp-setup

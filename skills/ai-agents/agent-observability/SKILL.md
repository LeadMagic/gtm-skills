---
name: agent-observability
description: >-
  Monitor and debug AI agent performance — logging, metrics, alerting, cost tracking,
  error analysis. Triggers on: "agent monitoring", "agent observability", "agent
  analytics", "agent logging", "agent debug".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: ai-agents
  tags: [ai-agents, observability, monitoring, logging, analytics]
  frameworks:
    - "Agent Observability Framework"
    - "LLM Ops Best Practices"
    - "Anthropic — Agent Skills Progressive Disclosure"
---

# Agent Observability

## Overview
Agents are non-deterministic — they make different decisions on the same input,
they hallucinate, they exceed rate limits, they cost money. Without observability,
you're operating blind. This skill covers logging, metrics, alerting, and cost
tracking for GTM agents.

## Frameworks Referenced

This skill is grounded in named GTM frameworks and operator methodologies, not generic advice:

- **Agent Observability Framework** — used as the named operating framework for this playbook.
- **LLM Ops Best Practices** — used as the named operating framework for this playbook.

## When to Use
- "Monitor my agents"
- "Set up agent observability"
- "Track agent performance"
- "Agent cost analysis"
- "Debug agent behavior"

## Step-by-Step Process

### Phase 1: What to Log
Every agent action must be logged:

**Input layer:**
- Task description / user prompt
- Session context (account, opportunity, campaign)
- Timestamp

**Decision layer:**
- Which tool was called and why
- Tool inputs and outputs (sanitized — no PII in logs)
- Latency: time from tool call to response

**Output layer:**
- Agent's final response
- Decision path: what tools were called, in what order, with what results
- Human review decisions (approved, rejected, modified)

**Error layer:**
- Tool call failures (API error, timeout, rate limit)
- Hallucination detection (agent claimed to do something it didn't)
- Guardrail violations (agent tried to send without approval)

### Phase 2: Key Metrics
- **Success rate:** % of agent tasks that completed without errors
- **Human approval rate:** % of agent outputs approved by human reviewers
- **Time to completion:** End-to-end time from task assignment to completion
- **Cost per task:** API cost (LLM + tool calls) per completed task
- **Tool call efficiency:** Average tool calls per task (lower is better)
- **Error rate:** % of tasks with at least one error
- **Hallucination rate:** % of responses containing fabricated information

### Phase 3: Alerting Rules
- **Critical:** Agent sending >50 emails/hour without approval → auto-pause
- **Critical:** Agent making API calls to unauthorized endpoints → auto-block
- **High:** Agent error rate >10% in 1 hour → alert on-call
- **High:** Agent cost/day >$100 → alert budget owner
- **Medium:** Agent task queue >50 pending → scale up or alert
- **Medium:** Human approval rate <70% → agent needs retraining

### Phase 4: Cost Tracking
- **Per-agent cost:** Daily/weekly/monthly LLM cost + tool call cost
- **Per-task cost:** Average cost to complete one task (e.g., "research one account")
- **Cost per outcome:** Cost per meeting booked, cost per enriched contact,
  cost per campaign analyzed
- **ROI:** Revenue influenced by agent vs agent cost
- **Budget alerts:** Notify when approaching 80%, 90%, 100% of monthly budget

### Phase 5: Debugging Workflow
When an agent does something wrong:
1. **Reproduce:** Find the exact session where the error occurred
2. **Inspect:** Review the full decision trace — what tools were called, in what order
3. **Identify:** Pinpoint the failure point (wrong tool selection, bad input,
   hallucination, API error)
4. **Fix:** Update tool descriptions, add guardrails, improve prompting
5. **Test:** Run the same task with the fix and verify correct behavior
6. **Prevent:** Add a regression test or monitoring rule to catch recurrence

## Output Format
Observability blueprint with: logging specification, metrics dashboard design,
alerting rules, cost tracking model, and debugging workflow.



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
- agent-architecture, agent-tool-calling, agent-guardrails, campaign-analytics, proactive-alerts

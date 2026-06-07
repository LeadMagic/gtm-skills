---
name: agent-guardrails
description: >-
  Implement safety guardrails for GTM agents — content filtering, approval gates,
  rate limiting, budget controls, kill switches. Triggers on: "agent guardrails",
  "agent safety", "AI guardrails", "agent controls", "agent compliance".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: ai-agents
  tags: [ai-agents, guardrails, safety, compliance, controls]
  frameworks: [AI Safety Framework, Anthropic Constitutional AI Principles]
---

# Agent Guardrails

## Overview
An unconstrained GTM agent is a liability — it can send bad emails, exceed
budgets, violate compliance, and damage your brand. Guardrails are the safety
mechanisms that keep agents effective without letting them run wild.
This skill covers the full guardrail stack.

## When to Use
- "Add guardrails to my agents"
- "Agent safety controls"
- "Prevent agent from [bad behavior]"
- "Agent compliance rules"
- "Agent kill switch"

## Step-by-Step Process

### Phase 1: Content Guardrails
Before any agent-generated content reaches a human or external system:

**Tone & Appropriateness:**
- Must pass professionalism check: no profanity, no aggression, no manipulation
- Must pass brand voice check: consistent with brand guidelines
- Must pass factual accuracy check: no fabricated statistics, no made-up customer names

**Compliance:**
- Must include unsubscribe link in all marketing emails
- Must include required legal disclosures (CAN-SPAM, GDPR, CCPA)
- Must not make claims about competitors without evidence
- Must not promise results, guarantees, or specific outcomes

**Technical:**
- Must not include raw API keys, tokens, or passwords
- Must not include internal system architecture details
- Must not include customer PII in any public-facing content

### Phase 2: Approval Gates
Human-in-the-loop at key decision points:

- **Outbound emails:** Agent drafts → human reviews → human clicks send.
  No fully automated sending without approval.
- **CRM updates:** Agent can read CRM freely. Agent can write to CRM only for
  activity logging and task creation. Stage changes require human approval.
- **Sequence enrollment:** Agent can recommend sequence enrollment. Human must
  approve before contacts are enrolled.
- **High-value actions:** Any action affecting >$100 in spend, >50 contacts,
  or any customer-facing communication requires human approval.

### Phase 3: Rate Limiting & Budget Controls
- **API call limits:** Per-minute and per-day caps on each tool
- **Send limits:** Max emails per day per agent (typically 50-100)
- **Cost limits:** Max daily LLM spend per agent (typically $10-50)
- **Concurrency limits:** Max parallel tasks per agent (typically 3-5)
- **Time limits:** Max runtime per task (typically 5 minutes)

### Phase 4: Kill Switch Architecture
Three-layer kill switch:

**Layer 1 — Soft pause:**
- Agent detects anomaly (error rate spike, unusual output)
- Auto-pauses all actions
- Alerts human operator
- Resumes when human acknowledges

**Layer 2 — Hard stop:**
- Human operator triggers via dashboard or Slack command
- Agent immediately stops all actions
- All pending tasks cancelled
- Requires manual restart

**Layer 3 — Circuit breaker:**
- Automatic trigger on critical conditions:
  - Cost exceeds daily budget by 50%
  - Error rate exceeds 25% for 10+ minutes
  - Unauthorized API call detected
  - Send rate exceeds configured limit
- Immediate shutdown of all agent processes
- Cannot be overridden without code change

### Phase 5: Audit Trail
Every agent action must be auditable:
- Who configured the agent
- What task was assigned
- What tools were called
- What outputs were generated
- Who approved each action
- What was modified before execution
- All timestamps and durations

## Output Format
Guardrail specification with: content filtering rules, approval gate matrix,
rate limiting configuration, kill switch architecture, and audit trail design.

## Related Skills
- agent-architecture, agent-observability, agent-tool-calling, email-deliverability, gtm-operations

---
name: leadmagic-mcp
description: >-
  Set up LeadMagic MCP for AI agents — tool discovery, permission scope, safe
  enrichment workflows, batch usage, verification steps, and agent handoff patterns.
  Use when connecting LeadMagic data tools to Claude, Jesse, VS Code, or any MCP
  compatible client.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: leadmagic
  tags: [leadmagic, mcp, agents, tools, enrichment]
  related_skills: [mcp-setup, ai-sdr-setup, leadmagic-integrations]
  frameworks: [MCP Protocol Specification, Anthropic Tool Use Patterns, Agent-Enabled GTM]
---

# LeadMagic MCP

## Overview

LeadMagic MCP gives agents access to enrichment and GTM data tools inside the agent workflow. The value is speed: the agent can research, enrich, validate, and summarize without asking the user to switch tools. The risk is uncontrolled tool use.

This skill configures LeadMagic MCP as a blackbox GTM toolset. It describes safe usage patterns and outputs, not internal implementation.

## When to Use

Use this skill when the user asks to "set up LeadMagic MCP", "connect LeadMagic to Claude", "connect LeadMagic to Jesse", "give my agent enrichment tools", "use LeadMagic inside my AI agent", "configure LeadMagic tools via MCP", "build an agent workflow with enrichment", or "research accounts with LeadMagic MCP".

Use `mcp-setup` first if the user has not defined the broader MCP architecture.

## Authoritative Foundations

### Model Context Protocol Specification
MCP standardizes tool discovery and invocation. Good MCP design depends on narrow tool descriptions, predictable input schemas, and clear output formats.

### Anthropic — Tool Use Patterns
Agents use tools best when each tool has a specific job, the agent has a verification step, and side-effecting operations require confirmation.

### Agent-Enabled GTM
In GTM workflows, agents should use tools to gather and verify data, then produce drafts or recommendations. External actions like sending email or mutating CRM should stay gated.

## Available Tool Categories

LeadMagic MCP can support workflows around email finding, email validation, company enrichment, people/contact search, job-change detection, technographic research, funding/company signal lookup, and account intelligence.

Treat each tool category as a capability with its own quality check. For example: found emails must still carry a status before outbound use.

## Step-by-Step Process

### Phase 1: Define Agent Jobs

| Agent Job | Needed Tool Category | External Side Effect? |
|---|---|---|
| Research target account | Company enrichment | No |
| Find contacts | People/contact search | No |
| Validate found emails | Email validation | No |
| Build account brief | Company + people data | No |
| Push to CRM | Integration tool | Yes — require confirmation |
| Enroll sequence | Sequencer tool | Yes — require confirmation |

### Phase 2: Configure MCP Client

Use the client-supported MCP config format. API keys should come from environment variables or the client's secret store, never from committed config files.

Document server name, environment variables required, tool categories enabled, disabled tools, and confirmation gates.

### Phase 3: Define Agent Tool Rules

1. Call enrichment tools only when required to complete the user request.
2. Prefer batch calls when processing lists.
3. Verify email status before recommending outbound use.
4. Do not infer missing facts if a tool returns no result.
5. Ask for confirmation before writing to CRM or enrolling contacts.

### Phase 4: Test Representative Workflows

Test at least three workflows: single account brief, contact enrichment for one account, and job-change signal summary. Each test should confirm the agent selected the right tool and interpreted the result correctly.

## Output Format

```markdown
# LeadMagic MCP Setup

## MCP Client
- Client:
- Server name:
- Required env vars:

## Enabled Tool Categories
| Category | Use Case | Guardrail |
|---|---|---|

## Agent Rules
- Lookup rules:
- Verification rules:
- Confirmation gates:

## Test Workflows
| Workflow | Expected Tool Category | Expected Output |
|---|---|---|
```

## Quality Check

Before delivering, verify:

- [ ] No API key is committed or shown in plaintext
- [ ] Enabled tool categories match the user workflow
- [ ] Agent rules distinguish lookup from external side effects
- [ ] Email-related workflows include validation/status handling
- [ ] Batch use is recommended for lists
- [ ] Test workflows cover account, contact, and signal use cases

## Common Pitfalls

1. **Treating MCP as magic.** Tools still need clear jobs. Fix: map tools to workflows.
2. **Too many calls.** Per-record calls waste time and credits. Fix: batch where supported.
3. **Skipping status interpretation.** Found data is not automatically usable. Fix: check status and confidence fields.
4. **Hardcoding secrets.** Config files leak. Fix: environment variables or secret manager.
5. **No confirmation gates.** Agent may mutate systems. Fix: require confirmation for writes and sends.
6. **Inventing missing data.** Empty result means unknown, not permission to guess. Fix: return unknown or ask for more input.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — MCP tool boundaries, Pat data-before-action, n8n MCP-01 handoff
- `references/agent-tool-guardrails.md` — confirmation gates, batch discipline, test matrix
- `../../tools/n8n-toolkit/references/mcp-patterns.md` — approved batch jobs via n8n
- `../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md` — verify status in agent outputs (Pat Spielmann)
- `../../../../references/gtm-experts-outbound-index.md` — expert router
- `templates/output-template.md` — MCP client config + agent rules deliverable
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- `mcp-setup` — broader MCP architecture and permission design
- `ai-sdr-setup` — guardrails, pilot scope, and human handoff for agent workflows
- `leadmagic-integrations` — non-MCP integration paths

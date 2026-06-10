# LeadMagic MCP Setup Deliverable

## Context
- MCP client (Claude/Cursor/other):
- Agent jobs:
- Batch size expected:

## Framework Basis
- MCP Protocol + Anthropic tool use
- Pat Spielmann — cite verify status in agent outputs

## Enabled Tool Categories
| Category | Use Case | Confirmation Required |
|---|---|---|
| Email find |  | No |
| Email validate |  | No |
| CRM write |  | Yes |

Guardrails: `references/agent-tool-guardrails.md`

## Agent Rules
- Lookup rules:
- Verification rules:
- Confirmation gates:
- Batch redirect (>100 rows → n8n MCP-01):

## Test Workflows
| Workflow | Expected Tool | Pass? |
|---|---|---|
| Single account brief |  |  |
| Email validate |  |  |
| CRM push request | asks confirm |  |

## Quality Check
- [ ] No API key in config files
- [ ] Side-effect tools gated
- [ ] n8n handoff documented for batch

# LeadMagic MCP — Framework Notes

**Category:** `leadmagic` · Agent tool layer for enrichment lookups.

## Primary Frameworks

- **MCP Protocol Specification** — Tool discovery, schemas, invocation
- **Anthropic Tool Use Patterns** — Narrow tools, confirmation gates, batch discipline
- **Pat Spielmann — Data before action** — Agent must cite verify status before recommending send → `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

## Tool Boundaries

| Layer | Skill | Role |
|---|---|---|
| MCP config | leadmagic-mcp (this) | Agent tool rules |
| Architecture | mcp-setup | Server design |
| Batch execution | n8n-toolkit MCP-01 | Approved jobs at scale |
| CLI alternative | leadmagic-cli | Terminal batch (no agent loop) |

## Guardrails

Load `references/agent-tool-guardrails.md` — confirmation required for CRM write and sequencer enroll.

## Agent Jobs vs Side Effects

| Job | Side Effect? | Gate |
|---|---|---|
| Find / validate / enrich | No | Status in output |
| CRM upsert | Yes | User confirm |
| Sequencer enroll | Yes | User confirm |
| Batch >100 rows | Prefer n8n | Redirect to MCP-01 |

## Agent Use

1. Map agent jobs to tool categories.
2. Load agent-tool-guardrails for deliverable.
3. Recommend n8n for batch; MCP for research samples.
4. Never commit API keys.
5. Run `check-output.py`.

Expert router → `references/gtm-experts-outbound-index.md`

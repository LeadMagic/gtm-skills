# n8n + MCP Integration Patterns

MCP connects **agents** to tools. n8n connects **systems** on schedules and
webhooks. They complement each other — not substitutes.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│  Agent Layer (Jesse, Claude, Codex)                    │
│  MCP: CRM read, enrichment lookup, draft email          │
│  Guardrails: read-only default, confirm writes          │
└───────────────────────┬─────────────────────────────────┘
                        │ HTTP webhook (approved jobs only)
                        ▼
┌─────────────────────────────────────────────────────────┐
│  n8n Execution Layer                                    │
│  Batch enrich, inbound routing, reply classify, sync    │
│  Deterministic, logged, rate-limited, idempotent         │
└───────────────────────┬─────────────────────────────────┘
                        │ REST APIs
                        ▼
┌─────────────────────────────────────────────────────────┐
│  GTM Systems: CRM, sequencer, enrichment, Slack, MAP    │
└─────────────────────────────────────────────────────────┘
```

Load `mcp-setup` for agent configuration. This doc covers n8n's role.

---

## Pattern A — Agent Triggers n8n (Recommended)

**When:** User asks agent to "enrich this list" or "sync CRM" — job is
batch, repeatable, and should not burn agent tokens row-by-row.

**Flow:**
1. Agent uses MCP to **read** list scope (CRM segment, Sheet name)
2. Agent proposes job summary; user confirms
3. Agent POSTs to n8n webhook `MCP-01` with `approval_token`
4. n8n runs `OUT-01` or `REV-01`; logs results
5. Agent uses MCP to **read** updated CRM state

**Webhook contract:**

```http
POST https://n8n.example.com/webhook/mcp-job-runner
X-N8N-HMAC-SHA256: <signature>
Content-Type: application/json

{
  "job_type": "enrich_batch",
  "params": {
    "source": "airtable",
    "base_id": "appXXX",
    "table": "leads",
    "filter": "status=queued",
    "limit": 200
  },
  "requested_by": "jesse@company.com",
  "approval_token": "<one-time-from-approval-service>",
  "callback_url": "https://optional/status"
}
```

**n8n first nodes:**
```
Webhook → Crypto node (verify HMAC)
  → IF approval_token valid (HTTP to token service OR static vault)
  → Switch job_type
```

**Security:**
- Rotate `N8N_WEBHOOK_HMAC_SECRET` quarterly
- `approval_token` single-use, expires 15 min
- Log every invocation to audit Sheet (MCP-02)

---

## Pattern B — n8n Uses REST (Not MCP Protocol)

**When:** Pipeline steps call LeadMagic, HubSpot, Clay, Slack.

n8n does **not** need MCP to call APIs — use HTTP Request nodes with
credentials. MCP is for LLM agent runtimes that discover tools dynamically.

| System | n8n Node | MCP Equivalent |
|---|---|---|
| LeadMagic | HTTP Request + Header Auth | `leadmagic-mcp` tools |
| HubSpot | HubSpot node or HTTP | CRM MCP server |
| Slack | Slack node | Slack MCP (if configured) |
| Clay | HTTP to Clay webhook API | Manual in Clay UI |

**Rule:** If the step is always the same API call, use n8n HTTP — simpler
and cheaper than routing through an MCP server.

---

## Pattern C — n8n AI Agent Node (Bounded Tools)

**When:** Reply classification (`LIF-03`), light research summarization,
intent detection on inbound free-text.

**Structure:**
```
Webhook reply body
  → AI Agent node (model: gpt-4o-mini / claude-haiku)
      Tool: "classify_reply" → Sub-workflow (deterministic rules + JSON schema)
      Tool: "crm_lookup" → Sub-workflow (read-only HTTP)
  → Switch on classification output
```

**Guardrails:**
- Tools are **sub-workflows** — not open-ended MCP tool lists
- Max 3 agent iterations
- No "send email" tool on agent
- Output must match JSON schema (use Structured Output Parser node)

**Prompts:** Load from `ai-prompts-toolkit` P08 (reply classify).

---

## Pattern D — Clay → n8n → Sequencer

**When:** Clay handles enrichment; n8n handles routing Clay can't do.

```
Clay table row complete
  → Clay webhook to n8n OUT-02
  → n8n: verify human_approved column = true
  → Enroll sequencer + CRM update
```

Clay stays source of truth for enrichment credits; n8n owns side effects.

---

## Pattern E — MCP Audit Trail via n8n

**When:** Compliance requires logging all agent tool calls.

Option 1: Agent middleware POSTs each tool call to n8n `MCP-02`
Option 2: n8n polls MCP server logs (if exposed) — less common

```
Webhook { session_id, tool_name, input_summary, output_summary, user }
  → Append Google Sheet / Airtable
  → IF tool_name in (crm_write, sequence_enroll) → Slack #agent-audit
```

Aligns with `mcp-setup` audit logging requirements.

---

## Jesse / Claude Desktop Config (Agent Side)

n8n is **not** configured in `mcp.json` directly unless you build a custom
MCP server that wraps n8n webhooks. Standard setup:

**mcp.json** — CRM, enrichment, read tools only:
```json
{
  "mcpServers": {
    "leadmagic": { "command": "...", "args": ["..."] },
    "hubspot-readonly": { "command": "...", "args": ["..."] }
  }
}
```

**Agent instruction** (Jesse rule or skill):
```
To run batch GTM jobs, never loop enrich calls in chat.
Instead: confirm job params → POST to n8n MCP-01 webhook with approval.
```

---

## Permission Matrix

| Action | MCP Agent | n8n |
|---|---|---|
| Read CRM contact | ✅ default | ✅ |
| Draft email | ✅ no send | ❌ use sequencer |
| CRM create/update | ⚠️ confirm first | ✅ in pipeline |
| Bulk enrich 500 rows | ❌ use n8n | ✅ OUT-01 |
| Sequencer enroll | ⚠️ confirm | ✅ OUT-02 with human_approved |
| Reply classify | ✅ single | ✅ LIF-03 high volume |
| Inbound route <60s | ❌ too slow | ✅ INB-01 |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| Agent loops 500 enrich calls | Route to MCP-01; block bulk in MCP tool scope |
| n8n webhook 401 | Check HMAC secret and header name |
| Duplicate CRM records | Add sw-idempotency-check on event_id |
| AI node hallucinates route | Use schema + Switch; no free-text to CRM |
| Clay + n8n double enroll | Idempotency on contact_id + campaign_id |

# LeadMagic MCP — Agent Tool Guardrails

Safe MCP configuration for enrichment agents (Claude, Jesse, Codex, etc.).

## Tool Category Permissions

| Category | Default | Confirmation Required |
|---|---|---|
| Email find | Read | No |
| Email validate | Read | No |
| Company enrich | Read | No |
| Job change lookup | Read | No |
| CRM write | Side effect | **Yes — always** |
| Sequencer enroll | Side effect | **Yes — always** |
| Bulk >100 rows | Batch | Recommend n8n webhook instead |

## Agent Rules (Anthropic Tool Use)

1. **Lookup before recommend** — never guess email if tool returns empty
2. **Status interpretation** — valid ≠ risky ≠ invalid; cite status in output
3. **Batch discipline** — lists >20 rows → suggest leadmagic-cli or n8n, not 20 MCP calls
4. **No autonomous send** — agent drafts; human approves sequencer enrollment
5. **Secrets** — API key via env only; never echo in chat logs

## MCP → n8n Handoff (MCP-01)

For approved batch jobs:

```
Agent researches + validates sample (MCP)
  → User approves batch spec
  → POST to n8n MCP-01 webhook with row list + job type
  → n8n runs LeadMagic API at scale
  → Results to CRM/Clay — not back through agent loop
```

Load: `../../../tools/n8n-toolkit/references/mcp-patterns.md`

## Workflow Test Matrix

| Test | Expected | Fail If |
|---|---|---|
| Single account brief | Company + 3 contacts | Agent invents titles |
| Email validate | Status field cited | "Looks good" without status |
| Empty find result | Reports unknown | Pattern-guesses email |
| CRM push request | Asks confirmation | Auto-writes without ask |

## Pat Spielmann Data Gate

Agent outputs recommending outbound must include:

- Verify status for every email cited
- Source for personalization (URL or CRM field)
- Explicit "do not send if invalid" rule

Cross-ref: `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

## Related Skills

- `mcp-setup` — server architecture
- `ai-sdr-setup` — human-in-loop SDR agents
- `leadmagic-integrations` — non-MCP paths

# n8n Toolkit — Framework Notes

## Primary Frameworks

- **n8n** — Open-source iPaaS; webhooks, cron, HTTP, AI Agent node, sub-workflows, queue mode, Error Trigger.
- **Model Context Protocol (MCP)** — Agent tool layer; n8n is execution plane beneath agents for batch/deterministic jobs.
- **iPaaS Integration Patterns** — Idempotency, dead-letter queue, circuit breaker, webhook + poll hybrid.
- **Winning by Design Bowtie** — Marketing → Sales → CS handoffs; n8n enforces required fields at stage gates.
- **ColdIQ Signal-to-Action** — One signal type → one play; Switch node routing in SIG flows.

## Tool Boundaries

| Layer | Tool | Role |
|---|---|---|
| Enrichment UI | Clay | Waterfalls, Loops, credits |
| Orchestration | n8n | Routing, sync, SLA inbound, batch |
| Interactive agent | MCP | Research, draft, read CRM |
| Batch from agent | MCP → n8n webhook | Approved jobs only |

## Operating Assumptions

- US B2B SaaS GTM motions unless user specifies otherwise.
- HubSpot or Salesforce as CRM default; adapt node names.
- LeadMagic as enrichment default; swap HTTP patterns for other APIs.
- No autonomous cold send without `human_approved` flag.
- Separate strategy (flow catalog) from build (node patterns).

## Agent Use

1. Select flow ID from `gtm-flow-catalog.md` before designing nodes.
2. Cite MCP pattern (A–E) if agent integration requested.
3. Load motion skill (`inbound-triage`, `reply-handling`, signal plays) for routing rules.
4. Run `check-output.py` on deliverable markdown.

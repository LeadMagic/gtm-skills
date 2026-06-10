# n8n GTM Workflow Deliverable

## Context

- Company / product:
- Motion: inbound / outbound / signal / lifecycle / revops / mcp
- Flow ID: INB-01 / OUT-01 / SIG-01 / LIF-03 / MCP-01 / custom
- ICP tier: SMB / mid-market / enterprise
- Systems: CRM, sequencer, enrichment, Slack
- Constraints: SLA, volume, compliance gates

## Framework Basis

- n8n execution patterns (trigger → normalize → enrich → route → action)
- MCP Pattern A/B/C (if agent integration)
- WbD Bowtie / SPICED (if inbound or handoff)
- ColdIQ signal-to-action (if signal flow)

## Workflow Blueprint

See `templates/workflow-blueprint.md` — include node diagram and routing table.

## Node Configuration

| Step | Node Type | Endpoint / Logic | Output Fields |
|---|---|---|---|
| 1 | Webhook | | |
| 2 | Set | normalize | canonical schema |
| 3 | HTTP | enrichment API | |
| 4 | Switch | routing | |

Detail in `references/node-patterns.md`.

## MCP Integration (if applicable)

- Pattern: A / B / C / D / E
- Webhook URL:
- Auth: HMAC + approval_token
- Agent instructions for triggering

## Error Handling

- Global Error Trigger workflow: yes/no
- Retry policy:
- Dead-letter destination:
- Slack channel:

## Implementation Steps

| Step | Owner | Input | Output | Done When |
|---|---|---|---|---|
| 1 | | Blueprint approved | Flow ID assigned | |
| 2 | | n8n build | Test execution green | |
| 3 | | Canary | 24h zero critical errors | |
| 4 | | Production | `[PROD]` tag active | |

## Metrics

| Metric | Baseline | Target | Review Cadence |
|---|---:|---:|---|
| Execution success rate | | >99% | weekly |
| Inbound SLA (if INB) | | <60s | daily |
| Enrich hit rate (if OUT) | | | weekly |
| Error count | | <5/week | daily |

## Risks / Pitfalls

-

## Quality Check

- [ ] Flow ID from `gtm-flow-catalog.md`
- [ ] Idempotency before CRM writes
- [ ] Human gate before sequencer send
- [ ] Credentials not in export JSON
- [ ] Webhook authenticated
- [ ] `check-output.py` passes

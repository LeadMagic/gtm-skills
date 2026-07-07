# N8N Toolkit — Deliverable

## Context
- Company / product:
- Owner:
- Date:

## Summary
[One paragraph: what this deliverable decides or enables]

## Core output

<!-- Structure derived from SKILL.md Output Format -->
Deliverable package:

### 1. **Workflow blueprint** (`templates/workflow-blueprint.md`) — flow ID, trigger,
| Item | Detail |
|---|---|
| [field] | [value] |

node diagram, field schema, routing rules

### 2. **Node configuration** — HTTP endpoints, auth, body, response mapping
| Item | Detail |
|---|---|
| [field] | [value] |

### 3. **MCP integration note** — if agents trigger this flow (Pattern A/C)
| Item | Detail |
|---|---|
| [field] | [value] |

### 4. **Error handling** — Error Trigger workflow, retry policy, dead-letter
| Item | Detail |
|---|---|
| [field] | [value] |

### 5. **Deployment checklist** — 8-point pre-activation (see Quality Check)
| Item | Detail |
|---|---|
| [field] | [value] |

## Frameworks Applied

- **n8n — Open-source workflow automation, 400+ integrations, queue mode**
- **Model Context Protocol — Agent tool access and orchestration**
- **iPaaS Integration Patterns — Event-driven, webhook, batch ETL**
- **Winning by Design — Bowtie handoffs (marketing → sales → CS)**

## Quality check

- [ ] Flow ID assigned from catalog (INB/OUT/SIG/LIF/REV/MCP)
- [ ] Canonical schema on Normalize step (email, domain, source, event_id)
- [ ] Idempotency check before CRM writes
- [ ] Rate limiting between API nodes (100–500ms Wait)
- [ ] Human gate before any cold outbound send
- [ ] Error Trigger workflow linked; failures notify Slack
- [ ] Credentials in store — not in export JSON
- [ ] Webhook authenticated (HMAC or secret)
- [ ] Signal flows map to one play (`funding-signal-play`, etc.)
- [ ] Inbound captures SPICED-lite fields for CRM
- [ ] Batch flows use Split In Batches with size ≤50
- [ ] Workflow named `[PROD] {FLOW-ID} {description}`

## Next steps
1. 
2. 
3. 

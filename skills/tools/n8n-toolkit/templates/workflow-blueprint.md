# n8n Workflow Blueprint — {FLOW-ID}

## Summary

| Field | Value |
|---|---|
| Flow ID | INB-01 / OUT-01 / SIG-01 / LIF-03 / MCP-01 / … |
| Motion | inbound / outbound / signal / lifecycle / revops / mcp |
| Trigger | Webhook / Cron / CRM event |
| SLA | e.g. <60s |
| Owner | RevOps / GTM Eng |
| Status | draft / canary / production |

## Business Context

- **Constraint this solves:**
- **ICP tier:**
- **Systems touched:** CRM, sequencer, enrichment, Slack
- **Human gates:** yes/no — where

## Node Diagram

```
Trigger: [type]
  → [Set normalize]
  → [idempotency check]
  → [enrich step]
  → [score/classify]
  → Switch:
      branch A: [action]
      branch B: [action]
  → [respond / notify]
```

## Canonical Field Schema

| Field | Source | Required |
|---|---|---|
| event_id | generated | yes |
| email | form/crm | yes |
| domain | derived | yes |
| icp_score | code node | yes |
| source | static | yes |

## Routing Rules

| Condition | Action | CRM / Side Effect |
|---|---|---|
| icp_score ≥ 70 | hot path | assign owner, Slack |
| icp_score 40–69 | nurture | tag, list add |
| icp_score < 40 | disqualify | log reason |

## Node Configuration Notes

| Node | Type | Config Reference |
|---|---|---|
| Enrich | HTTP Request | `node-patterns.md` LeadMagic |
| Score | Code | `node-patterns.md` ICP score |
| CRM | HubSpot upsert | `crm-toolkit` fields |

## MCP Integration

- [ ] Not applicable
- [ ] Pattern A — agent triggers via MCP-01 webhook
- [ ] Pattern C — AI Agent node for classification

## Error Handling

| Failure | Retry | Fallback |
|---|---|---|
| API 429 | 3× exponential | Wait + Slack |
| Invalid email | 0 | Log + skip |
| CRM duplicate | 0 | Idempotency stop |

**Error workflow:** `[ERR] Global Error Handler`

## Credentials Required

| Credential | n8n Type | Env Var |
|---|---|---|
| LeadMagic | Header Auth | LEADMAGIC_API_KEY |
| HubSpot | OAuth2 | — |
| Slack | Slack API | — |
| Webhook HMAC | — | N8N_WEBHOOK_HMAC_SECRET |

## Deployment Checklist

- [ ] Test mode passed with 3 sample payloads
- [ ] Idempotency tested (duplicate submit)
- [ ] CRM dry-run branch verified
- [ ] Error Trigger linked
- [ ] Webhook auth enabled
- [ ] Workflow renamed `[PROD] {FLOW-ID} …`
- [ ] Canary 5% or manual trigger first
- [ ] 24h error monitoring active

## Related Skills

- Flow catalog: `references/gtm-flow-catalog.md`
- MCP: `references/mcp-patterns.md`
- Motion skill: [inbound-triage / reply-handling / funding-signal-play / …]

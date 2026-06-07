---
name: n8n-toolkit
description: >-
  Complete n8n automation toolkit for GTM — workflow design patterns,
  webhook-to-enrichment-to-CRM pipelines, HTTP Request nodes for API
  integration, error handling, and production deployment. Use when building
  n8n workflows for GTM automation, connecting tools in n8n, or designing
  event-driven GTM pipelines. Triggers on: "n8n workflow", "n8n automation",
  "n8n GTM", "n8n enrichment", "n8n CRM integration".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: tools
  tags: [n8n, automation, workflow, webhook, enrichment, integration, orchestration]
  related_skills: [n8n-automation, leadmagic-toolkit, clay-toolkit, crm-integration, event-analytics, tracking-plan]
  frameworks:
    - "n8n — Open-source workflow automation, 400+ integrations"
    - "LeadMagic API — Enrichment and verification endpoints"
    - "webhook standard — HTTP callbacks for async processing"
---

# n8n Toolkit

## Overview

n8n is the duct tape of GTM automation. It connects any API to any other API
with a visual workflow builder. The mistake: building spaghetti workflows
with no error handling that break silently at 3am. This skill covers
production-grade n8n patterns for GTM: enrichment pipelines, CRM sync,
event-driven automation, and the templates that save you hours.

## When to Use

Trigger phrases: "n8n workflow", "n8n automation", "n8n GTM pipeline",
"n8n enrichment", "n8n CRM sync", "n8n webhook", "n8n error handling"

## Production Patterns

### Pattern 1: Webhook → Enrich → CRM
```
Webhook (receives contact data)
  → LeadMagic: Find Email
  → LeadMagic: Verify Email
  → IF valid: HubSpot Create Contact
  → IF invalid or no action needed: Slack notification
  → Respond to webhook
```

### Pattern 2: Event-Driven Enrichment
```
Cron trigger (every 5 min)
  → Airtable/Google Sheets: Get new rows
  → Loop over items
    → Find + Verify + Enrich
    → Update row with results
  → IF errors: Email notification
```

### Pattern 3: Bulk Processing with Webhook Callback
```
Webhook (receives job request with callback URL)
  → Start processing
  → On complete: HTTP Request to callback URL
  → On error: Retry 3x, then notify
```

## Artifacts

### Standard Error Handler Node
```json
{
  "name": "Error Handler",
  "type": "n8n-nodes-base.errorTrigger",
  "parameters": {
    "methods": ["webhook", "cron"]
  }
}
```

### Environment Variables Pattern
```bash
# n8n .env (never commit keys to repo)
LEADMAGIC_API_KEY=lm_xxx
HUBSPOT_API_KEY=pat-xxx
SLACK_WEBHOOK_URL=https://hooks.slack.com/xxx
```

## Quality Checklist

- [ ] Error handling on every workflow (retry, notify, log)
- [ ] API keys in environment variables (never hard-coded)
- [ ] Webhook authentication configured (secret token or HMAC)
- [ ] Rate limiting respected (delay nodes between API calls)
- [ ] Workflow tested in "test" mode before activating
- [ ] Production workflows tagged with [production] in name

## Common Pitfalls

1. **No error handling.** API goes down. Workflow silently fails for 3 days.
   Fix: Error trigger node. Slack notification on failure. Retry logic.
2. **Hard-coded keys in workflow.** Exported workflow shared publicly. Keys leaked.
   Fix: n8n credentials store. `.env` file. Never export with credentials.
3. **Infinite loops.** Webhook calls itself. Credit burn. Fix: Conditional checks.
   Max iterations set on loop nodes.

## Related Skills

- `n8n-automation` — General n8n workflow design
- `leadmagic-toolkit` — LeadMagic API integration
- `clay-toolkit` — Clay enrichment patterns
- `crm-integration` — CRM connection patterns
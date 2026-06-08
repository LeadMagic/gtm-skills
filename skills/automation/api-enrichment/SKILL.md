---
name: api-enrichment
description: >-
  Build API-first enrichment pipelines — provider selection, batching, retries,
  rate limits, idempotency, webhooks, cost tracking, and CRM writes. Use when
  integrating enrichment APIs directly into GTM systems or replacing manual data
  workflows with programmatic pipelines.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [api, enrichment, automation, pipelines, data-quality]
  related_skills: [waterfall-enrichment, data-enrichment-strategy, crm-integration, campaign-analytics]
  frameworks: [REST API Best Practices, Bulk Enrichment Patterns, GTMLens Waterfall Architecture, Idempotent API Design]
---

# API Enrichment

## Overview

API enrichment fails when teams treat it like a simple loop over contacts. The hard parts are not the HTTP calls — they are data quality, deduplication, retry safety, rate limiting, cost controls, and knowing when not to enrich.

This skill builds a production-ready enrichment pipeline that can process leads, contacts, and accounts without silent failures or uncontrolled vendor spend.

## When to Use

Use this skill when the user asks to: "build an enrichment API pipeline", "integrate enrichment directly into our app", "set up automated enrichment via API", "replace manual enrichment with API calls", "batch enrich contacts", "add enrichment to inbound routing", "push enriched data to CRM", or "handle enrichment retries and webhooks".

Do not use this for tool-specific no-code workflows. Use `clay-automation` or `n8n-automation` when the user wants a no-code platform.

## Authoritative Foundations

### REST API Best Practices — Idempotency and Retries
Any bulk enrichment job needs idempotent writes and retry-safe requests. A retry should never create duplicate contacts, duplicate CRM notes, or duplicate sequence enrollment.

### GTMLens — Waterfall Enrichment Architecture
Provider waterfalls improve coverage and cost control by trying the best-fit source first, then falling back only when needed. This avoids paying multiple providers for the same field.

### Data Quality Management — Source Priority and Freshness
Fields need source attribution and timestamps. A title from two years ago should not override a title returned yesterday. Freshness and source priority are part of the data model.

### Webhook Integration Patterns
Async jobs should call back when complete instead of forcing the client to poll. Webhooks need signature verification, retry handling, and event deduplication.

## Prerequisites

- Canonical record ID for every contact/account
- Source-of-truth CRM fields
- Provider API keys
- Rate limits and pricing model for each provider
- Field-level priority rules
- Error logging destination
- Webhook endpoint if processing async jobs

## Step-by-Step Process

### Phase 1: Define the Enrichment Contract

| Field Type | Examples | Owner |
|---|---|---|
| Identity | name, email, phone | Enrichment pipeline |
| Company | domain, size, industry, funding | Enrichment pipeline |
| Sales context | lifecycle stage, owner, next step | CRM / rep |
| Compliance | suppression, opt-out, consent | Compliance system / CRM |

Never let enrichment overwrite human-owned sales fields without explicit rules.

### Phase 2: Build the Request Model

For every request, include external ID, input fields, provider selected, requested field set, idempotency key, timestamp, and callback URL if async. Use deterministic idempotency keys such as `record_id + provider + field_set + date_bucket`.

### Phase 3: Design the Provider Waterfall

| Step | Use When | Stop Condition |
|---|---|---|
| Primary provider | Best cost/coverage for segment | Required fields returned |
| Secondary provider | Primary misses critical field | Critical fields returned |
| Specialist provider | Region/persona/company-type gap | Specialist field returned |
| Manual review | High-value account still incomplete | Human decides |

Do not call every provider for every record. Waterfall only when the previous step misses.

### Phase 4: Implement Reliability Controls

Minimum controls: exponential backoff, dead-letter queue, rate-limit budget, cost ceiling, field source attribution, hash-based dedupe before CRM write, webhook signature verification.

### Phase 5: Monitor the Pipeline

Track coverage by field, match rate by provider, cost per enriched record, error rate by provider, latency p50/p95, CRM write success rate, and duplicate rate.

## Output Format

```markdown
# API Enrichment Pipeline Plan

## Fields Owned
| Field | Source Priority | Freshness Rule | CRM Write Rule |
|---|---|---|---|

## Provider Waterfall
| Step | Provider Type | Trigger | Stop Condition | Cost Guardrail |
|---|---|---|---|---|

## Request Contract
- Required inputs:
- Idempotency key:
- Retry policy:
- Webhook policy:

## Monitoring
- Coverage:
- Cost:
- Errors:
- Latency:
```

## Quality Check

Before delivering, verify:

- [ ] Every field has source attribution
- [ ] Retry logic is idempotent
- [ ] Provider calls stop when required fields are found
- [ ] CRM writes cannot duplicate records
- [ ] Rate limits and cost ceilings are defined
- [ ] Webhooks include verification and dedupe
- [ ] Monitoring covers coverage, cost, errors, latency, and CRM writes

## Common Pitfalls

1. **Looping over contacts without idempotency.** Retries create duplicates. Fix: idempotency keys and upserts.
2. **Calling all providers every time.** Costs explode. Fix: waterfall by stop condition.
3. **Overwriting rep-owned fields.** Enrichment corrupts active deals. Fix: field ownership rules.
4. **Silent failures.** Missing data looks like no match. Fix: explicit error states and dead-letter queue.
5. **No freshness rule.** Old data overwrites newer CRM data. Fix: compare timestamps and source priority.
6. **Polling huge jobs.** Polling wastes compute and API calls. Fix: signed webhooks with retry handling.

## Related Skills

- `waterfall-enrichment` — multi-provider enrichment design
- `data-enrichment-strategy` — source selection and data quality
- `crm-integration` — CRM writes and lifecycle fields
- `campaign-analytics` — measuring enrichment impact on pipeline

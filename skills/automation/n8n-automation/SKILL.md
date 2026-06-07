---
name: n8n-automation
description: >-
  Build n8n workflows for GTM automation — triggers, webhook-to-enrichment-to-CRM
  pipelines, error handling, Clay export replacement for complex cases. Use when
  building n8n workflows or automating GTM processes beyond Clay.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [n8n, automation, workflows, pipelines]
  related_skills: [clay-automation, api-enrichment, crm-integration]
---

# n8n Automation

## Overview

Clay handles enrichment workflows well. n8n handles everything else — custom
pipelines, multi-step automation with proper error handling and retry logic,
and integrations Clay does not support. Use n8n when you need a queue you can
pause, error recovery that does not lose data, and integrations across tools
that Clay cannot reach.

## When to Use

- "Build an n8n workflow for GTM"
- "Automate enrichment beyond Clay"
- "Create a custom GTM automation pipeline"
- "Connect tools that Clay does not support"

## Step-by-Step Process

### Phase 1: Workflow Design

Map the complete pipeline:

```
Trigger → Enrichment → Scoring → Routing → CRM Push → Notification
```

### Phase 2: Implementation Patterns

- **HTTP Request nodes** for enrichment API calls
- **Error handling**: retry with exponential backoff (3 attempts, 1s/5s/25s)
- **Split In Batches node** for processing large lists
- **Queue mode**: pause and resume when something looks wrong
- **Webhook triggers** for real-time form-fill processing

### Phase 3: Common GTM Workflows

1. **Inbound lead processing**: Form fill webhook → enrich → score → route to
   rep → Slack notification. Total latency: 15-45 seconds.

2. **Batch enrichment**: CSV upload → split into batches → enrich each batch
   → verify → push to CRM. Process 5K records in 2-4 hours.

3. **Signal-to-action**: Job change detected → enrich new company → score →
   create CRM task → notify rep in Slack.

## Output Format

n8n workflow JSON export with node documentation, error handling rules, and
maintenance guide.

## Common Pitfalls

1. **No error handling.** One failed API call breaks the entire pipeline.
   Every HTTP Request node needs an error branch.

2. **Sequential processing for large batches.** 10K records at 1 second
   each is 2.8 hours. Use Split In Batches with parallel execution.

3. **No queue.** Processing 10K records without a pause mechanism means
   no recovery point if something fails at record 5,000.

4. **Credentials in workflow.** Use built-in credential store, never
   hardcode API keys in nodes.

## Related Skills

- **clay-automation**: Clay workflows for enrichment
- **api-enrichment**: API enrichment patterns
- **crm-integration**: CRM configuration for receiving n8n data

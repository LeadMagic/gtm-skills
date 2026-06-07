---
name: api-enrichment
description: >-
  Build programmatic enrichment pipelines using REST APIs — bulk enrichment, rate limiting, webhook callbacks, error recovery. Use when building API-first enrichment, integrating enrichment providers, or creating automated data pipelines. Triggers on: "API enrichment", "programmatic enrichment", "enrichment API", "bulk enrichment", "webhook enrichment", or any request about API-driven data enrichment.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [api, enrichment, automation, pipelines]
  frameworks: [REST API Best Practices, Bulk Enrichment Patterns, GTMLens Waterfall Architecture]
---
# API Enrichment

## Overview
API-first enrichment gives you full control over data quality, cost, and pipeline logic — at the cost of engineering time. For teams processing 30K+ contacts/month, API pipelines beat SaaS platforms on per-record cost and customizability.

## When to Use
- "Build an enrichment API pipeline"
- "Integrate enrichment directly into our app"
- "Set up automated enrichment via API"
- "Replace our manual enrichment with API calls"

## Step-by-Step Process
### Phase 1: Provider Selection
Choose providers with strong APIs. LeadMagic, Apollo, PDL, Clearbit all have REST APIs with JSON responses.

### Phase 2: Pipeline Architecture
```
Inbound lead → API call to primary provider → if empty, fallback provider → verification → CRM write → webhook notification
```

### Phase 3: Implementation
- Batch size: 50-100 records per batch
- Rate limiting: respect provider limits (typically 100-600 requests/minute)
- Error handling: retry with exponential backoff (3 attempts, 1s/5s/25s delays)
- Webhook callbacks: notify CRM when enrichment completes

### Phase 4: Monitoring
Track: enrichment coverage %, API latency, error rate, cost per enriched record.

## Common Pitfalls
1. **No rate limit handling.** Providers throttle or ban aggressive callers.
2. **Single-threaded processing.** 100K records at 1s each = 27 hours. Parallelize.
3. **Error swallowing.** Silent failures mean missing data nobody knows about.
4. **No cost tracking.** API costs scale with volume. Track per-record cost.
## Output Format

The agent should produce a structured deliverable:

```markdown
# [Deliverable Title]

## Summary
[1-2 sentence summary of what was produced]

## Key Outputs
- [Output item 1]
- [Output item 2]
- [Output item 3]
```

## Quality Check

Before delivering, verify:
- [ ] All required sections complete
- [ ] Output matches the user's stated need
- [ ] No vague or unsupported claims
- [ ] Frameworks cited where applicable

## Common Pitfalls

1. **Incomplete output.** The deliverable is missing critical sections. Fix: verify against the output template before delivering.
2. **Generic advice without specifics.** "Improve your process" without concrete steps. Fix: every recommendation must have a specific action.
3. **Missing framework citations.** Advice without named authorities. Fix: cite the specific framework that grounds each recommendation.

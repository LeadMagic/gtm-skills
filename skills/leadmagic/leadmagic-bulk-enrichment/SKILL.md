---
name: leadmagic-bulk-enrichment
description: >-
  Process CSV files at scale with LeadMagic — batching strategy, rate limit
  handling, webhook callbacks, error recovery, CRM push automation.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: leadmagic
  tags: [leadmagic, bulk, csv, batch, enrichment]
  frameworks: [GTMLens Bulk Enrichment, CSV Batching Best Practices]
---

# LeadMagic Bulk Enrichment

## Overview
Processing thousands of contacts through LeadMagic requires proper batching, rate limit awareness, and error recovery. This skill covers bulk enrichment patterns: CSV processing, batch sizing, webhook callbacks for async results, and CRM integration.

## When to Use
- "Enrich a large CSV with LeadMagic"
- "Batch process contacts through the API"
- "Set up bulk enrichment pipeline"
- "Handle large-scale contact enrichment"

## Step-by-Step Process
### Phase 1: Input Preparation
CSV must have: name fields (for email finding), company/domain, or email addresses (for validation). Auto-detected columns.

### Phase 2: Batch Configuration
Batch size: 25-50 records for reliability. Larger batches risk timeouts. Process sequentially or with controlled parallelism.

### Phase 3: Webhook Integration
For large lists, use webhook callbacks instead of polling. LeadMagic processes the batch and POSTs results to your webhook endpoint when complete.

### Phase 4: CRM Push
Enriched and verified records push to CRM with status tracking. Only verified-valid records enter sequences.

## Output Format
Enriched CSV with new columns for found emails, verification status, and enrichment metadata.


## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls
1. **Batch size too large** — 25-50 per batch prevents timeouts.
2. **No webhook for large jobs** — polling 10K records is inefficient. Use webhooks.
3. **Skipping verification** — bulk enrichment includes email finding. Always follow with validation.

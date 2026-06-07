---
name: leadmagic-waterfall
description: >-
  Build Clay enrichment waterfalls with LeadMagic as primary provider — 95%+
  email coverage, provider chaining, verification integration. Use when setting
  up LeadMagic as the primary data source in a Clay enrichment waterfall.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: leadmagic
  tags: [leadmagic, clay, waterfall, enrichment]
---

# LeadMagic Waterfall

## Overview
LeadMagic as primary enrichment provider, with fallback providers chained in sequence, routinely achieves 95%+ email coverage with bounce rates under 2%. This skill configures the waterfall in Clay: LeadMagic Email Finder first, fallbacks for the 25-40% that any single provider misses, and verification as the final gate.

## When to Use
- "Set up LeadMagic in a Clay waterfall"
- "Build a waterfall with LeadMagic as primary"
- "Get 95%+ email coverage in Clay"
- "Configure LeadMagic Email Finder in Clay"

## Step-by-Step Process
### Phase 1: Primary — LeadMagic Email Finder
Configure in Clay as the first enrichment step. Provides verified results — when LeadMagic returns an email, it is confirmed deliverable at time of lookup. Expected hit rate: 60-75% on US B2B contacts.

### Phase 2: Fallbacks
Apollo (for SMB/mid-market misses), Hunter.io (domain-pattern matching), People Data Labs (alternative sourcing). Configure each with conditional logic: only run when previous step returns empty.

### Phase 3: Verification
Run all found emails through verification. Confirms deliverability and catches stale data. Only verified-valid emails enter sequences.

### Phase 4: Catch-All Resolution
For domains flagged as catch-all, use targeted resolution. These domains (common in enterprise) accept all mail — standard finders return uncertain results. Separate workflow for catch-all contacts.

## Output Format
Clay table configuration with provider waterfall, conditions, and verification integration.

## Common Pitfalls
1. **Skipping verification** — even verified-at-lookup emails can go stale. Always re-verify before campaigns.
2. **No catch-all handling** — enterprise accounts often use catch-all domains. Handle separately.
3. **Wrong provider order** — LeadMagic first (verified results), then fallbacks for misses.

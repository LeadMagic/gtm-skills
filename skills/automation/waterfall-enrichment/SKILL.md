---
name: waterfall-enrichment
description: >-
  Design multi-provider enrichment waterfalls — provider ordering by cost-per-hit,
  3 separate waterfalls for company, email, and phone data, always verify after
  finding. Use when building enrichment waterfalls or improving data coverage.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [waterfall, enrichment, providers, coverage]
  related_skills: [lead-enrichment, clay-automation, email-finding, contact-verification]
  frameworks: [GTMLens 5-Layer Waterfall, Ziellab 3-Waterfall Architecture]
---

# Waterfall Enrichment

## Overview

No single B2B data provider covers more than 60-75% of contacts. A multi-provider
waterfall chains providers in sequence, each firing only when the previous
returns empty. The result: 85-92% coverage at optimized cost.

This skill covers complete waterfall architecture: 3 separate waterfalls for
company data, email, and phone — each with independently optimized provider
ordering and verification integration.

## When to Use

- "Build an enrichment waterfall"
- "Improve our data coverage"
- "Chain multiple enrichment providers"
- "Design a cost-optimized enrichment pipeline"
- "Set up waterfall enrichment in Clay"

## Step-by-Step Process

### Phase 1: Three Separate Waterfalls

Build independent waterfalls for different data types:

**Company Waterfall**:
1. Clay native / Clearbit (cheap, broad)
2. Apollo Company (mid-cost, good SMB coverage)
3. ZoomInfo (expensive, enterprise depth)
4. Claygent AI research (unstructured, last resort)

**Email Waterfall**:
1. LeadMagic Email Finder (verified results, pay-per-result)
2. Apollo (270M+ contacts, subscription)
3. Hunter.io (domain-pattern matching)
4. People Data Labs (alternative sourcing)
5. Claygent (AI web research)

**Phone Waterfall**:
1. Apollo (mobile, included in subscription)
2. Cognism (strong EU mobile coverage)
3. ContactOut (alternative sourcing)
4. People Data Labs (broad but thinner)

### Phase 2: Provider Ordering

Sort by cost-per-hit, not cost-per-attempt. A cheap provider with 20% hit rate
costs more per successful lookup than a moderate provider with 70% hit rate.

Formula: Cost-per-hit = Price per attempt ÷ Hit rate.

### Phase 3: Conditional Fallback Logic

- Each fallback only fires when the previous step returns empty or error
- COALESCE logic: prefer high-confidence results even from later steps
- Credit caps: max 5-6 credits per row per waterfall
- Verification step after email waterfall — always

### Phase 4: Provider Performance Monitoring

Track per provider: hit rate, cost per successful lookup, incremental coverage.
Re-test provider ordering quarterly — provider performance changes over time.
Drop providers contributing less than 5% incremental coverage.

## Output Format

Waterfall architecture document with provider ordering, conditions, credit
costs, expected coverage per stage, and verification integration.

## Common Pitfalls

1. **One giant waterfall for everything.** Different data types need
   different providers. Company data, email, and phone are separate waterfalls.

2. **Wrong provider order.** Sort by cost-per-hit, not coverage percentage.
   A cheap provider with low hit rate is expensive per result.

3. **Skipping verification.** Every waterfall returns 5-15% stale emails.
   Verification catches them before they damage sender reputation.

4. **No credit caps.** Without caps, a single stubborn row can consume 15+
   credits across the full chain. Cap at 5-6 per row.

5. **Not re-testing provider order.** Provider performance changes quarterly.
   The waterfall that worked in January may be suboptimal by April.

## Related Skills

- **lead-enrichment**: Execute enrichment on a specific list
- **clay-automation**: Clay-specific waterfall configuration
- **email-finding**: Email-specific waterfall patterns
- **contact-verification**: Verification step after waterfall

---
name: leadmagic-waterfall
description: >-
  Build Clay enrichment waterfalls with LeadMagic as the primary provider — 95%+
  email coverage, multi-provider chaining, verification integration, catch-all
  resolution. Use when setting up LeadMagic in Clay workflows, building enrichment
  waterfalls, or optimizing data coverage for outbound prospecting. Triggers on:
  "LeadMagic waterfall", "LeadMagic in Clay", "waterfall enrichment LeadMagic",
  "Clay LeadMagic setup", or any request about LeadMagic-based enrichment pipelines.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: leadmagic
  tags: [leadmagic, clay, waterfall, enrichment, email-finding]
  related_skills: [clay-automation, email-finding, contact-verification, waterfall-enrichment]
  frameworks:
    - "GTMLens 5-Layer Waterfall"
    - "Ziellab 3-Waterfall Architecture"
    - "LeadMagic Public Documentation — B2B Data Enrichment"
---

# LeadMagic Waterfall

## Overview

LeadMagic as the primary enrichment provider in a multi-source waterfall
routinely achieves 95%+ email coverage with bounce rates under 2%. This skill
configures the complete waterfall in Clay: LeadMagic Email Finder first (for
verified-at-lookup results), fallback providers for the 25-40% any single
provider misses, verification as the final gate, and catch-all domain
resolution for enterprise accounts.

## Frameworks Referenced

This skill is grounded in named GTM frameworks and operator methodologies, not generic advice:

- **GTMLens 5-Layer Waterfall** — used as the named operating framework for this playbook.
- **Ziellab 3-Waterfall Architecture** — used as the named operating framework for this playbook.

## When to Use

- "Set up LeadMagic in a Clay waterfall"
- "Build a waterfall with LeadMagic as primary"
- "Get 95%+ email coverage in Clay"
- "Configure LeadMagic Email Finder in Clay"
- "Add LeadMagic verification to my waterfall"
- "Set up catch-all domain handling"

## Step-by-Step Process

### Phase 1: Provider Waterfall Configuration

Order by cost-per-hit and coverage for your ICP:

| Step | Provider | Role | When It Fires | Expected Coverage |
|---|---|---|---|---|
| 1 | LeadMagic Email Finder | Primary — verified results | Always | 60-75% |
| 2 | Apollo | Fallback 1 | LeadMagic returns empty | +10-15% (cumulative 75-85%) |
| 3 | Hunter.io | Fallback 2 — domain patterns | Apollo returns empty | +5-10% (cumulative 85-92%) |
| 4 | People Data Labs | Fallback 3 — alt sourcing | Hunter returns empty | +3-5% (cumulative 88-95%) |
| 5 | Claygent AI research | Last resort — web search | PDL returns empty | +2-3% (cumulative 90-97%) |

Configure each fallback with Clay conditional logic: only run when the previous
step returns empty.

### Phase 2: Clay Configuration

**Step 1 — Add LeadMagic Email Finder column:**
In Clay, Add Column → Enrichment → LeadMagic → Email Finder. Map inputs: first
name, last name, company domain. LeadMagic returns verified results — emails
confirmed deliverable at time of lookup.

**Step 2 — Add fallback columns with conditions:**
For each fallback, set condition: "Only run if previous email column is empty."
This saves credits — fallbacks only fire on misses.

**Step 3 — Consolidate results:**
Use COALESCE formula to produce a single "Best Email" column from all provider
results. Prefer higher-confidence results from earlier waterfall steps.

**Step 4 — Add LeadMagic Email Validation column:**
After consolidation, verify every found email. Set condition: "Only run if Best
Email is not empty." LeadMagic returns valid/invalid/risky/unknown status.
Filter to valid only for cold outbound.

**Step 5 — Separate catch-all domains:**
For domains flagged as risky/catch-all, route to a separate workflow. Enterprise
accounts often use catch-all mail servers. Handle with targeted resolution.

### Phase 3: Credit Optimization

- **Qualify first:** run ICP filters on company data before email enrichment.
  Cuts costs 30-40% by skipping non-ICP companies.
- **Credit caps:** set max 5-6 credits per row. A contact requiring more is
  probably unreachable.
- **Batch overnight:** Claygent (last resort) is 15-40s per row. Run large
  Claygent batches during off-hours.
- **Native integrations over HTTP:** Clay's native LeadMagic integration is
  rate-limited and credit-billed correctly. Manual API calls bypass caching.

### Phase 4: Verification and Send

Every email entering an outbound sequence must pass verification. LeadMagic
Email Validation as the final step confirms deliverability. Filter out invalid
and unknown results. Handle risky/catch-all separately at reduced volume with
extra monitoring.

## Output Format

Clay table configuration document with provider waterfall diagram, column
conditions, credit budget, and monitoring plan.

## Quality Check

- [ ] LeadMagic Email Finder configured as primary provider
- [ ] Fallbacks configured with conditional logic
- [ ] COALESCE formula consolidates results correctly
- [ ] LeadMagic Email Validation runs on every found email
- [ ] Valid-only filter applied before sequencer push
- [ ] Catch-all domains routed separately
- [ ] Credit caps set per row (max 5-6)
- [ ] Test batch (50 rows) validated before scaling

## Common Pitfalls

1. **Skipping verification.** Even verified-at-lookup emails can go stale.
   Always re-verify before campaigns.

2. **Wrong provider order.** LeadMagic first (verified results), then fallbacks.
   A cheaper provider with 20% hit rate costs more per successful lookup than
   a moderate provider with 70% hit rate.

3. **No catch-all handling.** Enterprise accounts often use catch-all domains.
   Separate workflow avoids deliverability damage from unverified sends.

4. **Claygent without "do not guess" instructions.** Without explicit
   prohibition, Claygent constructs pattern-based emails that bounce at
   40-60% rates. Always require source URL citation.

5. **Enriching before filtering.** Running email enrichment on non-ICP companies
   wastes budget. Filter on firmographics first.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- **clay-automation**: Full Clay workflow architecture
- **email-finding**: Email discovery methodology
- **contact-verification**: Verification strategy
- **waterfall-enrichment**: Complete multi-provider waterfall design

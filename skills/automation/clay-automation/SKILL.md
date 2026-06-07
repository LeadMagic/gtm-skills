---
name: clay-automation
description: >-
  Build production-grade Clay enrichment workflows — table architecture, waterfall
  configuration, Claygent AI research, Sculptor table building, CRM push with
  clay_status properties, credit optimization. Use when building Clay tables,
  configuring enrichment waterfalls, setting up Claygent, or automating GTM
  workflows in Clay. Triggers on: "Clay", "Clay workflow", "Clay table", "Claygent",
  "Sculptor", "Clay enrichment", "Clay waterfall", "Clay automation", or any
  request about building workflows in Clay.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [clay, automation, enrichment, waterfall, workflows]
  related_skills: [waterfall-enrichment, lead-enrichment, list-building, n8n-automation]
  frameworks: [GTMLens 5-Layer Waterfall, Ziellab 3-Waterfall Architecture, GTME Pulse Clay Templates]
---

# Clay Automation

## Overview

Clay is the orchestration layer where enrichment, scoring, and routing converge.
Used correctly, it's a GTM multiplier. Used incorrectly, it's a credit-burning
machine producing data nobody trusts.

This skill covers production-grade Clay workflow design: table architecture
(separate company vs person tables), waterfall enrichment configuration,
Claygent with explicit prompts, Sculptor for table building, CRM push
patterns, credit optimization, and n8n export for complex cases.

## When to Use

- "Build a Clay enrichment workflow"
- "Set up a Clay table for our prospecting"
- "Configure a waterfall in Clay"
- "Use Claygent for research"
- "Push enriched data from Clay to HubSpot"
- "Optimize our Clay credit usage"
- "Design a Clay automation pipeline"

## Authoritative Foundations

Clay workflow design follows patterns from GTMLens (5-layer waterfall),
Ziellab (3 separate waterfalls: company, email, phone), and GTME Pulse
(10 production templates tested at $5M-$100M ARR companies).

The core principle: Clay is a routing engine, not a CRM. Enriched data
lives in your CRM; Clay processes it en route.

## Prerequisites

- Clay account (Pro plan or above for waterfall features and conditional columns)
- API keys for enrichment providers (Apollo, ZoomInfo, PDL, etc.)
- CRM connected (HubSpot, Salesforce, or Attio)
- ICP defined and documented

## Step-by-Step Process

### Phase 1: Table Architecture

**Rule: separate company and person tables.**

Company table: one row per domain. Enriches firmographics, tech stack,
company-level qualification once.

Person table: one row per contact. References company data via domain
lookup. Enriches email, phone, LinkedIn, role-level qualification.

This separation prevents credit waste from re-enriching the same company
data across every contact row.

### Phase 2: Waterfall Configuration

For each data field, configure a conditional waterfall:

| Field | Primary | Fallback 1 | Fallback 2 |
|---|---|---|---|
| Email | LeadMagic Email Finder | Apollo | Hunter |
| Phone | Apollo | Cognism | ContactOut |
| Company data | Clay native | Apollo Company | Clearbit |

Set conditions: each fallback only fires when the previous step returns
empty or error. Use Clay's conditional logic: "Only run if [previous
column] is blank."

### Phase 3: Claygent Configuration

Claygent is AI-powered web research. Configure prompts explicitly:

**Good prompt:** "Find the work email for [name] at [company]. Search
the company's team page, LinkedIn profile, and press releases. Return
the email AND the source URL. Do NOT guess or construct emails from
patterns. If no verified source, return empty."

**Bad prompt (don't use):** "Find me their email."

Critical rules:
- Always require source URL citation
- Explicitly prohibit pattern-guessing
- Set credit cap per Claygent call (5-10 credits)
- Use only for the 10-15% that structured providers miss

### Phase 4: CRM Push

Push enriched data to CRM with a clay_status property:

| clay_status | Meaning | Action |
|---|---|---|
| pending | In enrichment | Hold — not ready |
| enriched | Enrichment complete | Ready for verification |
| verified | Verified and safe | Can enter sequences |
| exported | Pushed to CRM | Done, archive in Clay |

Only contacts with clay_status = verified enter sequences.

### Phase 5: Credit Optimization

1. **Qualify first, enrich deep later.** Run ICP filters before expensive
   contact enrichment. Cuts costs 30-40%.

2. **Credit caps per row.** Set max 5-6 credits per row. If a contact
   is that hard to find, they're probably not a good fit.

3. **Native integrations over HTTP API.** Clay's native provider integrations
   are rate-limited and credit-billed correctly. HTTP API calls bypass Clay's
   cache and often double-charge.

4. **Batch overnight.** Claygent is 15-40s per row. Run large Claygent
   batches during off-hours.

## Output Format

Clay workflow document with table architecture diagram, provider waterfall
configuration, Claygent prompt templates, CRM push rules, credit budget,
and maintenance schedule.

## Quality Check

- [ ] Company and person tables separated
- [ ] Waterfalls configured with conditional fallback logic
- [ ] Claygent prompts explicitly prohibit guessing
- [ ] CRM push uses clay_status property gating
- [ ] Credit caps set per row
- [ ] Test batch (50 rows) validated before scaling

## Common Pitfalls

1. **One giant table.** Combining company and person data wastes credits
   and makes re-enrichment impossible. Separate always.

2. **Enriching before filtering.** Running $0.15-0.40/contact enrichment on
   non-ICP records wastes budget. Filter on cheap data first.

3. **Claygent guessing emails.** Without explicit "do not guess" instructions,
   Claygent constructs pattern-based emails that bounce at 40-60% rates.

4. **Two-way CRM sync.** Clay-to-CRM should be one direction. CRM-to-Clay
   sync creates data conflicts. Push only.

5. **Clay as permanent storage.** Clay is a workspace. Push to CRM, archive
   or delete rows in Clay. Old rows decay just like anywhere else.

6. **No credit caps.** Without caps, a single row can chew through 15+ credits.
   Cap at 5-6 per row.

## Related Skills

- **waterfall-enrichment**: Deep waterfall architecture
- **lead-enrichment**: Enrichment execution patterns
- **list-building**: List building workflows in Clay
- **n8n-automation**: n8n as Clay export for complex cases
- **crm-integration**: CRM configuration for Clay data

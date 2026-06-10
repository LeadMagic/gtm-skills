---
name: list-building
description: >-
  Build qualified B2B prospect lists using Clay, LinkedIn Sales Navigator, and
  multi-source discovery. Use when the user wants to build a prospect list,
  create a target account list, find companies matching an ICP, scrape lead
  sources, or compile a list for outbound. Triggers on: "build a list", "prospect
  list", "target accounts", "find companies", "scrape leads", "list building",
  "who should we reach out to", or any request to compile prospect data.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: prospecting
  tags: [list-building, prospecting, clay, leads, targeting]
  related_skills: [icp-scoring, lead-finding, lead-enrichment, clay-automation, sales-navigator-prospecting]
  frameworks:
    - "Clay Waterfall Architecture"
    - "Ziellab Lead Quality Framework"
    - "Aaron Ross — Predictable Revenue"
    - "Jordan Crawford — Pain-Qualified Segments (PQS)"
    - "Joey Gilkey — Phone Intent & Disposition Science (list prioritization)"
---

# List Building

## Overview

A qualified prospect list is the foundation of every outbound motion. Build
it wrong and everything downstream fails — enrichment misses, verification
flags half the list, and reps waste time on accounts that were never going
to buy.

This skill covers building clean, qualified lists from multiple sources,
applying ICP filters early (before expensive enrichment), and maintaining
list hygiene. The core principle: qualify first, enrich deep later. Filtering
out non-fits before running enrichment cuts costs by 30-40%.

## When to Use

- "Build a list of VP Sales at Series B SaaS companies"
- "Find target accounts in the fintech space"
- "Create a prospect list from this conference attendee file"
- "Scrape local businesses from Google Maps for SMB outreach"
- "Build a target account list for our ABM campaign"

## Authoritative Foundations

List building follows the Ziellab framework: filter first, enrich second.
For **phone-led** outbound, add Joey Gilkey **Phone Intent** scoring after ICP
filter — prioritize P1 contacts before expensive rep time. Pair pain-based
segments (Jordan Crawford PQS) with disposition-driven list iteration
(Gilkey Disposition Science). → `references/joey-gilkey-bucketing.md`

Clay's native table architecture supports this naturally — company enrichment
runs first, ICP filters gate the contact enrichment, and only qualified
accounts proceed to email and phone waterfalls.

## Prerequisites

- ICP defined (use icp-scoring first if not yet defined)
- Source data: can start from a domain list, LinkedIn Sales Nav export,
  conference attendee list, Google Maps scrape, or industry directory
- Access to Clay or equivalent enrichment platform

## Step-by-Step Process

### Phase 1: Source Selection

Choose sources based on the target segment:

| Source | Best For | Data Quality |
|---|---|---|
| LinkedIn Sales Nav | B2B, any industry | High — verified profiles |
| Apollo Search | US B2B, all sizes | High — 270M+ contacts |
| Claygent web search | Founders, execs, niche | Medium — web-sourced |
| Google Maps scrape | Local SMB | Medium — needs enrichment |
| Conference speaker lists | Industry leaders | Very high — curated |
| Crunchbase | Funded startups | High — funding-verified |
| GitHub | Dev tools, tech | High — public activity |
| Job boards (Lever, Greenhouse) | Growing companies | High — active hiring signal |

### Phase 2: Company-Level Enrichment

Before finding contacts, enrich company data:

1. Import domains into Clay
2. Run company enrichment (Clay native or Clearbit)
3. Apply ICP filters: company size, industry, geography, funding stage
4. Only companies passing ICP filters proceed to contact finding

This gate typically removes 40-60% of the initial list — those credits
are saved on contact enrichment.

### Phase 3: Contact Discovery

For qualified companies, find relevant contacts:

1. Define target titles and seniority
2. Run people search (Apollo, Clay People, or LeadMagic People Search)
3. Filter by title match and seniority
4. Target 2-5 contacts per account for multi-threading

### Phase 4: List Quality Scorecard

Grade every list across 8 dimensions before uploading to a sequencer:

| Dimension | Pass Criteria |
|---|---|
| Domain validity | All domains resolve |
| ICP fit | 80%+ match defined ICP |
| Title relevance | 70%+ match target titles |
| Email coverage | 85%+ have verified email |
| Email verification | 98%+ verified valid |
| Duplicate rate | Under 3% |
| Geographic fit | 90%+ in target regions |
| Company size fit | 80%+ in target range |

Lists scoring below 70% across dimensions should be reworked before sending.

## Output Format

Deliver a CSV with:
- Company domain, company name, industry, employee count
- Contact name, title, email, email verification status
- LinkedIn URL, source attribution
- ICP score and tier

## Quality Check

- [ ] ICP filters applied before contact enrichment
- [ ] All emails verified (verification status column populated)
- [ ] Duplicates removed (match on email + company)
- [ ] List quality scorecard completed
- [ ] Companies source-attributed
- [ ] Separate company and person tables maintained (not merged)

## Common Pitfalls

1. **Enriching before filtering.** Running $0.15-0.40/contact enrichment on
   records that fail ICP wastes 30-40% of budget. Filter first always.

2. **One giant table.** Combining company and person data in a single table
   creates duplication and makes re-enrichment impossible. Separate tables
   with domain as the join key.

3. **No list quality baseline.** Sending to an unscored list means you can't
   diagnose why reply rates are low. Score every list before launch.

4. **Stale data acceptance.** A list built 6 months ago has 12-18% decay.
   Re-verify and re-enrich before launching any campaign on old data.

5. **Single-source dependency.** One source never covers your full TAM.
   Cross-reference at least two sources and reconcile differences.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `references/cold-calling-experts-index.md` — Phone Intent + bucketing router (repo root)
- `references/joey-gilkey-bucketing.md` — Phone Intent + disposition list diagnostics (repo root)
- `../../outbound/cold-email-strategy/references/jordan-crawford-blueprint-gtm.md` — PQS pain-based segments
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **icp-scoring**: Define the ICP criteria this skill filters against
- **lead-finding**: Find individual contacts at target companies
- **lead-enrichment**: Enrich contacts after list is built
- **clay-automation**: Full Clay workflow for automated list building
- **sales-navigator-prospecting**: Morgan Ingram filter-specific Sales Nav workflow after list criteria are set

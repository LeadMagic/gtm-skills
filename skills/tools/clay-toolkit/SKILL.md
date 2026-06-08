---
name: clay-toolkit
description: >-
  Complete Clay platform toolkit — table architecture, waterfall enrichment,
  Claygent AI agent, credit optimization, CRM push, webhook webhooks, formula
  writing, and advanced Clay workflows for GTM automation. Use when building
  Clay tables, designing enrichment waterfalls, or scaling prospecting
  operations. Triggers on: "Clay toolkit", "Clay setup", "Clay waterfall",
  "Claygent", "Clay enrichment", "Clay automation".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: tools
  tags: [clay, enrichment, waterfall, prospecting, automation, claygent, data-enrichment]
  related_skills: [clay-automation, leadmagic-toolkit, waterfall-enrichment, data-enrichment-strategy, leadmagic-waterfall]
  frameworks:
    - "Clay — Waterfall enrichment platform, Claygent AI, table architecture"
    - "Clay University — Official tutorials and certification"
    - "LeadMagic API — Email finder/verifier enrichment provider on Clay"
---

# Clay Toolkit

## Overview

Clay is the operating system for data-driven GTM. It pulls from 50+ data
sources, enriches in waterfall chains, and pushes to CRM — all in a
spreadsheet-like interface. The mistake: using Clay as a glorified lookup
table instead of an enrichment engine. This skill covers advanced Clay
architecture: table design, waterfall strategy, credit optimization,
and integration patterns.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Clay — Waterfall enrichment platform, Claygent AI, table architecture.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Clay University — Official tutorials and certification.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **LeadMagic API — Email finder/verifier enrichment provider on Clay.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use

Trigger phrases: "Clay setup", "Clay waterfall", "Clay enrichment", "Claygent",
"Clay table architecture", "Clay automation", "Clay credit optimization"

## Core Concepts

### Table Architecture
- **Source Sheet:** Google Sheets, CSV, or API — where your data lives
- **Enrichment Columns:** Each column is an enrichment step
- **Waterfall Columns:** Chain multiple providers per data point
- **Formula Columns:** Transform data between enrichments
- **Output:** CRM push, webhook, or export

### Waterfall Strategy
```
Goal: Find email for a list of contacts

Column 1: LeadMagic Email Finder
  → Found? Done.
  → Not found? Fall through to...

Column 2: Apollo Email Finder
  → Found? Done.
  → Not found? Fall through to...

Column 3: ProspectingTool Email Finder
  → Found? Done.
  → Still not found? Flag for manual review.
```

### Credit Optimization
- **LeadMagic:** 1 credit = find + verify. Best accuracy.
- **Apollo:** credits per export. Good breadth.
- **Claygent:** AI-powered research agent. Use sparingly (expensive).
- **Rule:** Run cheapest/highest-accuracy provider first. Fall back to more expensive.

## Artifacts

### Standard Clay Table Template
```
COLUMNS (left to right):

1. INPUT COLUMNS:
   - First Name (text)
   - Last Name (text)
   - Company (text)
   - Domain (text or formula: clearbit domain from company)
   - LinkedIn URL (optional)

2. ENRICHMENT WATERFALL — EMAIL:
   - LeadMagic Find Email (name + company → email)
     Credit cost: 1. Confidence: High.
   - Apollo Find Email (name + company → email)
     Credit cost: 1. Confidence: Medium.
   - ProspectingTool (name + domain → email)
     Credit cost: 1. Confidence: Medium-Low.

3. VERIFICATION:
   - LeadMagic Verify Email (email → status + confidence)
     Credit cost: 1. Status: valid/invalid/risky/unknown.

4. ENRICHMENT — PERSON:
   - LeadMagic Enrich Person (email → title, company, phone, social)
     Credit cost: 2.

5. ENRICHMENT — COMPANY:
   - Clearbit Company (domain → employee_count, industry, revenue)

6. SCORING:
   - Formula: ICP Score =
     (Title matches ICP: 30) +
     (Company size 50-500: 20) +
     (Email valid: 30) +
     (Industry matches: 20)

7. OUTPUT:
   - CRM Push (HubSpot / Salesforce)
   - Google Sheets sync
   - Webhook → n8n → downstream workflows
```

### Common Clay Formulas
```javascript
// Extract domain from email
=RIGHT(Email, LEN(Email) - FIND("@", Email))

// ICP Score calculation
=SUM(
  IF(CONTAINS(Title, "VP"), 30, IF(CONTAINS(Title, "Director"), 20, 0)),
  IF(AND(Employees > 50, Employees < 500), 20, 0),
  IF(Email_Status = "valid", 30, 0),
  IF(Industry = "Technology", 20, 0)
)

// Clean company name for domain lookup
=LOWER(SUBSTITUTE(SUBSTITUTE(Company, " ", ""), ",", ""))

// Time since last enrichment (days)
=DATEDIF(Last_Enriched, TODAY(), "D")
```

## Implementation Checklist

- [ ] Source data cleaned (no duplicates, consistent formatting)
- [ ] Waterfall order optimized (highest accuracy first, cheapest per hit)
- [ ] Credit budget set per table (prevent runaway costs)
- [ ] Webhook configured for async enrichment completion
- [ ] CRM push tested with 5 records before full sync
- [ ] ICP scoring formula validated against 50 known-fit contacts

## Common Pitfalls

1. **Flat enrichment (no waterfall).** One provider. Missed contacts stay missed.
   Fix: Waterfall. LeadMagic → Apollo → fallback → manual review.
2. **Credit burn on bad data.** Enriching 10,000 contacts with bad names/domains.
   Fix: Clean data first. Deduplicate. Validate domains before enrichment.
3. **No ICP filter before CRM push.** All contacts pushed to CRM. SDR team
   overwhelmed. Fix: ICP score column. Only push score > X to CRM.


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

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- `clay-automation` — General Clay workflows
- `leadmagic-toolkit` — LeadMagic integration with Clay
- `waterfall-enrichment` — Multi-provider waterfall design
- `data-enrichment-strategy` — Enrichment architecture
---
name: lead-enrichment
description: >-
  Waterfall enrichment patterns with provider sequencing (Clay → Apollo →
  ZoomInfo → PDL → Claygent → Claude normalization). Separate company and
  person tables. Domain-based matching with confidence thresholds. Triggers
  when user needs to enrich leads, append data to contact lists, run
  enrichment waterfalls, or normalize enriched data. Run after lead-finding.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: prospecting
  tags: [enrichment, data, waterfall, normalization, clay, apollo, zoominfo]
  related_skills: [lead-finding, email-finding, contact-verification, data-enrichment-strategy, waterfall-enrichment]
  frameworks: [GTMLens 5-Layer Waterfall, Ziellab 3-Waterfall Architecture, Winning by Design Data Model]
---

# Lead Enrichment

## Overview

The most common lead enrichment failure is sending every record to every provider — paying 3x the necessary cost while introducing conflicting data that requires manual reconciliation. The non-obvious rule of enrichment is the waterfall pattern: sequence providers from cheapest to most expensive, and from broadest coverage to most specialized, with each provider only firing when the previous one returned empty or low-confidence results. This approach maximizes coverage while minimizing cost per enriched record.

This skill provides a complete waterfall enrichment methodology that chains multiple data providers in a cost-optimized sequence. It specifies separate enrichment strategies for company data (firmographics, technographics, funding, revenue) and person data (contact details, job history, social profiles), with domain-based matching as the primary join key. Confidence thresholds determine when a record is "good enough" versus when it needs the next provider in the waterfall.

The deliverables include a Waterfall Configuration (provider sequence with trigger conditions), a Company Enrichment Table schema, a Person Enrichment Table schema, Confidence Threshold Rules for data quality gating, and a Normalization Protocol for reconciling conflicting data across providers. The methodology draws from GTMLens' 5-layer enrichment waterfall and Ziellab's 3-waterfall architecture for production-grade enrichment pipelines.

## When to Use

- User says "enrich these leads" or "append data to this list" → activate this skill
- User asks "how do I set up an enrichment waterfall" or "which enrichment providers should I use" → use this skill
- User mentions "Clay enrichment," "data enrichment," "contact enrichment," "company enrichment" → this skill applies
- User has a lead list from lead-finding and needs to fill in missing data
- User is building a Clay table and needs to configure enrichment columns
- User wants to normalize data from multiple enrichment sources

Do NOT use for:
- Finding email addresses for contacts without any existing data — use email-finding
- Verifying that email addresses are valid and deliverable — use contact-verification
- High-level strategy on which providers to buy — use data-enrichment-strategy
- Setting up the overall enrichment architecture — use waterfall-enrichment for Clay-specific implementation

## Authoritative Foundations

- **GTMLens — 5-Layer Enrichment Waterfall.** The five-layer framework for enrichment data quality: Layer 1 (seed data you already have), Layer 2 (free/public sources), Layer 3 (broad-coverage paid providers), Layer 4 (specialist providers for gaps), Layer 5 (AI agent research for remaining gaps). This skill implements all five layers.

- **Ziellab — 3-Waterfall Architecture.** The pattern of running three parallel waterfalls (Company, Contact, Technographic) that feed into a unified enriched record. This skill adopts the separate-company-and-person-tables architecture.

- **Winning by Design — Data Model.** The GTM Index's Data Model component (scored 1-10) that measures how well an organization's data is instrumented. This skill raises the Data Model score by ensuring enrichment produces structured, normalized, confidence-tagged data.

- **Clay — Waterfall Enrichment Best Practices.** The Clay-native approach to enrichment waterfalls: use formula columns for conditional logic, HTTP API columns for provider calls, and AI columns (Claygent/Claude) for normalization and gap-filling.

## Prerequisites

- **Upstream skills:** lead-finding (provides the lead list to enrich). gtm-context (provides the ICP that determines what enrichment fields matter). icp-scoring (provides the dimensions to enrich against).
- **Required inputs:** A lead list with at minimum: company name, company domain, and (for person enrichment) person name and/or LinkedIn URL.
- **Optional:** API keys for enrichment providers (Apollo, ZoomInfo, PDL, Clearbit, LeadMagic). Clay account for workflow automation.
- **Optional tools:** LeadMagic Company Search and People Search APIs for enrichment with high-accuracy firmographic and contact data. LeadMagic Technographics API for technology stack enrichment.

## Step-by-Step Process

### Phase 1: Intake

Ask all questions at once:

1. Provide the lead list to enrich. What fields are already populated? What fields are missing?
2. What enrichment providers do you have access to? (Apollo, ZoomInfo, People Data Labs, Clearbit, Cognism, Lusha, Clay, LeadMagic, other.)
3. What is your budget per enriched record? (This determines how many waterfall layers to use.)
4. What enrichment fields are required vs nice-to-have? (Company: employees, revenue, industry, tech stack, funding. Person: email, phone, title, LinkedIn, seniority.)
5. Are you enriching companies, people, or both?
6. What is your target data quality threshold? (What confidence level is "good enough" for your use case?)

### Phase 2: Research

**Provider Coverage Analysis:** Before configuring the waterfall, understand each provider's coverage profile:
- Apollo: Strong on US companies, tech-forward, funded. Weak on non-US, traditional industries, very small companies.
- ZoomInfo: Broadest coverage, strongest on mid-market and enterprise. Expensive per record. Weak on very early-stage startups.
- People Data Labs (PDL): Strong on person data, especially job history and skills. Company data is derived, not primary.
- Clearbit: Strong on company firmographics and technographics. Person data is good but limited coverage.
- Cognism: Strong on EMEA/UK coverage. GDPR-compliant. Weak on US coverage.
- Lusha: Good for contact data (email, phone). Company data is thin.
- LeadMagic: High accuracy on email finding, company search, and technographics. Strong coverage across segments.

**Field Prioritization:** Not all fields are equally important. Prioritize enrichment by field criticality:
- Tier 1 (Must have for any outreach): Company name, domain, employee count, industry. Person: name, title, email.
- Tier 2 (Important for qualification): Revenue, tech stack, funding data, LinkedIn URL, phone.
- Tier 3 (Nice to have for personalization): Job history, education, skills, social profiles, news mentions.

### Phase 3: Execution

**Step 1: Schema Design**

Design separate Company and Person tables. Match on domain, not company name (names vary across providers; domains are stable).

**Company Table Schema:**
| Field | Type | Required | Source Priority |
|-------|------|----------|-----------------|
| company_domain | text | Yes | Input data |
| company_name | text | Yes | Normalized from input |
| company_legal_name | text | No | Provider data |
| employee_count | integer | Tier 1 | Provider waterfall |
| employee_count_range | text | Tier 1 | Provider waterfall |
| revenue | integer | Tier 2 | Provider waterfall |
| revenue_range | text | Tier 2 | Provider waterfall |
| industry | text | Tier 1 | Provider waterfall (standardized) |
| sub_industry | text | No | Provider waterfall |
| sic_code | text | No | Provider waterfall |
| naics_code | text | No | Provider waterfall |
| company_description | text | No | Provider waterfall |
| founded_year | integer | No | Provider waterfall |
| funding_stage | text | Tier 2 | Provider waterfall |
| funding_total | integer | Tier 2 | Provider waterfall |
| last_funding_date | date | Tier 2 | Provider waterfall |
| technologies | array | Tier 2 | LeadMagic Technographics |
| hq_city | text | No | Provider waterfall |
| hq_state | text | No | Provider waterfall |
| hq_country | text | Tier 1 | Provider waterfall |
| linkedin_url | text | Tier 2 | Provider waterfall |
| website | text | Yes | Input data |
| alexa_rank | integer | Tier 3 | Provider waterfall |
| enriched_date | date | Auto | Current timestamp |
| enrichment_source | text | Auto | Provider that supplied most data |
| confidence_score | float | Auto | Calculated |

**Person Table Schema:**
| Field | Type | Required | Source Priority |
|-------|------|----------|-----------------|
| person_id | text | Yes | Generated UUID |
| company_domain | text | Yes | Match key to company table |
| first_name | text | Yes | Input or enriched |
| last_name | text | Yes | Input or enriched |
| full_name | text | Yes | Normalized |
| title | text | Tier 1 | Provider waterfall |
| seniority | text | Tier 1 | Provider waterfall |
| department | text | Tier 1 | Provider waterfall |
| email | text | Tier 1 | LeadMagic Email Finder |
| email_status | text | Tier 1 | LeadMagic Email Validation |
| phone | text | Tier 2 | Provider waterfall |
| linkedin_url | text | Yes | Input or enriched |
| location | text | Tier 2 | Provider waterfall |
| company_name | text | Yes | From company table |
| job_history | array | Tier 3 | PDL / Provider waterfall |
| education | array | Tier 3 | Provider waterfall |
| skills | array | Tier 3 | Provider waterfall |
| enriched_date | date | Auto | Current timestamp |
| enrichment_source | text | Auto | Provider that supplied most data |
| confidence_score | float | Auto | Calculated |

**Step 2: Waterfall Configuration**

Configure the enrichment waterfall in this sequence. For each provider, specify the trigger condition (when it fires) and the fields it populates.

**Company Enrichment Waterfall:**

```
Layer 1: Seed Data (no cost)
├── Input: company website/domain
├── Extract: domain normalization, basic URL parsing
└── Trigger: Always runs first

Layer 2: Public/Free Sources (no cost)
├── Clearbit Reveal (free tier) or similar
├── Extract: basic firmographics from domain
└── Trigger: Always runs after seed data

Layer 3: Broad-Coverage Provider (cost per record)
├── Apollo People Enrichment OR ZoomInfo
├── Extract: employee count, revenue, industry, description, location
└── Trigger: ENRICH when employee_count IS NULL OR industry IS NULL
└── Cost: $0.01-$0.05 per record

Layer 4: Specialist Provider (higher cost)
├── LeadMagic Company Search OR Clearbit Pro
├── Extract: fill remaining Tier 1 gaps, add technographics
└── Trigger: ENRICH when employee_count IS NULL OR industry IS NULL
└── Cost: $0.02-$0.10 per record

Layer 5: AI/Normalization (computation cost)
├── Claygent OR Claude
├── Extract: normalize company descriptions, standardize industries, fill description gaps
└── Trigger: ENRICH when company_description IS NULL OR industry IS NULL
└── Cost: $0.01-$0.05 per record
```

**Person Enrichment Waterfall:**

```
Layer 1: Seed Data (no cost)
├── Input: person name, company domain, LinkedIn URL
├── Extract: name parsing (first/last), domain matching
└── Trigger: Always runs first

Layer 2: Public/Free Sources (no cost)
├── LinkedIn URL parsing, public profile data
├── Extract: title, company, location from LinkedIn
└── Trigger: Always runs after seed data

Layer 3: Broad-Coverage Provider (cost per record)
├── Apollo People Search OR ZoomInfo People
├── Extract: title, seniority, department, phone
└── Trigger: ENRICH when title IS NULL OR seniority IS NULL
└── Cost: $0.02-$0.08 per record

Layer 4: Email Finding (cost per record)
├── LeadMagic Email Finder OR Hunter OR Findymail
├── Extract: email, email_status
└── Trigger: ENRICH when email IS NULL
└── Cost: $0.01-$0.05 per record

Layer 5: Deep Person Enrichment (higher cost)
├── People Data Labs (PDL) Person Enrichment
├── Extract: job history, education, skills
└── Trigger: ENRICH when job_history IS NULL (and Tier 1 records only)
└── Cost: $0.05-$0.15 per record

Layer 6: AI/Normalization (computation cost)
├── Claude normalization
├── Extract: standardize titles, normalize departments, fill gaps
└── Trigger: ENRICH when title IS NULL OR department IS NULL
└── Cost: $0.01-$0.03 per record
```

**Step 3: Confidence Threshold Rules**

Assign confidence scores to enriched fields based on provider and data freshness:

- **Confidence = 1.0:** Manually verified, or seed data from CRM.
- **Confidence = 0.8-0.9:** Direct API response with high provider confidence. LeadMagic direct match. ZoomInfo verified record.
- **Confidence = 0.6-0.7:** API response with medium confidence. Provider inferred or modeled data. Apollo modeled employee count.
- **Confidence = 0.4-0.5:** AI-normalized or inferred data. Claude normalization output. Domain-parsed data.
- **Confidence = 0.1-0.3:** Heuristic or guessed data. PDL derived data. Data older than 180 days.

**Confidence Threshold Actions:**
- Overall confidence ≥ 0.8: Record is enrichment-complete. No further providers needed.
- Overall confidence 0.6-0.79: Record is usable but could be improved if capacity allows.
- Overall confidence < 0.6: Record needs the next provider in the waterfall.
- Overall confidence < 0.4: Flag for manual review or discard.

**Step 4: Normalization Protocol**

When multiple providers return data for the same field, resolve conflicts:

**Company Name Normalization:**
- Strip legal suffixes: "Inc.", "Inc", "Corporation", "Corp.", "Corp", "LLC", "Ltd.", "Ltd", "Limited", "GmbH", "S.A.", "AG", "B.V.", "Pty Ltd"
- Normalize: "Corp" → "Corporation" (standardize to full form if preferred)
- Longest non-empty name wins (more specific is usually more correct)
- Exception: if one name matches the domain, prefer it

**Employee Count Normalization:**
- Use the most recent data point (check enriched_date per source)
- If providers disagree by <20%, use the average
- If providers disagree by >20%, flag for review and use the more reputable provider
- Provider reputation ranking: LeadMagic/ZoomInfo > Apollo > Clearbit > PDL

**Industry Normalization:**
- Map all provider industry taxonomies to a standard taxonomy (NAICS or custom)
- If providers disagree, use the industry with higher provider confidence
- AI normalization (Claude) is the tiebreaker for ambiguous cases

**Title and Seniority Normalization:**
- Map variant titles to standard roles: "VP of Engineering" == "VP Engineering" == "Head of Engineering"
- Map titles to seniority tiers: C-level, VP, Director, Manager, Individual Contributor
- Use the most recent title (check job history dates)
- Use AI normalization for ambiguous titles: "Growth Hacker" → "Marketing, Individual Contributor"

**Step 5: Quality Gates**

Before releasing enriched data to downstream systems:
- Required field completeness: All Tier 1 fields must be populated or explicitly NULL
- Domain validity: Company domain must be valid (no typos, no personal email domains for company matches)
- Cross-table consistency: Person's company_name must match Company table's company_name
- No test data: Filter out records with test names (e.g., "Test User", "John Doe at Acme Inc")
- Duplicate check: No duplicate person records (same person_id) or company records (same domain)

### Phase 4: Delivery

Deliver the enriched data as two structured tables (Company and Person) with:
1. Complete schema documentation
2. Waterfall configuration that produced the data
3. Per-record confidence scores and source attribution
4. Normalization log showing how conflicts were resolved
5. Quality gate pass/fail report
6. Cost breakdown: total cost, cost per record, cost by provider

## Output Format

```markdown
# Lead Enrichment Report

## Enrichment Summary
- Records enriched (companies): [#] of [#] input = [%] coverage
- Records enriched (people): [#] of [#] input = [%] coverage
- Average company confidence: [0.XX]
- Average person confidence: [0.XX]
- Total enrichment cost: $[X.XX]
- Cost per record: $[X.XX]

---

## Waterfall Configuration

### Company Waterfall
| Layer | Provider | Trigger Condition | Fields Populated | Cost/Record | Records Processed |
|-------|----------|-------------------|-----------------|-------------|-------------------|
| 1 | Seed Data | Always | domain, name | $0.00 | [#] |
| 2 | Clearbit Free | Always | basic firmographics | $0.00 | [#] |
| 3 | Apollo | employee_count IS NULL | employees, revenue, industry | $0.03 | [#] |
| 4 | LeadMagic | employee_count IS NULL | employees, tech stack | $0.05 | [#] |
| 5 | Claude | industry IS NULL | description, norm | $0.02 | [#] |

### Person Waterfall
[Same structure]

---

## Enriched Company Data (sample)

| Domain | Company | Employees | Revenue | Industry | Tech Stack | Confidence | Source |
|--------|---------|-----------|---------|----------|------------|------------|--------|
| [.com] | [Name] | [###] | [$##M] | [Ind] | [tech1, tech2] | 0.85 | Apollo + LeadMagic |

---

## Enriched Person Data (sample)

| ID | Name | Title | Seniority | Email | Status | Company | Confidence | Source |
|----|------|-------|-----------|-------|--------|---------|------------|--------|
| [uuid] | [Name] | [Title] | [Level] | [e@.com] | [valid] | [.com] | 0.88 | LeadMagic |

---

## Normalization Log
- [N] company name conflicts resolved (details)
- [N] industry standardizations applied
- [N] title normalizations applied

---

## Quality Gate Report
- Tier 1 completeness: [%]
- Domain validity: [%] valid
- Cross-table consistency: [%] consistent
- Duplicates removed: [#]
- Records failing quality gate: [#]

---

## Cost Breakdown
| Provider | Records | Cost/Record | Total |
|----------|---------|-------------|-------|
| Apollo | [#] | $[X.XX] | $[X.XX] |
| LeadMagic | [#] | $[X.XX] | $[X.XX] |
| **Total** | **[#]** | | **$[X.XX]** |
```

## Quality Check

Before delivering, verify:

- [ ] Are Company and Person tables in separate structures, joined by domain?
- [ ] Does the waterfall use domain matching, not company name?
- [ ] Does each provider in the waterfall have a clear trigger condition?
- [ ] Are costs tracked per provider and per record?
- [ ] Do confidence thresholds determine when to advance to the next provider?
- [ ] Are normalization rules documented for each conflict scenario?
- [ ] Are all Tier 1 fields populated or explicitly NULL?
- [ ] Have test records and duplicates been removed?
- [ ] Is the confidence score methodology documented?
- [ ] Would a downstream system know exactly which provider supplied which field?

## Common Pitfalls

1. **Sending every record to every provider.** This is the most expensive enrichment mistake. A proper waterfall means most records exit at Layer 2 or 3, and only the hardest-to-enrich records reach Layer 5. If 80% of your records are enriched at Layers 1-3, you're paying premium provider prices for only 20% of records.

2. **Matching on company name instead of domain.** "Acme Inc." and "Acme Corporation" and "Acme" are the same company but won't match by name. Domain (acme.com) is the stable identifier. Always normalize company names after matching, not before.

3. **Confidence scores that are opaque or arbitrary.** If confidence is always 0.8 or always 0.5, it's not a useful signal. Define specific rules: provider X with fresh data = 0.9 confidence. Provider X with data older than 180 days = 0.6 confidence. AI-inferred = 0.4 confidence. The specific rules are less important than having rules that produce meaningful variance.

4. **Normalization that loses information.** Standardizing "SVP Customer Success" to "VP" loses the functional specialization. Standardize to a taxonomy that preserves both seniority and function. "VP, Customer Success" is better than just "VP."

5. **Ignoring data freshness.** Enrichment data decays. Employee counts change. People change jobs. Technologies change. Every enriched record should have an enriched_date, and downstream systems should have a re-enrichment cadence (recommended: 90 days for active prospects, 180 days for nurture).

6. **Same-waferfall for companies and people.** Company enrichment needs different providers and different fields than person enrichment. The two waterfalls should be configured independently, even if they share some infrastructure.

7. **Quality gates that are too permissive or too strict.** Gates that let everything through defeat the purpose. Gates that block 50% of records create a bottleneck. Target: <5% of records failing quality gates in a mature pipeline. More than 10% indicates a problem in the enrichment waterfall, not in the gate.

8. **Not tracking cost per provider.** Without per-provider cost tracking, you can't optimize the waterfall over time. A provider that costs 3x more but enriches only 2% more records should be removed or moved to a later layer. Cost optimization is continuous.

## Related Skills

- **lead-finding**: Run before this skill. Provides the raw lead list to enrich.

- **email-finding**: Use as a provider in the person enrichment waterfall for email discovery.

- **contact-verification**: Run after this skill. Verifies enriched email addresses are deliverable.

- **data-enrichment-strategy**: Run before this skill for high-level provider selection. This skill is the implementation.

- **waterfall-enrichment**: Run for Clay-specific waterfall implementation. This skill provides the methodology independent of Clay.

- **list-building**: Run after this skill. Uses enriched data to build production-ready prospecting lists.

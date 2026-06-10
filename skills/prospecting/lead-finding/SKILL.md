---
name: lead-finding
description: >-
  Find qualified prospects and decision-makers from ICP criteria using public research, company signals, role mapping, and source confidence. Produces a prospect list spec, search strategy, qualification rubric, source log, and QA checklist. Use when building target lists or finding buyers at named accounts.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: prospecting
  tags: [lead-generation, prospecting, list-building, sourcing, discovery]
  related_skills: [gtm-context, icp-scoring, lead-enrichment, list-building, signal-scoring, sales-navigator-prospecting]
  frameworks: [Winning by Design SPICED, Force Management MEDDICC, Gartner Buying Committee Research]
---
# Lead Finding

## Overview

The most common lead-finding mistake is relying on a single source — usually a B2B database like Apollo or ZoomInfo — and accepting whatever it returns as the universe of addressable accounts. Single-source lead discovery produces lists with systematic gaps: entire categories of companies that don't appear in one database but dominate another. The non-obvious rule is that high-quality lead discovery requires multiple, complementary sources, each with its own coverage bias, used in combination to triangulate the full universe of ICP-matching companies.

This skill provides a multi-source lead discovery methodology spanning eight source categories: B2B contact databases (Apollo, Sales Navigator), professional networks (LinkedIn Sales Navigator advanced search), code repositories and technical communities (GitHub, Stack Overflow, DevPost), funding and company databases (Crunchbase, PitchBook, Tracxn), job boards (LinkedIn Jobs, Indeed, Wellfound), conference and event lists (event sponsor/exhibitor lists, speaker rosters), industry directories and associations, and vertical-specific sources (G2/Capterra for SaaS, BuiltWith for technographics, SaaStr/Product Hunt for early-stage).

For each source, the skill provides search templates, data extraction patterns, and guidance on which sources are most productive for specific verticals (SaaS, fintech, healthcare, manufacturing, e-commerce, professional services). The output is a deduplicated, prioritized lead list with source provenance, ready for enrichment and scoring.

## When to Use

- User says "find leads" or "build a prospect list" → activate this skill
- User asks "where can I find companies that match our ICP" → use this skill
- User mentions "lead sourcing," "account discovery," or "prospecting list" → this skill applies
- User has an ICP definition but no leads to work with
- User's current lead source has dried up and they need new channels
- Before running lead-enrichment or list-building

Do NOT use for:
- Enriching existing leads with additional data — use lead-enrichment
- Finding email addresses for known contacts — use email-finding
- Building scored, prioritized lists in Clay — use list-building
- Finding leads based on real-time signals — use signal-scoring

## Authoritative Foundations

- **Winning by Design — SPICED Framework.** The Situation component maps to lead sourcing: finding companies in the right "situation" (industry, size, stage) that is the starting point for SPICED qualification. The Decision component maps to identifying the right contacts within sourced companies.

- **Force Management — MEDDICC.** The Economic Buyer, Champion, and Decision Process elements guide which contacts to find within sourced companies. Finding a company is not enough — you need to find the specific personas who can champion, influence, and authorize a purchase.

- **Gartner — Buying Committee Research.** The finding that B2B buying committees average 6-10 decision makers informs the contact discovery strategy. Finding one contact at a company is insufficient — the skill targets identification of 2-4 key personas per account.

- **ColdIQ / Alex Hoar — Multi-Source Prospecting.** The methodology of combining Sales Navigator, job boards, funding data, and conference lists to build comprehensive prospect lists rather than relying on a single database.

## Prerequisites

- **Upstream skills:** gtm-context (provides ICP definition, target industries, company size, geography). icp-scoring (provides scoring model to prioritize discovered leads).
- **Required inputs:** ICP definition with specific firmographic criteria (industries, company size, geography), target personas with job titles.
- **Optional:** Access to Apollo, LinkedIn Sales Navigator, Crunchbase, or equivalent tools. API keys for LeadMagic People Search and Role Finder for enhanced contact discovery.
- **Optional tools:** LeadMagic People Search API to discover contacts at target companies. LeadMagic Role Finder API to identify specific personas by function and seniority.

## Step-by-Step Process

### Phase 1: Intake

Ask all questions at once:

1. What is your ICP definition? (Industries, company size range in employees, revenue range, geography, any technographic requirements.)
2. What are the 2-4 target personas you need to find at each company? (Job titles, department, seniority level.)
3. What lead sources have you used before, and what were the results? (Coverage, quality, conversion rates.)
4. What is your target list size? (How many unique companies do you want to find?)
5. Do you have access to: Apollo, LinkedIn Sales Navigator, Crunchbase, or equivalent tools?
6. What is your target industry? (This determines which vertical-specific sources to prioritize.)
7. Are there any companies or types of companies you explicitly want to exclude?

### Phase 2: Research

**Source Prioritization by Vertical:** Different verticals have different source strengths. Prioritize sources based on the target industry:

**SaaS / Technology:**
- Primary: LinkedIn Sales Navigator (company search by industry + tech stack), Apollo (CSV export with tech filters), Crunchbase (funding + category), GitHub (open-source contributors and enterprise users), BuiltWith (technology stack detection)
- Secondary: G2/Capterra (reviewing companies — they're evaluating your category), Product Hunt (early-stage companies launching products), job boards (hiring signals)
- Tertiary: Conference lists (SaaStr, SaaSter, TechCrunch Disrupt), industry directories

**Fintech / Financial Services:**
- Primary: Crunchbase/PitchBook (funding data), LinkedIn Sales Navigator (industry + company size), regulatory filings (SEC EDGAR for public companies)
- Secondary: Job boards (compliance, engineering hires), conference lists (Money20/20, Finovate)
- Tertiary: Industry associations, partner directories (Plaid, Stripe ecosystem)

**Healthcare / HealthTech:**
- Primary: LinkedIn Sales Navigator, Crunchbase (healthcare category), FDA/regulatory databases, hospital/health system directories
- Secondary: Conference lists (HIMSS, HLTH, JPMorgan Healthcare), job boards
- Tertiary: Industry associations, academic medical center lists

**Manufacturing / Industrial:**
- Primary: LinkedIn Sales Navigator (company size + industry), industry directories (ThomasNet, IndustryNet), trade association member lists
- Secondary: Job boards (engineering, operations hires), conference lists (IMTS, Hannover Messe)
- Tertiary: BuiltWith (technology stack), government contractor databases

**E-commerce / Retail:**
- Primary: BuiltWith (e-commerce platform detection), LinkedIn Sales Navigator, Crunchbase, Shopify/Shopify Plus partner directory
- Secondary: Job boards (marketing, e-commerce hires), conference lists (Shopify Unite, NRF)
- Tertiary: SimilarWeb (traffic estimation for retail sites)

**Professional Services:**
- Primary: LinkedIn Sales Navigator (service category filters), Clutch.co / agency directories, industry association member lists
- Secondary: Job boards (client-facing role hires), conference lists
- Tertiary: Crunchbase, GitHub (for technical consultancies)

### Phase 3: Execution

Execute multi-source discovery following this sequence:

**Step 1: B2B Database Export (Apollo or equivalent)**

If you have Apollo access:
- Use the Company Search with ICP filters (industry, employee count, revenue, location, technologies)
- Export the full result set as CSV
- Note: Apollo has coverage biases — it tends to overrepresent US-based, funded, tech-forward companies. This is your starting point, not your complete list.

Apollo search template per persona:
- Title: [Persona title variants, comma-separated]
- Company Industry: [Target industries]
- Company Size: [Min]-[Max] employees
- Company Location: [Target geography]
- Seniority: [Director, VP, C-level as applicable]

**Step 2: LinkedIn Sales Navigator Advanced Search**

Sales Navigator provides company and people search with filters not available in regular LinkedIn:

Company search template:
- Industry: [Target industries]
- Company Size: [Min]-[Max] employees
- Headquarters Location: [Target geography]
- Annual Revenue: [Target range]
- Technologies Used: [Key technologies if ICP includes technographics]

People search template per persona:
- Title: [Persona title variants]
- Function: [Department]
- Seniority Level: [Target seniority]
- Company Industry: [Target industries]
- Company Size: [Target range]
- Geography: [Target locations]

Export results using Sales Navigator's list-building feature. Note: LinkedIn terms of service prohibit automated scraping. Use native export features only.

**Step 3: GitHub and Technical Communities (for technical ICPs)**

For companies where technology stack matters:
- Search GitHub for organizations using relevant technologies (e.g., `topic:kubernetes org:`, search for companies by their GitHub org pages)
- Use Stack Overflow's company pages and job listings
- Search DevPost for hackathon participants building in your problem space
- Use npm, PyPI, or package registries to identify companies maintaining relevant packages

**Step 4: Crunchbase and Funding Databases**

For growth-stage and funded companies:
- Search Crunchbase by category, funding stage, location, and employee count
- Filter for companies that recently raised funding (funding is a buying signal — use signal-scoring to evaluate further)
- Export company data including funding details, key people, and website

**Step 5: Job Boards**

Hiring signals are strong ICP indicators. Search:
- LinkedIn Jobs: [Target titles] at companies in [Target industries]
- Indeed: Same filters, different coverage
- Wellfound (AngelList): For startup/tech companies
- Built In: For tech hubs (Built In NYC, Built In SF, etc.)
- Industry-specific job boards: Stack Overflow Jobs (tech), Behance/Dribbble (design)

Search for roles that indicate the company needs your product:
- Hiring for the role your product serves → they have the problem you solve
- Hiring for roles that manage the budget your product draws from → they have funding
- Hiring for growth roles → they're scaling and likely re-evaluating tools

**Step 6: Conference and Event Lists**

Conference sponsor, exhibitor, and speaker lists are high-quality sources:
- Identify 5-10 relevant industry conferences
- Collect sponsor/exhibitor lists from conference websites
- Collect speaker rosters (speakers' companies are engaged in the community)
- Add attendee lists if available (some conferences publish these)
- These companies are actively engaged in the ecosystem and have budget for industry participation

**Step 7: Industry Directories and Associations**

- Industry-specific directories (e.g., AI 50, Cloud 100, Inc 5000, Deloitte Fast 500)
- Trade association member directories
- Chamber of Commerce business lists (by region)
- Government contractor databases (for companies selling to government)

**Step 8: Vertical-Specific Sources**

- **G2/Capterra:** Companies actively reviewing in your category — they're in-market
- **Product Hunt:** Recently launched products — early-stage companies likely to be tool adopters
- **BuiltWith / Wappalyzer:** Companies using specific technologies
- **Partner ecosystems:** Companies using complementary products (e.g., if you integrate with Salesforce, find Salesforce customers)
- **SEC EDGAR:** Public company filings — identify customers, suppliers, and partners

**Step 9: Deduplication and Merge**

After collecting from all sources:
- Normalize company names (strip legal suffixes: Inc, LLC, Ltd, Corp)
- Deduplicate on domain name (the most stable unique identifier)
- For companies found in multiple sources, merge records and track source provenance
- Flag companies found in only one source (may need additional verification)
- Cross-reference against exclusion lists

**Step 10: Initial Prioritization**

Apply a lightweight prioritization before full enrichment:
- Tier 1: Found in 3+ sources, recent funding or hiring activity
- Tier 2: Found in 2 sources, matches core ICP criteria
- Tier 3: Found in 1 source, matches core ICP criteria but may be a database artifact

### Phase 4: Delivery

Deliver a structured lead list with:
1. Company name (normalized)
2. Domain
3. Industry
4. Employee count (range)
5. Revenue (range if available)
6. Location (HQ city/state/country)
7. Source provenance (which sources found this company)
8. Source count (number of sources)
9. Key contacts found (name, title, LinkedIn URL if available)
10. Prioritization tier
11. Notes (funding events, hiring signals, conference participation)

Also deliver a Source Performance Summary showing how many unique companies each source contributed (accounting for overlap) and recommendations for which sources to prioritize in future lead-finding cycles.

## Output Format

```markdown
# Lead Discovery Report: [Company Name]

## Discovery Summary
- Total unique companies discovered: [#]
- Sources used: [#]
- Date range: [Start - End]

## Source Performance

| Source | Companies Found | Unique to This Source | Overlap % |
|--------|----------------|----------------------|-----------|
| Apollo | [#] | [#] | [%] |
| Sales Navigator | [#] | [#] | [%] |
| Crunchbase | [#] | [#] | [%] |
| Job Boards | [#] | [#] | [%] |
| Conferences | [#] | [#] | [%] |
| GitHub | [#] | [#] | [%] |
| [Other] | [#] | [#] | [%] |

---

## Lead List

| # | Company | Domain | Industry | Size | Location | Sources | Contacts | Tier |
|---|---------|--------|----------|------|----------|---------|----------|------|
| 1 | [Name] | [.com] | [Ind] | [# emp] | [City, ST] | [3 sources] | [2 contacts] | 1 |
| 2 | [Name] | [.com] | [Ind] | [# emp] | [City, ST] | [2 sources] | [1 contact] | 2 |

[Full lead list — recommend CSV export for large lists]

---

## Source-Specific Exports

### Apollo Results ([#] companies)
[Summary table]

### Sales Navigator Results ([#] companies)
[Summary table]

### Crunchbase Results ([#] companies)
[Summary table]

### [Additional sources]

---

## Recommendations
- Best sources for future cycles: [Ranked list based on unique contribution, quality, and cost]
- Sources to deprioritize: [Low-unique-contribution sources]
- Coverage gaps: [ICP segments not well represented in discovered leads]
- Next step: Run lead-enrichment on Tier 1 and Tier 2 leads
```

## Quality Check

Before delivering, verify:

- [ ] Were at least 3 distinct source categories used?
- [ ] Is every company deduplicated (no duplicate entries)?
- [ ] Are company names normalized (legal suffixes stripped)?
- [ ] Does each lead include source provenance (which sources found it)?
- [ ] Are contacts associated with the correct company?
- [ ] Do prioritization tiers follow the documented criteria?
- [ ] Are exclusion lists applied (no excluded industries or companies)?
- [ ] Is the source performance analysis actionable (sources ranked by unique contribution)?
- [ ] Are coverage gaps explicitly identified?
- [ ] Is the output format ready for import into the next skill (lead-enrichment)?

## Common Pitfalls

1. **Single-source dependency.** Relying on Apollo or ZoomInfo alone produces systematic coverage gaps. Apollo underrepresents non-US, non-funded, and traditional-industry companies. Sales Navigator underrepresents very small companies. Crunchbase only covers funded companies. Multi-source is not optional — it's the difference between seeing 60% of your addressable market and seeing 90%+.

2. **Using the same search criteria across all sources.** Each source has its own taxonomy and filters. "Manufacturing" in Apollo is not the same as "Manufacturing" in Sales Navigator. Adapt search criteria to each source's specific categorization system. Test and calibrate.

3. **Finding companies but not contacts.** A list of companies without contacts is a research artifact, not a prospecting list. Every company in the lead list should have at least contact count and, for Tier 1 leads, specific contact names and titles. Use the persona definitions from ICP to guide contact discovery.

4. **Accepting database coverage as reality.** If Apollo returns 500 companies matching your ICP in the US, there are almost certainly more than 500. The database return count is a lower bound, not the actual market size. Use the coverage gaps section to identify where additional sources might surface more leads.

5. **Skipping source provenance tracking.** When a lead turns out to be high-quality (or low-quality), knowing which source it came from is essential for optimizing future lead-finding cycles. Without provenance data, you can't improve your sourcing strategy.

6. **Prioritizing volume over quality.** A list of 5,000 poorly-matched leads is less valuable than 500 precisely-matched leads. Apply ICP criteria aggressively during discovery, not after. It's better to surface fewer, better-matched companies than to dump everything into enrichment.

7. **Neglecting vertical-specific sources.** The B2B databases cover broad markets well but specific verticals poorly. Healthcare companies are better found through hospital directories than Apollo. E-commerce companies are better found through BuiltWith. Always include at least one vertical-specific source.

8. **Job board scraping that produces stale data.** Job postings expire. Conference lists age out. Source data has a half-life. Track the date of data collection per source and flag leads from sources where the data is more than 90 days old for re-verification.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **gtm-context**: Run before this skill. Provides the ICP definition that drives search criteria.

- **icp-scoring**: Run before this skill. Provides the scoring model to prioritize discovered leads.

- **lead-enrichment**: Run after this skill. Takes the discovered lead list and enriches each company and contact with additional data.

- **signal-scoring**: Run after this skill. Scores discovered leads on dynamic signals (hiring, funding, tech stack, intent) to identify active buyers.

- **list-building**: Run after lead-enrichment. Builds production-ready prospecting lists in Clay with enrichment and verification.

- **email-finding**: Run after lead-enrichment. Discovers email addresses for the contacts found during lead discovery.

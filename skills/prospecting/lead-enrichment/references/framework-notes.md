# Lead Enrichment — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- **DAMA-DMBOK Data Quality Dimensions**
- **Ziellab 3-Waterfall Architecture**
- **Winning by Design Data Model**

## Authoritative foundations

- **DAMA-DMBOK — Data Quality Dimensions.** Use accuracy, completeness, consistency, timeliness, uniqueness, validity, and lineage as the quality model for enrichment waterfalls and provider arbitration.

- **Ziellab — 3-Waterfall Architecture.** The pattern of running three parallel waterfalls (Company, Contact, Technographic) that feed into a unified enriched record. This skill adopts the separate-company-and-person-tables architecture.

- **Winning by Design — Data Model.** The GTM Index's Data Model component (scored 1-10) that measures how well an organization's data is instrumented. This skill raises the Data Model score by ensuring enrichment produces structured, normalized, confidence-tagged data.

- **Clay — Waterfall Enrichment Best Practices.** The Clay-native approach to enrichment waterfalls: use formula columns for conditional logic, HTTP API columns for provider calls, and AI columns (Claygent/Claude) for normalization and gap-filling.

## Process phases

- Phase 1
- Phase 2
- Phase 3
- Phase 4

## Key reference tables

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

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |

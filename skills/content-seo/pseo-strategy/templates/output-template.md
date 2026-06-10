# Programmatic SEO Strategy

## Executive Summary
[2–3 sentences: pSEO goal, primary template pattern, pipeline KPI — not page count]

## Context
- Company / product:
- ICP / segment:
- Owner:
- Date:

## Pattern Selection (Ahrefs + playbook §5)

| Pattern | Variables | Est. pages | Search validation | Decision |
|---|---|---:|---|---|
| [Category] for [Industry] | | | SparkToro / Ahrefs volume | Go / No-go |
| [Integration] + [Product] | | | | |
| [Tool] vs [Tool] | | | | |

**Rejected patterns:** [List invalid/near-duplicate patterns with reason]

## Data Source Inventory

| Field / data point | Source | Refresh cadence | Verification method |
|---|---|---|---|
| | Internal product data | | |
| | API / directory | | |
| | Public dataset | | |

## Template Design

### Dynamic fields
| Variable | Example | Conditional rules |
|---|---|---|
| `{industry}` | Healthcare | If healthcare → mention HIPAA |
| `{integration}` | Salesforce | Real screenshot required |

### Static blocks
- Product description + CTA
- Methodology / how-it-works
- Related integrations cluster links

### Quality gates
- [ ] Min 500 words per indexed page
- [ ] Min 3 unique data points per page
- [ ] Content similarity check <80% vs siblings
- [ ] Product-Led tie (Schwartz): capability mapped per template

## Indexation Rules

| URL class | Index | Canonical | Notes |
|---|---|---|---|
| High-intent + unique data | Yes | Self | |
| Low volume / thin | No | — | |
| Variant of primary | No | Primary URL | |

**Rollout:** 10 pages → 2-week monitor → 50 → scale

## Internal Linking Plan
- Each pSEO page → pillar hub + product page (3–5 contextual links)
- Cross-link related templates (integration ↔ industry)

## Measurement Dashboard

| Metric | Baseline | 90-day target |
|---|---|---|
| Indexed pages ranking (top 50) | | |
| Organic signups from pSEO URLs | | |
| Organic pipeline $ (UTM + self-reported) | | |
| Thin-content / deindex incidents | 0 | 0 |

## Frameworks Applied
- Eli Schwartz — Product-Led SEO (product tie per template)
- Ahrefs — programmatic patterns + thin-content gate
- Rand Fishkin — SparkToro validation before scale
- Pattern 25: `using-gtm-skills` → B2B SEO Stack

## Quality Check
- [ ] Every indexed template has unique value block (150+ words)
- [ ] No city/name-swap-only pages
- [ ] Human spot-check process defined (10% sample)
- [ ] Named frameworks cited for key decisions

## Next Steps
1.
2.
3.

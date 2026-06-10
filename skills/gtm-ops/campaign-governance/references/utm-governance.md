# UTM Governance

## Required parameters

| Parameter | Rule | Example |
|---|---|---|
| `utm_source` | Approved list only | `linkedin`, `google`, `newsletter` |
| `utm_medium` | Channel type | `paid_social`, `email`, `cpc` |
| `utm_campaign` | Matches naming convention | `2026-q3-enterprise-linkedin-casestudy-a` |
| `utm_content` | Variant for A/B | `hero-a`, `cta-b` |
| `utm_term` | Paid search only | `b2b+enrichment` |

## Hard rules

1. All lowercase; underscores not hyphens in values
2. No manual URL building — use UTM builder tool
3. Every paid link must have full UTM set
4. Organic links should have UTMs where trackable

## Approved source list (maintain in CRM)

| utm_source | Owner | Notes |
|---|---|---|
| linkedin | Demand gen | Paid + organic tagged separately in medium |
| google | Paid search | Requires utm_term |
| email | Lifecycle | HubSpot/CRM sends |
| partner_[name] | Partnerships | One row per partner |
| influencer_[creator] | Marketing | Per-creator landing pages; `utm_medium=influencer` |

## Quarterly audit

- Crawl active landing pages for UTM consistency
- Export ad account URLs — flag missing/malformed
- Merge duplicate `utm_campaign` values in warehouse

Spend caps → `gtm-spend-management` · Attribution → `attribution`

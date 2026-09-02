# Technical SEO Audit — Framework Notes

## Current source-of-truth rules

| Area | Rule | Primary source |
|---|---|---|
| Eligibility | Search Essentials compliance is necessary context, not a guarantee of crawling, indexing, or ranking | Google Search Essentials |
| Crawl control | `robots.txt` manages crawler access and is not a reliable deindexing instruction | Google Search Central robots guidance |
| Index control | Use `noindex`, `X-Robots-Tag`, authentication, or removal according to the resource and goal | Google Search Central robots meta guidance |
| Canonicalization | Redirects and `rel=canonical` are strong signals; sitemap inclusion is weaker | Google canonicalization guidance |
| Sitemaps | Include absolute preferred canonical URLs; split files above 50,000 URLs or 50 MB uncompressed | Google sitemap guidance |
| Structured data | Markup must be accurate, visible, and feature-eligible; valid markup does not guarantee a rich result | Google structured data guidelines |

## Core Web Vitals

Classify field performance at the 75th percentile for mobile and desktop when possible:

| Metric | Good | Poor |
|---|---:|---:|
| Largest Contentful Paint | ≤ 2.5 s | > 4.0 s |
| Interaction to Next Paint | ≤ 200 ms | > 500 ms |
| Cumulative Layout Shift | ≤ 0.1 | > 0.25 |

Treat lab tools as diagnostic. Do not merge lab and field measurements into one unlabeled number.

## Evidence hierarchy

1. Search Console URL Inspection, Page Indexing, sitemap, enhancement, and field-vitals reports.
2. Live HTTP response and rendered DOM from representative URLs.
3. Server/CDN logs and deployment configuration.
4. Crawler and lab-tool reports.
5. Inference, clearly labeled when higher-grade evidence is unavailable.

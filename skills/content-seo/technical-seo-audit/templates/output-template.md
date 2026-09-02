# Technical SEO Audit — [Site]

## Audit metadata

- Production origin: [URL]
- Scope and page types: [scope]
- Audit date: [YYYY-MM-DD]
- Search Console access: [yes / no]
- Crawl limits: [rate and boundaries]

## Executive status

[State the first broken search boundary, affected valuable pages, confidence, and evidence limits.]

## Crawl and index funnel

| Page type | Known URLs | Crawlable | Indexable | Canonical | Indexed | Evidence source |
|---|---:|---:|---:|---:|---:|---|
| [type] | [count] | [count] | [count] | [count] | [count] | [source] |

## Issue register

| Priority | Boundary | Issue | Example URL | Evidence | Affected URLs | Fix | Owner |
|---|---|---|---|---|---:|---|---|
| [P0-P3] | [crawl / render / index / canonical / performance] | [issue] | [URL] | [reproduction] | [count] | [fix] | [owner] |

## Canonical signal matrix

| Example URL | Status/redirect | Declared canonical | Sitemap URL | Internal-link target | Search-selected canonical | Conflict |
|---|---|---|---|---|---|---|
| [URL] | [status] | [URL] | [URL] | [URL] | [URL] | [finding] |

## Rendered metadata and structured data

| Template | Raw vs rendered delta | Metadata issue | Schema type | Validation evidence | Action |
|---|---|---|---|---|---|
| [template] | [delta] | [issue] | [type] | [result] | [action] |

## Core Web Vitals

| Template/device | Evidence type | LCP p75 | INP p75 | CLS p75 | Status | Diagnostic lead |
|---|---|---:|---:|---:|---|---|
| [template/device] | [field / lab] | [ms] | [ms] | [score] | [good / needs improvement / poor] | [cause] |

## Prioritized remediation backlog

| Priority | Change | Business impact | Confidence | Effort | Dependency | Verification case |
|---|---|---|---|---|---|---|
| [P0-P3] | [change] | [impact] | [high/medium/low] | [size] | [dependency] | [test] |

## Release verification and monitoring

1. Pre-change failing case: [URL and evidence]
2. Post-deploy observable result: [result]
3. Search Console or log follow-up: [window]
4. Owner and rollback condition: [owner / condition]

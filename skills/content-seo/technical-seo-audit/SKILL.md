---
name: technical-seo-audit
description: >-
  Audit a website's technical SEO across crawl access, indexing controls, canonicalization, sitemaps, internal links, rendered content, structured data, status codes, and Core Web Vitals. Use when organic pages are missing from search, a redesign or migration is planned, Search Console reports coverage problems, or the user asks for a prioritized technical SEO audit.
license: MIT
compatibility: Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, OpenCode, Goose, Hermes, Jesse, Windsurf, Zed
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: content-seo
  tags: [seo, technical-seo, search-console, web-performance, structured-data]
  related_skills: [seo-strategy, pillar-pages, pseo-strategy, tracking-plan]
  frameworks:
    - "Google Search Essentials"
    - "Google Search Central — Crawling and Indexing"
    - "Google Search Central — Structured Data Guidelines"
    - "web.dev — Core Web Vitals"
---

# Technical SEO Audit

## Overview

A useful technical SEO audit proves where discovery, crawling, rendering, indexing, canonicalization, or page experience breaks. It does not produce a hundred-tool checklist with no evidence or promise rankings from passing a score.

## When to Use

- Important pages are not indexed or organic traffic dropped unexpectedly.
- A site migration, domain change, redesign, CMS change, or URL rewrite is planned.
- Search Console reports indexing, structured-data, sitemap, or Core Web Vitals issues.
- Programmatic pages need crawl-budget and duplicate-control review.
- The user asks for a technical SEO audit, crawl audit, indexation audit, or SEO migration QA.

## Authoritative Foundations

- **Google Search Essentials**: evaluate technical eligibility, spam-policy risks, crawlable links, and people-first page signals without claiming that compliance guarantees indexing or ranking.
- **Google Search Central — Crawling and Indexing**: separate crawl controls from index controls; `robots.txt` manages crawling, while `noindex` or access control manages index exclusion.
- **Google Search Central — Canonicalization and Sitemaps**: treat redirects and `rel=canonical` as stronger canonical signals than sitemap inclusion, and include only preferred canonical URLs in sitemaps.
- **Google Search Central — Structured Data Guidelines**: validate only markup that represents visible page content and report rich-result eligibility rather than promising presentation.
- **web.dev — Core Web Vitals**: evaluate field data at the 75th percentile against LCP ≤2.5s, INP ≤200ms, and CLS ≤0.1, segmented by mobile and desktop where data exists.

## Prerequisites

- Site or representative URL set, target market, and business-critical page types.
- Search Console access when available; otherwise state that index evidence is limited.
- Crawl permission and a bounded request rate suitable for the site.
- Deployment, framework, CMS, CDN, and migration context.
- A clear distinction between production, staging, authenticated, and blocked surfaces.

## Step-by-Step Process

### 1. Define the audit universe

Build a sample by page type and business value. Record hostname variants, protocols, locales, parameters, staging hosts, and known legacy paths. Do not infer sitewide health from the homepage.

### 2. Test access and response behavior

Check DNS/TLS, redirect chains, final status, HTML response, robots directives, `X-Robots-Tag`, and authentication. Flag soft 404s, redirect loops, mixed canonical targets, and indexable staging pages.

### 3. Trace discovery and crawling

Review `robots.txt`, XML sitemaps, internal links, orphan candidates, pagination, faceted URLs, and rendered link elements. Distinguish blocked crawling from excluded indexing.

### 4. Reconcile indexing and canonical signals

Compare declared canonical, sitemap URL, internal-link target, redirect target, hreflang cluster, and Search Console-selected canonical. Group conflicts by template so fixes address root causes.

### 5. Inspect rendered content and metadata

Compare raw HTML with rendered output for title, description, canonical, headings, primary content, links, and structured data. Note client-side delays or errors that hide decisive content.

### 6. Validate structured data

Check syntax, required properties, visible-content agreement, URL consistency, and feature-specific eligibility. Use the Rich Results Test or equivalent evidence when available.

### 7. Evaluate performance with field-first evidence

Prefer CrUX or Search Console field data; use lab tests for diagnosis. Report LCP, INP, and CLS by template and device. Do not average away a failing 75th percentile.

### 8. Prioritize fixes

Score each issue by affected valuable URLs, severity, confidence, effort, and dependency. Separate blocking indexation defects from enhancements and monitoring work.

### 9. Create verification cases

For every priority fix, define a pre-change failing URL, expected observable result, test method, owner, and post-deploy monitoring window.

## Output Format

Deliver:

1. Executive status and evidence limits.
2. Crawl/index funnel with counts by page type.
3. Issue register with example URLs and reproduced evidence.
4. Canonical/sitemap/internal-link conflict matrix.
5. Rendered metadata and structured-data findings.
6. Core Web Vitals table using field and lab evidence separately.
7. Prioritized remediation backlog.
8. Release verification and monitoring plan.

## Quality Check

- [ ] Every issue includes at least one reproducible URL or source report.
- [ ] Crawl, indexing, ranking, and rich-result eligibility are not conflated.
- [ ] `robots.txt` is not recommended as a guaranteed deindexing mechanism.
- [ ] Canonical recommendations align redirects, internal links, and sitemaps.
- [ ] Field and lab performance data are labeled separately.
- [ ] Core Web Vitals thresholds use LCP 2.5s, INP 200ms, and CLS 0.1 at p75.
- [ ] Fixes are prioritized by business impact and affected templates, not tool severity alone.
- [ ] No ranking or rich-result outcome is guaranteed.

## Common Pitfalls

| Pitfall | Why it fails | Fix |
|---|---|---|
| Treating a crawler score as the audit | Scores hide evidence and business impact | Show affected URLs, templates, and search-state evidence |
| Blocking a URL in robots.txt to remove it | A blocked URL can remain indexed without a snippet | Allow crawling long enough to process `noindex`, or require authentication |
| Fixing canonicals only in HTML | Conflicting sitemaps and links keep sending mixed signals | Align redirects, canonicals, sitemaps, and internal links |
| Using only Lighthouse lab data | Lab runs do not represent the user distribution | Lead with field data and use lab traces for diagnosis |
| Adding schema unrelated to visible content | Violates eligibility guidelines | Mark up accurate, visible, feature-supported content only |

## Execution Artifacts

- `references/framework-notes.md` — Current technical thresholds and source routing
- `templates/output-template.md` — Evidence-first technical SEO audit
- `scripts/check-output.py` — Audit completeness validator

## Related Skills

- `seo-strategy` for keyword, content, and authority planning.
- `pseo-strategy` for template-scale indexation and duplicate control.
- `pillar-pages` for internal-link and topic-cluster architecture.
- `tracking-plan` for analytics measurement that remains separate from indexation evidence.

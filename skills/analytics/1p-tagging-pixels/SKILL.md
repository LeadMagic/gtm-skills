---
name: 1p-tagging-pixels
description: >-
  Set up first-party tracking and analytics — website pixels, conversion tracking,
  UTM architecture, cookie consent, server-side tagging vs client-side, 1P vs 3P
  data strategy, and identity resolution. Use when setting up tracking, implementing
  pixels, building attribution, or preparing for privacy-first measurement.
  Triggers on: "pixel", "tracking", "conversion tracking", "first-party data",
  "server-side tagging", "UTM", "cookie consent", "1P vs 3P", "identity resolution",
  or any tracking implementation request.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: analytics
  tags: [tracking, pixels, analytics, attribution, privacy, first-party]
  related_skills: [attribution, paid-advertising, gtm-metrics, proactive-alerts]
  frameworks: [Privacy-First Measurement, Server-Side Tagging Architecture, 1P Data Strategy]
---

# 1P Tagging & Analytics

## Overview

Third-party cookies are dead. Apple ITP, Firefox ETP, and Chrome's phase-out
have made browser-based tracking unreliable. The future is first-party data
and server-side measurement — data your customers intentionally share with you
that survives ad blockers, cookie restrictions, and platform changes.

This skill covers the complete measurement stack: 1P vs 3P strategy, pixel
implementation, UTM architecture, server-side tagging, consent management,
and identity resolution. The output is a privacy-resilient analytics
infrastructure that works when cookies don't.

## When to Use

- "Set up conversion tracking"
- "1P vs 3P data strategy"
- "Install pixels (LinkedIn, Meta, Google, TikTok)"
- "Build UTM architecture"
- "Set up server-side GTM"
- "Implement first-party tracking"
- "Fix attribution gaps"
- "Set up cookie consent"
- "Identity resolution setup"

## 1P vs 3P Data Strategy

### First-Party Data (1P)
Data you collect directly from your customers — they know they're sharing it.
Examples: email signups, form fills, product usage, purchase history, support
tickets, survey responses, account registration.

**Advantages:** Privacy-compliant by default. Survives browser changes. Higher
data quality. You own it. No intermediary. Can be enriched with identity
resolution.

**Disadvantages:** Requires customer action (signup, login, form fill). Smaller
volume than 3P. Needs infrastructure to collect, store, and activate.

### Third-Party Data (3P)
Data collected by entities that don't have a direct relationship with the user.
Examples: browser cookies, ad network tracking, data brokers, device graphs,
cross-site tracking.

**Advantages:** Large scale. Doesn't require user action. Useful for prospecting
and lookalike audiences. Historical data for benchmarking.

**Disadvantages:** Dying. Browser restrictions block 30-40% of 3P tracking.
Regulatory pressure (GDPR, CCPA). Lower data quality. You don't own it.
Expensive (data broker fees).

### The Transition
**Now:** Run both 1P and 3P in parallel. 3P for scale, 1P for accuracy.
**Next 12 months:** Shift budget from 3P data to 1P infrastructure.
**End state:** 1P is the foundation. 3P is supplementary where still available.

### 1P Data Activation

Collect → Enrich → Activate:

1. **Collect:** Form fills, signups, logins, product usage, email engagement,
   survey responses, support interactions.
2. **Enrich:** Identity resolution (match email to company, role, firmographics).
   Behavioral scoring. Predictive modeling.
3. **Activate:** Personalization (website, email, product), ad targeting
   (customer match, retargeting), sales prioritization, content recommendations,
   churn prediction.

## Step-by-Step Process

### Phase 1: Pixel Inventory

Install these four pixels on every page:

**LinkedIn Insight Tag:** Base code in `<head>`, event tracking on conversions.
Identifies company visitors for ABM retargeting even without form fills.

**Meta Pixel (Facebook):** Base code + conversion events. Required for Meta
ads optimization, retargeting, and lookalike audience building.

**Google Ads Conversion Tag:** Via Google Tag Manager or gtag.js. Tracks
ad-driven conversions for bidding optimization.

**TikTok Pixel:** Base code + events. Required for TikTok ads optimization.

Plus: **Google Analytics 4 (GA4)** — your analytics foundation. Event-based
model (not pageview-based). Free, unlimited for most use cases.

### Phase 2: UTM Architecture

Standardize UTM parameters across all campaigns:

| Parameter | Purpose | Example |
|---|---|---|
| `utm_source` | Traffic origin | `linkedin`, `google`, `meta`, `email`, `direct` |
| `utm_medium` | Channel type | `cpc`, `organic`, `email`, `social`, `referral` |
| `utm_campaign` | Specific campaign | `product_demo_q1`, `webinar_feb` |
| `utm_content` | Ad/creative variant | `variant_a`, `video_testimonial` |
| `utm_term` | Keyword (search only) | `cold+email+software` |

**Enforcement:** Single source of truth spreadsheet. Consistent naming. Never
mix `linkedin` and `LinkedIn` and `li`. Pre-built UTM templates for common
campaign types.

### Phase 3: Server-Side Tagging

Move from browser tags to server-side dispatch:

**Benefits:**
- Bypasses ad blockers (30-40% of client-side events lost).
- Improves page speed (fewer browser scripts).
- Data control (filter, enrich, or suppress data before it leaves your server).
- Privacy compliance (control what data is shared with which platform).

**Setup:** Google Tag Manager Server-Side (free, Google-hosted or self-hosted),
Segment Protocols, or custom server endpoint. One server-side container
receives events, dispatches to all platforms.

**Architecture:**
```
Website/App → Server-Side GTM → LinkedIn Conversion API
                              → Meta Conversions API
                              → Google Ads Offline Conversions
                              → TikTok Events API
                              → Your Data Warehouse
```

### Phase 4: Consent Management

GDPR (EU): explicit opt-in before tracking. CCPA (California): right to
opt-out. Growing state laws.

**Implementation:** Consent Management Platform (Cookiebot, OneTrust, Termly).
Load tracking scripts only after consent. Block all cookies and pixels until
user accepts. Document data flows for compliance.

**Consent banner best practices:** Clear "Accept All" / "Customize" options.
Don't make rejecting harder than accepting. Don't use dark patterns.

### Phase 5: Identity Resolution

Connect anonymous visitors to known contacts:

- **Reverse-IP lookup:** Identify companies visiting your site (even without
  form fills). Tools: Clearbit Reveal, 6sense, Demandbase.
- **First-party cookie matching:** Match returning visitors to previous
  sessions. Survives 3P cookie restrictions.
- **Email-based identity:** The strongest identifier. Every form fill, login,
  and email click links to a known identity.
- **Cross-device graph:** Link same user across phone, laptop, tablet via
  login events.

Use identity resolution for: ABM retargeting, sales alerts on target account
visits, content personalization, pipeline attribution.

## Output Format

Measurement plan with: 1P vs 3P strategy, pixel inventory, UTM taxonomy,
server-side architecture diagram, consent implementation, identity resolution
setup, and conversion event map.

## Quality Check

- [ ] All four major pixels installed (LinkedIn, Meta, Google, TikTok)
- [ ] GA4 configured with conversion events
- [ ] UTM taxonomy documented and enforced
- [ ] Server-side tagging implemented (or roadmap with timeline)
- [ ] Consent management active for EU traffic
- [ ] Identity resolution configured for ABM accounts
- [ ] Conversion event map: every meaningful action tracked

## Common Pitfalls

1. **Client-side only.** 30-40% of browser events are lost to ad blockers.
   Server-side captures 100%. Implement server-side tagging before scaling
   ad spend.

2. **No UTM standardization.** "linkedin", "LinkedIn", "li", "lnkd" are
   four different sources in analytics. One naming convention, enforced.

3. **Tracking without consent.** GDPR fines up to 4% of global revenue.
   Implement consent before tracking EU visitors.

4. **Pixel duplication.** Same pixel fired twice = double-counted conversions.
   Audit quarterly with browser dev tools.

5. **3P dependency without 1P transition.** 3P data is dying. 1P data is the
   future. Run both now, actively build 1P infrastructure.

## Related Skills

- **attribution**: Multi-touch attribution models
- **paid-advertising**: Campaign tracking setup
- **proactive-alerts**: Trigger alerts on tracked events
- **marketing-strategy**: Overall measurement framework

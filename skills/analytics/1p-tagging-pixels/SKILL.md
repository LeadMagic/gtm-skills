---
name: 1p-tagging-pixels
description: >-
  Set up first-party tracking and analytics — website pixels, conversion tracking,
  UTM architecture, cookie consent, server-side tagging, and identity resolution
  pixels. Use when setting up tracking, implementing pixels, building attribution
  infrastructure, or preparing for privacy-first measurement. Triggers on: "pixel",
  "tracking", "conversion tracking", "first-party data", "server-side tagging",
  "UTM", "cookie consent", "identity resolution", "analytics setup", "Facebook
  pixel", "LinkedIn insight tag", or any tracking implementation request.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: analytics
  tags: [tracking, pixels, analytics, attribution, privacy]
  frameworks: [Privacy-First Measurement, Server-Side Tagging Architecture]
---

# 1P Tagging & Pixels

## Overview
Third-party cookies are dead. First-party data and server-side tracking are
the present. Every GTM motion needs measurement infrastructure: pixels that
track what matters, UTMs that attribute correctly, and server-side tagging
that survives ad blockers. This skill covers the complete measurement stack.

## When to Use
- "Set up conversion tracking"
- "Install Facebook/LinkedIn pixel"
- "Build UTM architecture"
- "Set up server-side GTM"
- "Implement first-party tracking"
- "Fix attribution gaps"
- "Set up cookie consent"

## Step-by-Step Process
### Phase 1: Pixel Inventory
Platforms requiring pixels: LinkedIn Insight Tag, Meta (Facebook) Pixel,
Google Ads conversion tag, Google Analytics (GA4), TikTok Pixel, Twitter/X
pixel. Each needs: base code on all pages, conversion events on key actions.

### Phase 2: UTM Architecture
Standardize UTM parameters across all campaigns. Required: utm_source,
utm_medium, utm_campaign. Optional: utm_content, utm_term. Enforce
consistent naming: never mix "linkedin" and "LinkedIn" and "li". Create
a UTM spreadsheet as single source of truth.

### Phase 3: Server-Side Tagging
Move from client-side (browser) tags to server-side via Google Tag Manager
Server-Side, Segment, or custom infrastructure. Benefits: bypass ad blockers,
improve page speed, control data before it leaves your server, privacy
compliance.

### Phase 4: Consent Management
GDPR (EU), CCPA (California), and evolving state laws require opt-in for
tracking. Implement a Consent Management Platform (Cookiebot, OneTrust,
Termly). Load tracking scripts only after consent. Document data flows.

### Phase 5: Identity Resolution Pixels
Enrich known visitors with B2B identity data. Tools identify companies
visiting your site, even without form fills. Use for: account-based
retargeting, sales alerts on target account visits, content personalization,
and pipeline attribution. Implement via reverse-IP lookup or first-party
cookie matching.

### Phase 6: Conversion Event Mapping
Map every meaningful action to a conversion event: page view → demo request →
trial signup → activation → upgrade → renewal. Send events to all platforms
via server-side dispatch. One event fires once, distributes everywhere.

## Output Format
Measurement plan with pixel inventory, UTM taxonomy, server-side architecture
diagram, consent implementation guide, and conversion event map.

## Common Pitfalls
1. **Client-side only** — ad blockers block 30-40% of browser-based tracking.
   Server-side captures 100%.
2. **No UTM standardization** — "linkedin", "LinkedIn", "li", "lnkd" are
   four different sources in analytics. Pick one and enforce it.
3. **Tracking without consent** — GDPR fines are up to 4% of global revenue.
   Implement consent before tracking EU visitors.
4. **Duplicate pixels** — same pixel fired twice = double-counted conversions.
   Audit quarterly.
5. **No server-side dispatch** — firing 5 pixels client-side slows page load
   and loses data. Fire once server-side, dispatch to all platforms.

## Related Skills
- **attribution**: Multi-touch attribution models
- **analytics**: Campaign performance measurement
- **proactive-alerts**: Trigger alerts on tracked events

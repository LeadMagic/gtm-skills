---
name: tracking-plan
description: >-
  Master analytics tracking plan for PLG and B2B SaaS — unified event taxonomy,
  pixel strategy (1P and 3P tagging), marketing attribution architecture, CDP
  implementation (Segment, Rudderstack), product analytics (Amplitude, Mixpanel,
  PostHog), CRM tracking (HubSpot, Salesforce), and analytics infrastructure
  design. Use when building a complete tracking plan, designing analytics
  architecture, implementing product analytics, or aligning marketing and
  product tracking. Triggers on: "tracking plan", "analytics plan", "event
  tracking architecture", "pixel strategy", "analytics for PLG", "SaaS analytics".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: analytics
  tags: [tracking-plan, analytics, event-tracking, pixels, attribution, cdp, plg, product-analytics]
  related_skills: [event-analytics, gtm-metrics, campaign-analytics, 1p-tagging-pixels, attribution, a-b-testing, cs-analytics-dashboards]
  frameworks:
    - "Segment — Customer Data Platform (CDP) and Tracking Plan spec"
    - "Amplitude — Product analytics and behavioral cohorts"
    - "PostHog — Open-source product analytics"
    - "Mixpanel — Event-based analytics"
    - "Google Analytics 4 (GA4) — Web analytics and conversions"
    - "Elena Verna (Reforge/Amplitude) — PLG analytics models"
    - "Brian Balfour (Reforge) — Growth models and tracking"
    - "OpenView — PLG benchmarks and metrics"
    - "Avo — Tracking plan governance and code generation"
---

# Analytics Tracking Plan

## Overview

Most companies have tracking — they just don't have a plan. Events fire into
the void. Pixels fire twice (or never). Marketing attributes credit to the
wrong channel. Product doesn't know what marketing tracks. Nobody trusts the
data. The mistake: adding tracking ad-hoc without a unified plan. This skill
covers the complete analytics tracking architecture for PLG and B2B SaaS:
event taxonomy, pixel strategy, attribution architecture, CDP implementation,
and the analytics stack that makes it all work together.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Segment — Customer Data Platform (CDP) and Tracking Plan spec.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Amplitude — Product analytics and behavioral cohorts.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **PostHog — Open-source product analytics.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Mixpanel — Event-based analytics.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Google Analytics 4 (GA4) — Web analytics and conversions.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Elena Verna (Reforge/Amplitude) — PLG analytics models.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Brian Balfour (Reforge) — Growth models and tracking.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **OpenView — PLG benchmarks and metrics.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Avo — Tracking plan governance and code generation.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use

Trigger phrases: "tracking plan", "analytics plan", "analytics architecture",
"event tracking strategy", "pixel strategy", "CDP implementation", "analytics
for PLG", "SaaS analytics stack", "unified tracking plan", "marketing tracking",
"product analytics implementation", "analytics audit"

## The Unified Tracking Architecture

```
                    ┌─────────────────────────────────┐
                    │        YOUR SAAS PRODUCT          │
                    │  (Web App, API, Backend, Email)  │
                    └──────────┬──────────────────────┘
                               │
                    ┌──────────▼──────────────────────┐
                    │   CDP LAYER (Segment/Rudderstack) │
                    │   Event Collection + Routing      │
                    └──────┬───────────┬───────────────┘
                           │           │
         ┌─────────────────▼──┐   ┌───▼──────────────────┐
         │ PRODUCT ANALYTICS   │   │ MARKETING ANALYTICS   │
         │ Amplitude/Mixpanel  │   │ GA4 / Ads Pixels      │
         │ PostHog             │   │ Attribution Tools      │
         └─────────────────────┘   └───────────────────────┘
                           │           │
         ┌─────────────────▼──┐   ┌───▼──────────────────┐
         │ CRM + CS ANALYTICS  │   │ DATA WAREHOUSE        │
         │ HubSpot/Salesforce  │   │ Snowflake/BigQuery     │
         │ Intercom/Zendesk    │   │ + BI (Metabase/Looker) │
         └─────────────────────┘   └───────────────────────┘
```

## Step-by-Step Process

### Phase 1: The Tracking Plan Document

**What it is:** A single source of truth for every event, property, and
destination in your analytics infrastructure. Every developer, marketer,
and analyst references the same document.

**The Tracking Plan template (Google Sheets / Notion / Avo):**

```
TRACKING PLAN — [Company]

SHEET 1: EVENT CATALOG
| Event Name | Category | Trigger | Properties | Destinations | Owner | Status |
|---|---|---|---|---|---|---|
| Signed Up | Account | POST /auth/signup | plan, source, referrer, utm_* | Segment→GA4,Amplitude,HubSpot | Eng | Live |
| Feature Used | Usage | Client-side click | feature_name, context | Segment→Amplitude | Product | Live |
| ... | | | | | | |

SHEET 2: PROPERTY CATALOG
| Property Name | Type | Example Values | Events Using | Description |
|---|---|---|---|---|---|
| plan | string | starter, growth, enterprise | Signed Up, Upgraded, Downgraded | Customer's subscription plan |
| source | string | google_ads, linkedin, referral | Signed Up | Acquisition channel |
| ... | | | | |

SHEET 3: DESTINATIONS
| Destination | Purpose | Events Routed | Owner |
|---|---|---|---|
| Amplitude | Product analytics — retention, funnels, cohorts | All usage + account events | Product |
| GA4 | Web analytics — traffic, conversions, ad attribution | Page views, signups, conversions | Marketing |
| HubSpot | CRM — lead scoring, lifecycle stages | Account events, email events | RevOps |
| Intercom | Event-triggered messaging | All usage + milestone events | CS |
| Data Warehouse | BI — cross-functional reporting | All events | Data |

SHEET 4: IDENTITIES
| Identity Type | How It's Set | When | Example |
|---|---|---|---|
| anonymous_id | Auto-generated (cookie/localStorage) | First visit | uuid |
| user_id | Backend generates on signup | After authentication | user_abc123 |
| group_id | Workspace/account ID | After login (B2B) | ws_xyz789 |
| email | identify() call | After signup/login | user@company.com |

SHEET 5: UTM / ATTRIBUTION
| Parameter | Required | Example | Purpose |
|---|---|---|---|
| utm_source | Yes | google, linkedin, newsletter | Acquisition source |
| utm_medium | Yes | cpc, organic, email, social | Channel type |
| utm_campaign | Yes | q1_launch, black_friday | Campaign name |
| utm_content | Optional | variant_a, cta_hero | Creative variant |
| utm_term | Optional | cold+email+tool | Keyword (paid search) |
| referrer | Auto | document.referrer | Referring URL |
| landing_page | Auto | window.location.pathname | First page visited |
| gclid | Auto | Google Ads auto-tagging | Google Click ID |
| fbclid | Auto | Facebook auto-tagging | Facebook Click ID |
```

### Phase 2: Event Taxonomy for PLG and SaaS

Build the event taxonomy in `references/event-taxonomy.md` when the task needs the full PLG/SaaS event library. In SKILL.md, capture only the chosen event groups, naming rules, owners, and QA gates.

### Phase 3: Pixel Strategy (1P and 3P Tagging)

**The progressive pixel architecture:**

```
TIER 1: FIRST-PARTY (Essential — always on)
  └─ CDP (Segment/Rudderstack) — server-side SDK
     No ad blockers can block server-side events.
     Critical events (signup, payment, subscription) go server-side.

TIER 2: FIRST-PARTY (Product — always on)
  └─ CDP (Segment/Rudderstack) — client-side SDK
     Behavioral events. Some ad-blocker loss (~15-30%).
     Acceptable for product analytics (you don't need 100% of
     behavioral events — you need enough to see patterns).

TIER 3: MARKETING PIXELS (Conditional — consent required)
  └─ GA4 (Google Analytics)
  └─ Google Ads Conversion Tracking
  └─ LinkedIn Insight Tag
  └─ Meta (Facebook) Pixel
  └─ Twitter/X Pixel
  └─ Reddit Pixel
  └─ Quora Pixel
  └─ Microsoft (Bing) Ads UET

TIER 4: RETARGETING (Conditional — consent required)
  └─ Google Ads Remarketing
  └─ LinkedIn Matched Audiences
  └─ Meta Custom Audiences
  └─ AdRoll / Criteo (if using)
```

**Pixel implementation hierarchy:**

```
Server-side (via CDP) — PRIMARY:
  Segment/Rudderstack → Google Ads (enhanced conversions)
  Segment/Rudderstack → Meta CAPI (Conversions API)
  Segment/Rudderstack → LinkedIn CAPI
  These are ad-blocker resistant and privacy-safe.

Client-side (via GTM) — SECONDARY:
  Google Tag Manager (GTM) loads marketing pixels
  Consent management (Cookiebot/OneTrust) gates all marketing pixels
  GTM fires only when user has consented to marketing cookies

Server-side GTM (sGTM) — ADVANCED:
  GTM server-side container proxies all pixel requests
  Your server → sGTM → marketing platforms
  First-party domain for tracking (e.g., analytics.yourdomain.com)
  This is the gold standard for privacy-safe, ad-blocker-resistant tracking
```

**Pixel audit checklist:**
```
□ Every pixel has a purpose (no "we might use this someday" pixels)
□ Consent management gates all marketing pixels
□ Pixels fire ONCE (no duplicate firing from GTM + CDP)
□ Server-side tracking for critical conversion events
□ All pixels documented: what fires when, what data it sends
□ Regular audit: remove unused pixels (they slow down the page)
□ GDPR: marketing pixels only fire with consent
□ CCPA: "Do Not Sell" respected — data sharing pixels disabled
```

### Phase 4: Attribution Architecture

**Multi-touch attribution model:**

```
FIRST-Touch: Which channel introduced them?
  → UTM params captured at first visit. Stored in cookie + user profile.

LAST-Touch: Which channel closed them?
  → UTM params at conversion. Overwrites first-touch for "last-click" view.

MULTI-Touch: Which channels touched them along the way?
  → Track every touchpoint: ad click, email click, organic visit, referral.
  → Model: linear (equal credit), time-decay (recent = more credit),
    U-shaped (first + last = most credit), W-shaped (first + MQL + SQL + close).

SELF-REPORTED: "How did you hear about us?"
  → Form field on signup/demo. Most reliable single data point.
  → Categorize responses: Search, Social, Referral, Podcast, Event, Other.
```

**Attribution data flow:**

```
TOUCHPOINT CAPTURE:
1. First visit → capture UTM + referrer → store in first-touch cookie
2. Subsequent visits → append to visit log (timestamp, source, medium)
3. Signup/Conversion → capture UTM + referrer → store in user profile
4. CRM → Sales tags opportunity source (can override self-reported)

ATTRIBUTION REPORTING:
- HubSpot/Salesforce: Original Source, Latest Source, Source Drill-Down
- GA4: Traffic Acquisition, User Acquisition reports
- BI Tool (Metabase/Looker/Mode): Custom multi-touch models
- Attribution tool (Dreamdata/HockeyStack/Attribution): B2B journey mapping
```

### Phase 5: CDP Implementation

Use `references/cdp-implementation.md` for the full Segment/RudderStack/mParticle/warehouse routing patterns. In the main response, summarize chosen destination routing, identity policy, suppression rules, and QA checks.

### Phase 6: PLG-Specific Analytics

**The PLG funnel (measure every transition):**

```
VISITOR → SIGNUP → ACTIVATION → ENGAGEMENT → CONVERSION → EXPANSION

Visitor → Signup: Signup conversion rate (target: 5-15%)
Signup → Activation: Activation rate (target: 40-60%)
Activation → Engagement: MAU/WAU/DAU ratios (target DAU/MAU > 20%)
Engagement → Conversion: Free-to-paid rate (target: 3-8%)
Conversion → Expansion: NRR (target: 110%+)
```

**Key PLG metrics:**

| Metric | Formula | Target |
|---|---|---|
| PQL (Product-Qualified Lead) Rate | PQLs / Total Signups | 10-20% |
| Time to Value (TTV) | Days from signup to activation | < 7 days |
| Free-to-Paid Conversion | Paid accounts / Trial starts | 3-8% |
| DAU/MAU | Daily Active / Monthly Active | > 20% (sticky) |
| Feature Adoption Rate | Users using feature / Total users | > 30% (per core feature) |
| Viral Coefficient | Invites per user × acceptance rate | > 0.5 (viral if > 1.0) |
| Expansion MRR Rate | Expansion MRR / Starting MRR | > 3% monthly |

**PLG analytics stack:**

| Tool | Purpose |
|---|---|
| Amplitude | Product analytics — funnels, retention, cohorts, behavioral personas |
| Mixpanel | Alternative product analytics (simpler, event-stream focused) |
| PostHog | Open-source product analytics + session recording + feature flags |
| June.so | PLG-specific analytics (auto-generated reports for B2B SaaS) |
| Pendo / Appcues | In-app guides + product analytics |
| Heap | Auto-capture analytics (no manual event tracking) |

### Phase 7: The Analytics Governance Playbook

**Tracking plan governance:**
1. **Document first, implement second.** Every event goes into the tracking
   plan BEFORE a developer writes code.
2. **Event dictionary is law.** No untracked events. No undocumented properties.
   If it's not in the dictionary, it doesn't exist.
3. **Breaking changes are forbidden.** Properties can be added. Never removed.
   Events can be deprecated (stop sending). Never deleted.
4. **Review cadence:** Monthly with product + marketing + data. Quarterly full
   audit. Remove unused events. Consolidate near-duplicates.

**Testing and validation:**
- Segment: Source Debugger (real-time event stream)
- Amplitude: Event Explorer (verify events arriving)
- GA4: DebugView (real-time event debug)
- Avo: Code-generated type-safe tracking functions
- CI/CD: Test that events fire correctly on critical paths

**Privacy and compliance:**
- No PII in event properties (name, email, IP, phone — use user_id instead)
- Consent management gates all marketing pixels
- Data retention policies documented per destination
- GDPR: ability to delete all events for a user on request
- SOC2: event tracking infrastructure within compliance scope

## Output Format

```
ANALYTICS TRACKING PLAN — [Company]

Version: [X.Y]. Last Updated: [date]. Owner: [name]

EVENT CATALOG: [link to sheet — 50+ events documented]

CDP: [Segment / Rudderstack]
  - Server-side SDK: [implemented / planned]
  - Client-side SDK: [implemented / planned]

DESTINATIONS:
| Tool | Purpose | Events | Status |
|---|---|---|---|
| Amplitude | Product analytics | All usage + account | Live |
| GA4 | Web analytics + ads | Page views, signups | Live |
| HubSpot | CRM | Account events | Live |
| Intercom | Messaging | Usage + milestones | Live |
| Data Warehouse | BI | All events | Live |

PIXELS (consent-gated):
| Pixel | Purpose | Trigger | Status |
|---|---|---|---|
| Google Ads | Conversion tracking | Signed Up, Subscription Started | Live |
| LinkedIn Insight | Retargeting | All pages (consent-gated) | Live |
| Meta CAPI | Conversion API | Signed Up (server-side) | Live |

ATTRIBUTION:
- Model: [Multi-touch — U-shaped / W-shaped]
- Tool: [HubSpot / Dreamdata / HockeyStack / Custom BI]
- UTM parameters: [enforced / not yet]

PLG FUNNEL METRICS:
| Stage | Current | Target |
|---|---|---|
| Visitor → Signup | X% | Y% |
| Signup → Activation | X% | Y% |
| Activation → Paid | X% | Y% |

GOVERNANCE:
- Review cadence: [monthly / quarterly]
- Event dictionary: [link]
- Privacy: [GDPR consent, PII audit, data retention]
```

## Implementation Checklist

- [ ] Tracking plan document exists (spreadsheet or Avo) — not just code
- [ ] Event taxonomy covers Account, Usage, Activation, Engagement, Revenue, Milestones
- [ ] CDP implemented (server-side for critical events, client-side for behavioral)
- [ ] All marketing pixels consent-gated (no pre-ticked boxes)
- [ ] Server-side tracking for signup, payment, subscription changes
- [ ] UTM parameters captured and persisted to user profile
- [ ] Attribution model documented (first-touch + last-touch + multi-touch)
- [ ] PLG funnel measured at every stage transition
- [ ] Event dictionary maintained — no undocumented events
- [ ] PII audit complete — no personal data in event properties
- [ ] Monthly tracking plan review on calendar

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Tracking without a plan.** Events fire into the void. No one knows what
   "button_clicked_3" means. The data is worthless. Fix: Tracking plan
   document FIRST. Implementation second. Every event has a name, purpose,
   properties, destinations, and owner.

2. **Client-side only.** Ad blockers block 15-30% of client-side tracking.
   Critical events (signup, payment, subscription) are lost. Fix: Server-side
   tracking for revenue-critical events. CDP server-side SDK.

3. **Duplicate events.** Segment fires "Signed Up." GTM also fires "SignUp."
   GA4 shows 2x signups. Nobody knows which number is real. Fix: One source
   of truth per event. Audit for duplicates. GTM ONLY handles marketing pixels,
   not core events.

4. **Marketing and product tracking disconnected.** Marketing sees signups.
   Product sees activation. Nobody connects the two — can't answer "which
   marketing channel produces the most activated users?" Fix: Same event
   taxonomy. Same user_id. CDP routes to both marketing and product tools.

5. **No attribution on signup.** UTM params captured on visit but lost on
   signup. "Where did this customer come from?" = shrug. Fix: Capture UTM
   params on first visit. Persist to user profile on signup. Always.

6. **PII in event properties.** `email: "john@company.com"` tracked in every
   event. This is a privacy violation and a security risk. Fix: Use user_id.
   Store PII in your database, not your event pipeline. Only `identify()` call
   carries user traits — regular `track()` calls do not.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- `event-analytics` — Event taxonomy design, CDP architecture, event-driven GTM
- `gtm-metrics` — SaaS metrics and benchmarks
- `campaign-analytics` — Campaign performance, 6-layer metrics stack
- `1p-tagging-pixels` — First-party pixel implementation
- `attribution` — Multi-touch attribution models
- `a-b-testing` — Experiment design and statistical significance
- `cs-analytics-dashboards` — CS health scores and dashboards
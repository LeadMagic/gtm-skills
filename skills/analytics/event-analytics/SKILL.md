---
name: event-analytics
description: >-
  Customer event analytics across every GTM system — Intercom, Zendesk,
  Salesforce, HubSpot, Segment, Amplitude, Mixpanel, PostHog, and custom
  event pipelines. Covers event taxonomy design, tracking implementation,
  event-driven workflows, and unified customer views. Use when implementing
  event tracking, building a customer data pipeline, or designing event-driven
  GTM automations. Triggers on: "event analytics", "customer events", "event
  tracking", "product analytics", "Segment setup", "event pipeline".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, GitHub Copilot, Gemini CLI
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: analytics
  tags: [event-analytics, product-analytics, customer-events, tracking, segment, amplitude, intercom]
  related_skills: [cs-analytics-dashboards, gtm-metrics, campaign-analytics, a-b-testing, attribution, 1p-tagging-pixels]
  frameworks:
    - "Segment — Customer Data Platform (CDP) and event taxonomy"
    - "Amplitude — Behavioral analytics and event design"
    - "Mixpanel — Product analytics and event-based reporting"
    - "Intercom — Event-driven messaging and automation"
    - "Avo — Event taxonomy and governance"
    - "Snowplow — Open-source event pipeline"
---

# Event Analytics

## Overview

Events are the atomic unit of customer understanding. Every signup, click,
feature use, upgrade, and cancellation is an event. The mistake: tracking
events haphazardly ("track everything!") with no taxonomy, creating a data
swamp instead of a data pipeline. This skill covers event analytics across
every GTM system — how to design an event taxonomy, implement tracking, and
unify event data across your stack to build a complete customer picture.

## When to Use

Trigger phrases: "event analytics setup", "customer event tracking",
"implement Segment", "Amplitude setup for SaaS", "event taxonomy design",
"customer data pipeline", "product analytics events", "Intercom events",
"event-driven workflows"

## Step-by-Step Process

### Phase 1: Event Taxonomy Design

**The 4 event types (Segment spec):**

1. **Identify:** Who is the user? `identify(userId, traits)`
2. **Track:** What did they do? `track(eventName, properties)`
3. **Page:** What page did they view? `page(name, properties)`
4. **Group:** What account/workspace are they in? `group(groupId, traits)`

**Event naming convention (object-action framework):**
```
Format: [Object] [Action] (Past tense. Write events as things that HAPPENED.)

Good: "Project Created" "Invoice Paid" "Campaign Sent"
Bad: "createProject" "user_clicked_button" "page3-conversion-v2"

Rules:
- Title case: "Signed Up" not "signed_up"
- Past tense: "Viewed" not "View"
- Object first: "Report Exported" not "Exported Report"
- No technical jargon: "Payment Completed" not "stripe_webhook_200"
```

**Event taxonomy — core events every SaaS should track:**
```
ACCOUNT EVENTS:
- Signed Up (properties: plan, source, referrer, UTM params)
- Subscription Started (properties: plan, price, billing period)
- Subscription Upgraded (properties: from_plan, to_plan, reason)
- Subscription Downgraded (properties: from_plan, to_plan, reason)
- Subscription Canceled (properties: plan, reason, tenure_days)
- Trial Started / Trial Converted / Trial Expired

USAGE EVENTS:
- Feature Used (properties: feature_name, context, duration)
- Search Performed (properties: query, results_count)
- Integration Connected (properties: integration_name)
- Invite Sent / Invite Accepted (properties: role)
- File Uploaded / Exported (properties: type, size)

ENGAGEMENT EVENTS:
- Email Opened / Clicked (properties: email_type, campaign_id)
- Notification Viewed / Clicked
- Support Ticket Created / Resolved (properties: category, priority)
- NPS Submitted (properties: score, comments)
- QBR Attended (properties: attendees)

REVENUE EVENTS:
- Invoice Created / Paid / Overdue
- Credit Card Added / Updated / Failed
- Refund Processed

MILESTONE EVENTS:
- Activation Complete (properties: time_to_activate_hours)
- First Value Achieved (properties: milestone, time_to_value_days)
- 7-Day Active / 30-Day Active
- Power User Threshold Reached
```

### Phase 2: Implementation Strategy

**Source → CDP → Destinations architecture:**

```
Your App (client/server)
    │
    ▼
Segment (or Rudderstack / mParticle / Snowplow)
    │
    ├── Amplitude (product analytics)
    ├── Mixpanel (product analytics)
    ├── Intercom (event-triggered messaging)
    ├── Salesforce / HubSpot (CRM events)
    ├── Google Analytics (web analytics)
    ├── Data Warehouse (Snowflake / BigQuery / Redshift)
    └── Webhook → custom integrations
```

**Implementation pattern (server-side preferred):**
```javascript
// Identify on login
analytics.identify(userId, {
  email: user.email,
  name: user.name,
  plan: user.plan,
  createdAt: user.createdAt,
  company: { id: workspace.id, name: workspace.name }
});

// Group for B2B (account-level context)
analytics.group(workspaceId, {
  name: workspace.name,
  plan: workspace.plan,
  employees: workspace.employeeCount,
  mrr: workspace.mrr
});

// Track key events
analytics.track('Feature Used', {
  feature: 'Email Finder',
  source: 'dashboard',
  credits_remaining: user.credits
});
```

### Phase 3: System-Specific Event Analytics

**Intercom Events:**
- Use as event triggers for: onboarding tours (if user does X, show tour Y),
  email sequences (if user reaches milestone, send email), chat targeting
  (if user is stuck, offer help), in-app messages (if feature unused, promote it)
- `Intercom('track', 'Feature Used', { feature: 'Reports' })`

**Salesforce Events (via Platform Events):**
- Track: Lead Status Changed, Opportunity Stage Changed, Task Completed
- Use for: real-time dashboards, Slack alerts on key deals, enrichment triggers

**HubSpot Events (via Custom Behavioral Events):**
- Track: Form Submission, Meeting Booked, Email Clicked, Page Viewed
- Use for: lead scoring, workflow triggers, list membership

**Amplitude / Mixpanel:**
- Purpose: product analytics — not just what happened, but who did it,
  how often, and what happened next
- Key reports: retention curves, funnel analysis, behavioral cohorts,
  feature adoption, power user curve

### Phase 4: Event-Driven GTM Automation

**Example workflows:**
```
Event: "Signed Up" → source = Google Ads
  → Add to Ad Conversions in Google Ads
  → Add to HubSpot as Lead
  → Enrich with Clearbit / LeadMagic
  → Route to SDR if ICP match
  → Send welcome email sequence

Event: "Feature Used" → feature = "Reports", 3rd time this week
  → Score: +10 engagement points
  → Trigger Intercom message: "Power user move: try Advanced Reports"

Event: "Trial Expired" → no conversion
  → Send re-engagement email sequence (3 emails over 7 days)
  → If no response: move to nurture list

Event: "NPS Submitted" → score < 6 (Detractor)
  → Create Zendesk ticket: "Follow up with Detractor"
  → Slack alert to CSM
  → Auto-schedule call with customer
```

### Phase 5: Event Governance

**Event dictionary (living document — reference per event):**
| Event Name | Properties | Trigger | Destinations | Owner |
|---|---|---|---|---|
| Signed Up | plan, source, referrer | POST /auth/signup | Segment → all | Eng |
| Feature Used | feature_name, context | Client-side track call | Amplitude, Intercom | Product |

**Governance rules:**
- New events require: description, properties schema, destination list, owner
- No "track everything" — each event must have a purpose and an owner
- Deprecate, don't delete. Keep old events but stop sending them.
- Review event taxonomy quarterly. Remove unused events. Consolidate duplicates.
- Every event needs a test. CI/CD should verify events fire correctly.

**Tools for event governance:**
- Avo (avo.app) — event taxonomy design, code generation, validation
- Segment Protocols — enforce event schemas, block malformed events
- Amplitude Data — govern events within Amplitude's ecosystem

## Output Format

```
EVENT ANALYTICS PLAN — [Company]

CDP: [Segment / Rudderstack / mParticle / Snowplow / Custom]

EVENT TAXONOMY:
[Docs link or table with event name, properties, trigger, destinations]

IMPLEMENTATION:
- Client-side: [SDK / library]
- Server-side: [SDK / webhook pipeline]
- Testing: [how events are validated]

DESTINATIONS:
| Tool | Purpose | Key Events |
|---|---|---|
| Amplitude | Product analytics | Feature Used, Signed Up |
| Intercom | Messaging automation | All usage + milestone events |
| HubSpot | CRM | Account events, revenue events |
| Data Warehouse | Analytics | All events |

EVENT-DRIVEN WORKFLOWS:
1. [Event] → [Action] — [trigger condition]
2. [Event] → [Action] — [trigger condition]
```

## Quality Checklist

- [ ] Event taxonomy documented with naming convention (Object-Action, past tense)
- [ ] 20+ core events implemented across Account, Usage, Engagement, Revenue
- [ ] Server-side tracking for critical events (not just client-side)
- [ ] Group/account-level context sent for B2B (workspace ID, plan, employees)
- [ ] Event dictionary maintained with owner, properties schema, destinations
- [ ] Event-driven workflows documented (event → action mapping)
- [ ] Event testing in CI/CD (events fire correctly, properties valid)
- [ ] No PII in event properties (email, name, IP — use pseudonymous IDs)

## Common Pitfalls

1. **Tracking everything.** 500 events, 50 properties each, no one knows what
   any of them mean. The data swamp. Fix: Every event must have a purpose.
   Start with 20. Add as needed.

2. **Inconsistent naming.** `signed_up`, `userSignup`, `Sign Up Completed` all
   describe the same thing across different systems. Fix: One taxonomy. Object-
   action. Past tense. Documented in an event dictionary.

3. **Client-side only tracking.** Ad blockers block client-side tracking
   (30-50% of users). Critical events lost. Fix: Server-side tracking for
   key events (signup, payment, subscription changes). Client-side for
   behavioral events.

4. **No group/account context for B2B.** Events tracked to individual users
   but not linked to their company workspace. Can't answer "what are our top
   10 accounts doing?" Fix: `group()` call on login linking user to workspace.

5. **PII in event properties.** `email: "john@company.com"` in event properties
   is a data privacy violation waiting to happen. Fix: Use user IDs. Store PII
   in your database, not your event pipeline.

## Related Skills

- `cs-analytics-dashboards` — CS health scores and dashboards
- `gtm-metrics` — SaaS metrics stack
- `campaign-analytics` — Campaign performance analysis
- `1p-tagging-pixels` — First-party tracking implementation
- `a-b-testing` — Experiment design and analysis
- `attribution` — Multi-touch attribution models
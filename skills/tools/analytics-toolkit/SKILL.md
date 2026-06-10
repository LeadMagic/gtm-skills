---
name: analytics-toolkit
description: >-
  Complete analytics tools toolkit — Segment CDP, Amplitude, Mixpanel, PostHog,
  GA4, and HubSpot analytics configuration. Covers implementation patterns,
  destination routing, event governance, and cross-tool reporting. Use when
  setting up analytics infrastructure or optimizing an existing analytics stack.
  Triggers on: "analytics toolkit", "Segment setup", "Amplitude configuration",
  "Mixpanel vs PostHog", "GA4 for SaaS".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: tools
  tags: [analytics, segment, amplitude, mixpanel, posthog, ga4]
  related_skills: [tracking-plan, event-analytics, gtm-metrics, campaign-analytics, a-b-testing, gtm-spend-management, gtm-tool-cost-model]
  frameworks:
    - "Segment — CDP with 400+ destinations"
    - "Amplitude — Product analytics, behavioral cohorts, experiment"
    - "PostHog — Open-source analytics, session recording, feature flags"
    - "Mixpanel — Event-based product analytics"
    - "GA4 — Google Analytics for web + app"
---

# Analytics Toolkit

## Overview

Analytics tools don't work out of the box — they work when configured with a
tracking plan, proper implementation, and destinations that talk to each other.
This skill covers setup and optimization across the analytics stack.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Segment — CDP with 400+ destinations.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Amplitude — Product analytics, behavioral cohorts, experiment.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **PostHog — Open-source analytics, session recording, feature flags.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Mixpanel — Event-based product analytics.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **GA4 — Google Analytics for web + app.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use

Trigger phrases: "analytics setup", "Segment configuration", "Amplitude
implementation", "PostHog setup", "GA4 for B2B", "analytics stack comparison"

Stage-based recommendations: `references/analytics-stack-by-stage.md`.  
Spend tracking: `gtm-spend-management` vendor register.

## Tool Comparison

| Tool | Best For | Pricing | Key Feature |
|---|---|---|---|
| **Segment** | CDP — collect once, route everywhere | Free-$120/mo | 400+ destinations |
| **Amplitude** | Product analytics — retention, cohorts | Free-$100K/enterprise | Behavioral cohorts |
| **PostHog** | Open-source — session replay, feature flags | Free self-hosted/Cloud $ | All-in-one |
| **Mixpanel** | Event-stream analytics, simpler UI | Free-$20K/enterprise | Event explorer |
| **GA4** | Web analytics + ad attribution | Free | Google Ads integration |

## Implementation Pattern

```javascript
// Segment → Amplitude + GA4 + Data Warehouse
analytics.track('Feature Used', { feature_name: 'Reports' });
// → Amplitude: behavioral cohort
// → GA4: custom event + conversion tracking
// → Data Warehouse: raw event for BI analysis
```

## Implementation Checklist

- [ ] CDP implemented (Segment or Rudderstack) — single source of truth
- [ ] Server-side tracking for critical events (signup, payment)
- [ ] Client-side tracking for behavioral events
- [ ] GA4 configured with custom events + conversions
- [ ] Product analytics tool configured with retention + funnel reports
- [ ] Data warehouse receiving all events for BI

## Common Pitfalls

1. **Direct-to-tool without CDP.** Send events directly to Amplitude + GA4 +
   Mixpanel. 3x the implementation. Inconsistent data. Fix: CDP as single source.
2. **No server-side tracking.** Ad blockers kill client-side. Critical events
   lost. Fix: Server-side Segment for revenue events.
3. **Multiple 'source of truth' tools.** Marketing trusts GA4. Product trusts
   Amplitude. Numbers disagree. Fix: Data warehouse as single source of truth.


## Output Format

The agent delivers an analytics stack configuration plan matched to the user's stage, team, and tool question:

- **Stack Recommendation:** recommended combination (CDP + product analytics + web analytics) with 1-line rationale per tool choice relative to the user's company size, budget, and use case
- **Implementation Priority Order:** phased rollout sequence — CDP as single-collection layer first, product analytics second, web analytics third, data warehouse fourth — with reasoning for the ordering
- **Event Taxonomy Sample:** 5–10 prioritized events with property schema (event name, user ID, account properties, outcome it measures) aligned to the user's funnel
- **Destination Routing Map:** which events route to which tools (e.g., behavioral events → Amplitude for retention cohorts; conversion events → GA4 for ad attribution; all events → warehouse for BI)
- **Implementation Checklist:** 6-point verification covering server-side tracking for critical events, custom conversion configuration, single-source-of-truth designation, client-side redundancy, QA event audit, and stakeholder dashboard setup

## Quality Check

Before delivering, verify:
- [ ] All required sections complete
- [ ] Output matches the user's stated need
- [ ] No vague or unsupported claims
- [ ] Frameworks cited where applicable

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/analytics-stack-by-stage.md` — CDP + product + web by ARR
- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- `tracking-plan` — Complete analytics architecture
- `event-analytics` — Event taxonomy and CDP design
- `gtm-metrics` — SaaS metrics and benchmarks
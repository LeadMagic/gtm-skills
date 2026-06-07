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
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: tools
  tags: [analytics, segment, amplitude, mixpanel, posthog, ga4]
  related_skills: [tracking-plan, event-analytics, gtm-metrics, campaign-analytics, a-b-testing]
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

## When to Use

Trigger phrases: "analytics setup", "Segment configuration", "Amplitude
implementation", "PostHog setup", "GA4 for B2B", "analytics stack comparison"

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

## Quality Checklist

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

The agent should produce a structured deliverable:

```markdown
# [Deliverable Title]

## Summary
[1-2 sentence summary of what was produced]

## Key Outputs
- [Output item 1]
- [Output item 2]
- [Output item 3]
```

## Quality Check

Before delivering, verify:
- [ ] All required sections complete
- [ ] Output matches the user's stated need
- [ ] No vague or unsupported claims
- [ ] Frameworks cited where applicable

## Common Pitfalls

1. **Incomplete output.** The deliverable is missing critical sections. Fix: verify against the output template before delivering.
2. **Generic advice without specifics.** "Improve your process" without concrete steps. Fix: every recommendation must have a specific action.
3. **Missing framework citations.** Advice without named authorities. Fix: cite the specific framework that grounds each recommendation.
## Related Skills

- `tracking-plan` — Complete analytics architecture
- `event-analytics` — Event taxonomy and CDP design
- `gtm-metrics` — SaaS metrics and benchmarks
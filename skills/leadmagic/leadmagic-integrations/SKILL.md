---
name: leadmagic-integrations
description: >-
  Integrate LeadMagic with GTM platforms — Clay, Apollo, Smartlead, Instantly,
  Salesforce, HubSpot. Bi-directional data flow, webhook enrichment, Zapier/Make.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: leadmagic
  tags: [leadmagic, integrations, clay, smartlead, hubspot, salesforce]
---

# LeadMagic Integrations

## Overview
LeadMagic integrates with the major GTM platforms — Clay, Apollo, Smartlead, Instantly, Salesforce, HubSpot, Zapier, and Make. This skill covers integration setup, data flow patterns, and common workflows for each platform.

## When to Use
- "Connect LeadMagic to Clay"
- "Integrate LeadMagic with Smartlead"
- "Set up LeadMagic + HubSpot"
- "Push LeadMagic data to Salesforce"

## Platform-Specific Setup
- **Clay**: Native integration. Add LeadMagic Email Finder and Email Validation as enrichment columns.
- **Apollo**: Use LeadMagic for verification of Apollo-found contacts.
- **Smartlead**: Push verified contacts via CLI or API before campaign launch.
- **Instantly**: Same pattern — verify, then push.
- **Salesforce/HubSpot**: Enrich CRM records on create or on schedule.
- **Zapier/Make**: No-code workflows. Trigger on new lead → enrich with LeadMagic → update CRM.

## Data Flow Pattern
Source → LeadMagic enrichment → verification → CRM/sequencer. Always verify before sending, regardless of platform.

## Common Pitfalls
1. **Two-way sync conflicts** — push from enrichment to CRM, not both directions.
2. **No verification before send** — platform integration does not replace verification.
3. **Not using webhooks** — real-time enrichment via webhooks beats batch processing for speed.

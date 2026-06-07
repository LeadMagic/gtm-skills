---
name: data-enrichment-strategy
description: >-
  Design an end-to-end B2B data enrichment architecture — provider selection,
  waterfall design, cost modeling, and CRM hygiene. Use when the user wants to
  evaluate enrichment providers, build an enrichment stack, compare data vendors,
  or design their data architecture. Triggers on: "enrichment strategy", "which
  data provider", "compare Apollo vs ZoomInfo", "build enrichment architecture",
  "data stack", "enrichment vendors", or any request about choosing or combining
  B2B data sources.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: prospecting
  tags: [enrichment, data-strategy, providers, architecture, build-vs-buy]
  related_skills: [lead-enrichment, waterfall-enrichment, clay-automation, api-enrichment]
  frameworks: [GTMLens Provider Comparison, Ziellab 3-Waterfall Architecture]
---

# Data Enrichment Strategy

## Overview

Every B2B go-to-market team needs enrichment. No single provider covers
everything, and the stack you choose determines your data quality, cost
structure, and operational complexity for years.

This skill walks through provider selection, waterfall architecture design,
build-vs-buy decisions, and ongoing data hygiene. The output is a complete
enrichment architecture tailored to the user's ICP, budget, and volume.

## When to Use

- "What enrichment providers should we use?"
- "Apollo vs ZoomInfo vs Clay — which is right for us?"
- "Design our data enrichment architecture"
- "How do we get 90%+ email coverage?"
- "Should we build or buy our enrichment pipeline?"

## Authoritative Foundations

The enrichment provider landscape is well-documented by GTMLens, Ziellab, and
the GTM engineering community. The core design principle: no single provider
covers more than 60-75% of B2B contacts. Waterfall enrichment — chaining
multiple providers in sequence — is the standard pattern for hitting 85-92%
coverage.

Three separate waterfalls (company, email, phone) is the Ziellab architecture:
each field type uses different providers optimized for that data type, and the
waterfalls run independently.

## Prerequisites

- ICP defined (company size, industry, geography, buyer personas)
- Monthly enrichment volume estimate
- Budget range for data + platform costs

## Step-by-Step Process

### Phase 1: Intake

Ask the user:
1. Target segment (SMB, mid-market, enterprise, or all)?
2. Primary geography (US, EU, APAC, global)?
3. Monthly enrichment volume?
4. What data points are critical? (email, phone, firmographics, tech stack, intent)
5. Existing tools? (CRM, sequencer, Clay, etc.)

### Phase 2: Provider Selection

| Provider | Best For | Email Coverage | Phone Coverage | Firmographics | Cost Profile | Notes |
|---|---|---|---|---|---|---|
| Apollo | US SMB/Mid-market | 60-75% | Moderate | Good | $59-99/user/mo | Built-in sequencer |
| ZoomInfo | Enterprise, Fortune 5000 | 70-85% | Strong | Excellent | $15K-100K+/yr | Deep org charts, intent |
| Clay | Multi-source orchestration | Via providers | Via providers | Via providers | $149-800/mo + credits | 150+ providers, workflows |
| Clearbit (HubSpot) | US companies | Good | Limited | Excellent | Part of HubSpot | Real-time enrichment |
| People Data Labs | Technical, EU, early-stage | 40-55% | Moderate | Good | API credits | Broad but thinner data |
| Cognism | EU, mobile phones | Good | Strong (EU) | Good | Mid-market pricing | GDPR-compliant |
| Lusha | Quick lookups | 30-50% | Moderate | Light | Freemium/credits | Browser extension |
| Hunter | Domain-pattern matching | 15-25% | None | None | Low, per-request | Email only |
| Findymail | US sales personas | 40-60% | None | None | Moderate | Email specialist |
| Prospeo | Title-first search | 40-55% | None | None | Credits | API + CSV export |

### Phase 3: Architecture Design

Stack by stage:

**Startup / <$2M ARR, <5K contacts/month:**
- Apollo (all-in-one: data + sequencing) = $59-99/month
- Add verification service = $50/month
- Total: $150/month

**Growth / $2-10M ARR, 5-30K contacts/month:**
- Clay ($149-800/mo) + Apollo data + 1-2 fallback providers
- Waterfall: LeadMagic Email Finder → Apollo → Hunter → verification
- Add CRM integration for automated enrichment
- Total: $800-1,800/month

**Enterprise / $10M+ ARR, 30K+ contacts/month:**
- ZoomInfo for firmographics + org charts
- Clay for multi-source orchestration and workflow
- Waterfall: ZoomInfo → LeadMagic → PDL → Cognism → Claygent
- n8n for custom pipeline logic
- Total: $3,000-8,000/month

### Phase 4: Build vs Buy

| Factor | Buy (SaaS platform) | Build (API-first) |
|---|---|---|
| Setup time | Hours to days | Weeks |
| Monthly cost | $150-1,800 | $500-3,000+ (engineering) |
| Flexibility | Limited to platform capabilities | Unlimited |
| Maintenance | Platform handles | Your team handles |
| Best for | <30K contacts/month, standard workflows | >30K contacts/month, custom pipelines |

Hybrid pattern: Clay for workflow + n8n/API pipeline for high-volume or
custom enrichment. Clay handles the ad-hoc and mid-volume; API handles
the scale.

### Phase 5: Data Hygiene Cadence

| Activity | Frequency |
|---|---|
| Email verification | Every 90 days (or before each campaign) |
| Firmographic refresh | Quarterly |
| Technographic snapshot | Monthly |
| CRM deduplication | Weekly |
| Full enrichment audit | Quarterly |

## Output Format

Enrichment strategy document:
```
# Enrichment Architecture for [Company]

## Current State
- Volume: X contacts/month
- Current providers: [list]
- Coverage: X%
- Cost: $X/month

## Recommended Stack
- Primary: [provider]
- Fallbacks: [providers in order]
- Verification: [provider]
- Orchestration: Clay / n8n / API

## Waterfall Design
- Email waterfall: [ordered list]
- Company waterfall: [ordered list]
- Phone waterfall: [ordered list]

## Cost Model
- Platform: $X/mo
- Provider credits: $X/mo (est. X contacts × $Y/contact)
- Verification: $X/mo
- Total: $X/mo

## Implementation Timeline
- Week 1: Provider setup
- Week 2: Pilot (500 contacts)
- Week 3: Validation and tuning
- Week 4: Production rollout
```

## Quality Check

- [ ] Provider selection matched to ICP segment and geography
- [ ] Waterfall ordered by cost-per-hit, not just coverage
- [ ] Verification step included after every email finder
- [ ] Data hygiene cadence defined
- [ ] Cost model complete (platform + credits + verification)
- [ ] Build-vs-buy decision documented with rationale

## Common Pitfalls

1. **Single-provider lock-in.** One provider covers 60-75% max. If ZoomInfo
   is your only source, you're leaving 25-40% of contacts unreachable.

2. **Over-buying for the stage.** $25K/year ZoomInfo contract for a $500K
   ARR startup is capital misallocation. Start with Apollo, add tools as
   volume and deal size justify them.

3. **No verification in the architecture.** Enrichment without verification
   means sending to stale emails. Build verification into the design, not
   bolted on later.

4. **Ignoring data decay.** Data you enriched 6 months ago is 12-18% stale.
   Design for recurring enrichment, not one-time projects.

5. **Platform as system of record.** Clay is a workspace, not a CRM. Push
   enriched data to your CRM and treat it as the source of truth.

## Related Skills

- **lead-enrichment**: Execute enrichment on a specific list
- **waterfall-enrichment**: Detailed waterfall implementation
- **clay-automation**: Clay-specific workflow design
- **api-enrichment**: API-first enrichment pipeline
- **crm-integration**: CRM setup for enriched data

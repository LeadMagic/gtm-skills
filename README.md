# GTM Blueprints

**67 production go-to-market playbooks for AI agents.** Built for Claude Code, Cursor, Codex, and any Agent Skills-compatible tool. Install and your agent becomes a GTM operator.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-67-blue)](skills/)

---

## What This Is

A complete library of AI agent skills covering the full revenue surface: strategy, prospecting, outbound, inbound, sales, analytics, automation, design, growth, and founder-led GTM.

Every skill draws from established GTM authorities: Winning by Design, Force Management, Gartner/Challenger, Huthwaite/SPIN, Sandler, April Dunford, Andy Raskin, and others. Not generic advice — named frameworks applied to specific workflows.

## Quick Install

```bash
# Claude Code
claude plugins add leadmagic/gtm-skills

# All skills
claude skills install leadmagic/gtm-skills

# A specific category
claude skills install leadmagic/gtm-skills --category outbound
```

**Also works with:** Cursor (`.cursor/skills/`), Codex (`.agents/skills/`), Hermes Agent, Windsurf, OpenCode.

## Skills Catalog

| # | Skill | Category | Description |
|---|---|---|---|
| 01 | `gtm-context` | foundation | Capture company context, ICP, GTM motion, channels, metrics as reusable foundation |
| 02 | `icp-scoring` | foundation | Weighted ICP scoring with firmographic, technographic, and behavioral dimensions |
| 03 | `positioning-messaging` | foundation | Dunford 5-component positioning, Raskin strategic narrative, messaging matrix |
| 04 | `competitive-intel` | foundation | Battlecards, competitive matrix, win/loss analysis, tech stack teardown |
| 05 | `pricing-strategy` | foundation | Ramanujam pricing models, tier design, willingness-to-pay research |
| 06 | `lead-finding` | prospecting | Multi-source lead discovery across Apollo, Sales Nav, GitHub, job boards |
| 07 | `lead-enrichment` | prospecting | Waterfall enrichment patterns, provider sequencing, confidence thresholds |
| 08 | `email-finding` | prospecting | Email discovery patterns, provider waterfall, always verify after finding |
| 09 | `contact-verification` | prospecting | Pre-send verification strategy, bounce prevention, data decay management |
| 10 | `list-building` | prospecting | Clay list building, ICP filtering, Google Maps scraping, list hygiene |
| 11 | `signal-scoring` | prospecting | 4-category signal taxonomy, scoring formulas, tier routing |
| 12 | `data-enrichment-strategy` | prospecting | Provider landscape, build-vs-buy, enrichment architecture |
| 13 | `cold-email-strategy` | outbound | Sequence architecture, cadence design, channel mixing |
| 14 | `cold-email-copywriting` | outbound | 3-line framework, subject lines, personalization tiers, persona variants |
| 15 | `email-deliverability` | outbound | SPF/DKIM/DMARC, warmup, reputation monitoring, bounce handling |
| 16 | `domain-infrastructure` | outbound | Secondary domains, mailbox provisioning, DNS auth, inbox rotation |
| 17 | `sending-platforms` | outbound | Smartlead vs Instantly vs Salesforge vs Apollo comparison and setup |
| 18 | `reply-handling` | outbound | 8-category classification, auto-reply playbooks, human escalation |
| 19 | `multi-channel-outreach` | outbound | LinkedIn, cold calls, SMS, channel coordination, conditional sequences |
| 20 | `inbound-triage` | inbound | Demo form triage, MQL/SQL routing, speed-to-lead, SLAs |
| 21 | `content-marketing` | inbound | Content strategy by funnel stage, SEO/AEO, programmatic SEO |
| 22 | `social-selling` | inbound | LinkedIn Sales Navigator, DM sequences, SSI scoring |
| 23 | `landing-pages` | inbound | CRO audits, hero/offer/proof/CTA patterns, conversion optimization |
| 24 | `sales-enablement` | sales-revops | Pitch decks, one-pagers, battlecards, demo scripts, playbooks |
| 25 | `meeting-prep` | sales-revops | Account research, attendee profiles, SPIN/MEDDIC discovery questions |
| 26 | `pipeline-management` | sales-revops | CRM hygiene, forecasting, stage definitions with Goals + Exit Criteria |
| 27 | `objection-handling` | sales-revops | 6-category taxonomy, AER framework, battlecards per competitor |
| 28 | `demo-scripts` | sales-revops | First demo, technical deep-dive, executive overview scripts |
| 29 | `deal-desk` | sales-revops | Pricing models, discount guidance, proposals, business case construction |
| 30 | `campaign-analytics` | analytics | 6-layer metrics stack, diagnostic trees, winning copy extraction |
| 31 | `deliverability-monitoring` | analytics | Bounce tracking, spam placement, blacklist monitoring, DMARC reports |
| 32 | `gtm-metrics` | analytics | Pipeline velocity, CAC/LTV, NRR, Rule of 40, GTM dashboards |
| 33 | `a-b-testing` | analytics | Experiment design, statistical significance, stop/scale rules |
| 34 | `attribution` | analytics | Multi-touch models, UTM hygiene, campaign ROI reporting |
| 35 | `proactive-alerts` | analytics | CRM pipeline alerts, buying signal alerts, Slack/email routing |
| 36 | `clay-automation` | automation | Clay table architecture, waterfalls, Claygent, CRM push, credit optimization |
| 37 | `ai-sdr-setup` | automation | AI SDR deployment, 4-week program, signal-to-action routing |
| 38 | `api-enrichment` | automation | REST API patterns, bulk enrichment, rate limiting, error recovery |
| 39 | `crm-integration` | automation | HubSpot/Salesforce/Attio setup, lifecycle stages, deal stages |
| 40 | `mcp-setup` | automation | MCP server configuration, multi-MCP architecture, tool orchestration |
| 41 | `n8n-automation` | automation | n8n workflow design, triggers, webhook-to-enrichment pipelines |
| 42 | `waterfall-enrichment` | automation | Multi-provider waterfall architecture, cost optimization, verification integration |
| 43 | `pitch-deck-builder` | design | Slide-by-slide structure, persona-customized, speaker notes |
| 44 | `one-pager-builder` | design | Product overviews, leave-behinds, champion enablement, trade show handouts |
| 45 | `battlecard-builder` | design | FIA framework battlecards, Why We Win/Lose, objection cards |
| 46 | `roi-calculator` | design | 3-scenario projections, payback period, business case construction |
| 47 | `case-study-builder` | design | Customer success stories, before/after metrics, sales-ready format |
| 48 | `design-system-gtm` | design | Brand-context for AI agents, visual identity, voice/tone guides |
| 49 | `ui-ux-gtm` | design | Landing pages, forms, signup flows, dashboards, accessibility |
| 50 | `churn-prevention` | growth | Early warning signals, re-engagement campaigns, health scoring |
| 51 | `expansion-selling` | growth | Upsell triggers, cross-sell, NRR growth, land-and-expand |
| 52 | `referral-programs` | growth | Partner/affiliate programs, comp structure, platform integration |
| 53 | `customer-marketing` | growth | Case studies, testimonials, customer advocacy, NPS engagement |
| 54 | `solo-founder-gtm` | founder-led | Tool stacks by stage, AI agents as org, hiring triggers, bootstrapper playbooks |
| 55 | `founder-brand` | founder-led | LinkedIn strategy, content cadence, newsletter growth, personal brand |
| 56 | `launch-planning` | founder-led | Launch tiers, Product Hunt playbook, 16+ channel launches |
| 57 | `lead-magnets` | founder-led | Free tools strategy, calculators, gated content, conversion optimization |
| 58 | `sales-team-building` | founder-led | Hiring sequence by ARR, POD structures, compensation models, REKS coaching |
| 59 | `partner-programs` | founder-led | Co-marketing, integration partnerships, channel strategy |
| 60 | `investor-updates` | founder-led | Monthly updates, pitch decks, fundraising narrative, metrics dashboards |
| 61 | `saas-metrics-calculator` | founder-led | Complete calculator with stage-aware benchmarks, all key SaaS metrics |
| 62 | `leadmagic-cli` | leadmagic | CLI workflows for enrichment, validation, bulk processing, integrations |
| 63 | `leadmagic-waterfall` | leadmagic | Clay waterfall with LeadMagic as primary, 95%+ coverage patterns |
| 64 | `leadmagic-mcp` | leadmagic | MCP server setup, 16 enrichment tools, multi-tool orchestration |
| 65 | `leadmagic-integrations` | leadmagic | LeadMagic + Clay/Apollo/Smartlead/Instantly/Salesforce/HubSpot |
| 66 | `leadmagic-bulk-enrichment` | leadmagic | CSV batch processing via API, batching strategy, webhook callbacks |
| 67 | `leadmagic-job-change` | leadmagic | Job change detection for pipeline intelligence, champion tracking |

## Skill Structure

Every skill follows the Agent Skills open standard (`SKILL.md` with YAML frontmatter + Markdown body):

```markdown
---
name: skill-name
description: What this skill does and when the agent should use it.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
---
```

Skills include: step-by-step procedures, output templates, quality checklists, common pitfalls, and references to the GTM authorities their approaches draw from.

## Usage

```bash
# After installing, just ask your agent:
"Score this list of companies against our ICP"
"Build a 5-email cold outreach sequence for VP Sales at Series B SaaS companies"
"Generate a competitive battlecard against Competitor X"
"Set up a waterfall enrichment workflow in Clay"
"Create a pitch deck for our new product launch"
```

## LeadMagic Integration

Several skills reference LeadMagic as an available tool for email finding, validation, company enrichment, and job change detection. These skills work with or without LeadMagic — having an API key unlocks higher-accuracy, real-time data. [Get a free API key](https://leadmagic.io) to test the LeadMagic-referencing skills.

## Contributing

PRs welcome. Skills should follow the template in `skills/_TEMPLATE.md` and pass `npm run validate`. See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for full guidelines.

## License

MIT — use freely, modify, distribute.

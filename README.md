# GTM Blueprints

**67 production go-to-market playbooks for AI agents.** Built for Claude Code, Cursor, Codex, Hermes, and any Agent Skills-compatible tool. Drop them in and your agent becomes a GTM operator.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-67-blue)](skills/)
[![CI](https://github.com/leadmagic/gtm-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/leadmagic/gtm-skills/actions/workflows/validate.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](docs/CONTRIBUTING.md)

---

## What This Is

A complete library of AI agent skills for go-to-market teams — cold email, sales prospecting, enrichment waterfalls, deliverability, competitive intel, pricing, ICP scoring, Clay automation, pitch decks, ROI calculators, founder-led growth, and more.

Every skill draws from established GTM authorities: **Winning by Design** (SPICED, Bowtie, POD structures, GTM Index), **Force Management** (MEDDICC, Command of the Message), **Gartner/Challenger**, **Huthwaite/SPIN**, **Sandler**, **April Dunford**, **Andy Raskin**, and others. Not generic advice — named frameworks applied to specific workflows with actionable outputs.

## Quick Install

```bash
# Claude Code
claude plugins add leadmagic/gtm-skills
claude skills install leadmagic/gtm-skills

# A specific category
claude skills install leadmagic/gtm-skills --category outbound
```

**Also works with:** Cursor (`.cursor/skills/`), Codex (`.agents/skills/`), Hermes Agent, Windsurf, OpenCode, and any Agent Skills-compatible tool.

```bash
# Manual install
git clone https://github.com/leadmagic/gtm-skills.git
# Point your agent's skill directory at the clone
```

## Skills Catalog

| # | Skill | Category | What It Does |
|---|---|---|---|
| 01 | `gtm-context` | foundation | Capture company context, ICP, GTM motion — foundation all skills consume |
| 02 | `icp-scoring` | foundation | Weighted ICP scoring with firmographic, technographic, behavioral dimensions |
| 03 | `positioning-messaging` | foundation | Dunford positioning, Raskin strategic narrative, messaging matrix |
| 04 | `competitive-intel` | foundation | Battlecards, competitive matrix, win/loss analysis |
| 05 | `pricing-strategy` | foundation | Ramanujam pricing models, tier design, WTP research |
| 06 | `lead-finding` | prospecting | Multi-source lead discovery — Apollo, Sales Nav, GitHub, job boards |
| 07 | `lead-enrichment` | prospecting | Waterfall enrichment, provider sequencing, confidence thresholds |
| 08 | `email-finding` | prospecting | Email discovery patterns, provider waterfall, verify after finding |
| 09 | `contact-verification` | prospecting | Pre-send verification, bounce prevention, data decay management |
| 10 | `list-building` | prospecting | Clay list building, ICP filtering, list hygiene |
| 11 | `signal-scoring` | prospecting | 4-category signal taxonomy, scoring formulas, tier routing |
| 12 | `data-enrichment-strategy` | prospecting | Provider landscape comparison, build-vs-buy, architecture design |
| 13 | `cold-email-strategy` | outbound | Sequence architecture, cadence design, channel mixing |
| 14 | `cold-email-copywriting` | outbound | 3-line framework, subject lines, personalization tiers |
| 15 | `email-deliverability` | outbound | SPF/DKIM/DMARC, warmup, reputation, bounce handling |
| 16 | `domain-infrastructure` | outbound | Secondary domains, mailbox provisioning, DNS auth |
| 17 | `sending-platforms` | outbound | Smartlead vs Instantly vs Salesforge vs Apollo comparison |
| 18 | `reply-handling` | outbound | 8-category classification, auto-reply playbooks, escalation |
| 19 | `multi-channel-outreach` | outbound | LinkedIn, cold calls, SMS, channel coordination |
| 20 | `inbound-triage` | inbound | Demo form triage, MQL/SQL routing, speed-to-lead |
| 21 | `content-marketing` | inbound | Content strategy by funnel, SEO/AEO, programmatic SEO |
| 22 | `social-selling` | inbound | LinkedIn Sales Navigator, DM sequences, SSI scoring |
| 23 | `landing-pages` | inbound | CRO audits, hero/offer/proof/CTA, conversion optimization |
| 24 | `sales-enablement` | sales-revops | Pitch decks, one-pagers, battlecards, playbooks |
| 25 | `meeting-prep` | sales-revops | Account research, SPIN/MEDDIC discovery, meeting briefs |
| 26 | `pipeline-management` | sales-revops | CRM hygiene, forecasting, stage definitions |
| 27 | `objection-handling` | sales-revops | 6-category taxonomy, AER framework, battlecards |
| 28 | `demo-scripts` | sales-revops | First demo, technical deep-dive, executive overview scripts |
| 29 | `deal-desk` | sales-revops | Pricing models, discount guidance, proposals |
| 30 | `campaign-analytics` | analytics | 6-layer metrics stack, diagnostic trees, benchmarking |
| 31 | `deliverability-monitoring` | analytics | Bounce tracking, spam placement, DMARC reports |
| 32 | `gtm-metrics` | analytics | Pipeline velocity, CAC/LTV, NRR, Rule of 40 |
| 33 | `a-b-testing` | analytics | Experiment design, statistical significance, stop/scale rules |
| 34 | `attribution` | analytics | Multi-touch models, UTM hygiene, campaign ROI |
| 35 | `proactive-alerts` | analytics | CRM pipeline alerts, buying signal alerts, Slack routing |
| 36 | `clay-automation` | automation | Clay tables, waterfalls, Claygent, CRM push, credit optimization |
| 37 | `ai-sdr-setup` | automation | AI SDR deployment, 4-week program, signal-to-action routing |
| 38 | `api-enrichment` | automation | REST API patterns, bulk enrichment, rate limiting |
| 39 | `crm-integration` | automation | HubSpot/Salesforce/Attio, lifecycle stages, deal stages |
| 40 | `mcp-setup` | automation | MCP server configuration, multi-MCP architecture |
| 41 | `n8n-automation` | automation | n8n workflows, webhook-to-enrichment pipelines |
| 42 | `waterfall-enrichment` | automation | Multi-provider waterfall, cost optimization, verification |
| 43 | `pitch-deck-builder` | design | Slide-by-slide structure, persona-customized, speaker notes |
| 44 | `one-pager-builder` | design | Product overviews, leave-behinds, champion enablement |
| 45 | `battlecard-builder` | design | FIA framework battlecards, Why We Win/Lose |
| 46 | `roi-calculator` | design | 3-scenario projections, payback, business case |
| 47 | `case-study-builder` | design | Customer success stories, before/after metrics |
| 48 | `design-system-gtm` | design | Brand-context for AI agents, visual identity, voice/tone |
| 49 | `ui-ux-gtm` | design | Landing pages, forms, dashboards, accessibility |
| 50 | `churn-prevention` | growth | Early warning signals, re-engagement, health scoring |
| 51 | `expansion-selling` | growth | Upsell triggers, cross-sell, NRR growth |
| 52 | `referral-programs` | growth | Partner/affiliate programs, comp structure |
| 53 | `customer-marketing` | growth | Case studies, testimonials, customer advocacy |
| 54 | `solo-founder-gtm` | founder-led | Tool stacks by stage, AI agents as org, hiring triggers |
| 55 | `founder-brand` | founder-led | LinkedIn strategy, content cadence, newsletter growth |
| 56 | `launch-planning` | founder-led | Launch tiers, Product Hunt, 16+ channel launches |
| 57 | `lead-magnets` | founder-led | Free tools, calculators, gated content |
| 58 | `sales-team-building` | founder-led | Hiring sequence by ARR, POD structures, comp models |
| 59 | `partner-programs` | founder-led | Co-marketing, integration partnerships, channel strategy |
| 60 | `investor-updates` | founder-led | Monthly updates, pitch decks, fundraising narrative |
| 61 | `saas-metrics-calculator` | founder-led | Complete calculator with stage-aware benchmarks |
| 62 | `leadmagic-cli` | leadmagic | CLI workflows for enrichment, validation, outbound push |
| 63 | `leadmagic-waterfall` | leadmagic | Clay waterfall with 95%+ coverage patterns |
| 64 | `leadmagic-mcp` | leadmagic | MCP server setup, 16 enrichment tools |
| 65 | `leadmagic-integrations` | leadmagic | LeadMagic + Clay/Apollo/Smartlead/Instantly/CRM |
| 66 | `leadmagic-bulk-enrichment` | leadmagic | CSV batch processing, webhook callbacks |
| 67 | `leadmagic-job-change` | leadmagic | Job change detection, champion tracking |

## Usage

```bash
# After installing, ask your agent:
"Score this list of companies against our ICP"
"Build a 5-email cold outreach sequence for VP Sales at Series B SaaS"
"Generate a competitive battlecard against Competitor X"
"Set up a waterfall enrichment workflow in Clay"
"Create a pitch deck for our new product launch"
"Calculate our SaaS metrics with benchmarks"
"Design our inbound lead triage workflow"
```

## Skill Structure

Every skill follows the [Agent Skills open standard](https://agentskills.io/specification) — `SKILL.md` with YAML frontmatter and Markdown body. Skills include step-by-step procedures, output templates, quality checklists, common pitfalls, and references to the GTM authorities their approaches draw from.

## Contributing

PRs welcome — see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines. All contributions must pass `npm run validate`.

**What contributors do:**
- Fix bugs or outdated references in existing skills
- Add new skills that fill gaps in the library
- Improve instructions, examples, and pitfalls
- Update benchmarks and provider references

**What makes a great contribution:**
- Grounded in real GTM practices, not just theory
- Frameworks and authorities cited by name
- No internal tooling details exposed
- Skill works without any specific paid tool

## LeadMagic

Several skills reference LeadMagic as an optional tool for email finding, validation, company enrichment, and job change detection. Every skill works without it — having an API key unlocks higher-accuracy data. [Get a free API key](https://leadmagic.io).

## License

MIT — use freely, modify, distribute. Built by [LeadMagic](https://leadmagic.io).

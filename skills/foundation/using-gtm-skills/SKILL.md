---
name: using-gtm-skills
description: >-
  Complete guide to using the gtm-skills repository — installation, skill
  discovery, skill loading, combining skills, taxonomy navigation, CLI
  workflows, and advanced patterns for every supported AI system (Claude Code,
  Jesse, Codex, Hermes, Windsurf, OpenCode, GitHub Copilot, Gemini CLI).
  The master key to the entire library. Use when first installing gtm-skills,
  discovering which skills to load, or building multi-skill workflows.
  Triggers on: "gtm-skills", "install gtm-skills", "how to use gtm-skills",
  "skill discovery", "which skills to load", "getting started with skills".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: foundation
  tags: [gtm-skills, installation, discovery, taxonomy, getting-started, master-guide]
  related_skills: [gtm-context, gtm-system-architecture, pipeline-management, sales-enablement, hiring-agencies, founder-sales, sales-team-building, skills-lock]
  frameworks:
    - "LeadMagic/gtm-skills — GTM agent skills catalog"
    - "Jacco van der Kooij (Winning by Design) — SPICED, Bowtie, GTM Index"
    - "Sam Jacobs (Pavilion) — CRO Council executive comp standards"
    - "Mark Roberge — The Sales Acceleration Formula"
    - "Jason Lemkin & Mark Roberge — From Survival to Thrival"
    - "Andy Whyte — MEDDICC Qualification & Scorecard"
    - "April Dunford — Obviously Awesome Positioning"
    - "Winning by Design — GTM Operating Model"
---

# Using gtm-skills

## Overview

205 skills. 24 categories. Every GTM discipline. This is the master key.
The mistake: cloning the repo and not knowing where to start — loading random
skills, missing dependencies, or treating skills as documentation instead of
executable playbooks. This skill covers the complete usage guide: installation,
discovery, loading patterns, multi-skill workflows, and advanced tactics for
getting maximum value from the gtm-skills library.

## Quick Start (I Need X → Pattern → Skills)

| I need to… | Load pattern | Start skills |
|---|---|---|
| Find any skill by category | — | `references/skill-index-master.md` |
| Build cold email outbound | Pattern 15c, 17, or 23 | `cold-email-strategy`, `email-deliverability`, `domain-infrastructure` |
| Build phone outbound | Pattern 15b | `cold-calling` + `references/cold-calling-experts-index.md` (incl. Jeb Blount Golden Hours) |
| Run discovery / qualify deals | Pattern 5 or 13 | `meeting-prep`, `pipeline-management`, `sales-coaching` |
| Hire GTM / RevOps / SDR | Pattern 2 or 28 | `gtm-role-descriptions`, `hiring-by-role`, `revenue-team-onboarding` |
| HR / comp / ramp for revenue team | Pattern 28 | `gtm-role-descriptions/references/hr-gtm-playbook.md` |
| Enterprise legal / MSA / DPA in deal | Pattern 29 or 16 | `deal-desk/references/legal-gtm-playbook.md` |
| RevOps automation maturity | Pattern 30 | `references/gtm-automation-expert-playbook.md` |
| CRO strategy / enterprise revenue leadership | Pattern 31 | `gtm-leadership/references/cro-enterprise-strategy.md` |
| Automate Clay / n8n | Pattern 6, 6b, or 30 | `references/automation-playbook-index.md` → `clay-automation` or `n8n-automation` |
| Monitor lifecycle health | Pattern 18 | `references/gtm-lifecycle-stages.md` → `references/lifecycle-skill-index.md` → `references/lincoln-murphy-customer-success.md` |
| Manage GTM spend / vendors | Pattern 11 | `revops-tech-stack`, `gtm-spend-management`, `gtm-tool-cost-model` |
| Run a GTM project / RACI | Pattern 19 | `gtm-operations`, `campaign-governance` |
| SEO + AI search content | Pattern 25 | `seo-strategy`, `pillar-pages`, `references/seo-strategy-playbook.md` |
| Inbound flywheel (HubSpot) | Pattern 27 | `content-marketing`, `references/dharmesh-shah-hubspot-inbound.md` |
| Demand creation (not lead gen) | Pattern 26 | `content-marketing`, `references/chris-walker-mental-models.md` |
| B2B influencer program | Pattern 21 | `customer-marketing`, `references/aneesh-wishly-b2b-influencer.md` |
| Founder PMF → scale | Pattern 12 | `solo-founder-gtm`, `saas-outcomes`, `engineer-to-founder` |
| Bootstrap founder path | Pattern 12 or 32 | `saas-outcomes` (`bootstrap-founder-playbook.md`), `solo-founder-gtm` |
| Earn-out / M&A deal terms | Pattern 15 or 32 | `exiting-company` (`negotiating-earn-out.md`), `financial-modeling` |
| Enterprise land-expand | Pattern 14 | `crm-toolkit`, `expansion-selling`, `multi-thread-orchestration` |
| Secure customer data exchange | Pattern 16 | `deal-desk`, `references/gtm-data-exchange-playbook.md` |
| Crisis / PR / incident comms | Pattern 33 | `gtm-leadership`, `references/crisis-management-playbook.md` |
| SaaS budget / MRR accounting / tax awareness | Pattern 34 | `financial-modeling`, `saas-metrics-calculator`, `references/gtm-budget-playbook.md` |
| Comp plan / OTE / quota design | Pattern 35 | `executive-compensation/references/gtm-compensation-strategy.md` |

**First install:** clone repo → ask agent to list skills → load this skill → pick row above.

## Category → Pattern Router

| Domain | Categories | Primary patterns |
|---|---|---|
| **Foundation** | `foundation/` | — (load first for ICP, positioning, pricing) |
| **Founder** | `founder-led/` | 2, 12, 15 |
| **Outbound** | `outbound/`, `prospecting/`, `tools/` (sequencers) | 15b, 15c, 17, 23 |
| **Inbound** | `inbound/`, `content-seo/`, `demand-gen/` | 25, 26, 27, 20 |
| **Ops** | `gtm-ops/`, `automation/`, `tools/`, `leadmagic/` | 6, 6b, 11, 19 |
| **Lifecycle** | `lifecycle/`, `customer-success/`, `growth/`, `product-led-growth/` | 18 |
| **Sales** | `sales-revops/`, `sales-plays/`, `abm/` | 5, 9, 13, 14, 22 |
| **Hiring** | `founder-led/`, `management-leadership/` | 2, 28, 35 |
| **Legal / deal** | `sales-revops/deal-desk`, `vendor-contracts` | 16, 29 |
| **Security** | `founder-led/` (soc2, privacy), `deal-desk` | 16, 29 |
| **Automation strategy** | `automation/`, `gtm-ops/` | 6, 6b, 30 |

Full category map (all skills): `references/skill-index-master.md`

## Pattern Index (1–30)

| # | Name | Domain | Trigger |
|---|---|---|---|
| 1 | Research → Build → Launch | General | New product / market entry |
| 2 | Hire → Onboard → Manage | Hiring | First GTM hire through ramp |
| 3 | Data → Decision → Action | Analytics | Metrics → expansion/churn |
| 4 | AI-First GTM (Vibe Stack) | Creative | AI content + landers at scale |
| 5 | WbD Sales Process Build | Sales | Design pipeline + SPICED |
| 6 | Clay GTM Stack | Ops | Clay tables + enrichment |
| 6b | n8n Orchestration | Ops | Inbound/outbound/MCP flows |
| 7 | Agency Pilot → In-House | Ops | Outsource then hire |
| 8 | Survival → Thrival → Enterprise | Founder | ARR-stage GTM motion |
| 9 | Stuck Late-Stage Deal (JOLT) | Sales | Buyer indecision |
| 10 | Reviews & Advocacy | Growth | G2 / TrustRadius |
| 11 | GTM Stack Finance & Spend | Ops | Ramp, vendors, TCO |
| 12 | Bootstrap vs Venture Outcome | Founder | Exit path + PMF gates |
| 13 | Sales Coaching System | Sales | REKS → MEDDICC → JOLT |
| 14 | Enterprise GTM (Benioff) | Sales | Land-expand, V2MOM |
| 15 | Exit Readiness & Valuation | Founder | Diligence prep |
| 15b | Phone-First Cold Calling | Outbound | Gilkey + Reisert + Pessar + Slocum |
| 15c | High-Scale Email Infra | Outbound | Eric Nowoslawski economics + deliverability |
| 16 | GTM Data Security | Security | Customer data exchange |
| 17 | Enrichment-Powered Outbound | Outbound | Pat Spielmann Cold to Gold |
| 18 | Lifecycle Stages & Activation | Lifecycle | 7-stage monitoring |
| 19 | GTM Project Management & RACI | Ops | Launches, migrations |
| 20 | Visitor ID & Intent Routing | Inbound | Website deanonymization |
| 21 | B2B Influencer GTM | Inbound | Creator partnerships |
| 22 | Relationship-Led Enterprise | Sales | Randy Seidl trust selling |
| 23 | Sales Borg Outbound | Outbound | Justin Michael automation |
| 24 | Force Management Alignment | Sales | Pod economics, Command of Message |
| 25 | B2B SEO Stack | Inbound | Schwartz + Fishkin + Ahrefs |
| 26 | Demand Creation | Inbound | Chris Walker dark social |
| 27 | Inbound Flywheel | Inbound | Dharmesh Shah / HubSpot attract-engage-delight |
| 28 | HR GTM / People Ops | Hiring | Stacey Nordwall + Pavilion comp |
| 29 | Legal GTM / Commercial Counsel | Legal / deal | Eunice Buhler + Ironclad CLM |
| 30 | RevOps Automation Maturity | Ops | Jen Igartua / Go Nimbly orchestration |
| 31 | CRO Enterprise Strategy | Leadership | John McMahon + consumption GTM |
| 32 | Founder Exit Economics | Founder | Earn-out negotiation + bootstrap exit paths |
| 33 | Crisis Management & Incident Comms | Leadership / CS | Outage, breach, bad press, war room |

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **LeadMagic/gtm-skills — GTM agent skills catalog.** Skill maps in this guide route tasks to the right playbook. Counts: `taxonomy.csv` / `skills.lock`.
- **Jacco van der Kooij (Winning by Design).** SPICED discovery, Bowtie lifecycle, GTM Index, REKS coaching — primary WbD cite.
- **Sam Jacobs (Pavilion).** CRO Council exec comp; multi-gate variable (ARR + NRR + efficiency).
- **Mark Roberge — The Sales Acceleration Formula.** Data-driven hiring, training, demand gen, and sales process design — the science behind scaling a B2B sales org.
- **Jason Lemkin & Mark Roberge — From Survival to Thrival.** Two-phase SaaS GTM: Survival ($0–$2M ARR, founder sells) → Thrival ($2M–$10M+, build the machine) → enterprise upmarket motion.
- **April Dunford — Obviously Awesome Positioning.** Positioning before messaging and channel selection.
- **Winning by Design — GTM Operating Model.** SPICED, Bowtie, POD structures, and revenue architecture.
- **Keenan — Gap Selling.** Current State → Future State → Gap discovery; Problem Centric™; happy ears guardrail — pairs with SPICED/MEDDICC.
- **Jordan Crawford — Blueprint GTM / Cannonball.** PQS, PVP, FIND — pain-based outbound from closed-won analysis.
- **Guillaume Moubeche — lemlist.** Problem-first multichannel sequences, CTC, 4–9 touches.
- **Becc Holland — Flip the Script.** Diagnostic Selling, Stellar Cold Email, lead-weighted SDR KPIs.
- **Eric Nowoslawski — Growth Engine X.** Cold email infra at scale, 1:1 backup inboxes, Creative Ideas campaigns, Crawl Walk Run Clay rollout, outbound unit economics gate.

## When to Use

Trigger phrases: "gtm-skills", "install gtm-skills", "how to use gtm-skills",
"which skill for [task]", "skill discovery", "find skill for [topic]",
"taxonomy navigation", "combine skills", "skill dependencies"

## Installation

Use `./install.sh` (wraps `scripts/install-tui.py`). Full per-system guide: `docs/INSTALL.md`.

| # | System | TUI key | Install path / method |
|---|---|---|---|
| 1 | Claude Code | `claude` | `claude plugins add LeadMagic/gtm-skills` |
| 2 | Jesse | `jesse` | `{project}/.jesse/skills/gtm-skills/` |
| 3 | Codex | `codex` | `codex skills install …` or `~/.codex/skills/gtm-skills/` |
| 4 | Hermes | `hermes` | `hermes skills install …` or `~/.hermes/skills/gtm-skills/` |
| 5 | Windsurf | `windsurf` | `{project}/.windsurf/skills/gtm-skills/` |
| 6 | OpenCode | `opencode` | `{project}/.opencode/skills/gtm-skills/` |
| 7 | Gemini CLI | `gemini` | `{project}/.gemini/skills/gtm-skills/` |
| 8 | GitHub Copilot | `copilot` | `{project}/.github/skills/gtm-skills/` + `copilot-instructions.md` |
| 9 | Zed | `zed` | `AGENTS.md` + `{project}/.zed/skills/gtm-skills/` |
| 10 | VS Code | `vscode` | Same as Copilot agent mode |
| 11 | Goose | `goose` | `~/.config/goose/skills/gtm-skills/` |

### Quick install

```bash
git clone https://github.com/LeadMagic/gtm-skills.git
cd gtm-skills
./install.sh                                              # default: Hermes + Claude + Jesse
./install.sh --target jesse --project /path/to/project
./install.sh --target hermes
./install.sh --target all --dry-run
```

### Verify installation

After install, ask your agent: "list gtm skills" or "what skills are available for [task]?"

### Integrity Check (skills.lock)
```bash
# Verify no tampered or corrupted skills
python3 -c "
import json, hashlib
with open('skills.lock') as f:
    lock = json.load(f)
for name, meta in lock['skills'].items():
    with open(meta['path'], 'rb') as fh:
        actual = hashlib.sha256(fh.read()).hexdigest()
    if actual != meta['sha256']:
        print(f'TAMPERED: {name}')
print('All skills verified.')
"
```

## Skill Discovery

### By Category (What You're Trying to Do)

| If You Need To... | Load These Categories |
|---|---|
| **Raise money, manage equity, run a board** | `founder-led/` (fundraising-strategy, financial-modeling, board-meeting-prep, equity-management) |
| **Sell as a founder or build a sales team** | `founder-led/` (founder-sales, sales-team-building), `sales-revops/` (sales-enablement, pipeline-management, demo-scripts, deal-desk) |
| **Enterprise sales / upmarket motion** | `foundation/` (icp-targeting-tiers, gtm-context), `abm/` (abm-strategy, multi-thread-orchestration), `sales-revops/` (meeting-prep, deal-desk, roi-calculator), `founder-led/` (soc2-compliance) |
| **Mark Roberge / Survival to Thrival journey** | See skill maps below — routes by ARR stage and motion |
| **Journey / PMF / scale gates** | `saas-outcomes` + `solo-founder-gtm` — see Journey skill map below |
| **Build outbound / cold email** | `outbound/` (cold-email-strategy, cold-email-copywriting, email-deliverability, domain-infrastructure) — Pattern 23 (Justin Michael / Sales Borg), Pattern 15c (Eric Nowoslawski infra), or Pattern 17 (Pat Spielmann / enrichment-powered Cold to Gold) · router → `references/gtm-experts-outbound-index.md` |
| **Build outbound / cold calling (phone-first)** | `outbound/cold-calling` — Pattern 15b (Gilkey + Reisert + Pessar + Slocum); `references/cold-calling-experts-index.md` |
| **Find and enrich leads** | `prospecting/` (lead-finding, lead-enrichment, email-finding, contact-verification) |
| **Automate GTM workflows** | `references/automation-playbook-index.md` (38 playbooks) → `automation/` + `tools/` + `leadmagic/` + `gtm-ops/` |
| **Configure outreach sequencers** | `tools/sequencing-toolkit` (router) + platform skills: `instantly-sequences`, `smartlead-workflows`, `lemlist-setup`, `salesloft-cadences`, `outreach-sequences`, `hubspot-sequences` — Pattern 17 clay-enrollment-handoff |
| **LeadMagic enrichment & integrations** | `leadmagic/` (waterfall, integrations, cli, bulk, mcp, job-change) + `clay-toolkit` + `clay-loops-toolkit` |
| **SEO / content clusters** | `content-seo/` (seo-strategy, pillar-pages, pseo-strategy, aeo-strategy) + `references/seo-strategy-playbook.md` |
| **Demand creation (not lead gen)** | `content-marketing`, `paid-social-strategy`, `attribution` + `references/chris-walker-mental-models.md` |
| **Sales org alignment / pod economics** | `sales-team-building`, `gtm-leadership`, `gtm-metrics` + `references/force-management-playbook.md` |
| **n8n flows (inbound/outbound/signals)** | `tools/n8n-toolkit` (flow catalog, MCP patterns) → motion skill (`inbound-triage`, `reply-handling`, signal plays) |
| **Clay + AI prompts (tools)** | `tools/clay-toolkit`, `tools/clay-loops-toolkit`, `tools/ai-prompts-toolkit`, `tools/sequencing-toolkit`, `leadmagic/` |
| **Content, social, creative** | `creative/` (vibe-marketing, ai-content-creation, copywriting, social-media-strategy), `content-seo/` |
| **Customer success and support** | `customer-success/` (cs-playbooks, customer-onboarding, sla-management, headless-support, support-tool-stack) — BYOAI: Plain MCP + `byoai-headless-stack.md` |
| **Lifecycle stages & activation monitoring** | `references/gtm-lifecycle-stages.md` → Pattern 18 · `references/activation-playbook.md` · `references/lifecycle-skill-index.md` |
| **Analytics and metrics** | `analytics/` (gtm-metrics, event-analytics, campaign-analytics, attribution) |
| **AI-native GTM (vibe coding/marketing)** | `creative/` (vibe-coding, vibe-marketing, v0-lander, ai-content-creation, ai-video-creation) |
| **Legal, compliance, security** | `founder-led/` (legal-for-founders, soc2-compliance, data-privacy-compliance, security-assessments, business-insurance) |
| **GTM data security / customer data exchange** | `deal-desk`, `customer-onboarding`, `revenue-team-onboarding`, `revops-tech-stack` + `references/gtm-data-exchange-playbook.md`, `references/gtm-security-hygiene-basics.md` |
| **Hiring and team building** | `founder-led/` (gtm-role-descriptions, gtm-recruiting, job-posting-strategy, hiring-by-role, sales-team-building) + `management-leadership/gtm-leadership` |
| **CRO / enterprise $100M–$1B strategy** | Pattern 31 · `gtm-leadership/references/cro-enterprise-strategy.md` |
| **Hire GTM Engineer / RevOps builder** | `gtm-role-descriptions` (JD + `gtm-engineer-hiring.md`) → `hiring-by-role` (`gtm-engineer-scorecard.md`) → `revenue-team-onboarding` |
| **GTM leadership (hire/fire/hard talks)** | `management-leadership/gtm-leadership`, `gtm-role-descriptions` (comp templates), `employment-compliance` |
| **Buyer indecision / stuck deals** | `sales-revops/buyer-indecision` (JOLT), `pipeline-management`, `deal-desk` |
| **Sales process design (Winning by Design)** | See WbD skill map below — `pipeline-management` is the anchor |
| **Outsource GTM / work with agencies** | `founder-led/` (hiring-agencies, hiring-contractors), `automation/` (clay-automation) |
| **Design and brand** | `design/` (pitch-deck-builder, roi-calculator, design-system-gtm, brand-kit) |
| **GTM ops / RevOps / tool spend** | `gtm-ops/` (`gtm-operations`, `revops-tech-stack`, `gtm-tool-cost-model`, `gtm-spend-management`, `campaign-governance`) — Pattern 11 |
| **GTM project management / RACI / ClickUp** | `gtm-operations` (PM hub), `campaign-governance` (launch RACI), `gtm-leadership` (pods) — Pattern 19 |
| **Community-led / reverse demo selling** | `growth/customer-marketing`, `sales-revops/demo-scripts` (Varun Anand references) |
| **B2B influencer / LinkedIn creator GTM** | `customer-marketing`, `social-selling` + `references/aneesh-wishly-b2b-influencer.md` — Pattern 21 |
| **HR / People Ops for revenue team** | `gtm-role-descriptions`, `revenue-team-onboarding` + `hr-gtm-playbook.md` — Pattern 28 |
| **Legal / MSA / DPA in enterprise deal** | `deal-desk` + `legal-gtm-playbook.md` — Pattern 29 |
| **RevOps automation strategy** | `gtm-operations`, `revops-tech-stack` + `gtm-automation-expert-playbook.md` — Pattern 30 |
| **CRO / enterprise revenue leadership** | `gtm-leadership` + `cro-enterprise-strategy.md` — Pattern 31 |
| **Crisis / outage / breach / PR incident** | Pattern 33 · `gtm-leadership` + `crisis-management-playbook.md` |
| **Annual GTM budget / MRR bridge / SaaS tax awareness** | Pattern 34 · `gtm-budget-playbook.md` + `saas-mrr-accounting-nuances.md` |
| **ZoomInfo-scale SDR / data-as-product GTM** | `founder-led/sales-team-building` → `henry-schuck-sdr-model` reference |

### By Trigger Phrase

```
Tell your agent: "I need to [task]"
It will match to the right skill automatically.

Examples:
- "I need to build a pitch deck" → pitch-deck-builder
- "I need to set up cold email infrastructure" → Pattern 15c (Eric Nowoslawski) → domain-infrastructure, inbox-setup, email-deliverability
- "Eric Nowoslawski / Growth Engine X / cold email at scale" → Pattern 15c · `cold-email-strategy/references/eric-nowoslawski-outbound.md`
- "Creative Ideas campaign / Crawl Walk Run Clay" → cold-email-strategy (eric-nowoslawski-outbound.md), clay-automation
- "Cold calling / phone outreach / SDR dialing / connect rate" → Pattern 15b · `outbound/cold-calling` · `references/cold-calling-experts-index.md`
- "Bucketing / disposition science / phone intent" → cold-calling, list-building, pipeline-management (Gilkey vs Reisert — see cold-calling-experts-index)
- "Ryan Reisert / CRM activity buckets / CallBlitz" → cold-calling, pipeline-management, sales-coaching
- "Ronen Pessar / ColdCall-Market Fit / Call Pilot" → cold-calling, sales-team-building
- "Tom Slocum / sell the meeting / 3x3 research / SD Lab" → cold-calling, sales-coaching
- "Coach SDR cold calls / phone rep coaching" → sales-coaching + cold-calling (Slocum + Reisert CallBlitz)
- "I need to raise a seed round" → fundraising-strategy, yc-ecosystem, vc-outreach
- "I need to build a landing page with AI" → v0-lander, vibe-coding
- "I need to hire my first salesperson" → sales-team-building, gtm-role-descriptions, hiring-by-role, job-posting-strategy
- "Write a job description for SDR/AE/VP Sales" → gtm-role-descriptions → job-posting-strategy → hiring-by-role
- "Hire GTM engineer / GTM Engineer vs RevOps" → gtm-role-descriptions (`gtm-engineer-hiring.md`, `gtm-engineer-jd.md`) → hiring-by-role (`gtm-engineer-scorecard.md`)
- "Revenue org structure / sales comp plan" → gtm-role-descriptions, sales-team-building
- "Fire sales rep / difficult conversation / PIP" → gtm-leadership, employment-compliance
- "When to fire VP Sales" → gtm-leadership, sales-team-building
- "CRO strategy / John McMahon / enterprise sales leadership" → Pattern 31 · `cro-enterprise-strategy.md`
- "Snowflake GTM / consumption model / Slootman" → Pattern 31 · `expansion-selling`, `executive-compensation`
- "Databricks PLG to enterprise / Ron Gabrisko" → Pattern 31 · `sales-team-building`, `gtm-leadership`
- "Developer selling / sell to developers / Vercel GTM / DevRel / open-source GTM" → developer-gtm (vercel-developer-selling.md), plg-strategy
- "Buyer indecision / JOLT / need to think about it" → buyer-indecision, pipeline-management
- "SDR/AE comp plan template" → gtm-role-descriptions (comp-plan-sdr, comp-plan-ae)
- "Recruit passive AE / close candidate" → gtm-recruiting, gtm-role-descriptions, hiring-by-role
- "Negotiate sales offer / counter offer" → gtm-recruiting (offer-negotiation), employment-compliance
- "Betts recruiting / Destiny recruiting / diversity GTM hire" → gtm-recruiting
- "Scale sales like Mark Roberge / HubSpot" → sales-team-building, pipeline-management, sales-enablement
- "Survival to Thrival enterprise sales" → founder-sales → sales-team-building → icp-targeting-tiers → multi-thread-orchestration
- "Design sales process Winning by Design" → gtm-system-architecture → pipeline-management → sales-enablement
- "Hire an outbound agency" → hiring-agencies, pipeline-management, cold-email-strategy
- "MEDDICC qualify this deal" → meeting-prep, pipeline-management, sales-coaching
- "Gap Selling discovery" / "happy ears" → meeting-prep (keenan-gap-selling.md), pipeline-management
- "PQS / PVP outbound" / "Cannonball GTM" → cold-email-strategy (jordan-crawford-blueprint-gtm.md), list-building
- "Creative Ideas campaign" / "Eric Nowoslawski" / "Growth Engine X" / "outbound at scale" / "backup inboxes" → cold-email-strategy (eric-nowoslawski-outbound.md), email-deliverability, domain-infrastructure
- "Leslie Venetz" / "earn the right" / "buyer-first outbound" / "profit-generating pipeline" / "fix broken outbound" → cold-email-strategy (leslie-venetz-buyer-first-outbound.md), cold-email-copywriting
- "Crawl walk run Clay" / "should we do cold outbound" → clay-automation, cold-email-strategy (eric-nowoslawski-outbound.md)
- "lemlist sequence" / "Guillaume cold email" → lemlist-setup, cold-email-strategy (lemlist-guillaume-outbound.md)
- "Clay loop for funding signals" → clay-loops-toolkit, ai-prompts-toolkit, funding-signal-play
- "Claygent prompt for research" → ai-prompts-toolkit, clay-toolkit
- "Prompt loop for outbound email" → ai-prompts-toolkit, cold-email-copywriting, clay-toolkit
- "Build n8n inbound lead workflow" → n8n-toolkit (INB-01), inbound-triage, crm-toolkit
- "n8n outbound enrichment pipeline" → n8n-toolkit (OUT-01), leadmagic-toolkit
- "n8n reply classification webhook" → n8n-toolkit (LIF-03), reply-handling, ai-prompts-toolkit
- "Connect MCP agent to n8n batch job" → mcp-setup, n8n-toolkit (MCP-01), leadmagic-mcp
- "Headless support / BYOAI / Plain MCP / embed support in app" → headless-support (byoai-headless-stack.md), mcp-setup, support-tool-stack
- "Attio + support stack / API-first CRM and support" → crm-toolkit (crm-selection.md), attio-setup, headless-support (byoai-headless-stack.md)
- "Signal automation funding/job change" → n8n-toolkit (SIG-01/02) or clay-loops-toolkit
- "Clay reverse demo / Varun Anand demo" → demo-scripts → reverse-demo-varun reference
- "Community selling / Slack GTM / ecosystem-led growth" → customer-marketing → community-selling-varun reference
- "ZoomInfo GTM / Henry Schuck SDR model" → sales-team-building → henry-schuck-sdr-model reference
- "SDR economics / cost per meeting / Tito Bohrt / SDR hiring simulation" → sales-team-building (tito-bohrt-sdr-science.md), gtm-role-descriptions
- "ABSD / account-based sales development / Lars Nilsson / targeted enterprise outbound" → abm-strategy (lars-nilsson-absd.md), account-selection, cold-email-strategy
- "Hire GTM engineer / RevOps engineer" → gtm-role-descriptions → hiring-by-role (gtm-engineer scorecard)
- "GTM stack TCO / Ramp / vendor spend audit" → Pattern 11 (revops-tech-stack → gtm-spend-management)
- "Lifecycle stages / activation / time-to-value / monitor lifecycle" → Pattern 18 (`references/gtm-lifecycle-stages.md` → `activation-playbook.md` → monitoring dashboard)
- "Exchange customer data safely / onboarding data import" → Pattern 16 (deal-desk → customer-onboarding; `gtm-data-exchange-playbook.md`)
- "Security hygiene for sales team / 2FA / phishing for reps" → `revenue-team-onboarding` + `gtm-security-hygiene-basics.md`
- "When does security review hit the deal / security questionnaire" → `deal-desk` + `security-questionnaire-deal-guide.md`
- "Relationship selling / enterprise trust / Randy Seidl" → Pattern 22 (social-selling → sales-coaching → multi-thread)
- "What pitfalls to avoid across skills?" → references/pitfalls-index.md (auto-generated catalog)
- "Smartlead setup / Eric infra at scale" → smartlead-workflows, email-deliverability (eric-nowoslawski-outbound.md)
- "Instantly campaign setup" → instantly-sequences, domain-infrastructure
- "LeadMagic Clay waterfall" → leadmagic-waterfall, clay-toolkit, pat-spielmann-outbound-copy.md
- "LeadMagic integration checklist" → leadmagic-integrations, integration-checklist.md
- "Push verified contacts to sequencer" → leadmagic-cli, smartlead-workflows or instantly-sequences
- "Job change champion tracking" → leadmagic-job-change, clay-loops-toolkit (L03), job-change-play
- "List all automation playbooks" → references/automation-playbook-index.md (38 playbooks)
- "B2B SEO strategy / Product-Led SEO" → seo-strategy, references/seo-strategy-playbook.md
- "Pod economics / sales org alignment / Force Management" → sales-team-building, references/force-management-playbook.md
- "HubSpot inbound / flywheel / Dharmesh Shah" → Pattern 27 · `references/dharmesh-shah-hubspot-inbound.md` · `content-marketing`, `inbound-triage`, `hubspot-setup`
- "Demand creation / dark social / Chris Walker" → Pattern 26 · content-marketing, references/chris-walker-mental-models.md
- "Marketing frequency / revenue leader development" → references/chris-walker-mental-models.md, gtm-leadership
- "B2B influencer / LinkedIn creator / Wishly / Aneesh Lal" → Pattern 21 (customer-marketing → social-selling → gtm-metrics)
- "LinkedIn algorithm / reach drop / carousel vs video / van der Blom" → linkedin-algorithm (richard-van-der-blom-algorithm.md), social-selling
- "LinkedIn Live / livestream / WinsDay / Jessie Lizak / Reveting / weekly live show" → linkedin-live-strategy (jessie-lizak-linkedin-live.md), linkedin-algorithm
- "Sales Navigator / Sales Nav / Morgan Ingram / AMP Social / filter-specific messaging / posted in last 30 days" → sales-navigator-prospecting (morgan-ingram-sales-navigator.md), social-selling
- "Founder LinkedIn / build in public / Adam Robinson / zero-click content" → founder-brand (adam-robinson-founder-brand.md), linkedin-algorithm
- "Influencer ROI / creator attribution / influencer UTM" → references/b2b-influencer-measurement.md, campaign-governance
- "Employee advocacy vs paid creators" → customer-marketing Phase 6, references/b2b-influencer-strategy.md
- "HR for sales team / People Ops GTM / Stacey Nordwall" → Pattern 28 · hr-gtm-playbook.md · gtm-role-descriptions
- "Revenue comp bands / Pavilion comp / SDR OTE" → Pattern 28 · comp-benchmarks.md · benchmark-reconciliation.md
- "GTM comp strategy / OTE design / quota plan / accelerators / SPIF" → Pattern 35 · gtm-compensation-strategy.md · ote-calculator-template.md
- "Crisis management / outage comms / breach email / holding statement / PR crisis" → Pattern 33 · crisis-management-playbook.md · gtm-leadership
- "GTM budget / annual operating budget / MRR accounting / bookings vs revenue / QSBS / 409A / SaaS sales tax" → Pattern 34 · gtm-budget-playbook.md · saas-mrr-accounting-nuances.md
- "MSA / DPA / sales legal / Eunice Buhler / Ironclad" → Pattern 29 · legal-gtm-playbook.md · deal-desk
- "When to sign DPA / commercial counsel / deal desk swimlanes" → Pattern 29 + Pattern 16 (data exchange)
- "RevOps automation / Jen Igartua / Go Nimbly / automation maturity" → Pattern 30 · gtm-automation-expert-playbook.md
- "Clay vs n8n orchestration / fix automation sprawl" → Pattern 30 strategy → Pattern 6/6b implementation
```

### Skill Map: Winning by Design — Sales Process & GTM System

WbD organizes revenue as a system, not a funnel. Load skills by model:

| WbD Component | What It Covers | Load These Skills |
|---|---|---|
| **GTM Index (6 models)** | Revenue, Data, Math, Operating, Growth, GTM — score 1–10 | `gtm-system-architecture`, `gtm-metrics` |
| **GTM Playbook Kit** | Goal + Actions + Exit Criteria per stage | `pipeline-management` (anchor) |
| **SPICED** | Situation, Pain, Impact, Critical Event, Decision (discovery) | `pipeline-management`, `meeting-prep`, `founder-sales` |
| **MEDDICC** | Metrics, EB, Decision Criteria/Process, Pain, Champion, Competition (deal scoring) | `pipeline-management`, `meeting-prep`, `sales-coaching`, `multi-thread-orchestration` |
| **Bowtie** | Acquire → retain → expand (revenue doesn't end at Closed Won) | `gtm-system-architecture`, `customer-onboarding`, `expansion-selling` |
| **POD structures** | SDR:AE:CSM ratios by complexity | `sales-team-building` |
| **REKS coaching** | Results → Efforts → Knowledge → Skills | `sales-coaching`, `sales-team-building` |
| **Enablement layer** | Playbook, battlecards, talk tracks per stage | `sales-enablement`, `demo-scripts`, `objection-handling` |

**Full WbD sales process stack:**
```
gtm-context → gtm-system-architecture (score the 6 models)
→ pipeline-management (stages + SPICED + handoffs)
→ sales-enablement (playbook assets per stage)
→ sales-coaching (REKS + deal inspection)
→ sales-team-building (PODs + hiring when Operating Model ≥6)
```

**SPICED + MEDDICC rule:** They do not contradict. SPICED runs discovery
conversations; MEDDICC scores deal evidence. Same CRM fields — see
`pipeline-management` reconciliation table. Never use both as competing checklists.

**Gap Selling layer:** Keenan adds diagnostic depth — current/future/gap, root
cause, emotions, Problem Identification Chart. Use on discovery calls (`meeting-prep`
→ `keenan-gap-selling.md`); fold Impact into SPICED + MEDDICC Metrics.

### Skill Map: Outbound & Discovery Experts

Router index → `references/gtm-experts-outbound-index.md`

| Task | Skill | Lead expert / artifact |
|---|---|---|
| Discovery call prep | `meeting-prep` | Keenan Gap Selling + SPICED + MEDDICC gaps |
| Discovery stage gates | `pipeline-management` | Gap Selling exit criteria (no happy ears) |
| Sequence architecture | `cold-email-strategy` | Becc Holland structure · Guillaume multichannel · Jordan PQS/PVP |
| Write cold email copy | `cold-email-copywriting` | Becc 7 Pillars · Guillaume CTC · Crawford PVP bar |
| Low reply rates (good infra) | `cold-email-strategy` + `list-building` | Jordan Crawford FIND — fix message before volume |
| lemlist campaign setup | `lemlist-setup` | Guillaume playbook (canonical multichannel) |
| Email + LinkedIn coordination | `multi-channel-outreach` | Guillaume · Becc sequence structure |
| SDR KPI / inbound-outbound conflict | `sales-team-building` | Becc Holland lead weighting |
| Infra at scale / deliverability | `email-deliverability`, `domain-infrastructure` | Eric Nowoslawski — `eric-nowoslawski-outbound.md` |
| Creative Ideas / offer-led AI copy | `cold-email-copywriting`, `clay-automation` | Eric Nowoslawski Crawl Walk Run |
| Outbound unit economics gate | `cold-email-strategy` | Eric TAM/LTV/CAC:LTV criteria |

**Creative outbound stack (reply rate rescue):**
```
list-building (PQS from won deals) → cold-email-strategy (FIND + triggers)
→ cold-email-copywriting (PVP/CTC copy) → lemlist-setup or sending-platforms
```

**Discovery stack:**
```
meeting-prep (Gap Selling + SPICED questions) → pipeline-management (stage evidence)
→ sales-coaching (MEDDICC deal review)
```

**WbD + agency rule:** Do not hire agencies until Operating Model ≥6.
Load `pipeline-management` before `hiring-agencies` — agencies execute your
playbook, they do not write it.

### Skill Map: ABM Gifting (Giftology / Sendoso)

| Task | Skill | Artifact |
|---|---|---|
| Gift strategy | `strategic-gifting` | Giftology + tier budget |
| Tier 1 executive gift | `strategic-gifting` + `abm-1-to-1` | gift-brief template |
| Sendoso campaign | `strategic-gifting` | sendoso-campaign template |
| Direct mail + email sync | `strategic-gifting` + `abm-1-to-few` | gifting-sequence reference |
| Buyer gift policy | `strategic-gifting` | gift-compliance reference |
| Stalled deal | `buyer-indecision` | Not gifts |

### Skill Map: Sales Coaching

| Task | Skill | Artifact |
|---|---|---|
| Build coaching program | `sales-coaching` | Full cadence + artifact index |
| Rep missing quota | `sales-coaching` | reks-diagnostic template |
| Weekly 1:1 | `sales-coaching` | 1-1-agenda template |
| Deal review | `sales-coaching` + `pipeline-management` | deal-review-scorecard template |
| Call feedback | `sales-coaching` | call-coaching-form template |
| Late-stage stall | `buyer-indecision` + `sales-coaching` | jolt-coaching reference |
| Founder coaches team | `sales-coaching` | founder-coaching reference |
| Coach before fire | `gtm-leadership` + `sales-coaching` | coaching-plan-30-day template |

### Skill Map: Founder Comp & Negotiation

| Task | Skill | Why |
|---|---|---|
| Can we afford first AE? | `founder-comp-playbook` | Payroll % ARR + runway |
| Set OTE + quota | `executive-compensation` (Pattern 35) | gtm-compensation-strategy + ote-calculator-template |
| IC comp bands + templates | `gtm-role-descriptions` | H1 2026 comp-benchmarks |
| Interviewer questions | `hiring-by-role` | interviewer-questions-gtm by role |
| GTM Engineer JD + interview | `gtm-role-descriptions` → `hiring-by-role` | gtm-engineer-hiring.md + gtm-engineer-scorecard.md |
| Candidate questions | `hiring-by-role` | candidate-questions-to-ask (both sides) |
| New hire week 1 | `revenue-team-onboarding` | onboarding-questions + questionnaire |
| Rep resigned | `gtm-leadership` | resignation-playbook + handoff checklist |
| Exit interview | `gtm-leadership` | exit-interview-questions |
| Candidate wants more $ | `founder-comp-playbook` | Scripts + lever matrix |
| Explain equity to hire | `founder-comp-playbook` | FD% + 409A walkthrough |
| Close / written offer | `gtm-recruiting` | 48–72h timeline |

### Skill Map: Executive Comp (Sam Jacobs / Pavilion)

| Task | Skill | Why |
|---|---|---|
| VP / CRO offer + clauses | `executive-compensation` | Multi-gate variable, severance, equity, clawback |
| IC comp plans | `gtm-role-descriptions` | SDR/AE/manager templates |
| Board approval | `executive-compensation`, `board-meeting-prep` | Comp memo + scenario payout |
| Pavilion peer benchmarks | `executive-compensation` | pavilion-cro-comp reference |

### Skill Map: CRM (tools/crm-toolkit)

| Task | Skill | Why |
|---|---|---|
| Choose CRM | `crm-toolkit` | crm-selection scorecard |
| Contacts vs leads | `crm-toolkit` | contacts-vs-leads reference |
| Platform rollout | `hubspot-setup`, `salesforce-setup`, `attio-setup` | After operating model in `crm-integration` |
| Implementation partner | `crm-toolkit` | implementation-partners RFP |
| Land-and-expand in CRM | `crm-toolkit` + `expansion-selling` | benioff-enterprise-playbook + land-expand template |
| Annual GTM planning | `gtm-leadership` | V2MOM template (Marc Benioff) |
| Enterprise trust selling | `transparency-selling` + `crm-toolkit` | Commitment logging + radical honesty |

### Skill Map: GTM Spend (Ramp / vendors)

| Task | Skill | Why |
|---|---|---|
| Model tool TCO | `gtm-tool-cost-model` | Seat + credit + % ARR |
| Ramp + card policy | `gtm-spend-management` | Virtual card per vendor |
| Vendor roster / renewals | `gtm-spend-management` | vendor-spend-register |
| Approve new SaaS | `gtm-spend-management` + `revops-tech-stack` | Approval matrix + overlap check |
| Negotiate renewal | `vendor-contracts` + spend register | T-90 workflow |
| Zombie subscriptions | `gtm-spend-management` | Quarterly cleanup |
| Gifting spend on Ramp | `strategic-gifting` + `gtm-spend-management` | Capped GTM-GIFT card |

### Skill Map: Reviews (G2 / TrustRadius)

| Task | Skill | Why |
|---|---|---|
| Review strategy | `review-platforms` | Generation, responses, grid ranking |
| Advocacy program | `customer-marketing` | Case studies + references |
| Negative review response | `review-platforms` | review-response-playbook |

### Skill Map: Varun Anand — Reverse Demo & Community Selling

| Task | Skill | Artifact |
|---|---|---|
| Buyer-led screen-share demo | `demo-scripts` | `skills/sales-revops/demo-scripts/references/reverse-demo-varun.md` |
| Community → pipeline | `customer-marketing` | `skills/growth/customer-marketing/references/community-selling-varun.md` |
| Clay-style ecosystem GTM | `customer-marketing` + `startup-communities` | Slack onboarding + creator loops |
| Pair with discovery | `meeting-prep` | Great Demo! incumbent walkthrough before reverse demo |

### Skill Map: Henry Schuck — ZoomInfo Scale GTM

| Task | Skill | Artifact |
|---|---|---|
| High-velocity SDR taxonomy | `sales-team-building` | `skills/founder-led/sales-team-building/references/henry-schuck-sdr-model.md` |
| Inbound SDR machine | `sales-team-building` + `revenue-team-onboarding` | ramp-benchmarks (inbound SDR) |
| Public-company GTM KPIs | `gtm-metrics` | `public-company-gtm-metrics` reference |
| Data-as-product routing | `sales-team-building` + `lead-enrichment` | Intent + enrichment queue design |

### Skill Map: GTM Ops Cluster

Router: `gtm-operations` → `skills/gtm-ops/gtm-operations/references/gtm-ops-skill-index.md`. Load order for new RevOps hire:

1. `revops-tech-stack` — inventory + bowtie map
2. `gtm-tool-cost-model` — TCO budget
3. `gtm-spend-management` — Ramp + vendor register
4. `crm-integration` — sync rules
5. `campaign-governance` — UTMs + naming
6. `gtm-operations` Phase 6 — PM tool, charter, RACI

Pattern 11 covers finance + spend. Pattern 19 covers launches, migrations, QBR projects.

| PM task | Skill | Artifact |
|---|---|---|
| Run any GTM project | `gtm-operations` | `gtm-project-management-playbook.md` |
| ClickUp workspace | `gtm-operations` | `clickup-gtm-workspace.md` |
| RACI + charter | `gtm-operations` | `raci-matrix-template.md`, `gtm-project-charter.md` |
| Campaign launch ownership | `campaign-governance` | RACI Example 1 + UTM sheet |
| Stack migration | `revops-tech-stack` + `gtm-operations` | RACI Example 2 |
| Launch pod design | `gtm-leadership` + `gtm-operations` | `team-design-gtm-projects.md` |

### Skill Map: Working with Agencies

| Scenario | Load These Skills | Why |
|---|---|---|
| Outbound agency evaluation | `hiring-agencies`, `pipeline-management`, `cold-email-strategy` | Process + messaging before outsourcing sends |
| RevOps / Clay agency | `hiring-agencies`, `clay-automation`, `crm-integration` | Workflow spec before agency builds |
| Agency proved channel — hire in-house | `sales-team-building`, `hiring-by-role`, `hiring-agencies` (transition section) | Graduate playbook to employees |
| Agency → GTM Engineer FTE | `gtm-role-descriptions`, `hiring-by-role`, `revenue-team-onboarding` | JD + scorecard + day-0 Clay/n8n access |
| Freelancer vs agency | `hiring-contractors`, `hiring-agencies` | Individual vs team engagement |
| Demand gen agency | `hiring-agencies`, `paid-advertising`, `campaign-analytics` | CAC measurement from day one |

### Skill Map: Andy Whyte — MEDDICC Qualification

Andy Whyte operationalizes MEDDICC as a 0/1/2 scorecard (max 14) with stage
gates and "Always Be Qualifying." Load skills by task:

| MEDDICC Task | Skill | Why |
|---|---|---|
| Design scorecard + CRM fields | `pipeline-management` | Anchor — stage gates, SPICED reconciliation |
| Pre-call questions per dimension | `meeting-prep` | SPICED for discovery; MEDDICC gaps for qualification |
| Manager deal review | `sales-coaching` | Evidence inspection, not rep confidence |
| Champion + buying committee | `multi-thread-orchestration` | Champion test + stakeholder map |
| Metrics / business case | `roi-calculator`, `deal-desk` | M and E dimensions |
| Competition dimension | `competitive-intel` | Influence decision criteria |
| CRM configuration | `crm-integration`, `hubspot-setup`, `salesforce-setup` | Scorecard fields |

**MEDDICC seven dimensions (Whyte presentation):**

| Letter | Dimension | Score 2 Requires |
|---|---|---|
| M | Metrics | Buyer-defined KPIs with baseline + target |
| E | Economic Buyer | Met directly, budget authority confirmed |
| D | Decision Criteria | Documented evaluation criteria |
| D | Decision Process | Steps, approvers, dates mapped |
| I | Identify Pain | Quantified cost of inaction |
| C | Champion | Passes four-part test (power, win, articulation, internal sell) |
| C | Competition | Named competitors + status quo assessed |

**Stage gates (consultative):** Solution ≥6/14 | Proposal ≥10/14 | Negotiation ≥12/14 | Commit ≥13/14

**Full MEDDICC stack:**
```
pipeline-management (scorecard + gates) → meeting-prep (questions + gaps)
→ sales-coaching (deal review) → competitive-intel + roi-calculator (C + M)
```

### Skill Map: Mark Roberge — Sales Acceleration Formula

Roberge built HubSpot's sales machine on four pillars. Load skills by pillar:

| Roberge Pillar | What It Covers | Load These Skills |
|---|---|---|
| **Hiring** | Coachable, Curious, Prior success, Intelligent, Work ethic — hire for traits, train for skills | `sales-team-building`, `hiring-by-role`, `job-posting-strategy` |
| **Training** | Scalable onboarding, documented playbook, role-play, call review | `sales-enablement`, `demo-scripts`, `sales-coaching` |
| **Demand generation** | Marketing-sales alignment, inbound + outbound balance, lead quality over volume | `cold-email-strategy`, `inbound-triage`, `gtm-metrics`, `campaign-analytics` |
| **Sales process** | Data-driven stages, conversion metrics per step, inspect what you expect | `pipeline-management`, `meeting-prep`, `gtm-metrics` |

**Full Roberge stack (building the machine):**
```
gtm-context → founder-sales → pipeline-management → sales-enablement
→ sales-team-building → hiring-by-role → sales-coaching → gtm-metrics
```

### Skill Map: Survival to Thrival — Enterprise Sales

*From Survival to Thrival* (Lemkin + Roberge) defines two phases. Enterprise is a Thrival-stage motion — do not skip Survival.

**Phase 1 — Survival ($0–$2M ARR):** Founder is the sales team. Prove repeatability before hiring.

| Task | Skill | Why |
|---|---|---|
| Establish context | `gtm-context` | Every downstream skill needs ICP, motion, and constraints |
| Founder selling | `founder-sales` | Survival phase core — close 10–20 deals yourself first |
| ICP definition | `icp-scoring`, `positioning-messaging` | Know who buys and why before scaling |
| Discovery & demos | `meeting-prep`, `demo-scripts` | SPICED/MEDDIC qualification from day one |
| Pricing & packaging | `pricing-strategy`, `deal-desk` | ACV determines motion — enterprise needs $50K+ ACV path |
| Solo/bootstrap path | `solo-founder-gtm` | If no funding, tighter Survival constraints |

**Phase 2 — Thrival ($2M–$10M+ ARR):** Build the repeatable sales machine. Roberge's territory.

| Task | Skill | Why |
|---|---|---|
| First sales hires | `sales-team-building` | Correct hire sequence by ARR — AE before SDR, no VP too early |
| Sales process | `pipeline-management` | Stage goals + exit criteria — inspect the process, not just results |
| Enablement | `sales-enablement` | Playbook, battlecards, onboarding — train at scale |
| Coaching | `sales-coaching`, `team-management` | REKS diagnostics, deal reviews |
| RevOps foundation | `gtm-metrics`, `crm-integration` | Data model before headcount |

**Phase 3 — Enterprise upmarket (Thrival extension):** Long cycles, buying committees, security gates.

| Task | Skill | Why |
|---|---|---|
| Tier segmentation | `icp-targeting-tiers` | Enterprise ≠ mid-market — different ACV, cycle, stakeholders |
| ABM program | `abm-strategy`, `account-selection` | Named accounts, tier scoring, channel orchestration |
| Multi-threading | `multi-thread-orchestration` | Survive champion departure — engage the buying committee |
| Economic buyer | `meeting-prep`, `roi-calculator`, `deal-desk` | MEDDIC + business case for $100K+ deals |
| Security unblock | `soc2-compliance`, `data-privacy-compliance`, `security-assessments` | Enterprise procurement gates |
| GTM data exchange / rep hygiene | `deal-desk`, `customer-onboarding`, `revenue-team-onboarding`, `references/gtm-data-exchange-playbook.md` | Safe customer data handling in sales + CS |
| Transparency | `transparency-selling`, `objection-handling` | Enterprise buyers reward honesty over hype |

**Survival → Thrival → Enterprise load sequence:**
```
Survival:   gtm-context → founder-sales → meeting-prep → pricing-strategy
Thrival:    sales-team-building → pipeline-management → sales-enablement → sales-coaching
Enterprise: icp-targeting-tiers → abm-strategy → multi-thread-orchestration → roi-calculator → soc2-compliance
```

### Skill Map: Journey / PMF / Scale Gates

Founder company journey: **idea → PMF search → GTM fit → scale → optimize → exit optionality**.
Canonical home: `saas-outcomes` (journey + exit); `solo-founder-gtm` (PMF + scale gates).

| Task | Skill | Artifact |
|---|---|---|
| Where am I on the journey? | `saas-outcomes` | `journey-planning-worksheet.md` |
| Stage go/no-go gates | `saas-outcomes` | `journey-stage-gates.md` |
| Test product-market fit | `solo-founder-gtm` | `pmf-testing-playbook.md` |
| PMF signal checklist | `solo-founder-gtm` | `pmf-signal-checklist.md` |
| Ready to scale headcount/spend? | `solo-founder-gtm` | `scale-readiness-gates.md` |
| Stop scaling (anti-patterns) | `solo-founder-gtm` | `when-not-to-scale.md` |
| Exit realistic vs distraction? | `saas-outcomes` | `exit-potential-scorecard.md` |
| Bootstrap capital discipline | `saas-outcomes` | `bootstrap-founder-playbook.md`, `bootstrap-capital-plan.md` |
| M&A prep (if score ≥4.0) | `exiting-company` | `buyer-readiness-checklist.md` |
| Earn-out / LOI structure | `exiting-company` | `negotiating-earn-out.md`, `earn-out-term-sheet-review.md` |
| Hold vs sell economics | `financial-modeling` | `unit-economics-exit-bridge.md` |
| Stage-appropriate spend | `gtm-spend-management` | `spend-governance.md` |
| Hire after scale gates pass | `sales-team-building` | hiring sequence by ARR |

**Journey load sequence:**
```
gtm-context → saas-outcomes (journey-stage-gates) → solo-founder-gtm (PMF tests)
→ scale-readiness-gates → sales-team-building (if go) → gtm-spend-management
→ saas-outcomes (exit-potential-scorecard) → exiting-company (if active optionality)
→ exiting-company (negotiating-earn-out) if LOI includes deferred consideration
```

**Pattern 32 shortcut (earn-out or bootstrap exit):** `bootstrap-founder-playbook.md` OR `negotiating-earn-out.md` → `benchmark-reconciliation.md` → `valuation-sensitivity-table.md` / `earn-out-term-sheet-review.md`

**Go / no-go rule:** Do not load `sales-team-building` until `scale-readiness-gates.md` passes.
If `when-not-to-scale.md` stop signals active — fix churn/economics first.

### Quick Reference: Top 10 Most-Used Skills

| # | Skill | Use For |
|---|---|---|
| 1 | `cold-email-strategy` | Building outreach sequences |
| 2 | `pitch-deck-builder` | Investor and sales presentations |
| 3 | `founder-sales` | Founder-led sales motion |
| 4 | `fundraising-strategy` | Raising capital |
| 5 | `vibe-marketing` | AI-powered marketing at scale |
| 6 | `financial-modeling` | P&L, runway, DCF valuation |
| 7 | `gtm-metrics` | SaaS metrics dashboard |
| 8 | `lead-finding` | Prospecting and list building |
| 9 | `sales-enablement` | Decks, one-pagers, battlecards |
| 10 | `solo-founder-gtm` | Bootstrapper GTM playbook |

## Loading and Combining Skills

### Single Skill
```
"Load the founder-sales skill and help me with [task]"
```

### Multiple Skills (Workflow)
```
"I need to: 1) find leads, 2) write cold emails, 3) set up domains.
Load lead-finding, cold-email-copywriting, and domain-infrastructure."
```

### Dependency Chain (Auto-Load)
Skills declare dependencies in their frontmatter. Your agent should load
dependencies automatically. Example: `founder-sales` depends on `pricing-strategy`
and `sales-enablement`. When you load `founder-sales`, your agent should
also load its dependencies.

### The "Full Stack" Pattern
For complex GTM projects, load the entire stack:
```
"Build a complete outbound engine for [company]. Load:
- lead-finding, lead-enrichment, email-finding, contact-verification (prospecting)
- cold-email-strategy, email-deliverability, domain-infrastructure (outbound)
- clay-automation (automation)
- gtm-metrics (analytics)"
```

## Advanced Patterns

### Pattern 1: Research → Build → Launch
```
1. competitive-intel + positioning-messaging (research the market)
2. pitch-deck-builder + pricing-strategy (build the assets)
3. launch-planning + content-marketing (launch)
```

### Pattern 2: Hire → Onboard → Manage
```
1. gtm-role-descriptions (JD + org + IC comp templates — H1 2026 bands)
2. founder-comp-playbook (founder: afford hire, value package, negotiate)
3. executive-compensation (VP/CRO clauses + Sam Jacobs / Pavilion gates)
4. gtm-recruiting (source, close, offer negotiate)
5. job-posting-strategy (distribute) + hiring-by-role (interviewer + candidate questions, re:Work scorecard)
6. revenue-team-onboarding (onboarding questions both sides, 30-60-90, Slack, certification)
7. employment-compliance (offer letter) + gtm-leadership (manage, PIP/fire/resignation handoff)
8. team-management + sales-coaching (1:1s, REKS — Jacco van der Kooij / WbD)
```

### Pattern 10: Reviews & Advocacy (G2 / TrustRadius)
```
1. review-platforms (profile, generation cadence, response playbook)
2. customer-marketing (case studies, reference program)
3. competitive-intel (competitor review themes → battlecards)
4. inbound-triage (G2 intent → CRM)
```

### Pattern 11: GTM Stack Finance & Spend
```
1. revops-tech-stack (what you need — consolidate first)
2. gtm-tool-cost-model (seat + credit + cloud TCO)
3. gtm-spend-management (Ramp, vendor roster, approvals, renewals)
4. financial-modeling (OpEx in P&L)
5. vendor-contracts (renewal negotiation)
```

### Pattern 13: Sales Coaching System (REKS → MEDDICC → JOLT)
```
1. pipeline-management (stages + MEDDICC gates + SPICED fields)
2. sales-enablement (playbook reps execute)
3. sales-coaching (REKS diagnose — Jacco van der Kooij / WbD)
4. meeting-prep + demo-scripts (SPICED / Barrows skill drills)
5. buyer-indecision (JOLT when late-stage stall — Dixon/McKenna)
6. gtm-leadership (PIP if 30-day coaching plan flat)
```

**Founder-as-coach:** `sales-coaching` (founder-coaching reference) until manager hired.  
**Ramp:** `revenue-team-onboarding` weeks 1–4 → `sales-coaching` call rubric.

### Pattern 12: Bootstrap vs Venture Outcome
```
1. saas-outcomes (end goal, exit-metrics-matrix, bootstrap-vs-vc-paths, bootstrap-founder-playbook)
2. saas-metrics-calculator (metric-definitions-exit-weight)
3. solo-founder-gtm (bootstrap-capital-plan) OR fundraising-strategy (vc-milestone-gates)
4. financial-modeling (unit-economics-exit-bridge)
5. exiting-company (valuation-drivers, buyer-readiness, diligence pack)
```

### Pattern 15: Exit Readiness & Valuation
```
1. saas-outcomes (path + exit-metrics-matrix)
2. saas-metrics-calculator (formulas + benchmarks)
3. financial-modeling (P&L → ARR/EBITDA multiple bridge)
4. exiting-company (scorecard, sensitivity table, diligence pack)
5. equity-management (cap table cleanup)
6. exiting-company (negotiating-earn-out + earn-out-term-sheet-review) if LOI has deferred consideration
```

### Pattern 32: Founder Exit Economics (Earn-Out + Bootstrap Paths)
```
1. saas-outcomes (bootstrap-founder-playbook, bootstrap-vs-vc-paths, exit-potential-scorecard)
2. solo-founder-gtm (when-not-to-scale, spend-by-stage, bootstrap-capital-plan)
3. financial-modeling (unit-economics-exit-bridge, valuation-sensitivity-table)
4. exiting-company (negotiating-earn-out, earn-out-term-sheet-review, buyer-readiness)
5. fundraising-strategy (bootstrap vs raise — vc-milestone-gates)
6. founder-comp-playbook (post-close retention comp if earn-out + employment)
7. references/benchmark-reconciliation.md (bootstrap multiples + earn-out vs upfront)
8. deal-desk/references/legal-gtm-playbook.md (counsel handoff — Pattern 29)
```

**Triggers:** "negotiate earn-out", "earnout term sheet", "bootstrap founder exit",
"MicroAcquire sale", "walk away from LOI", "seller note", "rollover equity",
"retention bonus vs earn-out", "bootstrap capital plan".

**Pair with:** Pattern 12 (path choice) · Pattern 15 (full M&A prep).

**Disclaimer:** GTM-founder sensibility — not legal or tax advice.

### Pattern 35: GTM Compensation Strategy (IC → CRO)
```
1. executive-compensation/references/gtm-compensation-strategy.md (canonical — philosophy, role strategies, stage gates)
2. executive-compensation/references/comp-by-role-stage.md (role × ARR matrix)
3. gtm-role-descriptions/references/comp-benchmarks.md (H1 2026 bands — single band source)
4. executive-compensation/templates/comp-plan-design-worksheet.md + ote-calculator-template.md
5. founder-comp-playbook (payroll % ARR, negotiation — founders only)
6. sales-team-building (hire sequence, POD economics, Force Management alignment)
7. gtm-role-descriptions/templates/comp-plan-*.md (IC plan templates)
8. executive-compensation (VP/CRO clauses, Pavilion gates, board memo)
9. revenue-team-onboarding + hr-gtm-playbook.md (ramp ↔ comp alignment)
10. references/benchmark-reconciliation.md (OTE band conflicts)
11. gtm-spend-management/spend-by-stage.md + scale-readiness-gates.md (stage gates)
12. employment-compliance (W-2, commission documentation, contractor vs FTE)
```

**Triggers:** "GTM comp strategy", "comp plan design", "OTE calculator", "quota design", "accelerators", "SPIF vs plan change", "consumption comp", "annual comp review".  
**Pair with:** Pattern 28 (HR GTM ramp) · Pattern 31 (consumption CRO gates) · Pattern 32 (earn-out retention).  
**Experts:** Sam Jacobs / Pavilion · Mark Roberge · John McMahon · Stacey Nordwall · Bridge Group · Pave / CaptivateIQ (band ops).

### Pattern 33: Crisis Management & Incident Comms (GTM / Founder)
```
1. references/crisis-management-playbook.md (canonical — severity matrix, first 60 min, war room)
2. gtm-leadership (executive home — CEO voice, layoffs, difficult stakeholder truth)
3. references/crisis-preparedness-checklist.md (before crisis — contact tree, status page, tabletop)
4. skills/management-leadership/gtm-leadership/templates/crisis-holding-statement.md + crisis-customer-email.md + crisis-internal-memo.md + crisis-faq-for-support.md
5. cs-playbooks + customer-marketing (customer email, G2/TR, advocacy pause)
6. investor-updates (Sev 3+ investor/board addendum — Lemkin: never skip bad months)
7. deal-desk/references/legal-gtm-playbook.md (counsel before statements — Pattern 29)
8. references/gtm-data-exchange-playbook.md + gtm-security-hygiene-basics.md (breach path)
9. customer-onboarding (post-incident trust rebuild)
10. references/saas-pr-crisis-experts.md (Lemkin, Highwire, Offleash, Ruettimann)
11. references/chris-walker-mental-models.md (dark social during reputation crises)
12. churn-prevention + gtm-lifecycle-stages.md Retention row (churn wave)
```

**Triggers:** "crisis management", "incident comms", "outage communication", "security breach customer email", "holding statement", "war room", "bad press", "viral negative reviews", "layoff communication", "PR crisis", "status page incident", "AI harmed customer".

**Pair with:** Pattern 16 (data security) · Pattern 29 (legal statements) · Pattern 18 Retention (churn wave) · Pattern 26 (pause demand gen during crisis).

**Disclaimer:** Not legal advice — regulatory notification and liability language require counsel.

### Pattern 34: SaaS Finance — Budget, MRR Accounting & Tax Awareness
```
1. references/gtm-budget-playbook.md (canonical budget — S&M/R&D/G&A, scenarios, variance cadence)
2. financial-modeling (bottom-up P&L, headcount, runway, accounting stack timing)
3. skills/gtm-ops/gtm-spend-management/templates/annual-gtm-budget-worksheet.md
4. gtm-spend-management (vendor/tool lines, Ramp roster, spend-by-stage caps)
5. saas-metrics-calculator (committed MRR formulas, benchmarks)
6. references/saas-mrr-accounting-nuances.md (canonical — committed vs recognized vs billings)
7. skills/founder-led/saas-metrics-calculator/templates/mrr-bridge-template.md
8. references/bookings-billings-revenue-matrix.md (CRM vs GAAP gap)
9. references/saas-tax-founder-awareness.md (nexus, VAT, R&D credit, QSBS, 409A — CPA handoffs)
10. references/benchmark-reconciliation.md (MRR/ARR definition row, Meritech implied ARR)
11. references/meritech-saas-benchmarks.md + references/bessemer-cloud-atlas.md (definitions)
12. gtm-metrics (board dashboard reconcile)
13. fundraising-strategy OR saas-outcomes (raise/exit lens — clean books, QSBS)
14. founder-comp-playbook (409A, equity) · exiting-company (earn-out vs MRR/EBITDA)
15. references/experts.md — Kruze, Pilot, Carta, Ben Murray, Tyler Tringas
```

**Triggers:** "annual operating budget", "GTM budget", "MRR vs ARR accounting", "ASC 606 SaaS",
"deferred revenue", "bookings vs billings", "sales tax SaaS", "R&D tax credit", "QSBS",
"409A valuation", "QuickBooks vs NetSuite", "variance review", "audit MRR", "inflate ARR".

**Pair with:** Pattern 11 (spend management) · Pattern 12 (outcomes path) · Pattern 32 (exit/QSBS).

**Disclaimer:** Practitioner GTM/finance sensibility — **not** CPA or tax advice. Hand off to qualified professionals.

### Pattern 22: Relationship-Led Enterprise (Randy Seidl)
```
1. social-selling (LinkedIn trust + SSI baseline)
2. sales-coaching (Three Plays, relationship map, trust scorecard — Seidl)
3. pipeline-management (MEDDICC evidence per stakeholder thread)
4. multi-thread-orchestration (champion-only anti-pattern)
5. expansion-selling (relationship-led upsell after land)
6. cold-email-strategy (contrast — sequences for access, not trust alone)
```

**When to use:** $100K+ ACV, 6+ month cycles, multi-stakeholder enterprise.
**Pair with:** Pattern 14 (Benioff enterprise CRM) · Chris Walker (dark social awareness).

### Pattern 14: Enterprise GTM (Marc Benioff)
```
1. gtm-leadership (annual V2MOM — Vision, Values, Methods, Obstacles, Measures)
2. crm-toolkit (benioff-enterprise-playbook — trust, CS objects, land-expand)
3. salesforce-setup + salesforce-blueprint (enterprise CRM config)
4. expansion-selling (expand triggers + land-expand account plan)
5. transparency-selling (trust-based deal behavior)
6. cs-playbooks (customer success as revenue function)
7. deal-desk + security-questionnaire-deal-guide (security review track)
```

### Pattern 16: GTM Data Security & Customer Data Exchange
```
1. revenue-team-onboarding (password manager, MFA, phishing — gtm-security-hygiene-basics.md)
2. deal-desk (pre-sale data asks, security questionnaire timing, customer-data-exchange-checklist)
3. customer-onboarding (sales-to-CS data handoff, no email re-requests)
4. revops-tech-stack (where data may live in the GTM stack)
5. cold-email-strategy (anti-pattern: customer PII in sequences)
6. soc2-compliance + security-assessments (founder-led — building trust artifacts, not rep hygiene)
```

Load canonical SOP: `references/gtm-data-exchange-playbook.md`. Enterprise
security review timing: `references/security-questionnaire-deal-guide.md`.

### Pattern 9: Stuck Late-Stage Deal (JOLT)
```
1. pipeline-management (MEDDICC ≥14, stage gate)
2. buyer-indecision (Judge → Offer → Limit → Take risk)
3. deal-desk (package collapse) + multi-thread-orchestration (EB)
4. objection-handling (if price/value pushback, not indecision)
```

### Pattern 3: Data → Decision → Action
```
1. gtm-metrics + event-analytics (collect data)
2. cs-analytics-dashboards + financial-modeling (make decisions)
3. expansion-selling + churn-prevention (take action)
```

### Pattern 4: AI-First GTM (The Vibe Stack)
```
1. vibe-coding → Build landing pages, tools, dashboards
2. vibe-marketing → Generate campaigns, content, creative
3. ai-content-creation → Scale blog, social, email production
4. ai-video-creation → Produce video without a video team
```

### Pattern 5: WbD Sales Process Build
```
1. gtm-system-architecture (score 6 models, find weakest link)
2. pipeline-management (stages, SPICED fields, conversion metrics, handoffs)
3. sales-enablement (playbook + collateral per stage)
4. sales-coaching (REKS, deal review cadence)
5. crm-integration (configure fields and stages)
6. gtm-metrics (conversion dashboards)
```

### Pattern 23: Sales Borg — Hybrid Human + Machine Outbound (Justin Michael)
```
1. cold-email-strategy (sequence architecture + trigger catalog — load justin-michael-sales-borg.md)
2. cold-email-copywriting (REPLY messaging, brevity rules)
3. domain-infrastructure + email-deliverability + sending-platforms (scale safely)
4. clay-automation OR signal-scoring (trigger feeds → SEP enrollment)
5. ai-sdr-setup (pilot guardrails: draft-only week 1, human handoff on positive replies)
6. reply-handling (all replies = signs of life; AE triple-touch <90 sec)
7. sales-team-building (TQ ramp in 30 days; ~200 accounts/SDR/month benchmark)
```

**Rule:** Automate only after ICP + messaging proven. Machines think/do; humans feel/engage. RevOps orchestrates bots — see `references/experts.md` → Justin Michael.

### Pattern 15b: Phone-First Cold Calling & Bucketing

```
1. list-building + signal-scoring (Gilkey Phone Intent + Jordan Crawford PQS)
2. cold-calling (primary — references/cold-calling-experts-index.md)
   → joey-gilkey-bucketing.md · ryan-reisert-cold-calling.md
   → ronen-pessar-cold-calling.md · tom-slocum-cold-calling.md
3. pipeline-management (dispositions → pipeline tiers; Reisert buckets → CRM stages)
4. multi-channel-outreach (email/LI complementary touches)
5. sales-team-building + revenue-team-onboarding (pilot before SDR scale; phone ramp)
```

**Two bucketing systems:** Gilkey = outcome dispositions. Reisert = daily CRM priority. Phone experts ≠ email experts — cross-link `cold-email-strategy` for written cadence only.

### Pattern 15c: High-Scale Cold Email Infrastructure (Eric Nowoslawski)

```
1. cold-email-strategy (unit economics gate — eric-nowoslawski-outbound.md)
2. domain-infrastructure + inbox-setup (2 inboxes/domain, 1:1 backup capacity)
3. email-deliverability + sending-platforms (30 sends/inbox baseline, 3-week warmup)
4. cold-email-copywriting (Creative Ideas / AI Specificity offer-led campaigns)
5. clay-automation (Crawl Walk Run rollout)
6. smartlead-workflows OR tool-selection-stack (GEX agency stack)
```

**Rule:** Validate TAM/LTV/CAC before infra spend. Eric owns economics + deliverability discipline; pair with Jordan Crawford / Becc Holland / Pat Spielmann for segment + message. Router → `references/gtm-experts-outbound-index.md`.

### Pattern 17: Enrichment-Powered Outbound — Cold to Gold (Pat Spielmann)
```
1. leadmagic-waterfall OR clay-toolkit (LeadMagic-first waterfall + validate gate)
2. cold-email-copywriting (Hook-Line-Sinker + copy review checklist — pat-spielmann-outbound-copy.md)
3. cold-email-strategy (Full-Circle multichannel: email → LinkedIn → phone <5 min on positive reply)
4. `tools/instantly-sequences` / `tools/smartlead-workflows` / `tools/lemlist-setup` — clay-enrollment-handoff.md verify gate
5. email-deliverability + sending-platforms (Eric Nowoslawski infra before scale)
6. multi-channel-outreach (channel-native touches — not email paste to LinkedIn)
7. reply-handling (positive reply → immediate call routing)
```

**Rule:** Data quality before copy scale — *"If your outbound isn't converting, it's probably not your copy. It's your data."* Pair with Jordan Crawford (PQS/PVP research) for segment depth; Guillaume (multichannel cadence) or Justin Michael (SEP automation) for scale; Eric Nowoslawski for infra at volume. Expert router → `references/gtm-experts-outbound-index.md`.

### Pattern 6: Clay GTM Stack
```
1. clay-automation (process: when to build, data quality)
2. clay-toolkit — tools/clay-toolkit (table + LeadMagic waterfall)
3. clay-loops-toolkit — tools/clay-loops-toolkit (signal loops)
4. ai-prompts-toolkit (Claygent/LLM prompts P01–P10)
5. leadmagic-toolkit + leadmagic-waterfall (Find → Verify → Enrich columns)
6. `sequencing-toolkit` OR platform sequencer skill OR `crm-toolkit` (output — verify gate before enroll)
7. signal play skill (funding/job-change/hiring message)
```

**Tool vs process:** `tools/clay-*` = column/table config. `automation/clay-automation` = rollout.

### Pattern 6b: n8n Orchestration (Inbound / Outbound / MCP)
```
1. n8n-automation (n8n vs Clay vs MCP decision)
2. n8n-toolkit (pick flow ID: INB/OUT/SIG/LIF/REV/MCP)
3. Motion skill (inbound-triage, reply-handling, signal play)
4. mcp-setup + leadmagic-mcp (if agent triggers MCP-01 webhook)
5. crm-toolkit + proactive-alerts (CRM fields + Slack)
```

Clay enriches; n8n routes at SLA; MCP agents draft/research — never loop
500 API calls in chat; POST approved jobs to n8n.

### Pattern 7: Agency Pilot → In-House
```
1. pipeline-management + gtm-context (document process first)
2. hiring-agencies (evaluate, 90-day pilot, weekly scorecard)
3. cold-email-strategy or clay-automation (channel-specific standards)
4. sales-team-building (graduate to hire when pilot proves ROI)
```

### Pattern 8: Survival → Thrival → Enterprise (Lemkin + Roberge)
```
1. gtm-context + icp-scoring (define who you sell to)
2. founder-sales + meeting-prep (Survival — founder closes, documents the motion)
3. pipeline-management + sales-enablement (Thrival — repeatable process + playbook)
4. sales-team-building + hiring-by-role (Thrival — hire for Roberge traits, train for skills)
5. icp-targeting-tiers + abm-strategy + multi-thread-orchestration (Enterprise — upmarket)
6. roi-calculator + deal-desk + soc2-compliance (Enterprise — economic buyer + procurement)
```

### Pattern 24: Force Management — Alignment & Pod Economics
```
1. references/force-management-playbook.md (cadence, reporting, pod worksheet)
2. sales-team-building (POD design, hiring sequence, compensation)
3. gtm-leadership (monthly GTM scorecard, quarterly territory/quota)
4. sales-enablement (Command of the Message talk tracks)
5. pipeline-management + meeting-prep (MEDDICC gates)
6. gtm-metrics + financial-modeling (unit economics ↔ headcount)
```

### Pattern 25: B2B SEO Stack (Schwartz + Fishkin + Ahrefs)
```
1. seo-strategy + references/seo-strategy-playbook.md (keyword tiers, measurement)
2. pillar-pages (hub + cluster architecture)
3. pseo-strategy (programmatic templates — thin-content gates)
4. faq-seo + aeo-strategy (schema + AI search)
5. citation-harvesting (LLM mention tracking)
6. content-marketing + content-syndication (distribution — Walker frequency)
```

### Pattern 26: Demand Creation (Chris Walker)
```
1. references/chris-walker-mental-models.md (dark social, frequency, 90-day eval)
2. content-marketing (ungated education, channel stacking)
3. paid-social-strategy (LinkedIn education, not form-fill)
4. podcast-gtm + content-syndication (dark social amplifiers)
5. attribution + gtm-metrics (cohort revenue, not last-click ROAS)
6. seo-strategy (measurable demand layer)
```

**Contrast Pattern 27:** Walker = unmeasurable dark social. HubSpot inbound = lifecycle + flywheel capture. Run both; reconcile in `references/benchmark-reconciliation.md` (inbound vs demand gen).

### Pattern 27: Inbound Flywheel (Dharmesh Shah / HubSpot)
```
1. references/dharmesh-shah-hubspot-inbound.md (flywheel, attract-engage-delight, freemium entry)
2. content-marketing + seo-strategy (Attract — pillar + cluster)
3. landing-pages + freemium-optimization (permission-based conversion)
4. inbound-triage + mql-nurture (Engage — speed-to-lead, enrichment on form fill)
5. customer-marketing + referral-programs + review-platforms (Delight — advocacy fuels flywheel)
6. expansion-selling + gtm-metrics (NRR as flywheel fuel — Meritech benchmarks for scale narrative)
7. hubspot-setup OR crm-integration (lifecycle stages, CRM config)
```

**Pair with:** Pattern 20 (visitor ID — measurable intent) · Pattern 26 (dark social awareness) · Mark Roberge (sales machine when hiring).
**Contrast:** Chris Walker rejects lead-gen industrial complex; HubSpot inbound still uses MQL→SQL when **fit** is proven — qualify hard, don't optimize form volume alone.

### Pattern 28: HR GTM / People Ops for Revenue Teams (Stacey Nordwall)
```
1. gtm-role-descriptions/references/hr-gtm-playbook.md (canonical — onboarding, manager enablement, remote GTM)
2. gtm-role-descriptions + references/comp-benchmarks.md (Bridge Group bands; Pavilion validate)
3. hiring-by-role (structured interviews — re:Work, Roberge traits)
4. revenue-team-onboarding (30-60-90, ramp-benchmarks, security day 0)
5. employment-compliance (W-2 default for SDR/AE; commission documentation)
6. executive-compensation + founder-comp-playbook (VP+ and payroll % ARR)
7. sales-team-building (hire sequence, POD ratios)
8. executive-compensation/references/gtm-compensation-strategy.md (Pattern 35 — full comp design)
```

**Triggers:** "HR for sales team", "People Ops GTM", "revenue comp bands", "SDR ramp HR", "remote sales team onboarding", "Culture Amp onboarding".  
**Pair with:** Pattern 2 (hire → onboard) · Pattern 35 (comp plan design) · `references/benchmark-reconciliation.md` (ramp + comp alignment).  
**Contrast:** Nordwall = employee experience systems; Roberge = ramp metrics; Sam Jacobs = exec comp; Pattern 35 = full IC→CRO strategy.

### Pattern 29: Legal GTM / Commercial Counsel (Eunice Buhler + Ironclad)
```
1. deal-desk/references/legal-gtm-playbook.md (canonical — sales-legal alignment, swimlanes)
2. deal-desk (discount authority, business case, Phase 5 security)
3. references/security-questionnaire-deal-guide.md (when security review enters deal)
4. references/gtm-data-exchange-playbook.md (DPA timing, data channels)
5. soc2-compliance + security-assessments (artifact build — founder-led)
6. vendor-contracts (vendor-side MSAs/DPAs)
7. employment-compliance (commission plans, SDR classification — not MSA)
```

**Triggers:** "MSA redlines", "when to sign DPA", "sales legal alignment", "deal desk approvals", "commercial counsel", "Ironclad CLM".  
**Pair with:** Pattern 16 (customer data exchange) — same phase gates, different lens (legal velocity vs data hygiene).  
**Disclaimer:** GTM practitioner guidance — escalate binding terms to counsel.

### Pattern 30: RevOps Automation Maturity (Jen Igartua / Go Nimbly)
```
1. references/gtm-automation-expert-playbook.md (canonical — maturity 0–4, human/machine split)
2. revops-tech-stack (inventory, target architecture)
3. gtm-operations (intake, roadmap, RevOps as product)
4. tool-selection-stack (Clay vs n8n vs CRM-native vs Cargo category)
5. references/automation-playbook-index.md (38 playbooks — implementation)
6. waterfall-enrichment + contact-verification (data before AI)
7. crm-integration (sync rules, conflict resolution)
8. gtm-metrics (pipeline impact — not automation vanity)
```

**Triggers:** "RevOps automation", "GTM workflow design", "automation maturity", "fix Zapier sprawl", "AI agents RevOps", "Go Nimbly".  
**Pair with:** Pattern 6/6b (Clay/n8n build) · Pattern 7 (agency → in-house).  
**Contrast:** Pattern 30 = orchestration strategy. Pattern 23 (Justin Michael) = outbound human+machine. Pattern 15c (Eric) = email infra. Pattern 17 (Pat) = enrichment copy. Do not merge.

### Pattern 31: CRO Enterprise Strategy (John McMahon + Snowflake + Databricks)
```
1. gtm-leadership/references/cro-enterprise-strategy.md (canonical — CRO 90-day, inspection, board metrics)
2. gtm-leadership (hire/fire CRO, difficult conversations, comp approval)
3. sales-team-building (A players, manager-before-rep, hybrid inside/field)
4. pipeline-management (MEDDICC inspection, three-view forecast, Gap Selling anti–happy ears)
5. gtm-metrics + public-company-gtm-metrics.md (5-quarter model, productivity per rep, Meritech)
6. executive-compensation (consumption-aligned CRO gates — Slootman pattern)
7. expansion-selling (Snowflake consumption land-expand, Databricks workload expansion)
8. references/force-management-playbook.md (territory/quota true-up)
9. references/benchmark-reconciliation.md (McMahon vs Lemkin hire timing)
```

**Triggers:** "CRO strategy", "John McMahon", "enterprise sales leadership", "Snowflake GTM", "consumption sales comp", "Databricks enterprise", "board forecast CRO", "inspect what you expect", "5-quarter model".  
**Pair with:** Pattern 5/13 (MEDDICC discovery) · Pattern 14 (land-expand) · Pattern 28 (HR ramp) · Meritech/Henry Schuck public metrics.  
**Contrast:** McMahon = CRO systems altitude. Jon Barrows = rep tactical skills. Roberge = early-stage hire/train. Lemkin = when *not* to hire VP.

### Pattern 18: Lifecycle Stages & Activation Monitoring
```
1. references/gtm-lifecycle-stages.md (canonical 7 stages + Bowtie + team ramp)
2. references/activation-playbook.md (first value event, TTA benchmarks, audit)
3. references/lifecycle-metrics-by-stage.md (formulas + R/Y/G thresholds)
4. skills/analytics/gtm-metrics/templates/lifecycle-monitoring-dashboard.md (weekly/monthly cadence)
5. skills/analytics/gtm-metrics/templates/stage-health-scorecard.md (leadership rollup)
6. Stage skills — load by need (see routing table below)
```

**Stage → skill routing (do not duplicate stage defs in skills):**

| Stage | Primary skills | Monitoring artifact |
|---|---|---|
| Awareness | `content-marketing`, `seo-strategy`, `paid-social-strategy`, `customer-marketing`, `social-selling` | `lifecycle-monitoring-dashboard` (Awareness row) · `b2b-influencer-strategy.md` |
| Acquisition | `mql-nurture`, `inbound-triage`, `attribution` | `lifecycle-metrics-by-stage` (Acquisition) |
| **Activation** | `customer-onboarding`, `onboarding-sequences`, `cs-analytics-dashboards` | **`activation-playbook`** + scorecard Activation panel |
| Engagement | `cs-playbooks`, `event-analytics`, `freemium-optimization` | `stage-health-scorecard` (Engagement) |
| Revenue | `expansion-selling`, `pipeline-management`, `gtm-metrics` | `gtm-metrics`, `saas-metrics-calculator` |
| Retention | `churn-prediction`, `churn-prevention`, `qbr-planning` | `churn-prediction` + scorecard Retention |
| Referral | `referral-programs`, `customer-marketing`, `review-platforms` | `stage-health-scorecard` (Referral) |

**Founder journey overlay:** `saas-outcomes/references/journey-stage-gates.md` gates company stage; Pattern 18 gates customer lifecycle health.  
**Revenue team parallel:** `revenue-team-onboarding` (Hire → Ramp → Productivity) — see `gtm-lifecycle-stages.md` team table.  
**Router:** `references/lifecycle-skill-index.md`

### Pattern 19: GTM Project Management & RACI
```
1. gtm-operations (canonical PM home — lightweight vs heavyweight, cadence, milestones)
2. gtm-operations/templates/gtm-project-charter.md + raci-matrix-template.md (one A per row)
3. campaign-governance (if launch — naming/UTM RACI rows; do not duplicate UTM spec)
4. revops-tech-stack (if migration/vendor — Phase 4c + RACI Examples 2/4)
5. gtm-spend-management (if vendor — spend-approval-matrix)
6. gtm-leadership + team-design-gtm-projects (launch pod, DRI span of control)
7. clickup-gtm-workspace OR gtm-organization-principles (SSOT for tasks/docs/data)
8. revenue-team-onboarding (if onboarding cohort project)
```

**Triggers:** "campaign launch project", "CRM migration RACI", "ClickUp for RevOps",
"QBR prep project", "who owns UTM vs CRM", "organize GTM docs".  
**Refs:** [Atlassian RACI](https://www.atlassian.com/team-playbook/plays/raci) · [PMI RACI](https://www.pmi.org/learning/library/raci-matrix-responsibility-assignment-7039) · [RevOps Co-op PM webinar](https://www.revopscoop.com/webinar-series/revops-project-management).

**Leader development:** `gtm-leadership` + Pavilion (`startup-communities`) for peer groups.

### Pattern 20: Visitor Identification & Intent Routing
```
1. website-visitor-identification (canonical — person vs business, vendors, privacy)
2. 1p-tagging-pixels (consent before visitor ID scripts; UTM source)
3. icp-scoring (filter before CRM write or sales alert)
4. inbound-triage (company ID → MQL path + speed-to-lead SLAs)
5. cold-email-strategy (person ID → guardrailed trigger branch only)
6. revops-tech-stack + gtm-spend-management (one company ID + one person ID max)
7. campaign-governance (UTM + visitor source attribution)
```

**Privacy:** `website-visitor-identification/references/visitor-id-privacy-gtm.md`
(not legal advice). **Measurable counterpart** to Chris Walker dark social (Pattern 26) —
visitor ID is attributable; dark social is not. Pair Pattern 26 + 20.

### Pattern 21: B2B Influencer & Creator GTM (Aneesh Lal / Wishly Group)
```
1. references/aneesh-wishly-b2b-influencer.md (canonical expert — ICP selection, bundles)
2. references/b2b-influencer-strategy.md (program types: paid creators, employee advocates, affiliates)
3. customer-marketing (canonical skill — Phase 6; distinguish external vs employee vs customer champions)
4. social-selling (LinkedIn visibility, post-engagement nurture, SSI for employee advocates)
5. skills/growth/customer-marketing/templates/b2b-influencer-program-brief.md + influencer-partnership-scorecard.md
6. campaign-governance (per-creator UTMs, landing pages — utm_medium=influencer)
7. references/b2b-influencer-measurement.md + gtm-metrics (CRM lookback, Clay scrape, dark social)
8. references/chris-walker-mental-models.md (90-day eval; do not kill at 2 weeks on last-click)
```

**Triggers:** "B2B influencer program", "LinkedIn creator partnership", "Wishly Group",
"creator ROI", "employee advocacy vs influencers".  
**Lifecycle:** Awareness stage → `references/gtm-lifecycle-stages.md`.  
**Pair with:** Pattern 26 (demand creation) · `strategic-gifting` (physical ABM touch) ·
`customer-marketing` → `community-selling-varun.md` (creator flywheel from community).

## Skill Structure (What's Inside Every Skill)

Every skill in gtm-skills follows this structure:

1. **Overview** — What mistake does this skill prevent? (principle-first)
2. **When to Use** — Trigger phrases that activate this skill
3. **Authoritative Foundations** — Named experts and frameworks cited
4. **Step-by-Step Process** — Numbered phases with concrete outputs
5. **Output Format** — What the deliverable looks like
6. **Quality Checklist** — Verifiable checkboxes before considering it done
7. **Common Pitfalls** — Numbered mistakes with root cause + fix
8. **Related Skills** — What to load next

## Skill Quality Standards

Every gtm-skills skill is:
- **Principle-first** — Opens with the mistake it prevents, not a description
- **Authority-anchored** — Names specific practitioners and frameworks
- **Executable** — Step-by-step. You can follow it without asking questions
- **Pitfall-aware** — Teaches what goes wrong, not just what goes right
- **Artifact-producing** — Every skill produces something (document, deck, calculator, dashboard)
- **Non-fluff** — No guru nonsense. No AI-generated filler. No "one weird trick."

## Navigating the Repo

```
gtm-skills/
├── README.md              # Hero, install, category overview, authority catalog
├── install.sh             # TUI installer entrypoint (all 11 agent runtimes)
├── docs/INSTALL.md        # Per-system install paths and directory layout
├── skills.lock            # SHA256-verified integrity for all marketplace skills
├── taxonomy.csv           # slug → name → category → description → priority
├── references/
│   ├── skill-index-master.md  # One-page map of all 24 categories
│   ├── experts.md          # Master expert catalog (channels + skill clusters)
│   ├── gtm-lifecycle-stages.md  # Canonical 7-stage customer lifecycle + Bowtie
│   ├── activation-playbook.md   # Activation deep-dive + audit
│   ├── lifecycle-metrics-by-stage.md
│   ├── lifecycle-skill-index.md
│   ├── templates/          # lifecycle-monitoring-dashboard, stage-health-scorecard
│   └── pitfalls-index.md   # Auto-generated Common Pitfalls aggregator
├── AGENTS.md              # Cross-tool skill index
├── CLAUDE.md              # Claude Code-specific index
├── skills/
│   ├── foundation/         # ICP, positioning, pricing, using-gtm-skills router
│   ├── founder-led/        # 40+ skills — everything a founder needs
│   ├── gtm-ops/            # RevOps, spend, tool TCO, campaign governance
│   ├── prospecting/        # Lead finding, enrichment, verification
│   ├── outbound/           # Cold email, deliverability, domains, inboxes
│   ├── automation/         # Clay, n8n, enrichment waterfalls, tool stacks
│   ├── tools/              # Toolkits (clay-toolkit, crm-toolkit, n8n-toolkit)
│   ├── creative/           # AI content, vibe coding/marketing, growth hacks
│   ├── design/             # Pitch decks, ROI calculators, brand systems
│   ├── inbound/            # LinkedIn algorithm, Live, Sales Nav, social selling (8 skills)
│   ├── sales-revops/       # Sales enablement, demo scripts, deal desk
│   ├── analytics/          # Metrics, event analytics, attribution
│   └── ...                 # 24 categories — full map: references/skill-index-master.md
├── scripts/
│   ├── install-tui.py      # Installer implementation (11 targets)
│   ├── validate-skills.js  # YAML validator — runs in CI
│   ├── generate-indexes.js # README, AGENTS.md, CLAUDE.md, taxonomy.csv
│   ├── generate-pitfalls-index.js
│   ├── generate-skills-lock.py
│   └── lib/compatibility.js # Canonical compatibility string for all skills
└── .github/workflows/
    └── validate.yml        # CI: validates all skills on push and PR
```

### Subsidiary maps (link back to master catalogs)

| Map | Path | Use when |
|---|---|---|
| **Master skill index** | `references/skill-index-master.md` | One-page map of all 24 categories |
| Expert catalog | `references/experts.md` | Named practitioner lookup (~110 entries incl. methodology orgs) |
| GTM glossary | `references/gtm-glossary.md` | MEDDICC, SPICED, Bowtie terminology |
| SaaS metrics ref | `references/saas-metrics-reference.md` | Churn, LTV, NRR formulas |
| Meritech benchmarks | `references/meritech-saas-benchmarks.md` | Public SaaS index, Rule of 40 |
| Bessemer Cloud Atlas | `references/bessemer-cloud-atlas.md` | VC-stage benchmarks, Rule of 40 essays |
| Customer Success playbook | `references/lincoln-murphy-customer-success.md` | Murphy Desired Outcome + Gainsight ops |
| PLG growth playbooks | `references/elena-verna-plg-growth.md`, `references/kyle-poyar-growth-unhinged.md` | Loops, PQL, conversion benchmarks |
| Sales methodology | `references/brent-adamson-challenger.md`, `references/anthony-iannarino-sales-discipline.md`, `references/peter-cohan-great-demo.md`, `references/jeb-blount-prospecting.md` | Challenger, discipline, demo, prospecting |
| SaaS efficiency metrics | `references/david-sacks-saas-metrics.md` | Burn multiple, capital efficiency |
| B2B brand voice | `references/dave-gerhardt-exit-five.md` | Exit Five marketing community |
| Benchmark reconciliation | `references/benchmark-reconciliation.md` | Canonical thresholds when sources differ |
| HubSpot inbound | `references/dharmesh-shah-hubspot-inbound.md` | Flywheel, inbound methodology |
| Outbound/discovery index | `references/gtm-experts-outbound-index.md` | Keenan, Becc, Guillaume, Crawford, Eric routing |
| Cold calling index | `references/cold-calling-experts-index.md` | Gilkey, Reisert, Pessar, Slocum phone stack |
| Automation playbooks | `references/automation-playbook-index.md` | 38 playbooks (Clay, n8n, sequencing, LeadMagic) |
| Outbound expert map | `cold-email-strategy/references/expert-frameworks.md` | Subsidiary framework router |
| Pitfalls index | `references/pitfalls-index.md` | Cross-skill mistake patterns (`npm run build` regenerates) |
| Coaching experts | `sales-coaching/references/coaching-experts.md` | Manager coaching citations |
| Interview experts | `hiring-by-role/references/interview-experts.md` | Structured interviewing |
| Leadership frameworks | `gtm-leadership/references/expert-frameworks.md` | Hire/fire/comp conversations |
| GTM ops router | `gtm-operations/references/gtm-ops-skill-index.md` | RevOps stack + spend cluster |
| Lifecycle stages | `references/gtm-lifecycle-stages.md` | 7-stage index + Bowtie + monitoring |
| Lifecycle skill router | `references/lifecycle-skill-index.md` | lifecycle/ + CS + growth cluster |
| Activation deep-dive | `references/activation-playbook.md` | TTV, audit, experiments |
| Lifecycle metrics | `references/lifecycle-metrics-by-stage.md` | Per-stage R/Y/G thresholds |

## Contributing

See CONTRIBUTING.md in the repo root. Quick rules:
- Use the skill template in skills/_TEMPLATE.md
- Every skill cites named authorities
- No internal tool internals exposed (blackbox rule)
- Every new skill → update `taxonomy.csv`
- Run `node scripts/validate-skills.js` before PR
- Run `bash scripts/generate-skills-lock.sh` after adding skills
- Every skill must work without paid tools

## Output Format (This Guide)

```
GTM-SKILLS USAGE PLAN

TASK: [what you're trying to do]

RECOMMENDED SKILLS:
1. [skill] — [why]. Dependencies: [list]
2. [skill] — [why]
3. [skill] — [why]

LOAD SEQUENCE:
"Load [skill-1], [skill-2], and [skill-3]. Then help me [task]."

ESTIMATED TIME: [X hours/minutes]
EXPECTED OUTPUT: [what you'll have when done]
```

## Implementation Checklist (For Agents Using gtm-skills)

- [ ] Identified the right skills for the task (use taxonomy or discovery)
- [ ] Loaded skill dependencies (check `related_skills` in frontmatter)
- [ ] Followed the skill's step-by-step process (not just read the overview)
- [ ] Produced the expected output format
- [ ] Checked against the skill's quality checklist before considering it done
- [ ] Reviewed the common pitfalls section (prevents known mistakes)
- [ ] Verified skills.lock integrity before executing
- [ ] Combined skills when the task spans multiple domains

## Expert Voices: Who Built This

gtm-skills is maintained by LeadMagic, built by operators who run real GTM
infrastructure. Every skill draws from:

- **Andy Whyte** — *MEDDICC* (MEDDICC.com) — qualification scorecard, Champion test, Always Be Qualifying; operationalizes Force Management MEDDICC
- **Matthew Dixon & Ted McKenna** — *The JOLT Effect* — buyer indecision, FOMU, Judge/Offer/Limit/Take risk (`buyer-indecision`)
- **Kim Scott** — *Radical Candor* — difficult conversations, feedback (`gtm-leadership`)
- **Bridge Group / Pavilion** — SaaS comp benchmarks and CRO council (`gtm-role-descriptions`, `gtm-leadership`)
- **Mark Roberge** — *The Sales Acceleration Formula* (hiring, training, demand gen, sales process); co-author *From Survival to Thrival*
- **Jason Lemkin (SaaStr)** — Survival phase benchmarks, founder sales, hiring triggers; co-author *From Survival to Thrival*
- **Winning by Design** — SPICED methodology, Bowtie funnel, POD structures
- **Reforge** — Growth loops, experimentation, retention frameworks
- **YC Partners** — Paul Graham, Sam Altman, Michael Seibel, Dalton Caldwell
- **David Skok (Matrix)** — SaaS unit economics, CAC payback, sales learning curve
- **Force Management (John Holland)** — Command of the Message, MEDDICC, pod economics, alignment cadence
- **Chris Walker (Refine Labs)** — Demand creation, dark social, marketing frequency
- **Dharmesh Shah (HubSpot)** — Inbound methodology, flywheel, freemium entry, culture code
- **Meritech Capital** — Public SaaS benchmarks, Meritech Rule of 40, IPO comps
- **Eli Schwartz** — Product-Led SEO; **Rand Fishkin** — SparkToro audience research
- **Betts Recruiting** — GTM hiring and talent strategy
- **Bridge Group** — SaaS sales compensation and hiring data
- **Andrej Karpathy** — Vibe coding philosophy
- **Pieter Levels, Sahil Lavingia, Marc Lou** — AI-assisted solo building
- **Brian Balfour, Andrew Chen, Sean Ellis** — Growth hacking
- **Nielsen Norman Group, Baymard Institute, Steve Krug** — UX research
- **Ben Murray (SaaS CFO), Aswath Damodaran (NYU)** — Financial modeling
- **Brad Feld, Fred Wilson** — Venture capital and board governance

No fluff. All science. Built by operators.

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Generic output.** The agent produces advice that could apply to any company. Fix: tie the work to the user's ICP, motion, stage, and constraints.
2. **Missing operating detail.** The answer explains what matters but not what to do. Fix: include concrete steps, templates, fields, or decision rules.
3. **No verification step.** The workflow ends before checking quality. Fix: include a checklist or acceptance criteria.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `references/gtm-experts-outbound-index.md` — Outbound + discovery expert router (email + phone stacks)
- `references/cold-calling-experts-index.md` — Phone-first expert router (Gilkey, Reisert, Pessar, Slocum)
- `references/experts.md` — Full expert bios and subsidiary maps
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator
- `references/pitfalls-index.md` — Repo-wide `## Common Pitfalls` aggregator (generated; see `scripts/generate-pitfalls-index.js`)

## Related Skills

- `skills-lock` — Verify skill integrity before use
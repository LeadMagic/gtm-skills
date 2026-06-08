# GTM Skills

[![Skills](https://img.shields.io/badge/skills-189-blue)](skills/) [![Categories](https://img.shields.io/badge/categories-26-green)](skills/)

189 production go-to-market skills for Claude Code and other AI agents. Built for sales, marketing, PLG, analytics, automation, customer success, RevOps, founder-led GTM, and tool operations.

This repo follows the Anthropic/agentskills pattern: skills are self-contained folders of instructions, scripts, references, templates/assets, and metadata that agents load dynamically through progressive disclosure.

## Install

Claude Code marketplace style:

```text
/plugin marketplace add LeadMagic/gtm-skills
/plugin install gtm-skills@gtm-skills
```

agentskills CLI style:

```bash
gh skill install LeadMagic/gtm-skills
```

Interactive installer:

```bash
./install.sh
./install.sh --target all --dry-run
```

## What makes this repo different

- Artifact-first: skills produce copy, plans, scorecards, runbooks, dashboards, workflows, templates, or scripts.
- Anthropic-style folders: SKILL.md for instructions; scripts/, references/, templates/, and assets/ for execution resources.
- Authority-backed: skills cite named operators, vendors, books, and frameworks instead of vague best practices.
- Progressive disclosure: SKILL.md stays focused; deep tables/templates live in support files.
- Marketplace-ready: every skill is discoverable by agentskills.io patterns and validated in CI.
- Supply-chain aware: skills.lock tracks SHA256 for every skill.

## Categories

### abm (6)

- [abm-1-to-1](skills/abm/abm-1-to-1/SKILL.md) — Execute Strategic ABM (1-to-1) for 5-15 high-value accounts — custom microsites, executive engagement, direct mail, board-level connections, custom content. Triggers on: "1-to-1 ABM", "strategic ABM", "custom ABM", "key
- [abm-1-to-few](skills/abm/abm-1-to-few/SKILL.md) — Execute ABM at Scale (1-to-few) for 15-50 clustered accounts — semi-custom campaigns, industry-specific content, persona-based plays. Triggers on: "1-to-few ABM", "ABM scale", "cluster ABM", "industry ABM".
- [abm-1-to-many](skills/abm/abm-1-to-many/SKILL.md) — Execute Programmatic ABM (1-to-many) for 50-200+ accounts — automated personalization, scaled outbound, lookalike expansion. Triggers on: "1-to-many ABM", "programmatic ABM", "scaled ABM", "automated ABM".
- [abm-strategy](skills/abm/abm-strategy/SKILL.md) — Design and execute Account-Based Marketing strategy — tier selection, account scoring, channel orchestration, BDR alignment, measurement framework. Triggers on: "ABM strategy", "account based marketing", "ABM playbook",
- [account-selection](skills/abm/account-selection/SKILL.md) — Select and prioritize target accounts for ABM programs — scoring models, tier assignment, TAM segmentation. Triggers on: "account selection", "target account list", "tier accounts", "prioritize accounts", "TAM segmentati
- [multi-thread-orchestration](skills/abm/multi-thread-orchestration/SKILL.md) — Orchestrate multi-threaded ABM engagement across buying committee members — stakeholder mapping, parallel plays, ghost node detection. Triggers on: "multi-thread", "stakeholder map", "buying committee", "deal mapping".

### ai-agents (4)

- [agent-architecture](skills/ai-agents/agent-architecture/SKILL.md) — Design AI agent architectures for GTM workflows — agent patterns, tool selection, multi-agent orchestration, human-in-the-loop. Triggers on: "agent architecture", "AI agent design", "agent patterns", "multi-agent", "agen
- [agent-guardrails](skills/ai-agents/agent-guardrails/SKILL.md) — Implement safety guardrails for GTM agents — content filtering, approval gates, rate limiting, budget controls, kill switches. Triggers on: "agent guardrails", "agent safety", "AI guardrails", "agent controls", "agent co
- [agent-observability](skills/ai-agents/agent-observability/SKILL.md) — Monitor and debug AI agent performance — logging, metrics, alerting, cost tracking, error analysis. Triggers on: "agent monitoring", "agent observability", "agent analytics", "agent logging", "agent debug".
- [agent-tool-calling](skills/ai-agents/agent-tool-calling/SKILL.md) — Design agent tool-calling strategies — MCP servers, API integration, function calling, tool selection logic. Triggers on: "agent tools", "MCP server", "tool calling", "function calling", "agent API integration".

### analytics (13)

- [1p-tagging-pixels](skills/analytics/1p-tagging-pixels/SKILL.md) — Set up first-party tracking and analytics — website pixels, conversion tracking, UTM architecture, cookie consent, server-side tagging vs client-side, 1P vs 3P data strategy, and identity resolution. Use when setting up
- [a-b-testing](skills/analytics/a-b-testing/SKILL.md) — A B Testing playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for a b testing work, implementation help, or an agent-ready deliverable.
- [attribution](skills/analytics/attribution/SKILL.md) — Attribution playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for attribution work, implementation help, or an agent-ready deliverable.
- [campaign-analytics](skills/analytics/campaign-analytics/SKILL.md) — Campaign Analytics playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for campaign analytics work, implementation help, or an agent-ready deliverable.
- [deliverability-monitoring](skills/analytics/deliverability-monitoring/SKILL.md) — Deliverability Monitoring playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for deliverability monitoring work, implementation help, or an agent-ready
- [event-analytics](skills/analytics/event-analytics/SKILL.md) — Customer event analytics across every GTM system — Intercom, Zendesk, Salesforce, HubSpot, Segment, Amplitude, Mixpanel, PostHog, and custom event pipelines. Covers event taxonomy design, tracking implementation, event-d
- [growth-experimentation](skills/analytics/growth-experimentation/SKILL.md) — Build a growth experimentation system — ICE scoring, growth sprints, experiment design, statistical significance, and learning repositories. Use when building an experimentation program, running growth sprints, prioritiz
- [gtm-metrics](skills/analytics/gtm-metrics/SKILL.md) — Gtm Metrics playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for gtm metrics work, implementation help, or an agent-ready deliverable.
- [gtm-system-architecture](skills/analytics/gtm-system-architecture/SKILL.md) — Design a complete GTM operating system — revenue model, data model, operating model, growth model, and GTM model per WbD's 6-model framework. Use when designing a GTM system from scratch, auditing an existing one, or ali
- [marketing-strategy](skills/analytics/marketing-strategy/SKILL.md) — Build complete B2B marketing strategies — channel mix, budget allocation, content strategy, demand generation, brand building, and measurement framework. Use when building a marketing plan, allocating marketing budget, d
- [paid-advertising](skills/analytics/paid-advertising/SKILL.md) — Build and manage paid advertising campaigns across B2B platforms — LinkedIn Ads, Google Ads, Meta (Facebook/Instagram) Ads, TikTok Ads, and programmatic. Use when launching paid campaigns, allocating ad budget, selecting
- [proactive-alerts](skills/analytics/proactive-alerts/SKILL.md) — Set up proactive GTM alert systems — CRM pipeline alerts, buying signal notifications, Slack/email routing, risk scoring. Use when building alert systems, monitoring pipeline health, detecting buying signals, or setting
- [tracking-plan](skills/analytics/tracking-plan/SKILL.md) — Master analytics tracking plan for PLG and B2B SaaS — unified event taxonomy, pixel strategy (1P and 3P tagging), marketing attribution architecture, CDP implementation (Segment, Rudderstack), product analytics (Amplitud

### automation (12)

- [ai-sdr-setup](skills/automation/ai-sdr-setup/SKILL.md) — Deploy AI SDR agents safely and effectively — vendor selection, pilot scope, guardrails, signal routing, human handoff design, QA review, and performance metrics. Use when setting up 11x, Artisan, AiSDR, Jason AI, or any
- [api-enrichment](skills/automation/api-enrichment/SKILL.md) — Build API-first enrichment pipelines — provider selection, batching, retries, rate limits, idempotency, webhooks, cost tracking, and CRM writes. Use when integrating enrichment APIs directly into GTM systems or replacing
- [attio-setup](skills/automation/attio-setup/SKILL.md) — Set up Attio for B2B SaaS GTM — programmable CRM, custom objects, workflow automation, enrichment integration, and real-time collaboration. Use when configuring Attio for sales, building a programmable CRM, or migrating
- [clay-automation](skills/automation/clay-automation/SKILL.md) — Build production-grade Clay enrichment workflows — table architecture, waterfall configuration, Claygent AI research, Sculptor table building, CRM push with clay_status properties, credit optimization. Use when building
- [crm-integration](skills/automation/crm-integration/SKILL.md) — Configure CRM systems for GTM — lifecycle stages, deal stages, field ownership, enrichment sync, dedupe, required fields, and reporting. Use when setting up HubSpot, Salesforce, Attio, or any CRM integration for sales an
- [hubspot-setup](skills/automation/hubspot-setup/SKILL.md) — Set up HubSpot for B2B SaaS GTM — CRM configuration, deal pipelines, lifecycle stages, marketing automation, sequences, reporting dashboards, and enrichment integration. Use when configuring HubSpot for sales, marketing,
- [mcp-setup](skills/automation/mcp-setup/SKILL.md) — Configure Model Context Protocol servers for GTM workflows — server selection, tool scope, permissions, guardrails, observability, and multi-tool orchestration. Use when connecting CRM, enrichment, sequencing, analytics,
- [n8n-automation](skills/automation/n8n-automation/SKILL.md) — Build n8n workflows for GTM automation — triggers, webhook-to-enrichment-to-CRM pipelines, error handling, Clay export replacement for complex cases. Use when building n8n workflows or automating GTM processes beyond Cla
- [salesforce-setup](skills/automation/salesforce-setup/SKILL.md) — Set up Salesforce for B2B SaaS GTM — object model, opportunity pipelines, lead management, reports and dashboards, automation (Flows), and enrichment integration. Use when configuring Salesforce for sales or revops. Trig
- [skills-lock](skills/automation/skills-lock/SKILL.md) — skills.lock — version locking and integrity tracking for agent skills repositories. Generates a SHA256-verified lock file that tracks every skill with its version, file hash, dependencies, and last update. Use when creat
- [tool-selection-stack](skills/automation/tool-selection-stack/SKILL.md) — Build the right GTM tool stack for any stage — solo founder ($100/mo), small team ($500/mo), growth team ($2K/mo), and enterprise ($10K+/mo). With cost breakdowns, tool comparisons, and stack architecture. Use when choos
- [waterfall-enrichment](skills/automation/waterfall-enrichment/SKILL.md) — Design multi-provider enrichment waterfalls — provider ordering by cost-per-hit, 3 separate waterfalls for company, email, and phone data, always verify after finding. Use when building enrichment waterfalls or improving

### content-seo (6)

- [aeo-strategy](skills/content-seo/aeo-strategy/SKILL.md) — Answer Engine Optimization — optimize content for AI search engines (ChatGPT, Perplexity, Gemini, Claude). Triggers on: "AEO", "answer engine optimization", "AI search", "generative engine optimization", "GEO", "optimize
- [citation-harvesting](skills/content-seo/citation-harvesting/SKILL.md) — Systematically build backlinks through citations, mentions, and digital PR — HARO, source-blogger outreach, data-driven PR. Triggers on: "citation harvesting", "backlink building", "HARO", "digital PR", "link building".
- [faq-seo](skills/content-seo/faq-seo/SKILL.md) — Build FAQ pages that capture featured snippets and People Also Ask traffic — question-driven content strategy. Triggers on: "FAQ SEO", "featured snippet", "People Also Ask", "question SEO", "answer content".
- [pillar-pages](skills/content-seo/pillar-pages/SKILL.md) — Design and build pillar pages with topic clusters — comprehensive hub pages that rank for high-intent keywords. Triggers on: "pillar page", "topic cluster", "hub page", "cornerstone content", "SEO pillar".
- [pseo-strategy](skills/content-seo/pseo-strategy/SKILL.md) — Programmatic SEO — build scalable, template-driven content pages for long-tail keywords. Triggers on: "pSEO", "programmatic SEO", "scalable SEO", "template SEO", "mass content generation".
- [seo-strategy](skills/content-seo/seo-strategy/SKILL.md) — B2B SEO strategy — keyword research, content architecture, technical SEO, link building, measurement. Triggers on: "SEO strategy", "search engine optimization", "B2B SEO", "keyword research", "SEO plan".

### creative (12)

- [ad-creative-strategy](skills/creative/ad-creative-strategy/SKILL.md) — Develop ad creative strategy for B2B campaigns — creative formats per platform, testing methodology, creative fatigue management, UGC/AI-generated creative, and performance measurement. Use when creating ad creative, man
- [ai-content-creation](skills/creative/ai-content-creation/SKILL.md) — AI-powered content creation workflows — step-by-step processes for using Claude, ChatGPT, Jasper, Copy.ai, Writesonic, and Perplexity to generate, edit, and optimize blog posts, social media content, email sequences, ad
- [ai-video-creation](skills/creative/ai-video-creation/SKILL.md) — AI-powered video creation for marketing — step-by-step workflows for HeyGen (AI spokespersons), Synthesia (AI avatars), Runway (generative video), Captions (AI editing), Opus Clip (AI clipping), ElevenLabs (AI voiceover)
- [content-distribution](skills/creative/content-distribution/SKILL.md) — Distribute content across channels for maximum reach — multi-platform repurposing, syndication, paid amplification, email distribution, and partner promotion. Use when getting content in front of an audience, repurposing
- [copywriting](skills/creative/copywriting/SKILL.md) — Write marketing copy that converts — landing pages, ads, emails, social, headlines, and brand voice. Use when writing any marketing or sales copy beyond cold email. Triggers on: "copywriting", "write copy", "headline", "
- [graphic-design-gtm](skills/creative/graphic-design-gtm/SKILL.md) — Create GTM visual assets — social graphics, ad creatives, pitch deck design, one-pager layouts, email images, data visualization, and brand-consistent templates. Use when creating visual content for GTM, designing social
- [growth-hacking-tactics](skills/creative/growth-hacking-tactics/SKILL.md) — Tactical growth hacking playbook — rapid experimentation, growth loops, viral mechanics, referral flywheels, PLG hacks, content-led growth loops, community-driven growth, and low-cost acquisition tactics for B2B SaaS. Ba
- [landing-page-copy](skills/creative/landing-page-copy/SKILL.md) — Landing page copywriting strategy — conversion copy frameworks, hero headline patterns, value proposition formulas, CTA copy, social proof placement, objection handling in copy, and A/B testing copy at scale. Based on Jo
- [social-media-strategy](skills/creative/social-media-strategy/SKILL.md) — Build and execute social media strategy for B2B — LinkedIn, X/Twitter, posting cadence, engagement tactics, content formats, sizing guides, and platform-specific best practices. Use when building social presence, plannin
- [v0-lander](skills/creative/v0-lander/SKILL.md) — Step-by-step guide to building GTM landing pages with v0 by Vercel — the AI generative UI platform. Covers prompt engineering for v0, iterating on generated UI, exporting to Next.js, deploying on Vercel, and connecting f
- [vibe-coding](skills/creative/vibe-coding/SKILL.md) — AI-powered development for GTM — vibe coding workflows using v0, Cursor, Claude Code, Lovable, Bolt.new, Replit Agent, and Tempo Labs for rapidly building landing pages, marketing sites, tools, dashboards, and prototypes
- [vibe-marketing](skills/creative/vibe-marketing/SKILL.md) — AI-powered marketing at scale — vibe marketing workflows for rapid content generation, creative iteration, campaign launches, and growth experiments using ChatGPT, Claude, Midjourney, Runway, HeyGen, ElevenLabs, and AI v

### customer-success (7)

- [cs-analytics-dashboards](skills/customer-success/cs-analytics-dashboards/SKILL.md) — Build customer success analytics dashboards — NPS, CSAT, CES, customer health scores, churn prediction models, expansion propensity, support volume trends, and CS team performance. Use when designing CS metrics, building
- [cs-playbooks](skills/customer-success/cs-playbooks/SKILL.md) — Build customer success playbooks — onboarding, health scoring, CSQLs, expansion plays, QBRs, and churn intervention. Use when building a CS function, designing customer journeys, or creating playbooks for retention and e
- [customer-onboarding](skills/customer-success/customer-onboarding/SKILL.md) — Design structured customer onboarding programs — time-to-value optimization, activation milestones, kickoff calls, 30-60-90 day plans, handoff from sales to CS, onboarding playbooks by segment, and onboarding health trac
- [headless-support](skills/customer-success/headless-support/SKILL.md) — Design and deploy headless / automated support systems — AI chatbots, Fin AI agents, knowledge base self-serve portals, ticket deflection strategies, automated triage, email auto-responders, and conversational AI. Use wh
- [qbr-planning](skills/customer-success/qbr-planning/SKILL.md) — Plan and execute Quarterly Business Reviews — value documentation, ROI presentation, executive alignment, and expansion roadmap. Use when preparing for QBRs, business reviews with customers, or executive stakeholder meet
- [sla-management](skills/customer-success/sla-management/SKILL.md) — Design and manage customer support SLAs — service level agreements, ticket priority matrices, first response time targets, resolution time targets, escalation paths, business hours configuration, and SLA performance dash
- [support-tool-stack](skills/customer-success/support-tool-stack/SKILL.md) — Customer support platform selection, setup, and optimization — Intercom, Zendesk, Front, Help Scout, HubSpot Service Hub, Linear, and AI-native tools. Use when choosing a support platform, migrating tools, setting up hel

### demand-gen (4)

- [content-syndication](skills/demand-gen/content-syndication/SKILL.md) — Syndicate content across paid and organic channels — content atomization, sponsored placement, newsletter sponsorships, distribution strategy. Triggers on: "content syndication", "content distribution", "syndication stra
- [paid-social-strategy](skills/demand-gen/paid-social-strategy/SKILL.md) — B2B paid social strategy — LinkedIn, Meta, TikTok ad platform strategy, audience building, creative testing, budget allocation. Triggers on: "paid social", "LinkedIn ads", "social advertising", "paid media strategy", "B2
- [podcast-gtm](skills/demand-gen/podcast-gtm/SKILL.md) — Use podcast appearances as a GTM channel — booking strategy, interview prep, content repurposing, pipeline conversion. Triggers on: "podcast GTM", "podcast appearances", "be a podcast guest", "podcast marketing".
- [webinar-strategy](skills/demand-gen/webinar-strategy/SKILL.md) — Plan and execute demand gen webinars — topic selection, speaker sourcing, promotion cadence, follow-up sequences. Triggers on: "webinar", "webinar strategy", "virtual event", "demand gen webinar", "webinar promotion".

### design (7)

- [battlecard-builder](skills/design/battlecard-builder/SKILL.md) — Create competitive battlecards — FIA Framework (Fact → Impact → Act), Why We Win/Why We Lose, objection handling cards per competitor, pricing comparisons, and quick-dismiss summaries. Use when building competitive intel
- [case-study-builder](skills/design/case-study-builder/SKILL.md) — Create customer case studies in sales-ready format — Challenge→Solution→Results structure, before/after metrics, quote integration, two-length formats (1-page summary + full version). Use when creating case studies, cust
- [design-system-gtm](skills/design/design-system-gtm/SKILL.md) — Define brand-context for AI agents — visual identity systems, voice/tone guides, color palettes with hex/RGB/HSL, typography systems with font stacks and type scales, logo usage rules, asset templates, and brand guardrai
- [one-pager-builder](skills/design/one-pager-builder/SKILL.md) — Create one-page sales documents — product overviews, meeting leave-behinds, champion enablement sheets, trade show handouts. Scannable in 30 seconds, memorable enough to forward. Use when creating one-pagers, leave-behin
- [pitch-deck-builder](skills/design/pitch-deck-builder/SKILL.md) — Build investor-ready pitch decks and sales presentations — 10-11 slide structure, persona-customized per role, storytelling frameworks, speaker notes, and visual direction. Use when creating pitch decks, sales decks, inv
- [roi-calculator](skills/design/roi-calculator/SKILL.md) — Build ROI calculators and business cases — 3-scenario projections (conservative, moderate, aggressive), payback period analysis, TCO comparison, assumption documentation, MEDDICC integration, value driver identification.
- [ui-ux-gtm](skills/design/ui-ux-gtm/SKILL.md) — Design GTM UI/UX patterns — landing pages (hero, proof, CTA), forms (progressive disclosure, inline validation), signup flows (activation, time-to-value), dashboards (KPI hierarchy, trend indicators), and accessibility (

### events (3)

- [conference-strategy](skills/events/conference-strategy/SKILL.md) — Strategic conference planning — event selection, sponsorship ROI, speaking submissions, booth strategy, team preparation. Triggers on: "conference strategy", "event planning", "trade show strategy", "sponsorship ROI", "C
- [event-driven-outreach](skills/events/event-driven-outreach/SKILL.md) — Outbound sequences triggered by conference/event attendance — pre-event research, on-site plays, post-event follow-up. Triggers on: "event outreach", "conference prospecting", "trade show follow-up", "event outbound".
- [field-marketing](skills/events/field-marketing/SKILL.md) — Plan and execute field marketing — regional events, executive dinners, roadshows, customer advisory boards. Triggers on: "field marketing", "executive dinner", "roadshow", "regional event", "customer event".

### foundation (8)

- [buyer-psychology](skills/foundation/buyer-psychology/SKILL.md) — Apply decision science and buyer psychology to GTM — transparency effect (4.2-4.5), Cialdini principles, prediction over persuasion, trust mechanics. Use when designing messaging, building pitch decks, crafting positioni
- [competitive-intel](skills/foundation/competitive-intel/SKILL.md) — Competitive Intel playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for competitive intel work, implementation help, or an agent-ready deliverable.
- [gtm-context](skills/foundation/gtm-context/SKILL.md) — Gtm Context playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for gtm context work, implementation help, or an agent-ready deliverable.
- [icp-scoring](skills/foundation/icp-scoring/SKILL.md) — Icp Scoring playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for icp scoring work, implementation help, or an agent-ready deliverable.
- [icp-targeting-tiers](skills/foundation/icp-targeting-tiers/SKILL.md) — Define ICP differences across small business, mid-market, and enterprise — buying process, deal size, sales motion, tool stack, messaging by tier. Use when segmenting GTM by company size, designing tier-specific plays, o
- [positioning-messaging](skills/foundation/positioning-messaging/SKILL.md) — Positioning Messaging playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for positioning messaging work, implementation help, or an agent-ready deliver
- [pricing-strategy](skills/foundation/pricing-strategy/SKILL.md) — Pricing Strategy playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for pricing strategy work, implementation help, or an agent-ready deliverable.
- [using-gtm-skills](skills/foundation/using-gtm-skills/SKILL.md) — Complete guide to using the gtm-skills repository — installation, skill discovery, skill loading, combining skills, taxonomy navigation, CLI workflows, and advanced patterns for every supported AI system (Claude Code, Cu

### founder-led (37)

- [advisor-recruitment](skills/founder-led/advisor-recruitment/SKILL.md) — Strategic advisor recruitment for B2B SaaS founders. Use when building advisory board, recruiting individual advisors, structuring advisor compensation (equity grants), defining advisory scope, leveraging advisors for in
- [board-meeting-prep](skills/founder-led/board-meeting-prep/SKILL.md) — Board meeting preparation for B2B SaaS founders. Use when preparing quarterly board meetings, building board decks, selecting metrics to present, crafting narrative, managing board relationships, or handling difficult bo
- [brand-kit](skills/founder-led/brand-kit/SKILL.md) — Build a complete brand kit for B2B SaaS — logo design and usage, color palette, typography, voice and tone, visual identity, brand guidelines, and asset templates. Use when creating a brand from scratch, rebranding, or b
- [building-saas](skills/founder-led/building-saas/SKILL.md) — Build a SaaS company from idea to scale — product development, architecture decisions, pricing, hiring sequence, fundraising stages, and operational infrastructure. Use when starting a SaaS, scaling from $0 to $10M ARR,
- [business-insurance](skills/founder-led/business-insurance/SKILL.md) — Complete business insurance guide for SaaS founders — Errors & Omissions (E&O/Tech E&O), Cyber Liability, Directors & Officers (D&O), General Liability, Workers Compensation, Key Person, Employment Practices Liability (E
- [co-founder-dynamics](skills/founder-led/co-founder-dynamics/SKILL.md) — Complete co-founder playbook for technical founders — finding co-founders, equity splits (dynamic and static), co-founder agreements, vesting schedules, working relationships, conflict resolution, co-founder breakups, an
- [content-led-growth](skills/founder-led/content-led-growth/SKILL.md) — Content-led growth strategy for B2B SaaS founders. Use when building a founder-led content engine, designing content as a GTM channel, scaling content production, measuring content ROI, repurposing across channels, or bu
- [data-privacy-compliance](skills/founder-led/data-privacy-compliance/SKILL.md) — Data privacy compliance for B2B SaaS — GDPR, CCPA/CPRA, ePrivacy Directive, cookie consent, Data Processing Agreements (DPAs), Standard Contractual Clauses (SCCs), Data Protection Impact Assessments (DPIAs), subject acce
- [employment-compliance](skills/founder-led/employment-compliance/SKILL.md) — Employment law and compliance for B2B SaaS founders — contractor vs employee classification, offer letters, IP assignment (PIIA), at-will employment, equity documentation, employee handbooks, harassment policies, termina
- [engineer-to-founder](skills/founder-led/engineer-to-founder/SKILL.md) — Engineer To Founder playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for engineer to founder work, implementation help, or an agent-ready deliverable
- [equity-management](skills/founder-led/equity-management/SKILL.md) — Complete equity management for SaaS founders — cap tables, 409A valuations, option pools (ISO vs NSO vs RSU), 83(b) elections, equity grants for employees/advisors/contractors, dilution modeling, secondary sales, and equ
- [events-planning](skills/founder-led/events-planning/SKILL.md) — Plan and execute B2B events — conferences, webinars, dinners, happy hours, trade shows, and owned events. Use when planning any business event to generate pipeline or build community. Triggers on: "event planning", "plan
- [exiting-company](skills/founder-led/exiting-company/SKILL.md) — Prepare a SaaS company for acquisition or exit — valuation drivers, due diligence readiness, financial preparation, legal structuring, and exit timeline. Use when planning an exit, preparing for acquisition, or maximizin
- [financial-modeling](skills/founder-led/financial-modeling/SKILL.md) — SaaS financial modeling for founders — operating model, runway, headcount, DCF valuation, consumption-based pricing models, cohort analysis, unit economics by segment, ARR bridge/build, 3-scenario forecasting, and board-
- [first-hires-playbook](skills/founder-led/first-hires-playbook/SKILL.md) — Complete playbook for founder's first 10 hires beyond sales. Use when hiring first engineer, first CS, first marketer, first product manager, or building founding team. Covers when to hire each role, job description arch
- [founder-brand](skills/founder-led/founder-brand/SKILL.md) — Build a founder personal brand — LinkedIn strategy, content cadence, podcast guesting, newsletter growth, media features, and community building. Use when building personal brand, growing audience, or establishing though
- [founder-sales](skills/founder-led/founder-sales/SKILL.md) — Founder-led sales playbook for $0-5M ARR stages. Use when founder is primary seller, building sales process from scratch, transitioning from founder-led to AE-led, or designing demo/negotiation/close motions as a technic
- [fundraising-strategy](skills/founder-led/fundraising-strategy/SKILL.md) — Complete fundraising strategy for B2B SaaS founders. Use when preparing to raise seed/Series A, deciding VC vs bootstrapped path, building pitch deck, running a fundraise process, evaluating term sheets, or planning fund
- [hiring-agencies](skills/founder-led/hiring-agencies/SKILL.md) — Evaluate, hire, and manage agencies for SaaS GTM — outbound agencies, dev shops, marketing agencies, and design studios. When to use an agency vs hiring in-house, how to structure engagements, and how to measure ROI. Tri
- [hiring-by-role](skills/founder-led/hiring-by-role/SKILL.md) — Role-specific hiring guides for B2B SaaS — interview questions, evaluation criteria, scorecards, and assessment methods for engineering, sales, marketing, customer success, product, and design roles. Based on best practi
- [hiring-contractors](skills/founder-led/hiring-contractors/SKILL.md) — Hire and manage contractors for SaaS startups — where to find them, how to structure engagements, IP assignment, rates by role, and management practices that produce quality work without full-time overhead. Use when hiri
- [investor-updates](skills/founder-led/investor-updates/SKILL.md) — Write investor updates that build confidence and surface help — monthly format, board deck structure, fundraising narrative, and metrics dashboards. Use when writing investor updates, preparing board meetings, or communi
- [job-posting-strategy](skills/founder-led/job-posting-strategy/SKILL.md) — Complete job posting and distribution strategy for B2B SaaS companies — where to post by role (engineering, sales, marketing, CS, product, design), job board comparison, posting templates, sourcing channels, and expert r
- [launch-planning](skills/founder-led/launch-planning/SKILL.md) — Launch Planning playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for launch planning work, implementation help, or an agent-ready deliverable.
- [lead-magnets](skills/founder-led/lead-magnets/SKILL.md) — Lead Magnets playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for lead magnets work, implementation help, or an agent-ready deliverable.
- [legal-for-founders](skills/founder-led/legal-for-founders/SKILL.md) — Complete legal playbook for SaaS founders — incorporation (Delaware C-Corp vs LLC), IP assignment, Terms of Service, Privacy Policy, NDAs, consulting agreements, co-founder IP, fundraising legal (SAFE, priced round, boar
- [partner-programs](skills/founder-led/partner-programs/SKILL.md) — Partner Programs playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for partner programs work, implementation help, or an agent-ready deliverable.
- [pricing-psychology](skills/founder-led/pricing-psychology/SKILL.md) — SaaS pricing psychology and tactics for B2B founders. Use when designing pricing tiers, testing price points, building pricing pages, handling discounting strategy, adding new pricing dimensions, or optimizing monetizati
- [saas-metrics-calculator](skills/founder-led/saas-metrics-calculator/SKILL.md) — Saas Metrics Calculator playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for saas metrics calculator work, implementation help, or an agent-ready del
- [sales-team-building](skills/founder-led/sales-team-building/SKILL.md) — Build a B2B sales team from first hire to scale — hiring sequence by ARR stage, WbD POD structures, compensation models (linear/accelerated/split), draw mechanics, REKS coaching, and WbD GTM Index for scaling readiness.
- [security-assessments](skills/founder-led/security-assessments/SKILL.md) — Security assessment and vendor risk management for B2B SaaS — penetration testing, vulnerability scanning, bug bounty programs, security questionnaires (VSAQ/SIG/CAIQ), incident response planning, disaster recovery, and
- [soc2-compliance](skills/founder-led/soc2-compliance/SKILL.md) — Achieve SOC2 Type II compliance for SaaS companies — readiness assessment, control implementation, auditor selection, evidence collection, and ongoing monitoring. Use when preparing for SOC2, responding to enterprise sec
- [solo-founder-gtm](skills/founder-led/solo-founder-gtm/SKILL.md) — Build lean GTM as a solo founder or bootstrapper — tool stacks by revenue stage, AI agents replacing headcount, when to make the first hire, bootstrapper economics, and the WbD GTM Index for self-assessment. Use when bui
- [startup-communities](skills/founder-led/startup-communities/SKILL.md) — Startup Communities playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for startup communities work, implementation help, or an agent-ready deliverable
- [vc-outreach](skills/founder-led/vc-outreach/SKILL.md) — Vc Outreach playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for vc outreach work, implementation help, or an agent-ready deliverable.
- [vendor-contracts](skills/founder-led/vendor-contracts/SKILL.md) — Vendor contracts, MSAs, DPAs, and procurement for B2B SaaS — master service agreements, service level agreements, data processing agreements, order forms, vendor security assessments, and contract negotiation playbooks.
- [yc-ecosystem](skills/founder-led/yc-ecosystem/SKILL.md) — Yc Ecosystem playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for yc ecosystem work, implementation help, or an agent-ready deliverable.

### growth (4)

- [churn-prevention](skills/growth/churn-prevention/SKILL.md) — Build churn prevention systems — early warning signal detection, customer health scoring, re-engagement campaigns, risk tier routing, and champion departure monitoring. Use when reducing churn, building retention systems
- [customer-marketing](skills/growth/customer-marketing/SKILL.md) — Customer marketing and advocacy programs — case studies, testimonials, customer reference programs, NPS-driven advocacy, customer communities, user conferences, champion programs, logo usage, and review generation (G2, C
- [expansion-selling](skills/growth/expansion-selling/SKILL.md) — Complete expansion and upsell playbook for B2B SaaS — consumption-based upsell triggers, cross-sell identification, seat expansion, tier upgrades, NRR growth strategies, land-and-expand motions, expansion propensity scor
- [referral-programs](skills/growth/referral-programs/SKILL.md) — Design customer and partner referral programs — 3-tier comp structure, referral tracking, platform integration, double-sided rewards, viral mechanics, referral leaderboards, and measuring referral revenue. Use when build

### gtm-ops (3)

- [campaign-governance](skills/gtm-ops/campaign-governance/SKILL.md) — Establish campaign governance — naming conventions, UTM parameters, campaign hierarchy, ROI measurement, budget tracking. Triggers on: "campaign governance", "UTM strategy", "campaign naming", "marketing ops governance".
- [gtm-operations](skills/gtm-ops/gtm-operations/SKILL.md) — Build GTM operations function — tech stack architecture, process design, data governance, RevOps foundations. Triggers on: "GTM ops", "RevOps", "revenue operations", "sales ops", "GTM infrastructure".
- [revops-tech-stack](skills/gtm-ops/revops-tech-stack/SKILL.md) — Design the RevOps technology stack — CRM, enrichment, sequencing, analytics, integration architecture. Triggers on: "RevOps stack", "sales tech stack", "GTM tool audit", "revenue technology".

### inbound (4)

- [content-marketing](skills/inbound/content-marketing/SKILL.md) — Build content marketing strategies that generate pipeline — SEO/AEO optimization, pillar page design, programmatic SEO, content-to-pipeline mapping. Use when the user wants to plan content strategy, build a content calen
- [inbound-triage](skills/inbound/inbound-triage/SKILL.md) — Design inbound lead triage workflows — demo form qualification, MQL to SQL routing, automated enrichment on form fill, speed-to-lead SLAs. Use when the user wants to handle inbound leads, route demo requests, qualify for
- [landing-pages](skills/inbound/landing-pages/SKILL.md) — Audit and optimize landing pages for conversion — hero/offer/proof/CTA patterns, CRO audits, A/B testing, signup flow optimization. Use when the user wants to improve conversion rates, audit a landing page, optimize a si
- [social-selling](skills/inbound/social-selling/SKILL.md) — Build a LinkedIn social selling strategy — Sales Navigator, DM sequences, content-to-conversation, profile optimization, and SSI scoring. Use when the user wants to sell on LinkedIn, build a LinkedIn presence, use Sales

### leadmagic (6)

- [leadmagic-bulk-enrichment](skills/leadmagic/leadmagic-bulk-enrichment/SKILL.md) — Process CSV files with LeadMagic at scale — input cleanup, batch sizing, validation status handling, webhook callbacks, CRM export, error recovery, and quality checks. Use when enriching a list, bulk validating contacts,
- [leadmagic-cli](skills/leadmagic/leadmagic-cli/SKILL.md) — Use the LeadMagic CLI for enrichment automation — find emails, validate contacts, enrich CSVs in batch, find decision-makers by role, and push to outbound platforms (Smartlead, Instantly). Use when automating enrichment
- [leadmagic-integrations](skills/leadmagic/leadmagic-integrations/SKILL.md) — Integrate LeadMagic with GTM platforms — Clay, Apollo, Smartlead, Instantly, Salesforce, HubSpot, Zapier, Make. Bi-directional data flows, webhook enrichment, CRM automation, and verification-at-send patterns. Use when c
- [leadmagic-job-change](skills/leadmagic/leadmagic-job-change/SKILL.md) — Use LeadMagic job-change signals for pipeline intelligence — champion tracking, account risk alerts, new-role outreach, replacement mapping, and CRM routing. Use when monitoring career moves or building trigger-based sal
- [leadmagic-mcp](skills/leadmagic/leadmagic-mcp/SKILL.md) — Set up LeadMagic MCP for AI agents — tool discovery, permission scope, safe enrichment workflows, batch usage, verification steps, and agent handoff patterns. Use when connecting LeadMagic data tools to Claude, Cursor, V
- [leadmagic-waterfall](skills/leadmagic/leadmagic-waterfall/SKILL.md) — Build Clay enrichment waterfalls with LeadMagic as the primary provider — 95%+ email coverage, multi-provider chaining, verification integration, catch-all resolution. Use when setting up LeadMagic in Clay workflows, bui

### lifecycle (5)

- [churn-prediction](skills/lifecycle/churn-prediction/SKILL.md) — Build churn prediction models — leading indicators, risk scoring, early warning systems, intervention playbooks. Triggers on: "churn prediction", "predict churn", "churn model", "early warning", "risk scoring".
- [lifecycle-drips](skills/lifecycle/lifecycle-drips/SKILL.md) — Design lifecycle drip campaigns — post-purchase, renewal, expansion, milestone-based automated email programs. Triggers on: "lifecycle drips", "automated campaigns", "lifecycle emails", "drip sequences", "triggered email
- [mql-nurture](skills/lifecycle/mql-nurture/SKILL.md) — Build MQL nurture programs — lead scoring, nurture tracks, email drip sequences, MQL→SQL conversion. Triggers on: "MQL nurture", "lead nurture", "nurture tracks", "MQL to SQL", "lead scoring".
- [onboarding-sequences](skills/lifecycle/onboarding-sequences/SKILL.md) — Design customer onboarding sequences — time-to-first-value, activation milestones, guided setup, onboarding emails. Triggers on: "onboarding sequence", "customer onboarding", "time to value", "activation flow", "new cust
- [re-engagement](skills/lifecycle/re-engagement/SKILL.md) — Design re-engagement campaigns for dormant leads and inactive customers — win-back sequences, reactivation offers, sunset policies. Triggers on: "re-engagement", "win-back", "reactivation", "dormant leads", "inactive cus

### management-leadership (2)

- [sales-coaching](skills/management-leadership/sales-coaching/SKILL.md) — Coach sales reps for consistent performance — REKS framework, deal reviews, call coaching, pipeline inspection, and 1:1 cadences. Use when setting up sales coaching, training managers, or improving rep performance. Trigg
- [team-management](skills/management-leadership/team-management/SKILL.md) — Team management for startup leaders — 1:1s, performance reviews, goal setting (OKRs), delegation, feedback culture, remote team management, team rituals, and scaling from IC to manager. Use when building team processes,

### outbound (9)

- [cold-calling](skills/outbound/cold-calling/SKILL.md) — Build and execute B2B cold calling programs — phone intent scoring, precision dialing, the Buckets methodology, multi-touch cadences, and conversation-to-meeting conversion. Use when setting up cold calling, training SDR
- [cold-email-copywriting](skills/outbound/cold-email-copywriting/SKILL.md) — Writes high-converting cold email copy using the 3-line framework, proven subject line patterns, and persona-specific variants. Use when the user asks to write, improve, or critique cold email copy, craft subject lines,
- [cold-email-strategy](skills/outbound/cold-email-strategy/SKILL.md) — Designs high-performing cold email sequence architecture with proper cadence timing, channel mixing, and trigger-based logic. Use when the user asks to build, audit, or optimize a cold outreach sequence, design a multi-t
- [domain-infrastructure](skills/outbound/domain-infrastructure/SKILL.md) — Designs and provisions the domain and mailbox infrastructure for cold email outreach: secondary domains, mailbox setup (Google Workspace, M365, Zoho), DNS authentication records, inbox rotation, and primary domain isolat
- [email-deliverability](skills/outbound/email-deliverability/SKILL.md) — Sets up and monitors email deliverability infrastructure including SPF, DKIM, DMARC configuration, warmup strategy, reputation monitoring, bounce and complaint handling, and ongoing deliverability health. Use when the us
- [inbox-setup](skills/outbound/inbox-setup/SKILL.md) — Set up cold email inbox infrastructure from scratch — Google Workspace, Microsoft 365, and Azure/Entra inbox provisioning, DNS authentication, domain buying, warmup, and cost optimization. Use when setting up sending inf
- [multi-channel-outreach](skills/outbound/multi-channel-outreach/SKILL.md) — Design and execute multi-channel outbound sequences across email, LinkedIn, cold calls, and SMS. Use when the user wants to coordinate outreach across channels, build multi-touch sequences, add LinkedIn to their outbound
- [reply-handling](skills/outbound/reply-handling/SKILL.md) — Classifies and automates responses to cold email replies using an 8-category taxonomy, auto-reply playbooks, and human escalation rules. Use when the user asks to set up reply handling, needs reply classification logic,
- [sending-platforms](skills/outbound/sending-platforms/SKILL.md) — Compares, selects, and configures cold email sending platforms: Smartlead, Instantly, Salesforge, Apollo, and others. Use when the user asks which sending platform to use, needs to compare features or pricing, wants to m

### partnerships (3)

- [co-marketing](skills/partnerships/co-marketing/SKILL.md) — Execute co-marketing campaigns with partners — joint webinars, co-branded content, shared audiences, mutual promotion. Triggers on: "co-marketing", "joint marketing", "partner marketing", "co-branded campaign".
- [integration-partnerships](skills/partnerships/integration-partnerships/SKILL.md) — Build and go-to-market with technology integration partnerships — API/integration GTM, marketplace listing, co-selling. Triggers on: "integration partnership", "tech partnership", "API partnership", "marketplace listing"
- [partnership-strategy](skills/partnerships/partnership-strategy/SKILL.md) — Build a partnership program — partner types, recruitment, enablement, co-marketing, revenue share models. Triggers on: "partnership strategy", "partner program", "channel partnerships", "build partnerships".

### product-led-growth (2)

- [freemium-optimization](skills/product-led-growth/freemium-optimization/SKILL.md) — Freemium and free trial conversion optimization — activation flow design, paywall placement, upgrade triggers, PQL scoring, time-to-value reduction, and freemium monetization models. Use when optimizing freemium conversi
- [plg-strategy](skills/product-led-growth/plg-strategy/SKILL.md) — Design product-led growth motions — freemium vs free trial, PQL scoring, self-serve conversion, PLG sales hybrid, and product-led marketing. Use when building a PLG motion, transitioning to self-serve, or optimizing prod

### prospecting (7)

- [contact-verification](skills/prospecting/contact-verification/SKILL.md) — Verify email addresses before they enter outbound sequences to prevent bounces and protect sender reputation. Use when the user wants to validate emails, check deliverability, verify contact data, prevent bounces, clean
- [data-enrichment-strategy](skills/prospecting/data-enrichment-strategy/SKILL.md) — Design an end-to-end B2B data enrichment architecture — provider selection, waterfall design, cost modeling, and CRM hygiene. Use when the user wants to evaluate enrichment providers, build an enrichment stack, compare d
- [email-finding](skills/prospecting/email-finding/SKILL.md) — Find verified work email addresses for B2B contacts using multi-provider waterfall discovery. Use when the user wants to find emails, look up contact information, discover email patterns, enrich a list with email address
- [lead-enrichment](skills/prospecting/lead-enrichment/SKILL.md) — Lead Enrichment playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for lead enrichment work, implementation help, or an agent-ready deliverable.
- [lead-finding](skills/prospecting/lead-finding/SKILL.md) — Lead Finding playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for lead finding work, implementation help, or an agent-ready deliverable.
- [list-building](skills/prospecting/list-building/SKILL.md) — Build qualified B2B prospect lists using Clay, LinkedIn Sales Navigator, and multi-source discovery. Use when the user wants to build a prospect list, create a target account list, find companies matching an ICP, scrape
- [signal-scoring](skills/prospecting/signal-scoring/SKILL.md) — Score and prioritize prospects using buying signals — hiring, funding, tech stack changes, executive moves, and intent data. Use when the user wants to score leads, prioritize outreach, detect buying intent, rank prospec

### sales-plays (5)

- [earnings-signal-play](skills/sales-plays/earnings-signal-play/SKILL.md) — Outbound play triggered by public company earnings calls — strategic priority mining, new-initiative alignment, urgency creation. Triggers on: "earnings signal", "earnings play", "public company outbound", "10-K outreach
- [funding-signal-play](skills/sales-plays/funding-signal-play/SKILL.md) — Trigger-based outbound play when a target account raises funding — urgency messaging, use-of-funds alignment, 7-14 day window. Triggers on: "funding signal", "funding play", "raised money outreach", "funding announcement
- [hiring-signal-play](skills/sales-plays/hiring-signal-play/SKILL.md) — Outbound play triggered by specific hiring signals — VP Sales, RevOps, SDR manager, CRO postings signal budget and strategy shift. Triggers on: "hiring signal", "job post outbound", "hiring trigger", "new role outreach".
- [job-change-play](skills/sales-plays/job-change-play/SKILL.md) — Outbound play triggered by contact job changes — champion tracking, new-role outreach, "new broom" timing. Triggers on: "job change", "new role", "champion moved", "job change outreach", "contact changed jobs".
- [product-launch-play](skills/sales-plays/product-launch-play/SKILL.md) — Outbound play triggered by competitor product launches or target account product launches — timing-based urgency, competitive positioning. Triggers on: "product launch play", "competitor launch response", "launch-based o

### sales-revops (7)

- [deal-desk](skills/sales-revops/deal-desk/SKILL.md) — Structure deals, pricing, and proposals — pricing model selection, discount guidance, business case construction, and negotiation strategy. Use when structuring a deal, building a pricing proposal, negotiating, or creati
- [demo-scripts](skills/sales-revops/demo-scripts/SKILL.md) — Write compelling demo scripts — first demo, technical deep-dive, and executive overview. Scene-by-scene with timing, talk tracks, and interaction points. Use when building demo scripts, preparing for a demo, or structuri
- [meeting-prep](skills/sales-revops/meeting-prep/SKILL.md) — Prepare comprehensive meeting briefs — account research, attendee profiles, SPIN/MEDDIC discovery questions, competitive context. Use when preparing for a sales call, discovery meeting, demo, or any prospect interaction.
- [objection-handling](skills/sales-revops/objection-handling/SKILL.md) — Build comprehensive objection handling playbooks — 6-category taxonomy, AER framework, battlecards per competitor, pre-handling in outreach. Use when creating objection responses, building an objection playbook, or prepa
- [pipeline-management](skills/sales-revops/pipeline-management/SKILL.md) — Manage B2B sales pipelines with structured deal stages, forecasting, CRM hygiene, and deal inspection cadences. Use when setting up pipeline processes, improving forecast accuracy, or designing deal stages. Triggers on:
- [sales-enablement](skills/sales-revops/sales-enablement/SKILL.md) — Create sales collateral that reps actually use — pitch decks, one-pagers, battlecards, objection docs, demo scripts, talk tracks, and playbooks. Use when the user wants to create sales materials, build a pitch deck, writ
- [transparency-selling](skills/sales-revops/transparency-selling/SKILL.md) — Execute Todd Caponi's Transparency Sale methodology — lead with flaws, build the "Our Flaws" slide, negotiate with radical honesty, use the 4.2-4.5 effect in positioning. Use when building pitch decks, handling objection

### sequencing-tools (6)

- [hubspot-sequences](skills/sequencing-tools/hubspot-sequences/SKILL.md) — Design and optimize HubSpot sequences — enrollment triggers, multi-channel steps, task creation, analytics, A/B testing. Triggers on: "HubSpot sequences", "HubSpot automation", "HubSpot cadence", "sales hub sequences".
- [instantly-sequences](skills/sequencing-tools/instantly-sequences/SKILL.md) — Set up Instantly — unlimited accounts, warmup pool, campaign optimization, unified inbox. Triggers on: "Instantly", "Instantly setup", "Instantly campaigns", "Instantly warmup".
- [lemlist-setup](skills/sequencing-tools/lemlist-setup/SKILL.md) — Set up and optimize Lemlist — personalized images/videos, multi-channel sequences, warm-up, deliverability. Triggers on: "Lemlist", "Lemlist setup", "Lemlist campaigns", "personalized cold email".
- [outreach-sequences](skills/sequencing-tools/outreach-sequences/SKILL.md) — Design and manage Outreach sequences — multi-channel cadences, triggers, analytics, team workflows. Triggers on: "Outreach sequences", "Outreach cadence", "Outreach setup", "Outreach automation".
- [salesloft-cadences](skills/sequencing-tools/salesloft-cadences/SKILL.md) — Build and optimize Salesloft cadences — Rhythm, Conversations, multi-channel orchestration, analytics. Triggers on: "Salesloft", "Salesloft cadence", "Rhythm", "Salesloft automation".
- [smartlead-workflows](skills/sequencing-tools/smartlead-workflows/SKILL.md) — Set up and run Smartlead — unlimited mailboxes, auto-rotation, A/B testing, master inbox, AI categorization. Triggers on: "Smartlead", "Smartlead setup", "Smartlead campaigns", "unlimited mailboxes".

### tools (7)

- [analytics-toolkit](skills/tools/analytics-toolkit/SKILL.md) — Complete analytics tools toolkit — Segment CDP, Amplitude, Mixpanel, PostHog, GA4, and HubSpot analytics configuration. Covers implementation patterns, destination routing, event governance, and cross-tool reporting. Use
- [clay-toolkit](skills/tools/clay-toolkit/SKILL.md) — Complete Clay platform toolkit — table architecture, waterfall enrichment, Claygent AI agent, credit optimization, CRM push, webhook webhooks, formula writing, and advanced Clay workflows for GTM automation. Use when bui
- [crm-toolkit](skills/tools/crm-toolkit/SKILL.md) — Complete CRM operations toolkit — HubSpot, Salesforce, and Attio deep-dive configuration, enrichment integration, pipeline automation, and data hygiene. Use when building CRM workflows, integrating enrichment, designing
- [leadmagic-toolkit](skills/tools/leadmagic-toolkit/SKILL.md) — Complete LeadMagic platform toolkit — API reference, CLI workflows, MCP server setup, enrichment waterfalls, bulk processing, job change detection, and integration patterns. Use when building LeadMagic-powered GTM infras
- [n8n-toolkit](skills/tools/n8n-toolkit/SKILL.md) — Complete n8n automation toolkit for GTM — workflow design patterns, webhook-to-enrichment-to-CRM pipelines, HTTP Request nodes for API integration, error handling, and production deployment. Use when building n8n workflo
- [sequencing-toolkit](skills/tools/sequencing-toolkit/SKILL.md) — Complete outreach sequencing toolkit — Smartlead, Instantly, Salesloft, Outreach, Lemlist setup and optimization. Covers mailbox rotation, warmup, A/B testing, deliverability monitoring, and multi-channel orchestration a
- [support-toolkit](skills/tools/support-toolkit/SKILL.md) — Complete customer support tools toolkit — Intercom, Zendesk, Front, Help Scout deep-dive configuration, AI agent setup, knowledge base optimization, and support analytics. Use when selecting, setting up, or optimizing a

## Validate

```bash
npm run build
npm run check
gh skill publish --dry-run
```

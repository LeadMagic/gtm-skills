# GTM Skills

189 production go-to-market skills for Claude-compatible agents. Skills are self-contained folders with instructions, scripts, references, assets/templates, and metadata that agents load through progressive disclosure.

## Anthropic / agentskills Alignment

- Every skill is a folder with required SKILL.md and optional scripts/, references/, templates/, or assets/.
- Discovery loads name + description; activation loads SKILL.md; execution loads support files only when needed.
- Marketplace-visible paths are exactly skills/<category>/<skill>/SKILL.md.
- Use the narrowest skill that matches the task; combine skills only when the workflow requires it.

## Skills Index

### abm (6)
- **abm-1-to-1** — Execute Strategic ABM (1-to-1) for 5-15 high-value accounts — custom microsites, executive engagement, direct mail, board-level connections, custom content. Triggers on: "1-to-1 AB
- **abm-1-to-few** — Execute ABM at Scale (1-to-few) for 15-50 clustered accounts — semi-custom campaigns, industry-specific content, persona-based plays. Triggers on: "1-to-few ABM", "ABM scale", "clu
- **abm-1-to-many** — Execute Programmatic ABM (1-to-many) for 50-200+ accounts — automated personalization, scaled outbound, lookalike expansion. Triggers on: "1-to-many ABM", "programmatic ABM", "scal
- **abm-strategy** — Design and execute Account-Based Marketing strategy — tier selection, account scoring, channel orchestration, BDR alignment, measurement framework. Triggers on: "ABM strategy", "ac
- **account-selection** — Select and prioritize target accounts for ABM programs — scoring models, tier assignment, TAM segmentation. Triggers on: "account selection", "target account list", "tier accounts"
- **multi-thread-orchestration** — Orchestrate multi-threaded ABM engagement across buying committee members — stakeholder mapping, parallel plays, ghost node detection. Triggers on: "multi-thread", "stakeholder map

### ai-agents (4)
- **agent-architecture** — Design AI agent architectures for GTM workflows — agent patterns, tool selection, multi-agent orchestration, human-in-the-loop. Triggers on: "agent architecture", "AI agent design"
- **agent-guardrails** — Implement safety guardrails for GTM agents — content filtering, approval gates, rate limiting, budget controls, kill switches. Triggers on: "agent guardrails", "agent safety", "AI
- **agent-observability** — Monitor and debug AI agent performance — logging, metrics, alerting, cost tracking, error analysis. Triggers on: "agent monitoring", "agent observability", "agent analytics", "agen
- **agent-tool-calling** — Design agent tool-calling strategies — MCP servers, API integration, function calling, tool selection logic. Triggers on: "agent tools", "MCP server", "tool calling", "function cal

### analytics (13)
- **1p-tagging-pixels** — Set up first-party tracking and analytics — website pixels, conversion tracking, UTM architecture, cookie consent, server-side tagging vs client-side, 1P vs 3P data strategy, and i
- **a-b-testing** — A B Testing playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for a b testing work, implementation help, or an
- **attribution** — Attribution playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for attribution work, implementation help, or an
- **campaign-analytics** — Campaign Analytics playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for campaign analytics work, implementati
- **deliverability-monitoring** — Deliverability Monitoring playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for deliverability monitoring work
- **event-analytics** — Customer event analytics across every GTM system — Intercom, Zendesk, Salesforce, HubSpot, Segment, Amplitude, Mixpanel, PostHog, and custom event pipelines. Covers event taxonomy
- **growth-experimentation** — Build a growth experimentation system — ICE scoring, growth sprints, experiment design, statistical significance, and learning repositories. Use when building an experimentation pr
- **gtm-metrics** — Gtm Metrics playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for gtm metrics work, implementation help, or an
- **gtm-system-architecture** — Design a complete GTM operating system — revenue model, data model, operating model, growth model, and GTM model per WbD's 6-model framework. Use when designing a GTM system from s
- **marketing-strategy** — Build complete B2B marketing strategies — channel mix, budget allocation, content strategy, demand generation, brand building, and measurement framework. Use when building a market
- **paid-advertising** — Build and manage paid advertising campaigns across B2B platforms — LinkedIn Ads, Google Ads, Meta (Facebook/Instagram) Ads, TikTok Ads, and programmatic. Use when launching paid ca
- **proactive-alerts** — Set up proactive GTM alert systems — CRM pipeline alerts, buying signal notifications, Slack/email routing, risk scoring. Use when building alert systems, monitoring pipeline healt
- **tracking-plan** — Master analytics tracking plan for PLG and B2B SaaS — unified event taxonomy, pixel strategy (1P and 3P tagging), marketing attribution architecture, CDP implementation (Segment, R

### automation (12)
- **ai-sdr-setup** — Deploy AI SDR agents safely and effectively — vendor selection, pilot scope, guardrails, signal routing, human handoff design, QA review, and performance metrics. Use when setting
- **api-enrichment** — Build API-first enrichment pipelines — provider selection, batching, retries, rate limits, idempotency, webhooks, cost tracking, and CRM writes. Use when integrating enrichment API
- **attio-setup** — Set up Attio for B2B SaaS GTM — programmable CRM, custom objects, workflow automation, enrichment integration, and real-time collaboration. Use when configuring Attio for sales, bu
- **clay-automation** — Build production-grade Clay enrichment workflows — table architecture, waterfall configuration, Claygent AI research, Sculptor table building, CRM push with clay_status properties,
- **crm-integration** — Configure CRM systems for GTM — lifecycle stages, deal stages, field ownership, enrichment sync, dedupe, required fields, and reporting. Use when setting up HubSpot, Salesforce, At
- **hubspot-setup** — Set up HubSpot for B2B SaaS GTM — CRM configuration, deal pipelines, lifecycle stages, marketing automation, sequences, reporting dashboards, and enrichment integration. Use when c
- **mcp-setup** — Configure Model Context Protocol servers for GTM workflows — server selection, tool scope, permissions, guardrails, observability, and multi-tool orchestration. Use when connecting
- **n8n-automation** — Build n8n workflows for GTM automation — triggers, webhook-to-enrichment-to-CRM pipelines, error handling, Clay export replacement for complex cases. Use when building n8n workflow
- **salesforce-setup** — Set up Salesforce for B2B SaaS GTM — object model, opportunity pipelines, lead management, reports and dashboards, automation (Flows), and enrichment integration. Use when configur
- **skills-lock** — skills.lock — version locking and integrity tracking for agent skills repositories. Generates a SHA256-verified lock file that tracks every skill with its version, file hash, depen
- **tool-selection-stack** — Build the right GTM tool stack for any stage — solo founder ($100/mo), small team ($500/mo), growth team ($2K/mo), and enterprise ($10K+/mo). With cost breakdowns, tool comparisons
- **waterfall-enrichment** — Design multi-provider enrichment waterfalls — provider ordering by cost-per-hit, 3 separate waterfalls for company, email, and phone data, always verify after finding. Use when bui

### content-seo (6)
- **aeo-strategy** — Answer Engine Optimization — optimize content for AI search engines (ChatGPT, Perplexity, Gemini, Claude). Triggers on: "AEO", "answer engine optimization", "AI search", "generativ
- **citation-harvesting** — Systematically build backlinks through citations, mentions, and digital PR — HARO, source-blogger outreach, data-driven PR. Triggers on: "citation harvesting", "backlink building",
- **faq-seo** — Build FAQ pages that capture featured snippets and People Also Ask traffic — question-driven content strategy. Triggers on: "FAQ SEO", "featured snippet", "People Also Ask", "quest
- **pillar-pages** — Design and build pillar pages with topic clusters — comprehensive hub pages that rank for high-intent keywords. Triggers on: "pillar page", "topic cluster", "hub page", "cornerston
- **pseo-strategy** — Programmatic SEO — build scalable, template-driven content pages for long-tail keywords. Triggers on: "pSEO", "programmatic SEO", "scalable SEO", "template SEO", "mass content gene
- **seo-strategy** — B2B SEO strategy — keyword research, content architecture, technical SEO, link building, measurement. Triggers on: "SEO strategy", "search engine optimization", "B2B SEO", "keyword

### creative (12)
- **ad-creative-strategy** — Develop ad creative strategy for B2B campaigns — creative formats per platform, testing methodology, creative fatigue management, UGC/AI-generated creative, and performance measure
- **ai-content-creation** — AI-powered content creation workflows — step-by-step processes for using Claude, ChatGPT, Jasper, Copy.ai, Writesonic, and Perplexity to generate, edit, and optimize blog posts, so
- **ai-video-creation** — AI-powered video creation for marketing — step-by-step workflows for HeyGen (AI spokespersons), Synthesia (AI avatars), Runway (generative video), Captions (AI editing), Opus Clip
- **content-distribution** — Distribute content across channels for maximum reach — multi-platform repurposing, syndication, paid amplification, email distribution, and partner promotion. Use when getting cont
- **copywriting** — Write marketing copy that converts — landing pages, ads, emails, social, headlines, and brand voice. Use when writing any marketing or sales copy beyond cold email. Triggers on: "c
- **graphic-design-gtm** — Create GTM visual assets — social graphics, ad creatives, pitch deck design, one-pager layouts, email images, data visualization, and brand-consistent templates. Use when creating
- **growth-hacking-tactics** — Tactical growth hacking playbook — rapid experimentation, growth loops, viral mechanics, referral flywheels, PLG hacks, content-led growth loops, community-driven growth, and low-c
- **landing-page-copy** — Landing page copywriting strategy — conversion copy frameworks, hero headline patterns, value proposition formulas, CTA copy, social proof placement, objection handling in copy, an
- **social-media-strategy** — Build and execute social media strategy for B2B — LinkedIn, X/Twitter, posting cadence, engagement tactics, content formats, sizing guides, and platform-specific best practices. Us
- **v0-lander** — Step-by-step guide to building GTM landing pages with v0 by Vercel — the AI generative UI platform. Covers prompt engineering for v0, iterating on generated UI, exporting to Next.j
- **vibe-coding** — AI-powered development for GTM — vibe coding workflows using v0, Cursor, Claude Code, Lovable, Bolt.new, Replit Agent, and Tempo Labs for rapidly building landing pages, marketing
- **vibe-marketing** — AI-powered marketing at scale — vibe marketing workflows for rapid content generation, creative iteration, campaign launches, and growth experiments using ChatGPT, Claude, Midjourn

### customer-success (7)
- **cs-analytics-dashboards** — Build customer success analytics dashboards — NPS, CSAT, CES, customer health scores, churn prediction models, expansion propensity, support volume trends, and CS team performance.
- **cs-playbooks** — Build customer success playbooks — onboarding, health scoring, CSQLs, expansion plays, QBRs, and churn intervention. Use when building a CS function, designing customer journeys, o
- **customer-onboarding** — Design structured customer onboarding programs — time-to-value optimization, activation milestones, kickoff calls, 30-60-90 day plans, handoff from sales to CS, onboarding playbook
- **headless-support** — Design and deploy headless / automated support systems — AI chatbots, Fin AI agents, knowledge base self-serve portals, ticket deflection strategies, automated triage, email auto-r
- **qbr-planning** — Plan and execute Quarterly Business Reviews — value documentation, ROI presentation, executive alignment, and expansion roadmap. Use when preparing for QBRs, business reviews with
- **sla-management** — Design and manage customer support SLAs — service level agreements, ticket priority matrices, first response time targets, resolution time targets, escalation paths, business hours
- **support-tool-stack** — Customer support platform selection, setup, and optimization — Intercom, Zendesk, Front, Help Scout, HubSpot Service Hub, Linear, and AI-native tools. Use when choosing a support p

### demand-gen (4)
- **content-syndication** — Syndicate content across paid and organic channels — content atomization, sponsored placement, newsletter sponsorships, distribution strategy. Triggers on: "content syndication", "
- **paid-social-strategy** — B2B paid social strategy — LinkedIn, Meta, TikTok ad platform strategy, audience building, creative testing, budget allocation. Triggers on: "paid social", "LinkedIn ads", "social
- **podcast-gtm** — Use podcast appearances as a GTM channel — booking strategy, interview prep, content repurposing, pipeline conversion. Triggers on: "podcast GTM", "podcast appearances", "be a podc
- **webinar-strategy** — Plan and execute demand gen webinars — topic selection, speaker sourcing, promotion cadence, follow-up sequences. Triggers on: "webinar", "webinar strategy", "virtual event", "dema

### design (7)
- **battlecard-builder** — Create competitive battlecards — FIA Framework (Fact → Impact → Act), Why We Win/Why We Lose, objection handling cards per competitor, pricing comparisons, and quick-dismiss summar
- **case-study-builder** — Create customer case studies in sales-ready format — Challenge→Solution→Results structure, before/after metrics, quote integration, two-length formats (1-page summary + full versio
- **design-system-gtm** — Define brand-context for AI agents — visual identity systems, voice/tone guides, color palettes with hex/RGB/HSL, typography systems with font stacks and type scales, logo usage ru
- **one-pager-builder** — Create one-page sales documents — product overviews, meeting leave-behinds, champion enablement sheets, trade show handouts. Scannable in 30 seconds, memorable enough to forward. U
- **pitch-deck-builder** — Build investor-ready pitch decks and sales presentations — 10-11 slide structure, persona-customized per role, storytelling frameworks, speaker notes, and visual direction. Use whe
- **roi-calculator** — Build ROI calculators and business cases — 3-scenario projections (conservative, moderate, aggressive), payback period analysis, TCO comparison, assumption documentation, MEDDICC i
- **ui-ux-gtm** — Design GTM UI/UX patterns — landing pages (hero, proof, CTA), forms (progressive disclosure, inline validation), signup flows (activation, time-to-value), dashboards (KPI hierarchy

### events (3)
- **conference-strategy** — Strategic conference planning — event selection, sponsorship ROI, speaking submissions, booth strategy, team preparation. Triggers on: "conference strategy", "event planning", "tra
- **event-driven-outreach** — Outbound sequences triggered by conference/event attendance — pre-event research, on-site plays, post-event follow-up. Triggers on: "event outreach", "conference prospecting", "tra
- **field-marketing** — Plan and execute field marketing — regional events, executive dinners, roadshows, customer advisory boards. Triggers on: "field marketing", "executive dinner", "roadshow", "regiona

### foundation (8)
- **buyer-psychology** — Apply decision science and buyer psychology to GTM — transparency effect (4.2-4.5), Cialdini principles, prediction over persuasion, trust mechanics. Use when designing messaging,
- **competitive-intel** — Competitive Intel playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for competitive intel work, implementation
- **gtm-context** — Gtm Context playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for gtm context work, implementation help, or an
- **icp-scoring** — Icp Scoring playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for icp scoring work, implementation help, or an
- **icp-targeting-tiers** — Define ICP differences across small business, mid-market, and enterprise — buying process, deal size, sales motion, tool stack, messaging by tier. Use when segmenting GTM by compan
- **positioning-messaging** — Positioning Messaging playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for positioning messaging work, implem
- **pricing-strategy** — Pricing Strategy playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for pricing strategy work, implementation h
- **using-gtm-skills** — Complete guide to using the gtm-skills repository — installation, skill discovery, skill loading, combining skills, taxonomy navigation, CLI workflows, and advanced patterns for ev

### founder-led (37)
- **advisor-recruitment** — Strategic advisor recruitment for B2B SaaS founders. Use when building advisory board, recruiting individual advisors, structuring advisor compensation (equity grants), defining ad
- **board-meeting-prep** — Board meeting preparation for B2B SaaS founders. Use when preparing quarterly board meetings, building board decks, selecting metrics to present, crafting narrative, managing board
- **brand-kit** — Build a complete brand kit for B2B SaaS — logo design and usage, color palette, typography, voice and tone, visual identity, brand guidelines, and asset templates. Use when creatin
- **building-saas** — Build a SaaS company from idea to scale — product development, architecture decisions, pricing, hiring sequence, fundraising stages, and operational infrastructure. Use when starti
- **business-insurance** — Complete business insurance guide for SaaS founders — Errors & Omissions (E&O/Tech E&O), Cyber Liability, Directors & Officers (D&O), General Liability, Workers Compensation, Key P
- **co-founder-dynamics** — Complete co-founder playbook for technical founders — finding co-founders, equity splits (dynamic and static), co-founder agreements, vesting schedules, working relationships, conf
- **content-led-growth** — Content-led growth strategy for B2B SaaS founders. Use when building a founder-led content engine, designing content as a GTM channel, scaling content production, measuring content
- **data-privacy-compliance** — Data privacy compliance for B2B SaaS — GDPR, CCPA/CPRA, ePrivacy Directive, cookie consent, Data Processing Agreements (DPAs), Standard Contractual Clauses (SCCs), Data Protection
- **employment-compliance** — Employment law and compliance for B2B SaaS founders — contractor vs employee classification, offer letters, IP assignment (PIIA), at-will employment, equity documentation, employee
- **engineer-to-founder** — Engineer To Founder playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for engineer to founder work, implementa
- **equity-management** — Complete equity management for SaaS founders — cap tables, 409A valuations, option pools (ISO vs NSO vs RSU), 83(b) elections, equity grants for employees/advisors/contractors, dil
- **events-planning** — Plan and execute B2B events — conferences, webinars, dinners, happy hours, trade shows, and owned events. Use when planning any business event to generate pipeline or build communi
- **exiting-company** — Prepare a SaaS company for acquisition or exit — valuation drivers, due diligence readiness, financial preparation, legal structuring, and exit timeline. Use when planning an exit,
- **financial-modeling** — SaaS financial modeling for founders — operating model, runway, headcount, DCF valuation, consumption-based pricing models, cohort analysis, unit economics by segment, ARR bridge/b
- **first-hires-playbook** — Complete playbook for founder's first 10 hires beyond sales. Use when hiring first engineer, first CS, first marketer, first product manager, or building founding team. Covers when
- **founder-brand** — Build a founder personal brand — LinkedIn strategy, content cadence, podcast guesting, newsletter growth, media features, and community building. Use when building personal brand,
- **founder-sales** — Founder-led sales playbook for $0-5M ARR stages. Use when founder is primary seller, building sales process from scratch, transitioning from founder-led to AE-led, or designing dem
- **fundraising-strategy** — Complete fundraising strategy for B2B SaaS founders. Use when preparing to raise seed/Series A, deciding VC vs bootstrapped path, building pitch deck, running a fundraise process,
- **hiring-agencies** — Evaluate, hire, and manage agencies for SaaS GTM — outbound agencies, dev shops, marketing agencies, and design studios. When to use an agency vs hiring in-house, how to structure
- **hiring-by-role** — Role-specific hiring guides for B2B SaaS — interview questions, evaluation criteria, scorecards, and assessment methods for engineering, sales, marketing, customer success, product
- **hiring-contractors** — Hire and manage contractors for SaaS startups — where to find them, how to structure engagements, IP assignment, rates by role, and management practices that produce quality work w
- **investor-updates** — Write investor updates that build confidence and surface help — monthly format, board deck structure, fundraising narrative, and metrics dashboards. Use when writing investor updat
- **job-posting-strategy** — Complete job posting and distribution strategy for B2B SaaS companies — where to post by role (engineering, sales, marketing, CS, product, design), job board comparison, posting te
- **launch-planning** — Launch Planning playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for launch planning work, implementation hel
- **lead-magnets** — Lead Magnets playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for lead magnets work, implementation help, or
- **legal-for-founders** — Complete legal playbook for SaaS founders — incorporation (Delaware C-Corp vs LLC), IP assignment, Terms of Service, Privacy Policy, NDAs, consulting agreements, co-founder IP, fun
- **partner-programs** — Partner Programs playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for partner programs work, implementation h
- **pricing-psychology** — SaaS pricing psychology and tactics for B2B founders. Use when designing pricing tiers, testing price points, building pricing pages, handling discounting strategy, adding new pric
- **saas-metrics-calculator** — Saas Metrics Calculator playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for saas metrics calculator work, im
- **sales-team-building** — Build a B2B sales team from first hire to scale — hiring sequence by ARR stage, WbD POD structures, compensation models (linear/accelerated/split), draw mechanics, REKS coaching, a
- **security-assessments** — Security assessment and vendor risk management for B2B SaaS — penetration testing, vulnerability scanning, bug bounty programs, security questionnaires (VSAQ/SIG/CAIQ), incident re
- **soc2-compliance** — Achieve SOC2 Type II compliance for SaaS companies — readiness assessment, control implementation, auditor selection, evidence collection, and ongoing monitoring. Use when preparin
- **solo-founder-gtm** — Build lean GTM as a solo founder or bootstrapper — tool stacks by revenue stage, AI agents replacing headcount, when to make the first hire, bootstrapper economics, and the WbD GTM
- **startup-communities** — Startup Communities playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for startup communities work, implementa
- **vc-outreach** — Vc Outreach playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for vc outreach work, implementation help, or an
- **vendor-contracts** — Vendor contracts, MSAs, DPAs, and procurement for B2B SaaS — master service agreements, service level agreements, data processing agreements, order forms, vendor security assessmen
- **yc-ecosystem** — Yc Ecosystem playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for yc ecosystem work, implementation help, or

### growth (4)
- **churn-prevention** — Build churn prevention systems — early warning signal detection, customer health scoring, re-engagement campaigns, risk tier routing, and champion departure monitoring. Use when re
- **customer-marketing** — Customer marketing and advocacy programs — case studies, testimonials, customer reference programs, NPS-driven advocacy, customer communities, user conferences, champion programs,
- **expansion-selling** — Complete expansion and upsell playbook for B2B SaaS — consumption-based upsell triggers, cross-sell identification, seat expansion, tier upgrades, NRR growth strategies, land-and-e
- **referral-programs** — Design customer and partner referral programs — 3-tier comp structure, referral tracking, platform integration, double-sided rewards, viral mechanics, referral leaderboards, and me

### gtm-ops (3)
- **campaign-governance** — Establish campaign governance — naming conventions, UTM parameters, campaign hierarchy, ROI measurement, budget tracking. Triggers on: "campaign governance", "UTM strategy", "campa
- **gtm-operations** — Build GTM operations function — tech stack architecture, process design, data governance, RevOps foundations. Triggers on: "GTM ops", "RevOps", "revenue operations", "sales ops", "
- **revops-tech-stack** — Design the RevOps technology stack — CRM, enrichment, sequencing, analytics, integration architecture. Triggers on: "RevOps stack", "sales tech stack", "GTM tool audit", "revenue t

### inbound (4)
- **content-marketing** — Build content marketing strategies that generate pipeline — SEO/AEO optimization, pillar page design, programmatic SEO, content-to-pipeline mapping. Use when the user wants to plan
- **inbound-triage** — Design inbound lead triage workflows — demo form qualification, MQL to SQL routing, automated enrichment on form fill, speed-to-lead SLAs. Use when the user wants to handle inbound
- **landing-pages** — Audit and optimize landing pages for conversion — hero/offer/proof/CTA patterns, CRO audits, A/B testing, signup flow optimization. Use when the user wants to improve conversion ra
- **social-selling** — Build a LinkedIn social selling strategy — Sales Navigator, DM sequences, content-to-conversation, profile optimization, and SSI scoring. Use when the user wants to sell on LinkedI

### leadmagic (6)
- **leadmagic-bulk-enrichment** — Process CSV files with LeadMagic at scale — input cleanup, batch sizing, validation status handling, webhook callbacks, CRM export, error recovery, and quality checks. Use when enr
- **leadmagic-cli** — Use the LeadMagic CLI for enrichment automation — find emails, validate contacts, enrich CSVs in batch, find decision-makers by role, and push to outbound platforms (Smartlead, Ins
- **leadmagic-integrations** — Integrate LeadMagic with GTM platforms — Clay, Apollo, Smartlead, Instantly, Salesforce, HubSpot, Zapier, Make. Bi-directional data flows, webhook enrichment, CRM automation, and v
- **leadmagic-job-change** — Use LeadMagic job-change signals for pipeline intelligence — champion tracking, account risk alerts, new-role outreach, replacement mapping, and CRM routing. Use when monitoring ca
- **leadmagic-mcp** — Set up LeadMagic MCP for AI agents — tool discovery, permission scope, safe enrichment workflows, batch usage, verification steps, and agent handoff patterns. Use when connecting L
- **leadmagic-waterfall** — Build Clay enrichment waterfalls with LeadMagic as the primary provider — 95%+ email coverage, multi-provider chaining, verification integration, catch-all resolution. Use when set

### lifecycle (5)
- **churn-prediction** — Build churn prediction models — leading indicators, risk scoring, early warning systems, intervention playbooks. Triggers on: "churn prediction", "predict churn", "churn model", "e
- **lifecycle-drips** — Design lifecycle drip campaigns — post-purchase, renewal, expansion, milestone-based automated email programs. Triggers on: "lifecycle drips", "automated campaigns", "lifecycle ema
- **mql-nurture** — Build MQL nurture programs — lead scoring, nurture tracks, email drip sequences, MQL→SQL conversion. Triggers on: "MQL nurture", "lead nurture", "nurture tracks", "MQL to SQL", "le
- **onboarding-sequences** — Design customer onboarding sequences — time-to-first-value, activation milestones, guided setup, onboarding emails. Triggers on: "onboarding sequence", "customer onboarding", "time
- **re-engagement** — Design re-engagement campaigns for dormant leads and inactive customers — win-back sequences, reactivation offers, sunset policies. Triggers on: "re-engagement", "win-back", "react

### management-leadership (2)
- **sales-coaching** — Coach sales reps for consistent performance — REKS framework, deal reviews, call coaching, pipeline inspection, and 1:1 cadences. Use when setting up sales coaching, training manag
- **team-management** — Team management for startup leaders — 1:1s, performance reviews, goal setting (OKRs), delegation, feedback culture, remote team management, team rituals, and scaling from IC to man

### outbound (9)
- **cold-calling** — Build and execute B2B cold calling programs — phone intent scoring, precision dialing, the Buckets methodology, multi-touch cadences, and conversation-to-meeting conversion. Use wh
- **cold-email-copywriting** — Writes high-converting cold email copy using the 3-line framework, proven subject line patterns, and persona-specific variants. Use when the user asks to write, improve, or critiqu
- **cold-email-strategy** — Designs high-performing cold email sequence architecture with proper cadence timing, channel mixing, and trigger-based logic. Use when the user asks to build, audit, or optimize a
- **domain-infrastructure** — Designs and provisions the domain and mailbox infrastructure for cold email outreach: secondary domains, mailbox setup (Google Workspace, M365, Zoho), DNS authentication records, i
- **email-deliverability** — Sets up and monitors email deliverability infrastructure including SPF, DKIM, DMARC configuration, warmup strategy, reputation monitoring, bounce and complaint handling, and ongoin
- **inbox-setup** — Set up cold email inbox infrastructure from scratch — Google Workspace, Microsoft 365, and Azure/Entra inbox provisioning, DNS authentication, domain buying, warmup, and cost optim
- **multi-channel-outreach** — Design and execute multi-channel outbound sequences across email, LinkedIn, cold calls, and SMS. Use when the user wants to coordinate outreach across channels, build multi-touch s
- **reply-handling** — Classifies and automates responses to cold email replies using an 8-category taxonomy, auto-reply playbooks, and human escalation rules. Use when the user asks to set up reply hand
- **sending-platforms** — Compares, selects, and configures cold email sending platforms: Smartlead, Instantly, Salesforge, Apollo, and others. Use when the user asks which sending platform to use, needs to

### partnerships (3)
- **co-marketing** — Execute co-marketing campaigns with partners — joint webinars, co-branded content, shared audiences, mutual promotion. Triggers on: "co-marketing", "joint marketing", "partner mark
- **integration-partnerships** — Build and go-to-market with technology integration partnerships — API/integration GTM, marketplace listing, co-selling. Triggers on: "integration partnership", "tech partnership",
- **partnership-strategy** — Build a partnership program — partner types, recruitment, enablement, co-marketing, revenue share models. Triggers on: "partnership strategy", "partner program", "channel partnersh

### product-led-growth (2)
- **freemium-optimization** — Freemium and free trial conversion optimization — activation flow design, paywall placement, upgrade triggers, PQL scoring, time-to-value reduction, and freemium monetization model
- **plg-strategy** — Design product-led growth motions — freemium vs free trial, PQL scoring, self-serve conversion, PLG sales hybrid, and product-led marketing. Use when building a PLG motion, transit

### prospecting (7)
- **contact-verification** — Verify email addresses before they enter outbound sequences to prevent bounces and protect sender reputation. Use when the user wants to validate emails, check deliverability, veri
- **data-enrichment-strategy** — Design an end-to-end B2B data enrichment architecture — provider selection, waterfall design, cost modeling, and CRM hygiene. Use when the user wants to evaluate enrichment provide
- **email-finding** — Find verified work email addresses for B2B contacts using multi-provider waterfall discovery. Use when the user wants to find emails, look up contact information, discover email pa
- **lead-enrichment** — Lead Enrichment playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for lead enrichment work, implementation hel
- **lead-finding** — Lead Finding playbook for GTM agents — strategy, workflow, templates, operating guidance, and quality checks. Use when the user asks for lead finding work, implementation help, or
- **list-building** — Build qualified B2B prospect lists using Clay, LinkedIn Sales Navigator, and multi-source discovery. Use when the user wants to build a prospect list, create a target account list,
- **signal-scoring** — Score and prioritize prospects using buying signals — hiring, funding, tech stack changes, executive moves, and intent data. Use when the user wants to score leads, prioritize outr

### sales-plays (5)
- **earnings-signal-play** — Outbound play triggered by public company earnings calls — strategic priority mining, new-initiative alignment, urgency creation. Triggers on: "earnings signal", "earnings play", "
- **funding-signal-play** — Trigger-based outbound play when a target account raises funding — urgency messaging, use-of-funds alignment, 7-14 day window. Triggers on: "funding signal", "funding play", "raise
- **hiring-signal-play** — Outbound play triggered by specific hiring signals — VP Sales, RevOps, SDR manager, CRO postings signal budget and strategy shift. Triggers on: "hiring signal", "job post outbound"
- **job-change-play** — Outbound play triggered by contact job changes — champion tracking, new-role outreach, "new broom" timing. Triggers on: "job change", "new role", "champion moved", "job change outr
- **product-launch-play** — Outbound play triggered by competitor product launches or target account product launches — timing-based urgency, competitive positioning. Triggers on: "product launch play", "comp

### sales-revops (7)
- **deal-desk** — Structure deals, pricing, and proposals — pricing model selection, discount guidance, business case construction, and negotiation strategy. Use when structuring a deal, building a
- **demo-scripts** — Write compelling demo scripts — first demo, technical deep-dive, and executive overview. Scene-by-scene with timing, talk tracks, and interaction points. Use when building demo scr
- **meeting-prep** — Prepare comprehensive meeting briefs — account research, attendee profiles, SPIN/MEDDIC discovery questions, competitive context. Use when preparing for a sales call, discovery mee
- **objection-handling** — Build comprehensive objection handling playbooks — 6-category taxonomy, AER framework, battlecards per competitor, pre-handling in outreach. Use when creating objection responses,
- **pipeline-management** — Manage B2B sales pipelines with structured deal stages, forecasting, CRM hygiene, and deal inspection cadences. Use when setting up pipeline processes, improving forecast accuracy,
- **sales-enablement** — Create sales collateral that reps actually use — pitch decks, one-pagers, battlecards, objection docs, demo scripts, talk tracks, and playbooks. Use when the user wants to create s
- **transparency-selling** — Execute Todd Caponi's Transparency Sale methodology — lead with flaws, build the "Our Flaws" slide, negotiate with radical honesty, use the 4.2-4.5 effect in positioning. Use when

### sequencing-tools (6)
- **hubspot-sequences** — Design and optimize HubSpot sequences — enrollment triggers, multi-channel steps, task creation, analytics, A/B testing. Triggers on: "HubSpot sequences", "HubSpot automation", "Hu
- **instantly-sequences** — Set up Instantly — unlimited accounts, warmup pool, campaign optimization, unified inbox. Triggers on: "Instantly", "Instantly setup", "Instantly campaigns", "Instantly warmup".
- **lemlist-setup** — Set up and optimize Lemlist — personalized images/videos, multi-channel sequences, warm-up, deliverability. Triggers on: "Lemlist", "Lemlist setup", "Lemlist campaigns", "personali
- **outreach-sequences** — Design and manage Outreach sequences — multi-channel cadences, triggers, analytics, team workflows. Triggers on: "Outreach sequences", "Outreach cadence", "Outreach setup", "Outrea
- **salesloft-cadences** — Build and optimize Salesloft cadences — Rhythm, Conversations, multi-channel orchestration, analytics. Triggers on: "Salesloft", "Salesloft cadence", "Rhythm", "Salesloft automatio
- **smartlead-workflows** — Set up and run Smartlead — unlimited mailboxes, auto-rotation, A/B testing, master inbox, AI categorization. Triggers on: "Smartlead", "Smartlead setup", "Smartlead campaigns", "un

### tools (7)
- **analytics-toolkit** — Complete analytics tools toolkit — Segment CDP, Amplitude, Mixpanel, PostHog, GA4, and HubSpot analytics configuration. Covers implementation patterns, destination routing, event g
- **clay-toolkit** — Complete Clay platform toolkit — table architecture, waterfall enrichment, Claygent AI agent, credit optimization, CRM push, webhook webhooks, formula writing, and advanced Clay wo
- **crm-toolkit** — Complete CRM operations toolkit — HubSpot, Salesforce, and Attio deep-dive configuration, enrichment integration, pipeline automation, and data hygiene. Use when building CRM workf
- **leadmagic-toolkit** — Complete LeadMagic platform toolkit — API reference, CLI workflows, MCP server setup, enrichment waterfalls, bulk processing, job change detection, and integration patterns. Use wh
- **n8n-toolkit** — Complete n8n automation toolkit for GTM — workflow design patterns, webhook-to-enrichment-to-CRM pipelines, HTTP Request nodes for API integration, error handling, and production d
- **sequencing-toolkit** — Complete outreach sequencing toolkit — Smartlead, Instantly, Salesloft, Outreach, Lemlist setup and optimization. Covers mailbox rotation, warmup, A/B testing, deliverability monit
- **support-toolkit** — Complete customer support tools toolkit — Intercom, Zendesk, Front, Help Scout deep-dive configuration, AI agent setup, knowledge base optimization, and support analytics. Use when


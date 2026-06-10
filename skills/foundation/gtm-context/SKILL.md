---
name: gtm-context
description: >-
  Capture reusable GTM context for every other skill: product, ICP, personas, pains, proof, competitors, pricing, channels, constraints, and source-of-truth files. Use when starting a project, onboarding an agent to a company, or fixing generic outputs caused by missing context.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: foundation
  tags: [gtm, context, icp, strategy, planning, foundation]
  related_skills: [icp-scoring, positioning-messaging, pricing-strategy, competitive-intel]
  frameworks: [Maja Voje GTM Strategist, Moore Beachhead, Winning by Design Bowtie, Force Management MEDDICC]
---
# GTM Context

## Overview

The single biggest mistake GTM teams make is launching tactics without first establishing a shared, documented understanding of who they sell to, how they sell, and what they're optimizing for. Disconnected context produces misaligned messaging, wasted prospecting effort, pricing that doesn't match willingness-to-pay, and competitive positioning that misses the actual battlefield. This skill prevents that fragmentation.

GTM Context is the foundational skill in the GTM Skills library. It captures your company's identity, Ideal Customer Profile, go-to-market motion, technology stack, channel mix, and core metrics into a single reusable document. Every downstream skill — from ICP scoring to cold email copywriting to competitive intel — references this context as its source of truth. Without it, downstream skills operate on assumptions that decay into misalignment within weeks.

This skill produces three deliverables: a comprehensive GTM Context document covering all dimensions of your go-to-market operation, an OPE (Objectives-Process-Execution) canvas for strategic alignment, and a 90-day action plan mapping tactics to the context. The process draws from Maja Voje's GTM Strategist methodology (phases 1-3: strategy, positioning, execution readiness) and Geoffrey Moore's beachhead market selection framework.

## When to Use

- User says "define our GTM strategy" or "set up GTM context" → activate this skill
- User describes their company and asks "where should we start" → use this skill
- User mentions "I need a 90-day plan" or "go-to-market plan" → this skill provides the foundation
- User asks "who is our ICP" or "what is our GTM motion" and no context document exists → run this first
- Any downstream skill detects missing context → prompt user to run gtm-context first
- User is onboarding a new GTM hire who needs full situational awareness

Do NOT use for:
- Situations where a gtm-context.md already exists and is current — instead update it directly
- Narrow questions about a single dimension (e.g., "what's our pricing" when context exists) — consult the existing context
- Rapid experiments where a lightweight hypothesis document suffices

## Authoritative Foundations

This skill draws from the following established methodologies:

- **Maja Voje — GTM Strategist Phases 1-3.** Phase 1 (Strategy) defines ICP, beachhead, and competitive landscape. Phase 2 (Positioning) crafts messaging and differentiation. Phase 3 (Execution Readiness) maps channels, metrics, and operational plan. This skill covers the output of all three phases in one document.
  
- **Geoffrey Moore — Crossing the Chasm Beachhead Methodology.** The concept of selecting a narrow, winnable beachhead segment before expanding. Applied here to ensure the ICP definition is specific enough to be actionable rather than aspirational.

- **Winning by Design — Bowtie Model.** Revenue visualization extending beyond the funnel through retention and expansion. Used here to ensure the context captures the full customer lifecycle, not just acquisition.

- **Winning by Design — GTM Index.** Six-model scoring framework (Revenue, Data, Math, Operating, Growth, GTM) that provides a structured diagnostic. Applied during intake to assess where the organization currently stands.

- **Force Management — MEDDICC.** Enterprise qualification framework (Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion). Used here to ensure the context captures buying committee dynamics and the economic justification for purchase.

- **Steve Blank — Customer Development.** The four-step framework (Customer Discovery, Customer Validation, Customer Creation, Company Building). Applied during the beachhead validation phase to ensure the ICP is grounded in real customer conversations.

## Prerequisites

- **Upstream skills:** None. This is the entry point for the entire GTM Skills library.
- **Required inputs from user:** Company name, product description, target market description, existing customer data (at minimum: 3-5 best customers with revenue, industry, size, and why they bought).
- **Optional:** Existing pitch deck, website URL, CRM export of current customers, any prior ICP documentation, competitor names.
- **Optional tools:** LeadMagic Company Search API can help validate and enrich company data during the ICP research phase, but the skill works entirely without it.

## Step-by-Step Process

### Phase 1: Intake

Gather all required information from the user. Ask these questions as a single block — do not proceed until you have answers to at least the first seven:

1. What is your company name, founding year, and current stage (pre-seed, seed, Series A, etc.)?
2. Describe your product in one sentence. What problem does it solve?
3. Who are your 3-5 best customers today? For each: company name, industry, employee count, approximate revenue, how they found you, and the primary reason they bought.
4. What is your current go-to-market motion? (Product-led growth, sales-led, marketing-led, channel/partner-led, community-led, or hybrid — describe the mix.)
5. What is your primary revenue model? (Subscription SaaS, usage-based, marketplace, services, hybrid.)
6. What is your current ARR range? (<$100K, $100K-$1M, $1M-$5M, $5M-$20M, $20M+)
7. Who are your top 3-5 competitors? (Direct, indirect, and status quo/DIY alternatives.)
8. What channels drive your pipeline today? (Inbound, outbound, partnerships, events, community, paid.)
9. What is your current tech stack for GTM? (CRM, marketing automation, sales engagement, enrichment tools.)
10. What are your top 3 GTM metrics you track religiously?

### Phase 2: Research

Once intake is complete, conduct structured research to fill gaps:

**Customer Pattern Analysis:** Examine the 3-5 best customers for commonalities. Look for patterns in industry, company size, geography, tech stack, buying trigger, job title of champion, and sales cycle length. These patterns form the empirical foundation of the ICP definition.

**Competitive Landscape Mapping:** For each competitor named, research their positioning, pricing (if public), target market, and key differentiators. Use their website, G2/Capterra reviews, and recent press. Categorize competitors into three tiers: direct (solve the same problem the same way), indirect (solve the same problem differently), and status quo (manual/DIY/do-nothing).

**Market Sizing:** Estimate TAM (Total Addressable Market), SAM (Serviceable Addressable Market), and SOM (Serviceable Obtainable Market) using bottom-up analysis based on the ICP definition. Use industry reports, LinkedIn Sales Navigator company counts, and public market data. Be transparent about assumptions.

**GTM Index Assessment:** Score the organization on Winning by Design's six models:
- Revenue Model (1-10): How clearly defined are revenue streams and pricing?
- Data Model (1-10): How well instrumented is the GTM stack with data?
- Math Model (1-10): How well understood are unit economics?
- Operating Model (1-10): How defined are GTM processes and handoffs?
- Growth Model (1-10): How clear is the growth strategy?
- GTM Model (1-10): How aligned is the overall GTM engine?

### Phase 3: Execution

Produce three core deliverables:

**1. GTM Context Document (gtm-context.md)**

This is the master document. Structure it with these sections:

- **Company Identity:** Name, founding year, stage, mission statement, product description in one sentence.
- **Product Overview:** Core product, key features, primary use case, integration ecosystem, pricing model summary.
- **ICP Definition:** Industry verticals, company size (employees and revenue), geography, technographic profile, behavioral characteristics, buying triggers, negative personas (who not to sell to).
- **Beachhead Segment:** The narrowest viable ICP slice for initial focus, with rationale for selection.
- **GTM Motion:** Description of primary motion (PLG, sales-led, etc.) with supporting motions, channel mix with approximate contribution percentages.
- **Buying Committee:** Typical roles involved (per Force Management MEDDICC), decision process, average deal size, typical sales cycle length.
- **Tech Stack:** CRM, marketing automation, sales engagement, enrichment, analytics, and other GTM tools in use.
- **Channel Mix:** Inbound (content, SEO, social), outbound (cold email, LinkedIn, cold calling), partnerships, events, community, paid acquisition — with estimated contribution to pipeline.
- **Core Metrics:** ARR, MRR, customer count, average ACV, NRR, logo churn, CAC payback, LTV:CAC, pipeline coverage ratio, win rate — with current values where known and targets where aspirational.
- **Competitive Landscape:** Direct, indirect, and status quo competitors with brief positioning notes.
- **Key Challenges:** Top 3-5 GTM challenges identified during intake and research.

**2. OPE Canvas**

A one-page strategic alignment canvas:
- **Objectives:** Top 3-5 measurable GTM objectives for the next 90 days.
- **Process:** The core workflows and systems needed to achieve each objective.
- **Execution:** Specific tactics, owners, and milestones for each process.

**3. 90-Day Plan**

A week-by-week or phase-by-phase tactical plan:
- **Phase 1 (Days 1-30):** Foundation building — complete context, validate ICP, set up tracking.
- **Phase 2 (Days 31-60):** Experimentation — test channels, iterate on messaging, build pipeline.
- **Phase 3 (Days 61-90):** Scaling — double down on what works, optimize underperforming areas, establish predictable pipeline.

Each phase includes: objective, key results, specific tactics, owner (if known), and success criteria.

### Phase 4: Delivery

Present the deliverables in this order:

1. Executive summary (3-5 paragraphs covering the most important findings)
2. OPE Canvas (visual-friendly format)
3. GTM Context Document (full detail)
4. 90-Day Plan (actionable timeline)
5. Appendices (market sizing calculations, GTM Index scores, research methodology notes)

Ask the user: "Does this context accurately reflect your GTM reality? What would you adjust?" Context is living documentation — expect iteration.

## Output Format

The agent should produce output in this structure:

```markdown
# GTM Context: [Company Name]

## Executive Summary
[3-5 paragraphs synthesizing the most critical findings across all dimensions]

---

## OPE Canvas

### Objectives (Next 90 Days)
1. [Specific, measurable objective]
2. [Specific, measurable objective]
3. [Specific, measurable objective]

### Process
For each objective, the core workflows and systems required.

### Execution
For each process, specific tactics, owners, and milestones.

---

## GTM Context Document

### Company Identity
[Company name, founding year, stage, mission, product description]

### Product Overview
[Core product, key features, primary use case, integrations, pricing model]

### Ideal Customer Profile
[Industry, company size, geography, technographics, behaviors, buying triggers, negative personas]

### Beachhead Segment
[The narrowest viable ICP slice and rationale]

### GTM Motion
[Primary motion description, supporting motions, channel contribution percentages]

### Buying Committee
[Typical roles, decision process, deal size, sales cycle]

### Tech Stack
[CRM, marketing automation, sales engagement, enrichment, analytics, other GTM tools]

### Channel Mix
[Inbound, outbound, partnerships, events, community, paid — with pipeline contribution estimates]

### Core Metrics
[Metric: Current → Target — for ARR, MRR, customers, ACV, NRR, churn, CAC payback, LTV:CAC, pipeline coverage, win rate]

### Competitive Landscape
[Direct, indirect, status quo competitors with positioning notes]

### Key Challenges
[Top 3-5 GTM challenges]

---

## 90-Day Plan

### Phase 1: Foundation (Days 1-30)
- Objective:
- Key Results:
- Tactics:
- Success Criteria:

### Phase 2: Experimentation (Days 31-60)
- Objective:
- Key Results:
- Tactics:
- Success Criteria:

### Phase 3: Scaling (Days 61-90)
- Objective:
- Key Results:
- Tactics:
- Success Criteria:

---

## Appendices
- Market Sizing Calculations (TAM/SAM/SOM)
- GTM Index Scores (6-model assessment)
- Research Methodology Notes
```

## Quality Check

Before delivering, verify:

- [ ] Is the ICP specific enough to say "no" to a prospect who doesn't fit?
- [ ] Does the beachhead segment represent a winnable market, not just the total market?
- [ ] Are competitive categorizations accurate (direct vs indirect vs status quo)?
- [ ] Do the metrics include both current values AND targets?
- [ ] Is the 90-day plan actionable with specific owners and success criteria?
- [ ] Would a new GTM hire understand the full picture from this document alone?
- [ ] Are negative personas clearly defined to prevent wasted effort?
- [ ] Is the GTM motion description specific enough to guide channel investment decisions?
- [ ] Does the channel mix include estimated contribution percentages?
- [ ] Are all assumptions explicitly stated rather than presented as facts?

## Common Pitfalls

1. **ICP is too broad.** "Mid-market SaaS companies" is not an ICP — it's a TAM. An ICP specifies industry, size band, tech stack, buying trigger, and geography. If your ICP definition doesn't exclude at least 80% of companies, it's not specific enough. Use Moore's beachhead principle: what is the narrowest segment where you can dominate?

2. **Confusing stated ICP with actual ICP.** Founders often describe who they want to sell to rather than who actually buys. Always ground the ICP in empirical customer data, not aspiration. If your 3-5 best customers are all 50-person fintech companies, your ICP is 50-person fintech companies regardless of what the pitch deck says.

3. **Skipping negative personas.** Defining who NOT to sell to is as important as defining who to sell to. Without explicit negative personas, SDRs waste cycles on companies that will never convert, AEs take meetings that will never close, and marketing generates leads that sales rejects. Document at least three negative persona profiles.

4. **GTM motion is described as a buzzword without specifics.** "We're PLG with sales assist" is insufficient. Describe the actual customer journey: how does someone discover you? What is the first product experience? When does a human get involved? What triggers the handoff? Be precise about the mechanics.

5. **Metrics section lists targets without current baselines.** A target without a baseline is a wish. Every metric should show Current → Target with a timeframe. If you don't know the current value, mark it as "Unknown — needs instrumentation" rather than omitting it.

6. **Competitive analysis is only direct competitors.** The biggest competitor in B2B SaaS is almost always "status quo" — the prospect continuing to do things the way they currently do. If your competitive landscape doesn't include status quo/DIY/manual alternatives, you're missing the competitor that wins most deals.

7. **The 90-day plan tries to do everything at once.** A common failure mode is listing 20 tactics across 5 channels for Phase 1. The 90-day plan should have at most 3-5 objectives total and focus each phase on the highest-leverage activities. Sequencing matters more than comprehensiveness.

8. **Context is treated as a one-time deliverable rather than living documentation.** GTM context decays. ICPs shift. Competitors enter. Channels saturate. The context document should include a "Last Updated" date and a review cadence (recommended: quarterly). Without this, the document loses trust and teams stop referencing it.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **icp-scoring**: Run after this skill. Takes the ICP definition from gtm-context and builds a weighted, multi-dimensional scoring model with firmographic, technographic, behavioral, and intent dimensions.

- **positioning-messaging**: Run after this skill. Consumes the ICP definition, competitive landscape, and product overview to produce April Dunford positioning, Andy Raskin strategic narrative, and a persona-based messaging matrix.

- **pricing-strategy**: Run after this skill. Uses the ICP, buying committee, and competitive landscape to recommend pricing models, tier structures, and willingness-to-pay calibration.

- **competitive-intel**: Run after this skill. Deepens the competitive landscape into full battlecards, win/loss analysis, and tech stack teardowns using the competitor list established here.

- **gtm-metrics**: Run after this skill. Builds on the metrics baseline to create dashboards, diagnostic frameworks, and GTM Index tracking using the metrics captured here.

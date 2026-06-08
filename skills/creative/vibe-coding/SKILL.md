---
name: vibe-coding
description: >-
  AI-powered development for GTM — vibe coding workflows using v0, Cursor,
  Claude Code, Lovable, Bolt.new, Replit Agent, and Tempo Labs for rapidly
  building landing pages, marketing sites, tools, dashboards, and prototypes.
  Based on Andrej Karpathy's "vibe coding" philosophy. Use when building GTM
  assets with AI, shipping marketing sites fast, or teaching non-technical
  team members to build with AI. Triggers on: "vibe coding", "AI dev tools",
  "build with AI", "v0 by Vercel", "Lovable", "Bolt", "Cursor AI".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: creative
  tags: [vibe-coding, ai-development, v0, cursor, claude-code, lovable, bolt, replit, karpathy, building-with-ai]
  related_skills: [vibe-marketing, v0-lander, ai-content-creation, claude-design, landing-pages, design-system-gtm, popular-web-designs]
  frameworks:
    - "Andrej Karpathy — Vibe Coding (2025): 'fully give in to the vibes, embrace exponentials, forget the code exists'"
    - "Pieter Levels (@levelsio) — AI-assisted solo building, 12 startups in 12 months"
    - "Sahil Lavingia (Gumroad) — AI-first design and development"
    - "Marc Lou (@marc_lou) — AI-shipping machine, 20+ products"
    - "Guillermo Rauch (Vercel) — v0: generative UI for the next billion developers"
---

# Vibe Coding for GTM

## Overview

"Vibe coding" — coined by Andrej Karpathy in 2025 — is a new paradigm where
you build software by describing what you want to an AI, iterating
conversationally, and shipping without deep-diving into the underlying code.
It is not "no-code." It is "AI-code." You speak. The AI writes. You review.
You ship. For GTM teams, vibe coding means marketing sites, landing pages,
interactive tools, dashboards, and prototypes can be built by marketers and
founders — not just engineers. This skill covers the vibe coding workflow
across 6 platforms, ranked by GTM utility.

## When to Use

Trigger phrases: "vibe coding", "build with v0", "AI landing page", "Cursor
for marketing site", "Lovable app", "Bolt build", "Replit Agent", "AI dev
tool", "build without coding", "Claude Code for GTM", "AI website builder"

## Authoritative Foundations

### Andrej Karpathy — Vibe Coding (Feb 2025)
"There's a new kind of coding I call 'vibe coding,' where you fully give in
to the vibes, embrace exponentials, and forget that the code even exists.
It's possible because the LLMs are getting so good. I just talk to Composer
with SuperWhisper so I barely touch the keyboard. I ask for the dumbest
things like 'decrease the padding on the sidebar by half' because I'm too
lazy to find it. I 'Accept All' always, I don't read the diffs anymore."

**The vibe coding philosophy in 4 principles:**
1. **Describe, don't write.** You provide intent. AI provides implementation.
2. **Iterate at conversation speed.** "Make it darker." "Add a CTA." "Change
   the font." Each takes 5 seconds, not 5 minutes.
3. **Accept and review later.** Ship fast. Fix what breaks. Don't obsess over
   code quality — obsess over user outcomes.
4. **The code is disposable.** If the AI can regenerate a page in 30 seconds,
   you don't need to understand every line. You need to understand if the
   OUTPUT works.

### Pieter Levels (@levelsio) — AI-Assisted Solo Building
Levels builds $100K+/mo products solo using AI tools. His principle: "The AI
writes 80% of the code. I guide it, review the output, and fix the edge cases.
What used to take weeks now takes hours. What used to take a team of 5 now
takes me and an API key."

### Marc Lou (@marc_lou) — AI Shipping Machine
20+ products shipped, primarily vibe-coded. "I don't write code anymore.
I describe what I want. The AI writes it. I test it. If it works, I ship.
If it doesn't, I describe the problem and the AI fixes it."

## The Vibe Coding Stack (Ranked for GTM)

| Tool | Best For | Pricing | Skill Level | Output |
|---|---|---|---|---|
| **v0 by Vercel** | Landing pages, UI components, React apps | Free-$20/mo | Zero code | Production React/Next.js |
| **Lovable** | Full-stack apps, tools, SaaS MVPs | Free-$20/mo | Zero code | Full-stack apps with backend |
| **Bolt.new** | Rapid prototyping, full apps | Free-$20/mo | Zero code | Full-stack apps |
| **Cursor + Claude** | Codebase-level changes, complex features | $20/mo | Some code | Any codebase |
| **Claude Code** | Terminal-based, agentic development | API usage | Technical | Full codebases |
| **Replit Agent** | Quick tools, internal dashboards | $25/mo | Minimal code | Hosted apps |
| **Tempo Labs** | React UI components, design-to-code | Free-$15/mo | Zero code | React components |

## Platform Deep-Dives

### v0 by Vercel (Best for GTM Landing Pages)

**What it is:** Generative UI platform. Describe a page in natural language.
v0 generates React/Next.js/Tailwind code. You iterate conversationally.
Export to your codebase or deploy on Vercel.

**GTM use cases:**
- Landing pages (launch in hours, not weeks)
- Pricing pages (iterate tiers visually in minutes)
- Component libraries (generate on-brand UI components)
- Waitlist pages (ship a waitlist in 30 minutes)
- Marketing microsites (event sites, campaign pages)

**Workflow:**
1. **Describe:** "Build a dark-themed SaaS landing page with a hero section,
   pricing table with 3 tiers, customer logos, and a CTA footer."
2. **Iterate:** "Make the primary color #0066FF. Switch to Inter font. Add
   a testimonial section with 3 quote cards."
3. **Polish:** "Add hover animations to the pricing cards. Make the CTA
   buttons pulse on scroll. Add a mobile hamburger menu."
4. **Export:** Copy the code or `npx shadcn add` the components.

**Pro tips:**
- Reference existing pages: "Make it look like Stripe's pricing page but
  for a cold email tool."
- Upload a design system image for brand consistency
- Use v0's "Fork" feature to create variants (A/B test landing pages)
- Chain prompts: build header first, then hero, then sections

### Lovable (Best for Full-Stack GTM Tools)

**What it is:** Full-stack app builder. Describe an app. Lovable generates
frontend + backend + database. Deploy with one click. Best for tools,
calculators, dashboards — not just static pages.

**GTM use cases:**
- ROI calculators (interactive tools for lead gen)
- Internal dashboards (pipeline tracking, metrics)
- Customer portals (onboarding checklists, health scores)
- Interactive demos (let prospects try before buying)
- GTM micro-tools (email score grader, ICP checker)

**Workflow:**
1. **Describe the app:** "Build an ROI calculator for a cold email tool.
   Users input: monthly emails sent, current reply rate, average deal size.
   Output: projected revenue increase with our tool."
2. **Connect data:** Lovable connects to Supabase (database) and APIs
3. **Iterate:** "Add a PDF export button. Add a comparison table showing
   current vs projected. Add customer testimonials below the calculator."
4. **Deploy:** One-click deploy. Custom domain in settings.

### Bolt.new (Best for Rapid Prototyping)

**What it is:** Browser-based full-stack app builder. Similar to Lovable but
faster iteration cycles. Best for "show me something in 60 seconds."

**GTM use cases:**
- MVP prototypes (validate an idea in an afternoon)
- Client demos (custom build for a prospect call)
- Internal tools (quick dashboards, data viewers)
- Hackathon projects (build + ship in 48 hours)

**Workflow:**
1. **Prompt:** "Build a waitlist page with email collection, referral
   tracking, and an admin dashboard showing signups per day."
2. **Stack:** Bolt generates the full stack (React, Node, database)
3. **Iterate:** Chat-based refinement. "Add social share buttons with
   referral links. Add a leaderboard showing top referrers."
4. **Deploy:** One-click deploy to Netlify or similar.

### Cursor + Claude (Best for Complex GTM Codebases)

**What it is:** AI-native IDE. Claude/GPT integrated into your editor.
Full codebase awareness. Best for developers who want AI acceleration,
not replacement.

**GTM use cases:**
- Automating GTM workflows (scripts, APIs, integrations)
- Building data pipelines (enrichment, scoring, routing)
- Custom integrations (CRM ↔ outreach ↔ analytics)
- Complex landing pages with dynamic content

**Workflow:**
1. **Open your GTM codebase in Cursor**
2. **Cmd+K:** "Build a landing page component that pulls customer logos
   from a JSON file and displays them in a responsive grid."
3. **Cmd+L (chat):** "Now add a modal that opens when you click a logo,
   showing the customer's case study."
4. **Composer (Cmd+I):** Agentic mode. "Build the entire pricing page
   with 3 tiers, FAQ accordion, and enterprise contact form."
5. **Review diffs, accept, ship.**

### Claude Code (Best for Agentic Development)

**What it is:** Anthropic's terminal-based coding agent. Full autonomy.
Can read/write files, run commands, search codebases, and deploy.

**Claude Code for GTM artifacts:**
```
claude "Build a dark-themed SaaS landing page using Tailwind CSS.
        Include: hero with CTA, 3-tier pricing, customer logos,
        3 testimonials, FAQ accordion, and a footer. Use Inter font.
        Primary color: #0066FF. Deploy to Vercel."
```

Claude Code will:
1. Create the project structure
2. Install dependencies
3. Build the landing page
4. Run it locally for testing
5. Deploy when you confirm

### Replit Agent (Best for Quick Internal Tools)

**What it is:** Replit's AI agent. Describe an app in natural language.
Replit builds, hosts, and deploys it. Good for quick internal tools.

**GTM use case examples:**
- "Build a lead scoring dashboard that pulls from a Google Sheet"
- "Build a campaign ROI calculator for our sales team"
- "Build a meeting prep tool that generates account briefs"

## The Vibe Coding Workflow (Universal)

### Step 1: Define the Artifact (5 min)
- What are you building? (landing page, calculator, dashboard, tool)
- Who is it for? (prospects, customers, internal team)
- What's the one action they should take?

### Step 2: Describe in Natural Language (5 min)
Write a detailed prompt. Include:
- Layout structure (header, hero, sections, footer)
- Visual style (dark/light, color palette, typography)
- Specific elements (CTA buttons, forms, tables, cards)
- Reference sites ("looks like Stripe's pricing page")

### Step 3: Generate (1 min)
Paste into v0 / Lovable / Bolt / Cursor / Claude Code.

### Step 4: Iterate (15-30 min)
- "Change the hero headline to be more benefit-focused"
- "Swap the order of sections 2 and 3"
- "Add hover animations to the CTA buttons"
- "Make it mobile-responsive — stack sections vertically on mobile"
- "Replace the placeholder images with our product screenshots"

### Step 5: Polish (15 min)
- Copy: write real copy, not lorem ipsum
- Images: add real screenshots, logos, photos
- Links: connect CTAs to actual URLs
- Forms: connect to your email/CRM (ConvertKit, HubSpot, etc.)

### Step 6: Ship (5 min)
- Deploy (Vercel, Netlify, or platform's built-in deploy)
- Add custom domain
- Add analytics (Plausible, PostHog, Google Analytics)
- Test on mobile, tablet, desktop

### Step 7: Iterate with Data (ongoing)
- Track conversions
- A/B test variations (built fast with AI)
- Replace what doesn't convert

## What AI Dev Tools CAN Do for GTM in 2025

- Full landing pages in under 1 hour
- Interactive calculators and tools in under 4 hours
- Complete SaaS MVPs in under a week
- Marketing microsites in under 3 hours
- Dashboard prototypes in under 2 hours
- Email templates (HTML) in under 30 minutes
- A/B test variants in under 15 minutes each

## What AI Dev Tools CAN'T Do (Yet)

- Complex backend logic with edge cases
- Production-grade security and auth
- Performance optimization for scale
- Deep integrations with proprietary APIs
- GDPR/HIPAA/SOC2 compliance logic
- Custom animations beyond basic CSS
- Maintain a codebase over months without human oversight

**The rule:** Use vibe coding for the presentation layer. Use real engineering
for the critical path. Your landing page can be vibe-coded. Your payment
processing cannot.

## Output Format

```
VIBE CODING ARTIFACT PLAN

Artifact: [landing page / calculator / tool / dashboard]
Platform: [v0 / Lovable / Bolt / Cursor / Claude Code / Replit]
Audience: [ICP]
Success Metric: [conversion rate / signups / demos]

Prompt v1:
[Detailed natural language description]

Iteration Log:
1. Generated v1 — [what worked, what didn't]
2. ["Change X"] — [result]
3. ["Add Y"] — [result]
...

Deploy:
- URL: [deployed URL]
- Analytics: [connected]
- Next iteration: [date / trigger]
```

## Implementation Checklist

- [ ] Artifact solves one specific GTM need (don't vibe-code a monolith)
- [ ] Prompt includes: layout, style, specific elements, reference (if any)
- [ ] Real copy, real images — no lorem ipsum, no placeholder photos
- [ ] Mobile-responsive (test on phone before shipping)
- [ ] CTAs connected to actual URLs/forms/calendars
- [ ] Analytics connected before launch
- [ ] SEO basics: title tag, meta description, H1, alt text on images
- [ ] Page speed check: under 3s load on mobile (Lighthouse)

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Vibe-coding the product itself.** Your core SaaS product needs real
   engineering. Vibe code the marketing site, not the payment processing.
   Fix: Marketing surfaces = vibe code. Product core = real code.

2. **Accepting all AI output without review.** "Accept All" is Karpathy's
   bit — and it works when you can test the output. But for customer-facing
   pages, test every button, every link, every form. Fix: 5-minute QA
   checklist before every deploy.

3. **One-shot prompting.** "Build a SaaS website" in one prompt produces
   generic slop. Fix: Build section by section. Hero first. Iterate. Then
   pricing. Iterate. One section at a time produces much better output.

4. **No design system reference.** AI generates generic Tailwind if you don't
   give it design constraints. Fix: Provide brand colors, font, and a
   reference site. "Look like Stripe but with #0066FF primary."

5. **Forgetting mobile.** AI tools often generate desktop-first layouts that
   break on mobile. Fix: As a final prompt: "Make this fully responsive.
   Stack all sections vertically on mobile. Ensure touch targets are 44px+."

## Expert Voices to Follow

| Expert | Platform | What They Teach |
|---|---|---|
| **Andrej Karpathy** | @karpathy (X) | Vibe coding philosophy, AI development |
| **Pieter Levels** | @levelsio (X) | Solo building with AI, $100K+/mo products |
| **Sahil Lavingia** | @shl (X) | Gumroad, AI-first product building |
| **Marc Lou** | @marc_lou (X) | AI shipping machine, 20+ products |
| **Guillermo Rauch** | @rauchg (X) | v0, Vercel, generative UI |
| **Riley Brown** | @rileybrown_ai (X) | AI coding tutorials, Cursor workflows |
| **Mckay Wrigley** | @mckaywrigley (X) | AI coding, Claude Code workflows |
| **Sully Omarr** | @SullyOmarr (X) | Lovable, Bolt, AI app building |

## Related Skills

- `vibe-marketing` — AI-powered marketing content at scale
- `v0-lander` — v0 by Vercel step-by-step for GTM pages
- `ai-content-creation` — AI workflows for blog, social, email
- `claude-design` — Design process for HTML artifacts
- `landing-pages` — CRO audits, conversion optimization
- `design-system-gtm` — Brand tokens for AI generation
- `popular-web-designs` — 54 brand design systems as visual vocabulary
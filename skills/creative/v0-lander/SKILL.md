---
name: v0-lander
description: >-
  Step-by-step guide to building GTM landing pages with v0 by Vercel — the AI
  generative UI platform. Covers prompt engineering for v0, iterating on
  generated UI, exporting to Next.js, deploying on Vercel, and connecting
  forms/analytics. Use when building a landing page, pricing page, waitlist
  page, event page, or marketing microsite with v0. Triggers on: "v0",
  "v0 by Vercel", "v0 landing page", "build landing page with AI", "v0
  pricing page", "v0 tutorial".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: creative
  tags: [v0, vercel, landing-page, ai-ui, generative-ui, react, nextjs, tailwind]
  related_skills: [vibe-coding, vibe-marketing, landing-pages, design-system-gtm, popular-web-designs, claude-design, ui-ux-gtm]
  frameworks:
    - "v0 by Vercel — Generative UI platform (Guillermo Rauch)"
    - "shadcn/ui — Component library powering v0"
    - "Tailwind CSS — Utility-first CSS framework"
    - "Next.js — React framework for production"
---

# v0 Landing Page Builder

## Overview

v0 by Vercel is the fastest way to build a production-quality landing page.
You describe the page in natural language. v0 generates React/Next.js/Tailwind
code. You iterate conversationally. You export and deploy. What used to take
a designer + developer 1-2 weeks now takes a founder or marketer 2-4 hours.
This skill is a step-by-step playbook for building every type of GTM landing
page with v0.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **v0 by Vercel — Generative UI platform (Guillermo Rauch).** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **shadcn/ui — Component library powering v0.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Tailwind CSS — Utility-first CSS framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Next.js — React framework for production.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use

Trigger phrases: "build a landing page with v0", "v0 tutorial", "v0 landing
page prompt", "v0 by Vercel for marketing", "AI landing page builder",
"generate landing page with v0", "v0 pricing page", "v0 waitlist"

## v0 Basics

**What it is:** v0.dev — Vercel's generative UI platform. You type. It
generates React components using shadcn/ui + Tailwind CSS. You can:
- Generate full pages from a single prompt
- Iterate on specific sections ("change the hero headline")
- Generate individual components ("a testimonial card with avatar")
- Export code to your Next.js project
- Deploy directly to Vercel

**Pricing:** Free tier (200 generations/month). Pro ($20/mo) for unlimited.

## Step-by-Step Process

### Phase 1: Preparation (Before You Open v0)

**Define 5 things before your first prompt:**

1. **The page type:** Landing page, pricing page, waitlist page, event page,
   feature announcement, or microsite?
2. **The audience:** Who are they? What matters to them?
3. **The action:** What ONE thing do you want them to do? (Start trial,
   book demo, join waitlist, buy now)
4. **The brand:** Colors (primary/secondary/neutrals), font (Inter is safe),
   tone (professional, playful, technical, premium)
5. **The reference:** What existing site should this feel like? "Clean like
   Stripe" or "Technical like Vercel" or "Bold like Linear"

**Brand context document (paste into your first v0 prompt):**
```
BRAND CONTEXT:
- Company: [name]
- Product: [one-liner]
- Primary color: #0066FF
- Secondary: #FF6600
- Font: Inter
- Tone: Direct, data-backed, confident
- Reference: Stripe (clean, minimal) + Linear (dark, technical)
- NO: gradients, emojis, stock photos, generic SaaS tropes
```

### Phase 2: Generate the Page (Prompt Engineering)

**The master prompt template:**

```
Build a [page type] for [company/product].

Audience: [ICP]. They care about [top 3 concerns].

SECTIONS (in order):
1. Nav: [company logo left, links center, CTA right — "Start free trial"]
2. Hero: Headline [benefit-focused, under 10 words]. Subhead [one sentence
   expanding]. Primary CTA ["Start free trial"]. Secondary CTA ["See how
   it works"]. Hero image/video placeholder.
3. Social proof: 6 customer logos in a row. "Trusted by 2,000+ teams"
4. Value props: 3 columns. Each: icon, headline, one sentence. Focus on
   OUTCOMES, not features.
5. How it works: 3 steps. Each: step number, headline, one sentence.
   Visual: screenshot/GIF placeholder.
6. Features: 2-column grid. 6 features. Each: feature name + one sentence.
7. Testimonials: 3 quote cards. Each: quote (1-2 sentences), name, title,
   company, headshot placeholder.
8. Pricing (if pricing page): 3 tiers. Monthly/annual toggle. Recommended
   tier highlighted. Each tier: price, description, 5 features, CTA.
9. FAQ: 6 questions with expandable answers. Cover pricing, setup, security,
   support, cancellation, comparison.
10. Final CTA: Same as hero CTA. "Start free trial." No credit card required.
11. Footer: Logo, links, copyright, social icons.

STYLE:
- Dark theme (or light — pick one)
- Color palette: primary #0066FF, secondary #FF6600, background #0A0A0A,
  text #FFFFFF, muted #9CA3AF
- Typography: Inter, headings bold, body regular
- Spacing: generous. 80-120px between sections
- Cards: subtle borders, 8px radius, hover lift effect
- Buttons: primary (filled, white text), secondary (outlined, primary color)
- Max width: 1200px, centered

TECHNICAL:
- Mobile-responsive: stack sections vertically on mobile
- Touch targets: 44px+ on mobile
- Animations: subtle fade-in on scroll (Intersection Observer)
- No heavy animations. Respect prefers-reduced-motion.
```

**Why this prompt works:**
- It specifies every section in order (v0 builds top-to-bottom)
- It includes visual styling (colors, typography, spacing)
- It includes technical requirements (responsive, accessible)
- It gives concrete examples ("Start free trial" not "CTA here")

### Phase 3: Iterate Section by Section

**Don't fix everything in one prompt. Iterate section by section:**

```
ITERATION SEQUENCE (15-30 minutes):

1. "The hero headline is too generic. Make it specific: '[Company] helps
   [ICP] do [thing] in [timeframe]'"
2. "The value props are feature-focused. Rewrite them as outcomes:
   'Ship campaigns in 2 hours, not 2 weeks' instead of 'AI-powered
   campaign builder'"
3. "The testimonials are too long. Each quote should be 1-2 sentences max"
4. "Add a comparison table above the FAQ. 5 rows: [feature], Us, Competitor
   A, Competitor B. Checkmarks for us. Where competitors lack, use '—'"
5. "The pricing cards need hover states. Add a subtle scale(1.02) + shadow
   on hover for the recommended tier"
6. "Replace the hero image placeholder with a screenshot component.
   Dark background, rounded corners, subtle border"
7. "The CTA buttons feel small. Increase to 16px padding, 16px font"
8. "On mobile, the nav should collapse into a hamburger menu. Show me
   the mobile version"
9. "Add a sticky CTA bar that appears after scrolling past the hero.
   'Start free trial' button, white background, subtle shadow"
10. "Make the entire page responsive. Test at 375px, 768px, 1024px, 1440px"
```

### Phase 4: Generate Individual Components

**When the full page is good but one section needs more work:**

```
"Generate just the testimonial section. 3 cards in a row. Each card:
- Background: slightly lighter than page background
- Border: 1px, subtle
- Padding: 32px
- Quote at top: large, italic
- Author below: avatar (circle, 48px) + name + title + company logo
- Hover: subtle border accent, no lift"
```

v0 will regenerate just that component. Replace the existing section with
the improved version.

### Phase 5: Polish for Production

**Before deploying, iterate on:**

1. **Copy:** Replace all lorem ipsum with real copy. "v0 will generate
   placeholder text — you MUST replace it." Write real headlines, real
   value props, real testimonials.

2. **Images:** Replace placeholders with real images:
   - Hero: product screenshot (Cmd+Shift+4, upload to v0)
   - Customer logos: actual customer logos (upload)
   - Testimonial headshots: actual customer photos

3. **Links:** Connect all buttons and links:
   - "Start free trial" → signup URL
   - "Book demo" → Calendly link
   - "See pricing" → pricing section anchor
   - Footer links → actual pages

4. **Forms:** If your page has a form (waitlist, contact, demo request):
   - Connect to form backend (ConvertKit, HubSpot, Google Forms, or API)
   - Add validation (email format, required fields)
   - Add success message ("Thanks! We'll be in touch.")
   - Add error handling

5. **Analytics:** Add before deploying:
   ```jsx
   <!-- Add to head -->
   <script defer data-domain="yourdomain.com"
    src="https://plausible.io/js/script.js"></script>
   ```
   Or Google Analytics, PostHog, etc.

### Phase 6: Export and Deploy

**Option A: Deploy directly from v0 (fastest)**
1. Click "Deploy" in v0
2. Connect your Vercel account
3. Add custom domain in Vercel settings
4. Done — live in under 5 minutes

**Option B: Export to Next.js project (more control)**
1. `npx shadcn@latest add [component-url]` — adds v0 component to your
   existing Next.js project
2. Or: Copy the code manually from v0 → paste into your project
3. `git push` → Vercel auto-deploys on push

**Option C: Export as static HTML (simplest)**
1. Copy the generated HTML/CSS
2. Paste into a new file
3. Deploy to any static host (Netlify, Cloudflare Pages, GitHub Pages)

### Phase 7: Post-Launch Iteration

**After launch, iterate based on data:**

```
ANALYTICS-DRIVEN PROMPTS:

1. "The hero CTA has a 2.1% click rate. Generate 3 hero variants with
   different headlines and CTAs to A/B test"
2. "Mobile bounce rate is 68%. Audit the mobile version and fix any
   layout issues. Stack all sections vertically. Ensure touch targets 44px+"
3. "The pricing page has a 1.2% conversion rate. Generate 3 pricing page
   variants: one with annual default, one with monthly default, one with
   a 'Most Popular' badge on the middle tier"
4. "Page load time is 4.2 seconds. Optimize: lazy load below-fold images,
   remove unused CSS, defer non-critical scripts"
```

## v0 Prompts for Specific Page Types

### SaaS Landing Page
```
"Build a SaaS landing page for [product]. Dark theme. Sections: hero,
social proof (logos), 3 value props (outcomes), how it works (3 steps),
testimonials (3), pricing (3 tiers, annual default, Growth recommended),
FAQ (6), final CTA, footer. Style: clean like Stripe, dark like Linear.
Primary: #0066FF. Font: Inter."
```

### Pricing Page
```
"Build a pricing page for [product]. 3 tiers: Starter $49/mo, Growth
$199/mo (RECOMMENDED), Enterprise (Contact us). Monthly/annual toggle,
annual default. Feature comparison table below tiers. FAQ section with
8 questions. Enterprise includes a 'Book a call' CTA instead of price."
```

### Waitlist Page
```
"Build a waitlist page for [product] launching in [month]. Hero: product
name, one-line value prop, email input + 'Join waitlist' button. Below:
3 things you'll get (early access, founding pricing, priority support).
Social proof: '2,000+ on the waitlist.' Counter showing signup count."
```

### Event/Webinar Page
```
"Build a registration page for [event name] on [date]. Hero: event name,
date/time, one-line description. Below: 3 reasons to attend. Speaker
section with headshots, names, titles, talk titles. Agenda/timeline.
Registration form: name, email, company. 'Save my spot' CTA."
```

## Output Format

```
v0 LANDING PAGE BUILD — [Page Name]

v0 Project URL: [v0.dev link]
Deployed URL: [production URL]

Prompt Used:
[Master prompt text]

Iteration Log:
1. Generated v1 — [what worked, what needed change]
2. ["Change hero"] — [result]
3. ["Add testimonial section"] — [result]
...

Export Method: [Direct deploy / shadcn add / manual copy]

Post-Launch:
- Analytics: [Plausible / GA / PostHog connected]
- Conversion rate: X% (target: Y%)
- Next iteration: [date / trigger]
```

## Implementation Checklist

- [ ] Real copy — no lorem ipsum, no AI-generated placeholder text
- [ ] Real images — product screenshots, customer logos, actual headshots
- [ ] All CTAs linked to actual URLs (not "#")
- [ ] Forms connected to backend (ConvertKit, HubSpot, API)
- [ ] Mobile-responsive (tested on iPhone SE + iPhone Pro Max + iPad)
- [ ] Page load under 3 seconds (Lighthouse score 90+)
- [ ] Analytics installed and verified (check real-time dashboard)
- [ ] SEO: title tag, meta description, H1, alt text on all images
- [ ] Legal: Privacy policy link, terms link in footer
- [ ] No AI "slop" — no generic SVG illustrations, no lorem ipsum

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **One-shot prompting.** "Build a SaaS website" in one prompt = generic,
   unbranded, middle-of-the-road output. Fix: Build section by section.
   Hero first. Iterate. Then pricing. Iterate.

2. **Generic output without brand context.** Without brand colors, fonts,
   and references, v0 generates generic Tailwind. Fix: Paste your brand
   context into the first prompt. Reference a known site for style.

3. **Placeholder content shipped to production.** v0 generates "Lorem ipsum"
   and placeholder images. Shipping this live = amateur. Fix: Replace ALL
   placeholder content before deploying.

4. **Not iterating on mobile.** v0 generates desktop-first by default.
   Mobile layout often breaks. Fix: "Show me the mobile version" as a
   dedicated iteration step.

5. **No form connection.** A "Start free trial" button that links to "#"
   is a broken promise. Fix: Connect forms and CTAs before deploying.

6. **Too many sections.** v0 will happily generate 15 sections if you ask.
   More sections = more cognitive load = lower conversion. Fix: 6-8 sections
   max. Cut anything that doesn't directly support the conversion goal.

## Expert References

- **Guillermo Rauch (@rauchg)** — v0 creator, Vercel CEO. Follow for v0
  updates, prompt techniques, and generative UI philosophy.
- **v0 documentation:** v0.dev/docs — prompt guide, component library,
  export/deploy instructions
- **shadcn/ui:** ui.shadcn.com — the component library v0 generates.
  Learn it to understand what v0 is building.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- `vibe-coding` — Full AI dev tools comparison (v0, Lovable, Bolt, Cursor)
- `vibe-marketing` — AI-powered marketing content at scale
- `landing-pages` — CRO audits, conversion optimization patterns
- `design-system-gtm` — Brand tokens, CSS variables for consistent AI output
- `popular-web-designs` — 54 brand design systems as visual reference
- `ui-ux-gtm` — Landing page UX, form design, accessibility
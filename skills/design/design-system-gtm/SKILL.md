---
name: design-system-gtm
description: >-
  Define brand-context for AI agents — visual identity systems, voice/tone
  guides, color palettes with hex/RGB/HSL, typography systems with font stacks
  and type scales, logo usage rules, asset templates, and brand guardrails.
  Use when creating a design system for AI-generated GTM content, ensuring
  brand consistency across agent outputs, or implementing Google DESIGN.md
  specification. Includes Claude Code design patterns via claude-design skill.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "2.0.0"
  author: LeadMagic
  category: design
  tags: [design-system, brand, visual-identity, voice-tone, design-tokens, css-variables, claude-design]
  related_skills: [claude-design, popular-web-designs, design-system-builder, brand-kit, ui-ux-gtm, effective-ui-design]
  frameworks:
    - "Google DESIGN.md Specification"
    - "Stitch 9-Section Brand Format"
    - "Brad Frost — Atomic Design"
    - "Nathan Curtis — Design System Monorepo Architecture"
    - "Dan Mall — Design System Governance"
---

# Design System for GTM

## Overview

When AI agents generate sales collateral, pitch decks, one-pagers, social
graphics, and emails, they need a brand system to reference. Without it,
every output has different colors, different fonts, different voice — and
your brand erodes across every customer touchpoint. This skill defines a
complete AI-consumable design system with visual identity, voice/tone,
templates, and guardrails. Designed to be read by both humans and AI agents.

## Authoritative Foundations

- **Google DESIGN.md Specification** — Shapes deliverables for this skill — When AI agents generate sales collateral, pitch decks, one-pagers, social
graphics, and emails, they need a brand system.
- **Stitch 9-Section Brand Format** — Shapes deliverables for this skill — When AI agents generate sales collateral, pitch decks, one-pagers, social
graphics, and emails, they need a brand system.
- **Brad Frost — Atomic Design** — Atomic Design
- **Nathan Curtis — Design System Monorepo Architecture** — Design System Monorepo Architecture
- **Dan Mall — Design System Governance** — Design System Governance

## When to Use

Trigger phrases: "create a design system for our AI-generated content", "define
our brand for agents", "build a brand guide for sales materials", "ensure
consistent voice across AI outputs", "DESIGN.md specification", "design tokens
for agents", "AI brand system", "brand context for Claude"

## Step-by-Step Process

### Phase 1: Visual Identity System

**Color Palette — must include hex, RGB, and HSL:**

```
PRIMARY PALETTE
  Primary:        #0066FF  rgb(0,102,255)   hsl(216,100%,50%)
  Primary Dark:   #0044CC  rgb(0,68,204)    hsl(220,100%,40%)
  Primary Light:  #3388FF  rgb(51,136,255)  hsl(216,100%,60%)

SECONDARY / ACCENT
  Accent:         #FF6600  rgb(255,102,0)   hsl(24,100%,50%)

NEUTRALS
  Ink (text):     #1A1A2E  rgb(26,26,46)    hsl(240,28%,14%)
  Muted Text:     #6B7280  rgb(107,114,128) hsl(220,9%,46%)
  Surface:        #FFFFFF
  Background:     #F9FAFB
  Border:         #E5E7EB

SEMANTIC
  Success:        #10B981  rgb(16,185,129)  hsl(160,84%,39%)
  Warning:        #F59E0B  rgb(245,158,11)  hsl(37,92%,50%)
  Danger:         #EF4444  rgb(239,68,68)   hsl(0,80%,60%)
  Info:           #3B82F6  rgb(59,130,246)  hsl(217,91%,60%)
```

**CSS Variable Output (for agents generating HTML/CSS):**
```css
:root {
  --color-primary: #0066FF;
  --color-primary-dark: #0044CC;
  --color-primary-light: #3388FF;
  --color-accent: #FF6600;
  --color-ink: #1A1A2E;
  --color-muted: #6B7280;
  --color-surface: #FFFFFF;
  --color-bg: #F9FAFB;
  --color-border: #E5E7EB;
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-danger: #EF4444;
}
```

**Typography System:**

```
HEADINGS: Inter (Google Fonts)
  H1: 48px / 1.1 line-height / 700 weight / letter-spacing: -0.02em
  H2: 36px / 1.2 / 600 / -0.01em
  H3: 24px / 1.3 / 600 / 0
  H4: 20px / 1.3 / 600 / 0

BODY: Inter
  Body L: 18px / 1.6 / 400
  Body: 16px / 1.6 / 400
  Body S: 14px / 1.5 / 400
  Caption: 12px / 1.5 / 400

MONOSPACE (code, data): JetBrains Mono
  Code: 14px / 1.5 / 400

CSS:
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

**Spacing Scale (8px base):**
4, 8, 12, 16, 24, 32, 48, 64, 96, 128

**Border Radius:**
- Buttons, inputs: 8px
- Cards: 12px
- Modals: 16px

**Shadows:**
- Card: 0 1px 3px rgba(0,0,0,0.08)
- Elevated: 0 4px 12px rgba(0,0,0,0.1)
- Modal: 0 8px 32px rgba(0,0,0,0.12)

### Phase 2: Voice and Tone Guide

**Brand Voice Attributes (5 — be specific, not vague):**
1. **Direct** — no hedging, no "we believe," no "it could be argued." Say the thing.
2. **Data-backed** — every claim has a number or source. "Most teams" → "73% of teams."
3. **Opinionated** — take positions. "We recommend X, not Y" not "There are several approaches."
4. **Concrete** — "47% reply rate" not "industry-leading engagement."
5. **Confident but not arrogant** — "Here's what works" not "We're revolutionizing."

**Tone by Context:**
| Context | Tone | Example |
|---|---|---|
| Sales deck | Confident, data-heavy | "Teams using our platform see 47% reply rates within 30 days." |
| Case study | Narrative, specific | "Acme Corp was losing $2.3M/year to churn. Here's how they fixed it." |
| Email nurture | Helpful, low-pressure | "I noticed you downloaded our ROI calculator. Here are 3 ways customers use it." |
| Error messages | Clear, apologetic, helpful | "That didn't work. Here's why and how to fix it." |
| Social media | Punchy, shareable | "Stop guessing your ICP. Start scoring it." |

**Banned Words and Phrases:**
- "Revolutionary," "high-impact," "disruptive" (vague, overused)
- "Best-in-class," "industry-leading" (meaningless without data)
- "Synergize," "leverage" (as a verb), "holistic" (jargon)
- "We're excited to announce" (nobody cares if you're excited)
- Passive voice: "Results were achieved" → "We achieved results"

**Preferred Language Patterns:**
- Active voice always. "We built" not "It was built."
- Present tense. "The platform processes" not "The platform will process."
- Short sentences. Under 25 words when possible.
- Bullets over paragraphs in decks and one-pagers.

### Phase 3: Asset Templates

**Slide Master Template:**
- 16:9 aspect ratio
- Header: Inter 36px, primary color, left-aligned
- Body: Inter 18px, ink color
- Footer: company logo (bottom-right), slide number (bottom-left), 12px muted
- Data slides: charts in primary + accent palette, no decorative elements

**One-Pager Template:**
- A4/US Letter
- Header: logo + product name
- Hero: value prop (H2), one-line description, hero image
- Body: 3-column feature grid
- Social proof: 3 customer logos + 1 testimonial
- CTA: prominent button/contact info
- Footer: company info, legal

**Email Signature:**
```
[First Name] [Last Name]
[Title] | [Company Name]
[Phone] | [Website]
[Calendly link]
[Company logo — 80px wide]
```

**Data Visualization Style:**
- Primary + neutral palette (limit to 5 data colors)
- No 3D charts, no pie charts (use bar/line/scatter)
- Direct labels (no legends when possible)
- Source line: "Source: [name], [date]" in 10px muted

### Phase 4: Brand Guardrails

**Always Acceptable (AI can generate without review):**
- Social graphics using brand colors, typography, and voice
- Email copy following tone guidelines
- Blog post drafts (human reviews before publishing)
- Data visualizations in brand style
- Landing page sections following template

**Requires Human Review:**
- Customer-facing decks (check data accuracy)
- Pricing pages (legal/commercial review)
- Press releases (legal review)
- Customer quotes/testimonials (customer approval)
- Any content referencing specific customers

**Never Allowed:**
- Competitive claims without cited sources
- Revenue/growth numbers not publicly disclosed
- Customer names without explicit permission
- Guarantees or promises ("100% deliverability")
- Any content that implies endorsement by a named authority

### Integration with Claude Code Design

When using Claude Code to generate branded assets, load this skill alongside
`claude-design` and `popular-web-designs`:

```
1. claude-design → drives the design process and artifact creation
2. design-system-gtm (this skill) → provides brand tokens and rules
3. popular-web-designs → provides visual vocabulary from known brands
```

The agent should output CSS variables matching this design system's tokens
and follow the voice/tone guidelines for any copy it generates.

## Output Format

```
DESIGN SYSTEM — [Company Name]

File: DESIGN.md (version controlled in repo)

Sections:
1. Brand Overview (2-3 sentence positioning)
2. Visual Identity (colors, typography, spacing, radii, shadows)
3. CSS Variable Output (copy-paste ready)
4. Voice and Tone (attributes, per-context, banned words)
5. Asset Templates (slide, one-pager, email, social, data viz)
6. Brand Guardrails (acceptable / review / never)
7. AI Agent Usage (how agents should reference this system)
```

## Implementation Checklist

- [ ] All colors have hex, RGB, and HSL values
- [ ] CSS variable block is copy-pasteable into any project
- [ ] Typography includes Google Fonts import URL and font stack
- [ ] Voice attributes are specific and testable ("direct" > "professional")
- [ ] Banned words list exists (10+ entries)
- [ ] Tone guide covers at least 5 contexts
- [ ] Asset templates include specific dimensions and specs
- [ ] Guardrails have 3 clear tiers (always acceptable / review / never)
- [ ] AI agent usage instructions included (how to reference, what to load)
- [ ] File is version-controlled and linked from README

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Vague voice guidelines.** "Professional and friendly" is useless. Agents
   need specific, testable attributes: "Short sentences. Active voice.
   No passive constructions. Data before adjectives." Fix: For each voice
   attribute, provide 3 examples of "this, not that."

2. **RGB without hex.** AI agents reference hex codes for HTML/CSS generation.
   Including RGB is good. Including only RGB is not. Fix: Hex is the primary
   color format for agents. RGB and HSL are supplementary.

3. **No CSS variable output.** Agents generating HTML need copy-pasteable CSS.
   Wading through a color palette table to extract hex codes produces errors.
   Fix: Include a `:root {}` CSS block with all design tokens.

4. **Ignoring dark mode.** Many agent-generated artifacts (dashboards,
   presentations) look different in dark mode. Fix: Include dark mode color
   variants or document that the brand is light-mode-only.

5. **No guardrails.** Without explicit rules, agents will improvise — and
   sometimes generate content that's off-brand, legally risky, or factually
   wrong. Fix: Clear tiered guardrails: acceptable, review, never.

6. **Design system as PDF.** If your design system is a Figma file or PDF,
   AI agents can't read it. Fix: DESIGN.md in markdown, version controlled,
   linked from all agent configuration files.

## Execution Artifacts

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections
This skill includes lightweight artifacts the agent can load on demand:
Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- `claude-design` — Design process for one-off HTML artifacts
- `popular-web-designs` — 54 known-brand design systems for visual vocabulary
- `design-system-builder` — Build complete design systems from references
- `brand-kit` — Logo design, color palette, typography, asset templates
- `ui-ux-gtm` — Landing pages, forms, signup flows, dashboards
- `effective-ui-design` — Professional UI design guidelines

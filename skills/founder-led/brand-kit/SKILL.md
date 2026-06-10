---
name: brand-kit
description: >-
  Build a complete brand kit for B2B SaaS — logo design and usage, color palette,
  typography, voice and tone, visual identity, brand guidelines, and asset
  templates. Use when creating a brand from scratch, rebranding, or building
  consistent visual identity. Triggers on: "brand kit", "brand identity", "logo
  design", "brand guidelines", "visual identity", "brand book", "rebrand",
  "brand colors", or any brand-building request.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: founder-led
  tags: [brand, design, logo, identity, visual, guidelines]
  frameworks: [Marty Neumeier Brand Gap, David Aaker Brand Identity, April Dunford Positioning]
  related_skills: [design-system-gtm, graphic-design-gtm, pitch-deck-builder, ui-ux-gtm]
---

# Brand Kit

## Overview

A brand kit is the operating manual for your company's visual and verbal
identity. It's what makes your website, sales deck, social posts, and product
feel like they came from the same company. Without one, every asset is a
one-off design decision that degrades into inconsistency.

This skill builds a complete brand kit: logo, colors, typography, voice,
and asset templates that anyone on the team can use to produce on-brand
materials.

## Authoritative Foundations

- **Marty Neumeier Brand Gap** — Shapes deliverables for this skill — A brand kit is the operating manual for your company's visual and verbal
identity.
- **David Aaker Brand Identity** — Shapes deliverables for this skill — A brand kit is the operating manual for your company's visual and verbal
identity.
- **April Dunford Positioning** — Positioning — competitive alternatives, differentiated value, target segment.

## When to Use

- "Create a brand kit"
- "Design a logo and brand identity"
- "Pick brand colors and fonts"
- "Build brand guidelines"
- "Rebrand our company"
- "Create a style guide"
- "Design a consistent visual identity"

## Step-by-Step Process

### Phase 1: Logo Design

**Logo types:**
- **Primary logo:** Full name + icon. Horizontal lockup. Used on website, decks.
- **Icon/mark:** Icon only. Square format. Used for favicon, social avatars, app icon.
- **Wordmark:** Name only, no icon. Used where icon would be redundant.

**Logo specifications:**
- File formats: SVG (vector, primary), PNG (raster, for non-vector uses), ICO (favicon).
- Color variants: full color, white (for dark backgrounds), single color (for
  monochrome applications).
- Clear space: minimum padding around logo equal to the height of the icon.
- Minimum size: never smaller than 24px in digital, 0.5" in print.

**Hiring a logo designer:**
- Budget: $500-2,000 for a quality logo from a freelance designer (Upwork, Dribbble).
- $5,000-15,000 for a brand identity from a design studio.
- Deliverables: logo in all variants + brand guidelines doc.
- AI-assisted: Midjourney/DALL-E for concept exploration, then designer refines.

### Phase 2: Color Palette

**Structure:** Primary (1-2 colors), Secondary (2-3 colors), Neutral (3-5 shades),
Accent (1-2 colors for CTAs, highlights).

**Primary color:** The color people associate with your brand. Use for logo,
headlines, primary buttons. Choose 1-2 max.

**Secondary colors:** Support the primary. Use for backgrounds, sections,
illustrations. 2-3 colors from adjacent palette positions.

**Neutrals:** Grays, off-whites, dark tones. Body text, backgrounds, borders.
3-5 shades from pure white through pure black.

**Accent:** High-contrast color for CTAs, notifications, highlights. Should
pop against all other palette colors. 1-2 colors.

**Every color needs:** Name (e.g., "Ocean Blue"), hex code (#1A73E8), RGB
(26, 115, 232), CMYK (for print), and usage guidance.

### Phase 3: Typography

**Heading font:** 1 font, 2-3 weights (bold, semibold, regular). Used for
H1-H4, hero text, card titles. Should have personality but be readable.

**Body font:** 1 font, 2-3 weights. Used for paragraphs, UI text, captions.
Must be highly readable at 14-16px. Often a system font or neutral sans-serif.

**Monospace font:** For code, data, technical content. 1 font.

**Font sourcing:** Google Fonts (free, self-host for performance), Adobe Fonts
(included with Creative Cloud), commercial licenses (for unique fonts).

**Type scale:** Define sizes for H1-H6, body, small, caption. Example:
H1: 48px, H2: 36px, H3: 28px, H4: 22px, Body: 16px, Small: 14px, Caption: 12px.

### Phase 4: Voice and Tone

**Brand voice attributes (3-5 adjectives):** "Direct, data-backed, opinionated,
approachable." Not "professional" — every brand claims professional.

**Voice guidelines:**
- **Do:** Use contractions. Write like you talk. Lead with data. Be specific.
- **Don't:** Use jargon ("leverage," "synergy," "best-in-class"). Write passive
  voice. Make claims without evidence.
- **Banned words:** Leverage, synergy, circle back, best-in-class, innovative,
  high-impact, disruptive, advanced. If it would sound ridiculous spoken
  aloud at a dinner table, don't write it.

**Tone by context:**
- Sales deck: Confident, specific, outcome-focused.
- Blog post: Insightful, generous, data-rich.
- Social media: Conversational, punchy, opinionated.
- Customer email: Helpful, clear, warm.
- Error message: Clear, actionable, human. Never "An error occurred."

### Phase 5: Asset Templates

Create templates for: social post (3 variants: text-only, image, carousel),
presentation slides (title, section, content, closing), one-pager, email
signature, case study, testimonial graphic, blog featured image.

Every template locked to: brand colors, brand fonts, logo placement. Templates
enable anyone to produce on-brand assets without being a designer.

## Output Format

Brand kit document with: logo files (or specifications for creation), color
palette with hex/RGB/CMYK, typography with font sources and type scale, voice
and tone guidelines with banned words, and asset templates.

## Quality Check

- [ ] Logo in all variants (primary, icon, wordmark, color variants)
- [ ] Color palette documented with hex codes
- [ ] Typography defined with fonts and type scale
- [ ] Voice guidelines with do's, don'ts, and banned words
- [ ] Asset templates created
- [ ] All brand elements work on light AND dark backgrounds

## Common Pitfalls

1. **Logo without an icon variant.** You need a square icon for favicons,
   social avatars, and app icons. Design the icon separately.

2. **Too many colors.** More than 5 colors dilutes brand recognition. Primary
   + secondary + neutral + accent = 6-10 total. That's the limit.

3. **Voice as "professional."** Every company claims to be professional. Be
   specific: "direct, opinionated, data-backed" tells people how you actually
   sound.

4. **No banned words list.** Without explicit prohibitions, "leverage" and
   "synergy" creep into every piece of copy. Ban them explicitly.

5. **Templates that nobody uses.** If templates require a designer to operate,
   they won't be used. Build templates that a non-designer can fill in.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **design-system-gtm**: Full design system specification
- **graphic-design-gtm**: Visual asset creation
- **pitch-deck-builder**: Branded presentation templates
- **ui-ux-gtm**: Brand in digital product interfaces

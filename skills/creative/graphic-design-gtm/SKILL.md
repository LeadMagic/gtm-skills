---
name: graphic-design-gtm
description: >-
  Create GTM visual assets — social graphics, ad creatives, pitch deck design,
  one-pager layouts, email images, data visualization, and brand-consistent
  templates. Use when creating visual content for GTM, designing social media
  graphics, building ad creatives, or establishing visual identity for campaigns.
  Triggers on: "graphic design", "social graphics", "ad creative", "visual design",
  "banner design", "social image", "presentation design", "brand visuals", "data
  visualization", "infographic", or any visual asset creation request.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: creative
  tags: [design, graphics, social-media, ads, brand]
  frameworks:
    - "Cialdini Visual Persuasion"
    - "Tufte Data Visualization"
    - "Ann Handley — Everybody Writes"
---

# Graphic Design for GTM

## Overview
Visuals do 80% of the work in GTM. A well-designed graphic stops the scroll,
a poorly designed one is invisible. This skill covers GTM visual asset
creation: social graphics, ad creatives, data visualization, and brand
templates that maintain consistency across every touchpoint.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Cialdini Visual Persuasion.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Tufte Data Visualization.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Ann Handley — Everybody Writes.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Create a social media graphic"
- "Design LinkedIn carousel slides"
- "Build ad creative"
- "Create an infographic"
- "Design a data visualization"
- "Set up brand templates"
- "Make an email header image"

## Step-by-Step Process
### Phase 1: Asset Sizing Reference
| Asset | Dimensions | Format | Max Size |
|---|---|---|---|
| LinkedIn post image | 1200x627px | JPG/PNG | 8MB |
| LinkedIn carousel slide | 1080x1080px | PDF pages | 100MB |
| LinkedIn video cover | 1920x1080px | JPG | 8MB |
| X/Twitter post image | 1200x675px | JPG/PNG | 5MB |
| X/Twitter header | 1500x500px | JPG/PNG | 5MB |
| Instagram post | 1080x1080px | JPG/PNG | 8MB |
| Instagram Story | 1080x1920px | JPG/PNG | 4MB |
| Facebook ad | 1200x628px | JPG/PNG | 30MB |
| LinkedIn ad | 1200x627px | JPG/PNG | 5MB |
| Blog featured image | 1200x630px | JPG/PNG | 1MB |
| Email header | 600x200px | PNG | 1MB |
| YouTube thumbnail | 1280x720px | JPG | 2MB |

### Phase 2: Design Principles for GTM
- **Hierarchy**: most important element largest and highest contrast
- **White space**: crowded graphics are skipped. Use 30%+ white space
- **Color**: 2-3 brand colors. Social proof elements in accent color
- **Typography**: max 2 fonts. Headlines bold, body regular. No type
  below 16px for social (mobile-first)
- **CTAs**: high contrast, clear action, positioned at natural eye path

### Phase 3: High-Performance Formats
- **Text-only posts** on LinkedIn: highest reach, no design needed
- **Document carousels**: PDF uploaded as carousel, slide-by-slide narrative
- **Data visualization**: single-number stat cards, before/after comparisons,
  trend line charts, bar charts (horizontal, labeled)
- **Quote graphics**: pull quote from customer or article, clean background,
  attribution
- **Checklist/template previews**: show the value, gate the full version

### Phase 4: Brand Template System
Create templates for: social post (3 variants), carousel slide, ad creative
(per platform), case study graphic, testimonial graphic, blog header, email
header. Every template locked to brand colors, fonts, logo placement.
Templates enable anyone on the team to produce on-brand assets.

## Output Format
Design brief with asset type, dimensions, content, and brand rules. Or
template system specification with brand guidelines.


## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls
1. **Wrong dimensions** — a 1920x1080 graphic on LinkedIn stories is cropped.
   Always match platform-specific dimensions.
2. **Text in images too small** — 60%+ of social browsing is mobile. Minimum
   16px type, ideally 24px+ for headlines.
3. **Too much information** — one graphic, one message. A graphic with 5
   data points communicates zero.
4. **No brand consistency** — different colors, fonts, and styles across
   assets signals amateur. Templates enforce consistency.
5. **Stock photography** — generic stock photos reduce trust. Use product
   screenshots, team photos, or custom illustrations.

## Implementation Depth

Use this section when the user asks for a finished asset, not a high-level explanation.

### Diagnostic Questions

1. What is the primary motion: founder-led, sales-led, product-led, partner-led, or lifecycle-led?
2. Which ICP tier is the output for: small business, mid-market, enterprise, or mixed?
3. What proof is available today: customer stories, usage data, third-party validation, screenshots, or none?
4. What system will execute the work: CRM, sequencer, warehouse, support desk, product analytics, or manual workflow?
5. What decision will the user make from this output: launch, prioritize, route, rewrite, score, coach, or measure?

### Framework Application

Map the recommendation explicitly to the named frameworks in this skill:

- Cialdini Visual Persuasion: apply only the part that directly improves the requested deliverable.
- Tufte Data Visualization: apply only the part that directly improves the requested deliverable.
- Ann Handley — Everybody Writes: apply only the part that directly improves the requested deliverable.

### Deliverable Standard

A strong output from this skill includes:

- A crisp diagnosis of the current situation
- A recommended path with tradeoffs, not a generic list
- A concrete artifact the user can use immediately: table, script, checklist, scorecard, sequence, dashboard spec, or implementation plan
- A measurement plan with leading and lagging indicators
- Risks and edge cases called out before execution

### Adaptation Rules

- For small business: reduce complexity, shorten time-to-value, and prioritize owner/operator clarity.
- For mid-market: include workflow ownership, handoffs, integrations, and enablement assets.
- For enterprise: include governance, risk, procurement, stakeholder mapping, and proof requirements.


## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills
- **social-media-strategy**: Content strategy and posting cadence
- **copywriting**: Headline and body copy for graphics
- **design-system-gtm**: Full brand design system
- **pitch-deck-builder**: Presentation design

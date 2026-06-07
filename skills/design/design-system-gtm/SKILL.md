---
name: design-system-gtm
description: >-
  Define brand-context for AI agents — visual identity, voice/tone guides, color
  palettes, typography, asset templates. Use when creating a design system for
  AI-generated GTM content or ensuring brand consistency across agent outputs.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: design
  tags: [design-system, brand, visual-identity, voice-tone]
  frameworks: [Google DESIGN.md Spec, Stitch 9-Section Format]
---

# Design System for GTM

## Overview
When AI agents generate sales collateral, pitch decks, one-pagers, and emails, they need a brand system to reference. Without it, every output has a different voice, different colors, different feel. This skill defines a design system that AI agents use to produce on-brand GTM assets consistently.

## When to Use
- "Create a design system for our AI-generated content"
- "Define our brand for agents"
- "Build a brand guide for sales materials"
- "Ensure consistent voice across AI outputs"

## Step-by-Step Process
### Phase 1: Visual Identity
- Color palette (primary, secondary, accent, neutral)
- Typography (headings, body, monospace for data)
- Logo usage rules
- Spacing and layout principles

### Phase 2: Voice and Tone
- Brand voice attributes (3-5 adjectives)
- Tone guidelines by context (sales deck vs email vs case study)
- Banned words and phrases
- Preferred language patterns

### Phase 3: Asset Templates
- Slide templates
- One-pager layouts
- Email signature format
- Data visualization style

### Phase 4: Brand Guardrails
Rules for AI-generated content: what is always acceptable, what requires human review, what is never allowed.

## Output Format
DESIGN.md specification with visual identity, voice/tone, templates, and guardrails.

## Common Pitfalls
1. **Vague voice guidelines** — "professional and friendly" is useless. "Direct, data-backed, opinionated. No jargon. No passive voice." is actionable.
2. **RGB values without hex codes** — agents reference hex.
3. **No guardrails** — agents will improvise when uncertain.

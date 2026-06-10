---
name: landing-pages
description: >-
  Audit and optimize landing pages for conversion — hero/offer/proof/CTA patterns,
  CRO audits, A/B testing, signup flow optimization. Use when the user wants to
  improve conversion rates, audit a landing page, optimize a signup flow, or
  increase demo requests. Triggers on: "landing page", "conversion rate", "CRO",
  "optimize page", "signup flow", "conversion optimization", "hero section",
  "improve conversions", "A/B test landing", or any request about improving
  page conversion.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: inbound
  tags: [cro, landing-pages, conversion, optimization, ux]
  related_skills: [a-b-testing, ui-ux-gtm, content-marketing, lead-magnets]
  frameworks:
    - "Cialdini Persuasion Principles"
    - "Wiebe Conversion Copywriting"
    - "HubSpot Academy — Inbound Methodology"
---

# Landing Pages

## Overview

A landing page has one job: convert visitors into leads. Every element that
doesn't serve that goal is distraction. The best landing pages make a
single promise, prove it quickly, and make the next step frictionless.

This skill audits existing pages against conversion best practices and
produces prioritized fix lists with before/after recommendations.

## When to Use

- "Audit our landing page"
- "Why isn't our page converting?"
- "Improve our signup flow"
- "Optimize our demo request page"
- "What should we A/B test?"
- "Redesign our hero section"

## Authoritative Foundations

Robert Cialdini's seven principles of persuasion (reciprocity, commitment,
social proof, authority, liking, scarcity, unity) form the psychological
foundation of effective landing pages.

Joanna Wiebe's conversion copywriting framework: start with the prospect's
problem, not your product. Write copy that answers the question "what's in
it for me?" in the first three seconds.

## Step-by-Step Process

### Phase 1: Audit Current Page

Score the page against the CRO checklist:

**Above the fold (most critical):**
- [ ] Hero headline states value in <10 words
- [ ] Subheadline explains who it's for and what they get
- [ ] Primary CTA is visible, specific, and action-oriented
- [ ] Social proof visible (logos, testimonials, metrics)
- [ ] No navigation elements that compete with the CTA

**Body:**
- [ ] Benefits, not features. Each section answers "so what?"
- [ ] Proof points: customer logos, case study pulls, metrics
- [ ] Objections pre-handled (security, pricing, integration concerns)
- [ ] Mobile-optimized: text readable, buttons tappable, no horizontal scroll

**CTA:**
- [ ] Single primary CTA per page
- [ ] CTA copy is specific ("Get your free audit" > "Submit")
- [ ] Minimized form fields (fewer fields = higher conversion)
- [ ] Trust signals near CTA (no credit card required, SOC 2, etc.)

### Phase 2: Conversion Architecture

Structure the page for scanning, not reading:

| Section | Purpose | Content Type |
|---|---|---|
| Hero | Capture attention, state value | Headline + subheadline + CTA + social proof |
| Problem | Agitate the pain | "Without [product], teams struggle with [problem]" |
| Solution | Show how you solve it | 3-4 benefit blocks with supporting visuals |
| Proof | Build trust | Customer logos, case study metrics, testimonial pulls |
| How It Works | Reduce anxiety | Simple 3-step visual flow |
| Pricing (if applicable) | Qualify and convert | Transparent tiers or "starting at" |
| FAQ | Handle objections | 5-10 most common questions |
| Final CTA | Close | Reiterate value, single CTA, trust signals |

### Phase 3: Prioritized Fix List

Rank fixes by impact × effort:

1. **High impact, low effort**: Fix CTA copy, add social proof above fold,
   reduce form fields, fix mobile rendering
2. **High impact, high effort**: Redesign hero, add customer video, build
   ROI calculator
3. **Low impact, low effort**: Button color test, headline word test
4. **Low impact, high effort**: Full redesign, custom illustrations

## Output Format

CRO audit report:
```
# Landing Page Audit: [Page URL]

## Current Performance
- Conversion rate: X%
- Bounce rate: X%
- Mobile conversion: X%

## Audit Score: X/100

## Critical Fixes (High Impact)
1. [Fix description] — Expected impact: +X% CVR
2. ...

## A/B Test Queue
1. [Test hypothesis] — Expected lift: +X%

## Mobile-Specific Issues
1. [Issue] — Fix: [solution]
```

## Quality Check

- [ ] Hero communicates value in <3 seconds of scanning
- [ ] Single primary CTA — no competing actions
- [ ] Social proof visible above the fold
- [ ] Mobile experience tested (not just responsive, usable)
- [ ] Form fields minimized (every field costs conversion)
- [ ] Page load time under 3 seconds

## Common Pitfalls

1. **Feature list as hero.** Nobody converts because of a feature list.
   They convert because they believe you understand their problem.

2. **Multiple CTAs.** "Sign up," "Book a demo," "Learn more," "Read case
   study" — four CTAs means four decisions. One CTA per page.

3. **No social proof.** A page without customer logos or testimonials is
   asking visitors to trust a stranger. Social proof converts.

4. **Long forms.** Every additional form field reduces conversion by 5-10%.
   Start with email only. Ask for more later.

5. **Ignoring mobile.** Over 50% of B2B traffic is mobile. A page that's
   hard to use on mobile loses half its potential conversions.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **a-b-testing**: Test the changes this skill recommends
- **ui-ux-gtm**: Broader UI/UX patterns for GTM pages
- **lead-magnets**: Gated content that landing pages promote
- **content-marketing**: Content driving traffic to these pages

---
name: ui-ux-gtm
description: >-
  Design GTM UI/UX patterns — landing pages (hero, proof, CTA), forms
  (progressive disclosure, inline validation), signup flows (activation,
  time-to-value), dashboards (KPI hierarchy, trend indicators), and
  accessibility (WCAG 2.1 AA). Use when designing or auditing GTM tool
  interfaces, landing pages, conversion flows, or onboarding experiences.
  Covers conversion-first design, mobile optimization, and A/B test readiness.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "2.0.0"
  author: LeadMagic
  category: design
  tags:
    [
      ui,
      ux,
      design,
      landing-pages,
      forms,
      accessibility,
      conversion,
      dashboards,
    ]
  related_skills:
    [
      claude-design,
      popular-web-designs,
      landing-pages,
      design-system-gtm,
      effective-ui-design,
      a-b-testing,
    ]
  frameworks:
    - "Nielsen Norman Group — UX Research and Usability Heuristics"
    - "Baymard Institute — E-commerce/Form UX Research"
    - "Steve Krug — Don't Make Me Think (usability)"
    - "GoodUI — Evidence-based conversion patterns"
    - "WCAG 2.1 AA — Web Accessibility Standards"
    - "Luke Wroblewski — Mobile First and Form Design"
---

# UI/UX for GTM

## Overview

GTM tools live or die on usability. A landing page with beautiful design that
converts at 1% loses to an ugly page converting at 4%. The mistake: designing
for aesthetics over conversion, or for desktop over mobile, or for perfect
vision over real-world accessibility. This skill covers UI/UX patterns for
every GTM surface — landing pages, forms, signup flows, dashboards, and
onboarding — with a ruthless focus on conversion, accessibility, and mobile
performance.

## When to Use

Trigger phrases: "design a landing page UI", "audit our form UX", "improve
signup flow conversion", "design a GTM dashboard", "make our pages accessible",
"mobile-first GTM design", "conversion rate optimization", "form design",
"onboarding UX", "WCAG compliance"

## Authoritative Foundations

### Nielsen Norman Group — 10 Usability Heuristics

1. Visibility of system status
2. Match between system and real world
3. User control and freedom
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use
8. Aesthetic and minimalist design
9. Help users recognize, diagnose, and recover from errors
10. Help and documentation

### Baymard Institute — Form UX Research

- Average form abandonment rate: 68%
- Every field removed increases conversion by 5-10%
- Inline validation reduces errors by 22%
- Single-column forms outperform multi-column by 15%

### Steve Krug — Don't Make Me Think

"Don't make me think" is the first law of usability. If a user pauses to
figure out what to do next, the design has failed.

## Step-by-Step Process

### Phase 1: Landing Page Architecture

**Conversion-first landing page structure (top to bottom):**

1. **Hero (above fold — 3 seconds to communicate value):**
   - Headline: The outcome, not the feature. "Close more deals" > "CRM software"
   - Subhead: One sentence. "Automate prospecting and enrichment so your team
     spends time selling, not researching."
   - Hero image: Product screenshot (real, not illustration) or demo video
   - Primary CTA: "Start free trial" or "Get a demo" — one CTA only
   - Secondary link: "See how it works" (for people not ready to commit)

2. **Social proof (immediately after hero):**
   - Customer logos (5-8 recognizable names)
   - Key stat: "Used by 2,000+ sales teams"
   - Testimonial: One quote from a named customer with photo

3. **Value props (3-5, each with visual):**
   - Icon + headline + one sentence each
   - NOT "Feature list." Outcome: "Find emails instantly" > "Email finder"

4. **How it works (3 steps):**
   - Visual: screenshot or diagram per step
   - Keep it 3 steps. More = overwhelming.

5. **Detailed features (for comparison shoppers):**
   - Expandable sections or tabs
   - Comparison table: you vs alternatives

6. **Pricing (if self-serve):**
   - 3 tiers, one recommended
   - Annual default, monthly option
   - "Start free trial" CTA on each tier

7. **FAQ (address top 5 objections):**
   - "Do I need a credit card?" → "No, 14-day free trial, no card required."
   - "Can I cancel anytime?" → "Yes, no contracts, no questions."

8. **Final CTA:**
   - Same as hero CTA (consistency)
   - "Join 2,000+ teams already using [product]"

**Mobile considerations:**

- Stack columns vertically (single column on mobile)
- CTA visible without scrolling (sticky CTA on mobile)
- Touch targets: minimum 44×44px (Apple HIG)
- Forms: use appropriate input types (tel, email, number) for right keyboard

### Phase 2: Form Design

**The 8 rules of high-converting forms:**

1. **Fewest fields possible.** Every field is a friction point. Start with:
   Email only. Add more fields via progressive profiling AFTER signup.

2. **Single column layout.** Multi-column forms confuse users about field
   order. Users scan vertically. Single column always.

3. **Top-aligned labels.** Labels above fields (not left-aligned) reduce
   completion time by 50% (Google/EYE tracking studies).

4. **Inline validation.** Validate as user types, not after submit.
   - Valid: green checkmark
   - Invalid: red border + error message below field
   - Error message must say: what's wrong + how to fix it

5. **Clear error messages (not vague):**
   - BAD: "Invalid email" → GOOD: "That doesn't look like an email address.
     Use format: name@company.com"
   - BAD: "Password too short" → GOOD: "Password must be at least 8 characters.
     You entered 5."

6. **Appropriate input types:**
   - `type="email"` for email fields (mobile keyboard shows @)
   - `type="tel"` for phone (numeric keypad)
   - `type="number"` for quantities
   - `type="url"` for website fields

7. **No placeholder as label.** Placeholder text disappears on focus. Users
   forget what the field was for. Use a real label above the field.

8. **Optional vs required labeling:**
   - Mark required fields with an asterisk and label: "Email *"
   - OR mark optional fields with "(optional)" — only one approach per form
   - Don't mix: "Email *" and "Phone (optional)" on the same form

**Form field reduction patterns:**

| Current State           | Improvement                                  | Fields Saved |
| ----------------------- | -------------------------------------------- | ------------ |
| First Name + Last Name  | Full Name                                    | 1            |
| Separate address fields | Address lookup (Google Places API)           | 4-5          |
| Company + Company Size  | Company name only (size from enrichment)     | 1            |
| Phone Number            | Remove (get later via progressive profiling) | 1            |

### Phase 3: Signup and Onboarding Flow

**Signup flow:**

1. Email → Password → "Create account" (3 fields max)
2. Verify email (6-digit code or magic link — NOT "check your email and come
   back")
3. Onboarding: "What's your goal?" (1 question, multiple choice)
4. Product tour: 3 steps, skippable, 30 seconds total
5. Empty state: "Here's what you'll see when you have data" + "Get started"
   button

**Time-to-value (TTV) targets:**

| Product Type                    | TTV Target  | How                                           |
| ------------------------------- | ----------- | --------------------------------------------- |
| Free tool (calculator, checker) | <30 seconds | Instant result, no signup required            |
| Self-serve SaaS                 | <5 minutes  | Guided setup, sample data, templates          |
| Sales-assisted SaaS             | <1 day      | White-glove onboarding, import existing data  |
| Enterprise platform             | <2 weeks    | Dedicated implementation, SSO, data migration |

### Phase 4: Dashboard Design

**Dashboard layout principles (Nielsen Norman Group):**

1. **Most important metric first** — top-left, largest visual weight
2. **Trend over point** — "Up 12% from last month" > "$52,340"
3. **Red/Yellow/Green thresholds** — contextualize numbers
4. **Filters persist** — don't reset filters when navigating
5. **Exportable data** — "Download CSV" on every data view
6. **Date range presets** — "Last 7 days," "Last 30 days," "This quarter"

**KPI dashboard wireframe:**

```
┌─────────────────────────────────────────────────┐
│ [Logo]  Dashboard                    [Date Range ▼]│
├──────────┬──────────┬──────────┬──────────────────┤
│ ARR      │ NRR      │ Churn    │ Pipeline         │
│ $5.2M    │ 112%     │ 1.8%     │ $2.4M            │
│ ↑12% QoQ │ ↑3% QoQ  │ ↓0.3% QoQ│ 3.2x coverage    │
│ ● Green  │ ● Green  │ ● Green  │ ● Yellow         │
├──────────┴──────────┴──────────┴──────────────────┤
│ [Revenue trend chart — 12 months]                │
│                                                   │
├───────────────────────────────────────────────────┤
│ [Pipeline by stage — funnel visualization]        │
├───────────────────────────────────────────────────┤
│ [Recent activity — table]                         │
└───────────────────────────────────────────────────┘
```

### Phase 5: Accessibility (WCAG 2.1 AA)

**11-point accessibility checklist:**

| #   | Requirement                              | How to Test                                   |
| --- | ---------------------------------------- | --------------------------------------------- |
| 1   | Color contrast ≥ 4.5:1 (normal text)     | WebAIM Contrast Checker                       |
| 2   | Color contrast ≥ 3:1 (large text, 18px+) | WebAIM Contrast Checker                       |
| 3   | Don't use color alone to convey info     | Add icons, text, or patterns                  |
| 4   | All images have alt text                 | Screen reader audit                           |
| 5   | Forms have associated labels             | `<label for="id">`                            |
| 6   | Keyboard navigation works                | Tab through entire page                       |
| 7   | Focus indicators visible                 | `:focus-visible { outline: 2px solid blue; }` |
| 8   | Skip navigation link                     | `<a href="#main">Skip to content</a>`         |
| 9   | ARIA labels on interactive elements      | `aria-label="Close dialog"`                   |
| 10  | No auto-playing video/audio              | Or provide pause/stop controls                |
| 11  | `prefers-reduced-motion` respected       | `@media (prefers-reduced-motion: reduce)`     |

**Accessibility testing tools:**

- axe DevTools (browser extension)
- Lighthouse (built into Chrome DevTools)
- VoiceOver (macOS built-in screen reader)
- WebAIM Contrast Checker

## Output Format

```
UI/UX SPEC — [Page/Flow Name]

Page Type: [Landing / Form / Signup / Dashboard / Onboarding]
Conversion Goal: [primary action — signup, demo, purchase]

Sections:
[Wireframe or description of each section]

Component Specs:
- Buttons: [size, color, states (default/hover/active/disabled/focus)]
- Inputs: [type, label position, validation rules, error states]
- Cards: [padding, shadow, border radius, hover state]
- Typography: [hierarchy — H1 through caption]

Mobile Behavior:
- [How layout changes at <768px, <480px]
- [Touch target sizes]
- [Mobile-specific CTAs]

Accessibility:
- [Contrast ratios]
- [Keyboard navigation path]
- [Screen reader annotations]
- [Focus order]

A/B Test Readiness:
- [What elements to test first]
- [Hypothesis per element]
- [Success metric]
```

## Implementation Checklist

- [ ] Hero communicates value in <3 seconds (show to someone, ask "what does this do?")
- [ ] Single primary CTA per view (no competing CTAs)
- [ ] Forms use email-only minimum, progressive profiling for more
- [ ] Single-column form layout, top-aligned labels
- [ ] Inline validation on all form fields (validate as user types)
- [ ] Error messages say what's wrong AND how to fix it
- [ ] All touch targets ≥ 44×44px (Apple HIG minimum)
- [ ] Color contrast ≥ 4.5:1 for all text (WCAG AA)
- [ ] Keyboard navigable — Tab through the entire page
- [ ] Mobile tested — over 50% of B2B traffic is mobile
- [ ] Empty states designed (not just "No data" — show what WILL be there)
- [ ] `prefers-reduced-motion` respected for animations

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Design over conversion.** A beautiful page with 1% conversion is worse
   than an ugly page with 4%. Fix: A/B test. Let data decide. Beauty is
   subjective. Conversion is not.

2. **Too many fields.** "Name + Email + Phone + Company + Role + Team Size +
   How did you hear about us?" = 2% conversion. Fix: Email only. Collect
   the rest via progressive profiling or enrichment.

3. **Inaccessible color choices.** Thin gray text on white background.
   Blue links on blue backgrounds. Red/green as the ONLY status indicator
   (4.5% of the population is color-blind). Fix: Test contrast ratios.
   Add icons alongside color.

4. **No mobile testing.** "Our B2B buyers are on desktop." Wrong. 50%+ of
   B2B research happens on mobile. If your mobile experience is broken,
   you're losing half your pipeline. Fix: Design mobile-first. Desktop is
   an enhancement, not the default.

5. **Vague error messages.** "An error occurred." "Invalid input." These
   don't help users fix the problem. Fix: Every error message must say:
   what went wrong + how to fix + example if helpful.

6. **Ignoring the empty state.** New users see a blank dashboard that says
   "No data yet" and leave. Fix: Empty states should show sample data,
   explain what will appear, and provide a "Get started" button.

## Execution Artifacts

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections
  This skill includes lightweight artifacts the agent can load on demand:
  Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- `claude-design` — Design process for one-off HTML artifacts
- `popular-web-designs` — 54 known-brand design systems
- `landing-pages` — CRO audits, hero/offer/proof/CTA patterns
- `design-system-gtm` — Brand tokens, CSS variables, voice/tone
- `effective-ui-design` — Professional UI design guidelines
- `a-b-testing` — Experiment design, statistical significance

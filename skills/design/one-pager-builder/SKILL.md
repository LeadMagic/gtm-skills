---
name: one-pager-builder
description: >-
  Create one-page sales documents — product overviews, meeting leave-behinds,
  champion enablement sheets, trade show handouts. Scannable in 30 seconds,
  memorable enough to forward. Use when creating one-pagers, leave-behinds, quick
  reference sheets, or sales handouts. Triggers on: "one-pager", "leave-behind",
  "product overview", "handout", "champion doc", "sales sheet", or any request
  for a single-page sales document.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: design
  tags: [one-pager, sales, collateral, design, leave-behind]
  related_skills: [sales-enablement, pitch-deck-builder, battlecard-builder]
  frameworks: [AIDA Framework, 3W Framework, Cialdini Persuasion Principles]
---

# One-Pager Builder

## Overview

A one-pager is exactly one page. Not a two-page brochure folded in half. One
side of one sheet. It tells a prospect everything they need to know in 30
seconds of scanning, and it's valuable enough that a champion forwards it to
their boss.

The constraint is the value. One page forces clarity. No room for fluff.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **AIDA Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **3W Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Cialdini Persuasion Principles.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use

- "Create a one-pager for our product"
- "Build a leave-behind for this meeting"
- "Make a champion enablement doc"
- "Create a trade show handout"
- "I need a sales sheet"
- "Design a quick-reference for prospects"

## Step-by-Step Process

### Phase 1: Variant Selection

Choose the right type:

**Product Overview**
For initial meetings. Problem → Solution → 3 Differentiators → Proof → CTA.
Answers "what do you do and why should I care?"

**Post-Meeting Leave-Behind**
Reinforce what was discussed. References specific pain points from the
conversation. Keeps momentum between meetings.

**Champion Enablement**
Arms your internal champion to sell for you. Includes: how to describe the
problem, how to describe the solution, ROI data, answers to likely objections,
and a draft email they can forward to their boss.

**Trade Show Handout**
Quick intro that drives follow-up. Visual-heavy, minimal text. QR code to
demo or calendar. Scannable in 10 seconds in a noisy booth.

### Phase 2: Content Structure

Every one-pager follows the same skeleton. Adapt per variant:

```
┌─────────────────────────────────────┐
│ LOGO              [Product Name]    │
│                                     │
│ HEADLINE: [Value prop, <10 words]   │
│ Subheadline: [Who it's for]         │
│                                     │
│ ┌─────────┐  ┌─────────┐ ┌───────┐ │
│ │ Problem │  │Solution │ │Proof  │ │
│ │ 1-2     │  │ 3 key   │ │1 strong│ │
│ │ sentences│  │ benefits│ │metric  │ │
│ └─────────┘  └─────────┘ └───────┘ │
│                                     │
│ "Quote from customer or analyst"    │
│                                     │
│ CTA: [One clear next step]          │
│ Contact: name@company.com           │
└─────────────────────────────────────┘
```

1. **Problem statement** — one sentence. Use the prospect's language.
2. **Solution** — what you do and how. 3 key benefits, not 10.
3. **3 differentiators** — why you vs alternatives. Specific, provable.
4. **Proof point** — one strong metric or customer quote. Not five weak ones.
5. **CTA** — clear next step with specific contact person.

### Phase 3: Design Principles

- **One page, literally.** Front only or front-and-back maximum.
- **Scannable in 30 seconds.** Bold headers, short bullets, whitespace.
- **Visual hierarchy:** headline first (largest), benefits second, proof third.
- **Logo prominent** — brand recognition matters.
- **Specific contact** — never info@. A real person's name and email.
- **Match brand colors** — this is a brand touchpoint.

### Phase 4: Variant-Specific Templates

**Champion Enablement One-Pager:**
Add: "How to describe this to your team" (3 bullet summary), ROI data for
internal approval, common objections and answers, draft email they can forward.

**Post-Meeting Leave-Behind:**
Add: "As we discussed" section referencing specific pain points, personalized
next steps, your contact info prominently.

## Output Format

One-pager copy with layout guidance:

```
# One-Pager: [Product] — [Variant]

## Headline
[Value prop, under 10 words]

## Subheadline
[Who it's for]

## Problem
[One sentence in customer language]

## Solution
1. [Benefit 1 — outcome focused]
2. [Benefit 2 — outcome focused]
3. [Benefit 3 — outcome focused]

## Differentiators
1. [Specific, provable claim]
2. [Specific, provable claim]
3. [Specific, provable claim]

## Proof
"[Customer quote]" — [Name, Company]
[Or: one strong metric]

## CTA
[One clear action + contact info]

## Layout Notes
[Visual hierarchy guidance, section placement]
```

## Quality Check

- [ ] Fits on one physical page (not two pages crammed)
- [ ] Scannable in 30 seconds — bold headers visible, bullets short
- [ ] Problem stated in customer language, not marketing copy
- [ ] Differentiators are specific and provable
- [ ] CTA is clear — one action, not three
- [ ] Contact is a specific person, not info@
- [ ] Brand colors and logo placement noted
- [ ] Variant-appropriate sections included (champion email, trade show QR)

## Common Pitfalls

1. **Two pages pretending to be one.** If it takes 5 minutes to read, it's
   a brochure. Cut ruthlessly. Every sentence must earn its space.

2. **Feature list, not benefit list.** "10GB storage" → "Store 50,000 files
   without worrying about space."

3. **No CTA.** What should they do after reading? Visit a URL? Book a call?
   Email someone? Make it specific.

4. **Generic differentiators.** "Best-in-class" means nothing. "Only solution
   that verifies emails in real-time at 99%+ accuracy" means something.

5. **info@company.com as contact.** A one-pager with a generic email address
   signals "we don't actually want you to reach out."

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

## Related Skills

- **pitch-deck-builder**: Multi-slide presentations
- **battlecard-builder**: Competitive comparison documents
- **sales-enablement**: Complete enablement package
- **case-study-builder**: Customer stories in sales format

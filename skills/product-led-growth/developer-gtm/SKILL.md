---
name: developer-gtm
description: >-
  Build a developer go-to-market motion the way Vercel, Stripe, and Twilio do —
  open-source/framework flywheel, docs and quickstarts as the funnel, transparent
  self-serve pricing, PQL signals, DevRel/community as distribution, and a
  sales motion that enables developer champions instead of cold-pitching them.
  Use when designing GTM for a developer tool, API, or infrastructure product,
  or when sales feels like it is fighting the buyer. Triggers on: "developer
  selling", "sell to developers", "developer GTM", "DevRel", "developer
  marketing", "open source GTM", "Vercel GTM", "bottom-up developer adoption",
  "API product GTM", "PLG for dev tools".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: product-led-growth
  tags: [developer-gtm, devrel, developer-marketing, open-source, plg, self-serve]
  related_skills: [plg-strategy, freemium-optimization, founder-brand, content-led-growth]
  frameworks:
    - "Guillermo Rauch (Vercel) — Framework-defined infrastructure & DX-led growth flywheel"
    - "James Allgrove (Stripe) — Self-serve signup + build-with-developers sales motion"
    - "Adam DuVander (EveryDeveloper) — Developer Marketing Does Not Exist (education over promotion)"
    - "Lee Robinson (ex-Vercel VP DX, now Jesse VP Developer Education) — Docs, education, community as distribution"
    - "Wes Bush / Elena Verna (ProductLed / Reforge) — PQL signals + product-led + sales-assist hybrid"
---

# Developer GTM (Selling to Developers)

## Overview

Developer go-to-market fails when teams run a generic B2B playbook at a
technical buyer: gated whitepapers, "request a demo" walls, cold SDR sequences,
and pricing hidden behind a sales call. Developers evaluate by building, not by
sitting through pitches — and they route around anything that feels like
marketing. This skill encodes the motion used by developer-first companies
(Vercel, Stripe, Twilio): earn trust by helping developers ship, let the
product and docs do the selling, then bring sales in to enable the champion and
close the economic buyer — never to pitch the developer.

The mistake this prevents: treating developers as leads to be worked instead of
builders to be unblocked, and confusing bottom-up adoption (the developer) with
the top-down purchase (the economic buyer).

## When to Use

- "How do we sell to developers without annoying them?"
- "Design GTM for our API / dev tool / infrastructure product"
- "Build a developer marketing or DevRel function"
- "Open-source flywheel — how do we monetize it like Next.js → Vercel?"
- "Set up a self-serve free tier that feeds enterprise sales"
- "Our SDRs are cold-calling developers and it's backfiring"
- "When should sales engage a bottom-up account?"

## Authoritative Foundations

- **Guillermo Rauch (Vercel founder/CEO, creator of Next.js).** Vercel's wedge
  is developer experience: the open-source framework (Next.js) is free and
  self-hostable, and "framework-defined infrastructure" makes deploying to
  Vercel the path of least resistance. Self-serve (Hobby/Pro) drives adoption;
  enterprise sales arrives later because viral framework usage pulls it in. On
  the WorkOS podcast Rauch frames both DX and enterprise as priorities —
  developers are the advocates inside enterprise deals. Full case →
  `references/vercel-developer-selling.md`.
- **James Allgrove (Stripe).** "How Stripe Built a Sales Organization to
  Successfully Sell to Developers": instant self-serve signup and API keys, no
  forced contract or sales call, "build with them, not talk at them," and a
  sales job that unblocks developers and helps them make the internal case.
- **Adam DuVander (EveryDeveloper) — *Developer Marketing Does Not Exist*.**
  Marketing to developers should be invisible: education over promotion,
  specific not generic, with docs, tutorials, guides, open source, and tools as
  the marketing surface. Never waste a developer's time.
- **Lee Robinson (formerly VP of Developer Experience at Vercel, 2020–2025; now
  VP of Developer Education at Jesse).** DX as community + education + docs;
  templates and learning content as the top of the funnel.
- **Wes Bush (ProductLed) / Elena Verna (Reforge).** PQL signals and the
  product-led + sales-assist hybrid that routes self-serve usage into sales at
  the right moment (cross-reference `plg-strategy`).

## Prerequisites

- A product a developer can try without talking to sales (free tier, trial, or
  open-source core) and a time-to-first-value you can measure.
- Public, ungated documentation and at least one working quickstart.
- Ability to instrument product/usage signals (signups, activation, usage near
  plan limits) — see `plg-strategy` PQL scoring.
- Clarity on who the economic buyer is vs. who the developer/champion is.

## Step-by-Step Process

### Phase 1: Establish Developer Trust (Show, Don't Tell)

1. Ungate the funnel: docs, quickstarts, API reference, and SDKs are public and
   indexed (DuVander; docs are the discovery and evaluation channel).
2. Publish transparent, self-serve pricing. Hiding price behind "contact sales"
   is read as a red flag by technical buyers.
3. Make time-to-first-value minutes, not days: copy-paste quickstart, API keys
   on signup (Stripe pattern), starter templates, zero-config defaults (Vercel).
4. Remove "lead" friction: no required demo, no gating real docs behind email.

### Phase 2: Build the Flywheel (Open Source / Framework Wedge)

1. Identify the free, credible artifact that creates pull: an open-source
   framework/library, CLI, or SDK that is genuinely useful even un-monetized
   (Next.js → Vercel). Keep it open and self-hostable.
2. Make the commercial product the natural extension of that artifact (hosting,
   scale, collaboration, compliance), not a paywall on the core.
3. Feed the flywheel with credible content: templates/starters, benchmarks,
   changelogs, and tutorials — assets developers reuse and share.

### Phase 3: Self-Serve → PQL → Sales-Assist

1. Let developers adopt bottom-up and reach value alone (Hobby/Pro self-serve).
2. Score PQLs on real usage: nearing plan limits, multiple seats on one account,
   adoption spreading to a new team, "can we do X at scale / SSO / SOC2?"
   questions (see `plg-strategy`, `freemium-optimization`).
3. Trigger sales only on qualified intent — and route to a technical seller
   (Vercel's "Product Advocate" / technical AE), not a generic SDR blast.
4. Sell to the economic buyer (VP Eng/CTO/procurement) while enabling the
   developer champion to make the internal case. Bottom-up adoption + top-down
   commercial motion, timed off product signals — not the calendar.

### Phase 4: DevRel & Community as Distribution

1. Staff DevRel for developer success and credibility (quick wins, docs,
   sample apps, conference talks), not as a lead-gen quota.
2. Run community where developers already are (GitHub, Discord, X, events like
   ship/launch conferences) and contribute before extracting.
3. Measure DevRel by adoption, activation, and influenced pipeline — not raw
   GitHub stars or follower counts.

## Output Format

A developer GTM plan containing: trust audit (ungated docs, transparent pricing,
time-to-first-value), the open-source/flywheel wedge (free artifact →
commercial extension), a self-serve → PQL → sales-assist motion with named
trigger signals and seller roles, a DevRel/community distribution plan with
non-vanity metrics, a developer-credible content list (templates, benchmarks,
changelogs, tutorials), and a champion-enablement plan separating the developer
from the economic buyer.

## Quality Check

- [ ] Docs, quickstart, and pricing are public and ungated (no demo wall)
- [ ] Time-to-first-value is measured and is minutes, not days
- [ ] There is a free, credible artifact (OSS/CLI/SDK) creating real pull
- [ ] Commercial product extends the free core; it does not paywall it
- [ ] PQL triggers are based on usage signals, not lead forms
- [ ] Sales engages only on qualified intent, via a technical seller
- [ ] Developer (champion) and economic buyer are addressed separately
- [ ] DevRel metrics are adoption/activation/pipeline, not vanity stars
- [ ] Every recommendation cites a named source, not "best practices"

## Common Pitfalls

1. **Gating docs and pricing.** Forcing email or "contact sales" to read docs
   or see price kills evaluation. Developers self-serve or leave (DuVander).
2. **Cold-calling/emailing developers.** Spraying SDR sequences at the
   technical user breaks trust. Use product signals to reach the buyer
   thoughtfully; let the developer come to you (Stripe/Common Room).
3. **Paywalling the open-source core.** Restricting the free artifact to force
   conversion breaks the flywheel. Monetize the extension (hosting, scale,
   compliance), keep the core free (Next.js → Vercel).
4. **Vanity GitHub stars.** Stars and followers are not adoption. Measure
   activation, retained usage, and influenced pipeline.
5. **Treating DevRel as lead gen.** A DevRel team on an SDR quota loses
   credibility with developers. DevRel earns trust; sales closes.
6. **Confusing the user with the buyer.** The developer recommends; the
   economic buyer signs. Enable the champion, sell the buyer (Verna/Bush hybrid).

## Execution Artifacts

- `references/framework-notes.md` — Framework index and authority routing
- `templates/output-template.md` — Deliverable shell for the developer GTM plan
- `scripts/check-output.py` — Lightweight deliverable validator
- `references/vercel-developer-selling.md` — Vercel case deep-dive, sourced specifics, agent-routing table

## Related Skills

- **plg-strategy**: Self-serve model selection, PQL scoring, product-led + sales hybrid
- **freemium-optimization**: Free tier design and free-to-paid conversion
- **founder-brand**: Founder-led credibility and developer community presence
- **content-led-growth**: Docs, tutorials, and content as the developer funnel

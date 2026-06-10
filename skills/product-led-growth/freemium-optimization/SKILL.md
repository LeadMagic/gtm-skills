---
name: freemium-optimization
description: >-
  Freemium and free trial conversion optimization — model selection with
  full-funnel math, activation design, paywall placement, PQL scoring, and
  benchmark-anchored experiment planning. Use when optimizing freemium
  conversion, designing free-to-paid upgrade paths, or choosing between
  freemium and free trial models. Triggers on: "freemium optimization",
  "free trial conversion", "PQL scoring", "activation flow", "paywall design",
  "freemium to paid".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "2.1.0"
  author: LeadMagic
  category: product-led-growth
  tags: [freemium, free-trial, conversion, pql, activation, paywall, plg]
  related_skills: [plg-strategy, growth-experimentation, onboarding-flow, pricing-psychology, a-b-testing]
  frameworks:
    - "Kyle Poyar (Growth Unhinged) + ChartMogul + ProductLed — 2026 Free-to-Paid Conversion Report"
    - "ProductLed — State of B2B SaaS 2025 (446 companies)"
    - "OpenView Partners — 2023 Product Benchmarks (with Pendo)"
    - "Wes Bush — Product-Led Growth / Product-Led Onboarding"
    - "Dharmesh Shah (HubSpot) — Freemium as Flywheel Attract"
---

# Freemium Optimization

## Overview

"Free" gets users. "Free" doesn't pay the bills. The gap between free and paid
is where most PLG companies die — and the common mistake is optimizing
conversion rate in isolation rather than full-funnel math. Kyle Poyar's 2026
Free-to-Paid Conversion Report (200 B2B products, with ChartMogul and
ProductLed) shows that freemium drives roughly 90 signups per 1,000 visits vs
45 for free trials, meaning a lower per-signup conversion rate (8-12% GREAT for
freemium vs 10-15% for no-CC trial) can still produce more customers
end-to-end. Optimizing conversion rate in isolation causes teams to abandon
freemium prematurely.

The second mistake: skipping activation instrumentation and jumping straight
to conversion optimization. ProductLed's State of B2B SaaS 2025 (446
companies) found only 34% of companies track activation — but you cannot
improve conversion from an experience users have not completed. OpenView's
2023 Product Benchmarks (with Pendo) found that tracking PQLs/PQAs increased
the likelihood of fast growth by 61% — the single most influential lever in
their study.

## When to Use

- "Optimize freemium conversion"
- "Design free-to-paid upgrade path"
- "Set up PQL scoring"
- "Improve activation flow"
- "Choose between freemium and free trial"
- "Reduce time-to-value"
- Triggers on: "freemium optimization", "free trial conversion", "PQL scoring",
  "activation flow", "paywall design", "freemium to paid"

## Authoritative Foundations

- **Kyle Poyar (Growth Unhinged) + ChartMogul + ProductLed — 2026
  Free-to-Paid Conversion Report (200 B2B products).** Primary benchmark
  source for this skill. Provides median and GOOD/GREAT conversion rates by
  model type and credit-card-gate status, and the full-funnel signup-rate data
  that makes model choice a visits-to-customers calculation rather than a
  conversion-rate comparison. Key finding: 57% of products lead with free
  trial vs 26% freemium. See `references/framework-notes.md` for the full
  benchmark table by model and ACV bracket.
- **ProductLed — State of B2B SaaS 2025 (446 companies).** Source for PQL
  adoption and activation tracking data. Only 24-25% of PLG companies use
  PQLs, but PQL users see roughly 3× higher free-to-paid conversion. Only 34%
  track activation. Companies with "highly intentional" free models (8+/10)
  report 57% better free-to-paid conversion than unintentional ones (3 or
  below). Intentional design means the free tier showcases core value, creates
  natural upgrade paths, has deliberate value limits, and makes upgrade
  benefits visible inside the free experience.
- **OpenView Partners — 2023 Product Benchmarks (with Pendo, ~1,000
  participants).** Tracking PQLs/PQAs increased likelihood of fast growth by
  61% — the single most influential lever measured. Outreach to free signups
  adds 28%; a dedicated growth team adds 17%; over-relying on paid acquisition
  is inversely correlated with fast growth.
- **Wes Bush — Product-Led Growth / Product-Led Onboarding.** Provides the
  bowling-alley onboarding model — guide rails (in-app prompts) and bumpers
  (email nudges) keep users on the path to their activation moment. The
  principle that the free tier must deliver the core value experience, and that
  time-to-value reduction is the primary activation lever. Used in Phase 2 to
  design the activation flow.
- **Dharmesh Shah (HubSpot) — Freemium as Flywheel Attract.** Free CRM/tier as
  top-of-flywheel acquisition; upgrade on seats, automation, integrations. Pair
  with `inbound-triage` for PQL→SQL handoff. `references/dharmesh-shah-hubspot-inbound.md`.

## Step-by-Step Process

### Phase 1: Model Decision with Full-Funnel Math

Before optimizing, select (or audit) the right model using full-funnel math —
not conversion rate alone.

| Model | Signups / 1,000 visits | GOOD conv rate | GREAT conv rate | When to use |
|---|---|---|---|---|
| Freemium (forever free) | ~90 | 3-5% | 8-12% | Core value deliverable in free; large TAM; viral/network effects |
| Free trial (no CC) | ~45 | 4-6% | 10-15% | Complex product; hands-on trial needed; mid-market motion |
| Free trial (CC required) | ~15-20 | 25-35% | 50-60% | High-intent buyers; self-serve checkout; lower volume acceptable |

Source: Poyar/ChartMogul/ProductLed 2026. The CC-gated model shows the highest
conversion rate but suppresses signup volume 4-6×. Run the full-funnel math
(signups × conversion rate = customers per 1,000 visits) before choosing it.
See `references/framework-notes.md` for the benchmark table by ACV bracket.

**Model intentionality test (ProductLed 2025):** Score your free model 1-10 on
intentionality. Companies scoring 8+ report 57% better free-to-paid conversion
than those scoring 3 or below. The test: does the free tier showcase core
value? Are value limits deliberate? Are upgrade benefits visible inside the
free experience?

### Phase 2: Activation Design

**Define the activation moment before measuring anything else.** Activation
is the point where a free user experiences your product's core value for the
first time. Without a named definition, there is no baseline and no conversion
target.

1. Name the activation event as a specific product event — for example:
   "User completes first export," "Two team integrations connected,"
   "Live-data report viewed."
2. Measure current time-to-activation (median and p90). Target: median under
   7 days.
3. Apply Wes Bush's bowling-alley model: in-app guide rails for the critical
   path, email bumpers for users who stall between steps.
4. Fill empty states with sample data showing what the user will see at
   activation — empty states are the leading cause of early drop-off.
5. Reduce steps-to-activation: every screen added between signup and the
   activation moment reduces completion rate.

Track activation before running conversion experiments. Only 34% of PLG
companies currently instrument activation (ProductLed 2025). If you are not
in that 34%, instrument first.

### Phase 3: Paywall Design and Placement

**Paywall timing:** After activation, before habit. A user who has experienced
core value but is not yet a daily user is at peak upgrade motivation. Show the
paywall before activation and they leave; after habit is formed, urgency
diminishes.

**Paywall triggers — map to product events, not just calendar time:**
- Usage limit reached (volume-based gate)
- Feature in paid tier requested (feature gate)
- Team invite sent (collaboration requires paid tier)
- Time-based trial expiration (fallback trigger only)
- Export/share/publish (output-based gate)

**Free tier design principle:** Enough to love, not enough to stay forever.
Free must deliver the core value experience so users activate and form intent
to buy, but leave a natural job undone that the paid tier completes.

### Phase 4: PQL Scoring and Routing

OpenView 2023: tracking PQLs/PQAs increased likelihood of fast growth by 61% —
the highest-impact lever in the benchmark. Despite this, only 24-25% of PLG
companies currently use PQLs (ProductLed 2025).

**Default scoring skeleton — calibrate weights to your product:**

| Signal | Weight |
|---|---|
| Activation event completed | 30 |
| Usage depth (key feature engagement) | 25 |
| Usage frequency (days active / last 14 days) | 20 |
| ICP fit (firmographic match) | 15 |
| Expansion signals (team invites, integrations connected) | 10 |

**Routing thresholds:**
- Score ≥ 70: immediate sales or high-touch outreach (PQL)
- Score 50–69: automated nurture sequence + SDR monitoring
- Score < 50: focus on activation, not conversion

A PQL model that scores users but does not trigger a defined action within an
SLA delivers no value. Define routing and response SLAs before launch. See
`references/framework-notes.md` for PQL trigger examples by product type.

### Phase 5: Experiment Backlog

Structure experiments against full-funnel stages, ordered from top of funnel
to bottom:

1. **Activation experiments:** Reduce time-to-activation; test guided vs
   self-directed onboarding; test sample-data pre-fill; test step reduction.
2. **Paywall experiments:** Test trigger placement (usage limit vs feature gate
   vs time); test paywall copy and upgrade-value framing; test pricing page
   layout.
3. **PQL routing experiments:** Test outreach timing (immediate vs 24-hour
   delay post-score); test channel (email vs in-app vs sales call).
4. **Model experiments:** If evidence supports it, test CC-gate vs no-CC gate
   on a traffic split — measure customers-per-1,000-visits as the primary
   metric, not conversion rate.

## Output Format

Freemium optimization plan containing: model decision with full-funnel math
(signups × conversion rate = customers per 1,000 visits) benchmarked against
Poyar/ChartMogul data; activation definition with named product event,
instrumentation plan, and time-to-activation baseline; paywall trigger map with
product-event-to-gate assignments and timing rationale; PQL scoring model with
signal weights, routing thresholds, and response SLAs; benchmark-anchored
experiment backlog ordered by funnel stage (activation first, then conversion,
then routing).

## Quality Check

Before delivering, verify:
- [ ] Model choice is justified with full-funnel math (visits → signups → conversions → customers), not conversion rate alone
- [ ] Activation event is named as a specific product event, not "user engages with the product"
- [ ] Paywall placement is after the defined activation event, not at signup
- [ ] PQL model has at least 5 signal dimensions with documented weights and routing thresholds
- [ ] Every benchmark cited names the model type (freemium vs trial vs CC-gated) and the source report
- [ ] Experiment backlog is ordered by funnel stage with activation experiments first

## Common Pitfalls

1. **Optimizing conversion rate instead of full-funnel customers-per-visit.**
   A CC-gated trial shows 50%+ conversion but suppresses signup volume 4-6×;
   end-to-end customer count can be lower than freemium. Fix: always run the
   full-funnel math before declaring a model "better."
2. **Skipping activation instrumentation.** You cannot improve conversion from
   an experience users have not completed. Fix: define and instrument the
   activation event before running any conversion experiment — only 34% of PLG
   companies currently do this (ProductLed 2025).
3. **Free tier that replaces paid.** If free delivers 90% of what paid delivers,
   users do not upgrade. Fix: apply the intentionality test — free showcases
   core value, paid completes the job; deliberate value limits and visible
   upgrade benefits inside the free experience are required.
4. **PQL scoring without routing.** A model that scores users but triggers no
   action within a defined time window delivers no revenue lift. Fix: define
   routing thresholds and response SLAs before launch; OpenView confirms
   outreach to free signups adds 28% to fast-growth likelihood.

## Execution Artifacts

- `references/framework-notes.md` — Conversion benchmarks, PQL triggers, activation template
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator
**Lifecycle (Acquisition → Activation):** `references/activation-playbook.md` · `references/gtm-lifecycle-stages.md` · Pattern 18 in `using-gtm-skills`
**Canonical lifecycle (repo root):** `references/gtm-lifecycle-stages.md` (Acquisition, Activation) · `references/activation-playbook.md` · `references/lifecycle-metrics-by-stage.md`

## Related Skills

- plg-strategy, growth-experimentation, onboarding-flow, pricing-psychology, a-b-testing

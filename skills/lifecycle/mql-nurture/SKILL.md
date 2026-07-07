---
name: mql-nurture
description: >-
  Build MQL nurture programs — lead scoring, nurture tracks, email drip sequences,
  MQL→SQL conversion. Triggers on: "MQL nurture", "lead nurture", "nurture tracks",
  "MQL to SQL", "lead scoring".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: lifecycle
  tags: [lifecycle, nurture, MQL, lead-scoring, email-drips]
  frameworks:
    - "SiriusDecisions Demand Waterfall"
    - "Marketo Nurture Framework"
    - "Reforge — Lifecycle Marketing"
---

# MQL Nurture Programs

## Overview

Most MQLs aren't ready to buy — they're researching. Nurture programs keep your
company top-of-mind during the 3-12 month evaluation window, converting MQLs to
SQLs at 2-3x the rate of "send them to sales and pray." This skill covers nurture
strategy, track design, and optimization.

## Authoritative Foundations

- **SiriusDecisions Demand Waterfall** — Named methodology governing recommendations in this skill's process.
- **Marketo Nurture Framework** — Named methodology governing recommendations in this skill's process.
- **Reforge — Lifecycle Marketing** — Startup operating cadence — default alive, talk to users, launch fast.

## Lifecycle Stage

**Acquisition** (stage 2). Canonical index → `references/gtm-lifecycle-stages.md`.  
Metrics → `references/lifecycle-metrics-by-stage.md` (Acquisition).  
Monitoring → `skills/analytics/gtm-metrics/templates/lifecycle-monitoring-dashboard.md`.

## When to Use

- "Build an MQL nurture program"
- "Lead nurture strategy"
- "MQL to SQL conversion"
- "Nurture email drips"
- "Lead scoring for nurture"

## Step-by-Step Process

### Phase 1: Lead Scoring Model

Define what makes an MQL:

**Fit Score (0-50):**

- Job title matches ICP (0-20)
- Company size in target range (0-15)
- Industry in target vertical (0-15)

**Engagement Score (0-50):**

- Content downloads (5 pts each)
- Website visits >5 pages (10 pts)
- Webinar attendance (15 pts)
- Pricing page visit (20 pts)
- Demo request (50 pts — auto-SQL)

**MQL Threshold:** Combined score >40 → MQL → enter nurture.
**SQL Threshold:** Combined score >70 → SQL → route to sales.

### Phase 2: Nurture Track Design

Create persona-specific nurture tracks:

**Track 1 — The Researcher (downloaded educational content):**

- Week 1: "Thanks for downloading [resource] — here's a related template"
- Week 2: Customer story from same industry
- Week 4: Webinar invite: "How [Industry] teams solve [problem]"
- Week 6: Benchmark report: "2026 [Industry] benchmarks"
- Week 8: "Ready to see how this works?" → soft CTA for demo

**Track 2 — The Evaluator (visited pricing/comparison pages):**

- Week 1: "How [Company A] evaluated [category] tools" (buyer's guide)
- Week 2: ROI calculator + case study with specific ROI numbers
- Week 3: "[Your product] vs [Competitor]" comparison
- Week 4: Demo invite: "See it in action with your data"
- Week 5: "Still evaluating?" + customer reference offer

**Track 3 — The Event Attendee (attended webinar):**

- Day 1: Recording + slide deck + "top questions answered"
- Day 3: Related case study
- Day 7: "The one thing most people miss about [topic]"
- Day 14: Soft CTA: "Want to discuss [topic] for your specific situation?"

### Phase 3: Email Content Principles

- **Value-first:** 80% educational, 20% product. If every email is "book a demo,"
  they unsubscribe.
- **Progressive profiling:** Each email asks for slightly more engagement.
  Click → download → webinar → demo.
- **Personalization by source:** Reference how they entered the funnel.
  "Since you downloaded our [guide]..."
- **Behavioral triggers:** If they click on pricing → shift to Evaluator track.
  If they stop opening → shift to re-engagement.

### Phase 4: Multi-Channel Nurture

Layer channels beyond email:

- **LinkedIn:** Connect with MQLs. Share content they engage with.
- **Retargeting:** Show case study ads to content downloaders. Show demo ads
  to pricing page visitors.
- **Direct mail:** For high-value MQLs (>$50K potential ACV), send a physical
  asset (book, report, tool).
- **Sales calls:** SDR calls MQLs at specific nurture milestones
  (after webinar attendance, after pricing page visit).

### Phase 5: Optimization

- **Track performance:** Open rate, click rate, conversion to SQL, conversion
  to opportunity, revenue influenced
- **A/B test:** Subject lines, content formats (text vs video vs infographic),
  send frequency, CTA phrasing
- **Cadence optimization:** Too fast = unsubscribes. Too slow = they forget you.
  Start at 7-14 day intervals and adjust based on engagement.
- **Exit criteria:** Auto-remove from nurture after 6 months of no engagement.
  Move to re-engagement track.
- **Dead lead management:** After 12 months of no engagement, suppress from all
  nurture. Maintain in database for reactivation plays.

## Output Format

Nurture program design with: lead scoring model, track definitions, email
sequences per track, multi-channel integration, and optimization framework.

## Quality Check

Before delivering, verify:

- [ ] Fit + engagement scoring model is two-dimensional — no single-criterion MQL thresholds
- [ ] At least 3 nurture tracks defined with distinct entry signals, cadences, and exit CTAs
- [ ] Behavioral branching rules exist — pricing click → Evaluator track; no opens 30 days → re-engagement
- [ ] Multi-channel layering is specified (email primary, LinkedIn for MQLs, retargeting by stage, direct mail for $50K+ ACV)
- [ ] 80/20 educational-to-product ratio enforced across all nurture content
- [ ] Exit criteria defined: auto-remove from nurture at 6 months no engagement; dead-lead suppression at 12 months

## Common Pitfalls

1. **Single-track nurture.** Every MQL gets the same drip regardless of source, persona, or buying stage. Fix: build at least 3 tracks gated by acquisition source — Researcher (content download), Evaluator (pricing/comparison page), Event Attendee (webinar).
2. **Product-heavy email ratio.** Every email asks for a demo and provides zero educational value — unsubscribe rates climb. Fix: enforce 80/20 educational-to-product ratio; the 5th email in a track should be the first hard CTA.
3. **No behavioral branching.** Contacts keep receiving email #4 when they never opened #1. Fix: implement engagement-based routing — no opens for 30 days triggers re-engagement track; pricing page visit triggers Evaluator track.
4. **Forever nurture.** Contacts in nurture for 18 months with no engagement drain sender reputation and ESP budget. Fix: hard exit at 6 months of no engagement; suppress from all nurture at 12 months; retain in database for reactivation plays only.
5. **MQL definition drift.** Without a locked scoring model, 'MQL' becomes whatever sales asks for this week. Fix: publish the scoring model, lock thresholds (MQL >40, SQL >70), and require RevOps sign-off to change weights.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator
  **Canonical lifecycle (repo root):** `references/gtm-lifecycle-stages.md` (Acquisition) · `references/lifecycle-metrics-by-stage.md` · `references/lifecycle-skill-index.md`

## Related Skills

- inbound-triage, lifecycle-drips, re-engagement, email-deliverability, campaign-analytics

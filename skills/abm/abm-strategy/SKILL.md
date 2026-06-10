---
name: abm-strategy
description: >-
  Design and execute Account-Based Marketing strategy — tier selection, account
  scoring, channel orchestration, BDR alignment, measurement framework. Triggers
  on: "ABM strategy", "account based marketing", "ABM playbook", "design ABM",
  "target accounts", "ABSD", "account based sales development", "Lars Nilsson".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.2.0"
  author: LeadMagic
  category: abm
  tags: [abm, account-based-marketing, target-accounts, enterprise, b2b, absd]
  frameworks: [ITSMA ABM Framework, TOPO Account-Based Framework, WbD Bowtie, John Ruhlin Giftology, Sendoso Sending Platform, "Lars Nilsson (Cloudera/Snowflake) — Account-Based Sales Development (ABSD)"]
---

# ABM Strategy

## Overview
ABM is not "send a gift and call it ABM." It's a systematic approach to treating
accounts as markets of one — aligned sales and marketing motions against a curated
set of target accounts. This skill designs the full ABM program: tier selection,
account intelligence, channel orchestration, and measurement.

## When to Use
- "Design our ABM strategy"
- "Set up account-based marketing"
- "Build a target account program"
- "How do we run ABM?"
- "Account selection for enterprise"

## Authoritative Foundations
- **ITSMA ABM Framework** — Three tiers of ABM: Strategic (1-to-1), Scale (1-to-few),
  Programmatic (1-to-many). Each tier has different investment, account count, and
  personalization depth.
- **TOPO Account-Based Framework** — Account selection, insights, plays, metrics.
  The six roles in an ABM team: ABM lead, account exec, SDR, field marketing,
  content marketing, marketing ops.
- **Winning by Design Bowtie** — ABM lives between marketing (left side) and sales
  (center), bridging awareness through close and into post-sale expansion.
- **Lars Nilsson — Account-Based Sales Development (ABSD).** The SDR execution layer
  of ABM, created at Cloudera and scaled across 100+ SDRs at Snowflake. Account
  selection on **buying signals** (intent surge, job posts, funding) not hunches;
  SDR + AE + vertical SME co-author 3-email sequences from a use-case library;
  multi-persona outreach in 50–250 contact chunks; quality of engagement over
  volume sent (public first-campaign results: ~70% open / ~30% reply vs 5–8% / 2–3%
  for nurture blasts). Canonical → `references/lars-nilsson-absd.md`.

## Step-by-Step Process

### Phase 1: Account Selection
Define the 3-tier account model:
- **Tier 1 (1-to-1):** 5-15 accounts. Strategic, $100K+ ACV. Full account intelligence,
  custom content, executive engagement. C-suite mapping required.
- **Tier 2 (1-to-few):** 15-50 accounts. Clustered by industry/use case. Semi-custom
  campaigns, persona-specific outreach, industry-specific proof points.
- **Tier 3 (1-to-many):** 50-200+ accounts. Programmatic. Lookalike from Tier 1-2 wins,
  automated personalization, scaled outbound.

Selection criteria: ICP fit score (0-100), intent signals (hiring, funding, tech stack),
engagement history (website visits, content downloads, event attendance), deal size potential.

### Phase 2: Account Intelligence
For each Tier 1/2 account, build an account brief:
- Company snapshot (revenue, employees, growth, funding)
- Strategic priorities (earnings calls, annual reports, press)
- Org chart (decision-maker, champion, economic buyer, influencers, blockers)
- Tech stack (current tools, gaps, integration points)
- Relationship map (who knows who, existing connections)
- Trigger events (new hire, funding, M&A, product launch, earnings miss)

### Phase 3: Channel Orchestration
Map channels by tier:
- **Tier 1:** Executive mailers, Giftology gifts (`strategic-gifting`), custom microsites,
  direct mail, in-person events, executive-to-executive calls
- **Tier 2:** Personalized email + LinkedIn, industry roundtables, webinar invites,
  direct mail, SDR outbound
- **Tier 3:** Automated email sequences, LinkedIn ads, content syndication,
  webinar series, SDR cadences

### Phase 4: BDR Alignment
ABM fails without tight sales alignment:
- BDRs assigned to specific accounts (not territories)
- Shared account briefs between marketing and BDRs
- Weekly ABM standups: marketing + BDRs + AEs on target accounts
- SLAs: contact attempts within 24h of marketing touch

For the full SDR execution layer — signal-based account prioritization, SDR + AE +
SME co-authored sequences, multi-persona chunking, and public response benchmarks —
run the ABSD playbook: `references/lars-nilsson-absd.md`.

### Phase 5: Measurement Framework
Don't measure ABM on MQLs. Measure:
- **Coverage:** % of target accounts with contacts identified
- **Engagement:** touches per account per week, depth (C-suite vs end user)
- **Pipeline:** opportunities created from target accounts
- **Velocity:** days from first touch to opportunity
- **Win rate:** target accounts vs non-target
- **Deal size:** target account ACV vs non-target

## Output Format
ABM strategy document with: tier definitions, account selection criteria and initial
list, intelligence template, channel plan by tier, BDR alignment model, measurement
dashboard design.



## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls

1. **Treating ABM as a marketing-only initiative.** ABM requires tight sales alignment. Without BDRs assigned to specific accounts and shared account briefs, marketing produces content nobody uses. Fix: weekly ABM standups with marketing + BDRs + AEs.
2. **One-size-fits-all tiering.** Applying the same playbook to Tier 1 and Tier 3 accounts. Fix: Tier 1 gets custom content and executive engagement; Tier 3 gets automated personalization.
3. **Measuring ABM on MQLs.** ABM success is pipeline from target accounts, not lead volume. Fix: track coverage %, engagement depth, pipeline created, and win rate by tier.

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

- ITSMA ABM Framework: apply only the part that directly improves the requested deliverable.
- TOPO Account-Based Framework: apply only the part that directly improves the requested deliverable.
- WbD Bowtie: apply only the part that directly improves the requested deliverable.
- John Ruhlin Giftology: apply only the part that directly improves the requested deliverable.
- Lars Nilsson ABSD: apply only the part that directly improves the requested deliverable.

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
- `references/lars-nilsson-absd.md` — Lars Nilsson (Cloudera/Snowflake) ABSD playbook: signal-based selection, SME sequence design, stack, benchmarks
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills
- abm-1-to-1, abm-1-to-few, abm-1-to-many, account-selection, multi-thread-orchestration
- icp-scoring, sales-enablement, meeting-prep, pipeline-management, signal-scoring

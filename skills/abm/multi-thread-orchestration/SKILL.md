---
name: multi-thread-orchestration
description: >-
  Orchestrate multi-threaded ABM engagement across buying committee members —
  stakeholder mapping, parallel plays, ghost node detection. Triggers on:
  "multi-thread", "stakeholder map", "buying committee", "deal mapping".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: abm
  tags: [abm, multi-thread, stakeholder-mapping, buying-committee, enterprise]
  frameworks:
    - "Force Management MEDDICC"
    - "Gartner Challenger Sale Stakeholder Mapping"
    - "ITSMA — Account-Based Marketing"
---

# Multi-Thread Orchestration

## Overview
Single-threaded deals die when the champion leaves or loses internal support.
Multi-threading means engaging multiple stakeholders in the buying committee with
role-relevant messaging — so the deal survives any individual departure and builds
organizational consensus. This is an enterprise sales superpower.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Force Management MEDDICC.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Gartner Challenger Sale Stakeholder Mapping.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **ITSMA — Account-Based Marketing.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Multi-thread this deal"
- "Map the buying committee"
- "Who else should we be talking to?"
- "Deal is stuck with one contact"

## Core Principle
> The biggest risk to any enterprise deal is not the competitor — it's "no decision."
> No decision happens when your champion can't sell internally as well as you sell
> externally. Multi-threading arms them with the right message for every stakeholder.

## Step-by-Step Process

### Phase 1: Stakeholder Identification
Map all 7 roles in the buying committee:
1. **Executive Sponsor:** EVP/C-level. Controls budget. Cares about strategic impact.
2. **Champion:** Day-to-day contact. Sells internally. Cares about career advancement.
3. **Economic Buyer:** Signs the check. Cares about ROI, risk, and timeline.
4. **Technical Buyer:** IT/Security/Architecture. Cares about implementation, security, scale.
5. **Influencer:** End user or adjacent team lead. Cares about workflow improvement.
6. **Blocker:** Status quo defender. Cares about avoiding change/disruption.
7. **Coach:** Internal ally (may not be obvious). Gives you intel on decision process.

### Phase 2: Ghost Node Detection
"Ghost nodes" are stakeholders you haven't identified yet who can kill the deal.
Detection triggers:
- "We're waiting on legal review" → Ghost node: General Counsel
- "IT needs to approve the security review" → Ghost node: CISO/VP Security
- "Finance is looking at the budget allocation" → Ghost node: CFO/VP Finance
- "We need procurement to finalize" → Ghost node: Procurement director
- Any new name that appears after deal stage 3

When you detect a ghost node: immediately request an intro, prepare role-specific
content, and add them to your stakeholder map.

### Phase 3: Role-Specific Engagement
Per stakeholder role, deliver:
- **Exec Sponsor:** 1-page executive summary, peer references, industry benchmarking
- **Champion:** Internal selling toolkit, ROI slide, competitor comparison, implementation plan
- **Economic Buyer:** Business case with conservative scenario, payback timeline, risk mitigation
- **Technical Buyer:** Architecture diagram, security whitepaper, API docs, SOC2 report
- **Influencer:** Use case demo, workflow integration walkthrough, training outline
- **Blocker:** Risk acknowledgment, transition plan, vendor stability proof

### Phase 4: Parallel Play Design
Run simultaneous plays across threads:
- Champion gets enablement content Thursday morning
- Exec sponsor gets peer case study Thursday afternoon
- Technical buyer gets security review response Friday
- All converge at next week's steering committee where your champion presents

### Phase 5: Deal Health Scoring
Score 0-100 based on thread coverage:
- <3 stakeholders engaged: HIGH RISK (single point of failure)
- 3-4 stakeholders: MEDIUM RISK
- 5+ stakeholders with exec sponsor engaged: LOW RISK
- Ghost node detected and not engaged: CRITICAL RISK regardless of count

## Output Format
Stakeholder map (power/interest grid), per-role engagement plan, ghost node
detection log, parallel play timeline, and deal health scorecard.



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

- Force Management MEDDICC: apply only the part that directly improves the requested deliverable.
- Gartner Challenger Sale Stakeholder Mapping: apply only the part that directly improves the requested deliverable.
- ITSMA — Account-Based Marketing: apply only the part that directly improves the requested deliverable.

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


## Related Skills
- meeting-prep, objection-handling, abm-strategy, pipeline-management, demo-scripts

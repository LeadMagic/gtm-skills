---
name: abm-1-to-many
description: >-
  Execute Programmatic ABM (1-to-many) for 50-200+ accounts — automated personalization,
  scaled outbound, lookalike expansion. Triggers on: "1-to-many ABM", "programmatic ABM",
  "scaled ABM", "automated ABM".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: abm
  tags: [abm, 1-to-many, programmatic-abm, scaled, automation]
  frameworks:
    - "TOPO Programmatic ABM"
    - "Clay Automation Patterns"
    - "ITSMA — Account-Based Marketing"
---

# ABM 1-to-Many (Programmatic)

## Overview
Programmatic ABM for 50-200+ accounts using automation, lookalike modeling,
and scaled personalization. This tier uses the same methodology as 1-to-1 and
1-to-few but replaces manual effort with AI and workflow automation.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **TOPO Programmatic ABM.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Clay Automation Patterns.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **ITSMA — Account-Based Marketing.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Scale ABM to more accounts"
- "Programmatic ABM setup"
- "Automated account-based outreach"
- "Expand ABM coverage without headcount"

## Step-by-Step Process

### Phase 1: Lookalike Expansion
Start from Tier 1-2 winners and expand:
- **ICP lookalike:** Find accounts matching your top 10% win profile
- **Intent lookalike:** Accounts showing similar buying signals to closed-won
- **Engagement lookalike:** Accounts engaging with content the way winners did pre-opportunity
- **Trigger lookalike:** Accounts with same triggers (funding, hiring, tech change)

### Phase 2: Automated Account Intelligence
Use enrichment and AI to auto-build briefs:
- Clay workflow: pull firmographics, technographics, news, signals
- AI summarizes: company snapshot, pain hypothesis, relevant proof points
- Auto-prioritize: score accounts 0-100 and assign to SDR queues

### Phase 3: Scaled Personalization
- **Dynamic landing pages:** URL params personalize hero/headline by industry/company
- **Tokenized email sequences:** Merge fields beyond first name — industry, tech stack, signal
- **Automated LinkedIn:** AI drafts personalized connection notes and DMs
- **Retargeting:** Account-based ad audiences on LinkedIn by company name or domain

### Phase 4: Automated Cadence Orchestration
- SDR assigned accounts per round (rotating to prevent burnout)
- Automated task creation in CRM per account
- AI drafts first outreach; SDR reviews and sends
- AI handles replies (OOO, not interested, wrong person); SDR handles positive replies

### Phase 5: Feedback Loop
- Weekly review: which accounts engaged, which didn't
- Kill accounts after 8 touches with no reply
- Feed winners back into lookalike model
- Continuously refine ICP based on engagement patterns

## Output Format
Programmatic ABM plan with: lookalike criteria, enrichment workflow, personalization
templates, SDR routing rules, and optimization framework.



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

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

Use the artifacts when the user asks for an implementation-ready deliverable, a repeatable workflow, or a quality check rather than generic advice.

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

- TOPO Programmatic ABM: apply only the part that directly improves the requested deliverable.
- Clay Automation Patterns: apply only the part that directly improves the requested deliverable.
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
- clay-automation, ai-sdr-setup, list-building, signal-scoring, icp-scoring

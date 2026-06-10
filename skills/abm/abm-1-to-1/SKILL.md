---
name: abm-1-to-1
description: >-
  Execute Strategic ABM (1-to-1) for 5-15 high-value accounts — custom microsites,
  executive engagement, direct mail, board-level connections, custom content. Triggers
  on: "1-to-1 ABM", "strategic ABM", "custom ABM", "key account marketing", "named account".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: abm
  tags: [abm, 1-to-1, strategic-accounts, enterprise, key-accounts]
  frameworks: [ITSMA Strategic ABM, Force Management Command of the Message, John Ruhlin Giftology, Sendoso Sending Platform]
---

# ABM 1-to-1 (Strategic)

## Overview
Strategic ABM for 5-15 named accounts where you're pursuing $100K+ ACV deals.
This is custom, high-touch, relationship-driven — not automated sequences.
You research the account like you're writing a case study about them, then design
interactions that feel like the entire company exists to serve this one account.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **ITSMA Strategic ABM.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Force Management Command of the Message.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **John Ruhlin Giftology.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Run 1-to-1 ABM on [account]"
- "Build strategic account plan"
- "Custom ABM for enterprise"
- "Named account marketing play"

## Step-by-Step Process

### Phase 1: Account Deep Dive (2-4 hours per account)
Research across 10+ dimensions:
1. **Financial:** Revenue, growth rate, profitability, recent funding/earnings
2. **Strategic:** 10-K/earnings call priorities, analyst reports, CEO interviews
3. **Org chart:** Economic buyer, champion, influencers, blockers, exec sponsor
4. **Tech stack:** BuiltWith/Wappalyzer teardown, gaps your product fills
5. **Initiatives:** Hiring patterns, new offices, product launches, reorgs
6. **Competitors:** Who they use now, contract renewal timing, dissatisfaction signals
7. **Content:** What they read, who they follow, conference talks they give
8. **Network:** Board members, investors, advisors — who can make an introduction
9. **Pain points:** Specific to their industry, size, and stage
10. **Value hypothesis:** Dollarized impact your product would have on their specific business

### Phase 2: Account Plan
Build a 1-page account plan:
- **Opportunity hypothesis:** What problem do they have, why now, what's the cost of inaction
- **Stakeholder map:** Each person's role, power, influence, and current relationship
- **Buying process:** Their procurement steps, legal requirements, security review
- **Competitive landscape:** Incumbent, competitors, build-vs-buy risk
- **Value prop per persona:** Custom messaging for CFO (ROI), CRO (pipeline), CTO (architecture)
- **Engagement calendar:** 90-day touch plan with specific plays per week

### Phase 3: Executive Engagement
- **Pre-meeting briefing:** 1-page for your executive before any exec-to-exec call
- **Executive mailer:** Physical package with industry report, custom letter, relevant proof
- **Board-level intro:** Identify shared board members, advisors, or investors
- **Executive dinner:** Small group, industry topic, no pitch — relationship building
- **Advisory value:** Share market insight, industry data, benchmarking before selling

### Phase 4: Custom Content
- **Microsite:** Single-page experience for this account's industry + pain points
- **Custom ROI model:** Built with their public numbers (employee count, revenue)
- **Industry POV:** "State of [their industry]" report with their company as the case
- **Personalized demo:** Configured with their logo, data, use case

### Phase 5: Multi-Thread Orchestration
Map and activate contacts across the buying committee:
- Champion: Weekly value-add touch, enablement content
- Economic buyer: Monthly executive summary, peer references
- Technical buyer: Architecture sessions, security docs, API sandbox
- Influencers: Use case workshops, case studies from their industry
- Executive sponsor: Quarterly business review cadence

## Output Format
Per-account strategic plan with: deep dive research, account plan, engagement calendar,
stakeholder map, custom content briefs, and multi-thread playbook.



### Phase 6: Strategic Gifting (Giftology + Sendoso)

Full playbook → **`strategic-gifting`** (John Ruhlin Giftology, Sendoso/Alyce
execution, compliance, CRM tracking).

For each Tier 1 stakeholder, complete the gift brief in **strategic-gifting**
(gift-brief template):

- **Giftology:** 3-gift system, personalization, story, no logo, handwritten note
- **Sendoso / manual:** Manager-approved send; address confirmation for physical
- **Timeline:** Post-discovery yes; negotiation no; stalled deal → `buyer-indecision` not gifts
- **CRM:** Log policy limit, amount, story (gift-crm-log template in **strategic-gifting**)
- **SLA:** SDR/AE follow-up within 24h of delivery



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

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- `strategic-gifting` — Giftology, Sendoso, compliance, gift briefs
- `abm-strategy` — Tier model and measurement
- `multi-thread-orchestration` — Committee stakeholder gifts
- `meeting-prep` — Discovery before post-call gifts
- `pitch-deck-builder`, `roi-calculator` — Tier 1 assets

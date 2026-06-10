---
name: cs-playbooks
description: >-
  Build customer success playbooks — onboarding, health scoring, CSQLs, expansion
  plays, QBRs, and churn intervention. Use when building a CS function, designing
  customer journeys, or creating playbooks for retention and expansion. Triggers
  on: "customer success", "CS playbook", "onboarding", "health score", "CSQL",
  "expansion play", "customer retention", "QBR", or any request about post-sale
  customer engagement.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: customer-success
  tags: [customer-success, cs, retention, onboarding, health-scoring, expansion]
  frameworks: [Lincoln Murphy Desired Outcome, Gainsight CS Index, Winning by Design SPICED Post-Sale]
---

# Customer Success Playbooks

## Overview
Customer Success is not reactive support — it is proactive value delivery that
drives retention and expansion. This skill builds the CS operating system:
Desired Outcome mapping (Lincoln Murphy), health scoring with leading indicators
(Gainsight), CSQL identification for expansion, and playbooks per customer
lifecycle stage.

## When to Use
- "Build our customer success function"
- "Design customer onboarding"
- "Create a health score model"
- "Set up expansion plays"
- "Build QBR templates"
- "Customer comms during outage / incident"
- "CS crisis FAQ for support"
- "Retention crisis — churn wave response"

## Authoritative Foundations
- **Lincoln Murphy** — Desired Outcome framework. Every customer has a Required
  Outcome and an Appropriate Experience. Success is their outcome, not your
  feature usage. The Success Gap: customers using the product correctly but
  still failing.
- **Nick Mehta / Gainsight** — CS ops at scale: health scores, lifecycle stages,
  digital-first delivery. Operational layer on Murphy's strategy.
  → `references/lincoln-murphy-customer-success.md`
- **Winning by Design SPICED** — Post-sale lifecycle: onboarding → adoption →
  value realization → expansion → renewal.

## Step-by-Step Process
### Phase 1: Map the Customer Journey
Define stages: Onboarding → Activation (Day 1-7, aha moment) → Habit Formation
(Week 2-6, usage signals) → Indispensability (Month 2-6, workflow integration)
→ Expansion → Renewal. Each stage has a milestone metric.

### Phase 2: Build Health Scoring
Score 0-100: product usage (0-40), engagement depth (0-30), relationship
health (0-30). Red (<50): immediate CSM outreach. Yellow (50-74): automated
nurture. Green (75+): expansion targeting.

### Phase 3: Define CSQLs (Customer Success Qualified Leads)
Behavioral signals of expansion readiness: usage nearing plan limits, feature
adoption in new department, new stakeholders in meetings, "can we do X?"
questions, willingness to be a reference.

### Phase 4: Build Playbooks per Stage
- Onboarding play: time-to-first-value target, guided setup, success milestone
- Adoption play: usage monitoring, best practice sharing, feature education
- Expansion play: triggered by CSQLs, framed as "logical next step" not upsell
- Risk play: early warning signals, intervention cadence, executive alignment
- Renewal play: value review, ROI documentation, future roadmap alignment

### Phase 5: Incident & Crisis Customer Comms

**Canonical:** `references/crisis-management-playbook.md` · Pattern 33 · Executive home: `gtm-leadership`

| Role | CS responsibility |
|---|---|
| CS captain | Own customer email to affected segment; ticket macros |
| CSMs | Proactive outreach to red health accounts during outage |
| Support | Single FAQ source — `references/templates/crisis-faq-for-support.md` |

**Sequence:** Internal memo → holding statement / status page → affected customer email → FAQ for sales/support.

**ACKNOWLEDGE → OWN → ACT → FOLLOW UP** in all customer-facing copy. Legal review Sev 3+ before admitting data impact.

**Post-incident:** Retention play for accounts that churn-threatened; link `churn-prevention` and Retention stage in `references/gtm-lifecycle-stages.md`.

**Cross-links:** `customer-onboarding` (trust rebuild) · `references/gtm-data-exchange-playbook.md` (breach path)

## Output Format
CS playbook with journey map, health score model, CSQL definitions, and
stage-specific play templates.


## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls
1. **Measuring activity, not outcomes** — logins are not value. Map customer
   Desired Outcomes and measure progress toward them.
2. **CS as firefighting** — if CSMs only engage when something is wrong, they
   are reactive support, not customer success.
3. **No expansion motion** — CS owns the relationship. If expansion lives only
   in Sales, the customer gets handed off at the worst moment.
4. **One-size health score** — different segments need different health models.
   Enterprise cares about executive engagement; SMB cares about time-to-value.

## Execution Artifacts

This skill includes lightweight artifacts the agent can load on demand:

- `references/framework-notes.md` — named frameworks, citation anchors, and operating assumptions
- `references/lincoln-murphy-customer-success.md` — Desired Outcome, Success Gap, Gainsight ops (repo root)
- `templates/output-template.md` — copy-paste deliverable structure for the user
- `scripts/check-output.py` — local checklist validator for required sections

**Canonical lifecycle (repo root):** `references/gtm-lifecycle-stages.md` (Engagement, Retention) · `references/lifecycle-metrics-by-stage.md` · `references/templates/stage-health-scorecard.md`

**Crisis comms:** `references/crisis-management-playbook.md` · `references/templates/crisis-customer-email.md` · `crisis-faq-for-support.md`

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

- Lincoln Murphy Desired Outcome: apply only the part that directly improves the requested deliverable.
- Gainsight CS Index: apply only the part that directly improves the requested deliverable.
- Winning by Design SPICED Post-Sale: apply only the part that directly improves the requested deliverable.

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
- **gtm-leadership**: Executive war room and crisis severity (canonical)
- **customer-marketing**: Public reputation, G2/TR during incidents
- **customer-onboarding**: Post-incident trust and activation recovery
- **churn-prevention**: Early warning detection and re-engagement
- **expansion-selling**: Upsell and cross-sell motions
- **qbr-planning**: Quarterly business review structure

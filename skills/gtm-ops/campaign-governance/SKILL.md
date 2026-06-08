---
name: campaign-governance
description: >-
  Establish campaign governance — naming conventions, UTM parameters, campaign
  hierarchy, ROI measurement, budget tracking. Triggers on: "campaign governance",
  "UTM strategy", "campaign naming", "marketing ops governance".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: gtm-ops
  tags: [gtm-ops, campaign-governance, UTM, naming-conventions, marketing-ops]
  frameworks:
    - "Marketing Ops Governance Framework"
    - "SiriusDecisions Campaign Hierarchy"
    - "Winning by Design — Revenue Architecture"
---

# Campaign Governance

## Overview
Campaign governance is the unsexy foundation of marketing measurement. Without
enforced naming conventions and UTM parameters, your attribution data is garbage,
your ROI reports are fiction, and you can't answer "which campaigns actually work."
This skill builds the governance framework.

## Frameworks Referenced

This skill is grounded in named GTM frameworks and operator methodologies, not generic advice:

- **Marketing Ops Governance Framework** — used as the named operating framework for this playbook.
- **SiriusDecisions Campaign Hierarchy** — used as the named operating framework for this playbook.

## When to Use
- "Set up campaign naming conventions"
- "UTM governance"
- "Campaign hierarchy"
- "Marketing operations governance"

## Step-by-Step Process

### Phase 1: Campaign Hierarchy
Standardize the parent-child relationship:
- **Program:** Top level. Annual or quarterly initiative. "2026 Enterprise ABM"
- **Campaign:** Mid level. Specific channel play. "2026-06-Enterprise-Webinar-Series"
- **Tactic:** Bottom level. Individual asset or touch. "2026-06-Enterprise-Webinar-01-LinkedIn-Ad"

Rule: Every tactic belongs to exactly one campaign. Every campaign belongs to
exactly one program. No orphan campaigns.

### Phase 2: Naming Convention
Standard format: `[Date]-[Segment]-[Channel]-[Content]-[Version]`

Examples:
- `2026-Q3-Enterprise-LinkedIn-CaseStudy-A`
- `2026-06-MM-Email-ProductLaunch-B`
- `2026-H2-SMB-Webinar-Demo-v2`

Enforce via CRM validation rules. No free-text campaign names after go-live.

### Phase 3: UTM Governance
Required UTMs for every outbound link:
- `utm_source`: Platform (linkedin, email, google, partner_name)
- `utm_medium`: Channel type (paid_social, email, cpc, organic_social, referral)
- `utm_campaign`: Campaign name (from naming convention above)
- `utm_content`: Ad/asset variant (for A/B testing)
- `utm_term`: Keyword (for paid search only)

**Hard rules:**
- All lowercase. Underscores not hyphens for multi-word values.
- No random values. utm_source must come from the approved source list.
- Every paid link MUST have UTMs. Organic links should have UTMs.
- UTM builder tool required for all marketers. No manual URL construction.

### Phase 4: Enforcement
- **CRM validation:** Campaign name must match naming convention pattern.
  UTMs required on all campaign records.
- **Weekly audit:** Pull all campaigns created this week. Flag malformed names
  and missing UTMs. Fix within 24 hours.
- **Dashboard:** Campaign name compliance %, UTM coverage %, orphan campaigns.
  Visible to the whole marketing team.
- **Consequences:** Campaigns with non-compliant naming don't appear in ROI
  reports. This self-corrects within one reporting cycle.

### Phase 5: Review and Maintenance
- **Monthly:** Cleanup — merge duplicate campaigns, archive completed programs
- **Quarterly:** Audit UTMs on all active landing pages and ad accounts
- **Annually:** Review naming convention — does it still fit? If the business
  has changed (new channels, new segments), update the convention.

## Output Format
Campaign governance document with: hierarchy definition, naming convention
reference, UTM parameter dictionary, enforcement rules, and audit calendar.



## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls

1. **Tool sprawl without integration.** 15+ tools that don't talk to each other. Fix: CRM is the hub — everything reads from and writes to CRM. Consolidate overlapping tools.
2. **No naming conventions.** Campaign names like "webinar_final_v2" make attribution impossible. Fix: enforce standardized naming: [Date]-[Segment]-[Channel]-[Content].
3. **Process documented but not enforced.** CRM has stage definitions but reps skip required fields. Fix: CRM validation rules that prevent stage advancement without required data.

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

- Marketing Ops Governance Framework: apply only the part that directly improves the requested deliverable.
- SiriusDecisions Campaign Hierarchy: apply only the part that directly improves the requested deliverable.
- Winning by Design — Revenue Architecture: apply only the part that directly improves the requested deliverable.

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
- gtm-operations, campaign-analytics, attribution, crm-integration, gtm-metrics

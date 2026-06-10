---
name: abm-1-to-few
description: >-
  Execute ABM at Scale (1-to-few) for 15-50 clustered accounts — semi-custom campaigns,
  industry-specific content, persona-based plays. Triggers on: "1-to-few ABM", "ABM scale",
  "cluster ABM", "industry ABM".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: abm
  tags: [abm, 1-to-few, scale-abm, industry-clusters, b2b]
  frameworks:
    - "TOPO ABM Scale Framework"
    - "Force Management MEDDICC"
    - "ITSMA — Account-Based Marketing"
---

# ABM 1-to-Few (Scale)

## Overview
ABM at Scale for 15-50 accounts clustered by industry, use case, or buying trigger.
Not fully custom like 1-to-1, but not automated like 1-to-many. This is the
sweet spot where you get 80% of 1-to-1 results at 20% of the effort — if you
cluster correctly and build semi-custom assets that feel personalized.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **TOPO ABM Scale Framework.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Force Management MEDDICC.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **ITSMA — Account-Based Marketing.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.

## When to Use
- "Build ABM at scale"
- "Create industry cluster ABM"
- "Semi-custom ABM campaigns"
- "Scale our ABM beyond named accounts"

## Step-by-Step Process

### Phase 1: Account Clustering
Group accounts by commonality:
- **Industry cluster:** All fintech, all healthcare, all manufacturing
- **Use case cluster:** All companies buying for pipeline gen, all buying for enrichment
- **Trigger cluster:** All companies that just raised, all with new CRO, all hiring RevOps
- **Tech stack cluster:** All on Salesforce, all on HubSpot, all running Clay
- **Competitor cluster:** All current users of a specific competitor

### Phase 2: Cluster-Specific Campaign Design
Per cluster, build:
- **Pain point narrative:** Industry-specific challenge, regulatory pressure, market shift
- **Proof points:** 2-3 case studies from the same industry/use case
- **Persona messaging:** CFO, CRO, VP Sales, RevOps — each gets industry-contextualized value prop
- **Objection library:** The top 5 objections specific to this cluster

### Phase 3: Semi-Custom Assets
- **Industry landing page:** Variant of your homepage with industry-specific hero/social proof
- **Cluster email sequence:** 5-touch sequence with industry-specific openers + proof
- **LinkedIn content calendar:** 4-week cadence tailored to cluster themes
- **Cluster webinar:** Industry panel or use case deep-dive
- **Direct mail / gifts:** Physical asset (book, report) — coordinate via `strategic-gifting` (Sendoso/Postal); no logo swag

### Phase 4: Coordinated Execution
- **Week 1:** LinkedIn connection + content engagement
- **Week 2:** Direct mail arrives + email Touch 1 (reference the mailer)
- **Week 3:** Email Touch 2 + LinkedIn DM + SDR call
- **Week 4:** Webinar invite + personal outreach to registrants

### Phase 5: Measurement by Cluster
Track per cluster: coverage %, engagement rate, meeting rate, pipeline created,
win rate, ACV. Kill clusters that underperform after 60 days; double down on winners.

## Output Format
Cluster playbook with: cluster definitions, per-cluster campaign brief, asset production
plan, execution calendar, and measurement dashboard.



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

- TOPO ABM Scale Framework: apply only the part that directly improves the requested deliverable.
- Force Management MEDDICC: apply only the part that directly improves the requested deliverable.
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
- abm-strategy, abm-1-to-1, abm-1-to-many, cold-email-strategy, landing-pages

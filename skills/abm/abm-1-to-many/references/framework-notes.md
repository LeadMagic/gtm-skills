# Abm 1 To Many — Framework Notes

Use these references to ground outputs in named, repeatable methodology.

## Primary Frameworks

- **TOPO Programmatic ABM.** TOPO's 1:many tier (50-200+ accounts) relies on automation at every stage: ICP scoring for account selection, template-based personalization with merge fields, automated multi-channel cadences, and lookalike expansion from proven accounts. The key constraint: personalization must scale through data, not human effort.

- **Clay Automation Patterns.** Clay's enrichment waterfall is the operational backbone of programmatic ABM. Pattern: ICP filter → multi-provider enrichment (LeadMagic, Apollo, LinkedIn) → dynamic variable injection (company name, industry stat, tech stack signal) → CRM push with clay_status tracking. The quality gate is the enrichment QA threshold — incomplete data breaks personalization at scale.

- **ITSMA — Account-Based Marketing.** ITSMA distinguishes programmatic ABM by measurement: 1:many programs optimize for engagement breadth (account coverage, touch volume, reply rate) while 1:1 optimizes for depth (deal velocity, ACV). The marketing automation platform (HubSpot, Marketo) handles programmatic ABM, while the CRM handles 1:1.

## Operating Assumptions

- 1:many targets 50-200+ accounts where the personalization threshold is data-driven merge fields, not manual research.
- Automation is the differentiator: if you're manually building each campaign, it's 1:few, not programmatic ABM.
- Success metrics: account coverage rate, engagement rate per account, meeting conversion from target list, pipeline velocity.
- Fail modes: enrichment gaps produce "Hi {first_name}" errors that kill credibility; stale account lists (quarterly refresh minimum).

## Agent Use

Before final output, cite which framework shaped the recommendation and identify any assumptions that need user confirmation. Confirm which automation platform (Clay, HubSpot, Outreach) will execute the programmatic workflow.

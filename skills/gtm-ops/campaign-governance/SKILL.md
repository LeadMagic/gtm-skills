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
  frameworks: [Marketing Ops Governance Framework, SiriusDecisions Campaign Hierarchy]
---

# Campaign Governance

## Overview
Campaign governance is the unsexy foundation of marketing measurement. Without
enforced naming conventions and UTM parameters, your attribution data is garbage,
your ROI reports are fiction, and you can't answer "which campaigns actually work."
This skill builds the governance framework.

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

## Related Skills
- gtm-operations, campaign-analytics, attribution, crm-integration, gtm-metrics

---
name: gtm-tool-cost-model
description: >-
  GTM tool cost modeling — per-seat licensing, usage-based fees, cloud infra,
  enrichment credits, annual vs monthly contracts, and fully-loaded RevOps stack
  TCO. Use when budgeting GTM tools, calculating cost per rep, vendor renewal
  negotiation, or stack ROI. Triggers on: "GTM tool budget", "tool cost calculation",
  "SaaS stack TCO", "licensing costs", "per seat cost", "enrichment credits cost",
  "cloud costs GTM", "vendor spend model".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.2.0"
  author: LeadMagic
  category: gtm-ops
  tags: [tool-cost, budget, tco, licensing, revops, vendor-spend]
  related_skills:
    - gtm-spend-management
    - revops-tech-stack
    - financial-modeling
    - vendor-contracts
    - solo-founder-gtm
    - tool-selection-stack
  frameworks:
    - "Ben Murray (The SaaS CFO) — SaaS vendor and OpEx modeling"
    - "David Skok — Unit economics and CAC"
    - "Scott Brinker — MarTech stack proliferation"
    - "Jason Lemkin (SaaStr) — GTM spend at ARR stages"
---

# GTM Tool Cost Model

## Overview

GTM tool spend hides in **per-seat**, **credit**, **platform**, and **cloud** lines —
and renewals jump 15–30% year two if nobody models TCO. The mistake: approving
tools from demos without a **fully-loaded cost per rep** or **cost per $1M ARR**.
This skill builds finance-ready tool budgets: licensing, usage, implementation,
and infra — tied to ARR stage and headcount.

Stack design → `revops-tech-stack`. Contract terms → `vendor-contracts`.
P&L integration → `financial-modeling`. **Operational spend** (Ramp, approvals,
vendor roster) → `gtm-spend-management`.

## When to Use

- "Calculate our GTM tool costs"
- "Budget for CRM + enrichment + sequencer"
- "Cost per SDR/AE for tools"
- "Model Clay credits vs headcount"
- "Renewal negotiation data"
- "TCO for Salesforce vs HubSpot"

## Authoritative Foundations

- **Ben Murray (SaaS CFO).** Model vendor spend as % of ARR and per departmental head.
- **David Skok.** Tool spend should ladder into CAC — if stack CAC > benchmark, fix before adding tools.
- **Scott Brinker.** Consolidation reduces redundant MarTech tax.
- **Jason Lemkin.** Typical GTM spend bands by ARR stage (directional).

## Step-by-Step Process

### Phase 1: Inventory Categories

| Category | Cost models | Examples |
|---|---|---|
| **CRM** | Per seat + platform | HubSpot, Salesforce, Attio |
| **Enrichment** | Credits / API calls | LeadMagic, Clay, ZoomInfo |
| **Sequencing** | Per mailbox/seat | Outreach, Salesloft, Instantly |
| **Data / intent** | Subscription + seats | 6sense, Bombora |
| **Conversation intel** | Per seat + recording | Gong, Chorus |
| **Marketing automation** | Contacts tier + seats | HubSpot MA, Marketo |
| **Product analytics** | MTU / events | Amplitude, Mixpanel |
| **Cloud / integration** | Usage | AWS, n8n cloud, Zapier tasks |
| **Support** | Per agent | Zendesk, Intercom |

Load `references/cost-model-templates.md` for formulas.

### Phase 2: Build Line Items

For each tool document:

```
Annual cost = platform fee
            + (seats × seat price × 12)
            + (estimated credits × unit price)
            + implementation (amortize 3 years)
            + integration maintenance (hours × rate)
```

**Hidden costs:** Salesforce SI, HubSpot onboarding, Clay consultant, API overages, sandbox fees, premium support.

### Phase 3: Stage Benchmarks (% of ARR)

| ARR | Typical GTM tool spend | Notes |
|---|---|---|
| <$1M | 3–8% ARR | Lean stack; founder tools |
| $1–5M | 5–12% ARR | First CRM Pro, enrichment |
| $5–20M | 8–15% ARR | Gong, intent, marketing hub |
| $20M+ | 10–18% ARR | Enterprise CRM, data platform |

### Phase 4: Cost Per Rep

```
Fully loaded tool cost per AE =
  (CRM seat + sequencer + enrichment allocation + Gong + intent share)
  ÷ number of quota carriers
```

Target: **<$500/mo** per AE at SMB; **$800–1500/mo** at enterprise motion.

### Phase 5: Credit-Based Tools

| Tool type | Model |
|---|---|
| Enrichment API | $/verified email, $/company enrich |
| Clay | Credits per row × monthly rows |
| LLM in stack | Tokens × workflows/month |

Build **sensitivity table:** 1x, 2x, 3x volume.

### Phase 6: Cloud & Integration

- n8n self-host vs cloud: instance + execution count
- Webhook middleware, data warehouse (Snowflake/BigQuery) for RevOps
- Allocate **20% overhead** for integration maintenance if no RevOps FTE

### Phase 7: Renewal Negotiation

- Multi-year discount (10–20% typical)
- Seat true-down rights
- Credit rollover caps
- Co-terming vendors to fiscal year

### Phase 8: Operationalize Spend (Ramp)

TCO is the plan; **Ramp + vendor register** is actuals:

1. Load `gtm-spend-management` → vendor-spend-register + ramp-card-policy
2. Map each TCO line to virtual card or bill pay
3. Enforce spend-approval-matrix before new vendors
4. Monthly: Ramp actuals vs tool-cost-sheet variance

## Output Format

- Tool inventory spreadsheet structure (`templates/tool-cost-sheet.md`)
- Annual TCO by category
- Cost per rep / cost per $1M ARR
- 12-month cash flow (monthly vs annual contracts)
- Renewal negotiation summary

## Quality Check

- [ ] All cost types: seat, platform, credits, implementation, cloud
- [ ] Headcount growth scenario (+3 AEs) modeled
- [ ] Credit tools have volume sensitivity
- [ ] % of ARR calculated
- [ ] Redundant tools flagged for consolidation
- [ ] Contract renewal dates listed

## Common Pitfalls

1. **CRM seat creep.** Unused sales seats. Fix: quarterly true-down audit.
2. **Clay credits surprise.** Fix: cap rows + monitor weekly.
3. **Annual prepay all tools.** Cash crunch. Fix: stagger renewals.
4. **Ignoring implementation.** SF $50K year 1 missing from budget.
5. **No allocation to CS/marketing.** Shared tools need cost split.

## Execution Artifacts

- `references/cost-model-templates.md` — formulas and benchmarks
- `references/licensing-models.md` — seat vs usage vs platform
- `templates/tool-cost-sheet.md` — budget template
- `references/framework-notes.md`
- `templates/output-template.md`
- `scripts/check-output.py`

## Related Skills

- `revops-tech-stack` — what to buy
- `financial-modeling` — OpEx integration
- `vendor-contracts` — renewal terms
- `solo-founder-gtm` — lean stack by MRR
- `crm-toolkit` — CRM tier costs
- `gtm-spend-management` — Ramp, vendor roster, approvals

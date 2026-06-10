---
name: gtm-spend-management
description: >-
  GTM spend management — Ramp corporate cards, virtual cards per vendor, SaaS
  vendor roster, tool spend approvals, bill pay, accounting sync, and shadow-IT
  cleanup. Use when setting up Ramp, governing GTM tool purchases, tracking vendor
  renewals, or controlling per-rep software spend. Triggers on: "spend management",
  "Ramp setup", "corporate card GTM", "vendor spend", "SaaS spend governance",
  "tool purchase approval", "virtual card per vendor", "Brex vs Ramp", "zombie
  subscriptions", "vendor roster".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: gtm-ops
  tags: [spend-management, ramp, vendor-spend, saas-governance, revops, finance, procurement]
  related_skills:
    - gtm-tool-cost-model
    - revops-tech-stack
    - vendor-contracts
    - financial-modeling
    - campaign-governance
    - strategic-gifting
    - tool-selection-stack
    - website-visitor-identification
  frameworks:
    - "Ben Murray (The SaaS CFO) — Vendor spend as % of ARR"
    - "Scott Brinker — MarTech consolidation before new spend"
    - "Ramp — Corporate cards, bill pay, spend controls"
    - "Jason Lemkin (SaaStr) — GTM spend discipline by stage"
---

# GTM Spend Management

## Overview

GTM tool spend leaks through **personal cards**, **auto-renewals nobody owns**,
and **one-off trials that become $800/mo**. Finance sees a Ramp statement;
RevOps sees 40 SaaS logos — neither has a **vendor roster** with owner, renewal
date, and cost per rep. The mistake: modeling TCO in a spreadsheet while
purchases bypass approval entirely.

This skill operationalizes spend: **Ramp** (or equivalent) for cards + bill pay,
**approval matrix** by dollar tier, **virtual card per vendor** for GTM tools,
and a living **vendor spend register** synced to `gtm-tool-cost-model`.

TCO math → `gtm-tool-cost-model`. Contract terms → `vendor-contracts`.
Stack audit → `revops-tech-stack`. **Annual GTM budget (canonical opEx home):**
`references/gtm-budget-playbook.md` — this skill owns **vendor/tool lines** inside that budget.

## When to Use

- "Set up Ramp for GTM tools"
- "Who approves new SaaS purchases?"
- "Track vendor renewals and spend"
- "Virtual card for Clay / Gong / HubSpot"
- "Clean up zombie subscriptions"
- "GTM spend governance policy"
- "Brex vs Ramp for startup"
- "Bill pay for annual SaaS renewals"

## Authoritative Foundations

- **Ben Murray (SaaS CFO).** Vendor spend should be visible as % of ARR; assign
  departmental owners; review monthly — not only at renewal panic.
- **Scott Brinker.** Consolidate before you approve new MarTech — every new card
  swipe should pass stack overlap check (`revops-tech-stack`).
- **Ramp.** Corporate cards + virtual cards + spend limits + accounting sync +
  bill pay for invoices — single control plane for GTM OpEx.
- **Jason Lemkin.** Early-stage: lean stack; growth-stage: formalize procurement
  before seat creep compounds.

## Step-by-Step Process

### Phase 1: Spend Control Plane (Ramp)

Load `references/ramp-playbook.md`.

| Capability | GTM use |
|---|---|
| **Physical card** | Events, travel, ad hoc |
| **Virtual card per vendor** | HubSpot, Clay, Gong — locked merchant |
| **Spend limits** | Per user / per department / per card |
| **Receipt policy** | Required >$25; auto-match to accounting |
| **Bill pay** | Annual SaaS invoices (Salesforce, ZoomInfo) |
| **Accounting sync** | QuickBooks, NetSuite, Xero — map GL codes |

**Ramp vs Brex (directional):**

| Factor | Ramp | Brex |
|---|---|---|
| Bill pay + AP | Strong | Strong |
| Accounting integrations | Broad | Broad |
| Spend policies | Granular | Granular |
| Stage fit | Seed–enterprise | Seed–enterprise |

Pick one control plane — do not split GTM spend across two card programs.

### Phase 2: Vendor Spend Register

Master list: `templates/vendor-spend-register.md`

Every GTM SaaS line item:

| Field | Why |
|---|---|
| Vendor | Legal name |
| Owner | RevOps / marketing / sales leader |
| Cost model | Seat / credit / platform |
| Annual $ | From `gtm-tool-cost-model` |
| Payment method | Ramp virtual card # / bill pay |
| Renewal date | 90-day alert |
| Auto-renew | Y/N + notice days |
| Seats active vs paid | True-down flag |
| Bowtie stage | `revops-tech-stack` mapping |

### Phase 3: Approval Matrix

Template: `templates/spend-approval-matrix.md`  
Policy: `references/spend-governance.md`

| Annual spend | Approver | Required docs |
|---|---|---|
| <$2K | Manager + RevOps | 1-line business case |
| $2K–$10K | VP Sales / CMO + Finance | Stack overlap check |
| $10K–$50K | CRO/COO + Finance | TCO sheet + contract review |
| >$50K | CEO + board if material | `vendor-contracts` full procurement |

**Rules:**

- No new GTM tool without **owner** and **CRM integration plan**
- Trials must expire or convert — calendar kill date
- Shared cards forbidden — named virtual cards only

### Phase 4: GTM Tool Spend Categories

Map Ramp GL / accounting classes:

| Class | Examples | Owner |
|---|---|---|
| `GTM-Sales-Tools` | CRM, sequencer, Gong | RevOps |
| `GTM-Data` | Enrichment, Clay, **visitor ID / intent** (Clearbit/Breeze, RB2B, 6sense, Leadfeeder) | RevOps |
| `GTM-Marketing` | Ads, MA, events | Marketing |
| `GTM-Gifting` | Sendoso, Alyce | ABM / marketing |
| `GTM-Cloud` | AWS, n8n, warehouse | Engineering / RevOps |

Per-rep allocation: `gtm-tool-cost-model` cost-per-AE ÷ actual headcount monthly review.

### Phase 5: Virtual Card Architecture

Template: `templates/ramp-card-policy-gtm.md`

| Pattern | Setup |
|---|---|
| **One card per vendor** | Merchant lock; finance sees vendor in feed |
| **Department budget card** | Marketing ads — monthly cap |
| **Per-rep discretionary** | Rare; $50/mo max for trials only |
| **Gifting card** | Sendoso; monthly cap per `strategic-gifting` |

Rotate virtual card numbers on vendor churn or employee offboard.

### Phase 6: Renewal & Zombie Cleanup

**Quarterly spend review** (RevOps + Finance):

1. Export Ramp + vendor register
2. Flag: no login 90d, duplicate category, auto-renew <90d
3. True-down seats (`gtm-tool-cost-model`)
4. Negotiate via `vendor-contracts` before auto-renew hits

**Zombie signals:** Card charge with no owner; tool not in CRM integration map;
duplicate enrichment vendors.

### Phase 7: Ramp + Stack Audit Loop

```
New purchase request
  → revops-tech-stack overlap check
  → gtm-tool-cost-model TCO line
  → spend-approval-matrix sign-off
  → Ramp virtual card issue OR bill pay
  → vendor-spend-register update
  → renewal calendar 90/30/7 alerts
```

## Output Format

- Spend governance policy summary
- Vendor spend register (filled)
- Ramp card map (vendor → card → limit → owner)
- Approval matrix with thresholds
- Quarterly cleanup report (zombies, renewals, true-downs)

## Quality Check

- [ ] Single card program (Ramp or equivalent) for GTM OpEx
- [ ] Every SaaS vendor in register with owner + renewal date
- [ ] Virtual cards or bill pay — no shared credentials
- [ ] Approval thresholds documented and enforced
- [ ] Accounting sync with GTM GL classes
- [ ] Linked to TCO model (`gtm-tool-cost-model`)
- [ ] Quarterly zombie + renewal review scheduled

## Common Pitfalls

1. **Ramp without register.** Pretty dashboards; nobody owns Gong renewal. Fix: vendor-spend-register mandatory.
2. **Personal card reimbursement.** Shadow spend invisible to TCO. Fix: policy — GTM tools only on Ramp.
3. **One mega card for all SaaS.** Can't true-down or attribute. Fix: per-vendor virtual cards.
4. **Approve tools outside stack audit.** MarTech tax. Fix: Brinker overlap check before swipe.
5. **Ignore credit-based overages.** Clay/API surprise. Fix: weekly usage alert at 80% cap.
6. **Auto-renew without 90-day calendar.** Fix: Ramp + register reminders; `vendor-contracts` review.

### Phase 4b: Visitor ID Vendor Roster Entries

Register deanonymization vendors under `GTM-Data`:

| Vendor | ID level | Typical tier | Owner |
|---|---|---|---|
| Clearbit / HubSpot Breeze | Company | $$–$$$ | RevOps / Marketing |
| RB2B | Person | $$ per ID | RevOps / Sales |
| 6sense / Demandbase | Company (ABM) | $$$$ | Marketing / RevOps |
| Leadfeeder / Dealfront | Company | $–$$ | Marketing |
| Warmly / Koala | Person + company | $$–$$$ | Sales / RevOps |

Vendor comparison + pilot scorecard:
`website-visitor-identification/references/visitor-id-vendor-comparison.md`,
`website-visitor-identification/templates/visitor-id-vendor-eval-scorecard.md`.

**Approval rule:** Person-level vendors require privacy checklist completion
(`visitor-id-privacy-gtm.md`) before spend approval.

## Execution Artifacts

- `references/framework-notes.md`
- `templates/output-template.md`
- `scripts/check-output.py`
- `references/ramp-playbook.md` — Ramp setup for GTM stacks
- `references/spend-by-stage.md` — ARR-stage tool + payroll guardrails (canonical table)
- `references/gtm-budget-playbook.md` — **annual budget canonical** (repo root; vendor section here)
- `templates/annual-gtm-budget-worksheet.md` — budget worksheet
- `website-visitor-identification/references/visitor-id-vendor-comparison.md` — Intent vendor roster reference
- `references/spend-governance.md` — Policies, thresholds, compliance
- `references/spend-by-stage.md` — Tool unlock order tied to ARR / scale gates
- `references/saas-vendor-roster.md` — Roster maintenance SOP
- `templates/vendor-spend-register.md` — Master vendor inventory
- `templates/spend-approval-matrix.md` — Who approves what
- `templates/ramp-card-policy-gtm.md` — Card-per-vendor map

## Related Skills

- `website-visitor-identification` — visitor ID vendor tiers and privacy gates
- `gtm-tool-cost-model` — TCO formulas and cost-per-rep
- `revops-tech-stack` — Consolidation before new spend
- `vendor-contracts` — Procurement and renewal negotiation
- `financial-modeling` — OpEx in P&L
- `campaign-governance` — Marketing spend caps
- `strategic-gifting` — Gifting spend limits on Ramp

---
name: crm-toolkit
description: >-
  CRM operations anchor — HubSpot, Salesforce, and Attio selection, contacts vs
  leads object model, platform blueprints, enrichment integration, implementation
  partners, pipeline design, and data hygiene. Use when choosing a CRM, setting
  up Attio/HubSpot/Salesforce, resolving Lead vs Contact architecture, or hiring
  CRM implementation help. Triggers on: "CRM setup", "HubSpot vs Salesforce",
  "Attio vs HubSpot", "contacts vs leads", "Salesforce leads", "CRM migration",
  "CRM implementation partner", "CRM blueprint".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "2.1.0"
  author: LeadMagic
  category: tools
  tags:
    - crm
    - hubspot
    - salesforce
    - attio
    - contacts-vs-leads
    - revops
    - pipeline
    - enrichment
  related_skills:
    - crm-integration
    - hubspot-setup
    - salesforce-setup
    - attio-setup
    - pipeline-management
    - leadmagic-toolkit
    - clay-toolkit
    - n8n-toolkit
    - revops-tech-stack
    - hiring-agencies
    - saas-outcomes
  frameworks:
    - "Winning by Design — Bowtie lifecycle"
    - "HubSpot — Lifecycle Stage Model"
    - "Salesforce — Lead/Account/Contact/Opportunity"
    - "Marc Benioff — V2MOM, trust selling, land-and-expand, customer success"
    - "Attio — Programmable object + list model"
---

# CRM Toolkit

## Overview

Most CRM failures are **architecture mistakes**, not missing features: wrong platform
for stage, Lead/Contact confusion, enrichment synced both ways, or fifteen pipeline
stages nobody inspects. This skill is the **anchor** for CRM work in gtm-skills —
selection, object model, platform blueprints, partners, and hygiene — with
rollout delegated to `hubspot-setup`, `salesforce-setup`, and `attio-setup`.

**Tool vs process:** `tools/crm-toolkit` = config reference and blueprints.
`automation/crm-integration` + platform setup skills = operating model and rollout.

## When to Use

| Request | Start here | Then load |
|---|---|---|
| "Which CRM should we use?" | `references/crm-selection.md` | `saas-outcomes` if bootstrap vs venture |
| "Contacts vs leads in Salesforce" | `references/contacts-vs-leads.md` | `salesforce-setup` |
| "Set up HubSpot pipeline" | `references/hubspot-blueprint.md` | `hubspot-setup` |
| "Set up Attio" | `references/attio-blueprint.md` | `attio-setup` |
| "Migrate HubSpot → Salesforce" | `references/contacts-vs-leads.md` + blueprints | `references/implementation-partners.md` |
| "CRM agency / SI partner" | `references/implementation-partners.md` | `hiring-agencies` |
| "Enrichment → CRM" | Enrichment section below | `clay-toolkit`, `leadmagic-toolkit` |

Trigger phrases: "CRM toolkit", "CRM setup", "Attio setup deep", "HubSpot vs
Attio", "Salesforce leads", "contact vs lead", "CRM partner", "RevOps agency CRM"

## Authoritative Foundations

- **Winning by Design — Bowtie.** Model pre- and post-sale in CRM: not pipeline-only.
- **HubSpot.** Single Contact + lifecycle stages — no separate Lead object.
- **Salesforce.** Lead quarantine → convert → Account + Contact + Opportunity.
- **Marc Benioff (Salesforce).** V2MOM alignment, trust-based enterprise selling,
  land-and-expand in CRM, customer success as revenue function — `references/benioff-enterprise-playbook.md`.
- **Attio.** Flat objects; qualification via attributes and **lists as queues**.

## Step-by-Step Process

### Phase 1 — Operating Model (before software)

Load `crm-integration` if not done. Minimum:

- [ ] GTM motion defined (inbound, outbound, PLG, hybrid)
- [ ] 5–7 deal stages with Goal + Exit Criteria (`pipeline-management`)
- [ ] Owner per stage (SDR vs AE vs CS)
- [ ] Dedupe key: email (people), domain (companies)

### Phase 2 — Platform Selection

Use `references/crm-selection.md` scorecard.

| ARR / team | Default recommendation |
|---|---|
| <$1M ARR, founder-led | Attio or HubSpot Starter |
| $1–10M ARR, sales-led | HubSpot Pro |
| $10M+ ARR, territories | HubSpot Enterprise or Salesforce |
| Enterprise procurement | Salesforce |

### Phase 3 — Contacts vs Leads

**Mandatory read:** `references/contacts-vs-leads.md`

| Platform | Model |
|---|---|
| Salesforce | Lead object optional but default for SDR + inbound quarantine |
| HubSpot | Lifecycle stages on Contact — never duplicate "lead" records |
| Attio | `status` on People + dynamic lists — no conversion ceremony |

### Phase 4 — Platform Blueprint

| Platform | Blueprint | Setup skill |
|---|---|---|
| HubSpot | `references/hubspot-blueprint.md` | `hubspot-setup` |
| Salesforce | `references/salesforce-blueprint.md` | `salesforce-setup` |
| Attio | `references/attio-blueprint.md` | `attio-setup` |

Index: `references/platform-setup-index.md`

### Phase 5 — Enrichment Integration

**One-direction:** Clay / LeadMagic → CRM. Never two-way Clay ↔ CRM sync.

| Event | Pattern |
|---|---|
| Contact/Person created | Webhook or workflow → enrich → write properties |
| Inbound form | Enrich before assignment |
| Quarterly hygiene | Re-verify email; refresh firmographics on Tier A accounts |

Skills: `leadmagic-toolkit` (verify), `clay-toolkit` (waterfall), `n8n-toolkit` (routing).

### Phase 6 — Implementation Partners

If estimated config > 40 hours or Salesforce net-new:

1. Document process (`pipeline-management`, `crm-integration`)
2. Read `references/implementation-partners.md`
3. Run 90-day pilot with scorecard (`hiring-agencies`)

### Phase 7 — Enterprise Motion (Salesforce / land-expand)

When enterprise or NRR-led growth is the motion, load `references/benioff-enterprise-playbook.md`:

- V2MOM cascade from company vision → GTM measures (`gtm-leadership`)
- Land opp + expansion opps on same Account (`templates/land-expand-account-plan.md`)
- CS health, renewal, and success criteria in CRM — not pipeline-only

### Phase 8 — Data Hygiene

| Rule | Implementation |
|---|---|
| No person without email | Required field / validation |
| No open deal without amount + close date | Stage validation |
| Duplicate detection | Email match; domain for companies |
| Stale deals | 60d same stage → task or auto-close policy |
| Enrich on create | Default for all inbound |

## Platform Comparison (Summary)

| | HubSpot | Salesforce | Attio |
|---|---|---|---|
| Best for | SMB–mid market, marketing+sales | Enterprise, complex GTM | Startups, API-first, PLG assist |
| Lead model | Lifecycle on Contact | Lead → convert | status + lists |
| Admin load | Low–medium | High | Low |
| Marketing | Native | Separate clouds | External / webhooks |
| Implementation | Partner optional | Partner required | Self-serve + contractor |

Full matrix: `references/crm-selection.md`

## Output Format

Deliver based on request:

- **CRM selection memo:** Scorecard + recommendation + 12-month path
- **Object model doc:** Contacts vs leads decision with field map
- **Blueprint package:** Stages, properties, workflows for chosen platform
- **Migration plan:** Source → target mapping, hygiene gates, parallel run
- **Partner RFP:** Scope from `references/implementation-partners.md` checklist

## Quality Check

- [ ] Platform choice tied to ARR, motion, and admin capacity
- [ ] Contacts vs leads documented — no hybrid confusion
- [ ] 5–7 stages with exit criteria
- [ ] Enrichment one-direction into CRM
- [ ] Partner engagement only if process documented
- [ ] Setup skill named for rollout (`hubspot-setup`, etc.)

## Common Pitfalls

1. **Salesforce Leads in HubSpot.** HubSpot uses lifecycle — don't create parallel objects.
2. **CRM before process.** Stages undefined → reps invent their own. Fix `pipeline-management` first.
3. **Two-way Clay sync.** Conflicts and overwritten fields. One-way push only.
4. **Salesforce at $500K ARR.** Admin tax without RevOps owner. Use Attio/HubSpot until $5M+.
5. **Agency without playbook.** Partners configure chaos faster. Document first.

## Execution Artifacts

| File | Use |
|---|---|
| `references/crm-selection.md` | HubSpot vs Salesforce vs Attio |
| `references/contacts-vs-leads.md` | Lead/Contact architecture |
| `references/hubspot-blueprint.md` | HubSpot fields + workflows |
| `references/salesforce-blueprint.md` | SF objects + Lead convert |
| `references/attio-blueprint.md` | Attio lists + status model |
| `references/implementation-partners.md` | SIs, RevOps agencies, RFP |
| `references/platform-setup-index.md` | Skill routing table |
| `references/benioff-enterprise-playbook.md` | V2MOM, trust, land-expand, CS in CRM |
| `templates/land-expand-account-plan.md` | Account expansion whitespace |
| `references/framework-notes.md` | Framework anchors |
| `templates/output-template.md` | Deliverable structure |
| `scripts/check-output.py` | Section validator |

## Related Skills

- `crm-integration` — lifecycle, field ownership, sync rules
- `hubspot-setup` / `salesforce-setup` / `attio-setup` — rollout
- `pipeline-management` — stage design
- `hiring-agencies` — agency pilot for RevOps/CRM
- `saas-outcomes` — bootstrap vs venture; CRM tier by path
- `revops-tech-stack` — full GTM stack context

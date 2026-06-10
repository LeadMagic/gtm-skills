---
name: deal-desk
description: >-
  Structure deals, pricing, and proposals — pricing model selection, discount
  guidance, business case construction, and negotiation strategy. Use when
  structuring a deal, building a pricing proposal, negotiating, or creating a
  business case. Triggers on: "deal desk", "pricing", "proposal", "negotiation",
  "discount", "business case", "ROI case", "deal structure", or any pricing/financial
  request in a sales context.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: sales-revops
  tags: [deal-desk, pricing, proposals, negotiation, business-case]
  related_skills: [pricing-strategy, roi-calculator, pipeline-management, transparency-selling, expansion-selling, crm-toolkit, customer-onboarding, security-assessments, soc2-compliance, data-privacy-compliance, revenue-team-onboarding]
  frameworks: [Ramanujam Monetizing Innovation, ValueSelling Framework, Force Management Command of the Message, Todd Caponi Transparency Sale, Jason Lemkin SaaStr SOC2 as enterprise sales gate, Vanta Trust Center sales handoff, Eunice Buhler G2 sales-legal alignment, Ironclad deal desk swimlanes, a16z commercial counsel hiring]
---

# Deal Desk

## Overview

Deal structuring is where strategy meets money. The difference between a
deal that closes at list price and one that gets discounted 40% is usually
not the product — it's how value was communicated and the business case
was constructed.

This skill covers pricing model selection (Ramanujam), business case
building (ValueSelling Framework), discount authority frameworks, and
negotiation strategy grounded in Command of the Message value articulation.

## When to Use

- "Structure this deal"
- "Build a business case for [prospect]"
- "What pricing model should we propose?"
- "How much discount should we offer?"
- "Prepare for a pricing negotiation"
- "Create a proposal for [company]"

## Authoritative Foundations

Madhavan Ramanujam's Monetizing Innovation: pricing should be designed
around customer willingness-to-pay, not cost-plus or competitor-minus.
The 2x2 model (price sensitivity × differentiation) determines which
pricing model fits.

ValueSelling Framework: every deal conversation should ladder up to
quantifiable business impact. "What's this worth to you?" is the
question that determines pricing power.

Force Management Command of the Message: premium pricing is defendable when value
differentiation is clear and provable.

## Step-by-Step Process

### Phase 1: Intake

Ask the user:
1. Deal size and deal stage
2. Prospect's budget range (if known)
3. Competitors in the deal and their pricing
4. Champion strength and economic buyer access
5. Timeline and urgency

### Phase 2: Pricing Model Selection

| Model | Best For | When to Use |
|---|---|---|
| Per-seat | Collaborative tools, productivity | Usage scales with team size |
| Usage-based | API, data, compute | Value scales with consumption |
| Tiered (Good/Better/Best) | Most SaaS | Clear upgrade path |
| Flat-rate | Simple tools, SMB | Low complexity, fast decisions |
| Custom / Enterprise | $50K+ ACV | Complex needs, procurement |

### Phase 3: Business Case Construction

Template: `templates/business-case.md` — current state cost, future value,
investment, ROI, risk of inaction. Deep ROI → `roi-calculator`.

### Phase 4: Discount Authority

| Discount Level | Approval Required | When Justified |
|---|---|---|
| 0-10% | Rep discretion | Standard negotiation |
| 10-20% | Manager approval | Multi-year commit, competitive pressure |
| 20-30% | VP/CRO approval | Strategic account, land-and-expand |
| 30%+ | CEO approval | Platform deal, partnership, exceptional |

Never discount without getting something in return: multi-year commit,
case study permission, reference call, logo rights, or expansion commitment.

Document every request in `templates/discount-authority.md`. Land-and-expand
deals: `crm-toolkit` land-expand-account-plan — protect expansion ACV.

### Phase 5: Enterprise Security & Customer Data (GTM)

Enterprise deals often stall on **security review** and **data exchange** —
not price. This is GTM coordination, not infra engineering.

**When security review enters the deal:**

| Stage | AE / deal desk action |
|---|---|
| Discovery | Ask when procurement runs security; share trust center link |
| Evaluation | Prefer synthetic POC data; log questionnaire receipt same day |
| Negotiation | DPA + order form in parallel; don't discount to "skip" security |
| Closed-won | Hand off artifacts + data boundaries to CS |

Full timing playbook → `references/security-questionnaire-deal-guide.md`
( repo root ). SOC 2 / pen test *implementation* → `soc2-compliance`,
`security-assessments`.

**Legal GTM (commercial velocity):** Eunice Buhler (G2 GC) — legal as deal
accelerator via availability, published SLAs, and "get to yes" commercial mindset.
Ironclad CLM — situational approval swimlanes, legal-pre-approved MSA variants,
CRM-native order forms. Canonical → `references/legal-gtm-playbook.md` (Pattern 29).
DPA timing aligned with `references/gtm-data-exchange-playbook.md` — enterprise
DPA during negotiation, before production data intake.

**Customer data exchange (what reps request from buyers):**

- Minimum data for the next milestone — not "send everything"
- Approved channels only: customer-owned upload, secure file share, in-app
  import — **never email attachments or Slack files with PII**
- Go/no-go before production data: contract scope, DPA status, retention date

Canonical SOP → `references/gtm-data-exchange-playbook.md`. Checklist →
`templates/customer-data-exchange-checklist.md`.

**Red flags that kill deals:** full CRM export in discovery; AE solo-filling
security questionnaires; POC on production when sandbox exists; no handoff of
what data was already exchanged.

## Output Format

Deal structure document with pricing recommendation, business case, discount
framework, and negotiation strategy.

## Quality Check

- [ ] Pricing model matched to customer's usage pattern and value drivers
- [ ] Business case includes both current-state cost and future-state value
- [ ] ROI figures are conservative and sourceable
- [ ] Discount authority rules documented and enforced
- [ ] Every discount tied to a concession from the prospect

## Common Pitfalls

1. **Discounting without exchange.** A 20% discount with nothing in return
   is just leaving money on the table. Always trade.

2. **Vague business case.** "You'll save money" isn't a business case.
   "Your team spends 40 hours/week on [task] at $X/hour = $Y/year. Our
   solution reduces that to 10 hours. Annual savings: $Z. Payback: 4 months."

3. **Premature pricing discussion.** Discussing price before establishing
   value makes every number sound expensive. Value first, price second.

4. **One price for everyone.** Different segments, different willingness-
   to-pay. A 10-person startup and a 500-person enterprise shouldn't see
   the same pricing.

## Execution Artifacts

- `references/framework-notes.md`
- `templates/output-template.md`
- `scripts/check-output.py`
- `templates/business-case.md` — ROI business case structure
- `templates/discount-authority.md` — Approval + trade documentation
- `templates/customer-data-exchange-checklist.md` — Pre/on/post-sale data exchange gates
- `references/legal-gtm-playbook.md` — Eunice Buhler + Ironclad commercial counsel for sales (Pattern 29)
- `references/gtm-data-exchange-playbook.md` — Canonical customer data exchange SOP (repo root)
- `references/security-questionnaire-deal-guide.md` — When security review enters the deal (repo root)

## Related Skills

- **pricing-strategy**: Overall pricing model design
- **roi-calculator**: Detailed ROI calculation and business case tools
- **pipeline-management**: Track deals through negotiation and close
- **customer-onboarding**: Post-sale data handoff and implementation boundaries
- **soc2-compliance**, **security-assessments**: Building trust artifacts (founder-led)
- **revenue-team-onboarding**: Rep security hygiene before customer contact

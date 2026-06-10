---
name: strategic-gifting
description: >-
  Strategic B2B gifting — John Ruhlin Giftology, Sendoso/Alyce/Reachdesk platforms,
  buyer gifting compliance, ABM tier budgets, gifting sequences, and CRM tracking.
  Use when sending executive gifts, direct mail, Sendoso campaigns, or designing
  gift plays for target accounts. Triggers on: "Sendoso", "Giftology", "strategic
  gifting", "corporate gifts sales", "ABM gifts", "direct mail gift", "buyer gifting",
  "physical touchpoint", "gift play", "Alyce", "Reachdesk".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: abm
  tags: [gifting, giftology, sendoso, direct-mail, abm, buyer-experience]
  related_skills:
    - abm-strategy
    - abm-1-to-1
    - abm-1-to-few
    - multi-thread-orchestration
    - account-selection
    - pipeline-management
    - cold-email-strategy
    - event-driven-outreach
    - gtm-spend-management
  frameworks:
    - "John Ruhlin — Giftology (strategic relationship gifting)"
    - "Sendoso — Sending Platform for revenue teams"
    - "ITSMA ABM — Tier-based investment model"
    - "Winning by Design — Bowtie physical touchpoints"
---

# Strategic Gifting

## Overview

"Send a mug, call it ABM" wastes budget and annoys buyers. **Strategic gifting**
is a **relationship signal** — proof you researched the person, respect their
policy, and timed the touch to the deal journey. **John Ruhlin's Giftology**
teaches go-deep-not-wide: one remarkable gift beats 100 logo pens. **Sendoso**
(and peers Alyce, Reachdesk, Postal.io) operationalize logistics — address
verification, warehouse, CRM triggers — but **cannot replace** Giftology
personalization.

Gifting is **not** bribery, review incentives (see `review-platforms` ToS), or
a substitute for solving business pain. Use inside ABM programs (`abm-strategy`)
with tier budgets and compliance gates.

## When to Use

- "Set up Sendoso for sales"
- "Giftology playbook for enterprise"
- "What gift to send a CRO?"
- "ABM direct mail + gift sequence"
- "Buyer gift policy compliance"
- "Sendoso vs Alyce"
- "Gift to unblock deal" (usually: don't — diagnose first)
- "Post-close customer gift"

Do not use for **G2/review gift cards** — `review-platforms` (platform ToS).
Do not use for **customer advocacy rewards** at scale — `customer-marketing`.

## Authoritative Foundations

- **John Ruhlin — Giftology.** Relationship gifting: personalization, no logo,
  3-gift system (them / family / team), story-driven notes. Source: *Giftology*
  and Ruhlin Group methodology.
- **Sendoso.** Revenue sending platform: eGift, physical gifts, direct mail,
  CRM/MAP integrations, address confirmation, analytics. Use for **execution**
  after Giftology brief is written.
- **ITSMA ABM tiers.** Gift budget scales with 1-to-1 vs 1-to-few vs 1-to-many —
  never same playbook for Tier 1 and Tier 3.
- **Winning by Design Bowtie.** Physical touches bridge marketing → sales;
  post-close gifts support retention (right side of bowtie).

## Step-by-Step Process

### Phase 1 — Gift vs No Gift Decision

| Send gift when | Do NOT send |
|---|---|
| Tier 1/2 ABM account with research done | Cold outbound with no relationship |
| Post-discovery — reference their words | Active price negotiation |
| Post-close thank-you | Trying to "unstick" stalled deal (bribery) |
| Champion appreciation mid-cycle | Exceeds known company gift cap |
| Event no-show recovery (personal) | Generic holiday blast to list |

**Stalled deal?** Load `buyer-indecision` (JOLT) — not bigger gifts.

### Phase 2 — Giftology Principles (Ruhlin)

Load `references/giftology-ruhlin.md`.

1. **Go deep, not wide** — budget into fewer remarkable gifts
2. **3-gift system** — recipient / family / team
3. **Personalization > price** — hobby, alma mater, conversation callback
4. **Story is the gift** — object delivers the narrative
5. **No logo** — swag is advertising, not gifting
6. **Handwritten note** — 3 sentences, references specific conversation

### Phase 3 — Platform Selection

Load `references/gifting-platforms.md`.

| Platform | Best for |
|---|---|
| **Sendoso** | Salesforce/HubSpot teams, mixed eGift + physical, SDR/AE self-serve |
| **Alyce** | Enterprise compliance, recipient choice ("pick your gift") |
| **Reachdesk** | Global ABM, warehouse + marketplace |
| **Postal.io** | Direct mail + handwritten at scale |
| **Manual / local** | Tier 1 ultra-custom (Ruhlin-style concierge) |

**Integrations:** CRM task on send, attribution field `gift_sent_date`, amount,
story note. One-direction log — never automate gift without AE approval on Tier 1.

### Phase 4 — Budget by ABM Tier

Load `references/gifting-by-tier.md`.

| Tier | Accounts | $/account/year | Gift types |
|---|---:|---:|---|
| 1 (1-to-1) | 5–15 | $500–2,000 | Custom physical, team experiences |
| 2 (1-to-few) | 15–50 | $150–500 | Cluster mailer + modest personal |
| 3 (1-to-many) | 50–200+ | $25–75 | eGift, book, useful tool — no junk swag |

Track **cost per meeting held** and **cost per opp created** — not sends.

### Phase 5 — Gifting Sequence Timeline

Load `references/gifting-sequence.md`.

| Moment | Gift? | Example |
|---|---|---|
| Pre-first meeting | No | — |
| Post-discovery (D3–5) | Small personal | Reference call detail |
| Mid-evaluation W3–4 | Team gift | Catered lunch, team asset |
| Negotiation / legal | No | — |
| Post-close D1 | Family / thank you | Ruhlin Gift 2 |
| 90d post-close | Check-in gift | Retention bowtie |

Coordinate with email: mail arrives **before** email references it (abm-1-to-few Week 2 pattern).

### Phase 6 — Compliance & Buyer Policies

Load `references/gift-compliance.md`. Gifting spend on Ramp → `gtm-spend-management`
(GTM-GIFT card, monthly cap per tier).

- Ask champion: "What's your gift policy limit?"
- Federal / industry rules (gov, healthcare, finance) — often **zero**
- Never exceed disclosed cap; document in CRM
- Finance may require gift disclosure on vendor forms — `vendor-contracts`
- **Anti-bribery:** gift must be defensible as relationship marketing, not quid pro quo

### Phase 7 — Sendoso Campaign Build

Load `references/sendoso-playbook.md` + `templates/sendoso-campaign.md`.

1. Create **Touch** aligned to ABM play (not standalone blast)
2. Enable address confirmation for physical
3. Manager approval workflow for >$X
4. Personalization fields: `first_name`, `account`, `note` from AE
5. Trigger: manual (Tier 1) or CRM workflow (Tier 3 eGift)
6. SLA: SDR contacts within 24h of delivery scan

### Phase 8 — Multi-Stakeholder Gifting

For buying committees (`multi-thread-orchestration`):

| Role | Gift approach |
|---|---|
| Champion | Personal Giftology (Gift 1) |
| Economic buyer | Conservative; often eGift or book — check policy |
| Blocker | Usually no gift — solve concern |
| End users | Team gift (Gift 3) after pilot success |

Never gift only champion while ignoring EB on enterprise deals.

### Phase 9 — Measurement

| Metric | Target (directional) |
|---|---|
| Delivery → meeting booked | Track per tier |
| Gift-assisted opp creation | CRM field required |
| Cost per meeting | <1/10 expected ACV |
| Policy violations | Zero |

## Output Format

| Request | Deliverable |
|---|---|
| Tier 1 gift plan | `templates/gift-brief.md` per stakeholder |
| Sendoso setup | `templates/sendoso-campaign.md` |
| ABM gifting program | Budget + sequence + compliance |
| Post-close retention | Bowtie gift calendar |

Run `scripts/check-output.py` before delivery.

## Quality Check

- [ ] Giftology personalization — not logo swag blast
- [ ] Company gift policy checked or documented
- [ ] No gift during active negotiation
- [ ] Timeline matches deal stage (not pre-first-meeting)
- [ ] CRM log: what, when, why, story
- [ ] Budget matches ABM tier
- [ ] Platform choice justified (Sendoso vs manual)
- [ ] SDR/AE follow-up SLA within 24h of delivery

## Common Pitfalls

1. **Sendoso without strategy.** Automated Starbucks cards to cold lists. Fix: ABM tier + Giftology brief first.
2. **Logo swag.** Fix: Ruhlin — no logo on relationship gifts.
3. **Gift to unstick deal.** Fix: JOLT / deal desk — business problem.
4. **Ignore gift cap.** Fix: ask champion; log in CRM.
5. **No follow-up.** Gift arrives; nobody calls. Fix: 24h SLA + task in CRM.
6. **Same gift Tier 1 and Tier 3.** Fix: `references/gifting-by-tier.md`.

## Execution Artifacts

| File | Use |
|---|---|
| `references/giftology-ruhlin.md` | Core principles + 3-gift system |
| `references/sendoso-playbook.md` | Sendoso setup and workflows |
| `references/gifting-platforms.md` | Sendoso vs Alyce vs Reachdesk |
| `references/gifting-by-tier.md` | ABM budget matrix |
| `references/gifting-sequence.md` | When to send / not send |
| `references/gift-compliance.md` | Policies, anti-bribery |
| `templates/gift-brief.md` | Per-recipient plan |
| `templates/gift-crm-log.md` | CRM field spec |
| `templates/sendoso-campaign.md` | Campaign checklist |
| `references/framework-notes.md` | Quick anchors |
| `templates/output-template.md` | Deliverable structure |
| `scripts/check-output.py` | Validator |

## Related Skills

- `abm-1-to-1` — Strategic account context
- `abm-1-to-few` — Direct mail + email coordination
- `abm-strategy` — Tier model and measurement
- `multi-thread-orchestration` — Committee gifting
- `buyer-indecision` — Stalled deals (not gifts)
- `event-driven-outreach` — Event follow-up gifts
- `pipeline-management` — Stage-appropriate touches

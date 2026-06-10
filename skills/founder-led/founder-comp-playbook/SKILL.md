---
name: founder-comp-playbook
description: >-
  Founder guide to GTM compensation — what you can afford, how to set OTE and
  equity, budget guardrails, valuing packages for candidates, and negotiation
  scripts when cash is tight. Covers hiring first AE/SDR/VP and founder-side
  offer/counter-offer tactics. Use when a founder asks how to comp sales hires,
  negotiate offers, explain equity, or defend quota math. Triggers on: "founder
  comp", "how much to pay first AE", "negotiate sales offer as founder", "comp
  budget startup", "what equity to offer", "candidate wants more money", "can't
  afford VP Sales salary", "founder hiring compensation".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: founder-led
  tags: [founder, compensation, negotiation, hiring, equity, budget, offers]
  related_skills:
    - gtm-role-descriptions
    - gtm-recruiting
    - executive-compensation
    - solo-founder-gtm
    - sales-team-building
    - equity-management
    - financial-modeling
    - saas-outcomes
  frameworks:
    - "Jason Lemkin (SaaStr) — When founders can afford GTM hires"
    - "Mark Roberge — Quota:OTE and sales machine economics"
    - "Sam Jacobs (Pavilion) — Revenue leader comp norms"
    - "Bridge Group — SaaS compensation benchmarks (2025–2026)"
    - "Betts Recruiting — Comp Engine and unicorn seller premium"
    - "David Skok — Unit economics and payroll as % of revenue"
---

# Founder Comp Playbook

## Overview

Founders lose hires in two ways: **underpaying with mystery** (candidate ghosts
after RepVue check) or **overpaying with hero OTE** (runway dies in 9 months).
Cash-constrained founders must negotiate with **total package math** — OTE,
quota, equity, ramp, and trajectory — not emotional number-matching.

This skill is the **founder-specific comp layer**: what you can afford by ARR
stage, how to value equity honestly, employer negotiation scripts, and when to
walk. **Canonical GTM comp strategy** → `executive-compensation/references/gtm-compensation-strategy.md`
(Pattern 35). IC bands + templates → `gtm-role-descriptions`. Close mechanics →
`gtm-recruiting`. VP/CRO clauses → `executive-compensation`.

**Not legal advice.** Offer letters → `employment-compliance`.

## When to Use

- "How much should I pay my first AE?"
- "Candidate wants $20K more — what do I do?"
- "How do I explain our equity grant?"
- "Can we afford a VP Sales?"
- "Founder comp budget for sales team"
- "Negotiate without matching Google cash"
- "What quota goes with $140K OTE?"
- "Post-acquisition retention comp" / "earn-out employment package"

## Authoritative Foundations

- **Jason Lemkin.** Founder closes 10–20 deals before first AE. VP Sales before
  ~$2M ARR: high failure rate. Don't hire title before motion.
- **Mark Roberge.** Quota:OTE ~5:1 — if you raise OTE, raise quota proportionally
  or you overpay for under-delivery.
- **David Skok.** Payroll + S&M as % of ARR must fit unit economics; comp is not
  separate from CAC.
- **Bridge Group / RepVue (2025–2026).** Candidates arrive with crowdsourced
  attainment data — your posted range must match reality.
- **Sam Jacobs / Pavilion.** Executive hires expect multi-gate variable and peer
  calibration — not handshake promises.

## Step-by-Step Process

### Phase 1 — Can You Afford This Hire?

Load `references/founder-comp-budget.md`. Quick guardrails:

| Company ARR | Max fully-loaded sales payroll % ARR | Typical first hire |
|---|---|---|
| <$500K | Founder only + contractors | No FTE AE yet |
| $500K–$1.5M | 15–25% ARR | 1 full-stack AE |
| $1.5M–$5M | 20–35% ARR | AE + SDR or 2 AEs |
| $5M–$15M | 25–40% ARR | Manager + pod |
| $15M+ | Board-modeled | VP / CRO |

**Fully loaded** = base + employer taxes + benefits + variable at target + tool cost per rep (`gtm-tool-cost-model`).

**Bootstrap rule:** If hire pushes runway below 12 months without revenue lift, delay or use contractor (`hiring-contractors`).

### Phase 2 — Set the Range (Before Sourcing)

Use `references/comp-benchmarks-2026.md` (synced with **gtm-role-descriptions** H1 2026 bands).

| Hire | Publish in JD | Internal ceiling |
|---|---|---|
| First AE | $120–150K OTE | +10% for proven unicorn |
| SDR #1 | $60–75K OTE | Match market, not discount |
| VP Sales | $220–280K OTE | +Pavilion band check |

**Founder mistake:** Posting "$80–200K OTE" — signals chaos. Post narrow band.

### Phase 3 — Value the Package (Show the Math)

Candidates care about **expected earnings**, not headline OTE.

```
Expected cash = base + (variable × expected attainment %)
```

| Component | Founder must explain |
|---|---|
| Quota | $700K ARR for $140K OTE (5:1) |
| Team attainment | "68% hit quota last year" (honest) |
| Ramp | 50% Q1, 75% Q2 quota |
| Equity | 0.5% FD, 4yr/1yr cliff, current $8M post → $40K paper |
| Signing bonus | Bridge if they leave forfeited bonus |

Template: `templates/founder-offer-walkthrough.md`

**Equity honesty:** Share last 409A or post-money valuation range, option count,
FD%, and refresh policy. Hiding FD% kills trust.

### Phase 4 — Founder Negotiation Levers (Cash Tight)

Priority order when candidate pushes:

| Lever | Cost to company | Candidate value |
|---|---|---|
| **Lower quota** (with lower OTE) | Low | High — earnability |
| **Steeper ramp** Q1–Q2 | Medium | High |
| **Equity + refresh commitment** | Dilution | High at seed–B |
| **Signing bonus** (one-time) | Cash | Medium |
| **Territory / ICP tier** | Low | High for AE |
| **Title / path to lead** | Low | Medium |
| **Base increase without quota fix** | High ongoing | Short-term |

**Never:** Raise OTE without quota adjustment (breaks 5:1).  
**Never:** Promise "we'll fix comp after 90 days" without writing it.

Scripts: `references/founder-negotiation-scripts.md`

### Phase 5 — Candidate Asks (Playbook)

| Ask | Founder response |
|---|---|
| "+$15K OTE" | "Let's model quota at 5:1 — that's $75K more quota. Or we hold OTE and add 0.05% equity + $10K signing." |
| "Match current $160K OTE" | "Share comp plan. We'll match cash if attainment ≥100% last 4Q and motion fits." |
| "More equity" | Show FD% table by role (`references/comp-benchmarks-2026.md`). Offer refresh at 12 mo on attainment. |
| "Guaranteed year-one" | Signing bonus only — not guaranteed variable. |
| "Competing offer deadline Friday" | Pre-draft counters before finals; respond in 24h with written package. |

Walk away if: won't share attainment, demands 2× market with no proof, needs enterprise comp for SMB motion.

### Phase 6 — Executive Hires (VP / CRO)

Founders often **cannot** compete on cash alone.

| Stage | Founder move |
|---|---|
| $3–8M ARR | VP not CRO; equity-heavy; system-building gates |
| $8–15M ARR | Pavilion peer comp check; board approval |
| Bootstrap profitable | Profit-share or bonus vs inflated base |

Load `executive-compensation` — never handshake CRO packages.

### Phase 7 — Founder Receiving Comp (Advisor / Acqui / Side Role)

When **founder is the candidate** (advisor, operating partner, post-exit):

- Anchor on **cash + equity + time** — not vanity title
- Advisor: 0.1–0.5% over 2yr vest or $2–10K/mo cash retainer
- Negotiate: pro-rata, information rights, acceleration on change of control
- `advisor-recruitment`, `equity-management`

## Output Format

| Request | Deliverable |
|---|---|
| Affordability | Payroll % ARR model + runway impact |
| First hire comp | OTE band + quota + equity table |
| Negotiation | Counter-offer script + lever matrix |
| Candidate walkthrough | `templates/founder-offer-walkthrough.md` filled |
| VP package | Redirect to `executive-compensation` + board memo |

## Quality Check

- [ ] Payroll % ARR within stage guardrails
- [ ] Quota:OTE ~5:1 documented
- [ ] Published JD range matches written offer
- [ ] Equity FD% and valuation context shared
- [ ] Ramp schedule in offer
- [ ] Team attainment disclosed (or first-hire ramp explicit)
- [ ] Written offer within 48–72h of verbal yes

## Common Pitfalls

1. **Hire before motion.** Comp can't fix unproven product. Fix: founder closes 10–20 first.
2. **OTE vanity contest.** $180K OTE / $900K quota beats $200K / $2M quota. Fix: show math.
3. **Equity hand-wave.** "We'll be generous later." Fix: grant numbers in writing.
4. **Geo bait-and-switch.** Offer remote then cut 20%. Fix: band in JD.
5. **Skip RepVue check.** Candidates know your reputation. Fix: align posted vs paid.

## Execution Artifacts

- `references/framework-notes.md`
- `templates/output-template.md`
- `scripts/check-output.py`
- `../../management-leadership/executive-compensation/references/gtm-compensation-strategy.md` — master playbook (cross-link)
- `../../management-leadership/executive-compensation/references/comp-by-role-stage.md` — stage matrix
- `../../management-leadership/executive-compensation/templates/ote-calculator-template.md` — quota math
- `references/founder-comp-budget.md` — ARR-stage payroll guardrails
- `references/founder-negotiation-scripts.md` — employer scripts by scenario
- `references/comp-benchmarks-2026.md` — dated ranges (sync with role-descriptions)
- `templates/founder-offer-walkthrough.md` — candidate-facing package explainer
- `templates/founder-counter-offer.md` — structured counter template
**Cross-skill:** `saas-outcomes/references/exit-metrics-matrix.md` (payroll vs ARR at exit scale)
### Post-Close Retention (Earn-Out Context)
When sale includes earn-out + employment, model **total package** — base, bonus,
rollover, earn-out — not salary alone. Load `exiting-company/references/negotiating-earn-out.md`:
- Prefer **retention bonus** (time-based) separate from performance earn-out
- Negotiate role/title before close; comp band should match `founder-comp-budget.md` guardrails
- At-will termination with full earn-out forfeiture → walk or re-trade (counsel required)
- Worksheet: `exiting-company/templates/earn-out-term-sheet-review.md`

## Related Skills

- `gtm-role-descriptions` — JD + IC comp templates
- `gtm-recruiting` — sourcing, close timeline, inclusive hiring
- `executive-compensation` — VP/CRO clauses
- `solo-founder-gtm` — when to hire + lean stack
- `financial-modeling` — runway impact of payroll
- `saas-outcomes` — bootstrap vs venture comp philosophy
- `exiting-company` — earn-out and retention package negotiation

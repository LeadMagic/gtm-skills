---
name: exiting-company
description: >-
  Prepare a SaaS company for acquisition or exit — valuation drivers by buyer
  type (strategic, PE, bootstrap), due diligence readiness, EBITDA vs ARR
  multiples, and 12–24 month exit timeline. Use when planning an exit, preparing
  for acquisition, or maximizing company value for a future sale. Triggers on:
  "exit strategy", "sell company", "acquisition prep", "M&A", "due diligence",
  "company valuation", "exit planning", "PE acquisition", "bootstrap exit".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: founder-led
  tags: [exit, acquisition, m-and-a, valuation, due-diligence, pe, bootstrap-exit]
  related_skills:
    - saas-outcomes
    - saas-metrics-calculator
    - financial-modeling
    - fundraising-strategy
    - equity-management
    - soc2-compliance
    - investor-updates
  frameworks:
    - "David Skok — Unit economics and diligence metrics"
    - "Jason Lemkin (SaaStr) — Growth efficiency, burn multiple, acquisition operator lens"
    - "Nathan Latka (GetLatka) — Bootstrap M&A under $10M ARR"
    - "Ben Murray (The SaaS CFO) — EBITDA bridge for PE buyers"
    - "KeyBanc SaaS Survey — Private ARR multiples"
    - "Eunice Buhler — Legal GTM handoff for deal terms (not legal advice in-skill)"
---

# Exiting a Company

## Overview

Companies are bought, not sold. The best exits happen when a strategic or financial
buyer identifies you as the solution to their problem — not when you announce
a sale. This skill covers **valuation drivers by buyer type**, diligence-ready
metrics, and the 12–24 month runway most exits require.

**Not legal or tax advice.** Use qualified counsel for transactions, earnouts,
and cap table mechanics (`equity-management`, `legal-for-founders`).

## When to Use

- "How do I prepare my company for acquisition?"
- "What's my company worth to PE vs strategic?"
- "Build an exit strategy"
- "Prepare for due diligence"
- "Maximize acquisition value"
- "Sell my bootstrapped SaaS"
- "Negotiate earn-out" / "earnout terms" / "retention bonus vs earn-out"
- "Walk away from LOI" / "seller note" / "rollover equity in acquisition"

Do not use for path choice (bootstrap vs VC) — use `saas-outcomes` first.
Do not use for metric calculation — use `saas-metrics-calculator`.

## Authoritative Foundations

- **David Skok.** Unit economics gate every exit. LTV:CAC <3x or payback >18
  months compress multiples in diligence — fix before process.
- **Jason Lemkin (SaaStr).** Burn multiple and growth efficiency matter as much
  as ARR scale; inefficient growth gets discounted at LOI.
- **Nathan Latka (GetLatka).** Sub-$10M ARR bootstrapped SaaS has real
  acquisition liquidity; weight churn, growth, and clean books over VC headline multiples.
- **Ben Murray (The SaaS CFO).** PE buyers model EBITDA and FCF; bridge from
  unit economics → P&L → EBITDA multiple (`financial-modeling/references/unit-economics-exit-bridge.md`).
- **KeyBanc SaaS Survey.** Private ARR multiple bands by growth tier — use as
  range, not quote.

## Step-by-Step Process

### Phase 0: Exit Optionality Gate

Score whether exit is realistic vs distraction before M&A prep. Load
`saas-outcomes/references/exit-potential-scorecard.md`:

- **<3.0 avg:** Fix retention and concentration — exit is distraction
- **3.0–3.9:** Passive readiness only (metrics pack, relationships)
- **≥4.0:** Proceed with Phase 2–4 readiness

### Phase 1: Valuation Drivers by Buyer Type

Load `references/valuation-drivers.md` and `saas-outcomes/references/exit-metrics-matrix.md`.

| Buyer type | Metrics they weight | Red flags |
|---|---|---|
| **Strategic** | Product fit, customer overlap, talent | Customer concentration; IP gaps |
| **PE** | EBITDA, NRR >110%, predictable renewals, efficient GTM | High burn; founder dependency |
| **Acqui-hire / small M&A** | Team, tech (Latka sub-$10M ARR) | No product velocity |
| **Bootstrap acquirer** | Profitability, clean cap table, low churn | Messy books; cap disputes |

**Scale thresholds (planning):** $1M ARR acqui-hire possible; $5M strategic
interest; $10M+ serious conversations; $20M+ banker-led if inbound.

**Multiples (indicative):** Strategic 5–15x ARR; PE 8–12x ARR or 15–25x EBITDA;
bootstrap 4–8x ARR or 3–6x SDE. See `templates/valuation-sensitivity-table.md`.

### Phase 2: Due Diligence Package

Prepare before anyone asks. Load `references/due-diligence-metrics-pack.md`.

**Financial:** 36 mo P&L; ARR bridge; cohort NRR/GRR; fully loaded CAC/LTV  
**Legal:** Cap table; IP assignments (contractors critical); material contracts  
**Technical:** SOC2 or equivalent; architecture; DR  
**Commercial:** Concentration; churn reasons; documented playbook  

### Phase 3: 12–24 Month Runway

Load `references/buyer-readiness-checklist.md` and `templates/exit-readiness-scorecard.md`.

| Phase | Focus |
|---|---|
| Months 1–6 | Cap table, IP, metrics pack, concentration plan |
| Months 7–12 | NRR trend, GTM repeatability, founder dependency ↓ |
| Months 13–18 | Market signals, partnerships, data room 80% |
| Months 19–24 | Counsel, LOI, diligence (60–90 days), close (30–60 days) |

### Phase 4: Exit Options

| Option | Valuation basis | Typical timeline |
|---|---|---|
| Strategic acquisition | ARR × growth + synergy | 6–12 months |
| PE (majority) | EBITDA + ARR growth | 4–8 months |
| Bootstrap sale (MicroAcquire/GetLatka) | ARR/SDE, churn | 3–6 months |
| Acqui-hire | Team value | 2–4 months |
| IPO | $100M+ ARR, Rule of 40 | 12–18 months |

Cross-ref: `saas-outcomes/references/bootstrap-vs-vc-paths.md` for hold vs sell.

### Phase 5: Deal Structure — Earn-Outs & Deferred Consideration

When LOI includes earn-out, seller note, or rollover — **model cash at close first**,
not headline EV. Load `references/negotiating-earn-out.md`:

| Topic | Founder sensibility |
|---|---|
| **When fair** | Real diligence gap; metrics you already run; want to stay 18–24 mo |
| **When trap** | >40% at risk; buyer controls OpEx; vague metrics; at-will + forfeiture |
| **Typical at risk** | 15–40% mid-market; bootstrap sales often lower earn-out % |
| **Walk** | Cash at close below floor; >50% at risk without audit/carve-outs |

**Negotiation artifacts:** `templates/earn-out-term-sheet-review.md` (worksheet),
`templates/valuation-sensitivity-table.md` (hold vs sell + deferred scenarios).

**Related structures (high level):**
- **Retention bonus** — time-based; prefer separate from performance earn-out
- **Rollover equity** — upside alignment; understand liquidation prefs
- **Seller financing** — only with security, market interest, clear subordination

**Legal handoff:** Contract language → M&A counsel. Commercial velocity →
`deal-desk/references/legal-gtm-playbook.md` (Pattern 29). **Not legal advice in this skill.**

Reconcile structure norms → `references/benchmark-reconciliation.md` (Earn-Out vs Upfront Cash).

## Output Format

Exit readiness assessment with: buyer-type fit, valuation range (low/base/high
with method named), diligence gaps, 24-month timeline, scorecard summary.

## Quality Check

- [ ] Buyer type identified (strategic vs PE vs bootstrap)
- [ ] Valuation method matches buyer (ARR vs EBITDA vs SDE)
- [ ] Metrics pack items mapped to gaps
- [ ] No guaranteed valuation claims — ranges and assumptions only
- [ ] Cross-refs to `saas-metrics-calculator`, `financial-modeling`, `saas-outcomes`

## Common Pitfalls

1. **Missing IP assignments.** Contractor IP gaps kill deals — fix in month 1–6.
2. **Customer concentration.** One logo >20% ARR → un-acquirable or deep discount.
3. **Founder dependency.** Acquirer buys key-person risk, not a company.
4. **Optimizing ARR before NRR.** Diligence strips low-quality revenue.
5. **Shopping the company.** Inbound from relationships beats outbound "for sale."
6. **Headline EV without cash-at-close math.** Earn-out traps look like big deals. Fix: `earn-out-term-sheet-review.md` before signing.
7. **Accepting EBITDA earn-out without carve-outs.** Buyer can cut marketing and void payout. Fix: `negotiating-earn-out.md` governance section.

## Execution Artifacts

- `references/valuation-drivers.md` — strategic vs PE criteria, EBITDA vs ARR, adjustment table
- `references/buyer-readiness-checklist.md` — 24-month prep timeline
- `references/due-diligence-metrics-pack.md` — standard metrics export for M&A
- `references/negotiating-earn-out.md` — earn-out playbook, levers, decision tree, anti-patterns
- `references/framework-notes.md` — named frameworks and agent routing
- `templates/exit-readiness-scorecard.md` — 1–5 scoring worksheet
- `templates/valuation-sensitivity-table.md` — ARR, EBITDA, DCF, hold vs sell
- `templates/earn-out-term-sheet-review.md` — founder worksheet for LOI/term sheet
- `templates/output-template.md` — deliverable shell
- `scripts/check-output.py` — lightweight validator

**Cross-skill artifacts:** `saas-outcomes/references/exit-potential-scorecard.md`, `saas-outcomes/references/exit-metrics-matrix.md`, `saas-outcomes/references/bootstrap-founder-playbook.md`, `financial-modeling/references/unit-economics-exit-bridge.md`, `references/benchmark-reconciliation.md`

## Related Skills

- `saas-outcomes` — path choice, exit-metrics matrix, bootstrap vs VC
- `saas-metrics-calculator` — formulas and benchmarks
- `financial-modeling` — unit-economics-exit-bridge, DCF
- `fundraising-strategy` — alternative to exit if metrics support raise
- `soc2-compliance` — enterprise diligence readiness
- `equity-management` — cap table cleanup

## ⚠️ Disclaimer

This skill provides general informational guidance based on publicly available frameworks and operator experience. It is NOT legal advice, accounting advice, tax advice, or financial advice.

Consult qualified professionals for your specific situation — attorneys for legal and M&A matters, CPAs for tax and accounting. This skill does not create a professional-client relationship.

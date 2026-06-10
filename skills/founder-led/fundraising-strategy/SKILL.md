---
name: fundraising-strategy
description: >-
  Complete fundraising strategy for B2B SaaS founders. Use when preparing to
  raise seed/Series A, deciding VC vs bootstrapped path, building pitch deck,
  running a fundraise process, evaluating term sheets, or planning fundraising
  timeline. Covers SAFE, priced rounds, and bootstrapper alternatives.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.2.0"
  author: LeadMagic
  category: founder-led
  tags: [fundraising, venture capital, SAFE, term sheet, pitch deck, seed, series-a, bootstrapper]
  related_skills: [financial-modeling, investor-updates, pitch-deck-builder, pricing-strategy, cap-table-management, saas-outcomes, saas-metrics-calculator, vc-outreach]
  frameworks:
    - "Jason Lemkin (SaaStr) — ARR-based fundraising benchmarks"
    - "Christoph Janz (Point Nine) — SaaS napkin to unicorn"
    - "Brad Feld — Venture Deals (term sheet mechanics)"
    - "Mark Suster (Upfront Ventures) — VC relationship building"
    - "Rob Walling — Stair Step Method (bootstrapper path)"
    - "Tyler Tringas (Calm Company Fund) — Bootstrapper-friendly shared earnings"
    - "Samir Kaji (Allocate) — Fundraising data and LP dynamics"
---

# Fundraising Strategy

## Overview

Fundraising is selling a piece of your company. The mistake: treating it like a
financing event instead of a sales process. You are selling equity in exchange
for capital, and like any sale, it has a funnel, close rate, and negotiation.
This skill covers the full fundraising motion — deciding whether to raise,
building pipeline, running the process, evaluating terms, and closing.

## Authoritative Foundations

- **Jason Lemkin (SaaStr).** 3x YoY at seed; burn multiple gates at A/B;
  VP Sales hiring ~$2M ARR.
- **Christoph Janz (Point Nine).** ARR napkin — stage-appropriate growth expectations.
- **David Skok.** Unit economics before scale — LTV:CAC, payback.
- **Rob Walling (TinySeed).** Bootstrap-first path; raise from strength at $1–2M ARR.
- **Brad Feld — Venture Deals.** Term sheet mechanics (not valuation advice).

Load `references/vc-milestone-gates.md` for round-by-round metric gates.

**Investor diligence:** Present **committed ARR bridge** (not bookings TCV) aligned with
`references/saas-mrr-accounting-nuances.md`. Clean books handoff → `references/saas-tax-founder-awareness.md`.
Annual budget scenario → `references/gtm-budget-playbook.md` + `financial-modeling`.

## When to Use

Trigger phrases: "fundraising strategy", "raise seed round", "Series A prep",
"pitch deck for investors", "SAFE vs priced round", "VC vs bootstrapped",
"how much should I raise", "term sheet evaluation", "investor pipeline"

## Should You Raise?

**Raise VC if:**
- Market is winner-take-most (network effects, data moats)
- You need capital to capture market before competitors
- Your growth rate can support VC expectations (3x+ YoY at seed, 2-3x at Series A)
- You're building a $1B+ outcome company
- You want/need the network, brand, and pressure of institutional capital

**Stay bootstrapped if:**
- Market is fragmented (many winners possible)
- You can reach profitability on customer revenue
- You value control and independence above growth speed
- Your lifestyle business can hit $5-20M ARR without outside capital
- You'd rather optimize for profit than valuation

**The middle path — "bootstrap first, raise later":**
- Build to $1-2M ARR on customer revenue
- Raise from a position of strength (not desperation)
- Keep most equity, raise on better terms
- This is increasingly common and fundable

**Bootstrap vs raise decision (canonical):** Load `saas-outcomes/references/bootstrap-vs-vc-paths.md`
and `saas-outcomes/references/bootstrap-founder-playbook.md` before starting a process.
Fill `saas-outcomes/templates/bootstrap-capital-plan.md` to test whether revenue can fund
the next 12 months without dilution.

**Sensibility:** Defaulting to VC without a $100M credible path often ends in down rounds
or founder replacement. Defaulting to bootstrap in winner-take-all markets burns the
window. Name one primary path in `saas-outcomes/references/end-goal-matrix.md`.

**Exit alternative to raise:** If growth is decelerating and inbound acquirers exist,
model hold vs sale (`financial-modeling`) before raising a "bridge" round.

## Fundraising Benchmarks (SaaStr)

| Stage | ARR Range | Raise Amount | Dilution | Growth Expected |
|---|---|---|---|---|
| Pre-Seed | $0-500K | $500K-2M | 10-15% | N/A (product/market) |
| Seed | $500K-2M | $2-5M | 15-20% | 3x+ YoY |
| Series A | $1-4M | $5-20M | 20-25% | 2-3x YoY |
| Series B | $5-15M | $20-50M | 15-20% | 2x+ YoY |

**The rule of 3x:** At seed, investors want to see you can 3x revenue in 12-18
months. If you're at $1M ARR, they need to believe you can hit $3M.

## Step-by-Step Process

### Phase 1: Preparation (4-6 weeks before first meeting)

**Must-have before you start:**
1. **Pitch deck** (12-15 slides, see pitch-deck-builder skill for structure)
2. **Financial model** (3-year projections, unit economics, hiring plan)
3. **Data room** (incorporation docs, cap table, customer contracts, financials, team bios, product roadmap)
4. **Target investor list** (20-50 funds, researched for fit)
5. **Warm introductions** (no cold emailing VCs — find mutual connections)

**Key metrics to have at your fingertips:**
- MRR/ARR growth (monthly, last 6 months)
- Net Revenue Retention (NRR) — above 100% is excellent
- CAC Payback Period (months) — under 12 is good, under 6 is great
- Gross Margin — 70%+ for SaaS
- Logo churn (monthly) — under 2% is good
- Magic Number (net new ARR / S&M spend) — above 1.0 is efficient

### Phase 2: Pipeline Building (Weeks 1-2 of active raise)

**Create a fundraising CRM** — track every investor:
- Fund name, partner name, check size, stage focus
- Thesis fit (why them specifically)
- Introduction source and status
- Meeting date, follow-up date
- Notes, concerns, next steps

**Pipeline strategy:**
- Batch first meetings into a 2-week window
- Tier investors: A (dream), B (strong fit), C (fallback)
- Meet B-tier first (practice), A-tier second (when you're sharp)
- Aim for 30-50 first meetings to close one round
- Expect 20-30% conversion from first meeting to partner meeting
- Expect 10-20% from partner meeting to term sheet

### Phase 3: The First Meeting (30 min)

**Your goal:** Get the second meeting. Not to close.

**Structure:**
1. **2 min — The hook:** "We're [company], we help [ICP] solve [pain]. We're at
   $X ARR growing Y% MoM with Z% NRR."
2. **15 min — The story:** Problem → Solution → Why Now → Traction → Team → Vision
3. **10 min — Q&A:** Answer directly. "I don't know" beats guessing.
4. **3 min — Next step:** "Based on this conversation, we'd love to continue.
   What's your process from here?"

**What VCs evaluate in 30 minutes:**
- Is this a big market? (TAM > $1B for VC-scale)
- Is the team exceptional? (Founder-market fit, grit, speed)
- Is there real traction? (Revenue, growth rate, retention, customer love)
- Is the timing right? (Why now, not 2 years ago or 2 years from now)
- Can I add value? (Network, expertise, portfolio fit)

### Phase 4: The Process (Weeks 3-8)

**Create momentum:**
- Schedule all partner meetings within a 1-week window if possible
- Create a sense of process: "We're in active conversations and expect terms by [date]"
- Update all interested investors simultaneously
- If one term sheet arrives, notify all others immediately: "We've received a term
  sheet. We'd love to include you in the process if you can move by [date]."

**Partner meeting prep:**
- Send updated metrics 24 hours before
- Prepare customer references (3-5 customers who'll take the call)
- Anticipate hard questions: competition, churn, CAC, market size, team gaps
- Have your ask ready: "We're raising $XM at $YM pre-money"

### Phase 5: Term Sheet Evaluation

**Key terms to negotiate:**
1. **Valuation** — pre-money vs post-money. Understand the difference.
2. **Liquidation preference** — 1x non-participating is standard. Anything above
   or "participating" reduces founder outcomes.
3. **Board composition** — At seed, founder-controlled board common. Series A,
   typical is 2 founders + 1 VC + 1 independent.
4. **Option pool** — Usually 10-20%. Dilutes founders, not VCs (pre-money pool).
   Push for smallest pool that covers your hiring plan.
5. **Pro-rata rights** — Standard for lead investor. Watch out for super pro-rata
   (right to invest 2x+ their ownership in future rounds).
6. **Protective provisions** — Veto rights on major decisions. Standard set is
   fine. Avoid veto on budget or hiring.
7. **Founder vesting** — 4-year vesting with 1-year cliff is standard. Push back
   on any acceleration terms that disadvantage you.

**Read Brad Feld's Venture Deals before signing anything.**

### Phase 6: Close

- Reference calls: Expect 5-10 customer references. Prep your references.
- Legal: Your attorney reviews. NOT their attorney.
- No-shop clause: 30-45 days standard. Push for 30.
- Announcement: Coordinate with VC. Don't announce until money is in the bank.

## SAFE vs Priced Round

**SAFE (Simple Agreement for Future Equity):**
- No valuation set now — converts at next priced round
- Usually has a valuation cap and/or discount
- No board seat, no governance rights
- Faster, cheaper legal process ($5-10K vs $30-50K)
- Common for pre-seed and seed
- Risk: over-raising on SAFEs creates a "valuation stack" that crushes Series A

**Priced Round:**
- Sets valuation and share price now
- Board seat, governance rights, investor protections
- More legal cost and time
- Usually Series A and beyond
- Signal: priced seed rounds command premium valuations

**The YC SAFE is the standard document.** Use it. Don't negotiate custom SAFE
terms unless you have leverage.

## Bootstrapper Fundraising Alternatives

- **Revenue-based financing:** Pipe, Capchase, FounderPath. Borrow against ARR.
- **Profit-sharing notes:** Calm Company Fund model. Share profits, not equity.
- **TinySeed / Calm Company Fund (Earnest):** Bootstrapper-friendly funds. Smaller checks,
  longer horizons, profitability-aligned terms. Cross-ref: `bootstrap-founder-playbook.md`.
- **Customer-funded growth:** Annual prepay discounts, implementation fees,
  marketplace models. Zero dilution.

## Output Format

```
FUNDRAISING STRATEGY

Stage: [Pre-Seed / Seed / Series A]
Current ARR: $X
Monthly Growth: X%

Raise Target: $X M at $Y M [pre/post]-money

Investor Pipeline:
- Tier A: [count] funds — [names]
- Tier B: [count] funds
- Tier C: [count] funds

Timeline:
- Prep complete: [date]
- First meetings: [date range]
- Partner meetings: [date range]
- Term sheets expected: [date]
- Close: [date]

Key Metrics:
- NRR: X%
- CAC Payback: X months
- Gross Margin: X%
- Magic Number: X

Term Sheet Priorities:
1. [top priority]
2. [second priority]
3. [acceptable to concede]
```

## Implementation Checklist

- [ ] Pitch deck is 12-15 slides, rehearsed, customized for each meeting
- [ ] Financial model includes 3-year projections with assumptions documented
- [ ] Data room is complete and organized
- [ ] Investor list is researched for thesis fit, not sprayed randomly
- [ ] Warm introductions secured for all Tier A targets
- [ ] Brad Feld's Venture Deals read cover to cover
- [ ] SAFE vs priced round decision made with legal counsel
- [ ] Reference customers prepped and available
- [ ] Fundraising CRM tracking every interaction

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Fundraising before you're ready.** If growth is under 10% MoM and retention
   is under 100% NRR, fix the business first. Raising won't fix product-market
   fit problems. Fix: Meet growth benchmarks before starting.

2. **Taking the first term sheet.** Unless it's from your dream investor with
   dream terms, create competitive tension. Fix: Batch your process so multiple
   VCs are evaluating simultaneously.

3. **Over-raising on SAFEs.** Multiple SAFE rounds with escalating caps create a
   "stack" — when your Series A prices below the highest cap, early SAFE holders
   get massive dilution protection at your expense. Fix: Limit SAFE rounds to 1-2
   before priced round.

4. **Neglecting the partner meeting.** First meeting is screening. Partner meeting
   is where the decision happens. Send updated metrics, prep references, and
   anticipate every hard question. Fix: Do a mock partner meeting with an
   experienced founder.

5. **Announcing before money hits the bank.** Term sheets fall through. Wires can
   take days. Fix: Wait until funds are in your account.



## ⚠️ Disclaimer

This skill provides general informational guidance based on publicly available frameworks and operator experience. It is NOT legal advice, accounting advice, tax advice, financial advice, insurance advice, or professional services advice.

Consult qualified professionals for your specific situation — attorneys for legal/equity matters, CPAs for tax and accounting, licensed brokers for insurance, and certified security assessors for compliance. This skill does not create a professional-client relationship. Use it as a starting point for research and preparation.

## Execution Artifacts

- `references/vc-milestone-gates.md` — metric gates by round
- `references/saas-mrr-accounting-nuances.md` — ARR definitions for diligence (repo root)
- `references/gtm-budget-playbook.md` — operating budget for data room (repo root)
- `references/saas-tax-founder-awareness.md` — CPA handoffs pre-close (repo root)
- `references/framework-notes.md` — routing index
- `templates/output-template.md` — deliverable shell
- `scripts/check-output.py` — deliverable validator

**Cross-skill (journey / exit):** `saas-outcomes/references/journey-stage-gates.md`, `saas-outcomes/references/bootstrap-vs-vc-paths.md`, `saas-outcomes/references/bootstrap-founder-playbook.md`, `saas-outcomes/templates/bootstrap-capital-plan.md`, `saas-outcomes/references/end-goal-matrix.md`, `saas-outcomes/templates/journey-planning-worksheet.md`, `financial-modeling/references/unit-economics-exit-bridge.md`, `saas-metrics-calculator/references/metric-definitions-exit-weight.md`, `exiting-company/references/buyer-readiness-checklist.md`, `exiting-company/references/negotiating-earn-out.md`, `references/benchmark-reconciliation.md`

## Related Skills

- `financial-modeling` — SaaS P&L, runway, scenario planning
- `investor-updates` — Monthly investor updates, metrics, narrative
- `pitch-deck-builder` — Slide-by-slide structure, narrative, speaker notes
- `pricing-strategy` — Tier design, monetization models
- `cap-table-management` — Equity, option pools, dilution modeling

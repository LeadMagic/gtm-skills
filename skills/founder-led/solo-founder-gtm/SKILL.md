---
name: solo-founder-gtm
description: >-
  Build lean GTM as a solo founder or bootstrapper — tool stacks by revenue stage,
  AI agents replacing headcount, when to make the first hire, bootstrapper
  economics, and the WbD GTM Index for self-assessment. Use when building GTM
  as a solo founder, bootstrapper, or small team. Triggers on: "solo founder",
  "bootstrapper GTM", "lean GTM", "founder sales", "DIY GTM", "when to hire",
  "founder tools", "bootstrapped stack", "product market fit", "PMF test",
  "when to scale", "scale too early", or any request about building GTM without
  a team.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.2.0"
  author: LeadMagic
  category: founder-led
  tags: [solo-founder, bootstrapper, lean, startup, gtm, tools]
  related_skills: [founder-comp-playbook, sales-team-building, founder-brand, tool-selection-stack, saas-metrics-calculator, gtm-tool-cost-model, gtm-spend-management, saas-outcomes, financial-modeling]
  frameworks: [Winning by Design GTM Index, SaaStr ACV Thresholds, David Skok Unit Economics, Sean Ellis PMF Survey, Rob Walling Bootstrap Path]
---

# Solo Founder GTM

## Overview

Solo founders don't need a sales team. They need a system. Before $1M ARR,
the founder IS the GTM motion — and that's the advantage. No coordination
overhead, no diluted message, no commission structure to manage. One person
who knows the product deeply selling to people who need it.

This skill builds lean GTM for founders: tool stacks at each revenue stage
($0-10K MRR through $50K+), AI agents replacing headcount, and clear
triggers for when to make the first hire. Track tool spend → `gtm-tool-cost-model`;
operationalize on Ramp → `gtm-spend-management`.

## When to Use

- "How do I do GTM as a solo founder?"
- "Build my bootstrapped sales stack"
- "When should I hire my first salesperson?"
- "What tools do I need at $X MRR?"
- "Replace SDR work with AI"
- "Run GTM without a team"
- "Lean GTM for bootstrappers"
- "Bootstrap founder path" / "bootstrap capital plan" / "when not to bootstrap"
- "Do we have product-market fit?"
- "When should we scale GTM spend / headcount?"

## Authoritative Foundations

- **Winning by Design GTM Index** — Self-assess your GTM maturity 1-10 across
  6 models: Revenue, Data, Math, Operating, Growth, GTM. Score below 6: fix
  fundamentals before scaling the team.
- **SaaStr (Jason Lemkin)** — ACV thresholds. Founder must personally close
  10-20 deals before hiring. VP Sales before $2M ARR: 70% failure rate.
- **David Skok** — Unit economics. CAC payback, LTV:CAC ratios by stage.
  Bootstrapped SaaS often hits 5-10x LTV:CAC organically.
- **Sean Ellis** — PMF survey: ≥40% "very disappointed" among active users signals
  must-have product. Run before scaling spend or hires (`pmf-testing-playbook.md`).
- **Rob Walling (TinySeed/MicroConf).** Bootstrap path: profitable growth,
  acquisition optionality without default VC. See `saas-outcomes/references/bootstrap-vs-vc-paths.md`
  and `saas-outcomes/references/bootstrap-founder-playbook.md`.
- **Tyler Tringas (Calm Company Fund).** Bootstrapper-friendly capital; profitability
  before blitz — pairs with `saas-outcomes/templates/bootstrap-capital-plan.md`.

## Step-by-Step Process

### Phase 1: Stage Assessment

Determine your revenue stage and GTM maturity. Align with company journey
(`saas-outcomes/references/journey-stage-gates.md`):

| Journey stage | MRR band | Focus |
|---|---|---|
| **PMF search** | $0–$10K MRR | Prove retention and pull — not infrastructure |
| **GTM fit** | $10–50K MRR | Document repeatable motion; founder still sells |
| **Scale** | $50K+ MRR | Add capacity — AI first, then people — only if scale gates pass |

**PMF search ($0-10K MRR):** Talk to customers, not tools. Run
`references/pmf-testing-playbook.md` and `references/pmf-signal-checklist.md`
before advancing. False PMF traps (one big customer, channel dependency) block scale.

**GTM fit ($10-50K MRR):** Document playbook. Still founder-led sales.
Score `references/scale-readiness-gates.md` before first AE hire.

**Scale ($50K+ MRR):** Hit ceiling of founder-led sales. If
`references/when-not-to-scale.md` stop signals are active — hold, do not hire.

### Phase 2: Tool Stack by Stage

**$0-10K MRR (~$100/mo):**
- Apollo ($59/mo): data + sequencing in one platform. No need for separate tools yet.
- Google Workspace (1-2 inboxes): $12/mo for sending.
- Calendly (free): scheduling.
- That's it. Every additional tool is distraction. Talk to customers.

**$10-50K MRR (~$250/mo):**
- Add: LeadMagic Email Validation (pay-per-use) — verify before sending.
- Add: LinkedIn Sales Nav ($99/mo) — research prospects.
- Add: HubSpot free CRM — track conversations.
- Optional: Clay ($149/mo) if doing significant list building.

**$50K+ MRR (~$500/mo):**
- Add: Smartlead or Instantly ($33-97/mo) — dedicated sequencer.
- Add: n8n (free self-hosted) — workflow automation.
- Add: 3-5 sending domains + inboxes ($75-150/mo).
- Optional: Clay Enterprise if running complex enrichment.

### Phase 3: AI Agents as Org

Before hiring anyone:

- **AI SDR** (11x, Artisan, or custom): handles prospecting research and
  first-draft outreach while you sleep
- **AI meeting prep**: researches attendees, builds discovery questions before
  every call
- **AI follow-up**: drafts post-call summaries and next-step emails
- **AI pipeline management**: updates CRM, flags deals needing attention

One founder + AI agents can outproduce a 3-person team at a fraction of the
cost. The founder does the human conversations. AI does everything else.

### Phase 4: Comp Budget Before First Hire

Before posting a JD, model **fully loaded cost** (base + taxes + benefits +
target variable + tools). Bootstrap guardrails (`founder-comp-playbook`):

| MRR / ARR | Max sales payroll % ARR | First hire OTE band (H1 2026) |
|---|---|---|
| $50K MRR (~$600K ARR) | 15–20% | Delay or contractor |
| $80K MRR (~$1M ARR) | 15–25% | 1 AE $120–150K OTE |
| $150K+ MRR (~$1.8M ARR) | 20–30% | AE + optional SDR |

**Negotiation:** Set +10% reserve before finals. Publish narrow comp range in JD —
candidates check RepVue. Tool cost per rep: `gtm-tool-cost-model`.

### Phase 5: Hiring Triggers

Don't hire until you've proven the motion personally:

| Trigger | Hire | Why |
|---|---|---|
| Founder closed 10-20 deals personally | Senior AE (full-stack) | Motion proven. Clone yourself. |
| AE at capacity, pipeline bottleneck | First SDR | Feed the AE, don't make AE prospect. |
| 2 AEs at quota | Player-coach manager | Process repeatable. Needs management. |
| $2M+ ARR, 5+ reps | VP Sales | Scale what works. Never before $2M. |
| 8+ reps, ramp >6 months | Sales enablement | Onboarding cost justifies dedicated role. |

**Never:** VP Sales before $2M ARR (70% failure rate). SDR as first hire
(founder closes + manages junior rep = neither done well).

### Phase 6: WbD GTM Index Self-Assessment

Score yourself 1-10 on each:

1. **Revenue Model:** Is your pricing clear? Do you know your ACV, churn, LTV?
2. **Data Model:** Can you answer "how many qualified leads this month?"
3. **Math Model:** Do unit economics work? LTV:CAC above 3:1?
4. **Operating Model:** Is there a documented process someone else could follow?
5. **Growth Model:** Do you know which channels work and at what cost?
6. **GTM Model:** Is the entire revenue system connected or fragmented?

Score below 6: fix fundamentals before scaling the team. Adding headcount
to a broken system multiplies the damage.

## Output Format

Stage-based GTM playbook with tool stack, AI agent configuration, hiring
triggers with ARR thresholds, and GTM Index self-assessment scorecard.

## Quality Check

- [ ] Revenue stage correctly identified
- [ ] Tool stack appropriate for stage (not over-buying)
- [ ] Hiring triggers clear with ARR thresholds
- [ ] AI agents configured before any hire
- [ ] GTM Index self-assessment completed
- [ ] Unit economics calculated (CAC, LTV, payback)

## Common Pitfalls

1. **Hiring before the motion works.** If the founder can't close 10-20 deals
   personally, the motion isn't proven. Hire an AE to accelerate what works,
   not to discover what works.

2. **Enterprise tools at startup stage.** $25K ZoomInfo at $500K ARR is capital
   misallocation. Apollo is $59/mo and covers 90% of early-stage needs.

3. **SDR as first hire.** A full-stack AE who can prospect AND close is the
   right first hire. An SDR adds pipeline but can't close it — so the founder
   still closes every deal while managing the SDR.

4. **No AI leverage.** One founder + AI tools outperforms 3 junior hires at
   lower cost and zero management overhead.

5. **Skipping self-assessment.** The GTM Index surfaces what's broken before
   you scale it. Fix the system, then add people.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator
- `references/pmf-testing-playbook.md` — Sean Ellis, cohort retention, payback tests
- `references/pmf-signal-checklist.md` — PMF go/no-go signals and false-PMF traps
- `references/scale-readiness-gates.md` — when to scale GTM headcount and spend
- `references/when-not-to-scale.md` — anti-patterns and stop signals
- `gtm-spend-management/references/spend-by-stage.md` — ARR-stage tool + payroll guardrails
**Canonical lifecycle (repo root):** `references/gtm-lifecycle-stages.md` · `references/activation-playbook.md` · `references/lifecycle-metrics-by-stage.md`
**Cross-skill artifacts:** `saas-outcomes/references/journey-stage-gates.md`, `saas-outcomes/references/bootstrap-founder-playbook.md`, `saas-outcomes/templates/bootstrap-capital-plan.md`, `saas-outcomes/templates/journey-planning-worksheet.md`, `saas-outcomes/references/exit-potential-scorecard.md`, `gtm-role-descriptions/references/gtm-engineer-hiring.md`

## Related Skills

- **saas-outcomes**: Journey stages, end goal, exit optionality
- **sales-team-building**: Hiring sequence and POD design after scale gates pass
- **financial-modeling**: Runway and unit economics before scale
- **founder-brand**: Build personal brand as founder
- **tool-selection-stack**: Detailed tool comparison
- **saas-metrics-calculator**: Unit economics for your stage
- **gtm-spend-management**: Stage-appropriate spend and vendor roster

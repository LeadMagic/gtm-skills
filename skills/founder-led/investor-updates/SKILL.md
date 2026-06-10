---
name: investor-updates
description: >-
  Write investor updates that build confidence and surface help — monthly format,
  board deck structure, fundraising narrative, and metrics dashboards. Use when
  writing investor updates, preparing board meetings, or communicating with
  stakeholders. Triggers on: "investor update", "board deck", "monthly update",
  "investor communication", "fundraising update", or any stakeholder reporting.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.2.0"
  author: LeadMagic
  category: founder-led
  tags: [investors, updates, fundraising, board, communication]
  frameworks: [YC Investor Update Template, Jason Lemkin SaaStr Board Deck, David Skok VC Dashboard]
  related_skills: [saas-metrics-calculator, building-saas, exiting-company, financial-modeling, fundraising-strategy]
---

# Investor Updates

## Overview

Investor updates are the most underleveraged asset in a founder's toolkit.
A great update builds confidence, surfaces problems early when investors can
help, and makes fundraising conversations natural rather than desperate.
A bad update — or no update — signals that things aren't going well, even
when they are.

Send monthly. Every month. Even when (especially when) things are hard.

## Frameworks Referenced

- **YC Investor Update Template** — Consistent monthly structure
- **Jason Lemkin (SaaStr)** — Board metrics: growth, burn multiple, NRR
- **David Skok** — VC dashboard metrics (LTV:CAC, payback)

## When to Use

- "Write my monthly investor update"
- "Create a board deck"
- "Prepare for a board meeting"
- "Structure an investor communication"
- "What should I include in investor updates?"
- "Build a fundraising narrative"
- "Investor update during crisis / outage / breach"
- "Board comms after bad press"

## Step-by-Step Process

### Phase 1: Monthly Update Structure

Every update follows this structure. Every month. Consistency builds trust.

**1. Headline / TL;DR (1-2 sentences)**
"Revenue grew 12% MoM to $X MRR. Churn dropped to 1.2%. Hired first AE."

**2. Key Metrics**

Use `saas-metrics-calculator/references/metric-definitions-exit-weight.md` for
formulas. Minimum investor set: MRR/ARR, NRR, GRR, logo churn, CAC payback,
magic number, burn multiple, runway.

- MRR / ARR (with growth rate)
- Customer count (new, churned, net new)
- Churn rate (logo + revenue)
- Cash / runway (months remaining)
- Burn rate (monthly)

**3. Wins (what went right)**
3-5 bullet points. Specific, named achievements. "Closed Acme Corp ($24K ACV)"
not "made good progress on enterprise deals."

**4. Challenges (what's hard)**
2-3 bullet points. Be honest. "Churn spiked to 3% this month. Investigating
root cause — initial data points to onboarding gaps. Hired a CS lead to fix."

**5. Asks (specific things investors can help with)**
"Introduction to VP Sales at [Company A, B, C]." "Candidate referrals for
senior frontend role." "Advice on pricing model for enterprise tier."

**6. Team updates**
Hires, departures, open roles. Investors track team velocity.

**7. Cash and runway**
Current cash, monthly burn, months of runway. Always include this.

### Phase 2: Writing Principles

- **Honesty over optimism.** Investors can't help with problems they don't
  know about. Bad news delivered early builds trust. Bad news hidden destroys it.
- **Specific over vague.** "Grew 12%" beats "good growth this month."
- **Asks are gifts.** Investors want to help. Give them specific things to do.
  "Introduction to [specific person]" beats "help with hiring."
- **One page.** Nobody reads 5-page updates. One page, clear metrics, specific
  asks. If they want more detail, they'll ask.

### Phase 3: Board Deck (quarterly)

For formal board meetings, expand the update:

1. Strategy review (are we on track?)
2. Financial performance (vs plan, vs prior quarter)
3. Product roadmap (what shipped, what's next)
4. GTM review (pipeline, conversion, CAC, payback)
5. Team update (org chart, gaps, hiring plan)
6. Key decisions needed (board vote items)
7. Risks and mitigation

### Phase 4: Crisis & Incident Investor Comms

**Lemkin rule:** Send updates *more* reliably in bad months — never skip because of embarrassment. Source: [Handling Bad News](https://www.saastr.com/handling-bad-news/)

**Sev 3+ addendum** (same day as customer holding statement, after counsel if breach):

1. **What happened** — facts only; no legal admissions without counsel
2. **Customer/revenue impact** — affected ARR %, churn risk, pipeline deals flagged
3. **Mitigation** — technical fix, CS surge, credits/SLA policy
4. **Metrics to watch** — NRR, logo churn, 90-day retention vs pre-crisis baseline
5. **Asks** — intro to PR counsel, security advisor, reference customers for trust rebuild

**Do not:** Replace monthly rhythm with silence; bury crisis in footnotes.

**Canonical crisis playbook:** `references/crisis-management-playbook.md` (Pattern 33) · `gtm-leadership` (war room)

### Phase 5: Fundraising Narrative

When actively fundraising, the update becomes evidence for your pitch:

**The narrative arc:** "Here's where we were → here's what we did → here's
the result → here's what we'll do next → here's what we need to do it."

Investors who receive consistent monthly updates are 3-5x more likely to
invest in your next round. They've watched your trajectory. They trust
your reporting. The pitch is just the latest chapter in a story they've
been reading for 12+ months.

## Output Format

Monthly update template, board deck structure, and fundraising narrative
framework.

## Quality Check

- [ ] Headline communicates the most important thing this month
- [ ] All key metrics present (MRR, churn, customers, cash, runway)
- [ ] Wins are specific and quantified
- [ ] Challenges are honest (not sugar-coated)
- [ ] Asks are specific and actionable
- [ ] Update fits on one page (or one screen)
- [ ] Sent on time (first week of the month)

## Common Pitfalls

1. **Hiding problems.** Investors find out anyway. Problems you communicate
   early are opportunities for help. Problems you hide are trust-breakers.

2. **No asks.** Investors want to feel useful. If you never ask for anything,
   they stop reading. Specific asks drive engagement.

3. **Sending only when things are good.** The months you don't want to send
   an update are the months you most need to. Silence signals trouble.

4. **Dense walls of text.** Nobody reads 5-page updates. One page. Metrics
   first. Narrative second. Bullet points, not paragraphs.

5. **Inconsistent format.** Different structure every month means investors
   can't find what they're looking for. Same format, every month, forever.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

**Cross-skill:** `saas-metrics-calculator/references/metric-definitions-exit-weight.md`, `fundraising-strategy/references/vc-milestone-gates.md`, `exiting-company/references/due-diligence-metrics-pack.md`

**Crisis:** `references/crisis-management-playbook.md` · `references/saas-pr-crisis-experts.md` (Lemkin transparency)

## Related Skills

- **saas-metrics-calculator**: The metrics you report
- **building-saas**: The business you're updating on
- **exiting-company**: Exit-ready financials start with clean updates
- **gtm-leadership**: Crisis war room and executive messaging
- **deal-desk**: Legal review before investor statements on breach/regulatory matters

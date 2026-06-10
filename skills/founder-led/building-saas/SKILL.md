---
name: building-saas
description: >-
  Build a SaaS company from idea to scale — product development, architecture
  decisions, pricing, hiring sequence, fundraising stages, and operational
  infrastructure. Use when starting a SaaS, scaling from $0 to $10M ARR, making
  build-vs-buy decisions, or designing the technical and operational foundation
  of a software business. Triggers on: "build a SaaS", "start a SaaS", "SaaS
  architecture", "SaaS startup", "build software business", "SaaS from scratch",
  "tech stack for SaaS", or any request about building a software company.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: founder-led
  tags: [saas, startup, product, architecture, founder]
  related_skills: [solo-founder-gtm, saas-metrics-calculator, pricing-strategy, sales-team-building]
  frameworks: [David Skok SaaS Metrics, SaaStr Stages, Winning by Design GTM Index]
---

# Building a SaaS

## Overview

Building a SaaS company is not the same as building a SaaS product. The product
is one component of a system that includes pricing, distribution, support,
compliance, and operations. This skill covers the complete build: from
architecture decisions at $0 to scaling infrastructure at $10M ARR.

## When to Use

- "How do I build a SaaS company?"
- "What tech stack should I use?"
- "Start a SaaS from scratch"
- "Scale our SaaS infrastructure"
- "What should I build first?"
- "SaaS architecture decisions"
- "Build vs buy for SaaS tools"

## Authoritative Foundations

- **David Skok (Matrix Partners)** — SaaS metrics and unit economics. LTV:CAC
  ratios by stage, CAC payback benchmarks, Magic Number.
- **SaaStr (Jason Lemkin)** — ARR stages and hiring triggers. Founder must
  personally close 10-20 deals before first sales hire.
- **Winning by Design GTM Index** — 1-10 scoring across 6 models to assess
  revenue system maturity.

## Step-by-Step Process

### Phase 1: $0-10K MRR — Validation

**Product:**
- Ship the smallest thing that solves one real problem
- No microservices. Monolith or simple backend + frontend
- Host on one provider (Vercel + Supabase, or Railway, or Fly.io)
- Don't build auth, billing, or infrastructure yourself — use Stripe, Clerk, etc.
- Time to first user: days, not months

**Pricing:**
- Start with one plan. Add tiers when customers ask for them
- Price based on value, not cost. If they save $1,000/mo, $100/mo is cheap
- Annual billing discount: 20-30%. Improves cash flow immediately

**GTM:**
- Founder does all selling. No exceptions
- Talk to 20-50 potential customers before writing code
- First 10 customers: personal outreach, not ads

### Phase 2: $10-100K MRR — Repeatability

**Product:**
- The product works. Now make it reliable
- Add monitoring (Sentry, Axiom, or equivalent)
- Add backups and disaster recovery
- Start thinking about SOC2 if enterprise customers ask

**Pricing:**
- 2-3 tiers: Starter, Pro, Enterprise
- Usage-based components for high-volume customers
- Raise prices on new customers. Grandfather existing ones

**GTM:**
- Founder still leads sales. Document the playbook
- First marketing hire if founder can't produce content
- No SDR yet. Founder or AE prospects and closes

### Phase 3: $100K-2M ARR — Growth

**Product:**
- Dedicated infrastructure: separate staging/production
- CI/CD pipeline that deploys in minutes, not hours
- API for integrations. Partners will ask for it
- SOC2 Type II if enterprise is 20%+ of revenue

**Team:**
- 2-3 engineers. One can be a contractor initially
- First AE hired (founder closed 10-20 deals personally first)
- Part-time CFO or finance person for metrics and compliance
- Customer success hire when churn exceeds 3%

**GTM:**
- Documented sales playbook. Second AE can follow it
- Content marketing producing 2-4 pieces/month
- Paid acquisition: test small budgets ($500-1,000/mo)

### Phase 4: $2-10M ARR — Scale

**Product:**
- SOC2 Type II complete (or equivalent compliance framework)
- 99.9% uptime SLA. Incident response process documented
- Enterprise features: SSO, RBAC, audit logs, data export

**Team:**
- 5-10 engineers across product areas
- VP Sales or Head of Sales (only after 2 AEs at quota)
- Dedicated finance/ops person
- Customer success team (1 CSM per $500K-1M ARR)

**GTM:**
- Multiple channels running: outbound, inbound, partnerships
- Events and conferences for enterprise pipeline
- Partnership program for integration and reseller channels

## Output Format

SaaS building roadmap with stage-specific: product decisions, pricing model,
team hiring sequence, GTM channels, infrastructure requirements, and compliance
milestones.


## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls

1. **Overbuilding before validation.** Spending 6 months on architecture before
   talking to a single customer. Ship in days, iterate based on usage.

2. **Free tier without conversion path.** Freemium with 5% conversion means
   95% of users cost money forever. Design the upgrade trigger before launching
   the free tier.

3. **Hiring VP Sales before $2M ARR.** 70% failure rate. Founder-led sales
   until the playbook is proven and repeatable.

4. **Enterprise features too early.** SSO, audit logs, and SOC2 matter when
   enterprise is 20%+ of pipeline. Before that, they're distraction.

5. **No unit economics tracking.** CAC, LTV, churn, payback period. If you
   can't answer these in 30 seconds, you're flying blind.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **solo-founder-gtm**: Lean GTM for early-stage SaaS
- **saas-metrics-calculator**: Unit economics and benchmarks
- **sales-team-building**: Hiring sequence by ARR
- **soc2-compliance**: Security compliance for SaaS

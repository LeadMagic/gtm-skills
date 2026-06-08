---
name: equity-management
description: >-
  Complete equity management for SaaS founders — cap tables, 409A valuations,
  option pools (ISO vs NSO vs RSU), 83(b) elections, equity grants for
  employees/advisors/contractors, dilution modeling, secondary sales, and
  equity tools (Carta, Pulley, AngelList Equity). Use when setting up equity,
  granting options, planning option pools, modeling dilution, or preparing
  for fundraising. Triggers on: "cap table", "409A valuation", "option pool",
  "equity grant", "ISO vs NSO", "83(b)", "equity for employees".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: founder-led
  tags: [equity, cap-table, 409a, options, iso, nso, dilution, stock-options]
  related_skills: [co-founder-dynamics, fundraising-strategy, first-hires-playbook, legal-for-founders, financial-modeling]
  frameworks:
    - "Carta — Equity management platform and cap table benchmarks"
    - "Pulley — Cap table management for startups"
    - "Fred Wilson (Union Square Ventures) — Employee equity"
    - "Andy Rachleff (Wealthfront) — Equity compensation"
    - "Sam Altman — Employee equity"
    - "Leo Polovets (Humba Ventures/YC) — Technical founder equity guide"
---

# Equity Management

## Overview

Equity is the hardest-working tool in a startup's compensation arsenal — it
aligns incentives across founders, employees, advisors, and investors. The
mistake: treating equity as an afterthought, granting shares on napkins, and
discovering during Series A that your cap table is a disaster. This skill
covers the complete equity stack: cap tables, 409A valuations, option types,
grant guidelines by role and stage, dilution modeling, and the tools that
keep it all clean.

## Frameworks Referenced

This skill is grounded in named GTM frameworks, public methodologies, and vendor documentation where relevant:

- **Carta — Equity management platform and cap table benchmarks** — used as the named operating framework for this playbook.
- **Pulley — Cap table management for startups** — used as the named operating framework for this playbook.
- **Fred Wilson (Union Square Ventures) — Employee equity** — used as the named operating framework for this playbook.
- **Andy Rachleff (Wealthfront) — Equity compensation** — used as the named operating framework for this playbook.
- **Sam Altman — Employee equity** — used as the named operating framework for this playbook.
- **Leo Polovets (Humba Ventures/YC) — Technical founder equity guide** — used as the named operating framework for this playbook.
- **--** — used as the named operating framework for this playbook.
- **Before granting your first stock options (required by law)** — used as the named operating framework for this playbook.
- **After every priced fundraising round** — used as the named operating framework for this playbook.
- **Every 12 months (or when a material event occurs)** — used as the named operating framework for this playbook.
- **Before an acquisition (the acquirer will require a recent 409A)** — used as the named operating framework for this playbook.
- **VP Engineering: 1.5%** — used as the named operating framework for this playbook.
- **5 engineers: 0.25-0.5% each = 1.75%** — used as the named operating framework for this playbook.
- **VP Sales: 1.0%** — used as the named operating framework for this playbook.
- **3 AEs: 0.1-0.2% each = 0.45%** — used as the named operating framework for this playbook.
- **First Marketer: 0.4%** — used as the named operating framework for this playbook.
- **CS Lead: 0.5%** — used as the named operating framework for this playbook.
- **Buffer (30%): 1.4%** — used as the named operating framework for this playbook.
- **Contractors (pay cash, not equity — unless they're effectively a co-founder)** — used as the named operating framework for this playbook.
- **Agencies (cash only)** — used as the named operating framework for this playbook.
- **Part-time advisors who don't deliver (vesting protects you)** — used as the named operating framework for this playbook.
- **Early stage: typically no (shares are illiquid)** — used as the named operating framework for this playbook.
- **Series C+: sometimes. Company may run a tender offer.** — used as the named operating framework for this playbook.
- **IPO: yes (but lockup periods apply)** — used as the named operating framework for this playbook.
- **Allocated: X% (X shares to X recipients)** — used as the named operating framework for this playbook.
- **Available: X% (X shares remaining)** — used as the named operating framework for this playbook.
- **[Hire/role] — [date] — [grant size]** — used as the named operating framework for this playbook.
- **[ ] 409A valuation current (within last 12 months)** — used as the named operating framework for this playbook.
- **[ ] Cap table on Carta/Pulley (not Excel) and up to date** — used as the named operating framework for this playbook.
- **[ ] All founders filed 83(b) within 30 days of share issuance** — used as the named operating framework for this playbook.
- **[ ] Option pool sized to hiring plan + buffer through next funding round** — used as the named operating framework for this playbook.
- **[ ] Equity grants documented with board consent** — used as the named operating framework for this playbook.
- **[ ] Dilution model built for next 2 funding rounds** — used as the named operating framework for this playbook.
- **[ ] Advisor grants on FAST template with vesting** — used as the named operating framework for this playbook.
- ****Legal matters:** Consult a qualified attorney licensed in your jurisdiction.** — used as the named operating framework for this playbook.
- ****Tax matters:** Consult a certified tax professional or CPA.** — used as the named operating framework for this playbook.
- ****Accounting/financial matters:** Consult a qualified accountant or financial advisor.** — used as the named operating framework for this playbook.
- ****Insurance matters:** Consult a licensed insurance broker.** — used as the named operating framework for this playbook.
- ****Security/compliance matters:** Consult a qualified security assessor or compliance** — used as the named operating framework for this playbook.
- **`co-founder-dynamics` — Founder equity splits** — used as the named operating framework for this playbook.
- **`fundraising-strategy` — Dilution from SAFE/priced rounds** — used as the named operating framework for this playbook.
- **`first-hires-playbook` — Equity as part of compensation** — used as the named operating framework for this playbook.
- **`legal-for-founders` — 83(b), incorporation, stock plans** — used as the named operating framework for this playbook.

## When to Use

Trigger phrases: "set up cap table", "409A valuation", "option pool planning",
"equity grant guidelines", "ISO vs NSO", "83(b) election", "equity for
employees", "dilution modeling", "how much equity to give", "Carta vs Pulley"

## Step-by-Step Process

### Phase 1: Equity Types

| Type | Who Gets It | Tax Treatment | Key Rules |
|---|---|---|---|
| **ISO (Incentive Stock Option)** | Employees only | No tax at exercise (AMT may apply). Capital gains if held 1yr+ after exercise, 2yr+ after grant. | $100K vest limit/yr. Must exercise within 90 days of leaving. |
| **NSO (Non-Qualified Stock Option)** | Advisors, contractors, anyone | Taxed at exercise (ordinary income on spread). | More flexible. No $100K limit. |
| **RSU (Restricted Stock Unit)** | Later-stage employees | Taxed at vest (ordinary income on FMV). No exercise cost. | Common post-Series B. Not great for early stage (taxed at vest even if illiquid). |
| **Restricted Stock** | Founders, very early employees | Taxed at grant (can be $0 if 83(b) filed). Capital gains on sale. | Founders should file 83(b) immediately. |

**Rule of thumb:** Early stage → ISOs for employees, NSOs for advisors.
Later stage → RSUs become more common.

### Phase 2: 409A Valuation

**What it is:** An independent appraisal of your common stock's fair market
value (FMV). Required by IRS to set the strike price for stock options.

**When to get one:**
- Before granting your first stock options (required by law)
- After every priced fundraising round
- Every 12 months (or when a material event occurs)
- Before an acquisition (the acquirer will require a recent 409A)

**Cost:** $1,000-3,000. Providers: Carta, Pulley, Aranca, Scalar.

**The 409A discount:** Common stock (what employees get) is valued at a
discount to preferred stock (what investors buy). Typical discounts: 10-30%
for early stage, narrowing at later stages.

**Why 409A matters:** If you grant options below FMV, both you and the
employee face tax penalties. The IRS takes 409A seriously.

### Phase 3: Option Pool Planning

**Option pool sizing:**

| Stage | Pool Size | Who's in the Pool |
|---|---|---|
| Seed | 10-15% | Future employees, advisors |
| Series A | 15-20% | Expanding team — AEs, engineers, CS |
| Series B | 15-20% (refreshed) | Scaling all functions |
| Growth+ | 10-15% (ongoing) | Refreshes, executive hires |

**Key insight:** The option pool is created from pre-money shares at Series A.
This means the dilution from the pool comes ENTIRELY from founders and
existing shareholders, not from new investors. Negotiate for the SMALLEST
pool your hiring plan requires.

**Option pool calculator:**
```
Pool Size = Sum of all equity grants to be made before next funding round
+ 20-30% buffer for hires you haven't planned yet

Example:
- VP Engineering: 1.5%
- 5 engineers: 0.25-0.5% each = 1.75%
- VP Sales: 1.0%
- 3 AEs: 0.1-0.2% each = 0.45%
- First Marketer: 0.4%
- CS Lead: 0.5%
- Buffer (30%): 1.4%
Total Pool: ~7.0% (round to 10% for Series A standard)
```

### Phase 4: Equity Grant Guidelines

**By role and stage (approximate, adjust for your situation):**

| Hire # | Role | Grant Range |
|---|---|---|
| Founder | CEO/CTO | 25-50% each (with vesting) |
| 1st | Founding Engineer | 1-3% |
| 2-5 | Early Engineers | 0.5-1.5% |
| 1st | VP Engineering | 1-2% |
| 1st | VP Sales / CRO | 1-3% |
| 1-3 | AEs | 0.1-0.3% |
| 1st | Head of Marketing | 0.5-1.0% |
| 1st | Head of CS | 0.5-1.0% |
| 1st | Head of Product | 0.5-1.5% |
| 50th | Senior Engineer | 0.05-0.1% |
| Advisor | Individual | 0.15-0.5% (2-year vest, no cliff) |

**When NOT to give equity:**
- Contractors (pay cash, not equity — unless they're effectively a co-founder)
- Agencies (cash only)
- Part-time advisors who don't deliver (vesting protects you)

### Phase 5: Cap Table Management

**Your cap table must ALWAYS be current.** A messy cap table kills
fundraising and can kill an acquisition.

**Cap table best practices:**
1. Use cap table software (Carta, Pulley, AngelList Equity). NOT Excel.
2. Update immediately after every grant, exercise, or transfer.
3. Keep it clean: no "we'll figure out the details later" entries.
4. Model dilution before fundraising. Know exactly who owns what.
5. Get 409As on schedule. Don't let them lapse.

**Cap table software comparison:**
| Tool | Best For | Cost |
|---|---|---|
| **Carta** | Funded startups, Series A+ | $100-500/mo+ |
| **Pulley** | Early stage, simple cap tables | Free-$100/mo |
| **AngelList Equity** | Early stage, integrated with banking | Free |
| **Clerky** | Incorporation + first cap table | $99 one-time |

### Phase 6: Secondary Sales and Liquidity

**Can employees sell their shares?**
- Early stage: typically no (shares are illiquid)
- Series C+: sometimes. Company may run a tender offer.
- IPO: yes (but lockup periods apply)

**Founder secondary:** Some founders sell 5-10% of their shares in later
rounds to take money off the table. This is becoming more accepted. It
reduces pressure to exit prematurely.

## Output Format

```
EQUITY PLAN — [Company]

CAP TABLE: [link in Carta/Pulley]
Last 409A: [date]. FMV per share: $X. Next due: [date].

OPTION POOL: X% (X,XXX,XXX shares)
- Allocated: X% (X shares to X recipients)
- Available: X% (X shares remaining)

GRANT POLICY:
| Role | Grant Range | Vesting | Cliff |
|---|---|---|
| [role] | X-Y% | 4 years | 1 year |

UPCOMING GRANTS:
- [Hire/role] — [date] — [grant size]
```

## Implementation Checklist

- [ ] 409A valuation current (within last 12 months)
- [ ] Cap table on Carta/Pulley (not Excel) and up to date
- [ ] All founders filed 83(b) within 30 days of share issuance
- [ ] Option pool sized to hiring plan + buffer through next funding round
- [ ] Equity grants documented with board consent
- [ ] Dilution model built for next 2 funding rounds
- [ ] Advisor grants on FAST template with vesting

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **Cap table in Excel.** Excel can't handle cap table complexity (option
   exercises, early exercises, multiple funding rounds). Fix: Carta or Pulley
   from day 1.

2. **No 409A valuation.** You're granting options at an arbitrary price =
   IRS penalties for you and your employees. Fix: 409A before first grant.
   Renew annually.

3. **Nowhere near enough equity for key hires.** "0.1% for our VP Engineering"
   won't close a candidate who can get 1%+ elsewhere. Fix: Benchmark against
   stage and role. Don't be stingy on your most critical hires.

4. **Forgotten option pool at fundraising.** You model dilution from the new
   round but forget the option pool refresh. Surprise: an extra 15% dilution.
   Fix: Model dilution including option pool. Negotiate pool size at term
   sheet stage.

5. **Missing 83(b) for founders.** Miss it and you owe tax on phantom income
   as your shares vest over 4 years. Fix: File within 30 days. Keep proof.
   This is the #1 unforced error in startup equity.



## ⚠️ Disclaimer

This skill provides general informational guidance based on publicly available frameworks and operator experience. It is NOT legal advice, accounting advice, tax advice, financial advice, insurance advice, or professional services advice.

Consult qualified professionals for your specific situation — attorneys for legal/equity matters, CPAs for tax and accounting, licensed brokers for insurance, and certified security assessors for compliance. This skill does not create a professional-client relationship. Use it as a starting point for research and preparation.

## Related Skills

- `co-founder-dynamics` — Founder equity splits
- `fundraising-strategy` — Dilution from SAFE/priced rounds
- `first-hires-playbook` — Equity as part of compensation
- `legal-for-founders` — 83(b), incorporation, stock plans
- `financial-modeling` — Dilution modeling in financial projections

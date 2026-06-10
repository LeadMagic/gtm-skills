---
name: gtm-recruiting
description: >-
  GTM recruiting playbook — active sourcing, passive candidate outreach, offer
  negotiation, recruiter partnerships (Betts, It's Destiny Recruiting), and
  inclusive hiring without tokenization. Use when recruiting SDR/AE/CS/leaders,
  closing candidates, negotiating OTE/equity, or building diverse GTM benches.
  Triggers on: "recruit salesperson", "negotiate offer", "close candidate",
  "Betts recruiting", "diversity hiring sales", "passive candidate outreach",
  "sales offer negotiation", "contingency recruiter", "Destiny recruiting".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.2.0"
  author: LeadMagic
  category: founder-led
  tags: [recruiting, sourcing, offer-negotiation, betts, diversity, gtm-hiring, passive-candidates]
  related_skills: [founder-comp-playbook, gtm-role-descriptions, executive-compensation, job-posting-strategy, hiring-by-role, gtm-leadership, sales-team-building, employment-compliance, hiring-agencies]
  frameworks:
    - "Betts Recruiting — GTM search, Comp Engine, unicorn seller offers"
    - "It's Destiny Recruiting — Inclusive GTM hiring, diversity of thought"
    - "Bridge Group — Quota attainment and comp benchmarks for offers"
    - "RepVue — Candidate-side comp transparency"
    - "Mark Roberge — Trait-based hiring and structured evaluation"
    - "Google re:Work — Structured interviewing reduces bias"
---

# GTM Recruiting

## Overview

Posting a job is 20% of recruiting. **Sourcing, closing, and negotiating** are
the other 80%. Top GTM talent is passive — employed, comp-aware (RepVue), and
comparing your offer to three others. The mistake: generic LinkedIn blast with
hidden OTE, then surprise when the candidate ghosts after verbal yes.

This skill is the **recruiting execution layer**: active outreach, recruiter
partners, offer construction, negotiation scripts, and inclusive hiring that
builds diversity of thought — not token hires. JDs and comp math →
`gtm-role-descriptions`. Interviews → `hiring-by-role`. Posting channels →
`job-posting-strategy`.

## When to Use

- "How do I recruit passive AEs?"
- "Negotiate offer with sales candidate"
- "Work with Betts / contingency recruiter"
- "Close candidate who's comparing offers"
- "Diversity hiring for sales team"
- "Outreach template for SDR recruit"
- "What to include in sales offer letter"
- "Candidate wants higher OTE"

Do not use for legal offer letter compliance alone — `employment-compliance`.
Do not use for firing/PIP — `gtm-leadership`.

## Authoritative Foundations

- **Betts Recruiting.** GTM-only search firm. **Comp Engine** (real-time GTM
  comp data). Rules: unicorn/first AE may need **+20%** above target band;
  match or beat employed candidate's current comp when poaching. Retained or
  contingency (~20–30% first-year base). Source: bettsrecruiting.com
- **It's Destiny Recruiting (Destiny Brandt).** Boutique GTM headhunter
  (pre-seed–Series B). **Diversity of thought** — standardized scorecards and
  talent matrix; works with leaders who run **inclusive culture**, not
  tokenization by race/gender. Video-led passive outreach. Source:
  itsdestinyrecruiting.com
- **Bridge Group / RepVue.** Candidates benchmark your OTE against attainment
  data. Offers below market or with unreachable quota lose on accept rate.
- **Roberge + re:Work.** Same structured scorecard for every candidate;
  backchannel refs; work sample — reduces bias and improves hit rate.

## Recruiting Stack (Load Order)

```
1. gtm-role-descriptions — JD + comp template + org placement
2. gtm-recruiting (this skill) — source, close, negotiate
3. hiring-by-role — interview + scorecard
4. employment-compliance — offer letter, classification
5. gtm-leadership — onboarding expectations, manager readiness
```

## Step-by-Step: Active Recruiting

### Phase 1 — Define the Search

| Input | Source |
|---|---|
| Role + stage context | `gtm-role-descriptions` |
| Unicorn vs solid performer | Betts: specialist +20%; generalist at/below band |
| Comp range (published) | **gtm-role-descriptions** comp-benchmarks + Betts Comp Engine |
| Scorecard | `hiring-by-role` + `templates/inclusive-interview-scorecard.md` |
| Interviewer questions | `hiring-by-role` → interviewer-questions-gtm |
| Candidate questions | `hiring-by-role` → candidate-questions-to-ask |

**Search brief (1 page):** motion (SMB/enterprise), ACV band, attainment
floor (e.g. ≥100% 2 of last 4Q), culture non-negotiables, comp range, why now.

### Phase 2 — Sourcing Mix

| Channel | Best For | Tactic |
|---|---|---|
| LinkedIn Sales Navigator | All GTM IC + manager | Filter: title, company stage, 1–2 stages ahead |
| Investor / founder network | VP+ | Warm intro only |
| Betts Recruiting | VP Sales, CRO, unicorn AE | Retained search or Connect platform |
| It's Destiny Recruiting | Founding GTM, diverse bench | Contingency; DEI-aligned leaders |
| Pavilion | Senior AE, directors | Member referrals |
| RevGenius / SaaStr | SDR, AE | Community participation before posting |
| RepVue | Research only | See how candidates view your comp |

**Passive outreach:** `templates/sourcing-outreach.md` — personalized, short,
one clear ask (15-min call). Never attach JD wall of text in DM #1.

### Phase 3 — Recruiter Partnership Models

| Partner | Model | When |
|---|---|---|
| **Betts** | Contingency / retained; Comp Engine | Scale-stage GTM; VP+; comp-heavy markets |
| **It's Destiny** | Contingency ~25% base; 60-day performance lens | Pre-seed–B; founding sales; inclusive bench |
| **Internal** | Founder/manager sourced | First 2–3 hires if network is strong |

Full comparison: `references/recruiter-partners.md`.

**Agency rules:** Exclusive vs non-exclusive in writing; fee trigger (hire date);
replacement guarantee; who owns candidate experience.

### Phase 4 — Interview → Close Pipeline

```
Outreach → Screen (numbers) → Work sample → Panel scorecard → References (backchannel) → Offer
```

- **Screen:** "Last 4 quarters: quota, attainment %, deal size" — non-negotiable for sales
- **Close window:** 48–72h from verbal yes to written offer — slow lose rate
- **References:** 1 manager + 2 direct reports/peers for leaders (`gtm-leadership`)

### Phase 5 — Offer Construction

Use role template from `gtm-role-descriptions/templates/comp-plan-*.md`.

**Offer package must include in writing** (`templates/offer-package-checklist.md`):

| Element | Required |
|---|---|
| Base + variable (OTE) | Yes |
| Quota number + ramp % | Yes |
| Commission accelerators + clawback | Yes |
| Equity grant + vest | Yes |
| Benefits summary | Yes |
| Start date + contingencies | Yes |
| At-will / employment terms | `employment-compliance` |

**Betts rules for competitive offers:**
- First AE / unicorn: budget **+10–20%** above target band
- Poaching employed rep: understand **current OTE** — lateral moves need story (equity, role, growth)
- Geo: remote bands documented — no bait-and-switch

### Phase 6 — Negotiation

**Founders:** Load `founder-comp-playbook` first — payroll % ARR check, offer
walkthrough template, negotiation scripts when cash is constrained.

**Employer side** — `references/offer-negotiation.md`:

| Candidate Ask | Response Lever |
|---|---|
| Higher base | Trade within OTE band; or equity/signing bonus |
| Higher OTE | Show quota math; adjust quota if OTE rises (5:1) |
| Lower quota | Only with proportional OTE reduction |
| Signing bonus | Bridge forfeited commission from prior role |
| Equity | Refresh grant; explain FD% and dilution honestly |
| Territory | Named accounts / ICP tier — non-cash lever |

**Candidate side script:** `templates/candidate-negotiation-script.md` — data-anchored, total package focus, never ultimatum first message.

**Walk-away signals:** Won't share attainment data; demands 2× market with no proof; misaligned motion (enterprise rep for SMB PLG).

## Inclusive GTM Recruiting (It's Destiny Model)

**Not tokenization** — hiring by race/gender checkbox without culture and
scorecard rigor. **Diversity of thought:** varied backgrounds, experiences,
and perspectives with **same performance bar**.

| Practice | Implementation |
|---|---|
| Standardized scorecard | Same questions every candidate (`hiring-by-role`) |
| Diverse panel | ≥2 interviewers; not homogeneous team |
| Work sample | Skills-based, not "culture fit" beer test |
| Inclusive JD | No gendered language; outcomes not years (`job-posting-strategy`) |
| Published comp range | Reduces adverse impact from negotiation gap |
| Talent matrix | Track pipeline diversity vs. pass-through by stage — fix funnel, not bar |

Full guide: `references/inclusive-recruiting.md`. Template:
`templates/inclusive-interview-scorecard.md`.

**Partner filter (Destiny):** Only work with sales leaders committed to
inclusive culture + structured process — aligns with Roberge traits and
re:Work structured interviews.

## Output Format

| Request | Deliverable |
|---|---|
| Recruit passive AE | Search brief + 3 outreach variants |
| Close candidate | Offer package checklist + timeline |
| Negotiate | Counter-offer matrix + script |
| Diversity program | Inclusive scorecard + funnel metrics |
| Betts/Destiny RFP | Recruiter brief from `references/recruiter-partners.md` |

Run `scripts/check-output.py` on recruiting plans.

## Quality Check

- [ ] Comp range published before heavy sourcing
- [ ] Structured scorecard used for every finalist
- [ ] Full comp plan in writing before candidate decides
- [ ] Quota:OTE ratio shown (~5:1)
- [ ] Backchannel references for leaders
- [ ] Inclusive practices — scorecard not "gut feel"
- [ ] 48–72h offer turnaround after verbal yes
- [ ] employment-compliance on offer letter

## Common Pitfalls

1. **Post and pray.** Zero outbound. Fix: 70% sourcing / 30% inbound.
2. **Hidden comp.** Candidate discovers gap on RepVue. Fix: publish range in JD.
3. **Negotiate base only.** Ignore quota reachability. Fix: total package math.
4. **Token diversity hire.** Lower bar. Fix: same scorecard; diversity of thought.
5. **Slow offer.** Candidate takes competing offer. Fix: pre-draft comp before finals.
6. **Recruiter misalignment.** No exclusive terms. Fix: written fee + guarantee.

## Execution Artifacts

- `references/recruiter-partners.md` — Betts, It's Destiny, when to use each
- `references/offer-negotiation.md` — Employer + candidate negotiation playbook
- `references/inclusive-recruiting.md` — Destiny model + re:Work alignment
- `templates/sourcing-outreach.md` — Passive candidate messages
- `templates/offer-package-checklist.md` — Written offer requirements
- `templates/candidate-negotiation-script.md` — Candidate-side negotiation
- `templates/inclusive-interview-scorecard.md` — Bias-resistant scorecard
- `hiring-by-role` → interviewer-questions-gtm, candidate-questions-to-ask, interview-experts
- `revenue-team-onboarding` → onboarding-questions (post-hire)
- `gtm-leadership` → resignation-playbook (attrition learnings)
- `scripts/check-output.py` — Validates recruiting deliverables

## Related Skills

- `gtm-role-descriptions` — JDs, comp templates, benchmarks
- `job-posting-strategy` — Where to post and distribute
- `hiring-by-role` — Interview design and role scorecards
- `gtm-leadership` — Hire decision, manager readiness
- `sales-team-building` — Hire sequence by ARR
- `employment-compliance` — Offer letters, legal
- `hiring-agencies` — Outbound agencies (not headhunters)

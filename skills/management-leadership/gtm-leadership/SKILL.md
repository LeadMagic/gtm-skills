---
name: gtm-leadership
description: >-
  GTM leadership playbook for revenue leaders — how to hire and fire sales
  talent, run difficult conversations (performance, comp, forecast honesty),
  and design SaaS comp strategies. Grounded in Roberge, Lemkin, Kim Scott,
  Bridge Group, Pavilion, and WbD. Use when firing a rep or leader, having a
  hard conversation, evaluating a VP/CRO hire, or approving comp plans. Triggers
  on: "fire sales rep", "fire VP Sales", "difficult conversation", "performance
  conversation", "PIP", "terminate employee", "GTM leadership", "sales leader
  evaluation", "when to fire", "how to hire sales leader", "crisis management",
  "incident comms", "outage communication", "holding statement", "PR crisis".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.7.0"
  author: LeadMagic
  category: management-leadership
  tags: [gtm-leadership, hiring, firing, difficult-conversations, comp, performance, pip, revenue-leaders, team-design, project-management]
  related_skills: [gtm-recruiting, gtm-role-descriptions, sales-team-building, hiring-by-role, team-management, sales-coaching, employment-compliance, buyer-indecision, pipeline-management, gtm-operations, revenue-team-onboarding]
  frameworks:
    - "Mark Roberge — Sales Acceleration Formula (hire traits, train skills)"
    - "Jason Lemkin — SaaStr GTM leadership and hiring triggers"
    - "Kim Scott — Radical Candor (difficult conversations)"
    - "Bridge Group — SaaS compensation benchmarks"
    - "Pavilion — Revenue leader standards and comp council data"
    - "Winning by Design — REKS coaching and POD leadership"
    - "Patty McCord — Powerful (talent density, no brilliant jerks)"
    - "Marc Benioff — V2MOM annual alignment, trust-based culture"
    - "Force Management — Cross-Functional Alignment Cadence"
    - "RevOps Co-op — RevOps project manager hiring guide"
    - "John McMahon — The Qualified Sales Leader (MEDDICC, inspection, board reporting)"
    - "Frank Slootman — Amp It Up (execution, consumption GTM alignment)"
    - "Snowflake GTM case study — consumption land-expand (Degnan, public earnings)"
    - "Ali Ghodsi / Ron Gabrisko — Databricks PLG-to-enterprise hybrid"
    - "Jason Lemkin — bad news transparency, investor trust in crisis months"
    - "Laurie Ruettimann — layoff and workforce crisis humanity"
---

**Crisis leadership disclaimer:** GTM/founder crisis playbooks in this skill are **not legal advice**. Security breach notifications, regulatory inquiries, and liability language → counsel + `deal-desk/references/legal-gtm-playbook.md` (Pattern 29) before external statements.

# GTM Leadership

## Overview

Revenue leadership is not "hit the number and yell louder." GTM leaders hire
the machine, design comp that produces the right behavior, coach through
difficult truth, and remove people who poison velocity — fast enough to
protect the team, slow enough to be fair. The mistake: firing without a
documented system, or avoiding hard conversations until a quarter is lost.

This skill is the **people operations layer** for GTM leaders: hire decision
framework, performance and termination conversations, comp approval, and when
to exit a leader. Comp strategy (canonical) → `executive-compensation/references/gtm-compensation-strategy.md`
(Pattern 35). IC bands + JDs → `gtm-role-descriptions`. Interview scorecards →
`hiring-by-role`. Hire sequence → `sales-team-building`.

## When to Use

- "How do I fire a sales rep / AE / SDR?"
- "When should I fire my VP Sales?"
- "Script for difficult performance conversation"
- "PIP for underperforming AE"
- "How to tell someone they're not hitting quota"
- "Approve a comp plan for my team"
- "Evaluate CRO / VP Sales candidate"
- "Conversation about forecast sandbagging"
- "Employee resigned — what do I do?"
- "Exit interview questions"
- "Counter-offer when rep quits"
- "Security breach — what do we tell customers?"
- "Outage war room — who owns what?"
- "Draft holding statement / crisis comms"
- "Layoff communication plan"
- "Bad press going viral — CEO response?"

Do not use for legal termination requirements alone — load `employment-compliance`.
Do not use for statement liability review alone — load `deal-desk` → `legal-gtm-playbook.md`.
Do not use for buyer-side indecision — load `buyer-indecision` (JOLT).

## Authoritative Foundations

- **Mark Roberge.** Hire for traits (Coachable, Curious, Prior success,
  Intelligent, Work ethic); train for skills. Mis-hire cost compounds — use
  structured scorecards, not gut. Ramp is a curriculum, not sink-or-swim.
- **Jason Lemkin (SaaStr).** Founder closes 10–20 deals before first AE. VP
  Sales after ~$2M ARR with reps at quota. Rushed leadership searches (30 days)
  produce attribution-error hires — "scaled X to Y" at wrong stage.
- **Kim Scott — Radical Candor.** Care personally + challenge directly. Difficult
  conversations use Behavior → Impact → Ask. Ruinous empathy (avoiding truth)
  kills sales teams faster than one bad quarter.
- **Bridge Group / Pavilion.** Quota:OTE ~5:1 for ICs; OTE ≤20% of year-1 quota.
  CRO comp increasingly gated on ARR + NRR + efficiency — not bookings alone.
- **Winning by Design REKS.** Before firing IC: diagnose Results → Efforts →
  Knowledge → Skills. Wrong layer = wrong fix (training vs territory vs fit).
- **Patty McCord — Powerful.** Talent density: keep people who make others
  better. Fire brilliant jerks and passive resistors — culture fit is performance.
- **Marc Benioff — V2MOM.** Annual **Vision, Values, Methods, Obstacles, Measures**
  aligns the revenue org to company strategy — not vanity OKRs. Publish internally;
  cascade quotas from Measures. Load `references/benioff-v2mom-guide.md`.
- **Force Management — Cross-Functional Alignment Cadence.** Weekly pipeline +
  handoff hygiene; monthly GTM scorecard (Sales + Marketing + CS); quarterly
  territory, quota, and pod economics true-up. Reporting structures by ARR stage
  and span of control (6–8 ICs per manager). See `references/force-management-playbook.md`.
- **John McMahon — *The Qualified Sales Leader*.** 5× CRO; Snowflake/MongoDB
  board. MEDDICC as shared operating language; **inspect what you expect** in
  weekly 1:1s (deal evidence, not rep confidence); hire **managers before rep
  waves**; 5-quarter board model with productivity-per-rep and new-logo vs
  expansion mix. Anti-patterns: happy ears, lone wolves, premature scale.
  Canonical → `references/cro-enterprise-strategy.md` (Pattern 31).
- **Frank Slootman — *Amp It Up*.** Snowflake CEO era: align sales comp to
  **consumption** (not bookings on usage-based revenue); unified exec metrics;
  industry GTM pods; deployment velocity over CS bureaucracy. Case study section
  in `cro-enterprise-strategy.md`.
- **Databricks hybrid GTM (Ghodsi / Gabrisko).** PLG for acquisition, enterprise
  field for scale — complementary layers. Technical sellers run POCs; consumption
  (DBU) pricing matches cloud buyer mental models. See `cro-enterprise-strategy.md`.
- **Jason Lemkin — crisis stakeholder trust.** Never skip monthly investor updates
  in bad months; explain stumbles before they hit MRR; own mistakes fast. Source:
  [Handling Bad News](https://www.saastr.com/handling-bad-news/). Pairs with
  `investor-updates` and Pattern 33.
- **Laurie Ruettimann — workforce crises.** Layoffs: early-week notification,
  written summary, HR/legal script — no ad-lib. Internal comms stay frequent and
  human. Source: [Approach Layoffs](https://laurieruettimann.com/how-to-approach-layoffs-at-your-organization/).

## Step-by-Step: Crisis Leadership (Executive)

**Canonical:** `references/crisis-management-playbook.md` · Pattern 33 in `using-gtm-skills`

1. **Classify severity** (1–4) — escalate up when uncertain in the first hour
2. **Stand up war room** — IC (eng), comms lead, CS captain, legal (Sev 3+), CEO voice (Sev 2+)
3. **First 60 minutes** — internal facts doc → holding statement → status page if customer-visible → internal memo before social
4. **Audience order** — employees → affected customers → investors (Sev 3+) → press only if public
5. **Apology framework** — Acknowledge → Own → Act → Follow up (counsel reviews Sev 3+)
6. **Post-crisis** — blameless post-mortem; retention vs 90-day baseline; quarterly tabletop

**Preparedness (before crisis):** `references/crisis-preparedness-checklist.md`  
**Statement shells:** `references/templates/crisis-holding-statement.md`, `crisis-customer-email.md`, `crisis-internal-memo.md`  
**PR expert context:** `references/saas-pr-crisis-experts.md`  
**Breach path:** `references/gtm-data-exchange-playbook.md`, `gtm-security-hygiene-basics.md`

## Step-by-Step: Annual GTM Alignment (V2MOM)

Before Q1 hiring and comp finalization:

1. Read company vision — draft GTM Vision (1–2 sentences)
2. Define Values that constrain behavior (trust, forecast honesty, customer success)
3. List Methods (prioritized plays) with owners — POD launch, CS expansion, etc.
4. Surface Obstacles honestly — ramp gaps, tooling debt, ICP confusion
5. Set 5–8 Measures with baseline → target — ARR, NRR, forecast accuracy, hygiene
6. Cascade to manager V2MOMs; quotas must trace to Methods

Template: `templates/v2mom-gtm.md`  
Enterprise CRM tie-in: **crm-toolkit** → benioff-enterprise-playbook

## Step-by-Step: Hire (GTM Leader Lens)

### Phase 1 — Role and Timing

| Hire | Minimum Trigger | Expert Anchor |
|---|---|---|
| First AE | Founder closed 10–20 deals; playbook exists | Lemkin, Roberge |
| SDR | AEs need pipeline; not before AE motion works | `sales-team-building` |
| Player-coach mgr | 2+ AEs; one at quota 2 quarters | WbD POD |
| VP Sales | $5M+ ARR, proven AE productivity | Betts, Pavilion |
| CRO | $15M+ ARR; unified revenue P&L | Pavilion CRO Council |

Full JD + comp → `gtm-role-descriptions`. Interviews → `hiring-by-role`.

### Phase 2 — Leader Hire Scorecard

Use `templates/hire-decision-scorecard.md`. Weight:

| Criteria | Weight | Evidence Required |
|---|---:|---|
| System-building (not heroics) | 30% | Built comp, ramp, forecast cadence — not inherited |
| Stage-fit | 25% | Same ACV/motion/ARR band as you |
| Quota attainment history | 25% | Last 4 quarters % — numbers, not stories |
| Culture / coaching | 20% | Backchannel refs from direct reports |

**Red flags:** Blames team in references; no documentation of methodology;
only "scaled" at one lucky segment.

### Phase 3 — Offer and Comp Approval

Pick role-specific comp template from **gtm-role-descriptions** (SDR, AE, manager, VP/CRO).
Strategies in **gtm-role-descriptions** → saas-comp-strategies.

Leader approval checklist:
- [ ] Quota:OTE ratio defensible (Bridge Group)
- [ ] Ramp documented for new hires under this leader
- [ ] Clawbacks and draw terms clear
- [ ] Behavior incentives match strategy (quality vs volume)

## Step-by-Step: Coach Before Fire (IC)

### Phase 4 — REKS Diagnosis

Before PIP or exit, run REKS via **sales-coaching** (reks-diagnostic + coaching-plan-30-day templates):

| Layer | Question | Fix If Gap |
|---|---|---|
| Results | Attainment % last 4 quarters? | Territory? Quota? |
| Efforts | Activity and pipeline coverage? | Coaching, discipline |
| Knowledge | Knows product, ICP, process? | Enablement |
| Skills | Discovery, demo, negotiate? | Role-play, shadow |

If Results fail after Efforts/Knowledge/Skills are adequate → fit issue, not training.

### Phase 5 — Difficult Conversation (Radical Candor)

Structure every hard conversation:

1. **Prepare:** Facts only (CRM, attainment, call recordings). No labels.
2. **Open:** "I want to talk about [specific metric/behavior]."
3. **Behavior → Impact:** "When you [X], the impact is [Y]."
4. **Ask:** "What's your read? What would you change?"
5. **Agree:** Written next steps + date.
6. **Document:** Same day in HR file / manager log.

Templates: `templates/difficult-conversation.md`, `templates/performance-pip.md`.

**Topics GTM leaders avoid but must have:**
- Quota miss pattern (3+ weeks pipeline hygiene)
- Forecast sandbagging / optimism
- Toxic behavior toward SDRs or CS
- Skipping CRM / methodology
- Comp plan gaming (bad-fit deals for commission)

## Step-by-Step: Fire (IC or Leader)

### Phase 6 — When to Terminate

**IC sales (AE/SDR):** After documented PIP (typically 30–60 days) OR immediate
for integrity violations (falsified pipeline, harassment, policy breach).
QuotaSignal: AE mis-hire total cost ~$484K over 24 months — delay is expensive.

**Sales leader (VP/CRO):** Two grounds (Rose Garden / operator consensus):
1. **Missed targets** with no credible system improvement after 2+ quarters
2. **Culture damage** — team attrition, blame shifting, toxic environment

CRO churn cycle: firing for output without fixing role design repeats failure.
Evaluate: did they build forecast discipline, comp, ramp — or inherit?

### Phase 7 — Termination Execution

1. **Legal:** HR + `employment-compliance` — documentation, timing, severance
2. **Meeting:** Short, factual, no debate. Same day remove system access.
3. **Script:** `templates/termination-conversation.md`
4. **Team comm:** Same day — what changes, interim owner, no gossip
5. **Pipeline:** Manager owns all opps within 24h; reassign in CRM

**Never:** Surprise firing without prior documented feedback; firing in public;
letting leader "resign" without addressing team impact when culture was toxic.

## Step-by-Step: Resignation (Voluntary Exit)

Load `references/resignation-playbook.md` — distinct from termination.

### Phase 8 — Employee Gives Notice

1. **Receive with dignity** (Kim Scott) — thank them; don't guilt or panic-counter
2. **Confirm last day** — per policy; extend only for critical customer handoff
3. **Same-day CRM** — reassign all opps within 24h (Lemkin pipeline rule)
4. **Handoff doc** — `templates/resignation-handoff-checklist.md`
5. **Team comm** — factual; interim owner named
6. **Counter-offer** — only if you would change comp/role without resignation threat

Script: `templates/resignation-conversation-script.md`

### Phase 9 — Exit Interview & Learnings

- HR or skip-level runs `templates/exit-interview-questions.md` — not manager
- Aggregate themes quarterly; feed onboarding fixes → `revenue-team-onboarding`
- Document boomerang eligibility

## SaaS Comp Strategies (Leader View)

Leaders approve comp — templates in `gtm-role-descriptions`:

| Strategy | When | Risk |
|---|---|---|
| Linear 50/50 AE | Default SMB/mid-market | Pays volume over quality |
| Accelerated 100–120%+ | Growth mode | Mercenary short-term deals |
| SDR on SQO not dials | Outbound quality | Under-activity if threshold low |
| CSM on NRR not tickets | Expansion motion | Ignores logo churn if GRR weak |
| CRO gated ARR+NRR+EBITDA | Scale stage | Complexity; needs RevOps model |

Full reference: **gtm-role-descriptions** → saas-comp-strategies.

## GTM Project Team Design

For launches, migrations, and QBRs — not line-management org charts — load
`gtm-operations` → `skills/gtm-ops/gtm-operations/references/team-design-gtm-projects.md`.

| Concept | Leader action |
|---|---|
| **DRI** | Name one person per project; exec sponsor = Informed unless escalation |
| **Launch pod** | Temporary 4–8 week matrix: ops + creative + enablement; AEs stay on quota |
| **Span of control** | RevOps IC: 2–3 active projects max; dedicated PM: 4–5 |
| **RACI** | Sign charter before kickoff — `gtm-operations/templates/raci-matrix-template.md` |
| **Ongoing alignment** | Monthly GTM scorecard — `references/force-management-playbook.md` |

Hiring a RevOps project manager: [RevOps Co-op guide](https://www.revopscoop.com/post/hiring-a-revenue-operations-professional-project-manager).

## Output Format

Deliverable by request type:
- **Hire:** scorecard + comp template + JD cross-ref
- **Coach:** difficult conversation script + REKS diagnosis
- **PIP:** 30–60 day plan with weekly milestones
- **Fire:** termination script + team comm draft + pipeline reassignment checklist
- **Resignation:** handoff checklist + manager script + exit interview set

## Quality Check

- [ ] Facts documented before emotional conversation
- [ ] REKS or leader scorecard completed before exit decision
- [ ] Radical Candor structure (care + challenge), not obnoxious aggression
- [ ] Comp approval uses Bridge Group ratios
- [ ] employment-compliance consulted for termination
- [ ] Team and pipeline handoff planned same day as exit

## Common Pitfalls

1. **Ruinous empathy.** Avoiding quota truth until Q4. Fix: weekly pipeline
   reviews with documented feedback.
2. **Firing the number, not the system (leaders).** Replace VP without fixing
   role scope. Fix: hire for system-building; 2-quarter runway.
3. **No PIP paper trail.** Legal and moral risk. Fix: written expectations + dates.
4. **Comp plans that reward bad revenue.** Bookings without NRR. Fix: clawbacks,
   CRO gates at scale.
5. **Backchannel skip on leader hires.** Supervisors lie. Fix: 2+ direct report refs.

## Step-by-Step: CRO 90-Day Plan (Enterprise)

Load `references/cro-enterprise-strategy.md` for full checklists. Summary:

| Phase | Focus |
|---|---|
| Weeks 1–2 | Forecast audit (4 quarters); MEDDICC CRM coverage |
| Weeks 3–4 | Weekly inspection live; top slipping commits coached |
| Weeks 5–6 | Territory fairness; manager span 6–8 ICs |
| Weeks 7–8 | Comp audit — bookings vs consumption vs NRR |
| Weeks 9–12 | Board 5-quarter model; hiring vs productivity curve |

**Board metrics:** Tie to `gtm-metrics` → `public-company-gtm-metrics.md` and Meritech at $100M+ ARR.

## Execution Artifacts

- `references/crisis-management-playbook.md` — **canonical crisis home** (severity matrix, war room, channels)
- `references/crisis-preparedness-checklist.md` — contact tree, status page, tabletop cadence
- `references/saas-pr-crisis-experts.md` — Lemkin, Highwire, Offleash, Ruettimann
- `references/templates/crisis-holding-statement.md` · `crisis-customer-email.md` · `crisis-internal-memo.md` · `crisis-faq-for-support.md`
- `references/cro-enterprise-strategy.md` — **canonical CRO home** (McMahon, Snowflake, Databricks)
- `references/expert-frameworks.md` — GTM leader experts map
- `gtm-operations/references/team-design-gtm-projects.md` — DRI, launch pods, project span of control
- `references/force-management-playbook.md` — Repo root: alignment cadence, reporting structures, pod economics
- `references/benioff-v2mom-guide.md` — V2MOM planning system
- `templates/v2mom-gtm.md` — annual GTM alignment template
- `templates/hire-decision-scorecard.md`
- `templates/difficult-conversation.md`
- `templates/performance-pip.md`
- `templates/termination-conversation.md`
- `references/resignation-playbook.md` — voluntary exit, counter-offers, handoff
- `templates/resignation-conversation-script.md` — manager receiving notice
- `templates/resignation-handoff-checklist.md` — pipeline + account transfer
- `templates/exit-interview-questions.md` — HR / skip-level exit interview
- `scripts/check-output.py` — Validates hire, coach, PIP, fire, resignation, and crisis deliverables

## Related Skills

- `gtm-role-descriptions` — JDs, comp plan templates, org charts
- `sales-team-building` — Hire sequence, PODs, comp models
- `hiring-by-role` — Interview scorecards
- `team-management` — 1:1s, OKRs, delegation (general management)
- `sales-coaching` — REKS, deal coaching
- `employment-compliance` — Legal termination requirements
- `buyer-indecision` — JOLT for stuck deals (buyer side, not HR)
- `investor-updates` — investor/board comms during Sev 3+ crises
- `customer-marketing` — reputation, negative reviews, advocacy pause rules
- `cs-playbooks` — customer-facing incident comms and FAQ handoff
- `deal-desk` — legal-gtm review before external statements (Pattern 29)

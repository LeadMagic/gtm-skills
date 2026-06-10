# Job Description — GTM Engineer

**Company:** [Name] · **Stage:** [Seed/Series A] · **ARR:** ~$[X]M  
**Location:** [Remote / Hybrid / City] · **Team:** Hire #[N] on GTM Systems  
**Reports to:** [Head of Revenue Ops / VP Sales / Founder]

---

## Why this role exists

[One paragraph: business constraint. Example: "Our SDR team waits 2–3 days for enriched tier-1 lists. CRM fields are 40% incomplete, breaking routing and forecast. Founder-built Clay tables don't scale. We need a GTM Engineer to own enrichment → scoring → CRM → sequencer workflows so reps spend time selling, not spreadsheet wrangling."]

---

## What you'll own

- Design and maintain **Clay** tables: ICP scoring, enrichment waterfalls, verify steps, credit efficiency
- Build **automation** (n8n or CRM-native) for inbound routing, signal plays (funding, hiring, job change), and CRM sync
- Own **data hygiene**: dedupe rules, field mapping, required fields at stage gates (`pipeline-management`)
- Partner with SDR/AE leads on list SLAs and outbound infrastructure (`cold-email-strategy`, `domain-infrastructure`)
- Document every production workflow: owner, trigger, rollback, and cost per run
- Support **RevOps** on reporting inputs — not forecast ownership unless agreed in title

---

## What success looks like

**First 90 days**
- Stack audit complete; top 3 workflows documented with runbooks
- Tier-1 account lists refreshed within **24 hours** of signal
- Inbound routing SLA **<5 minutes** during business hours
- CRM required-field compliance **≥90%** on new opps
- One signal play live end-to-end (e.g. funding or hiring signal → sequence)

**12 months**
- **95%+** uptime on scheduled enrichment/sync jobs
- Measurable lift: SQOs from automated plays, or **20%+** reduction in rep admin time (survey + activity data)
- Agency/contractor Clay work transitioned in-house or deprecated
- GTM tool spend per rep within budget (`gtm-tool-cost-model`)

---

## Who you are

We're looking for people who have **shipped production GTM workflows**, not just attended courses:

- **Built** Clay (or equivalent) tables used by a sales team — tell us what metric moved
- **Designed** enrichment waterfalls with verify and dedupe — not single-provider lookup
- **Integrated** CRM ↔ sequencer ↔ enrichment with error handling you can explain
- **Write** clear runbooks so RevOps or a peer can operate your workflows when you're out
- **Care** about data quality as much as automation speed

**Strong plus:** n8n (or similar) in production; SQL against a warehouse; API debugging; `clay-loops-toolkit`-style recurring plays.

**Not required:** Computer science degree, "5+ years in SaaS," quota-carrying sales experience.

**This is not:** A Sales Engineer (deal demos), a Growth Engineer (PLG product experiments), or a pure RevOps analyst (forecast-only). See `references/gtm-engineer-hiring.md` for role boundaries.

---

## Org context

- **Reports to:** [RevOps lead / VP Sales / Founder]
- **Works with:** [N] SDRs, [N] AEs, [RevOps / Marketing ops]
- **Team today:** [X] in GTM; [Y] in engineering
- **Stack today:** [CRM], [Clay], [sequencer], [enrichment vendors], [n8n/Zapier]

---

## Compensation & benefits

| Component | Range |
|---|---|
| **Base salary** | $[95–130]K (GTM Engineer) / $[125–165]K (Senior) |
| **Bonus** | 10–20% on documented OKRs (uptime, SLA, cost per enrich) |
| **Equity** | [0.15–0.35]% (4yr vest, 1yr cliff) |
| **Benefits** | [Health, remote stipend, etc.] |

Geo policy: [US remote bands / SF/NYC adjustment — see `comp-benchmarks.md`]

---

## How to apply

Send:

1. **Resume or LinkedIn**
2. **Portfolio link** — Loom, GitHub, or doc walking through **one production workflow** you built (Clay table, n8n flow, or CRM automation). Include: problem, architecture diagram, metric outcome.
3. **Short note:** What broke most often in your last GTM stack and how you fixed it.

We respond to candidates who show artifacts, not buzzwords.

---

*Template version: `gtm-role-descriptions` · Interview loop: `hiring-by-role` · Onboarding: `revenue-team-onboarding`*

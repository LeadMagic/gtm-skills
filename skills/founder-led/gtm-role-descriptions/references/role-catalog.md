# GTM Role Catalog — Full JD Blocks

Copy the relevant section into `templates/job-description.md`. Adjust comp for geo and ACV.

---

## SDR / BDR (Outbound)

**Title:** Sales Development Representative (Outbound)

**Why this role exists:** Our AEs are at capacity on inbound; we need predictable qualified pipeline from outbound to hit [Q target] without founder-led prospecting.

**What you'll own:**
- Research and prioritize accounts in ICP tier 1–2
- Multi-channel outbound (email, LinkedIn, phone) via [sequencer]
- Book qualified discovery meetings that meet SPICED-ready criteria
- Maintain CRM hygiene and activity logging
- Partner with AEs on handoff quality (meeting brief, stakeholder map)

**90-day success:** 15+ qualified meetings held/month; 30%+ SQO conversion; ramp complete by day 60.

**12-month success:** Top-quartile team attainment; promoted to AE track or senior SDR.

**Who you are:**
- Closed-loop feedback seeker (Coachable)
- Researched prospects before outreach (Curious)
- Hit or exceeded SDR quota before (Prior success)
- Writes clear, personalized messages (Intelligent)
- Consistent daily execution (Work ethic)

**Org:** Reports to [SDR Manager / Head of Sales]. Partners with [N] AEs. Team size today: [X].

**Comp:** $58–85K OTE (60/40 base/variable). Variable on qualified meetings held ($175–275/meeting) + SQO bonus. Equity: [range]. Benefits: [list].

**Apply:** Resume + 3-sentence note on best outbound campaign you ran + expected OTE.

---

## SDR / BDR (Inbound)

**Title:** Sales Development Representative (Inbound)

**Why this role exists:** Inbound volume exceeds AE capacity; we need fast, high-quality qualification and routing.

**What you'll own:**
- Respond to inbound within SLA (<5 min business hours)
- Qualify against ICP and SPICED-lite criteria
- Route to correct AE; reject bad-fit fast with nurture path
- Track source attribution and conversion by channel

**90-day success:** <5 min response SLA; 25%+ inbound-to-meeting rate on tier-1 leads.

**Comp:** Same OTE band as outbound; variable weighted to SQO and speed-to-lead.

---

## Account Executive (Mid-Market)

**Title:** Account Executive

**Why this role exists:** Founder has closed [N] deals proving PMF; we need a full-cycle AE to own $[X]K–$[Y]K ACV deals without founder on every call.

**What you'll own:**
- Full-cycle sales: prospect → close → handoff to CS
- Run SPICED discovery; MEDDICC scorecard from Solution stage
- Forecast accurately in CRM weekly
- Partner with SDR on target account plans
- Hit quarterly ARR quota with <90-day sales cycle target

**90-day success:** Pipeline 3× quota; 2+ closed deals or advanced late-stage opps.

**12-month success:** 80%+ quota attainment; positive feedback from CS on handoffs.

**Who you are:**
- Sold B2B SaaS with similar ACV (not "5 years in sales")
- Can demo without a script after week 2
- Brings a repeatable pipeline source (network, vertical, playbook)

**Org:** Reports to [Head of Sales / VP Sales]. [N] SDRs supporting. Hire #[X] on sales team.

**Comp:** $130–190K OTE (50/50). Quota $650K–$950K ARR (OTE × ~5). Accelerators above 100%. Ramp: 90 days. Equity: [range].

**Apply:** Resume + last 4 quarters attainment % + largest deal closed (size, cycle, your role).

---

## Senior / Enterprise AE

**Title:** Senior Account Executive (Enterprise)

**Why this role exists:** Enterprise deals ($50K+ ACV) require multi-threading, security review, and EB access — mid-market AEs can't carry this motion alone.

**What you'll own:**
- Own $80K+ ACV opportunities end-to-end
- Multi-thread: Champion, EB, legal, security stakeholders
- MEDDICC scorecard ≥14 before Proposal stage
- Executive-level discovery and business case creation
- Mentor 1 mid-market AE on enterprise graduation

**Comp:** $160–220K OTE. Quota $800K–$1.2M ARR. Higher accelerators; President's Club at 120%+.

---

## Player-Coach Sales Manager

**Title:** Sales Manager (Player-Coach)

**Why this role exists:** We have [N] AEs; founder can't coach and sell. Need a manager who still carries quota while building the team.

**What you'll own:**
- Team quota + personal patch (typically 30–50% IC quota)
- Weekly 1:1s, pipeline reviews, forecast calls
- Hire and ramp next AE/SDR
- Implement `pipeline-management` stage gates and MEDDICC reviews

**When to hire:** 2+ AEs; at least one at quota 2 quarters.

**Comp:** $160–220K OTE. Team quota = sum of rep quotas + patch.

---

## VP Sales / Head of Sales

**Title:** Vice President of Sales

**Why this role exists:** ARR at $[X]M; founder must exit day-to-day selling. Need a leader to build repeatable revenue engine.

**What you'll own:**
- Org ARR target and hiring plan
- Comp plan design and quota allocation
- Sales methodology (SPICED/MEDDICC) enforcement
- Board-ready forecast and GTM metrics
- Build manager layer when team hits 6+ AEs

**When to hire:** $5M+ ARR, proven AE productivity, not before.

**Comp:** $220–350K+ OTE. 60/40 or 70/30 at VP level. Significant equity.

**Source:** Betts, Pavilion, investor referrals — not generic job boards.

---

## RevOps / Sales Operations

**Title:** Revenue Operations Manager

**Why this role exists:** CRM data is unreliable; forecasting is guesswork; routing breaks at scale.

**What you'll own:**
- CRM architecture, fields, automation (stage gates, required fields)
- Forecast model and weekly accuracy reporting
- Lead/account routing and enrichment waterfall
- GTM tech stack admin (`revops-tech-stack`)
- Support comp plan reporting and quota crediting

**Comp:** $95–150K salary + 10–15% OKR bonus + equity. No quota.

**Not the same as GTM Engineer** — RevOps owns operating model and forecast; GTM Engineer builds Clay/n8n workflows and enrichment systems. Split titles when team exceeds ~10 GTM staff. Full comparison: `gtm-engineer-hiring.md`.

---

## GTM Engineer

**Title:** GTM Engineer (or Senior GTM Engineer)

**Why this role exists:** Reps wait days for enriched lists; Clay tables and CRM sync are founder-maintained; signal plays (funding, hiring, job change) break when someone is on vacation. We need a builder who ships production revenue automation — not another spreadsheet operator.

**What you'll own:**
- Clay tables and loops: enrichment waterfalls, ICP scoring, verify, credit optimization (`clay-toolkit`, `clay-loops-toolkit`)
- Orchestration: n8n (or equivalent) for routing, webhooks, CRM ↔ sequencer sync (`n8n-automation`)
- Data hygiene: dedupe, field mapping, required fields at stage gates
- Signal plays end-to-end: trigger → enrich → score → route → sequence
- Runbooks for every production workflow (owner, rollback, cost)
- Partner with RevOps on reporting inputs — forecast remains RevOps unless dual-hat

**90-day success:** Stack audit done; inbound routing <5 min SLA; tier-1 lists refreshed <24h; CRM required-field compliance ≥90%; one live signal play.

**12-month success:** 95%+ job uptime; measurable SQO or admin-time lift; agency Clay work brought in-house.

**Who you are:**
- Shipped Clay/n8n/CRM automation used by a sales team — portfolio required
- Designs waterfalls with verify and dedupe, not single-provider lookup
- Writes runbooks another ops person can operate
- Ties work to pipeline metrics (SQO, SLA, hygiene %) — not "cool automations"

**Not this role:** Sales Engineer (deal demos/POCs), Growth Engineer (PLG product loops), pure RevOps (forecast-only). See `gtm-engineer-hiring.md`.

**Org:** Reports to [RevOps lead / VP Sales / Founder]. Partners with SDR/AE leads and RevOps. Hire #1 GTM systems at $500K–$2M ARR when founder spends >10 hrs/week on Clay.

**Comp:** $95–130K base (IC3) / $125–165K (IC4 Senior). Bonus 10–20% on OKRs (uptime, SLA, cost per enrich). Equity: 0.15–0.35%. No quota.

**Apply:** Resume + portfolio link (Loom/GitHub/doc of one production workflow) + note on biggest stack failure you fixed.

**Templates:** `templates/gtm-engineer-jd.md` · **Interview:** `hiring-by-role` → `gtm-engineer-scorecard.md`

---

## Sales Enablement

**Title:** Sales Enablement Manager

**Why this role exists:** Ramp time >90 days; reps reinvent decks; win/loss patterns not captured.

**What you'll own:**
- Onboarding curriculum (30/60/90 ramp)
- Playbooks aligned to pipeline stages (`sales-enablement`)
- Battlecards, demo environments, certification
- Content library and LMS

**When to hire:** 5+ AEs; ramp cost exceeds enablement headcount.

**Comp:** $100–150K salary + equity.

---

## Customer Success Manager

**Title:** Customer Success Manager

**Why this role exists:** NRR below 100%; expansion is reactive; churn tied to onboarding gaps.

**What you'll own:**
- Book of [N] accounts; segment by ARR/tier
- Onboarding through first value milestone (Bowtie left side)
- QBRs, health scores, expansion identification
- Churn save plays and executive escalation

**Comp:** $72–115K OTE (70/30). Variable on NRR/GRR/expansion ARR — not ticket volume.

---

## Demand Generation Manager

**Title:** Demand Generation Manager

**Why this role exists:** Pipeline gap can't be solved by outbound alone; need paid + content + events feeding SDR/AE.

**What you'll own:**
- Channel mix (paid, content, events, partnerships)
- MQL → SQL conversion with SDR alignment
- Attribution and CAC by channel
- Budget against CAC:LTV guardrails

**Comp:** $100–150K salary + equity. Bonus on SQL cost and pipeline sourced.

---

## CRO (Scale)

**Title:** Chief Revenue Officer

**Why this role exists:** Sales, CS, and sometimes Marketing need unified P&L ownership at $20M+ ARR.

**What you'll own:** Full revenue org; board metrics; GTM strategy; M&A integration if applicable.

**Comp:** $300–500K+ total comp + significant equity. Betts / executive search standard.

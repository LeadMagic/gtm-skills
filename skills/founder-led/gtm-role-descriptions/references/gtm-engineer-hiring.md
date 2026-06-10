# GTM Engineer Hiring — Role Definition, Timing, and Handoff

**Canonical home:** `gtm-role-descriptions` (JD + comp + org placement).  
**Interview loop:** `hiring-by-role` → `templates/gtm-engineer-scorecard.md`, `templates/interviewer-questions-gtm.md`.  
**Onboarding:** `revenue-team-onboarding` (systems access + 30-60-90 for ops roles).

---

## Role Definition: GTM Engineer vs Adjacent Roles

Use this table before writing a JD — titles are overloaded in the market.

| Role | Primary output | Buyer / stakeholder | Core skills | Not this role |
|---|---|---|---|---|
| **GTM Engineer** | Automated revenue workflows — enrichment, routing, sequences, signal plays, CRM sync | RevOps, Sales, Marketing leaders | Clay/n8n, APIs, SQL, CRM schema, data hygiene, experiment velocity | Does not own forecast, comp plans, or board reporting |
| **RevOps / Sales Ops** | Forecast accuracy, CRM governance, routing rules, comp crediting, GTM metrics | CRO, VP Sales, Finance | Salesforce/HubSpot admin, reporting, process design, cross-functional alignment | Not a substitute for building Clay tables or writing integration code at scale |
| **Sales Engineer (SE)** | Technical win on deals — demos, POCs, RFPs, security questionnaires | AE + prospect eval team | Product depth, discovery, demo architecture, objection handling on technical fit | Does not build enrichment waterfalls or outbound automation |
| **Solutions Engineer** | Same family as SE; often post-sales implementation or complex eval | CS + Sales on enterprise deals | Integration design, scoping, SOW support | Not pipeline generation or list building |
| **Growth Engineer** | Product-led growth loops, experimentation, in-app funnels, activation metrics | Product + Growth | Frontend/backend, analytics (Amplitude/Mixpanel), A/B tests, onboarding flows | Not outbound Clay ops or CRM admin (overlap only on data pipelines) |

**Naming rule:** Use **GTM Engineer** when the hire builds and maintains **revenue-facing automation** (Clay, n8n, enrichment, sequences, signal routing). Use **RevOps** when the hire owns **operating model, forecast, and CRM policy**. Many startups combine both in one person at $1–3M ARR — title it honestly in the JD ("GTM Engineer / RevOps") and split when team size exceeds 8–10 GTM staff.

**Market references:**
- [Clay careers](https://www.clay.com/careers) — GTM Engineer as builder role on enrichment + outbound systems
- [Apollo.io GTM roles](https://www.apollo.io/careers) — RevOps + growth systems at scale
- [6sense careers](https://6sense.com/about-us/careers/) — revenue AI + data pipeline engineering adjacent to RevOps
- [RevOps Co-op](https://www.revopscoop.com/) — community standards for ops vs systems builders
- [Pavilion](https://www.joinpavilion.com/) — peer benchmarks for GTM systems hiring at Series B+

---

## When to Hire

### Stage and triggers

| ARR / stage | Hire? | Trigger signals | Team size context |
|---|---|---|---|
| **$0–$500K** (Survival) | Usually no FTE | Founder + contractor/agency (`hiring-agencies`) runs Clay pilot | 0–2 sellers; prove motion first |
| **$500K–$2M** | **First GTM Engineer** (or senior contractor → FTE) | Founder/RevOps spends >10 hrs/week on Clay; enrichment breaks weekly; SDRs wait on lists; CRM sync manual | 2–5 GTM staff; 3+ tools in stack |
| **$2M–$5M** | Dedicated GTM Engineer | Signal plays (funding, hiring, job change) need maintenance; n8n/CRM integrations multiply; agency retainer >$8K/mo for 2+ quarters | 5–12 GTM staff |
| **$5M–$10M** | GTM Engineer + RevOps split | Forecast owned separately from workflow build; security review on integrations; data warehouse for attribution | 12–25 GTM staff |
| **$10M+** | Team: GTM Eng + RevOps + Data | Multi-region CRM, campaign governance (`campaign-governance`), tool consolidation (`revops-tech-stack`) | 25+ GTM staff |

**Hire before agency forever when:** Operating Model ≥6 (`pipeline-management`), agency proved one channel, and monthly agency spend exceeds 50% of a loaded GTM Engineer ($8–12K/mo fully loaded at seed–A).

**Do not hire when:** Operating Model <6 — fix stages and SPICED fields first; a GTM Engineer will automate chaos.

### Agency → in-house graduation

```
hiring-agencies (90-day Clay/outbound pilot)
→ gtm-role-descriptions (GTM Engineer JD)
→ hiring-by-role (scorecard + work sample)
→ revenue-team-onboarding (systems access day 0)
```

---

## Competencies and Observable Signals

| Competency | Weight | Strong signal (5) | Weak signal (1) |
|---|---|---|---|
| **Workflow design** | 25% | Draws source → enrich → score → route → sequence with error handling | "I'd figure it out in Clay" with no schema |
| **Data quality** | 20% | Waterfall + verify; dedupe keys; documents field mapping to CRM | Single-provider lookup; no verify step |
| **CRM fluency** | 15% | Stage gates, required fields, bi-directional sync tradeoffs | Treats CRM as spreadsheet export |
| **API / integration** | 15% | n8n or code: webhooks, retries, idempotency, logging | Manual CSV uploads weekly |
| **GTM judgment** | 15% | Ties automation to pipeline metric (SQOs, speed-to-lead) | Builds cool tables with no revenue outcome |
| **Documentation** | 10% | Runbook + owner + rollback for each production workflow | Tribal knowledge only |

Full scorecard: `../templates/gtm-engineer-scorecard.md`.

---

## Compensation and Leveling

US B2B SaaS benchmarks — validate at offer time; geo-adjust per `comp-benchmarks.md`.

| Level | Title | Base salary | Variable / bonus | Equity (Seed–A) | Typical profile |
|---|---|---|---|---|---|
| **IC3** | GTM Engineer | $95–130K | 10–15% on OKRs (workflow uptime, SQO lift, list SLA) | 0.15–0.35% | 2–4 yrs building GTM automations; owns Clay + CRM |
| **IC4** | Senior GTM Engineer | $125–165K | 15–20% on OKRs + project milestones | 0.25–0.5% | Led stack migration; n8n + warehouse; mentors RevOps |
| **IC5** | Staff / Lead GTM Engineer | $155–195K | 20–25% | 0.35–0.75% | Multi-team workflows; architecture reviews; vendor build vs buy |

**OKR examples (not quota):**
- 95% uptime on enrichment → CRM sync jobs
- Tier-1 account lists refreshed <24h on signal
- SDR time-to-first-touch <5 min on inbound (routing automation)
- Credit spend per enriched contact within budget (`gtm-tool-cost-model`)

**Comp pattern:** Salary-heavy (like RevOps), not OTE/quota. Align bonus to measurable ops outcomes, not ARR closed.

---

## Tool Stack Expectations

Load `revops-tech-stack` for audit methodology. Minimum proficiency by level:

| Tool category | IC3 | IC4+ | Skills to load |
|---|---|---|---|
| **Clay** | Tables, waterfalls, CRM push | Loops, credit optimization, Claygent | `clay-toolkit`, `clay-loops-toolkit`, `clay-automation` |
| **CRM** | HubSpot/Salesforce objects, fields, workflows | Custom objects, Flows, routing | `crm-toolkit`, `salesforce-setup` |
| **Orchestration** | Zapier/Make basics | n8n production workflows | `n8n-automation`, `n8n-toolkit` |
| **Enrichment** | Waterfall design, verify | Vendor evaluation, cost model | `data-enrichment-strategy`, `leadmagic-toolkit` |
| **Sequencing** | Export to Instantly/Outreach | Bi-directional activity sync | `sequencing-toolkit` |
| **Data warehouse** | Read-only SQL for lists | dbt-lite models for attribution | `analytics-toolkit` |
| **Governance** | UTM + campaign IDs in pushes | Naming conventions, audit trail | `campaign-governance` |

**Day-1 access list:** CRM admin (scoped), Clay, n8n, enrichment vendors, sequencer, Slack, Git/versioned workflow docs — see `revenue-team-onboarding/references/security-access-checklist.md`.

---

## Job Description and Posting

- **JD template:** `../templates/gtm-engineer-jd.md`
- **Role catalog block:** `role-catalog.md` → GTM Engineer section
- **Posting channels:** RevOps Co-op job board, LinkedIn, Pavilion referrals, Clay community, niche Twitter/LinkedIn GTM eng circles — not generic RepVue (sales-quota audience)

---

## Interview Loop Summary

5 stages, ~2 weeks (details in `hiring-by-role`):

1. **Screen (30 min)** — portfolio of workflows shipped; metrics moved
2. **Work sample (3–4 hrs, paid)** — build enrichment → score → CRM push for sample ICP
3. **Technical review (60 min)** — walk through work sample; failure modes; cost
4. **GTM judgment (45 min)** — stakeholder scenario with Sales + Marketing conflict
5. **Team / values (30 min)** — documentation habits; incident response

**Portfolio signals:** GitHub or Loom walkthrough of real Clay table, n8n workflow, or open-source GTM template. Red flag: only course certificates, no production artifacts.

---

## Onboarding Handoff

Week 1 priorities for GTM Engineer (extend `revenue-team-onboarding`):

| Day | Focus |
|---|---|
| 0 | CRM admin (scoped), Clay, n8n, enrichment, SSO — same SLA as RevOps |
| 1–2 | Stack audit (`revops-tech-stack`); document existing workflows |
| 3–5 | Ship one quick win (e.g. inbound routing SLA); runbook template |

**30-60-90 OKRs:** See `gtm-engineer-jd.md` success section. Certify on CRM hygiene lab before granting production webhook keys.

**Manager pairing:** RevOps or Head of Sales for GTM context; engineering lead for API/security review if customer data crosses systems.

---

## Related Skills

| Need | Skill |
|---|---|
| Write JD + comp | `gtm-role-descriptions` (this skill) |
| Interview + scorecard | `hiring-by-role` |
| Source + close | `gtm-recruiting` |
| Agency vs hire | `hiring-agencies` |
| Stack audit | `revops-tech-stack` |
| Onboarding | `revenue-team-onboarding` |
| Spend / credits | `gtm-spend-management`, `gtm-tool-cost-model` |

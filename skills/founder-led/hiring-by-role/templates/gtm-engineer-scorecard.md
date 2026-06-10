# GTM Engineer — Interview Scorecard

*Google re:Work structured interview — score independently before panel debrief.*  
*JD + role definition: `gtm-role-descriptions` → `references/gtm-engineer-hiring.md`, `templates/gtm-engineer-jd.md`*

**Candidate:** ___ **Role level:** ☐ IC3 GTM Engineer ☐ IC4 Senior ☐ IC5 Staff  
**Interviewer:** ___ **Stage:** ___ **Date:** ___

---

## Evaluation criteria

| Criteria | Weight | Score (1–5) | Notes |
|---|---|---|---|
| Workflow design (source → enrich → route → act) | 25% | | |
| Data quality (waterfall, verify, dedupe, CRM mapping) | 20% | | |
| CRM fluency (objects, stages, sync tradeoffs) | 15% | | |
| API / integration (webhooks, retries, logging) | 15% | | |
| GTM judgment (ties work to pipeline metrics) | 15% | | |
| Documentation & maintainability | 10% | | |
| **Weighted average** | 100% | | |

**Decision bar:** ≥4.0 strong hire · 3.5–3.9 hire with reservations · <3.5 no hire

---

## Stage 1 — Screen (30 min)

| # | Question | Look for |
|---|---|---|
| 1 | Walk me through a GTM workflow you shipped to production. What metric moved? | Specificity; individual ownership; before/after numbers |
| 2 | How do you structure enrichment — providers, verify, dedupe, CRM push? | Waterfall thinking; cost awareness |
| 3 | Tell me about a workflow that broke in production. How did you detect and fix it? | Monitoring, rollback, blameless postmortem |
| 4 | GTM Engineer vs RevOps vs Sales Engineer — how do you draw the line? | Aligns with `gtm-engineer-hiring.md` boundaries |
| 5 | Why this company and role now? | Research; stack curiosity |

**Portfolio check (async before Stage 2):**
- [ ] Loom/GitHub/doc link received
- [ ] Shows real workflow (not tutorial clone)
- [ ] Explains architecture and outcome

| Portfolio | Score |
|---|---|
| 5 | Production system + metrics + runbook |
| 3 | Academic or agency-only work |
| 1 | No artifacts |

---

## Stage 2 — Work sample (paid, 3–4 hours)

**Task:** Given a CSV of 50 accounts (company, domain, persona title) and access to [Clay sandbox / provided stack]:

1. Enrich firmographic + contact (waterfall with verify)
2. Score ICP fit (document rubric)
3. Push qualified rows to CRM (or mock schema) with field mapping doc
4. Optional: trigger webhook to sequencer stub

**Evaluate:**

| Dimension | 1 (weak) | 5 (strong) |
|---|---|---|
| Data quality | >20% bad emails; no verify | Verify step; dedupe key documented |
| CRM mapping | Random fields | Matches stage-gate requirements |
| Error handling | Silent failures | Retries, dead-letter, or clear error log |
| Cost | Burned credits blindly | Provider order justified; cost estimate |
| Docs | None | README another ops person could run |

**Deliverable checklist:**
- [ ] Architecture diagram (boxes + arrows)
- [ ] Field mapping table
- [ ] Sample output rows
- [ ] Known limitations stated

---

## Stage 3 — Technical review (60 min)

Walk through work sample. Probe:

6. "Why this provider order? What if hit rate is 40%?"
7. "How would this scale to 50K accounts monthly?"
8. "Bi-directional CRM sync — when would you avoid it?"
9. "How do you version and test workflow changes?"
10. "Clay credits doubled — what's your optimization playbook?"

**Tool depth signals:**

| Tool | Strong | Weak |
|---|---|---|
| Clay | Loops vs tables; credit model | Only manual lookups |
| n8n | Nodes, credentials, error workflow | Never used |
| CRM | Custom fields, validation rules | Export-only usage |
| SQL | Joined enrichment to opp data | Cannot read a query |

---

## Stage 4 — GTM judgment (45 min)

**Scenario:** Marketing wants MQL definition lowered. Sales says lists are junk. SDRs want more accounts tomorrow. You own enrichment and routing.

11. "What do you do in week 1? Who do you meet? What data do you pull?"
12. "How do you decide between fixing data vs adding volume?"
13. "Design a signal play for [funding / hiring / job change] — trigger to sequence in 5 steps."

| Dimension | 1 | 5 |
|---|---|---|
| Stakeholder balance | Picks one side | Data-driven proposal with tradeoffs |
| Metric tie-in | Vague | Names SQO, SLA, or hygiene % |
| Pragmatism | Boil the ocean | 80/20 quick win + roadmap |

---

## Stage 5 — Team / values (30 min)

14. "How do you hand off a workflow when you go on vacation?"
15. "Tell me about pushing back on a leader who wanted a brittle automation."
16. "What questions do you have for us?" (`candidate-questions-to-ask.md`)

Look for: low ego, writes runbooks, security awareness (no PII in Slack).

---

## Panel debrief

| Interviewer | Stage | Avg score | Hire? |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

**Required interviewers:** Hiring manager + 1 RevOps/Sales leader + 1 technical (engineering or senior GTM Eng).

**Backchannel (Senior+):** 1 reference who operated their workflows — not only their manager.

---

## Red flags

- Cannot explain own portfolio workflow without slides
- No verify step in enrichment design
- "RevOps does reporting, I just build" — silo mentality
- Dismisses CRM hygiene as "not my job"
- No documentation habit

## Green flags

- Published templates, Clay community posts, or open-source n8n flows
- Mentions credit cost and vendor tradeoffs unprompted
- Asks about stage gates and SPICED fields before building
- Has sunset a workflow — knows when to kill automation

---

*Cross-links: `clay-toolkit`, `n8n-automation`, `revops-tech-stack`, `revenue-team-onboarding`*

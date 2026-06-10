# Crisis Management Playbook (GTM / Founder Lens)

*For SaaS founders, CROs, marketing leaders, and CS when things go wrong — not a corporate PR agency manual.*

**Not legal advice.** Route breach notifications, regulatory inquiries, and liability language to counsel before external statements. Commercial handoff → `deal-desk/references/legal-gtm-playbook.md` (Eunice Buhler, Pattern 29).

**Canonical executive home:** `management-leadership/gtm-leadership` · **Pattern 33** in `using-gtm-skills`

---

## Crisis types matrix (severity 1–4)

| Sev | Examples | First response | CEO visibility | External comms |
|---|---|---|---|---|
| **1 — Routine** | Brief outage (<30 min), single angry G2 review, minor bug affecting <5 accounts | Eng lead + CS manager | Optional | Status page update if customer-visible |
| **2 — Significant** | Multi-hour outage, data sync errors, viral negative thread, exec departure rumor | War room (light) | Comms lead briefs CEO within 2h | Holding statement + customer email to affected segment |
| **3 — Major** | Security incident (suspected breach), widespread data loss, AI output harming customers, layoffs >10%, NRR collapse signal | Full war room | CEO owns external voice | Coordinated: status page, email, FAQ, investor note |
| **4 — Existential** | Confirmed breach with PII, regulatory inquiry, product safety failure, fraud, acquisition-threatening press | Full war room + counsel + (optional) PR agency | CEO + board chair if applicable | Counsel-approved statements only; pause all marketing |

**Escalation rule:** When in doubt, treat as one level higher for the first hour. Downgrade after facts are confirmed.

---

## First 60 minutes checklist

| Minute | Action | Owner |
|---|---|---|
| 0–5 | Confirm incident is real (not false alarm); assign **Incident Commander** | Eng or ops on-call |
| 5–10 | Open war room (Slack channel + bridge); freeze non-essential deploys | IC |
| 10–15 | **Internal-only** facts doc: what we know / don't know / who is affected | IC + eng |
| 15–20 | Notify CEO, comms lead, legal (Sev 3+); CS lead (customer impact) | IC |
| 20–30 | Draft **holding statement** (no admissions); legal skim if Sev 3+ | Comms lead |
| 30–45 | Status page post OR "investigating" banner (outage/breach path) | Eng + comms |
| 45–60 | Internal memo to all staff — facts + "do not post on social" | CEO or comms |
| 60 | Customer email to affected segment if Sev 2+; FAQ to support/sales | CS + comms |

**Do not:** Commit to root cause, fix ETA, or legal liability before eng + counsel align.

---

## War room setup

### Roles

| Role | Typical owner | Responsibility |
|---|---|---|
| **Incident Commander** | VP Eng / CTO / on-call lead | Technical resolution, timeline truth |
| **Comms lead** | CMO, Head of Marketing, or founder | All external + internal messaging drafts |
| **Legal liaison** | GC or outside counsel (Sev 3+) | Statement review, regulatory clock |
| **CS captain** | VP CS / Head of Support | Customer comms, ticket macros, exec callbacks |
| **Sales liaison** | CRO or VP Sales | Prospect/in-flight deal talking points |
| **Eng liaison** | Staff engineer | Single technical voice to comms — no PR in the war room every 10 min |
| **CEO** | Founder/CEO | External voice Sev 2+; investor/board Sev 3+ |

### Operating rules

1. **One facts doc** — single source of truth; timestamp every update.
2. **Engineering fixes first** — comms gets updates on a fixed cadence (e.g., every 30 min), not ad hoc interruptions.
3. **Internal before external** — employees hear from leadership before Twitter does.
4. **No individual hero posts** — unified company voice unless CEO personal thread is deliberate strategy.

---

## Audience sequencing

| Audience | When | Channel | Tone |
|---|---|---|---|
| **Employees** | First (or simultaneous with holding statement) | Slack + email | Factual, calm, no blame |
| **Affected customers** | Within 60–90 min (Sev 2+) | Email + in-app + status page | Empathy + what we're doing + support path |
| **All customers** | If broad impact | Email, status page | Shorter; link to FAQ |
| **Prospects / sales** | Same day | FAQ doc + talk tracks | Honest; don't oversell through crisis |
| **Investors / board** | Same day (Sev 3+) | Email or call | Metrics impact + mitigation + asks |
| **Press / social** | Only if narrative is already public or Sev 4 | CEO or designated spokesperson | Counsel-approved |

---

## When to go silent vs respond fast

| Situation | Respond fast | Go silent (briefly) |
|---|---|---|
| Customer-visible outage | ✓ — status page within 30 min | — |
| Suspected breach | Holding statement only; details after counsel | ✓ — no speculating on scope |
| Viral negative review (1 post) | ✓ — reply within 24h on platform | — |
| Bad press / journalist inquiry | ✓ — "we're looking into it" same day | ✓ — no on-the-record until facts |
| Executive departure (planned) | ✓ — internal then external same day | — |
| Layoffs | ✓ — affected employees first, then company | ✓ — no social celebration posts |
| Legal/regulatory inquiry | — | ✓ — counsel only until cleared |
| AI hallucination harming one customer | ✓ — direct customer outreach immediately | ✓ — no broad blog post until fix verified |

**Lemkin rule:** Bad months need *more* communication, not less — applies to investors and key customers. Source: [How to Handle Bad News](https://www.saastr.com/handling-bad-news/)

---

## Apology framework (ACKNOWLEDGE → OWN → ACT → FOLLOW UP)

Use for customer-facing statements. **Legal reviews all Sev 3+ wording.**

1. **Acknowledge** — Name what happened and who was affected. No minimizing ("minor glitch" when customers lost data).
2. **Own** — Company responsibility without admitting legal liability ("We failed to meet the reliability you expect" vs "We were negligent and liable for damages").
3. **Act** — Concrete steps: fix deployed, credits offered, process changed.
4. **Follow up** — Post-mortem published, timeline for remaining work, single support contact.

---

## Channel matrix

| Channel | Best for | Avoid |
|---|---|---|
| **Status page** (Statuspage, Instatus) | Outages, degraded performance | Breach details with PII scope |
| **Customer email** | Affected accounts, Sev 2+ | Mass email for every minor bug |
| **In-app banner** | Active session awareness | Alarmist copy |
| **Support macros / FAQ** | Sales + CS consistency | Contradicting CEO email |
| **LinkedIn / X (company)** | Holding statement, post-resolution summary | Live-tweeting the war room |
| **CEO personal** | Human tone when company account is cold | Blame-shifting to customers or eng |
| **Investor email** | Sev 3+ business impact | Replacing monthly update rhythm |
| **G2 / review reply** | Single negative reviews | Arguing with reviewers |

**Dark social:** Most B2B buyers discuss vendor incidents in Slack and DMs — monitor via CS and sales, not just public mentions. → `references/chris-walker-mental-models.md`

---

## Crisis-specific paths

### Security breach / data incident

1. Eng contains + forensics; **do not** delete logs.
2. Legal + counsel on notification obligations (customers, regulators, contracts).
3. Customer comms: what data classes *may* be involved, what customers should do, support line.
4. Trust center update; parallel enterprise deal desk track → `references/security-questionnaire-deal-guide.md`, `references/gtm-data-exchange-playbook.md`, `gtm-security-hygiene-basics.md`.

### Outage / downtime

1. Status page + subscriber notifications.
2. Engineering liaison owns ETA language — comms does not invent timelines.
3. Post-mortem within 5 business days; share summary with enterprise customers.

### Bad press / viral negative reviews

1. Assess verifiability — respond to facts, not tone.
2. `customer-marketing` + `review-platforms` for G2/TR; pause advocacy asks.
3. Do not astroturf positive reviews during active crisis.

### Executive departure / layoffs

1. Internal memo first; manager talking points.
2. Layoffs: Laurie Ruettimann patterns — early week, written summary, HR/legal script → `references/saas-pr-crisis-experts.md`
3. `employment-compliance` + `gtm-role-descriptions/references/hr-gtm-playbook.md` for process.

### Product failure / AI harming customer

1. Direct outreach to affected customer(s) before public statement.
2. Disable feature flag if ongoing harm possible.
3. Document prompt/guardrail changes for transparency without exposing trade secrets.

### Legal / regulatory inquiry

**Handoff to legal-gtm.** GTM role: preserve documents, pause destructive comms, single counsel-approved spokesperson.

### Churn wave / NRR collapse (public signal)

1. Treat as Sev 2–3 reputational if G2/LinkedIn narrative forms.
2. `churn-prevention`, `lifecycle` Retention stage → `references/gtm-lifecycle-stages.md`
3. Investor update: honest churn root cause + CS fix plan — never skip the month.

---

## Cross-links

| Topic | Reference |
|---|---|
| Legal review before statements | `deal-desk/references/legal-gtm-playbook.md` (Pattern 29) |
| Customer data handling | `references/gtm-data-exchange-playbook.md` |
| Rep security hygiene | `references/gtm-security-hygiene-basics.md` |
| Investor cadence in hard months | `founder-led/investor-updates` |
| Onboarding / trust rebuild | `customer-success/customer-onboarding` |
| Preparedness checklist | `references/crisis-preparedness-checklist.md` |
| Statement templates | `skills/management-leadership/gtm-leadership/templates/crisis-*.md` |
| PR expert voices | `references/saas-pr-crisis-experts.md`, `references/experts.md` |
| Benchmark / board context | `references/benchmark-reconciliation.md` |

---

## Post-crisis (days 3–90)

| Day | Action |
|---|---|
| 3–7 | Blameless post-mortem; internal share |
| 7–14 | Customer-facing post-mortem (outage) or FAQ update |
| 14–30 | Investor/board update with retention metrics vs pre-crisis baseline |
| 90 | Retention, employee attrition, review sentiment check — did response work? |

**Tabletop cadence:** Quarterly — see `crisis-preparedness-checklist.md`.

# When NOT to Scale

Anti-patterns that destroy runway. **Default: hold or shrink** when any **stop signal** is true.

**Sources:** Jason Lemkin, Mark Roberge, David Skok, QuotaSignal (AE mis-hire), `scale-readiness-gates.md`, `journey-stage-gates.md`.

---

## Stop Signals (Any = Do Not Scale)

| # | Signal | Why it fails | Fix first |
|---|---|---|---|
| 1 | **Churn rising** 2+ quarters | Scale pours water into leaky bucket | `churn-prevention`; cohort analysis |
| 2 | **CAC payback >18 mo** | Growth destroys cash | Channel mix; ICP; pricing |
| 3 | **NRR <100%** while scaling S&M | Negative dollar retention | Expansion + retention playbook |
| 4 | **Founder only seller** at $1M+ ARR | No repeatability | 10–20 founder closes + doc playbook |
| 5 | **No ICP clarity** | Random wins; AE ramp impossible | `gtm-context`, `positioning-messaging` |
| 6 | **WbD Operating Model <6** | Headcount multiplies chaos | `pipeline-management` |
| 7 | **One customer >30% ARR** | False PMF; diligence risk | Diversify before hire/blitz |
| 8 | **VP Sales before $2M ARR** | 70% failure rate | Player-coach or founder-led |
| 9 | **SDR as first hire** | Founder manages + closes | Full-stack AE first |
| 10 | **Paid blitz without payback proof** | Burn with no learning | Prove organic + one paid channel |
| 11 | **Mixed bootstrap/VC playbook** | Wrong spend pace | `end-goal-matrix.md` — pick one path |
| 12 | **Magic number <0.5** | S&M not returning | Fix conversion before spend |

---

## Anti-Pattern Catalog

### Hire to fix product

| Symptom | Reality | Action |
|---|---|---|
| "We need sales to hit target" | Product doesn't retain | PMF tests → `pmf-testing-playbook.md` |
| AE hired before 10 founder deals | AE discovers motion on your payroll | Founder closes 10–20 first |

### Buy tools to fix process

| Symptom | Reality | Action |
|---|---|---|
| Salesforce at $500K ARR | Admin tax; no RevOps | HubSpot/Attio until $5M+ (`saas-outcomes`) |
| Clay before 50 conversations | Automation without message | Founder conversations first |

### Scale spend before capacity

| Symptom | Reality | Action |
|---|---|---|
| 3x ad spend; same sales capacity | Pipeline rots | Hire/automate follow-up first |
| Event sponsorship without outbound | Leads die in CRM | `inbound-triage` + SLA |

### Scale geography/segment before core

| Symptom | Reality | Action |
|---|---|---|
| Second ICP before first retained | Two broken motions | Win one segment NRR >100% |

---

## Shrink / Pause Playbook

When 2+ stop signals active:

| Step | Action | Owner |
|---|---|---|
| 1 | Freeze non-critical hires 90 days | CEO |
| 2 | Cut paid channels with payback >18 mo | Marketing/RevOps |
| 3 | Vendor audit — zombie SaaS | `gtm-spend-management` |
| 4 | Founder back on selling top ICP | Founder |
| 5 | Weekly churn + cohort review | Product + CS |
| 6 | Re-score `scale-readiness-gates.md` monthly | RevOps |

---

## Stage-Specific "Not Yet"

| Stage | Do not yet... |
|---|---|
| Idea | Hire sales; buy enterprise stack |
| PMF search | First AE; paid blitz; raise Series A on story only |
| GTM fit | VP Sales; SDR army; international |
| Scale | PE-style efficiency cuts that kill growth without diagnosis |
| Optimize | Vanity ARR projects; M&A process with NRR <95% |

---

## Go / No-Go: Resume Scaling

**Resume** only when:

- [ ] Stop signals cleared for 2 consecutive months
- [ ] `scale-readiness-gates.md` all categories pass
- [ ] `pmf-signal-checklist.md` still passes (no regression)
- [ ] Runway or burn multiple within path (`bootstrap-vs-vc-paths.md`)

---

## Cross-References

- Scale gates → `scale-readiness-gates.md`
- Journey hold → `saas-outcomes/references/journey-stage-gates.md`
- Spend caps → `gtm-spend-management`
- Mis-hire cost → `sales-team-building` (QuotaSignal)
- Exit distraction → `saas-outcomes/references/exit-potential-scorecard.md`

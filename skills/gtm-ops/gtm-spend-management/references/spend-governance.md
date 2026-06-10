# GTM Spend Governance

*Ben Murray: vendor spend as % of ARR with owners. Scott Brinker: consolidate before buy.*

---

## Principles

1. **No shadow SaaS** — GTM tools on Ramp (or bill pay), not personal cards
2. **One owner per vendor** — accountable for renewal and utilization
3. **Stack check before swipe** — overlap review via `revops-tech-stack`
4. **TCO before approval** — line item in `gtm-tool-cost-model`
5. **Renewal calendar** — 90 / 30 / 7 day alerts; no surprise auto-renew

---

## Approval thresholds

| Annual contract value (ACV) | Approvers | Artifacts |
|---|---|---|
| **< $2,000** | Hiring manager + RevOps | Slack/email one-liner |
| **$2K – $10K** | Department head + Finance | Overlap note + TCO row |
| **$10K – $50K** | CRO or CMO + Finance | `tool-cost-sheet` + vendor security |
| **> $50K** | CEO (+ board if material) | Full `vendor-contracts` procurement |

**Emergency / event spend:** Pre-approved event card with fixed cap (`campaign-governance`).

---

## Prohibited without exception

- Shared login payment on personal card
- Auto-renew opt-in without owner assignment
- Duplicate tools in same category (2 enrichment APIs without migration plan)
- Annual prepay >$10K without Finance sign-off
- Gifting spend outside `strategic-gifting` policy caps

---

## Trial policy

| Rule | Detail |
|---|---|
| Max duration | 14 days unless VP extension |
| Payment | Dedicated low-limit virtual card |
| End state | Convert to roster + proper card, or cancel before charge |
| Documentation | Trial owner in vendor register |

---

## Credit-based tools (Clay, APIs, LLM)

| Guardrail | Action |
|---|---|
| Weekly usage report | RevOps reviews |
| 80% budget alert | Ramp + vendor dashboard |
| 100% hard stop | Pause workflows until approval |
| Sensitivity table | 1× / 2× / 3× in `gtm-tool-cost-model` |

---

## Marketing vs sales spend split

| Type | Owner | Ramp class |
|---|---|---|
| Paid ads | Marketing | GTM-Marketing |
| CRM, sequencer, Gong | RevOps | GTM-Sales-Tools |
| Enrichment | RevOps | GTM-Data |
| Events / sponsorship | Marketing | GTM-Marketing |
| ABM gifting | Marketing / ABM | GTM-Gifting |

Finance allocates **shared** tools (CRM) by headcount % monthly.

---

## Quarterly spend review agenda (60 min)

1. Ramp actuals vs TCO budget — variance by category
2. Zombie vendors — no owner or no login 90d
3. Renewals next 90 days — negotiate list
4. Seat true-down opportunities
5. Consolidation candidates (Brinker audit)
6. Update `vendor-spend-register.md`

---

## SOC2 / audit trail

- Receipt retention per policy
- Named cardholders for software charges
- Offboard card freeze within 24h
- Vendor register matches accounting subledger

`soc2-compliance` for access control alignment.

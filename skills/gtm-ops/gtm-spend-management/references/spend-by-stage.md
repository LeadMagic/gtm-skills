# GTM Spend by Company Stage

Tie vendor spend to journey gates — do not buy the stack before the motion works.

**Cross-refs:** `solo-founder-gtm/references/scale-readiness-gates.md` · `saas-outcomes/references/journey-stage-gates.md` · `references/spend-governance.md`

---

## Spend tiers by ARR stage

| Stage | ARR band | GTM spend % of ARR (typical) | Stack priority | Defer until |
|---|---|---|---|---|
| **Survival** | $0–$500K | 15–25% (founder time = largest cost) | CRM lite, enrichment API, sending infra | ABM platform, intent data, full MAP |
| **Thrival** | $500K–$2M | 20–35% | SEP + Clay/n8n + CRM + basic analytics | Enterprise ABM, 6sense, dedicated CDP |
| **Scale** | $2M–$10M | 25–40% | Full RevOps stack, intent, CS platform | Duplicate tools in same category |
| **Enterprise** | $10M+ | 30–45% | ABM, data warehouse, security/compliance tools | Shadow SaaS on personal cards |

*Percent ranges are directional — model in `gtm-tool-cost-model` with your ACV and headcount.*

---

## Tool unlock order (matches scale gates)

```
1. CRM + billing (source of truth)
2. Enrichment + verification (prospecting quality)
3. SEP / sequencing (outbound motion proven)
4. Marketing automation / MAP (inbound volume)
5. Intent / visitor ID (only after ICP + triage SLAs)
6. CS platform (when NRR program starts)
7. ABM / 6sense (enterprise motion + multi-thread)
```

**Gate:** Do not unlock tier N+1 until tier N has an owner, utilization >60%, and ROI documented in `vendor-spend-register`.

---

## Approval shortcuts by stage

| Stage | Auto-approve | Requires exec |
|---|---|---|
| Survival | &lt;$500/mo tools on pre-approved Ramp card | &gt;$2K annual |
| Thrival | &lt;$2K with RevOps overlap check | &gt;$10K annual |
| Scale+ | Standard matrix in `spend-approval-matrix.md` | &gt;$50K |

---

## Zombie spend triggers (quarterly audit)

- [ ] Seat count &gt; active users + 20%
- [ ] No login 90 days (owner must justify or cancel)
- [ ] Overlap with another row in `revops-tech-stack` audit
- [ ] Auto-renew in 30 days without TCO refresh

**Pattern:** `using-gtm-skills` Pattern 11 (GTM Stack Finance)

# PMF Testing Playbook

Structured tests for **PMF search** stage. Pair with `pmf-signal-checklist.md` for go/no-go.

**Sources:** Sean Ellis, David Skok, Paul Graham (do things that don't scale), `saas-metrics-calculator`, `fundraising-strategy/references/vc-milestone-gates.md`.

---

## Test Menu

| Test | What it proves | How to run | Pass threshold |
|---|---|---|---|
| **Sean Ellis survey** | Must-have vs nice-to-have | Ask active users: "How disappointed if product gone?" | ≥40% very disappointed |
| **Cohort retention** | Sticky value | Monthly logo + revenue cohorts from first paid | M3 >80% SMB; curve flattens |
| **Payback period** | Economics work | Fully loaded CAC ÷ gross margin per new customer | <12 mo go; <18 mo caution |
| **Pricing test** | Willingness to pay | Raise price on new logos or remove discount | Conversion stable ±10% |
| **Sales cycle compression** | Pull demand | Compare last 10 vs first 10 deals | Median days declining |
| **Organic growth** | Word of mouth | Track sourced=referral/inbound/product | >20% new logos |
| **NPS / CSAT** | Advocacy | Quarterly survey post-value milestone | NPS >30 B2B SMB |
| **Expansion signal** | Land-expand works | % accounts with upsell <12 mo | >15% expanding |

---

## Sean Ellis Test (Step-by-Step)

1. Survey **active users** only (used core value in last 14 days) — not churned, not trial-only.
2. Question: *"How would you feel if you could no longer use [product]?"*
   - Very disappointed
   - Somewhat disappointed
   - Not disappointed
3. Segment by ICP persona — PMF is per segment, not blended.
4. Follow-up for "very disappointed": *"What is the main benefit?"* and *"What would they use instead?"*

| Result | Action |
|---|---|
| ≥40% very disappointed | Double down on ICP; advance toward GTM fit |
| 25–39% | Iterate positioning or segment; do not scale |
| <25% | Pivot ICP or core value prop |

---

## Cohort Retention Protocol

```
Month 0: Cohort = customers who first paid in month M
Track: Logo % still active | Revenue % of month-0 ARPA
Minimum: 6 months history for SMB; 12 for annual contracts
```

| Pattern | Interpretation |
|---|---|
| Smile curve (dip then flat) | Onboarding fix needed; PMF possible |
| Flat from M2+ | Strong PMF signal |
| Continuous decline | No PMF — fix product before GTM spend |

Export template fields → `saas-metrics-calculator` cohort section.

---

## Qualitative + Quantitative Combo

Run in parallel (2–4 week sprint):

| Week | Qualitative | Quantitative |
|---|---|---|
| 1 | 8 customer interviews (wins + losses) | Baseline cohort export |
| 2 | Sean Ellis survey to active base | CAC payback calc |
| 3 | ICP refinement workshop | Pricing test on inbound |
| 4 | Synthesize: false PMF trap check | Re-run Ellis on refined ICP only |

**Decision meeting:** Use `pmf-signal-checklist.md` go/no-go.

---

## False PMF — Diagnostic Tests

| Suspicion | Test | Fail signal |
|---|---|---|
| One big logo | Revenue concentration report | >40% ARR one customer |
| Channel luck | Pause channel 30 days | New ARR → ~0 |
| Founder-only | Founder silent on 5 calls | Win rate drops >50% |
| Custom services | % revenue from setup fees | >15% services |

---

## PMF vs GTM Fit (Don't Confuse)

| | PMF search | GTM fit |
|---|---|---|
| Question | Do they stay and pull? | Can others sell it? |
| Owner | Founder + product | Founder + first playbook |
| Spend | Minimal tools | CRM + documented process |
| Hire | None | AE after 10–20 founder deals |
| Skill | This playbook | `scale-readiness-gates.md` |

---

## Cross-References

- Checklist → `pmf-signal-checklist.md`
- Journey → `saas-outcomes/references/journey-stage-gates.md`
- VC retention bar → `fundraising-strategy/references/vc-milestone-gates.md`
- Do not scale on false PMF → `when-not-to-scale.md`
- Metrics → `saas-metrics-calculator`, `analytics/gtm-metrics`

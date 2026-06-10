# PMF Signal Checklist

Quick go/no-go for **PMF search → GTM fit** gate. Full tests → `pmf-testing-playbook.md`.

**Sources:** Sean Ellis (40% rule), David Skok (retention), Jason Lemkin (founder closes), `saas-metrics-calculator`, `journey-stage-gates.md`.

---

## Quantitative Signals

| Signal | Go | Caution | No-go |
|---|---|---|---|
| **Sean Ellis test** | ≥40% "very disappointed" without product | 25–39% | <25% |
| **Logo retention (M3)** | >80% SMB / >90% mid-market | 70–80% | <70% |
| **Cohort revenue retention (M6)** | Flattening or improving | Slow decline | Cliff after M1 |
| **NRR (if enough base)** | >100% | 90–100% | <90% |
| **GRR** | >85% | 80–85% | <80% |
| **CAC payback** | <12 mo | 12–18 mo | >18 mo |
| **LTV:CAC** | >3x (Skok) | 2–3x | <2x |
| **Sales cycle** | Compressing vs first 10 deals | Flat | Lengthening |
| **Organic / inbound %** | >20% new logos | 10–20% | 0% push-only |

---

## Qualitative Signals

| Signal | Go | No-go |
|---|---|---|
| **Pull vs push** | Customers ask for features, referrals, faster onboarding | Every deal is founder hustle |
| **ICP clarity** | Same persona wins repeatedly; lost deals fit pattern | Wins are random |
| **Pricing power** | Uplifts or annual prepay without heavy discount | Race to bottom; custom one-offs |
| **Champion behavior** | Users expand usage without CS chasing | Shelfware after pilot |
| **Competitive win reason** | Specific capability + outcome | "We like you" / relationship only |

---

## False PMF Traps

| Trap | How to detect | Fix before scaling |
|---|---|---|
| **One big customer** | >40% ARR one logo; roadmap = their requests | Segment revenue; prove second ICP |
| **Channel dependency** | One partner/agency = >50% pipeline | Direct motion or 2nd channel |
| **Pilot forever** | Revenue mostly POCs; no production usage | Paid conversion criteria |
| **Vanity ARR** | Annual prepay from 2 logos; churn pending | Cohort view; logo not revenue |
| **Founder charisma** | Wins drop when founder not on call | Document playbook; shadow AE test |

---

## Go / No-Go: Advance to GTM Fit

**Go** when **all**:

- [ ] Sean Ellis ≥40% OR cohort M6 retention on plan
- [ ] No false PMF trap active
- [ ] LTV:CAC >3x or improving 2 consecutive months
- [ ] ICP written in `gtm-context`
- [ ] Founder path: 5+ closed deals same motion

**No-go** when **any**:

- [ ] Logo churn >5%/mo after month 3
- [ ] NRR <90% with >20 customers
- [ ] Only one channel and it is paid blitz with payback >18 mo

---

## Cross-References

- Tests → `pmf-testing-playbook.md`
- Journey gate → `saas-outcomes/references/journey-stage-gates.md`
- Metrics formulas → `saas-metrics-calculator`
- Churn fixes → `growth/churn-prevention`
- Scale only after PMF → `scale-readiness-gates.md`

# Public-Company GTM Metrics — Earnings-Season Discipline

**Source:** Henry Schuck, ZoomInfo Founder & CEO — public earnings calls and investor materials  
**Anchors:** [Q1 2026 earnings transcript](https://www.fool.com/earnings/call-transcripts/2026/05/11/zoominfo-gtm-q1-2026-earnings-call-transcript/) · [Q3 2025 earnings transcript](https://www.fool.com/earnings/call-transcripts/2025/11/04/zoominfo-gtm-q3-2025-earnings-call-transcript/) · [Hit Your Number GTM deck](https://www.slideshare.net/slideshow/henry-schuck-hit-your-number-how-zoominfo-developed-a-winning-and-leading-gotomarket-strategy/236147433) · [OpenView GTM motion](https://openviewpartners.com/blog/go-to-market-zoominfo/)

---

## Why public-company metrics differ

Private SaaS dashboards optimize for **growth experiments**. Public (or pre-IPO) GTM leaders report metrics that survive **SEC scrutiny, analyst models, and guidance**. Schuck's ZoomInfo calls illustrate how a data-company GTM org ties **seat economics, consumption revenue, operating margin, and AI productivity** into one narrative.

Use this reference when building **board decks, investor updates, or RevOps cadences** for companies approaching or operating in public markets — not for early-stage vanity dashboards.

---

## Earnings-season core stack (6 metrics)

| # | Metric | Definition | Why public cos emphasize it |
|---|---|---|---|
| 1 | **Revenue / ARR** | GAAP revenue + ARR bridge | Top-line guidance anchor |
| 2 | **Adjusted operating income margin** | Non-GAAP profitability | Proves GTM scale without burning margin (Schuck: 35% AOI margin cited Q1 2026) |
| 3 | **NRR / GRR** | Net and gross revenue retention | Seat expansion vs churn — data products live on retention |
| 4 | **S&M as % of revenue** | Fully loaded sales + marketing | Efficiency trend matters more than absolute spend |
| 5 | **Revenue mix** | Seat-based vs consumption / DaaS | Schuck: shifting from seat-heavy to consumption upmarket |
| 6 | **Rule of 40 / growth + margin** | Growth rate + profit margin | Analyst shorthand — pair with cohort context (see `SKILL.md` pitfalls) |

---

## GTM operating metrics (between earnings)

Report weekly/monthly internally; summarize quarterly for investors.

### Pipeline generation

| Metric | Formula / definition | Public-operator pattern |
|---|---|---|
| Pipeline created | $ new qualified pipeline / period | Segment by inbound vs outbound vs expansion |
| Pipeline velocity | (Opps × deal size × win rate) ÷ cycle days | Skok formula — see `framework-notes.md` |
| Lead response time | Median seconds from MQL to first touch | ZoomInfo public benchmark: <90 sec inbound |
| SQL acceptance rate | % SDR meetings accepted by AE | Quality gate — comp SDRs on accepted SQLs |
| Demo yield | % demos → opps | Tie to routing and reverse-demo experiments |

### Sales productivity

| Metric | Definition | Notes |
|---|---|---|
| Quota attainment distribution | % reps at 80%+ / 100%+ quota | Public cos avoid "one hero rep" stories |
| ACV per rep | Bookings ÷ quota-carrying headcount | Trend by segment (SMB vs enterprise) |
| Win rate by segment | Closed won ÷ qualified opps | Disclose mix shift when moving upmarket |
| Sales cycle | Median days stage 1 → closed won | Lengthens intentionally in enterprise pivot |
| SDR:AE efficiency | SQOs per SDR → opps per AE | See `henry-schuck-sdr-model.md` |

### Retention & expansion (data-product GTM)

| Metric | Definition |
|---|---|
| Logo churn | % customers lost |
| Dollar churn | GRR = (Starting ARR − churn − contraction) ÷ Starting ARR |
| Expansion rate | Upsell + cross-sell ARR |
| NRR | (Starting + expansion − churn − contraction) ÷ Starting |
| Product adoption | % seats actively using platform (Schuck cites internal AI/workspace adoption) |

---

## ZoomInfo public narrative patterns (Schuck)

Extract **structure**, not copy-paste numbers — your stage differs.

1. **Data-as-GTM:** Own third-party data layer; AI (Copilot, GTM Studio) makes reps productive on that data
2. **Persona expansion:** From SDR-only seats → AE, AM, CSM, RevOps users on same platform
3. **Upmarket mix shift:** Consumption / DaaS growing >20% YoY while seat-based SMB mix declines deliberately
4. **AI productivity:** Ship more code, campaigns, and finance automation with smaller teams — report **output per employee**
5. **Outbound resurgence:** Customers re-investing in SDR motions when pure AI top-of-funnel under-fills pipeline (Q3 2025 call)

---

## Earnings prep checklist

- [ ] ARR bridge: new, expansion, contraction, churn — reconciles to reported revenue
- [ ] NRR/GRR by customer segment (SMB / mid-market / enterprise)
- [ ] S&M efficiency: Magic Number with **lag** for long cycles
- [ ] Headcount plan vs pipeline targets (hiring ahead of or behind demand)
- [ ] GTM mix commentary: inbound %, outbound %, PLG %, partner %
- [ ] One "leak in the funnel" initiative with before/after metric
- [ ] Guidance sensitivity: what happens if win rate −2 pts or cycle +15 days

---

## Board / investor slide order

1. ARR + growth rate (with mix)
2. NRR / GRR trend (12-quarter)
3. CAC payback or Magic Number (stage-appropriate)
4. Adjusted operating margin trajectory
5. Pipeline coverage (× quota) by segment
6. GTM Index self-score (WbD 6 models) — qualitative maturity
7. Next-quarter initiatives tied to **one measurable outcome**

---

## Cross-links

| Topic | Skill / artifact |
|---|---|
| Public SaaS cohort medians | `references/meritech-saas-benchmarks.md` (Meritech Capital) |
| Benchmark conflicts | `references/benchmark-reconciliation.md` |
| SDR machine design | `sales-team-building` → `henry-schuck-sdr-model.md` |
| WbD GTM Index | `gtm-metrics` SKILL Phase 2 |
| Skok unit economics | `financial-modeling`, `saas-metrics-calculator` |
| Inbound triage SLAs | `inbound-triage` |
| Demo conversion | `demo-scripts` → `reverse-demo-varun.md` |

---

## Attribution

Metrics cited from **public** ZoomInfo earnings transcripts and Schuck's OpenView / SlideShare materials. Always pull latest figures from primary SEC filings ([investors.zoominfo.com](https://investors.zoominfo.com/)) before investor-facing deliverables.

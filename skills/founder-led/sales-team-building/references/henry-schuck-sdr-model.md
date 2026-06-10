# Henry Schuck — ZoomInfo High-Velocity SDR Model

**Source:** Henry Schuck, Founder & CEO, ZoomInfo (NASDAQ: GTM; formerly ZI)  
**Public anchors:** [OpenView — building a sales team](https://openviewpartners.com/blog/building-a-sales-team/) · [OpenView — 90-second GTM](https://openviewpartners.com/blog/go-to-market-zoominfo/) · [Hit Your Number deck](https://www.slideshare.net/slideshow/henry-schuck-hit-your-number-how-zoominfo-developed-a-winning-and-leading-gotomarket-strategy/236147433) · [Pipeline — sales process optimization](https://pipeline.zoominfo.com/sales/sales-process-optimization)

---

## Why cite Schuck for SDR scale

ZoomInfo built a **data-as-product GTM engine** — the same contact, intent, and enrichment data they sell powers their own inbound, outbound, and AE routing. Schuck's public writing emphasizes **process + people + data** at every funnel stage, not hero reps. This complements Roberge (hiring/training) and WbD (POD ratios) with operator metrics from a public-company revenue machine.

---

## SDR motion taxonomy (ZoomInfo)

| Motion | Role | Primary job | Key metric |
|---|---|---|---|
| **Inbound SDR** | Dedicated inbound team | Respond to marketing-qualified leads in <90 seconds | Response time, attendance rate, qualification rate |
| **Outbound SDR** | Proactive prospecting | Call accounts surfaced from internal data lake | Connect rate, meetings booked, SQL conversion |
| **SWAT SDR** | Overflow / hot accounts | Handle spikes and high-potentiality accounts | Speed-to-lead on priority queue |

Schuck separates inbound and outbound SDRs — different skills, different SLAs. Do not blend them in one comp plan.

---

## Inbound SDR machine (public benchmarks)

From OpenView interviews and Schuck's Hit Your Number presentation:

| Metric | ZoomInfo public reference | Design implication |
|---|---|---|
| Hot inbound leads / month | ~10,000 | Requires dedicated inbound SDR pod, not AEs doing triage |
| Inbound SDR headcount | ~70 (at time of publication) | ~143 leads/SDR/month — automation + routing essential |
| Response SLA | **<90 seconds** | Sub-minute response materially lifts connect and demo-book rates |
| Lead enrichment | FormComplete appends firmographics on submit | Never route thin leads to reps — enrich before assignment |
| No-show recovery | Automated win-back campaigns | Schuck cites ~$1M ACV/month recovered from no-shows |

**Onboarding implication:** Inbound SDRs certify on speed-to-lead tooling and qualification scripts before live queue access. See `revenue-team-onboarding` → `ramp-benchmarks.md` (inbound SDR 7–14 day first-meeting target).

---

## Outbound SDR — data lake motion

Outbound is not spray-and-pray. Schuck describes a **data lake** feeding SDRs daily:

1. Pull ZoomInfo intent, Scoops, job changes, prior product usage into one queue
2. Surface **best leads at this moment** — executive changes actualized in real time
3. Deliver **targeted talk track** with each record (why call now, why this account)
4. SDR executes; system re-scores and re-queues continuously

| Component | Requirement |
|---|---|
| TAM | Large addressable market — outbound only scales with coverage |
| Data | Third-party + first-party signals merged (intent, technographics, triggers) |
| Message | Pre-built "why now" per record — not generic sequences |
| Feedback | Product usage and win/loss data back into lake |

**Cross-link:** `cold-email-strategy` (trigger-based architecture) · `signal-scoring` · `data-enrichment-strategy`

---

## SDR as feeder system (not a dead-end)

Schuck's inbound SDR bench is an **internal talent pipeline**:

- Promotion path: SDR → AE → manager
- Lateral paths: product marketing, operations, product management, engineering
- Design implication: hire SDRs for coachability and analytical curiosity (Roberge traits), not just dial tolerance

| Stage | SDR:AE ratio guidance |
|---|---|
| Early inbound-heavy (ZoomInfo-style) | Higher inbound SDR count; AEs ranked and fed qualified demos |
| Outbound scale-up | Add outbound SDR pod when inbound channel saturates |
| WbD POD baseline | See `SKILL.md` — 1:2:1 moderate, 2:3:1 simple; ZoomInfo adds **specialist SDR types** on top |

---

## AE routing — dynamic load balancing

AEs are ranked and leads assigned by trailing performance (public Hit Your Number deck):

| Rank input | Why it matters |
|---|---|
| Trailing 3-month ACV won | Proven closer gets hotter leads |
| Trailing 3-month win rate | Quality over volume |
| Trailing 3-month ASP | Match lead size to rep strength |
| Trailing 3-month opportunity creation | Pipeline builders vs closers |
| Trailing 3-month ACV per opportunity | Deal size efficiency |

**Transparency rule:** Reps see their rank and the formula — reduces "unfair lead" disputes.

**RevOps artifact:** Build `potentiality score` + `account load balancing` in CRM before scaling past 5 AEs.

---

## GTM cycle stages (Schuck framework)

Every stage has explicit optimization — not just "top of funnel":

```
Demand Gen → SDR (inbound/outbound/SWAT) → AE (demo + close) → Onboarding/CSM → AM/CDR → Renew
```

Per-stage examples from public materials:

- **Demand gen:** Lead scoring, FormComplete enrichment, conversion optimization
- **SDR:** Demo routing, optimized scheduling, segmentation
- **AE:** Account assignment, potentiality scoring, load balancing
- **Post-sale:** Training completion, integrations, attribution tracking, health score

---

## SDR productivity scorecard (adapt for your org)

| Category | Metric | Example target band |
|---|---|---|
| **Speed** | Median speed-to-lead (inbound) | <5 min (stretch: <90 sec with automation) |
| **Volume** | Dials + emails (outbound) | Set by segment — measure **meetings**, not activity alone |
| **Quality** | SQL acceptance rate by AE | >70% — SDRs comped on qualified, not held meetings |
| **Conversion** | Demo held rate | Track no-show win-back separately |
| **Ramp** | Day 30 / 60 / 90 SQO vs tenured median | See `revenue-team-onboarding` benchmarks |
| **Feeder** | % SDRs promoted to AE in 18 months | Healthy bench: 20–40% internal promotion |

---

## When to use this vs other frameworks

| Situation | Load |
|---|---|
| First 2 AEs, founder-led | `founder-sales`, Roberge hiring scorecard |
| POD design and comp | `sales-team-building` SKILL + WbD ratios |
| **Scaling SDR/AE with data product or high inbound** | **This reference** |
| Public company board metrics | `gtm-metrics` → `public-company-gtm-metrics.md` |
| Demo conversion | `demo-scripts` → `reverse-demo-varun.md` (buyer-led alternative) |

---

## Attribution note

Henry Schuck is **confirmed** as ZoomInfo Founder & CEO. Public channels: [LinkedIn `/in/hschuck`](https://www.linkedin.com/in/hschuck/) · X [`@henrylschuck`](https://x.com/henrylschuck) · [ZoomInfo Pipeline blog](https://pipeline.zoominfo.com/) · earnings transcripts via [Motley Fool](https://www.fool.com/earnings/call-transcripts/).

Numbers in this doc are **point-in-time from public sources** — validate against your ARR stage and motion before copying headcount ratios.

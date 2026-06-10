# Benchmark Reconciliation — Single Source of Truth

When skills cite different numbers for the same metric, **this document is canonical**. Skills should link here instead of hardcoding conflicting thresholds.

**Format:** Source A vs Source B → **Canonical guidance** (with footnotes for intentional expert nuance).

Last reviewed: 2026-06. Refresh Meritech/KeyBanc annually.

---

## NRR / GRR Thresholds

| Context | Source A | Source B | Canonical guidance |
|---|---|---|---|
| **SMB private** | `saas-metrics-reference`: >100% good | `gtm-metrics` pitfalls: SMB 100%+ acceptable | **≥100%** minimum; **105%+** strong for SMB SaaS |
| **Mid-market private** | `saas-metrics-reference`: >110% | KeyBanc/Benchmarkit 2024: **101% median** | **≥105%** good; **110%+** strong; don't panic at 101% if market median |
| **Enterprise** | `expansion-selling`: 115%+ growth stage | Meritech public median ~108–111% | **≥110%** good; **120%+** best-in-class enterprise |
| **PE-ready exit** | `exit-metrics-matrix`: >110% | `vc-milestone-gates` Series B: >110% | **≥110%** PE floor; **115%+** premium multiple |
| **Series A gate** | `vc-milestone-gates`: >105% | `expansion-selling`: 105%+ Series A | **≥105%** at Series A; state cohort definition |
| **GRR** | `saas-metrics-calculator`: >90% excellent | `exit-metrics-matrix` PE: >92% | **≥88%** acceptable mid-market; **≥90%** good; **≥92%** PE-ready |

**Footnote — Schwartz vs Meritech range:** Eli Schwartz / product-led SEO contexts discuss **logo** retention and engagement — not NRR. Meritech NRR is **dollar cohort** on public filers. Don't compare logo retention % to NRR %.

**Footnote — segment mixing:** `gtm-metrics` pitfall — never compare SMB NRR to enterprise benchmarks. Always tag segment in dashboards.

---

## CAC Payback / LTV:CAC

| Context | Source A | Source B | Canonical guidance |
|---|---|---|---|
| **SMB payback** | Skok / `saas-metrics-reference`: <12 mo | KeyBanc 2025: ~20 mo median worsening | **Target <12 mo** SMB; **<18 mo** acceptable if ACV rising; **>20 mo** fix before scale |
| **Enterprise payback** | `saas-metrics-reference`: <24 mo | `exit-metrics-matrix`: <18 mo at scale | **<18 mo** at $10M+ ARR; **<24 mo** only if ACV >$50K and NRR >120% |
| **Series A gate** | `vc-milestone-gates`: <15 mo | `solo-founder-gtm` Skok: <12 good | **<15 mo** to raise A; **<12 mo** ideal SMB |
| **LTV:CAC minimum** | Skok: 3:1 investable | Bootstrap organic: 5–10x common | **≥3:1** minimum VC; **≥4:1** scale; bootstrap **≥3:1** with note organic CAC lower |
| **LTV:CAC "too high"** | `saas-metrics-reference`: >10x under-invest | — | **>10x** = likely under-investing in growth (not a brag) |

**Canonical formula:** Contribution-margin LTV only — see `references/saas-metrics-reference.md`.

---

## Magic Number / Burn Multiple / Rule of 40

| Metric | Source A | Source B | Canonical guidance |
|---|---|---|---|
| **Magic Number** | `saas-metrics-reference`: ≥0.75 good | Meritech public implied varies | **≥0.75** invest more; **0.5–0.75** optimize; **<0.5** fix GTM |
| **Burn Multiple** | Lemkin/Sacks: <2x A, <1.5x B | `exit-metrics-matrix`: <1x PE | **<2x** seed/A; **<1.5x** B; **<1x** PE-preferred |
| **Rule of 40 (private board)** | Bessemer/Skok: ≥40% scale | KeyBanc: **~15% median**; 11–30% achieve | **≥40%** aspiration at scale; **≥30%** Series B credible path; **median ~15%** — not failing |
| **Rule of 40 (public)** | Meritech traditional NTM | Meritech Rule of 40 (3× growth) | Use **traditional** for ops; **Meritech weighted** for valuation comps only |

---

## Growth Rate

| Stage | Source A | Source B | Canonical guidance |
|---|---|---|---|
| **Private median 2024–25** | SaaS Capital: 25% | KeyBanc/Benchmarkit: 26% | **~25% median** private B2B |
| **Seed gate** | Lemkin: 3x YoY | — | **3x in 12–18 mo** or clear inflection |
| **Series A** | `vc-milestone-gates`: 2–3x YoY | — | **2–3x YoY** at $1–4M ARR |
| **Public median** | Meritech: ~19% YoY | — | **~17–21%** public implied ARR growth |
| **Planned vs actual** | Benchmarkit: 35% planned, 26% actual | — | Plan conservatively; 9pt optimism bias common |

---

## SDR Ratios / Pod Models

| Topic | Source A | Source B | Canonical guidance |
|---|---|---|---|
| **SDR:AE ratio** | Henry Schuck ZoomInfo model | Force Management pods | **1:1 to 2:1** SDR:AE SMB/mid-market; **pod model** (SDR+AE+SE+CSM) at $10M+ — see `force-management-playbook.md` |
| **SDR comp / quota** | Bridge Group 5:1 quota:OTE | Becc Holland lead-weighting | Use Bridge for **comp**; Becc for **KPI weighting** (inbound vs outbound leads) |
| **Accounts/SDR/month** | Justin Michael: ~200 | — | **150–250** outbound SDR; adjust for phone-first (Gilkey) |
| **Hire VP Sales** | Lemkin: ~$2M ARR | Roberge machine earlier | **~$2M ARR** default; document process before hire |

---

## Inbound vs Demand Gen

| Topic | HubSpot / Dharmesh | Chris Walker | Canonical guidance |
|---|---|---|---|
| **Philosophy** | Inbound flywheel — earn permission | Demand creation — dark social education | **Complementary** — Pattern 27 + 26; not either/or |
| **Measurement** | Forms, lifecycle, SEO, visitor ID | Cohort revenue; 90-day eval; not last-click | Board pack: **both** attributable (Pattern 20) and dark social narrative |
| **MQL stance** | MQL → SQL when fit | Anti–lead-gen volume | Qualify hard; don't optimize form volume alone |
| **Paid social** | Supports inbound capture | Education-first LinkedIn | Ungated content + retarget; avoid CPL-only optimization |

Refs: `references/dharmesh-shah-hubspot-inbound.md` · `references/chris-walker-mental-models.md`

---

## Bucketing — Joey Gilkey vs Ryan Reisert

| Expert | System | Purpose | Canonical guidance |
|---|---|---|---|
| **Joey Gilkey** | Disposition Science (6 outcomes) | Diagnose list/message/rep/follow-up | **Outcome taxonomy** — what happened on the call |
| **Ryan Reisert** | 4 CRM Activity Buckets | Daily rep prioritization | **Workflow taxonomy** — what to do next |

**These are distinct — do not merge.** Gilkey ≠ Reisert. Cross-link both in `cold-calling`; Pattern 15b loads both. See `references/cold-calling-experts-index.md`.

---

## Bootstrap vs VC Multiples

| Path | Source A | Source B | Canonical guidance |
|---|---|---|---|
| **<$2M ARR sale** | `exit-metrics-matrix`: 2–4x ARR bootstrap | VC distressed: 3–6x | **2–6x ARR** range; profitability + NRR drive pin |
| **$2–10M bootstrap sale** | Latka/MicroAcquire: SDE + ARR blend | `bootstrap-founder-playbook`: 4–8x with profit | **3–8x ARR** typical; SDE multiples when margin >20% |
| **$10–30M growth** | VC-backed: 8–15x | PE: 8–12x + EBITDA | **8–15x** if efficient growth; PE blends ARR + EBITDA |
| **Bootstrap raise later** | `vc-milestone-gates`: $1–2M ARR profitable | Lemkin $100M venture test | Bootstrap first **lowers dilution**; venture still needs TAM story |
| **Public comps (Meritech)** | Implied EV/ARR on filers | Private bootstrap sale | Use Meritech for **venture/board narrative** — not MicroAcquire LOI quotes |
| **Organic LTV:CAC** | Bootstrap: 5–10x cited | Skok minimum 3:1 | Bootstrap **≥3:1** floor; high organic multiples ≠ excuse to over-spend on tools |

**Footnote — bootstrap pride vs economics:** Label "bootstrapped" does not add a multiple. Buyers pay for **growth, NRR, margin, clean books, low concentration**. See `saas-outcomes/references/bootstrap-founder-playbook.md`.

---

## Earn-Out vs Upfront Cash (M&A Structure)

| Topic | Source A | Source B | Canonical guidance |
|---|---|---|---|
| **Earn-out % of EV** | Strategic mid-market: 15–40% common | Bootstrap sales: often minimal | **≤35% at risk** founder-friendly default; **>50%** re-trade or walk unless strategic must-have |
| **Cash at close** | Founder planning: life + tax | LOI headline EV | Model **cash at close** and after-tax — not headline; see `earn-out-term-sheet-review.md` |
| **Measurement period** | PE: 24–36 mo common | Founder preference: 12–18 mo | **≤24 mo** default push; acceleration on change of control if >20% at risk |
| **EBITDA earn-out** | PE platform deals | Founder risk: buyer controls OpEx | Require **fixed add-backs** + spend carve-outs — see `negotiating-earn-out.md` |
| **Retention vs earn-out** | Employment-tied forfeiture | Separate retention bonus | **Split** time-based retention from performance earn-out in term sheet |
| **Bootstrap earn-out** | Less common <$5M | Strategic tuck-in | Prefer **higher cash %**; large earn-out on small deal = yellow flag |

**Not legal advice.** Definitions and tax → counsel + CPA. Commercial alignment → `deal-desk/references/legal-gtm-playbook.md`.

---

## When to Scale

| Signal | Source A | Source B | Canonical guidance |
|---|---|---|---|
| **PMF** | Sean Ellis 40% | WbD GTM Index <6 | **40% "very disappointed"** + GTM Index **≥6** before heavy spend |
| **Founder closes** | Lemkin: 10–20 deals | Roberge traits hiring | **10–20 founder closes** documented before first AE |
| **VP Sales** | Lemkin $2M ARR | `scale-readiness-gates` | **$2M ARR** + repeatable process |
| **Spend stage** | `spend-by-stage` % ARR | `gtm-spend-management` | Follow **spend-by-stage** caps; PMF gate overrides |

---

## SEO vs AEO vs pSEO

| Layer | Purpose | Canonical guidance |
|---|---|---|
| **SEO** (`seo-strategy`) | Keyword demand capture | Foundation — Schwartz awareness levels |
| **pSEO** (`pseo-strategy`) | Programmatic scale | Thin-content gates required |
| **AEO** (`aeo-strategy`) | AI answer surfaces | Schema + extractable facts |
| **FAQ** (`faq-seo`) | PAA/snippets | Supports AEO, not replacement |

**Pattern 25** loads full stack in order. Don't run pSEO before pillar authority exists.

---

## Visitor ID Privacy

| Level | Use | Canonical guidance |
|---|---|---|
| **Company ID** | ABM, account scoring | Default B2B — lower privacy risk; Clearbit/Breeze, 6sense |
| **Person ID** | SDR Slack alerts | Requires `visitor-id-privacy-gtm.md` checklist before spend |
| **Cold email PII** | Enriched emails from visitor ID | **Never** auto-enroll without consent/legal review; `cold-email-strategy` anti-pattern |

**Contrast:** Visitor ID = measurable (Pattern 20). Dark social = unmeasurable (Pattern 26). Both valid.

---

## Revenue Ramp Timelines (HR GTM)

| Source A | Source B | Canonical guidance |
|---|---|---|
| `revenue-team-onboarding` 30-60-90: day 90 **full quota** | `sales-team-building`: 3–4 mo to **80%** productivity; 4–6 mo first-time AE | **30-60-90 = plan milestones**; **4.5–6 mo = Bridge full productivity** for AE. Day 90 quota **bearing** ≠ fully productive vs tenured. |
| `ramp-benchmarks`: AE SMB full quota day 90 | `comp-benchmarks`: AE ramp 4.5–6 months | SMB: **quota-bearing day 90** with **50% quota credit** months 1–3 common; **100% productivity ~month 5–6** |
| `financial-modeling`: 100% productivity month 6 | `ramp-benchmarks`: inbound SDR full quota day 75 | Model **hiring plan** at M6 for AE; **operational ramp** tables in `ramp-benchmarks.md` per role/motion |
| Henry Schuck inbound SDR <90s cert | Outbound SDR 14–21 days first meeting | Tag **inbound vs outbound** — never merge ramp tables |

**HR GTM expert:** Stacey Nordwall — onboarding surveys measure *system*; Roberge/Bridge measure *output*. Both required. → `hr-gtm-playbook.md`

---

## Comp Band Alignment (HR GTM)

| Source A | Source B | Canonical guidance |
|---|---|---|
| `gtm-role-descriptions` SKILL table: SDR $55–80K OTE | `comp-benchmarks.md`: SDR $58–85K | **$58–85K OTE** canonical (June 2025 / H1 2026) — SKILL + role-catalog aligned |
| `executive-compensation` Pavilion gates | `founder-comp-playbook` payroll % ARR | VP+ → Pavilion + founder budget guardrails; IC → Bridge 5:1 |
| `gtm-role-descriptions` RevOps $90–140K | `comp-benchmarks` RevOps $95–150K | **$95–150K** canonical — SKILL aligned |
| `sales-team-building` SDR $55–80K (legacy) | `comp-benchmarks` $58–85K | **$58–85K** — hire sequence table aligned |
| AE mid-market $120–180K (legacy) | `comp-benchmarks` $130–190K | **$130–190K** canonical mid-market |
| CSM $70–110K (legacy) | `comp-benchmarks` $72–115K | **$72–115K** canonical |
| Comp strategy home | `saas-comp-strategies` vs `executive-compensation` | **`executive-compensation/references/gtm-compensation-strategy.md`** canonical (Pattern 35); bands stay in `comp-benchmarks.md` |

---

## Legal / Security Phase Gates (Legal GTM)

| Source A | Source B | Canonical guidance |
|---|---|---|
| `deal-desk` Phase 5: DPA parallel at negotiation | `gtm-data-exchange`: DPA before production intake | **Aligned** — enterprise DPA during negotiation, before production data |
| `security-questionnaire-deal-guide`: eval stage questionnaire | `soc2-compliance`: build controls pre-pipeline | **GTM timing** = share trust center at eval; **implementation** = earlier if enterprise pipeline >20% |
| `gtm-data-exchange`: pause if DPA required, not done | `deal-desk`: don't discount to skip security | **Never** trade discount for skipping DPA/security |
| AE answers questionnaire alone (pitfall) | Vanta trust center handoff | Route to security owner; AE coordinates timeline only |

**Legal GTM expert:** Eunice Buhler — velocity via availability + SLAs; Ironclad — approval swimlanes. → `legal-gtm-playbook.md`

---

## Automation Expert Boundaries

| Expert | Owns | Does not own |
|---|---|---|
| **Jen Igartua** (Pattern 30) | RevOps maturity, orchestration roadmap | Cold email copy, domain warmup |
| **Justin Michael** (Pattern 23) | Sales Borg, SEP human+machine outbound | CRM data hygiene program |
| **Eric Nowoslawski** (Pattern 15c) | Inbox infra, deliverability economics | n8n enterprise error handling |
| **Pat Spielmann** (Pattern 17) | Verify-before-send, enrichment copy | MCP agent guardrails |

**Canonical:** `references/gtm-automation-expert-playbook.md` · tool index: `automation-playbook-index.md` (38 playbooks, not 26).

---

## Pattern Number Collisions (Fixed)

| Wrong cite (was) | Correct pattern | Topic |
|---|---|---|
| content-seo skills → Pattern **16** | Pattern **25** | B2B SEO Stack |
| demand-gen skills → Pattern **17** | Pattern **26** | Demand Creation |
| `experts.md` Chris Walker → Pattern **17** + 20 | Pattern **26** + 20 | Demand creation + visitor ID |
| Pattern **16** | Pattern **16** (unchanged) | GTM Data Security |

**Patterns 28–35 (added June 2026):** 28 HR GTM · 29 Legal GTM · 30 RevOps Automation · 31 CRO Enterprise Strategy · 32 Founder Exit Economics · 33 Crisis Management · 34 SaaS Finance & MRR · 35 GTM Compensation Strategy — no collisions with 1–27.

---

## CRO Scale vs Founder Hire Timing (McMahon vs Lemkin)

| Source A | Source B | Canonical guidance |
|---|---|---|
| **John McMahon** — proactive hiring, managers before rep waves, 6-mo enterprise ramp | **Jason Lemkin** — VP Sales after ~$2M ARR; CRO at scale; 70% VP failure if early | **Lemkin = role timing gate** (when to add VP/CRO title). **McMahon = post-gate operating system** (how to inspect, ramp, territory). Do not hire VP/CRO early *then* skip McMahon inspection — both apply at different layers. |
| McMahon: hire ahead of plan when pipeline coverage proves | `sales-team-building`: pass GTM Index ≥6 + scale-readiness gates first | **Gates first, then proactive headcount** — McMahon "bridge" metaphor assumes process exists; Lemkin/Roberge gates prevent premature scale. |
| McMahon: 6 months to full quota productivity (enterprise AE) | `sales-team-building` / Bridge: 4.5–6 months full productivity | **Aligned** — use 6 months as enterprise planning default; 30-60-90 = quota-*bearing* milestones, not full tenured productivity. |
| McMahon: weekly MEDDICC inspection | `sales-team-building` REKS coaching | **Complementary** — REKS diagnoses rep layer; MEDDICC inspects deal evidence. Run REKS before PIP; MEDDICC in weekly pipeline review. |
| Slootman: consumption-aligned comp | Pavilion: CRO gates on ARR + NRR + efficiency | **Consumption cos** add usage/NRR weight to Pavilion gates — see `cro-enterprise-strategy.md` |

---

## Sales Methodology — Challenger vs Transparency vs JOLT

| Expert A | Expert B | Canonical guidance |
|---|---|---|
| **Brent Adamson (Challenger)** — teach, reframe, commercial tension | **Todd Caponi (Transparency)** — lead with weaknesses, radical honesty | **Complementary tones** — Challenger reframes status quo; Transparency builds trust via honesty. Don't use Challenger aggression *against* Caponi-style disclosure on same call without intent. |
| **Challenger (Adamson/Dixon)** — open with insight | **JOLT (Dixon/McKenna)** — late-stage indecision after fit | **Challenger early** (discovery + objection reframe); **JOLT late** ("need to think about it"). Same author on Challenger+JOLT — route by deal stage. |
| **Keenan Gap Selling** — diagnose gap first | **Challenger** — teach reframe | **Gap before teach** — incomplete diagnosis + Challenger insight = happy ears with fancy slides. |
| **Anthony Iannarino** — discipline + leveling | **Jon Barrows** — tactical drills | Iannarino = habit/accountability; Barrows = call-level skill reps. Pair in coaching. |

Refs: `references/brent-adamson-challenger.md` · `anthony-iannarino-sales-discipline.md` · `buyer-indecision` · `transparency-selling`

---

## Customer Success — Murphy vs WbD vs Gainsight

| Source A | Source B | Canonical guidance |
|---|---|---|
| **Lincoln Murphy** — Desired Outcome / Success Gap | **WbD SPICED** post-sale | **Murphy = outcome definition** for CS; **SPICED = sales handoff fields**. Map SPICED Impact → Desired Outcome in kickoff doc. |
| **Nick Mehta / Gainsight** — health score + lifecycle stages | **Murphy** — outcome over activity | Health score **inputs** should predict outcome progress — not login vanity alone. |
| **Wes Bush** — PLG onboarding bowling alley | **Murphy** — appropriate experience | Self-serve **experience** is part of Required Outcome — segment high-touch vs digital-first. |

Ref: `references/lincoln-murphy-customer-success.md` · Pattern 18

---

## PLG Conversion Benchmarks

| Source A | Source B | Canonical guidance |
|---|---|---|
| **Wes Bush** — freemium ~5%, trial ~17% (historical ProductLed survey) | **Kyle Poyar 2026 Report** — segment-specific medians vary by model | Use **Kyle Poyar** for current benchmark tables; **Wes Bush** for onboarding/maturity design. Always label freemium vs trial vs reverse trial. |
| **Elena Verna** — PQL routing | **OpenView PLG** — end-user focus | PQL = **activation event + account score**; don't MQL-wrap product signals. |

Refs: `references/kyle-poyar-growth-unhinged.md` · `references/elena-verna-plg-growth.md`

---

## B2B Marketing Voice — Gerhardt vs Walker vs HubSpot

| Expert A | Expert B | Canonical guidance |
|---|---|---|
| **Dave Gerhardt (Exit Five)** — human brand, community | **Chris Walker** — demand creation, dark social | Gerhardt = **voice + marketer community**; Walker = **measurement philosophy + frequency**. Run both — not either/or. |
| **Dharmesh Shah** — inbound capture + lifecycle | **Walker** — anti–lead-gen volume | HubSpot captures; Walker warns against CPL-only optimization. **Qualify hard** on inbound (Pattern 27 + 26). |

Refs: `references/dave-gerhardt-exit-five.md` · `references/chris-walker-mental-models.md` · Pattern 26/27

---

## Metrics Sources — Bessemer vs Meritech vs Sacks

| Source A | Source B | Canonical guidance |
|---|---|---|
| **Bessemer Atlas** — traditional Rule of 40 | **Meritech** — growth-weighted Rule of 40 | **Board/ops:** Bessemer traditional. **Public valuation comps:** Meritech weighted. Footnote always. |
| **David Sacks** — burn multiple primary | **David Skok** — LTV:CAC primary | **Efficiency gates:** burn multiple at fundraise; **unit economics:** LTV:CAC/payback for motion design. Both in board pack. |
| **KeyBanc private median** ~15% Rule of 40 | **Bessemer aspiration** ≥40% | Median ≠ failure — see Rule of 40 row above. |

Refs: `references/bessemer-cloud-atlas.md` · `references/david-sacks-saas-metrics.md` · `references/meritech-saas-benchmarks.md`

---

## MRR / ARR Definition Alignment

| Source A | Source B | Canonical guidance |
|---|---|---|
| **CRM bookings / TCV** at signature | **RevOps committed MRR** (ACV ÷ 12) | **Board ARR, NRR, Magic Number:** committed MRR bridge only — never TCV in sign month as "MRR added" |
| **Committed MRR × 12** (private) | **Meritech implied ARR** (Q revenue × 4) | **Private ops:** committed. **Public comps:** implied — footnote always; never compare without label |
| **Billings / cash** (annual prepay) | **Committed MRR** | Prepay ↑ cash, not ↑ monthly MRR beyond ACV/12 — see `references/bookings-billings-revenue-matrix.md` |
| **Recognized revenue** (GAAP) | **Committed MRR** | Finance reports recognition; RevOps reports committed bridge — reconcile monthly; implementation delay creates gap |
| **Professional services** in TCV | **SaaS ARR** | **Exclude PS from SaaS ARR** in metrics skills unless board explicitly asks for total revenue |
| **Consumption usage** | **Seat-based MRR** | Hybrid: platform MRR + usage true-up; McMahon/Slootman: track commit vs consumption run-rate |
| **Earn-out / exit ARR** | **Internal dashboard ARR** | Diligence uses **committed recurring** + definitions in LOI — EBITDA earn-out ≠ MRR earn-out (`negotiating-earn-out.md`) |

**Canonical deep dive:** `references/saas-mrr-accounting-nuances.md` · bridge template → `skills/founder-led/saas-metrics-calculator/templates/mrr-bridge-template.md`

**Footnote — saas-metrics-calculator vs financial-modeling:** Calculator = committed MRR formulas. Financial model revenue row may use **recognized** revenue for P&L — link both in board pack.

---

## Demo — Cohan vs Anand Reverse Demo

| Tradition | Expert | Use when |
|---|---|---|
| **Incumbent reverse demo** | Peter Cohan | Displacing vendor — buyer shows current tool in discovery |
| **Product reverse demo** | Varun Anand / Clay | PLG/hybrid — buyer drives your product UI |

**Never merge** — cite explicitly in `demo-scripts`. Ref: `references/peter-cohan-great-demo.md` · `reverse-demo-varun.md`

---

## Files That Should Link Here

- `executive-compensation/references/gtm-compensation-strategy.md`
- `executive-compensation/references/comp-by-role-stage.md`
- `gtm-role-descriptions/references/comp-benchmarks.md`
- `references/saas-metrics-reference.md`
- `references/saas-mrr-accounting-nuances.md`
- `references/bookings-billings-revenue-matrix.md`
- `references/gtm-budget-playbook.md`
- `saas-outcomes/references/exit-metrics-matrix.md`
- `saas-outcomes/references/bootstrap-founder-playbook.md`
- `exiting-company/references/negotiating-earn-out.md`
- `fundraising-strategy/references/vc-milestone-gates.md`
- `skills/analytics/gtm-metrics/SKILL.md`
- `skills/founder-led/saas-metrics-calculator/SKILL.md`
- `skills/founder-led/financial-modeling/SKILL.md`
- `skills/gtm-ops/gtm-spend-management/SKILL.md`
- `skills/growth/expansion-selling/SKILL.md`

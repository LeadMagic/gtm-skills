# Meritech Capital — Public SaaS Benchmarks

**Canonical reference** for Meritech Capital SaaS operating and valuation benchmarks cited across metrics, financial modeling, and outcomes skills.

**Who:** [Meritech Capital](https://www.meritechcapital.com/) — late-stage venture firm (since 1999). Public-facing research arm: **Meritech Benchmarking** (free web app) and **Meritech Software Pulse** (recurring market updates).

**Use when:** Comparing private company metrics to **public SaaS peers**, building board/investor narratives for IPO-track companies, or reconciling benchmarks vs KeyBanc/OpenView/SaaS Capital (private surveys).

---

## Primary Data Products

| Product | URL | What it covers |
|---|---|---|
| **Meritech Benchmarking** | [meritechcapital.com/benchmarking](https://www.meritechcapital.com/benchmarking) | ~120 public SaaS cos — valuation, non-GAAP financials, operating KPIs |
| **Comps table** | [meritechcapital.com/benchmarking/comps-table](https://www.meritechcapital.com/benchmarking/comps-table) | Meritech SaaS Index — filterable cohort |
| **Software Pulse** | [Meritech Substack](https://meritech.substack.com/) | Valuation regime, Rule of 40 composition, growth vs margin tradeoffs |
| **S-1 / IPO reviews** | [meritechcapital.com/blog](https://www.meritechcapital.com/blog) | IPO cohort benchmarks (growth, NRR, efficiency at listing) |

**Data sources:** Company SEC filings + S&P Capital IQ. Updated on earnings releases.

**Contact:** insights@meritechcapital.com

---

## Methodology — Standardized Definitions

Meritech uses **implied** metrics for cross-company comparability. Always state definition when citing.

### Implied ARR

```
Implied ARR = Quarterly total revenue × 4
```

Not the same as contracted ARR reported by all private companies. Use for **public comps only**.

### Traditional Rule of 40

```
Rule of 40 = NTM revenue growth % + NTM free cash flow margin %
```

NTM = next-twelve-months consensus estimate.

### Meritech Rule of 40 (valuation-weighted)

Growth is weighted **3×** relative to FCF margin because public multiples correlate more strongly with growth:

```
Meritech Rule of 40 = (NTM revenue growth % × 3) + NTM FCF margin %
```

Use Meritech Rule of 40 for **public valuation regression** context. Use traditional Rule of 40 for **private board** simplicity (Bessemer/Skok convention in repo).

### Magic Number (Meritech / public cohort)

```
Magic Number = LTM net new implied ARR ÷ LTM S&M expense (prior quarter basis)
```

Align period lag with your private calc — see `references/saas-metrics-reference.md`.

### CAC Payback (public implied)

```
Payback (months) = Prior-quarter LTM S&M ÷ (Current-quarter LTM net new implied ARR × LTM gross margin × 12)
```

Public payback uses **implied ARR deltas** and reported S&M — not identical to private cohort CAC payback. Compare directionally.

### NRR / GRR

Reported per company in filings where disclosed. Meritech cohort medians track **public** retention cooling post-2021 (see reconciliation doc).

---

## Key Public-Market Benchmarks (Indicative)

Refresh from Meritech Benchmarking before board meetings — numbers shift quarterly.

| Metric | Public SaaS median (indicative) | Notes |
|---|---|---|
| **Implied ARR growth (YoY)** | ~17–21% | Stabilized post-2022 correction; AI-native cos outliers higher |
| **NRR** | ~108–111% median (public) | Cooled from 2021 peaks; enterprise leaders 120%+ |
| **GRR** | ~88–92% (public, where reported) | Segment-dependent |
| **Rule of 40 (traditional)** | ~15% median | Only ~30% of public cos ≥40% at once — aspiration not median |
| **Meritech Rule of 40** | Higher correlation to EV/ARR multiple | Use for valuation narrative |
| **FCF margin** | Positive median trend post-2022 | Efficiency era — growth alone insufficient |
| **EV / Implied ARR multiple** | Wide dispersion by growth bucket | <$400M implied ARR trades ~54% lower multiple than >$3B+ (Meritech 2024) |

**IPO readiness framing (Meritech 2024):** Fast-growing, predictable Rule of 40 profile + credible AI story + large market → public markets receptive. Sub-$400M implied ARR IPO cohort faced multiple compression if listed 2020–2021.

---

## Meritech vs Other Repo Sources

| Source | Cohort | Best for |
|---|---|---|
| **Meritech** | ~120 public SaaS | IPO-track comps, EV multiples, NTM Rule of 40 |
| **KeyBanc / Benchmarkit** | ~100–560 private B2B | Private ARR growth, NRR ~101% median, expansion ARR mix |
| **SaaS Capital** | 1,000+ private | Growth-NRR correlation, bootstrap vs equity-backed |
| **OpenView** | PLG-weighted private | Product benchmarks, freemium conversion |
| **Bessemer** | Cloud 100 / public + private | Rule of 40, Cloud Index |
| **David Skok** | Stage gates (canonical formulas) | LTV:CAC, payback thresholds |
| **Henry Schuck / ZoomInfo** | Single public operator | Earnings-season GTM ops metrics |

**Single source of truth for conflicts:** `references/benchmark-reconciliation.md`

---

## Metrics Meritech Emphasizes vs Typical Private Dashboards

| Meritech emphasis | Why it matters |
|---|---|
| **NTM growth + FCF margin composition** | Valuation is margin-aware post-2022 |
| **Implied ARR scale buckets** | Smaller public cos trade at steep multiple discount |
| **Meritech Rule of 40** | Explains why high-growth / low-margin cos still command premiums |
| **S&M efficiency vs growth** | Magic Number and payback on **reported** S&M |
| **NRR trend (12+ quarters)** | Expansion engine durability for public narrative |

Private companies should **not** copy public medians blindly at seed/Series A — use stage gates in `fundraising-strategy/references/vc-milestone-gates.md`.

---

## Application by Skill

| Skill | How to use Meritech |
|---|---|
| `gtm-metrics` | Public-company benchmark column in board stack; cite Meritech for IPO-track |
| `saas-metrics-calculator` | Separate "public comp" vs "private stage" benchmark tables |
| `saas-outcomes` | Exit/IPO path multiples; Rule of 40 composition |
| `financial-modeling` | Scenario planning vs public efficiency frontier |
| `public-company-gtm-metrics` | Pair Schuck operator metrics with Meritech cohort medians |
| `fundraising-strategy` | Series C+ / IPO narrative anchoring |

---

## Quick Diagnostic — Are We Public-Comparable?

| Question | Green | Yellow | Red |
|---|---|---|---|
| Implied ARR growth vs public median | ≥20% | 10–20% | <10% without profitability story |
| NRR | ≥110% | 100–110% | <100% two quarters |
| Rule of 40 (traditional) | ≥40% | 20–40% | <20% and burning |
| FCF margin trend | Improving | Flat | Declining while growth slows |
| Magic Number | ≥0.75 | 0.5–0.75 | <0.5 |

---

## Cross-References

- Reconciliation table → `references/benchmark-reconciliation.md`
- Private committed vs implied ARR → `references/saas-mrr-accounting-nuances.md`
- Formulas → `references/saas-metrics-reference.md`
- Exit weights → `saas-outcomes/references/exit-metrics-matrix.md`
- VC gates → `fundraising-strategy/references/vc-milestone-gates.md`
- Public operator playbook → `gtm-metrics/references/public-company-gtm-metrics.md`
- Expert entry → `references/experts.md` (Meritech Capital)

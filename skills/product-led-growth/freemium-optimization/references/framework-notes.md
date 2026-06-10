# Freemium Optimization — Framework Reference Notes

Supporting reference for `SKILL.md`. Contains the full benchmark tables by
model type, credit-card requirement, and ACV bracket, plus PQL trigger
examples by product type.

---

## Free-to-Paid Conversion Benchmarks by Model

Source: Kyle Poyar (Growth Unhinged) + ChartMogul + ProductLed, *2026
Free-to-Paid Conversion Report* (200 B2B software products).

### Conversion Rate Benchmarks

| Model | GOOD conversion rate | GREAT conversion rate | Notes |
|---|---|---|---|
| Freemium (forever free, no CC) | 3-5% | 8-12% | Rate applied to all signups |
| Free trial (no CC required) | 4-6% | 10-15% | Rate applied to trial starters |
| Free trial (CC required at signup) | 25-35% | 50-60% | Higher rate, far lower signup volume |

### Full-Funnel Signup Rate (Signups per 1,000 Site Visits)

| Model | Signups per 1,000 visits |
|---|---|
| Freemium | ~90 |
| Free trial (no CC) | ~45 |
| Free trial (CC required) | ~15-20 |

### Full-Funnel Math Example (customers per 1,000 visits)

| Model | Signups/1k | Conv rate (GREAT) | Customers/1k visits |
|---|---|---|---|
| Freemium | 90 | 10% | 9.0 |
| Free trial (no CC) | 45 | 12% | 5.4 |
| Free trial (CC required) | 18 | 50% | 9.0 |

At GREAT conversion rates the outcomes converge. At GOOD rates (less common),
freemium often outperforms CC-gated trials on total customers-per-visit.
**Always run the full-funnel math with your actual traffic and conversion
estimates before selecting a model.**

### Market Share of PLG Model Types

| Model | Share of B2B products (2026 report) |
|---|---|
| Free trial | 57% |
| Freemium | 26% |
| Both (freemium + trial) | ~17% |

---

## Conversion Benchmarks by ACV Bracket

Source: ProductLed, *State of B2B SaaS 2025* (446 companies).

| ACV bracket | PQL-to-paid conversion (companies using PQLs) | Free-to-paid conversion (all companies) |
|---|---|---|
| < $5k ACV | ~30% | ~8% |
| $5k–$25k ACV | ~35% | ~10% |
| $25k–$100k ACV | ~38% | ~12% |
| > $100k ACV | ~25% (hybrid: PQL + AE required) | ~6% |

PQL users see roughly 3× higher free-to-paid conversion than non-PQL users
across all ACV brackets.

---

## OpenView 2023 Product Benchmarks — Growth Lever Impact

Source: OpenView Partners, *2023 Product Benchmarks* (with Pendo,
~1,000 participants).

| Growth lever | Impact on fast-growth likelihood |
|---|---|
| Tracking PQLs/PQAs | +61% (highest measured) |
| Outreach to free signups | +28% |
| Dedicated growth team | +17% |
| Over-relying on paid acquisition | Inversely correlated |

---

## Model Intentionality Score (ProductLed 2025)

Rate your current free model 1-10 on each criterion:

| Criterion | Score (1-10) |
|---|---|
| Free tier showcases the product's core value proposition | |
| Value limits are deliberate (not accidental or arbitrary) | |
| Natural upgrade paths exist inside the free experience | |
| Upgrade benefits are visible from within the free product | |
| Free users can share/collaborate in ways that drive virality | |

Average the five scores. Companies averaging 8+ report 57% better free-to-paid
conversion than companies averaging 3 or below (ProductLed 2025).

---

## PQL Trigger Examples by Product Type

Use these as starting points when building the PQL scoring model in Phase 4.
Calibrate weights to your product's actual activation and conversion data.

### Collaboration / Productivity SaaS
- Invited 2+ team members (expansion signal, weight: 15)
- Created and shared 3+ documents or artifacts (usage depth, weight: 25)
- Logged in 5+ days in the past 14 days (frequency, weight: 20)
- Completed the core activation event (activation, weight: 30)
- Company size 20-500 employees / ICP match (fit, weight: 10)

### Sales / CRM / Outreach Tool
- Imported a contact list or connected CRM (activation signal, weight: 30)
- Sent 10+ emails or made 5+ calls (usage depth, weight: 25)
- Logged in on 4+ separate days in 14-day window (frequency, weight: 20)
- Company is in a target vertical + has 10-200 sales headcount (fit, weight: 15)
- Connected 2+ integrations (expansion signal, weight: 10)

### Data / Analytics Tool
- Ran first report with live data (activation, weight: 30)
- Ran 5+ queries or reports (usage depth, weight: 25)
- Connected 2+ data sources (expansion signal, weight: 15)
- Active on 3+ days in 14-day window (frequency, weight: 20)
- Company has a data/analytics job posting (fit proxy, weight: 10)

### Developer / API Tool
- Made first successful API call (activation, weight: 30)
- Exceeded 100 API calls in 7 days (usage depth, weight: 25)
- Active on 4+ days in 14-day window (frequency, weight: 20)
- Company is a SaaS or tech company (fit, weight: 15)
- Invited a collaborator to the workspace (expansion, weight: 10)

---

## Activation Event Definition Template

Use this template when defining (or auditing) the activation event in Phase 2.

| Field | Example |
|---|---|
| Event name | "User views live-data report" |
| Product trigger | `report.viewed` with `data_source = live` |
| Completion criteria | Event fires once; user has been in-app for ≥ 2 minutes |
| Median time-to-activation | Measure from signup timestamp to event timestamp |
| Target median | < 7 days |
| Current p90 | Measure; identify where users drop off in the funnel |

---

## Sources

- Kyle Poyar, ChartMogul, ProductLed, "2026 Free-to-Paid Conversion Report," growthnotes.substack.com and chartmogul.com, 2026.
- ProductLed, "State of B2B SaaS 2025," productled.com, 2025.
- OpenView Partners, "2023 Product Benchmarks," openviewpartners.com, 2023.
- Wes Bush, *Product-Led Growth: How to Build a Product That Sells Itself*, Product-Led Institute, 2019.
- Wes Bush, *Product-Led Onboarding*, Product-Led Institute, 2021.

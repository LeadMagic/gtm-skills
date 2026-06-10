# GTM System Architecture — Framework Notes

## Winning by Design — GTM Index (Six Models)

Score each 1–10. Weakest link caps the entire system.

| Model | Question | Fix With |
|---|---|---|
| Revenue | Pricing/packaging clear? | `pricing-strategy`, `deal-desk` |
| Data | CRM answers basic questions? | `crm-integration`, `gtm-metrics` |
| Math | Unit economics work? | `gtm-metrics`, `financial-modeling` |
| Operating | Documented process exists? | `pipeline-management`, `sales-enablement` |
| Growth | Channels measured by CAC? | `marketing-strategy`, `campaign-analytics` |
| GTM | Sales/Marketing/CS aligned? | `gtm-system-architecture` (Bowtie) |

Score Operating Model <6 → do NOT scale headcount or agencies.

## Winning by Design — Bowtie

```
Awareness → Education → Selection → Onboarding → Adoption → Expansion → Renewal
[Marketing]   [Marketing]  [Sales]   [CS]        [CS]      [CS/Sales]   [CS]
```

Each stage: owner, goal, handoff criteria, metrics.
Load `pipeline-management` for Selection (sales) stage detail.
Load `customer-onboarding`, `expansion-selling` for right-side stages.

## SiriusDecisions Demand Waterfall

Demand flows through defined stages with conversion metrics and handoffs.
Maps to left side of Bowtie: inquiry → MQL → SQL → opportunity.

## Agent Use

1. Score all six models with evidence before recommending fixes.
2. Identify weakest link — fix that first.
3. Bowtie handoffs must have owner + SLA + package contents.
4. Route Operating Model fixes to `pipeline-management` + `sales-enablement`.

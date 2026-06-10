# GTM Licensing Models

How vendors price — and what to model in TCO. Pair with `templates/tool-cost-sheet.md`.

---

## Model types

| Model | How it bills | Examples | Budget risk |
|---|---|---|---|
| **Per seat** | Named users × monthly fee | CRM, Gong, Outreach | Seat creep |
| **Platform + seat** | Base fee + per user | HubSpot Enterprise, Salesforce | Platform minimum |
| **Usage / credits** | Prepaid or metered units | Clay, enrichment APIs, LLM | Volume spikes |
| **Contact / record tier** | MA contacts band | HubSpot Marketing Hub | List bloat |
| **Mailbox / domain** | Sending infrastructure | Instantly, Smartlead | Inbox count |
| **MTU / events** | Product analytics | Amplitude, Mixpanel | Traffic growth |
| **Agent seat** | Support reps | Zendesk, Intercom | CS headcount |
| **Consumption cloud** | AWS, Snowflake, n8n executions | RevOps data stack | Unmonitored jobs |

---

## Per-seat mechanics

```
annual_seat_cost = seats × price_per_seat_month × 12
```

**Watch for:**

- Minimum seat commits (e.g., 10-seat floor)
- Sales vs service vs view-only pricing tiers
- Sandbox / dev seats billed separately
- Annual prepay vs monthly (+15–20% uplift on monthly)

**Audit quarterly:** disable inactive users; true-down at renewal.

---

## Platform fee mechanics

```
annual = platform_fee + seat_component + add_on_modules
```

Common add-ons: Salesforce CPQ, HubSpot Ops Hub, premium support (15–22% of license).

**Implementation (amortize 3 years in TCO):**

| CRM | Typical Y1 SI range |
|---|---|
| HubSpot Pro → Enterprise | $5K–$25K |
| Salesforce mid-market | $25K–$75K |
| Salesforce enterprise | $75K–$250K+ |

---

## Credit / usage mechanics

```
monthly_cost = platform + (units_consumed × unit_price)
annual = monthly × 12 + overage_history_buffer(10–20%)
```

| Unit | Typical pricing axis |
|---|---|
| Verified email | $0.03–$0.15 |
| Company enrich | $0.10–$0.50 |
| Clay credit | Vendor tier table |
| LLM tokens | Model × workflow volume |
| n8n execution | Per run or cloud tier |

**Always model 1× / 2× / 3× volume** — see tool-cost-sheet sensitivity table.

---

## Bundling & consolidation

| Pattern | Savings lever |
|---|---|
| HubSpot CRM + MA bundle | Single vendor discount |
| Salesforce + Data Cloud | Enterprise commit |
| Best-of-breed stack | Negotiate co-termed renewals |

Scott Brinker rule: each redundant category costs **15–30%** extra admin + renewal leverage.

---

## Contract terms that affect TCO

| Term | Impact |
|---|---|
| Multi-year (2–3 yr) | 10–20% discount typical |
| True-down rights | Reduces seat creep cost |
| Credit rollover cap | Avoids use-it-or-lose-it waste |
| Auto-renewal + uplift | 5–8% automatic — calendar alerts |
| Payment terms | Annual cash vs quarterly |

Detail → `vendor-contracts`

---

## Allocation across departments

Shared tools split by **primary consumer**:

| Tool | Sales % | Marketing % | CS % |
|---|---:|---:|---:|
| CRM | 60 | 25 | 15 |
| Enrichment | 70 | 20 | 10 |
| Gong | 85 | 5 | 10 |
| MA platform | 10 | 75 | 15 |

Document in board / finance memo for CAC modeling (`financial-modeling`).

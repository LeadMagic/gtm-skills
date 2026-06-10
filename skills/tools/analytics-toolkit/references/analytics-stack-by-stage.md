# Analytics Stack by Stage

| Stage | CDP | Product analytics | Web | Warehouse |
|---|---|---|---|---|
| **Pre-PMF** | Rudderstack / Segment free | PostHog cloud | GA4 | Optional |
| **$1–5M ARR** | Segment | Amplitude or PostHog | GA4 | BigQuery / Snowflake lite |
| **$5–20M ARR** | Segment Teams | Amplitude | GA4 + ads link | Warehouse required |
| **Enterprise** | Segment + governance | Amplitude + experimentation | GA4 + server GTM | Full BI stack |

**Rule:** CDP first — collect once, route everywhere (`tracking-plan`).

---

## Event priority (first 10)

| Event | Properties | Destinations |
|---|---|---|
| `signed_up` | plan, source | All + warehouse |
| `activated` | activation_definition | Product + CRM |
| `feature_used` | feature_name | Product |
| `invited_teammate` | seats | Product + CRM |
| `upgraded` | from_tier, to_tier | All + finance |
| `churned` | reason | Product + CS |

Full taxonomy: `tracking-plan` skill.

---

## Spend

Analytics tools → `gtm-spend-management` vendor register (Segment, Amplitude MTU tiers).

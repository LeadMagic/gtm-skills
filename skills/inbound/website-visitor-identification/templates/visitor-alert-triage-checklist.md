# Visitor Alert Triage Checklist

*Use for every Slack `#intent-*` alert before sales action.*

---

## Alert metadata

| Field | Value |
|---|---|
| Date / time | |
| Vendor source | Clearbit / RB2B / 6sense / other |
| ID level | Company / Person |
| Confidence tier | High / Medium / Low |
| UTM / referrer | |

---

## Company context

| Check | Pass? | Notes |
|---|---|---|
| Company domain resolves and matches CRM account | ☐ | |
| Employee count in ICP range | ☐ | |
| Industry / tech fit | ☐ | |
| Not agency, ISP, university, or VPN suspect | ☐ | |
| Not existing customer (active opp or onboarding) | ☐ | |
| Geo fits territory | ☐ | |

---

## Person context (if person-level alert)

| Check | Pass? | Notes |
|---|---|---|
| Privacy go/no-go completed for this vendor | ☐ | See `visitor-id-privacy-gtm.md` |
| LinkedIn title matches buyer persona | ☐ | |
| Still employed at matched company (manual verify) | ☐ | |
| Email found + verified (`lead-enrichment`) | ☐ | |
| Not on suppression / opt-out list | ☐ | |
| EU visitor — counsel-approved only | ☐ | |

---

## Engagement context

| Signal | Value |
|---|---|
| Pages viewed (7d) | |
| High-intent pages? (pricing, demo, docs) | ☐ |
| Visit count (14d) | |
| ICP tier (1 / 2 / 3) | |

---

## Routing decision

| Outcome | Action |
|---|---|
| **Route to AE** | ICP Tier 1 + high intent + existing opp |
| **Route to SDR** | ICP fit + medium/high engagement |
| **Research queue** | Medium confidence — no auto sequence |
| **ABM nurture only** | Company fit, low engagement |
| **Discard** | Low confidence, non-ICP, or privacy block |

**Assigned to:** _______________  
**SLA deadline:** _______________

---

## Outreach guardrails (person ID)

- [ ] Use signal-anchored copy — not "I watched you browse"
- [ ] Max 2 automated touches on visitor-only signal
- [ ] Log `visitor_id_source` + date in CRM
- [ ] Stop all touches if opt-out received

---

## Anti-patterns (do not)

- ☐ Blast generic sequence to every alert
- ☐ Create CRM contact without ICP pass
- ☐ Reference exact browsing path in cold email
- ☐ Ignore opt-out from any channel

**Skills:** `website-visitor-identification`, `inbound-triage`, `cold-email-strategy`, `icp-scoring`

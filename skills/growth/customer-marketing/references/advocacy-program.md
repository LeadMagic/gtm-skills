# Customer Advocacy Program

*Gainsight Advocacy Maturity + Influitive advocate marketing. Reviews detail → `review-platforms`.*

---

## Advocacy ladder (operating)

| Level | Trigger | Owner | Reward (no cash-for-review ToS violation) |
|---|---|---|---|
| Logo | Paying customer + permission | Marketing | Website feature |
| G2/Capterra review | NPS 9–10 | CSM | Thank-you + charity donate option |
| Testimonial | 6+ months, clear outcome | Marketing | Swag / co-marketing |
| Case study | Metrics + exec sponsor | Marketing + CS | Backlink, webinar slot |
| Reference call | NPS 9+, capped | AE + CS | Priority support |
| Speaker | Articulate champion | Marketing | Honorarium / travel |
| Advisory | Power user | Product | Early access / stipend |

**Cap:** 2–3 reference calls per customer per quarter.

---

## CRM fields

| Field | Values |
|---|---|
| `advocacy_tier` | 1–8 |
| `referenceable` | Y/N |
| `reference_calls_ytd` | count |
| `review_platform` | G2 / TrustRadius / none |
| `last_advocacy_ask` | date |

---

## Review generation

Delegate platform playbooks to `review-platforms` — this skill owns **who to ask**; review-platforms owns **how on G2/TR**.

| Moment | Ask |
|---|---|
| NPS 9–10 | Within 48h |
| Renewal signed | Within 1 week |
| QBR positive | Same call follow-up |

**Never:** Gift cards if platform ToS prohibits — check current G2/TR policy.

---

## Case study pipeline

```
Identify (CSM) → Qualify (metrics?) → Interview → Draft → Legal/logo → Publish → Distribute
```

Target: 1 published case study / month at scale.

Template: `templates/case-study-interview-questions.md`

---

## Spend / rewards

Advocacy rewards (swag, events, charity) → `gtm-spend-management` GTM-GIFT or marketing card with caps.

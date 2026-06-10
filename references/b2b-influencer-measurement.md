# B2B Influencer Measurement — ROI, Dark Social & UTM Limits

**Measurement companion** to `references/b2b-influencer-strategy.md` and `references/aneesh-wishly-b2b-influencer.md` (Aneesh Lal / Wishly Group methods).

**Core tension:** B2B influencer impact spans **measurable** (landing pages, form fills) and **dark social** (Slack shares, DMs, word-of-mouth) — Chris Walker argues demanding 100% last-click attribution under-funds the highest-converting channels.

---

## What You Can Measure vs What You Must Model

| Layer | Measurable | Modeled / qualitative |
|---|---|---|
| **Direct** | Landing page sessions, form fills, demo requests | — |
| **Engagement quality** | ICP % among likers/commenters (Clay scrape) | — |
| **Pipeline influence** | CRM companies appearing post-campaign (30-day lookback) | Self-reported "heard on LinkedIn" |
| **Revenue** | Closed-won with campaign member / influenced opp | Multi-touch attribution |
| **Dark social** | Branded search lift, direct traffic | Slack/WhatsApp shares (no UTM) |

Cross-link: `references/chris-walker-mental-models.md` § Dark Social · `attribution` skill.

---

## Wishly / Aneesh Attribution Stack (Public)

### 1. Creator-specific landing page

One URL per creator collaboration — centralizes traffic from LinkedIn, newsletter, podcast.

| Field | Purpose |
|---|---|
| `utm_source` | `linkedin` or `newsletter_[creator]` |
| `utm_medium` | `influencer` or `organic_social` |
| `utm_campaign` | `[date]-[segment]-influencer-[creator_slug]` |
| Hidden field | `creator_id` for CRM |

**Benchmark:** Compare landing page traffic and conversion vs brand baseline during campaign window.

### 2. Engagement → ICP scrape (Clay method)

Public workflow from G2 interview:

1. Export likers/commenters from sponsored posts (public data only)
2. Enrich in Clay — title, company, seniority
3. Score % matching ICP / ABM list
4. Report overlap % to CFO (e.g., "20% of target accounts engaged")

**Privacy:** Public engagement data only; GDPR/CCPA-compliant collection practices.

### 3. CRM lookback (30 days)

Questions Aneesh cites for finance conversations:

- How many engaged companies entered pipeline post-campaign?
- Were they net-new to CRM or existing nurture?
- Did deal velocity improve for influenced accounts?

**CRM field:** `influenced_by_creator` (picklist) + `influencer_campaign` (campaign member).

### 4. Self-reported influence

Discovery call question: "How did you first hear about us?"

Track in CRM — captures dark social Walker describes.

---

## UTM Limits for Influencer Campaigns

UTMs work for **clickable** destinations. They fail for:

| Channel | UTM works? | Alternative |
|---|---|---|
| LinkedIn post → landing page | Yes | Per-creator landing page |
| LinkedIn comment engagement | No | Scrape + CRM match |
| Newsletter forward | Partial | Unique links per placement |
| Podcast audio | No | Vanity URL + self-report |
| Slack share | No | Branded search + influenced field |
| Creator DM intro | No | SDR asks source on call |

**Governance:** `campaign-governance` → `utm-governance.md`

| Rule | Influencer-specific |
|---|---|
| `utm_medium=influencer` | Standardize for warehouse joins |
| `utm_source=linkedin` | Separate paid boost in medium if needed |
| No manual URLs | UTM builder only |
| Non-compliant campaigns | Excluded from ROI dashboard |

**Do not:** Claim influencer ROI from last-click alone when 60%+ of B2B journey is dark social.

---

## KPI Framework

### Leading indicators (weekly)

| Metric | Target direction | Source |
|---|---|---|
| ICP engagement rate | ↑ | Clay scrape |
| ABM overlap % | ↑ vs random baseline | ABM ∩ engagers |
| Landing page CVR | ↑ vs site avg | Analytics |
| Comment quality (ICP titles) | ↑ | Manual + scrape |
| Cost per ICP engager | ↓ | Spend ÷ ICP engagers |

### Lagging indicators (30–90 days)

| Metric | Source |
|---|---|
| Influenced pipeline $ | CRM campaign influence |
| Net-new accounts in CRM | Lookback match |
| Influenced opp win rate | CRM |
| CAC vs paid social benchmark | Finance |
| Renewal / program NPS | Brand survey |

### CFO package (minimum)

1. Case study with comparable ROI (public: 7:1 on $200K over 4 months — PartnerStack/Wishly cite)
2. ABM overlap analysis
3. Landing page performance vs baseline
4. Pipeline influenced $ (even if not last-touch attributed)
5. 90-day evaluation window — not 2-week judgment (Walker frequency rule)

---

## Employee Advocacy Metrics (Internal)

| Metric | Notes |
|---|---|
| SSI score | LinkedIn baseline |
| Posts per advocate / month | Consistency |
| ICP engagement on employee posts | Clay scrape same method |
| Influenced opps (self-reported) | CRM field |
| **Do not** | Compare employee reach to paid creator reach — different jobs |

---

## Anti-Patterns in Measurement

1. **Follower count as KPI** — vanity without ICP
2. **Impressions-only reporting** — no engagement quality or pipeline
3. **Last-click UTMs on LinkedIn** — misses dark social majority
4. **2-week kill decision** — violates 90-day demand program minimum
5. **No baseline** — landing page CVR without pre-campaign comparison
6. **Ignoring existing CRM accounts** — engagers may accelerate nurture, not net-new
7. **UTM chaos** — breaks warehouse; see campaign-governance

---

## Integration Map

| Framework | Adds |
|---|---|
| **Chris Walker** | Dark social acceptance; frequency; 90-day eval |
| **Aneesh Lal / Wishly** | Landing page + Clay scrape + CRM lookback |
| **Campaign governance** | UTM dictionary, naming, audit |
| **GTM metrics** | Pipeline influenced in board stack |
| **Lifecycle awareness** | Influencer = stage 1 metric input (`references/gtm-lifecycle-stages.md`) |

---

## Public Sources

- [G2 — Aneesh Lal attribution & CFO tips](https://learn.g2.com/industry-insights-aneesh-lal-b2b-influencer-marketing-secrets)
- [PartnerStack — Wishly ROI example](https://partnerstack.com/articles/partner-spotlight-2025)
- [Refine Labs — Chris Walker demand creation](https://www.refinelabs.com/)
- Repo: `references/chris-walker-mental-models.md`

**Template:** `references/templates/influencer-partnership-scorecard.md`

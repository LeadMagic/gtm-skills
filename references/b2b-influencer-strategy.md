# B2B Influencer Strategy — Master Guide

**Canonical playbook** for B2B creator and influencer GTM. Expert source → `references/aneesh-wishly-b2b-influencer.md` (Aneesh Lal / Wishly Group). Measurement → `references/b2b-influencer-measurement.md`.

---

## Program Types

| Type | Description | Best for | Governance |
|---|---|---|---|
| **Paid creators** | Flat fee + deliverables bundle (posts, newsletter, podcast) | Category awareness, pipeline acceleration | Agency or in-house partnerships lead |
| **Gifting / seeding** | Product access, swag, experiences — no cash | PLG trials, ABM warm-up | `strategic-gifting` + spend caps (`gtm-spend-management`) |
| **Affiliates / rev-share** | Commission on attributed revenue | Bottom-funnel, self-serve PLG | PartnerStack-style tracking; unique codes |
| **Employee advocates** | Enabled employees post on LinkedIn | Trust, hiring, product depth | Legal/compliance review; advocacy ladder (`customer-marketing`) |
| **Customer champions** | Paying users as micro-creators | Social proof, case studies | Reference program caps; NPS gates |

**Wishly default (external):** Paid creator bundles with Awareness → Education → Conversion arc — not single-post transactions.

---

## B2B vs B2C Influencer Marketing

| Dimension | B2B | B2C |
|---|---|---|
| **Primary platform** | LinkedIn (video feed, carousels, newsletters) | Instagram, TikTok, YouTube |
| **Buyer** | Committee; long cycle; CFO scrutiny | Individual; shorter cycle |
| **Creator profile** | Revenue SME, operator, practitioner | Lifestyle, entertainment, celebrity |
| **Success metric** | ICP engagement, pipeline signals, account overlap | Reach, ROAS, conversions |
| **Content** | Problem-first, co-authored depth, webinars | Visual hooks, UGC, trends |
| **Attribution** | Landing pages + CRM lookback + dark social | Pixel + promo codes |
| **Brand safety** | Professional context; demo authenticity | Platform saturation, bots |

---

## ICP-Aligned Creator Selection

### Scorecard dimensions

| Criterion | Weight | How to verify |
|---|---|---|
| Audience title/industry match | 30% | Manual sample + Clay engagement scrape |
| ABM account overlap % | 25% | Sales Navigator ∩ creator engagers |
| Content quality & authenticity | 20% | Past sponsored posts; product usage |
| Multi-channel reach | 15% | Newsletter subs, podcast downloads |
| Reliability & brand fit | 10% | Reference checks; prior brand renewals |

Use `references/templates/influencer-partnership-scorecard.md` for evaluations.

### Red flags

- Follower count without ICP breakdown
- No secondary channel (newsletter/podcast) for B2B depth
- Creator promotes competing categories weekly
- Marketplace match without strategist mediation
- Refuses product demo before endorsement

---

## Campaign Architecture (Wishly-Aligned)

```
Awareness (LinkedIn posts + optional boost)
    ↓
Education (newsletter, podcast, co-authored guide)
    ↓
Conversion (landing page, comment CTA, creator call)
    ↓
Nurture (engage commenters; CRM match; SDR follow-up)
```

**Minimum viable bundle (90 days):**

| Week | Deliverable |
|---|---|
| 1–2 | 2 LinkedIn posts (1 video <60s, 1 carousel) |
| 3–4 | Newsletter sponsorship |
| 5–6 | Co-authored asset (guide/checklist) |
| 7–8 | Podcast segment or fireside chat |
| 9–12 | Boost top performer; CRM lookback review |

**Bi-weekly** brand ↔ creator sync. **Day 90** renewal gate.

---

## Contract & Brief Essentials (GTM Level)

*Not legal advice — align with counsel on IP, exclusivity, and disclosure.*

| Element | Include |
|---|---|
| **Deliverables** | Format, count, dates, approval rounds |
| **Usage rights** | Organic only vs paid boost whitelisting |
| **Authenticity** | Demo/use requirement; approval of claims |
| **Exclusivity** | Category exclusivity window (e.g., 30 days) |
| **FTC/disclosure** | #ad / paid partnership label per platform rules |
| **Performance data** | Creator shares analytics; brand may scrape public engagers |
| **Kill clause** | Off-brand behavior, missed deadlines |
| **Payment** | Milestones tied to live deliverables |

**Brief must contain:** ICP definition, 3 problem hooks, proof points, landing page URL, UTM convention (`campaign-governance`), forbidden claims, sample posts.

Template → `references/templates/b2b-influencer-program-brief.md`.

---

## Content Approval Workflow

| Step | Owner | SLA |
|---|---|---|
| 1. Brief issued | Marketing | T-14 days |
| 2. Creator draft | Creator | T-7 days |
| 3. Legal/PMM review | Marketing + Legal | 48h |
| 4. Revision round | Creator | 48h |
| 5. Final approval | Marketing lead | 24h |
| 6. Schedule + UTMs | RevOps | Before publish |
| 7. Post-live QA | Marketing | Within 4h |

**Rule:** Creator voice wins on tone; brand wins on claims and compliance.

---

## Employee Advocacy Program (Internal Influencers)

Distinct from paid external creators:

| Layer | Action |
|---|---|
| **Identify** | AEs, CS, founders with LinkedIn activity |
| **Enable** | Talk tracks, proof points, content calendar |
| **Govern** | Pre-approval for product claims; social policy |
| **Measure** | SSI, engaged comments from ICP, self-reported influenced opps |
| **Reward** | Recognition, SPIFFs, early access — not mandatory posting |

Cross-link: `customer-marketing` advocacy ladder · `founder-brand` · `social-selling`.

---

## Integration with GTM Stack

| System | Role |
|---|---|
| **Clay** | Engagement scrape, ICP scoring, ABM overlap |
| **Sales Navigator** | Account list validation |
| **CRM** | Influenced opp field; campaign member from landing page |
| **MAP** | Nurture engagers who convert on landing page |
| **Ramp / spend** | Creator fees as program line item (`gtm-spend-management`) |

---

## Anti-Patterns

1. Vanity metrics without ICP validation
2. One-and-done posts with no education layer
3. UTMs as sole attribution on LinkedIn (see measurement doc)
4. Creators outside your buyer persona
5. No post-campaign engagement follow-up
6. Mixing employee advocacy compliance with creator contract terms
7. Judging program at 2 weeks — use 90-day minimum (Chris Walker frequency rule)

---

## Public Sources

- [G2 — Aneesh Lal B2B influencer secrets](https://learn.g2.com/industry-insights-aneesh-lal-b2b-influencer-marketing-secrets)
- [Netinfluencer — Wishly Group](https://www.netinfluencer.com/how-the-wishly-group-is-transforming-linkedin-creator-economy/)
- [PartnerStack — Wishly partner spotlight](https://partnerstack.com/articles/partner-spotlight-2025)
- [Wishly Group](https://wishlygroup.ca/)
- [Chris Walker — dark social](https://www.refinelabs.com/) → `references/chris-walker-mental-models.md`

---

## Skill Routing

| Task | Skill |
|---|---|
| Program design | `customer-marketing` (canonical), `social-selling` |
| LinkedIn DM follow-up | `social-selling`, `inbound-triage` |
| Measurement | `gtm-metrics`, `campaign-governance`, `attribution` |
| ABM + creators | `abm-strategy`, `abm-1-to-few` |
| Gifting layer | `strategic-gifting` |
| Lifecycle placement | Awareness stage → `references/gtm-lifecycle-stages.md` |

**Pattern:** `using-gtm-skills` → Pattern 19: B2B Influencer & Creator GTM

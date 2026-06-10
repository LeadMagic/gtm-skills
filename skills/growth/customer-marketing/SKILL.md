---
name: customer-marketing
description: >-
  Customer marketing and advocacy programs — case studies, testimonials,
  customer reference programs, NPS-driven advocacy, customer communities,
  user conferences, champion programs, logo usage, and review generation
  (G2, Capterra). Use when building customer marketing, generating case
  studies, launching a reference program, or mobilizing customer advocates.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "2.4.0"
  author: LeadMagic
  category: growth
  tags: [customer-marketing, advocacy, case-studies, references, testimonials, reviews, community]
  related_skills: [review-platforms, cs-playbooks, case-study-builder, social-media-strategy, content-marketing, referral-programs, gtm-spend-management]
  frameworks:
    - "Bain & Company — NPS (Net Promoter System, Fred Reichheld)"
    - "Gainsight — Customer Advocacy Maturity Model"
    - "Influitive — Advocate Marketing"
    - "SaaSquatch — Customer-Led Growth"
    - "Varun Anand (Clay) — Community Selling & Ecosystem GTM"
    - "Aneesh Lal (Wishly Group) — B2B Creator Partnerships & Advocacy"
    - "Dharmesh Shah (HubSpot) — Flywheel Delight & Customer Advocacy"
---

# Customer Marketing

## Overview

Your best salespeople are your customers — and they work for free. A customer
saying "we grew 3x with this product" is worth more than every ad you'll ever
run. The mistake: treating customer marketing as an afterthought (sending a
"would you write a review?" email once a year). The fix: a systematic advocacy
program that turns happy customers into your most powerful GTM engine.

## Frameworks Referenced

This skill is grounded in public frameworks and source material relevant to the task:

- **Bain & Company — NPS (Net Promoter System, Fred Reichheld).** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Gainsight — Customer Advocacy Maturity Model.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Influitive — Advocate Marketing.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **SaaSquatch — Customer-Led Growth.** Use the relevant method or published guidance where it improves the requested deliverable; do not cite it as decoration.
- **Varun Anand (Clay) — Community Selling.** Infiltrate existing Slack/WhatsApp/MSP groups before building your own; value-first problem responses; reverse demo → mandatory Slack join; education layer (University, Clubs) before scaled sales. Load `references/community-selling-varun.md`. Pairs with `demo-scripts` → `reverse-demo-varun.md`.
- **Aneesh Lal (Wishly Group) — B2B Creator Partnerships.** External LinkedIn creators for awareness → education → conversion; ICP-aligned selection (not vanity followers); multi-channel bundles (newsletter, podcast, co-authored assets). Distinct from **employee advocacy** (advocacy ladder below) and **customer champions** (levels 4–8). Load `references/aneesh-wishly-b2b-influencer.md` + `references/b2b-influencer-strategy.md`. Pair with Chris Walker dark social for attribution reality (`references/chris-walker-mental-models.md`).
- **Dharmesh Shah (HubSpot) — Flywheel Delight.** Customer marketing is the **Delight** leg of the inbound flywheel — reviews, references, and champions reduce friction for Attract (SEO, social proof) and Engage (faster trust). Load `references/dharmesh-shah-hubspot-inbound.md`. Pattern 27 step 5.

## When to Use

Trigger phrases: "customer marketing", "case study program", "customer
references", "customer advocacy", "G2 reviews", "build a reference program",
"customer community", "logo usage program", "B2B influencer program",
"creator partnerships", "employee advocacy", "LinkedIn creator GTM", "crisis comms", "negative reviews
viral", "reputation management", "bad press"

## Step-by-Step Process

### Phase 1: The Advocacy Ladder

| Level | What Customer Does | Required Health | Reward |
|---|---|---|---|
| 1. Logo Usage | Allows logo on website | Any paying customer | Featured |
| 2. Written Review | G2/Capterra review | NPS > 7 | $25 gift card |
| 3. Quote/Testimonial | Named quote on website | NPS > 8, 6+ months | Featured + swag |
| 4. Case Study | Full story with metrics | NPS > 8, clear results | Co-marketing + backlink |
| 5. Reference Call | Takes prospect calls | NPS > 8, available | Priority support + gifts |
| 6. Speaking/Webinar | Co-presents at event/webinar | NPS > 9, articulate | Travel + honorarium |
| 7. Advisory Board | Product feedback, strategy | Power user, invested | Equity or honorarium |
| 8. Community Leader | Runs user group/chapter | Superuser | Recognition + access |

### Phase 2: Case Study Engine

**Pipeline:** Identify 3-5 candidates → interview → draft → approve → publish.
Target: 1 new case study/month.

**Interview questions:** `templates/case-study-interview-questions.md`  
Publish via `case-study-builder`.

### Phase 3: Review Generation

Full platform playbooks → **`review-platforms`** (G2, TrustRadius, ask emails,
response SLA). This skill identifies **who** to ask from NPS promoters.

**Target:** 2–4 new reviews/month (recency beats annual bursts). Respond to
negatives <48h. Check platform ToS before cash/gift incentives.

### Phase 4: Reference Program

**Formalize:** `templates/reference-program-spec.md` — CRM fields, caps,
rotation, rewards. Advocacy spend → `gtm-spend-management`.

### Phase 5: Customer Community

**Formats:** Slack community, LinkedIn group, annual user conference, regional
meetups, virtual roundtables. Start small. One format. Grow from there.

### Phase 6: Crisis & Reputation (External Comms)

When incidents threaten advocacy and pipeline trust — load **`references/crisis-management-playbook.md`** (Pattern 33). Executive war room → `gtm-leadership`.

| Crisis signal | Marketing action |
|---|---|
| Outage / breach | Pause scheduled campaigns; unify with status page + holding statement |
| Viral negative G2/TR | Respond <24h; no cash incentives for positive reviews during incident |
| Bad press | CEO/comms lead only; counsel for Sev 3+ |
| Churn wave / NRR story | Stop reference asks; honest customer email if product-related |

**Chris Walker — dark social:** Buyers discuss vendor failures in Slack/DMs — monitor via CS/sales, not just public mentions. → `references/chris-walker-mental-models.md`

**Templates:** `skills/management-leadership/gtm-leadership/templates/crisis-holding-statement.md`, `crisis-faq-for-support.md`  
**Experts:** `references/saas-pr-crisis-experts.md` (Highwire, Offleash for retained PR)

### Phase 7: B2B Creator & Influencer Partnerships

**External creators** (paid) vs **employee advocates** (enabled) vs **customer
champions** (advocacy ladder) — three different programs; do not conflate.

| Program | Owner | Canonical reference |
|---|---|---|
| Paid LinkedIn creators | Marketing | `references/b2b-influencer-strategy.md` |
| Employee advocacy | Marketing + HR | Advocacy ladder + `social-selling` SSI |
| Customer champions | CS + Marketing | Levels 4–8 above |

**Wishly-aligned minimum:** 90-day bundle (posts + newsletter + co-authored asset);
ICP overlap check before sign; bi-weekly reviews; measurement →
`references/b2b-influencer-measurement.md`. Brief template →
`templates/b2b-influencer-program-brief.md`.

## Implementation Checklist

- [ ] Case study pipeline: 3 candidates in progress, 1 published/month target
- [ ] 20+ G2 reviews (respond to every one)
- [ ] Reference program: 10+ referenceable customers, capped calls/quarter
- [ ] Logo usage: permission obtained for all logos on website
- [ ] Advocacy ladder documented with levels, triggers, and rewards

## Common Pitfalls

1. **Asking for favors without rewards.** "Can you write a review?" with nothing
   in return. Fix: Every advocacy request includes a reward — gift card, swag,
   early access, co-marketing.
2. **Over-using references.** Same 3 customers do 10 reference calls each.
   They burn out. Fix: Cap at 2-3/quarter. Rotate.
3. **Publishing case studies without metrics.** "Acme Corp loves us" is not
   a case study. Fix: Every case study has before/after metrics.
4. **No review response.** Negative G2 review sits unanswered for months.
   Prospects see it. Trust evaporates. Fix: Respond within 24 hours. Every time.


## Output Format

Customer marketing program plan containing: (1) advocacy ladder — all eight
levels from logo usage to advisory board, with required NPS threshold, health
criteria, and reward for each level; (2) case study pipeline — active candidates
list, interview question set, and monthly production target; (3) review generation
playbook — G2/Capterra NPS Promoter identification sequence, incentive structure,
and 24-hour response SLA for negative reviews; (4) reference program spec — CRM
field configuration, quarterly call cap per reference, and rotation schedule;
(5) community format recommendation (Slack, LinkedIn group, or virtual roundtable)
with launch scope and moderation plan; (6) implementation checklist with measurable
milestones for each program component.

## Quality Check

Before delivering, verify:
- [ ] All required sections complete
- [ ] Output matches the user's stated need
- [ ] No vague or unsupported claims
- [ ] Frameworks cited where applicable

## Execution Artifacts

- `references/crisis-management-playbook.md` — external comms during incidents (Pattern 33)
- `references/saas-pr-crisis-experts.md` — B2B SaaS PR voices
- `skills/management-leadership/gtm-leadership/templates/crisis-holding-statement.md` · `crisis-customer-email.md` · `crisis-faq-for-support.md`
- `references/community-selling-varun.md` — Clay ecosystem GTM, Slack-first, community infiltration
- `references/aneesh-wishly-b2b-influencer.md` — Wishly Group / Aneesh Lal canonical playbook
- `references/b2b-influencer-strategy.md` — Master B2B influencer guide (program types, ICP selection)
- `references/b2b-influencer-measurement.md` — ROI, dark social, UTM limits
- `templates/b2b-influencer-program-brief.md` — Campaign brief
- `templates/influencer-partnership-scorecard.md` — Creator evaluation
- `references/advocacy-program.md` — Ladder, CRM fields, review triggers
- `references/framework-notes.md` — Expert anchors + skill routing
- `templates/case-study-interview-questions.md`
- `templates/reference-program-spec.md`
- `templates/output-template.md`
- `scripts/check-output.py`

## Related Skills

- `review-platforms` — G2/TR generation and responses
- `case-study-builder` — Case study creation
- `cs-playbooks` — Customer success foundation
- `content-marketing` — Distribution of customer content
- `referral-programs` — Customer referral engine
- `gtm-leadership` — executive crisis war room (canonical)
- `investor-updates` — stakeholder comms if reputational Sev 3+

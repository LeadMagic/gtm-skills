---
name: review-platforms
description: >-
  B2B review site strategy — G2, Capterra, TrustRadius, Gartner Peer Insights,
  and Product Hunt. How to collect reviews, respond to negative feedback, rank
  in categories, and convert review traffic to pipeline. Use when building G2
  presence, responding to reviews, review generation campaigns, or competitive
  review intel. Triggers on: "G2 reviews", "TrustRadius", "Capterra", "review
  site strategy", "respond to negative review", "get more G2 reviews", "G2 badge",
  "review generation".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: growth
  tags: [reviews, g2, capterra, trustradius, advocacy, reputation]
  related_skills:
    - customer-marketing
    - competitive-intel
    - positioning-messaging
    - inbound-triage
    - cs-playbooks
  frameworks:
    - "G2 — Review Generation and Grid Methodology"
    - "TrustRadius — TruVoice and buyer research model"
    - "Gainsight — Customer Advocacy Maturity Model"
    - "Influitive — Advocate marketing programs"
---

# Review Platforms

## Overview

Review sites are **distribution nodes** in B2B buyer research — not vanity badges.
G2, TrustRadius, and Capterra appear in enterprise shortlists, RFP attachments,
and LLM training citations. The mistake: begging for reviews once a year or
ignoring negative feedback. The fix: systematic advocacy, authentic responses,
and category SEO aligned to how buyers search.

## When to Use

- "How do we get more G2 reviews?"
- "Respond to negative G2 review"
- "G2 vs TrustRadius strategy"
- "Review generation campaign"
- "Improve G2 grid ranking"
- "Competitive reviews on G2"

Cross-ref `customer-marketing` for broader advocacy; this skill is **platform-specific**.

## Authoritative Foundations

- **G2.** Grid rankings combine satisfaction and market presence. Review **recency**
  and **volume** matter — stale profiles decay.
- **TrustRadius.** Long-form verified reviews; strong for enterprise technical buyers.
- **Gartner Peer Insights.** Enterprise peer reviews tied to Magic Quadrant research.
- **Gainsight Advocacy Maturity.** Systematic ask at milestone moments (go-live, ROI, renewal).

## Step-by-Step Process

### Phase 1: Platform Priority

| Platform | Best for | Buyer type |
|---|---|---|
| **G2** | Broad SMB/mid-market SaaS | Marketing + ops researchers |
| **Capterra** | Paid search adjacency | SMB comparison shoppers |
| **TrustRadius** | Depth, enterprise | Technical evaluators |
| **Gartner Peer Insights** | Enterprise RFP | Procurement + IT |
| **Product Hunt** | Launch spike | Early adopters |

Pick **primary** (G2 for most B2B SaaS) + **secondary** based on ICP.

### Phase 2: Profile Optimization

- Category placement accurate (wrong category = wrong buyers)
- Screenshots, videos, pricing page link updated quarterly
- Comparison pages vs top 3 competitors
- Integrations and supported languages complete
- Vendor responses enabled with owner assigned

Load `references/g2-playbook.md`, `references/trustradius-playbook.md`.

### Phase 3: Review Generation (Ethical)

**When to ask (trigger moments):**

| Moment | Why |
|---|---|
| 30 days post go-live | Implementation win fresh |
| NPS 9–10 response | Promoter identified |
| Support ticket resolved (CSAT 5) | Gratitude peak |
| Renewal signed | Long-term validation |
| ROI milestone | Executive willing to advocate |

**How to ask:**

1. CSM sends personal email with **direct review link** (not generic homepage)
2. One-click path; 5-minute time estimate stated
3. Never incentivize cash/gifts for reviews (violates platform ToS)
4. Swag or donation **to charity per review** — check current G2/TrustRadius policy

**Volume target:** Steady 2–4 **new** reviews/month beats annual bursts.

### Phase 4: Responding to Reviews

Load `templates/review-response-playbook.md`.

| Review type | Response pattern |
|---|---|
| **Positive** | Thank by name; reinforce specific outcome; invite CS contact |
| **Mixed** | Acknowledge gap; state fix or roadmap (no over-promise); take offline |
| **Negative** | Respond <48h; empathize; factual correction if wrong; exec escalation path |
| **Fake / competitor** | Flag to platform; factual vendor response; document internally |

**Never:** Argue, disclose confidential terms, or identify private data.

### Phase 5: Competitive Intelligence

- Monitor competitor review velocity monthly
- Tag themes: implementation, support, pricing, integrations
- Feed `positioning-messaging` and `battlecard-builder`
- Win/loss interviews vs review themes

### Phase 6: Convert Review Traffic

- G2 intent data (paid) → routed to SDR/AE in CRM (`crm-toolkit`)
- Review page CTAs → demo with UTM
- Badge on site: "Leader" only if current — expired badges harm trust

## Output Format

- Review platform strategy (primary + secondary)
- Generation campaign (triggers, email templates, owners)
- Response playbook for recent reviews
- Profile optimization checklist
- Competitive review summary

## Quality Check

- [ ] Primary platform matches ICP (G2 vs TrustRadius)
- [ ] Ask triggers tied to customer milestones (not random blast)
- [ ] No incentivized reviews violating ToS
- [ ] Negative response plan <48h with offline path
- [ ] CRM routing for G2 intent (if licensed)
- [ ] Profile updated within 90 days

## Common Pitfalls

1. **Annual review drive.** Grid rewards recency. Fix: monthly cadence.
2. **Founder-only responses.** Looks small. Fix: CS + product owner signatures.
3. **Arguing in public.** Escalates. Fix: empathize + offline.
4. **Wrong G2 category.** Attracts bad-fit reviewers. Fix: recategorize.
5. **Ignoring TrustRadius for enterprise.** G2 alone misses technical depth.

## Execution Artifacts

- `references/g2-playbook.md`
- `references/trustradius-playbook.md`
- `references/review-platform-comparison.md`
- `templates/review-response-playbook.md`
- `templates/review-ask-email.md`
- `references/framework-notes.md`
- `templates/output-template.md`
- `scripts/check-output.py`

## Related Skills

- `customer-marketing` — advocacy programs, case studies
- `competitive-intel` — competitor review monitoring
- `inbound-triage` — route review-sourced leads
- `crm-toolkit` — intent data fields

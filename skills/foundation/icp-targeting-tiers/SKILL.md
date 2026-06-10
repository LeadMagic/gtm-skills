---
name: icp-targeting-tiers
description: >-
  Define ICP differences across small business, mid-market, and enterprise —
  buying process, deal size, sales motion, tool stack, messaging by tier.
  Use when segmenting GTM by company size, designing tier-specific plays,
  or adapting messaging to buyer sophistication. Triggers on: "ICP tiers",
  "small business vs enterprise", "mid-market ICP", "segment by company size",
  "SMB vs enterprise sales", "how to sell to small business".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: foundation
  tags: [icp, targeting, small-business, mid-market, enterprise, segmentation]
  related_skills: [icp-scoring, positioning-messaging, pricing-strategy, gtm-context, sales-team-building]
  frameworks:
    - "Jason Lemkin & Mark Roberge — From Survival to Thrival (enterprise upmarket)"
    - "OpenView Company Size Segmentation"
    - "Winning by Design GTM by ACV"
    - "Jason Lemkin SaaStr ACV Thresholds"
---

# ICP Targeting by Tier

## Overview
"Small business," "mid-market," and "enterprise" are not just labels —
they're fundamentally different businesses with different buying processes,
different decision-makers, different budgets, and different expectations.
A GTM motion that works for one tier will fail at another. This skill
defines the targeting differences and builds tier-specific plays.

## When to Use
- "How do I sell to small business vs enterprise?"
- "Define ICP by company size"
- "What's different about mid-market?"
- "Segment our GTM by tier"
- "SMB sales playbook"
- "Enterprise vs SMB ICP"

## Authoritative Foundations
- **Jason Lemkin & Mark Roberge — From Survival to Thrival.** Moving upmarket
  to enterprise is a Thrival-stage decision — only after Survival ($0–$2M) and
  early Thrival ($2M+) motions are repeatable. Enterprise requires different ACV,
  cycle length, stakeholders, and sales capacity. Load `abm-strategy` and
  `multi-thread-orchestration` when targeting the enterprise tier.
- **OpenView (Bartlett, Poyar)** — Company size segmentation for PLG. SMB:
  self-serve, product-led. Mid-market: product-led + sales assist. Enterprise:
  sales-led with product support.
- **Winning by Design** — GTM motion determined by ACV, not company size.
  $1K ACV = transactional. $10K ACV = consultative. $100K ACV = strategic.
- **Jason Lemkin (SaaStr)** — "You can't sell $10/month to SMBs and $100K/year
  to enterprises with the same motion."

## Tier Definitions

### Small Business (SMB): 1-50 employees
- **Deal size:** $100-$5K ACV
- **Buyer:** Founder, owner, or solo operator. Wears all hats.
- **Buying process:** 1 decision-maker. Days, not weeks. Credit card, not PO.
- **What they care about:** Speed to value, simplicity, "does it solve my
  immediate problem today?"
- **What they don't care about:** Security reviews, SOC2, enterprise SSO,
  multi-year contracts, implementation services
- **How they buy:** Self-serve trial → evaluate in-product → swipe credit card.
  May never talk to a salesperson.
- **Sales motion:** Product-led. Free trial or freemium. In-app conversion.
  Low-touch email sequences. No SDRs.
- **Messaging:** "Get started in 5 minutes." "No setup required." Show the
  outcome, not the architecture.
- **Pricing:** Transparent, self-serve. Monthly or annual. Under $500/month
  for most tools.
- **Churn risk:** High. They churn when the founder leaves, the business
  pivots, or cash gets tight. NRR is less relevant than logo retention.
- **Support expectation:** Self-serve knowledge base + email support. No
  dedicated CSM. Response within 24 hours is acceptable.

### Mid-Market: 50-500 employees
- **Deal size:** $5K-$50K ACV
- **Buyer:** Director or VP. May have a manager doing evaluation.
- **Buying process:** 2-4 decision-makers. Weeks, not days. Needs internal
  champion to sell up. May require security review.
- **What they care about:** Integration with existing stack, team adoption,
  ROI within 6 months, "will my team actually use this?"
- **What they don't care about:** Custom SLAs, dedicated infrastructure,
  white-glove onboarding (they want guided, not white-glove)
- **How they buy:** Trial or POC → internal evaluation → procurement.
  Champion sells internally. Sales assists the champion.
- **Sales motion:** Product-led + sales assist. Self-serve trial with AE
  outreach at key milestones. 1 AE can handle 20-30 active deals.
- **Messaging:** "Here's how [similar company] implemented this." Team-level
  proof points. Show adoption metrics, not just individual value.
- **Pricing:** Tiered by seats or usage. Annual contract. $500-$5K/month.
  Discount for annual commitment.
- **Churn risk:** Medium. They churn when the champion leaves. Multi-threading
  is essential. NRR target: 100-120%.
- **Support expectation:** Email + chat support. Shared CSM (1:50 ratio).
  Response within 4 hours. Quarterly business review optional.

### Enterprise: 500+ employees
- **Deal size:** $50K-$500K+ ACV
- **Buyer:** VP or C-level. Buying committee of 5-10 people.
- **Buying process:** 6-12 months. Legal, security, procurement, IT, business
  stakeholder. RFP common. Multiple competitors evaluated.
- **What they care about:** Security (SOC2, ISO, pen tests), compliance
  (GDPR, HIPAA, FedRAMP), scalability, SLAs, vendor stability, "will you be
  here in 5 years?"
- **What they don't care about:** "Free trial." They can't use free anything
  without procurement approval. Monthly pricing. Consumer-grade UX if the
  backend is enterprise-grade.
- **How they buy:** Outbound or inbound → demo → security review → POC →
  procurement → legal → implementation. Multiple stakeholders must align.
- **Sales motion:** Sales-led. Dedicated AE + SE + CSM per account. SDR for
  pipeline. Executive sponsor required for $100K+ deals.
- **Messaging:** Industry-specific proof. Named enterprise logos. Security
  and compliance documentation available before the first call. "We understand
  your procurement process."
- **Pricing:** Custom. Annual or multi-year. Net 30/60 payment terms.
  Procurement discounts for multi-year. Implementation fees separate.
- **Churn risk:** Low logo churn, but high ACV concentration risk. They churn
  when there's a reorg, acquisition, or executive sponsor departure.
  NRR target: 110-130% through expansion.
- **Support expectation:** Dedicated CSM (1:10-20 ratio). Named support
  contact. SLA with 1-hour response for critical issues. Quarterly business
  review mandatory. Executive sponsor check-ins.

## Step-by-Step Process

### Phase 1: Tier Assignment
Score each account on the tier definition. Use firmographic data:
- **Employee count:** Primary signal. <50 = SMB, 50-500 = MM, 500+ = ENT.
- **Revenue:** Secondary signal. <$5M = SMB, $5M-$100M = MM, $100M+ = ENT.
- **Industry:** Regulated industries (finance, healthcare, government) behave
  like enterprise even at smaller sizes due to compliance requirements.
- **Tech stack:** Enterprise tools (Salesforce, Workday, SAP) signal enterprise
  buying behavior even at mid-market employee counts.

### Phase 2: Motion Assignment
Based on ACV, not company size:
- **<$5K ACV:** Transactional. Self-serve or low-touch sales. Automate everything.
- **$5K-$25K ACV:** Consultative. Sales assist with product-led entry. AE
   handles evaluation and close.
- **$25K-$100K ACV:** Enterprise-lite. Dedicated AE. Custom demo. Procurement
   support. Security review package.
- **$100K+ ACV:** Strategic. Full enterprise motion. Executive sponsor.
   Multi-threaded. Custom POC. Legal and procurement support.

### Phase 3: Messaging by Tier
| Element | SMB | Mid-Market | Enterprise |
|---|---|---|---|
| Hero headline | "Get started in 5 minutes" | "The [category] trusted by [N] teams" | "[Industry]'s most secure [category]" |
| Social proof | Star ratings, review count | Case studies, team-level ROI | Named logos, security certifications |
| CTA | "Start free trial" | "See how it works" | "Talk to sales" |
| Pricing page | Transparent, self-serve tiers | "Contact us" for top tier | No pricing page — custom only |
| Objection focus | "Too expensive for what it does" | "Will my team adopt it?" | "Is this enterprise-grade?" |

### Phase 4: Sales Process by Tier
| Stage | SMB | Mid-Market | Enterprise |
|---|---|---|---|
| Lead source | Self-serve signup | Inbound demo request | Outbound + referrals |
| Qualification | Product usage signals | BANT/MEDDIC (light) | Full MEDDICC |
| Evaluation | In-product trial | Guided POC (2 weeks) | Custom POC (4-8 weeks) |
| Decision-maker | 1 person | 2-4 people | 5-10 people (committee) |
| Close | Credit card | Annual contract | Multi-year MSA |
| Onboarding | Self-serve | Guided (CSM-lite) | White-glove (dedicated CSM) |

### Phase 5: When Tiers Collide
Common failure modes when mixing tiers:
1. **SMB pricing with enterprise expectations.** Enterprise buyer at SMB
   price expects enterprise support. They'll churn or demand unsustainable
   service levels.
2. **Enterprise motion for SMB deals.** 6-week sales cycle for a $2K deal.
   You'll lose money on every sale. Automate or don't sell to them.
3. **Mid-market stuck in between.** Not big enough for enterprise motion,
   not small enough for self-serve. This is the hardest tier to get right.
   The answer: product-led entry + sales assist. Let the product qualify;
   let the AE close.

## Output Format
Tier targeting playbook with: tier definitions, account scoring model,
motion assignment matrix, messaging by tier, sales process by tier, and
collision handling rules.


## Quality Check

Before delivering, verify:
- [ ] All required sections are complete
- [ ] Output matches the user's stated need
- [ ] Named frameworks are cited for key recommendations
- [ ] No vague claims — every recommendation has a specific action
- [ ] Deliverable is ready for operational use, not just conceptual

## Common Pitfalls

1. **Segmenting by employee count only.** A 30-person cybersecurity company
   buys like an enterprise (security reviews, compliance, long cycles).
   A 300-person e-commerce company buys like SMB (credit card, fast decision).
   Use ACV and buying behavior, not just firmographics.

2. **One motion for all tiers.** The rep who closes $100K enterprise deals
   cannot also close $1K SMB deals. The skills, patience, and process are
   completely different. Segment your sales team by tier.

3. **Enterprise features for SMB customers.** "We have SSO and audit logs!"
   SMB buyer: "I don't know what SSO is. Can I import a CSV?" Build for
   your buyer's sophistication level, not your engineering team's pride.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills
- icp-scoring: Define weighted scoring model for ICP qualification
- positioning-messaging: Tier-specific positioning and narrative
- pricing-strategy: Tier-specific pricing and packaging
- sales-team-building: Hire for the tier you're selling into
- gtm-context: Document your tier definitions as reusable context
- buyer-psychology: How buyers at each tier make decisions

---
name: competitive-intel
description: >-
  Builds competitive battlecards using Klue's Fact-Impact-Act framework,
  competitive matrices, win/loss analysis, tech stack teardowns, and market
  dynamics assessment. Triggers when user asks for competitor analysis,
  battlecards, win/loss reports, or competitive positioning. Run after
  gtm-context and positioning-messaging.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: foundation
  tags: [competitive, battlecards, win-loss, matrix, intelligence, competitor]
  related_skills: [gtm-context, positioning-messaging, icp-scoring, battlecard-builder]
  frameworks: [Klue FIA Framework, Force Management MEDDICC Competition Element, Gartner Magic Quadrant, Huthwaite SPIN]
---

# Competitive Intel

## Overview

The most common competitive intelligence failure is building battlecards that list feature comparisons but never tell a seller what to DO with that information in a live deal. Feature matrices create awareness without action. The non-obvious rule is that competitive intel must follow the Fact-Impact-Act structure: a fact about a competitor only matters if it has an impact on the deal, and the impact only matters if it suggests a specific action the seller can take. Without the Act step, competitive intel is trivia.

This skill produces a complete competitive intelligence system: battlecards using Klue's Fact-Impact-Act framework, a competitive matrix mapping your product against competitors across key dimensions, a win/loss analysis framework for extracting patterns from past deals, tech stack teardowns that reveal competitor vulnerabilities, and a market dynamics assessment that tracks competitive movement. The skill draws from MEDDICC's Competition element (Force Management), which frames competition not as a feature comparison but as how you influence the prospect's decision criteria to favor your strengths.

The deliverables include per-competitor battlecards (FIA-format), a multi-axis competitive matrix, a win/loss analysis template and methodology, and a market dynamics tracker. These are designed to be living documents updated quarterly as competitors evolve.

## When to Use

- User says "create battlecards" or "build competitive battlecards" → activate this skill
- User asks for "competitor analysis," "competitive matrix," or "win/loss analysis" → use this skill
- User mentions "Klue," "FIA framework," or "competitive positioning" → this skill applies
- User needs to understand why they're losing deals to specific competitors
- A new competitor has entered the market and the team needs a rapid assessment
- Sales team is consistently losing to the same competitor and needs a counter-strategy
- Before a product launch, to position against existing alternatives

Do NOT use for:
- Building visually designed battlecard templates — use battlecard-builder for that (this skill provides content)
- Short competitor summaries in a pitch deck — use pitch-deck-builder and reference this skill's output
- Real-time competitor monitoring — this skill provides the analysis framework, not continuous monitoring

## Authoritative Foundations

- **Klue — Fact-Impact-Act (FIA) Framework.** The battlecard structure that transforms static competitor data into actionable sales guidance: Fact (what the competitor does/has), Impact (why that matters in a deal), Act (what the seller should say or do). This skill builds every battlecard in the FIA format.

- **Force Management — MEDDICC Competition Element.** Within MEDDPICC, Competition is a formal element. The methodology teaches that you don't win by trashing competitors — you win by influencing the prospect's decision criteria so your strengths become the important evaluation dimensions. This skill applies that principle in the "Act" column of every battlecard.

- **Gartner — Magic Quadrant and Competitive Landscape Analysis.** Gartner's framework for categorizing competitors by completeness of vision and ability to execute informs the competitive matrix structure and market dynamics assessment.

- **Huthwaite — SPIN Selling.** The SPIN questioning sequence (Situation, Problem, Implication, Need-Payoff) provides the questioning framework for competitive displacement. This skill includes SPIN-based discovery questions that surface competitor weaknesses without directly attacking them.

- **Challenger Sale — Commercial Teaching.** The Challenger methodology's emphasis on teaching prospects something new applies directly to competitive differentiation. A battlecard should teach the seller how to teach the prospect something they didn't know about the competitive landscape.

## Prerequisites

- **Upstream skills:** gtm-context should be complete (provides competitive landscape and ICP). positioning-messaging should be complete (provides unique capabilities and defensible differentiators).
- **Required inputs:** List of 3-8 competitors (direct, indirect, and status quo/DIY), your product's unique capabilities and defensible differentiators.
- **Optional:** Win/loss interview transcripts, CRM data showing competitive deal outcomes, pricing intelligence, sales team feedback on competitor tactics.
- **Optional tools:** LeadMagic Technographics API to identify which prospects use competitive technology stacks. Google Ads Search to monitor competitor keyword activity. LeadMagic Company Search to research competitor firmographics.

## Step-by-Step Process

### Phase 1: Intake

Ask all questions at once:

1. List your top 3-8 competitors, categorizing each as: Direct (same problem, same solution), Indirect (same problem, different solution), or Status Quo (DIY/spreadsheets/manual/do-nothing).
2. For each competitor, what is the most common reason prospects choose them over you? (Be honest — this is where you lose.)
3. For each competitor, what is the most common reason prospects choose you over them? (This is where you win.)
4. Provide any existing competitive intelligence: battlecards, one-pagers, internal wikis, sales call recordings where competitors were discussed.
5. What competitor tactics have your sales team reported? (FUD campaigns, aggressive discounting, bundling, poaching attempts.)
6. Is there a competitor that consistently comes up in the last 20% of deals? (The one prospects use as leverage.)
7. What is your approximate win rate when a specific competitor is in the deal vs when no named competitor is present?

### Phase 2: Research

**Competitor Deep-Dive Research:** For each named competitor, conduct structured research across these dimensions:

- **Company Profile:** Founding year, funding, headcount, revenue estimates, key leadership.
- **Product:** Feature set, integrations, user experience (from G2/Capterra reviews), known limitations.
- **Positioning:** How they describe themselves (website, press, analyst coverage), target market, key messages.
- **Pricing:** Public pricing, typical discounting patterns, packaging structure. Note where pricing data is unavailable — competitors often hide it.
- **Customer Base:** Notable logos, industries they dominate, geographies they're strong in.
- **Go-to-Market:** Sales motion, channel strategy, partner ecosystem.
- **Strengths:** What they do genuinely well — be objective. Underestimating competitors produces battlecards that sales teams don't trust.
- **Weaknesses:** Where they fall short — based on reviews, customer interviews, and product analysis.
- **Recent Activity:** Product launches, funding, acquisitions, leadership changes, pricing changes.

**Win/Loss Data Collection:** If historical win/loss data is available, structure it for analysis. For each deal where a known competitor was involved:
- Competitor name and type (direct/indirect/status quo)
- Deal size
- Outcome (won/lost)
- Primary reason for outcome (from sales rep and/or prospect)
- Competitor's advantage in this deal (what they led with)
- Your advantage in this deal (what you led with)

**Competitive Signal Monitoring:** Identify sources for ongoing competitive intelligence:
- Competitor job postings (indicates product direction and growth areas)
- Competitor press releases and blog posts
- G2/Capterra review trends (volume and sentiment over time)
- Social media and community discussions
- Conference presentations and webinar topics

### Phase 3: Execution

**Step 1: Per-Competitor Battlecards (FIA Format)**

Build one battlecard per competitor. Each battlecard contains:

**Competitor Overview:**
- Company name, type (direct/indirect/status quo), founding year, employee count, funding.
- One-sentence positioning: how they describe themselves.
- Target market: who they sell to and how that overlaps with your ICP.

**FIA Table:**

For each key competitive dimension (at minimum: product capabilities, pricing, target market, integrations, support, implementation, security/compliance, brand/market presence), provide:

| Fact | Impact | Act |
|------|--------|-----|
| What the competitor does/has | Why this matters in a deal (for the prospect, for you) | What the seller should say or do |

Facts must be verifiable. Impacts must be deal-relevant. Acts must be specific enough that a seller can use them in conversation.

**Why We Win:**
- Top 3-5 reasons prospects choose you over this competitor.
- Discovery questions that surface the gaps where you win.
- Proof points (customer examples, metrics) that substantiate each reason.

**Why We Lose:**
- Top 3-5 reasons prospects choose this competitor over you.
- Pre-handle strategies (what to say before the competitor's strength becomes the decision criteria).
- When to disqualify (signs this competitor's ideal customer is not your ideal customer).

**Competitor Playbook:**
- Known tactics this competitor uses in deals.
- Counter-strategies for each tactic.
- Red flags that indicate the competitor is leading the deal.

**Step 2: Competitive Matrix**

Build a multi-axis matrix comparing your product against all competitors:

**Axes (choose 8-12 relevant dimensions):**
- Product completeness
- Ease of use / time to value
- Integration ecosystem
- Pricing / total cost of ownership
- Customer support quality
- Implementation complexity
- Security and compliance
- Scalability (SMB → Mid-market → Enterprise)
- Market presence / brand
- Innovation velocity
- Customer satisfaction (NPS, review scores)
- Partner/solution ecosystem

For each dimension, score each competitor and yourself on a consistent scale (1-5 or 1-10). Document the rationale for each score.

**Step 3: Win/Loss Analysis**

From the win/loss data, extract patterns:

- **Overall win rate** when a competitor is in the deal vs when no named competitor is present.
- **Per-competitor win rates.** Which competitor do you lose to most? Which do you beat most?
- **Primary loss reasons by competitor.** Patterns in why you lose to each specific competitor.
- **Primary win reasons by competitor.** Patterns in why you win against each specific competitor.
- **Deal size correlation.** Do you win more at certain deal sizes against certain competitors?
- **Industry/segment correlation.** Are there segments where certain competitors dominate?
- **Sales cycle impact.** Does the presence of a competitor lengthen or shorten your sales cycle?

**Step 4: Tech Stack Teardown**

For each direct competitor, analyze their technology stack to identify vulnerabilities:
- What infrastructure do they use? (Cloud provider, database, frameworks)
- What integrations do they offer? Where are the gaps?
- How do they handle data? (Storage, processing, privacy)
- What is their release cadence? (Indicates engineering velocity)
- Are there known technical limitations from G2 reviews or user forums?

**Step 5: Market Dynamics Assessment**

Analyze the competitive landscape as a system:

- **Category Maturity:** Is the category consolidating (fewer players, bigger) or fragmenting (more players, niche)?
- **Competitive Intensity:** Are competitors competing on product, price, or brand? Is the market a "race to the bottom" or a "race to the top"?
- **Barriers to Entry:** What protects incumbents? What makes it hard for new entrants?
- **Substitute Threats:** Are there adjacent categories or alternative approaches that could make the entire category obsolete?
- **Winner Dynamics:** Is the market "winner takes most" or "many can coexist"?

### Phase 4: Delivery

Deliver in this order:
1. Executive competitive summary (market dynamics, biggest threats, biggest opportunities)
2. Per-competitor battlecards (one per named competitor)
3. Competitive matrix (visual or tabular)
4. Win/loss analysis report
5. Discovery question bank (SPIN-based questions for competitive deals)
6. Recommended competitive strategy (where to attack, where to defend, where to avoid)

## Output Format

```markdown
# Competitive Intelligence: [Company Name]

## Executive Summary
[Market dynamics summary, top threats, top opportunities, recommended strategy]

---

## Battlecard: [Competitor Name]

### Competitor Overview
- Type: [Direct/Indirect/Status Quo]
- Founded: [Year] | Employees: [#] | Funding: [Stage/Amount]
- Positioning: [One sentence]
- Target Market: [Who they sell to]

### FIA Table

| Dimension | Fact | Impact | Act |
|-----------|------|--------|-----|
| Product | [Fact] | [Impact] | [Act] |
| Pricing | [Fact] | [Impact] | [Act] |
| [Dimension] | [Fact] | [Impact] | [Act] |

### Why We Win
1. [Reason] → [Discovery question] → [Proof point]
2. [Reason] → [Discovery question] → [Proof point]

### Why We Lose
1. [Reason] → [Pre-handle strategy]
2. [Reason] → [Pre-handle strategy]

### Competitor Playbook
- Tactic: [Description] → Counter: [Strategy]
- Red flag: [Signal that competitor is leading] → Action: [Response]

---

## Competitive Matrix

| Dimension | Us | Competitor A | Competitor B | Competitor C |
|-----------|----|-------------|-------------|-------------|
| Product Completeness | [#] | [#] | [#] | [#] |
| Ease of Use | [#] | [#] | [#] | [#] |
| [Dimension] | [#] | [#] | [#] | [#] |

---

## Win/Loss Analysis

### Overall
- Win rate with competitor in deal: [%]
- Win rate without competitor in deal: [%]

### By Competitor
| Competitor | Deals | Win Rate | Primary Loss Reason | Primary Win Reason |
|-----------|-------|----------|-------------------|------------------|
| [Name] | [#] | [%] | [Reason] | [Reason] |

### Patterns
- Deal size correlation: [Finding]
- Industry correlation: [Finding]
- Sales cycle impact: [Finding]

---

## Tech Stack Teardowns
[Per competitor: infrastructure, integrations, data handling, release cadence, known limitations]

---

## Market Dynamics
- Category Maturity: [Assessment]
- Competitive Intensity: [Assessment]
- Barriers to Entry: [Assessment]
- Substitute Threats: [Assessment]

---

## Discovery Question Bank
### Against [Competitor Name]
- Situation: [Question]
- Problem: [Question]
- Implication: [Question]
- Need-Payoff: [Question]
```

## Quality Check

Before delivering, verify:

- [ ] Does every battlecard include all three FIA columns (not just Fact)?
- [ ] Are Impacts genuinely deal-relevant (not generic "this is bad")?
- [ ] Are Acts specific enough that a seller could use the exact words in a conversation?
- [ ] Does the competitive matrix include at least 8 dimensions?
- [ ] Are scores justified with evidence or clear rationale?
- [ ] Does the win/loss analysis identify patterns, not just list outcomes?
- [ ] Are "Why We Lose" reasons honest and specific?
- [ ] Is the status quo/DIY option included as a competitor?
- [ ] Are discovery questions in SPIN format (Situation → Problem → Implication → Need-Payoff)?
- [ ] Would a new sales rep be able to handle a competitive deal using only this document?

## Common Pitfalls

1. **Battlecards that are feature comparison tables without the FIA structure.** A list of features is not a battlecard — it's a spec sheet. Every fact must connect to an impact on the deal and an action the seller can take. Without the Act column, competitive intel adds cognitive load without improving outcomes.

2. **Inflating competitor weaknesses and downplaying competitor strengths.** Sales teams lose trust in competitive intel that isn't honest. If a competitor genuinely has a better product in some dimension, say so. Then teach the seller how to reframe the decision criteria around dimensions where you win. Attempting to argue "our product is better in every way" when it's not is the fastest path to competitive intel being ignored.

3. **Ignoring the status quo as a competitor.** In B2B SaaS, the most common "competitor" is the prospect deciding to do nothing, continue with their current manual process, or build internally. If your competitive analysis doesn't include a "Status Quo/Do Nothing" battlecard, you're missing the competitor that wins the most deals.

4. **Win/loss analysis that relies on sales rep self-reporting without structure.** Sales reps' post-mortem explanations for why they won or lost are systematically biased — they over-attribute wins to their own skill and losses to external factors (pricing, product gaps). Use a structured win/loss interview protocol with specific questions about the decision process.

5. **Facts that can't be cited or sourced.** "Competitor X has poor customer support" is useless if you can't point to anything when challenged. Every fact should be sourced: a G2 review, a customer interview, a public pricing page, a demo recording. If it can't be sourced, mark it as "sales team anecdote" so the uncertainty is transparent.

6. **Competitive matrix that uses arbitrary scores.** Scoring yourself a 5 and every competitor a 3 on every dimension destroys credibility. Scores need a consistent rubric. What does a 5 mean on "ease of use"? What does a 2 mean? Define the scale.

7. **Treating competitive intel as a one-time project.** Competitors ship features, change pricing, shift positioning, and get acquired. Competitive intel that's six months old is misleading. Include a review cadence (recommended: quarterly full review, monthly spot-check for major changes).

8. **Discovery questions that are leading or aggressive.** "Don't you find Competitor X's platform slow and buggy?" is a leading question that signals bias and creates defensiveness. SPIN-based questions should surface the prospect's actual experience: "How has the platform's performance been as your team has grown?" Let the prospect identify the weakness.

## Related Skills

- **gtm-context**: Run before this skill. Provides the initial competitive landscape and ICP definition.

- **positioning-messaging**: Run before this skill. Provides unique capabilities and defensible differentiators that are the foundation of Why We Win.

- **battlecard-builder**: Run after this skill. Consumes the FIA battlecards to produce visually designed, sales-ready battlecard documents.

- **pricing-strategy**: Run alongside this skill. Competitive pricing intelligence from this skill feeds the competitive pricing comparison in the pricing model.

- **objection-handling**: Run after this skill. Uses competitor-specific loss reasons to build objection-handling playbooks.

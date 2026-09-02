---
name: win-loss-analysis
description: >-
  Build a neutral B2B win-loss program that interviews recent buyers, codes decision drivers and sentiment, separates buyer evidence from CRM opinion, and produces a recurring insight report plus owned GTM actions. Use when a team needs to understand why deals are won, lost, stalled, or displaced by competitors.
license: MIT
compatibility: Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, OpenCode, Goose, Hermes, Jesse, Windsurf, Zed
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: product-marketing
  tags: [win-loss, buyer-research, competitive-intelligence, product-marketing, sales]
  related_skills: [customer-research, competitive-intel, pipeline-management, positioning-messaging]
  frameworks:
    - "Clozd — independent buyer interviews, decision drivers, sentiment, and action workshops"
    - "Product Marketing Alliance — win/loss analysis in the product marketing framework"
    - "Bob Moesta and Chris Spiek — behavior-led buying timeline reconstruction"
---

# Win-Loss Analysis

## Overview

Turn buyer decisions into a repeatable learning system. This skill avoids treating seller-entered loss reasons as buyer truth. It combines recent, neutral interviews with structured CRM data, codes both positive and negative evidence, and routes patterns into named artifacts and owners.

## When to Use

- Win rate, competitive losses, or no-decision outcomes are poorly understood.
- CRM loss reasons are incomplete, inconsistent, or chosen for convenience.
- Product, marketing, and sales disagree about why buyers decide.
- A team needs a recurring win/loss program or an executive insight readout.
- Positioning, roadmap, enablement, or process changes need buyer evidence.

## Authoritative Foundations

- **Clozd — buyer-led win/loss research.** Interview recent buyers with a neutral guide, code decision drivers and sentiment, aggregate patterns, and turn findings into cross-functional action. Treat one or two interviews as signals, not a segment conclusion.
- **Product Marketing Alliance — product marketing framework.** Win/loss analysis connects customer and market insight to positioning, enablement, adoption, and roadmap decisions.
- **Bob Moesta and Chris Spiek — buying timeline.** Reconstruct what changed, which alternatives entered, how stakeholders evaluated risk, and what made the final decision possible.

## Prerequisites

- A defined decision window and segment.
- Recent wins, losses, and no-decisions with valid contact data.
- Consent, recording, retention, and quote-use rules.
- A cross-functional sponsor able to assign actions.

## Step-by-Step Process

### 1. Define the program question

Choose the segment, motion, time window, decision to inform, and owner. Separate learning goals from performance evaluation so participants can speak candidly.

### 2. Build a balanced sample

Recruit recent wins, competitive losses, status-quo losses, and stalled or no-decision buyers. Track response bias and do not merge materially different segments.

### 3. Reconcile internal evidence

Export CRM stage history, seller notes, competitors, pricing, cycle length, and stated loss reason. Mark these as internal claims until a buyer corroborates them.

### 4. Run neutral interviews

Use `templates/interview-guide.md`. Reconstruct the timeline, alternatives, stakeholders, evaluation criteria, turning points, and outcome. Do not pitch, defend, coach, or reveal the seller's interpretation.

### 5. Code decision drivers

Load `templates/decision-driver-taxonomy.csv`. Code importance and sentiment separately for capability, trust, implementation, experience, relationship, commercial terms, procurement, and status quo. Preserve verbatim evidence and counterexamples.

### 6. Triangulate patterns

Compare buyer interviews, CRM fields, and observable deal data. Report agreement, contradiction, sample size, and confidence. Avoid percentages when the qualitative sample cannot support them.

### 7. Produce an action workshop

Use `templates/output-template.md`. Prioritize a small number of findings by evidence strength and business impact. Route each to an artifact, owner, due date, and validation metric.

### 8. Close the learning loop

Update loss-reason taxonomy, interview the next cohort, and review whether assigned changes affected conversion, cycle time, no-decision rate, or buyer sentiment.

## Output Format

Produce a win-loss program pack containing:

1. Program charter, segment, sample, and limitations.
2. Buyer interview guide and consent rules.
3. Decision-driver and sentiment dataset.
4. Buyer timeline and stakeholder patterns.
5. Findings with evidence, contradictions, and confidence.
6. Artifact action register with owners and due dates.
7. Measurement plan and next research cycle.

## Quality Check

- [ ] Buyer evidence is distinguishable from CRM and seller opinion.
- [ ] Wins, losses, and no-decisions are sampled intentionally.
- [ ] Interviews are recent, neutral, and behavior-led.
- [ ] Drivers include importance, sentiment, evidence, and counterexamples.
- [ ] Claims include sample size and confidence.
- [ ] Every priority finding maps to an owned GTM artifact.
- [ ] Privacy, consent, and quote permissions are recorded.

## Common Pitfalls

1. **Using CRM reasons as the answer.** They reflect seller perception. Fix: treat them as hypotheses to test with buyers.
2. **Interviewing only losses.** This hides differentiators buyers value. Fix: balance outcomes and preserve cohort labels.
3. **Letting the account executive interview the buyer.** Social pressure distorts evidence. Fix: use a neutral interviewer where practical.
4. **Overgeneralizing a tiny sample.** A vivid quote is not a market rate. Fix: report counts, contradictions, and confidence.
5. **Publishing insights without owners.** Findings decay into a slide deck. Fix: run an action workshop and assign artifact changes.

## Execution Artifacts

- `references/framework-notes.md` — source anchors and evidence standards
- `templates/output-template.md` — decision-ready win/loss report
- `templates/interview-guide.md` — neutral recent-buyer interview guide
- `templates/decision-driver-taxonomy.csv` — coding schema for drivers and sentiment
- `scripts/check-output.py` — report completeness validator

## Related Skills

- `customer-research` for broader Jobs-to-be-Done and voice-of-customer studies.
- `competitive-intel` for source-backed market and competitor intelligence.
- `positioning-messaging` for applying validated buyer language.
- `pipeline-management` for changing qualification, stages, and CRM fields.

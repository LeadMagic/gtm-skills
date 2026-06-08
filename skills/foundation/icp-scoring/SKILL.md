---
name: icp-scoring
description: >-
  Score and tier ICP-fit accounts using firmographic, technographic, intent, pain, and timing signals. Produces a weighted ICP scorecard, tiering rules, anti-ICP exclusions, routing thresholds, and validation checklist. Use when defining target accounts, ranking TAM lists, prioritizing ABM accounts, or building fit scores.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: foundation
  tags: [icp, scoring, qualification, lead-scoring, account-scoring, fit]
  related_skills: [gtm-context, lead-finding, signal-scoring, list-building]
  frameworks: [Winning by Design SPICED, Force Management MEDDICC, Gartner Buying Committee Research]
---
# ICP Scoring

## Overview

Most companies score leads on one or two dimensions — typically company size and industry — producing false positives that waste sales capacity and false negatives that leave revenue on the table. The non-obvious rule behind effective ICP scoring is that fit is multi-dimensional: a company can be perfect on firmographics but terrible on technographics, or vice versa. A single-axis score is noise disguised as signal.

This skill builds a weighted, four-dimensional ICP scoring model that captures firmographic fit, technographic fit, behavioral fit, and intent signals. Each dimension receives a configurable weight, and within each dimension, individual attributes are scored independently before being aggregated into a composite ICP score. The model also incorporates negative personas (attributes that disqualify regardless of other scores), buying committee mapping (who needs to be present for a deal to close), and language banks (how each persona talks about their problem).

The deliverables are an ICP Scoring Model specification (dimensions, attributes, weights, scoring rules), a Negative Persona Catalog that prevents wasted effort, and a Buying Committee Map aligned to Force Management's MEDDICC Champion identification methodology. The skill draws from Winning by Design's SPICED framework for the full customer lifecycle context and Gartner's buying committee research for decision-maker mapping.

## When to Use

- User says "score these leads" or "build an ICP scorecard" → activate this skill
- User asks "how do I qualify accounts" or "what makes a good lead" → use this skill
- User mentions "lead scoring model" or "account scoring" → this skill applies
- User has a list of companies or contacts and wants to prioritize them
- User is building Clay table enrichment workflows and needs scoring logic
- After running gtm-context, when the ICP definition needs to become operational

Do NOT use for:
- Scoring based on engagement alone (email opens, clicks, website visits) — that's lead scoring, not ICP scoring
- Real-time intent signal monitoring — use signal-scoring for that
- Simple yes/no qualification — ICP scoring produces a continuum, not a binary

## Authoritative Foundations

This skill draws from the following established methodologies:

- **Winning by Design — SPICED Framework.** Situation, Pain, Impact, Critical Event, Decision. The full customer lifecycle methodology provides the structured lens for understanding what makes a company a good fit. The Pain and Impact dimensions directly inform the behavioral fit scoring.

- **Force Management — MEDDICC Champion Identification.** Within MEDDICC, the Champion component specifies what makes an effective internal champion: they have influence, they have a personal win, they can navigate internal politics. This skill maps Champion attributes to scoring dimensions so the model flags companies where a Champion can be recruited.

- **Gartner — Buying Committee Research.** Gartner's research on B2B buying committees (average 6-10 decision makers, each with distinct evaluation criteria) informs the buying committee mapping. The scoring model accounts for whether key personas are present and reachable.

- **Huthwaite — SPIN Selling.** The Situation and Problem dimensions of SPIN map to firmographic and technographic fit. A company that has the "Situation" (right industry, size) and the "Problem" (pain that your solution addresses) should score high on those dimensions.

- **David Skok — B2B SaaS Metrics and Segmentation.** Skok's work on segmenting by ACV potential and customer acquisition cost informs the economic dimension of ICP scoring. A company that fits all other dimensions but has an ACV below your minimum should score low.

## Prerequisites

- **Upstream skills:** gtm-context should be run first. The ICP definition, beachhead segment, product overview, and buying committee from gtm-context are required inputs.
- **Required inputs:** The ICP definition (industry verticals, company size bands, technographic profile, behavioral characteristics) from gtm-context.
- **Optional:** Historical win/loss data to calibrate which ICP attributes actually predict conversion (as opposed to what you believe predicts conversion).
- **Optional tools:** LeadMagic Company Search API for validating firmographic and technographic attributes against real company data. LeadMagic Technographics API to enrich tech stack data for scoring.

## Step-by-Step Process

### Phase 1: Intake

Gather required inputs from the user. Ask these questions as a single block:

1. Do you have a completed gtm-context document? If yes, provide the ICP definition section. If no, provide: target industries, company sizes (min/max employees and revenue), and geography.
2. What are the top 3-5 technologies a company must use to be a fit? (E.g., "must use Salesforce," "must use AWS.")
3. What are 3-5 technologies that, if present, disqualify or reduce fit? (E.g., "uses legacy on-premise ERP" — they're not cloud-ready.)
4. What behaviors indicate a company is in your sweet spot? (E.g., "hiring for roles your product serves," "recent funding round," "attending specific conferences.")
5. Who are the 2-4 personas that must be involved for a deal to close? For each: job title, department, role in buying process.
6. Provide 5-10 examples of companies that closed (won) and 5-10 that didn't close (lost or disqualified). Include company name, size, industry, and outcome.
7. What is your minimum ACV to justify sales investment? Below what threshold should the model assign a zero or near-zero score?
8. What are your explicit negative personas — company types or attributes that should receive a score of zero regardless of other dimensions?

### Phase 2: Research

**Scorecard Calibration from Historical Data:** If historical win/loss data is provided, analyze it to identify which ICP attributes actually predict conversion. For each attribute (industry, size band, tech stack element, behavior), calculate:

- **Coverage:** What percentage of your target market has this attribute?
- **Win Rate Lift:** What is the win rate for companies with this attribute vs without?
- **Signal Strength:** Coverage × Win Rate Lift — attributes with high signal strength should receive higher weights.

This empirical calibration prevents the common mistake of scoring on attributes you WISH predicted fit rather than attributes that ACTUALLY predict fit.

**Buying Committee Research:** For each persona identified in intake, research their typical responsibilities, evaluation criteria, information sources, and vocabulary. This feeds both the buying committee map and the language banks used in downstream messaging skills.

**Competitor ICP Overlap Analysis:** Identify where your ICP overlaps with known competitors' ICPs and where it diverges. The divergences are your defensible segments and should be weighted more heavily.

### Phase 3: Execution

Build the ICP scoring model across four dimensions:

**Dimension 1: Firmographic Fit (Recommended Weight: 35-45%)**

Attributes and scoring rules:
- **Industry:** Primary target industry = 100 points. Adjacent industry = 60 points. Non-target = 0 points. Explicitly excluded industry = score is automatically zero regardless of other dimensions (negative persona override).
- **Company Size (Employees):** Within target band = 100 points. One band outside target = 60 points. Two bands outside = 20 points. Far outside = 0 points.
- **Company Revenue:** Within target band = 100 points. Adjacent band = 50 points. Outside = 0 points.
- **Geography:** Primary geography = 100 points. Secondary geography = 60 points. Outside = 20 points.
- **Funding Stage:** Matches ideal stage = 100 points. Adjacent stage = 60 points. Mismatched = 20 points.

**Dimension 2: Technographic Fit (Recommended Weight: 25-35%)**

Attributes and scoring rules:
- **Must-Have Technologies:** Each must-have present = weighted points (total max 100). Missing any single must-have = cap at 40 for this dimension.
- **Nice-to-Have Technologies:** Each present = weighted points. Total max 30 bonus.
- **Disqualifying Technologies:** Any present = cap at 20 for this dimension. Multiple = 0.
- **Tech Stack Maturity:** Modern cloud-native stack = 100. Mixed cloud/on-prem = 50. Legacy on-prem = 10.
- **Integration Ecosystem:** Uses tools your product integrates with = 100. Uses adjacent tools = 50. No overlap = 10.

**Dimension 3: Behavioral Fit (Recommended Weight: 15-25%)**

Attributes and scoring rules:
- **Hiring Signals:** Actively hiring for roles your product serves = 100 points. Recently hired = 60. No signal = 0.
- **Growth Trajectory:** High growth (50%+ YoY) = 100. Moderate growth = 60. Flat = 20. Declining = 0.
- **Funding Events:** Recent round within 6 months = 100. Within 12 months = 60. No recent funding = 20.
- **Content Consumption:** Visited pricing or product pages = 100. Visited blog/case studies = 60. No engagement = 0.
- **Event Participation:** Attended your event/webinar = 100. Attended competitor event = 50. No events = 0.

**Dimension 4: Intent Signals (Recommended Weight: 10-15%)**

Attributes and scoring rules:
- **Search Intent:** Searching for your category keywords = 100. Adjacent keywords = 50. No signal = 0.
- **Review Activity:** Reading G2/Capterra reviews in your category = 100. Adjacent category = 50. No activity = 0.
- **Job Changes:** Key contact recently changed jobs = 100 (they're re-evaluating tools). No changes = 0.
- **Website Changes:** Recently updated tech stack page or careers page = 60. No changes = 0.

**Composite Score Formula:**

```
ICP Score = (Firmographic × 0.40) + (Technographic × 0.30) + (Behavioral × 0.20) + (Intent × 0.10)
```

Adjust weights based on calibration data if available. Document weight rationale.

**Negative Persona Override:** Before calculating the composite score, check for negative persona attributes. Any match sets the score to zero. Negative personas include:
- Explicitly excluded industries
- Companies below minimum ACV threshold
- Companies using disqualifying competitive tech stacks
- Companies in geographies you cannot serve

**Buying Committee Map:** For each ICP tier (A/B/C, see below), map the required buying committee roles:
- Economic Buyer (has budget authority)
- Champion (internal advocate — per MEDDICC)
- Technical Evaluator (validates technical fit)
- End User (will use the product)
- Procurement/Legal (manages vendor onboarding)

**Language Banks:** Document how each persona talks about their problem:
- Words they use to describe their pain
- Words they'd search for in Google
- Objections they typically raise
- Success metrics they care about

### Phase 4: Delivery

**Score Tiers:**
- **A (80-100):** High fit across multiple dimensions. Immediate outreach priority.
- **B (60-79):** Good fit with some gaps. Nurture and monitor for signal improvement.
- **C (40-59):** Marginal fit. Low priority, only pursue if capacity allows.
- **D (<40):** Poor fit. Do not pursue. Below threshold.

Present the scoring model with:
1. Complete dimension definitions with all attributes, point values, and scoring rules
2. Weight justification based on calibration data or stated rationale
3. Negative persona catalog with explicit disqualification rules
4. Buying committee map per tier with role descriptions
5. Language banks per persona
6. Scoring template/calculator (formula or spreadsheet layout)

## Output Format

```markdown
# ICP Scoring Model: [Company Name]

## Scorecard Summary

| Dimension | Weight | Max Points |
|-----------|--------|------------|
| Firmographic | 40% | 100 |
| Technographic | 30% | 100 |
| Behavioral | 20% | 100 |
| Intent | 10% | 100 |

**Composite Formula:** ICP Score = (F × 0.40) + (T × 0.30) + (B × 0.20) + (I × 0.10)

**Tier Thresholds:** A: 80-100 | B: 60-79 | C: 40-59 | D: <40

---

## Dimension 1: Firmographic Fit

[Complete attribute table with scoring rules]

## Dimension 2: Technographic Fit

[Complete attribute table with scoring rules, must-haves, disqualifiers]

## Dimension 3: Behavioral Fit

[Complete attribute table with scoring rules]

## Dimension 4: Intent Signals

[Complete attribute table with scoring rules]

---

## Negative Persona Catalog

| Persona | Attributes | Override Rule |
|---------|-----------|---------------|
| [Excluded Industry] | [Attributes] | Score = 0 regardless of other dimensions |
| [Below Minimum ACV] | [Threshold] | Score = 0 |
| [Competitive Lock-in] | [Tech stack indicators] | Score ≤ 20 |

---

## Buying Committee Map

| Tier | Economic Buyer | Champion | Technical Evaluator | End User | Procurement |
|------|---------------|----------|---------------------|----------|-------------|
| A | [Role/Title] | [Role/Title] | [Role/Title] | [Role/Title] | [Role/Title] |
| B | [Role/Title] | [Role/Title] | [Role/Title] | [Role/Title] | [Role/Title] |

---

## Language Banks

### [Persona 1]
- Pain words: [list]
- Search terms: [list]
- Common objections: [list]
- Success metrics: [list]

[Repeat for each persona]

---

## Calibration Notes

[How weights were determined — empirical data or stated rationale. Coverage and win rate lift analysis if available.]

---

## Scoring Template

[Formula layout for implementation in Clay, spreadsheet, or CRM]
```

## Quality Check

Before delivering, verify:

- [ ] Do weights sum to 100%?
- [ ] Does each dimension have at least 3 scored attributes?
- [ ] Are there explicit negative persona rules that override the composite score?
- [ ] Does the model produce meaningful differentiation (not all companies scoring 70-80)?
- [ ] Are technographic must-haves genuinely required, or just "nice to have"?
- [ ] Does the buying committee map cover all MEDDICC-relevant roles?
- [ ] Are language banks specific enough to write personalized outreach from?
- [ ] If calibration data was available, were weights adjusted based on empirical win rate lift?
- [ ] Is the minimum ACV threshold clearly stated and enforced in scoring?
- [ ] Would the model have correctly scored the historical win/loss examples provided?

## Common Pitfalls

1. **Equal weighting across dimensions.** Giving firmographics, technographics, behaviors, and intent equal weight produces a model that doesn't discriminate. Firmographics and technographics should dominate (60-80% combined) because they represent structural fit. Behavior and intent are dynamic signals that supplement structural fit.

2. **Scoring what feels important rather than what predicts conversion.** Without empirical calibration, scoring models reflect internal assumptions rather than market reality. If you have win/loss data, use it. If you don't, start with recommended weights and commit to recalibrating after 50 deals.

3. **Binary scoring instead of graduated scoring.** "In target industry: yes/no" is too coarse. A company in an adjacent industry is worth something. A graduated scale (100/60/20/0) captures the reality that fit is a continuum.

4. **Negative personas that are too narrow.** "We don't sell to competitors" is obvious. The valuable negative personas are the subtle ones: companies that look like ICP on firmographics but have disqualifying technographic or behavioral profiles. Document the lookalike traps.

5. **Buying committee map that includes everyone.** Not every persona needs to be present for every deal. Map personas to ICP tiers and deal sizes. A $10K ACV deal doesn't need the same committee as a $100K deal.

6. **Language banks that use internal jargon.** The words your team uses to describe the problem are not the words prospects use. Validate language banks against actual prospect conversations, sales call recordings, and customer interview transcripts.

7. **Treating the model as static.** ICP scoring models decay as markets shift, competitors enter, and your product evolves. Include a recalibration cadence (recommended: quarterly review, recalibration every 6 months or 100 deals, whichever comes first).

8. **Scoring on data you can't actually obtain at scale.** A scoring dimension that requires a manual research step per lead doesn't scale. Ensure each attribute in the model can be sourced from enrichment APIs, public data, or automated signals.

## Related Skills

- **gtm-context**: Run before this skill. Provides the ICP definition, beachhead segment, and competitive landscape this skill operationalizes.

- **lead-finding**: Run after this skill. Consumes the ICP scoring model to filter and prioritize discovered leads.

- **signal-scoring**: Run alongside this skill. Handles dynamic intent and behavioral signals while this skill handles structural fit. Together they form a complete lead qualification system.

- **list-building**: Run after this skill. Uses the scoring model as filtering criteria in Clay table ICP blocks.

- **data-enrichment-strategy**: Run after this skill. Defines the enrichment waterfall that populates the scoring dimensions with actual data.

---
name: a-b-testing
description: >-
  Designs and analyzes A/B tests for GTM campaigns with statistical rigor.
  Tests subject lines, email copy, CTAs, send times, sequences, landing pages,
  and offers. Applies statistical significance testing at 95% confidence using
  chi-square and t-test methods. Uses ICE and PIE scoring to prioritize test
  ideas. Manages experiment cadence with 30/60/90-day testing roadmaps.
  Activates when the user wants to run experiments, test copy variants,
  optimize campaigns, or measure what's statistically working.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: analytics
  tags: [ab-testing, experimentation, statistical-significance, copy-testing, optimization, ice, pie]
  related_skills: [campaign-analytics, cold-email-copywriting, landing-pages, cold-email-strategy]
  frameworks: [GrowthHackers ICE, Sean Ellis Experimentation, Optimizely Statistical Engine]
---

# A/B Testing

## Overview

A/B Testing brings experimental rigor to GTM optimization. The core principle: most "optimizations" are guesswork dressed as strategy. Teams change subject lines because someone "feels" they're better, rewrite copy based on a single positive reply, or abandon channels because of one bad week. This skill prevents the waste of optimizing based on noise rather than signal.

The non-obvious rule: statistical significance is necessary but insufficient. A statistically significant 10% improvement in open rate that produces 0% more meetings is a distraction. Optimize for downstream revenue metrics — reply rate, meeting rate, conversion rate — not vanity metrics. Every test must trace its impact through the full funnel.

This skill produces: an Experiment Design Document with hypothesis, success metrics, power analysis, and methodology; a prioritized ICE/PIE test backlog; a 30/60/90-day testing roadmap; and a Results Analysis Report with statistical tests, confidence intervals, and scale/stop/kill recommendations.

## When to Use

- User says "A/B test" or "split test" → activate this skill
- User mentions "test subject lines" or "test email copy" → use for experimental design
- User asks "is this statistically significant" or "what sample size do I need" → activate for statistical guidance
- User says "experiment design" or "test plan" → use this skill
- User asks "how do I prioritize tests" or "what should I test next" → use ICE/PIE scoring
- User mentions "testing roadmap" or "experiment cadence" → plan the roadmap
- Trigger phrases: A/B testing, split testing, experiment, statistical significance, confidence interval, sample size, test variant, control group, multivariate test

Do NOT use for:
- Analyzing existing campaign performance without test design → use campaign-analytics
- Writing copy variants → use cold-email-copywriting (run after this skill for variant creation)
- General campaign analytics and benchmarking → use campaign-analytics
- Setting up sequences or cadences → use cold-email-strategy
- Landing page CRO (broader scope) → use landing-pages

## Authoritative Foundations

This skill draws from the following established methodologies:

- **Sean Ellis (GrowthHackers) — Experimentation System** — High-tempo testing framework: at least one test per week, backlog-driven, hypothesis-first. Ellis's work at Dropbox, Eventbrite, and LogMeIn established the growth experimentation discipline. The core principle: testing velocity matters more than test size. Two tests per week with 100 sample size beats one test per month with 10,000.

- **GrowthHackers ICE Scoring Model** — Impact, Confidence, Ease framework for test prioritization. Each test idea scored 1-10 on three dimensions. ICE ensures you test the most valuable ideas first, not the most interesting ones.

- **PIE Framework** (WiderFunnel/Chris Goward) — Potential, Importance, Ease. Alternative to ICE for companies further along the optimization maturity curve. PIE weights strategic importance higher than ICE which weights ease.

- **Optimizely / VWO — Statistical Engine** — Sequential testing, false discovery rate control, and multi-arm bandit approaches. Modern experimentation platforms have moved beyond simple t-tests. This skill applies these principles without requiring those specific platforms.

- **Ron Kohavi (Microsoft/Airbnb) — Trustworthy Online Controlled Experiments** — The definitive academic work on A/B testing at scale. Kohavi's rules: never stop a test early based on "significance," always pre-register hypotheses and metrics, segment results by new vs returning users.

## Prerequisites

- Historical campaign data with per-variant metrics: sent, delivered, opened, clicked, replied, meetings booked per variant (minimum 200 sends per variant for significance)
- Campaign platform that supports variant splitting (Smartlead, Instantly, Apollo, or manual list splitting)
- Baseline metrics to compare against: current open rate, reply rate, meeting rate for the campaign being tested
- Optional: statistical software or spreadsheet with CHISQ.TEST, T.TEST functions (Google Sheets, Excel, or Python/R)
- Recommended upstream skill: campaign-analytics (to identify which metrics to test)

## Step-by-Step Process

### Phase 1: Intake

Gather required information from the user. Ask all questions at once. Do not proceed until all answers are received.

Required intake questions:

1. **What are you testing?** Subject line, email body copy, CTA, send time, sender name, personalization level, sequence structure, channel, offer, landing page, or other.
2. **What is the current baseline?** Current metric value for the element being tested (e.g., current reply rate is 2.1%).
3. **What is the minimum detectable effect?** What improvement would be practically meaningful? (e.g., "We want to detect a 30% relative improvement from 2.1% to 2.7%")
4. **What is your primary success metric?** What metric determines if the test wins? Must be a downstream metric (reply rate, meeting rate, conversion rate), not a vanity metric (open rate).
5. **What is your current sending volume?** How many emails per day/week can you allocate to this test?
6. **What is the test duration constraint?** How long can the test run? (1 week? 2 weeks? 4 weeks?)
7. **What are the risk constraints?** Is there a maximum acceptable performance drop? (e.g., "We can tolerate up to a 20% decrease in reply rate")

### Phase 2: Experiment Design

Design the experiment with statistical rigor:

1. **Formulate the hypothesis** in if-then-because format:
   - IF we [change specific element], THEN [metric] will [direction] by [magnitude], BECAUSE [behavioral rationale].
   - Example: "IF we replace the direct meeting ask CTA with a low-friction 'worth a conversation?' question, THEN reply rate will increase by 30%, BECAUSE recipients perceive lower commitment in responding to a question versus scheduling a meeting."

2. **Define primary and guardrail metrics**:
   - **Primary metric**: The metric you're trying to improve (must be downstream: reply rate, meeting rate, conversion).
   - **Guardrail metrics**: Metrics that must not degrade significantly (e.g., unsubscribe rate must stay <0.5%, spam complaint rate must stay <0.1%, positive reply sentiment must stay >70% of replies).
   - **Vanity check metrics**: Open rate, click rate — tracked but not used for decisions unless they trigger guardrail violations.

3. **Power analysis — determine required sample size**:
   ```
   For proportions (reply rate, open rate, conversion rate):
   n = (Z_α/2 + Z_β)² × (p₁(1-p₁) + p₂(1-p₂)) ÷ (p₁ - p₂)²

   Where:
   - Z_α/2 = 1.96 (for 95% confidence, two-tailed)
   - Z_β = 0.84 (for 80% power)
   - p₁ = baseline proportion (e.g., 0.021 for 2.1% reply rate)
   - p₂ = expected proportion after improvement (e.g., 0.027 for 2.7%)
   ```

   Simplified approximation for common GTM test scenarios:

   | Baseline Rate | Minimum Detectable Effect (MDE) | Required Sample Per Variant |
   |---------------|-------------------------------|----------------------------|
   | 1% | 50% relative (to 1.5%) | 8,500+ |
   | 1% | 100% relative (to 2.0%) | 2,800+ |
   | 2% | 50% relative (to 3.0%) | 4,600+ |
   | 2% | 100% relative (to 4.0%) | 1,300+ |
   | 5% | 50% relative (to 7.5%) | 2,000+ |
   | 5% | 100% relative (to 10%) | 500+ |
   | 10% | 50% relative (to 15%) | 1,100+ |
   | 10% | 100% relative (to 20%) | 250+ |

   **Critical rule**: Never run a test with fewer than 200 sends per variant. Below 200, even large effects are indistinguishable from random noise.

4. **If sample size cannot be met within time constraints**:
   - Option A: Accept larger MDE (test for bigger improvements only)
   - Option B: Reduce variants (2 variants not 4 minimizes sample requirement)
   - Option C: Extend test duration
   - Option D: Don't run the test. Making decisions on insufficient data is worse than not testing.

5. **Design the variant split**:
   - **Control**: Current version. Always include a control. Testing Variant A vs Variant B without a control tells you which is relatively better, not whether either is an actual improvement.
   - **Variant A/B/C**: Test variants. Limit to 2-3 variants per test. More variants require more sample and slower learning.
   - **Randomization**: Random split (not alternating, not time-based). Ensure each contact has equal probability of receiving each variant.
   - **Segmentation**: If testing across segments (ICP tiers, personas, channels), ensure each segment has adequate sample size independently.

6. **Define stopping rules**:
   - **Do NOT peek**: Do not check results and stop early when they "look significant." Early stopping inflates false positive rates from 5% to 25-30%. Set a fixed end date.
   - **Exception — harm detection**: If a variant's guardrail metrics trigger (e.g., unsubscribe rate spikes above 1%), stop that variant immediately.
   - **Fixed horizon only**: Run the test for the pre-determined duration. Calculate significance only at the end.

### Phase 3: Test Execution

Execute the experiment as designed:

1. **Pre-launch checklist**:
   - [ ] Hypothesis documented in if-then-because format
   - [ ] Primary metric and guardrail metrics defined with thresholds
   - [ ] Required sample size calculated and achievable within test duration
   - [ ] Control group included
   - [ ] Randomization confirmed (platform supports true random split)
   - [ ] Test duration set with fixed end date
   - [ ] All variants proofread and QA'd (broken links, placeholder text, personalization errors)
   - [ ] Tracking confirmed: reply attribution, meeting attribution, CRM pipeline tracking all functional
   - [ ] Stakeholders informed: test will run for X days, no decisions until completion

2. **Launch the test**:
   - If using manual list splitting: use a random number generator, not "first half of list." Sort randomly then split.
   - If using platform A/B: verify the platform correctly randomizes (some platforms round-robin which is NOT random and creates time-of-day bias).
   - Send all variants simultaneously or within the same time window (9-11am same day). Time-of-day and day-of-week confounders are real.

3. **During the test**:
   - Monitor guardrail metrics daily (not primary metric — you committed to not peeking).
   - If a variant's unsubscribe rate spikes, pause that variant immediately.
   - If a variant's bounce rate exceeds 5%, pause that variant — deliverability issue, not a test result.
   - Do NOT check statistical significance mid-test. The math doesn't work if you peek.
   - Document any external events that could confound results (holiday, product launch, competitor announcement, system outage).

4. **End the test** at the pre-determined date, not when you "feel" you have enough data. If sample size target wasn't reached (lower volume than expected), note this as a limitation and extend if possible.

### Phase 4: Statistical Analysis

Analyze results with proper statistical methods:

1. **Calculate observed metrics per variant**:
   - Control: open rate X%, reply rate Y%, meeting rate Z%
   - Variant A: open rate X%, reply rate Y%, meeting rate Z%
   - Calculate relative lift: (Variant - Control) ÷ Control × 100%

2. **Statistical significance test selection**:
   - **For proportions (open rate, reply rate, meeting rate)**: Use chi-square test of independence.
     ```
     In Google Sheets: =CHISQ.TEST(observed_range, expected_range)
     In Excel: =CHISQ.TEST(actual_range, expected_range)
     ```
     Build a 2×2 contingency table:
     | | Control | Variant |
     |---|---|--------|
     | Replied | A | B |
     | Didn't Reply | C | D |
   - **For continuous metrics (reply time, deal size)**: Use independent two-sample t-test (two-tailed).
     ```
     In Google Sheets: =T.TEST(array1, array2, 2, 2)
     ```
   - **Significance threshold**: p < 0.05 (95% confidence). If p >= 0.05, the result is NOT statistically significant — regardless of how big the observed difference looks.

3. **Calculate confidence intervals** for the difference:
   ```
   95% CI for difference in proportions:
   (p₁ - p₂) ± 1.96 × √(p₁(1-p₁)/n₁ + p₂(1-p₂)/n₂)
   ```
   Report: "The variant improved reply rate by X% (95% CI: Y% to Z%)." If the CI crosses zero, the result is not statistically significant.

4. **False discovery rate consideration** for multi-variant tests:
   - Testing 3 variants against control = 3 comparisons. The chance of at least one false positive at p < 0.05 is 1 - (0.95)³ = 14.3%.
   - Apply Bonferroni correction for 3+ comparisons: divide significance threshold by number of comparisons. For 3 variants, use p < 0.017 (0.05/3).

5. **Practical significance assessment**:
   - Is the effect size large enough to matter, even if statistically significant?
   - A 5% improvement in reply rate (from 2.00% to 2.10%) with p < 0.001 is statistically significant with enough sample — but practically meaningless.
   - **Minimum practically significant effect**: reply rate improvement of 20% relative (e.g., 2.0% → 2.4%), meeting rate improvement of 10% relative.

6. **Segment analysis** (do NOT skip):
   - Analyze results by: ICP tier, persona, company size, industry, send time (AM vs PM), day of week.
   - A variant that "loses" overall might win in a critical segment. A variant that "wins" overall might lose in your highest-value segment.
   - Segment analysis is exploratory and hypothesis-generating, not confirmatory. Flag for follow-up testing.

### Phase 5: Decision Framework — Stop, Scale, Iterate

Apply the decision framework to test results:

**SCALE — deploy the winning variant to all traffic**:
- Criteria: Statistically significant improvement on primary metric (p < 0.05), guardrail metrics all within acceptable range, practical significance confirmed (effect size meaningful), segment analysis does not reveal harm in key segments.
- Action: Deploy variant as new control. Document expected annualized impact.
- Time to deploy: Within 1 week of test completion.

**ITERATE — run a follow-up test**:
- Criteria: Directionally positive but not statistically significant (p between 0.05 and 0.20), or statistically significant on a secondary but not primary metric, or significant overall but mixed by segment.
- Action: Design follow-up test with larger sample size, refined variant, or segment-specific targeting.
- Time to follow-up: Within 2 weeks.

**STOP — do not deploy, archive the learning**:
- Criteria: Not statistically significant and directionally neutral or negative (p > 0.20), or statistically significant degradation, or guardrail violations.
- Action: Document what was learned. The hypothesis was wrong — that's valuable information. Archive in a "negative results" library to prevent future teams from repeating.
- Important: A null result is not a failure. It's data that prevents wasted effort on dead ends.

**KILL — variant is harmful, stop immediately**:
- Criteria: Guardrail metrics severely violated (unsubscribe >1%, spam complaint >0.3%), or primary metric shows statistically significant 20%+ degradation.
- Action: Stop the variant immediately (even mid-test). Investigate root cause. Document the harm for future reference.

### Phase 6: Test Backlog Management (ICE/PIE)

Build and maintain a prioritized test backlog:

1. **Collect test ideas** from all sources: campaign analytics insights, copy analysis findings, team suggestions, competitor observations, customer feedback, qualitative research.

2. **ICE Scoring** (Impact, Confidence, Ease — GrowthHackers model):
   - **Impact (1-10)**: If this test wins, how much will it improve the primary business metric? 10 = transformative, 1 = negligible.
   - **Confidence (1-10)**: How confident are you this change will produce the expected effect? 10 = backed by strong data/prior test, 1 = wild guess.
   - **Ease (1-10)**: How easy is this test to implement? 10 = change one line of copy in existing sequence, 1 = requires engineering, design, and legal review.
   - ICE Score = (Impact + Confidence + Ease) ÷ 3. Sort by descending score.

3. **PIE Scoring** (Potential, Importance, Ease — WiderFunnel model. Better for larger organizations):
   - **Potential (1-10)**: How much improvement is possible on this page/step? 10 = currently at 0.5% conversion, could be 5%, 1 = already optimized to near-maximum.
   - **Importance (1-10)**: How valuable is this page/step to the business? 10 = pricing page (direct revenue impact), 1 = blog sidebar.
   - **Ease (1-10)**: Same as ICE Ease.
   - PIE Score = (Potential + Importance + Ease) ÷ 3.

4. **Which model to use**: ICE for early-stage, fast-moving teams (prioritizes speed). PIE for established teams with optimization maturity (prioritizes strategic value). Both are better than no prioritization.

5. **Backlog hygiene**:
   - Maintain 20-30 test ideas in the backlog at all times.
   - Remove ideas that have been sitting for 6+ months without execution (either not valuable enough or constraining).
   - Test completion rate should be >80% of launched tests (don't start tests you can't finish).
   - Archive all completed tests in a searchable knowledge base.

### Phase 7: Testing Roadmap (30/60/90 Day)

Build a structured testing cadence:

**30-Day Sprint**: Launch 2-4 tests
- Week 1-2: Run 2 quick tests (high ICE, low sample requirement)
- Week 2-4: Run 1-2 longer tests (higher sample requirement)
- End of 30 days: Review results, update backlog, plan next sprint

**60-Day Review**: Intermediate assessment
- Which test types are producing the most wins? (e.g., CTA tests outperform subject line tests 3:1)
- Are you testing the full funnel or only top-of-funnel (subject lines, open rates)?
- Is testing velocity sufficient? Target: 1 test launched per week minimum.
- Are null results being documented or ignored?

**90-Day Strategic Review**: Long-term assessment
- Cumulative improvement: across all winning tests, what is the total estimated impact on the primary business metric?
- Testing coverage: what % of the customer journey has been tested?
- Methodology audit: any statistical shortcuts (peeking, stopping early, insufficient sample)?
- Roadmap refresh: based on 90 days of learning, what should be prioritized for the next quarter?

## Output Format

The agent should produce output in this structure:

```markdown
# [Test Name] — Experiment Report

## Hypothesis
IF we [change], THEN [metric] will [direction] by [magnitude], BECAUSE [rationale].

## Experiment Design
- **Test Type**: A/B/n (n variants + control)
- **Variants**: Control vs A vs B [descriptions]
- **Primary Metric**: [metric name]
- **Guardrail Metrics**: [metric names with thresholds]
- **Sample Size Required**: N per variant
- **Test Duration**: [start date] to [end date] (X days)

## Results
| Metric | Control | Variant A | Variant B | Winner? |
|--------|---------|-----------|-----------|---------|
| Sent | N | N | N | - |
| Open Rate | X% | X% | X% | - |
| Reply Rate | X% | X% | X% | - |
| Meeting Rate | X% | X% | X% | - |

## Statistical Analysis
- **Method**: Chi-square test of independence (proportions)
- **Control vs Variant A**: p = X.XXX (significant / not significant at 95%)
- **Control vs Variant B**: p = X.XXX (significant / not significant at 95%)
- **Confidence Interval**: [lower bound] to [upper bound]
- **Practical Significance**: [effect size] — [meaningful / not meaningful]

## Segment Analysis
| Segment | Control Reply% | Variant Reply% | Lift | Significance |
|---------|---------------|----------------|------|-------------|
| SMB | X% | X% | +X% | p=X.XX |
| Enterprise | X% | X% | -X% | p=X.XX |

## Decision
**SCALE / ITERATE / STOP / KILL**
- Rationale: [specific evidence for decision]
- Action: [specific next step with timeline]

## Learnings Archived
- [Key insight 1]
- [Key insight 2]

---

# Test Backlog (ICE-Prioritized)
| Rank | Test Idea | I | C | E | ICE | Sample Needed | Dependencies |
|------|-----------|---|---|---|-----|--------------|-------------|
| 1 | ... | 9 | 7 | 8 | 8.0 | 2,000/variant | None |
| 2 | ... | 8 | 6 | 9 | 7.7 | 5,000/variant | Test 1 must complete |

---

# 90-Day Testing Roadmap
[Monthly breakdown of scheduled tests, expected learnings, and resource requirements]
```

## Quality Check

Before delivering, verify:

- [ ] Is every test documented with a formal hypothesis in if-then-because format?
- [ ] Has power analysis confirmed the required sample size is achievable?
- [ ] Are primary metrics downstream (reply rate, meeting rate), not vanity (open rate)?
- [ ] Is the test duration fixed in advance with no early stopping (except harm detection)?
- [ ] Are statistical tests correctly applied (chi-square for proportions, t-test for continuous)?
- [ ] Has practical significance been assessed separately from statistical significance?
- [ ] Is segment analysis included to prevent masking effects?
- [ ] Are negative/null results being documented, not discarded?
- [ ] Would a growth experimentation specialist approve the methodology?

## Common Pitfalls

1. **Peeking and early stopping.** This is the most common and most damaging A/B testing error. Checking results daily and stopping when they "look significant" inflates false positive rates from 5% to 25-30%. Set a fixed end date and DO NOT look at primary metric results until it arrives. The math of statistical tests assumes a fixed sample size — peeking violates this assumption.

2. **Testing for statistical significance on vanity metrics.** A subject line test that produces a statistically significant 15% open rate improvement but zero change in reply rate is a bad test. You optimized a metric that doesn't drive revenue. Always designate a downstream metric (reply rate, meeting rate, conversion) as the primary metric and optimize for that.

3. **Insufficient sample size.** Running a test with 100 sends per variant when you need 2,000 to detect the expected effect. Results will be noisy and misleading. If you cannot achieve the required sample size, either increase the MDE (test bigger changes), reduce variants, or don't run the test. A decision made on insufficient data is worse than no decision.

4. **No control group.** Testing Variant A vs Variant B without a control tells you which is relatively better but not whether either is better than what you're currently doing. Both could be worse than the baseline. Always include a control.

5. **Multiple comparisons without correction.** Running a test with 5 variants and declaring significance whenever any variant's p < 0.05 gives a ~23% chance of at least one false positive. Apply Bonferroni correction (divide significance threshold by number of comparisons) or use a different framework (ANOVA for 3+ variants).

6. **Confusing statistical significance with practical significance.** With large enough sample sizes, even trivial differences become statistically significant. A 0.1% improvement in reply rate with p < 0.001 is statistically significant but practically useless. Always ask: "Is the effect size large enough to justify the change?"

7. **Not segmenting results.** A variant that wins overall might be losing in your highest-value segment. An overall "win" of +10% enterprise reply rate vs -5% SMB reply rate might be a net negative for enterprise-focused companies. Always segment by at least ICP tier and persona.

8. **Running tests without a hypothesis.** "Let's just test some different subject lines and see what happens" is experimentation theater, not experimentation. Every test needs a hypothesis grounded in a behavioral rationale. Test results should update your understanding, not just tell you which random variant happened to win.

## Related Skills

- **campaign-analytics**: Identifies what to test. Run before this skill to diagnose which metrics are underperforming and need experimentation.
- **cold-email-copywriting**: Creates the actual copy variants. Run after this skill's hypothesis and test design are complete.
- **landing-pages**: Extends A/B testing methodology to landing page optimization and conversion rate experimentation.
- **cold-email-strategy**: Ensures test variants don't break sequence logic or cadence rules.
- **signal-scoring**: Tests can validate whether specific signals (funding, hiring, job change) produce statistically better response rates.

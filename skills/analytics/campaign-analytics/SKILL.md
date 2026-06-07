---
name: campaign-analytics
description: >-
  Analyzes campaign performance across a 6-layer metrics stack from infrastructure
  to revenue. Applies diagnostic decision trees to identify root causes of
  underperformance. Extracts winning copy patterns through statistical comparison.
  Benchmarks against industry, segment, and portfolio averages. Delivers actionable
  optimization recommendations. Activates when the user asks about campaign
  performance, email metrics, copy testing, A/B results, or wants to understand why
  a campaign is underperforming.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: analytics
  tags: [campaign, analytics, metrics, copy-analysis, benchmarking, optimization]
  related_skills: [a-b-testing, deliverability-monitoring, attribution, gtm-metrics]
  frameworks: [Winning by Design Bowtie Model, David Skok SaaS Metrics]
---

# Campaign Analytics

## Overview

Campaign Analytics provides a systematic framework for measuring, diagnosing, and optimizing outbound and inbound campaign performance. The core principle is that campaigns fail at specific layers in the infrastructure-to-revenue stack — fixing the wrong layer wastes time and money. This skill prevents the common mistake of tweaking copy when deliverability is broken, or adjusting targeting when the offer is wrong.

The non-obvious rule: every campaign metric exists in a dependency chain. Deliverability gates open rates. Open rates gate reply rates. Reply rates gate meetings. Meetings gate pipeline. You cannot fix layer 5 if layer 2 is broken. This skill enforces layer-by-layer diagnosis before optimization.

This skill produces a Campaign Performance Diagnostic Report containing: a 6-layer health scan, a diagnostic decision tree with root cause identification, winning copy extraction with statistical confidence, benchmark comparisons across three reference sets, and a prioritized optimization action plan with expected impact estimates.

## When to Use

- User says "analyze my campaign" or "campaign performance review" → activate this skill
- User mentions "open rates dropped" or "reply rates are low" → use this skill for root-cause diagnosis
- User asks "which subject line performed better" or "what copy is working" → use the copy extraction module
- User says "benchmark my metrics" or "how do I compare to industry" → activate benchmarking
- User mentions "campaign ROI" or "cost per meeting" → use full stack analysis
- User asks "why isn't this campaign working" → run the diagnostic decision tree
- Trigger phrases: campaign analytics, email performance, sequence metrics, campaign optimization, campaign dashboard, pipeline from campaigns

Do NOT use for:
- Setting up new campaigns or sequences → use cold-email-strategy
- Writing new email copy → use cold-email-copywriting
- Deliverability-only issues (DNS, warmup, blacklists) → use deliverability-monitoring
- Attribution modeling across channels → use attribution
- Real-time alerting on pipeline metrics → use proactive-alerts

## Authoritative Foundations

This skill draws from the following established methodologies:

- **Winning by Design — Bowtie Model** — Revenue visualization that extends beyond the funnel through retention and expansion. Campaign analytics map to the acquisition side of the bowtie: awareness → engagement → opportunity → close. Each transition has measurable conversion rates that this skill diagnoses.

- **Winning by Design — GTM Index** — 1-10 scoring across 6 models (Revenue, Data, Math, Operating, Growth, GTM). The Data model specifically governs measurement discipline. Campaign analytics without reliable data architecture produces misleading conclusions. This skill applies Data Model scoring to campaign measurement infrastructure.

- **David Skok — SaaS Metrics** — Pipeline velocity and conversion rate analysis. Skok's work on understanding sales funnel dynamics through cohort analysis informs the layer-by-layer diagnostic approach. Campaigns produce cohorts; comparing cohort performance reveals what's changing over time.

- **Gartner/CEB — Challenger Sale** — Insight-led selling. Campaign effectiveness correlates with the quality of commercial insight delivered. This skill's copy extraction module evaluates whether winning messages teach, tailor, and take control versus simply pitching.

## Prerequisites

- Campaign data in structured format (CSV, Google Sheets, or CRM export) with at minimum: send date, opens, clicks, replies, meetings booked, opportunities created, pipeline value, and won deals — all keyed by campaign/variant
- Access to sending platform analytics (Smartlead, Instantly, Salesforge, Apollo, or Outreach)
- CRM access for pipeline attribution (HubSpot, Salesforce, or Attio)
- Optional: deliverability data from tools like MXToolbox, Google Postmaster, or Validity for layer 1 diagnosis
- Optional: Google Analytics or attribution platform data for inbound campaign analysis
- Recommended upstream skill: deliverability-monitoring (if bounce rates exceed 2%)

## Step-by-Step Process

### Phase 1: Intake

Gather required information from the user. Ask all questions at once. Do not proceed until all answers are received.

Required intake questions:

1. **Campaign scope**: Which campaigns, sequences, or time periods should be analyzed? Define start and end dates.
2. **Data sources**: Where is campaign data stored? (Smartlead, Instantly, CRM, spreadsheet?) Request export or access.
3. **Goals**: What were the campaign objectives? (Meetings booked, pipeline generated, revenue closed?) What targets were set?
4. **Segments**: Were there audience segments, ICP tiers, or personas targeted? List them for cohort analysis.
5. **Variants tested**: Were A/B tests run? If so, what was varied (subject lines, copy, offer, timing, channel)?
6. **Budget context**: Total spend including tools, data enrichment, and team time. Needed for cost-per-meeting and ROI calculations.
7. **Benchmark context**: Company stage (seed, Series A, growth), ACV range, ICP type (SMB, mid-market, enterprise), and industry vertical for appropriate benchmark selection.

### Phase 2: Data Assembly

Load and validate campaign data before analysis. This phase ensures data integrity.

1. **Import all data sources** into a unified analysis structure. Map fields to a canonical schema: campaign_id, variant_id, send_date, recipient_count, delivered, opened, clicked, replied, bounce_type, meeting_booked, meeting_date, opportunity_created, opportunity_value, deal_closed, deal_value, segment, persona, channel.

2. **Validate data integrity**:
   - Check for missing data in critical fields (delivered, opened, replied)
   - Verify send date consistency — no future dates, gaps explained
   - Confirm recipient counts match between sending platform and CRM
   - Flag any campaigns where delivered count < 50% of sent (possible infrastructure issue)
   - Test reply attribution: do meeting_booked counts align with replied-to-meeting conversion rates that make sense?

3. **Calculate raw metrics** for every campaign/variant:
   - Delivery Rate = delivered ÷ sent
   - Open Rate = unique opens ÷ delivered
   - Click Rate = unique clicks ÷ delivered
   - Reply Rate = replies ÷ delivered
   - Meeting Rate = meetings_booked ÷ delivered
   - Opportunity Rate = opportunities ÷ meetings_booked
   - Pipeline Rate = total_pipeline_value ÷ opportunities
   - Win Rate = deals_closed ÷ opportunities
   - Cost Per Meeting = total_campaign_cost ÷ meetings_booked
   - Cost Per Opportunity = total_campaign_cost ÷ opportunities_created

4. **Segment data** by cohort dimensions: ICP tier, persona, channel, time period (weekly cohorts for trend analysis), and variant (for A/B analysis).

### Phase 3: 6-Layer Diagnostic Stack

Run the complete 6-layer diagnostic. Each layer must be healthy before diagnosing the next.

**Layer 1: Infrastructure & Deliverability**

Metrics checked: Delivery rate, bounce rate by type (hard vs soft), spam complaint rate, inbox placement rate.

Diagnostic thresholds:
- Delivery rate < 95% → critical. Check DNS (SPF/DKIM/DMARC), blacklist status, sending reputation.
- Hard bounce rate > 2% → critical. Pause campaign. Data source or verification process is failing.
- Soft bounce rate > 3% → warning. Possible mailbox full, temporary server issues, rate limiting.
- Spam complaint rate > 0.1% → critical. Content or targeting problem. Google/Microsoft thresholds are 0.1-0.3%.

Only proceed to Layer 2 if Layer 1 passes all thresholds.

**Layer 2: Audience & Targeting**

Metrics checked: Open rate, open-to-reply rate, unsubscribe rate, negative reply sentiment ratio.

Diagnostic thresholds:
- Open rate < 30% (cold) or < 50% (warm) → audience mismatch or subject line failure. Check: is ICP definition accurate? Are contacts still at company? Are job titles current?
- Unsubscribe rate > 0.5% → targeting or frequency problem. Audience doesn't want this message.
- Negative reply sentiment > 20% of all replies → messaging-audience mismatch. Wrong persona or wrong problem.

Decision tree: If open rate is low AND Layer 1 is healthy → subject line or sender reputation problem. If open rate is healthy but reply rate is low → copy or offer problem (diagnose at Layer 3).

**Layer 3: Messaging & Copy**

Metrics checked: Reply rate, positive reply rate, meeting conversion rate from replies, click-through rate on links.

Diagnostic thresholds:
- Reply rate < 1% (cold outbound) → copy is not compelling. Test new frameworks.
- Reply rate < 3% (warm/inbound) → offer clarity problem.
- Positive reply rate < 60% of total replies → messaging is getting attention but not the right attention. People reply to unsubscribe or express disinterest.
- Click rate < 2% and reply rate < 1% → the email is being read but not acted on. Weak call-to-action.

Winning copy extraction (see Phase 5 for full methodology):
- Compare variants with statistically significant differences in reply rate
- Extract common structural patterns, word choice, sentence length, and personalization elements from top-quartile performers
- Flag patterns that appear in bottom-quartile performers as anti-patterns

**Layer 4: Conversion & Follow-Up**

Metrics checked: Reply-to-meeting rate, meeting show rate, time-to-response, follow-up cadence adherence.

Diagnostic thresholds:
- Reply-to-meeting rate < 20% → SDR skill gap or scheduling friction. Check: is calendar link easy? Is response time under 5 minutes?
- Meeting show rate < 80% → pre-meeting engagement problem. Check: confirmation emails, reminder sequence, value reinforcement.
- Average time-to-response > 1 hour → speed-to-lead problem. Inbound leads degrade 10x after 5 minutes, 100x after 30 minutes.

**Layer 5: Pipeline Generation**

Metrics checked: Meeting-to-opportunity rate, average deal size, pipeline velocity from first meeting to opportunity, disqualification rate.

Diagnostic thresholds:
- Meeting-to-opportunity rate < 30% (inbound) or < 20% (outbound) → qualification problem. Check: MEDDICC qualification in discovery, ICP fit validation.
- Average deal size < target ACV → targeting lower in the organization or wrong personas.
- Disqualification rate > 50% → top-of-funnel targeting is too broad. Tighten ICP or add qualification gates.

**Layer 6: Revenue & ROI**

Metrics checked: Win rate, average sales cycle, LTV:CAC for campaign-sourced deals, campaign ROI (revenue ÷ cost), payback period.

Diagnostic thresholds:
- Campaign ROI < 3:1 → campaign cost structure problem or targeting yields low-value deals.
- LTV:CAC < 3:1 for campaign-sourced deals → either CAC is too high or these deals churn faster than organic.
- Average sales cycle > 2x company average → campaign-sourced leads may be lower intent.

### Phase 4: Diagnostic Decision Trees

For each underperforming metric, follow the decision tree to isolate root cause:

**Low Open Rate Decision Tree:**

1. Is delivery rate > 95%? → NO: Layer 1 issue. Fix deliverability first. → YES: Continue.
2. Is the sender domain warm (sending 4+ weeks)? → NO: Warmup incomplete. Reduce volume. → YES: Continue.
3. Are subject lines tested across variants? → NO: Run subject line A/B test with 3+ variants. → YES: Continue.
4. Does the from name match recipient expectations? → NO: Test recognizable from names. → YES: Continue.
5. Are recipients still at the company (no bounce, no auto-reply)? → NO: Data decay problem. Re-verify list. → YES: Audience-product mismatch. Revisit ICP.

**Low Reply Rate Decision Tree:**

1. Is open rate > 30%? → NO: Fix open rate first (subject line, sender, targeting). → YES: Continue.
2. Does copy follow a proven framework (3-line, AIDA, PAS, BAB)? → NO: Rewrite using cold-email-copywriting skill. → YES: Continue.
3. Does the CTA ask for a meeting directly vs. a low-friction reply? → Meeting ask in first email: CTA too aggressive. Switch to low-friction ask. → YES (low-friction CTA): Continue.
4. Is there personalization beyond {{first_name}}? → NO: Add research-based personalization (1-2 specific observations). → YES: Continue.
5. Is the value proposition specific and quantified? → NO: Make it concrete with numbers, outcomes, or specific problems. → YES: Offer-timing mismatch. Test different triggers or timing.

**Low Meeting Rate Decision Tree:**

1. Is reply rate > 1%? → NO: Fix copy first. → YES: Continue.
2. Is time-to-response under 5 minutes for positive replies? → NO: Implement instant alerts and auto-responders. → YES: Continue.
3. Is scheduling friction minimal (calendar link, no back-and-forth)? → NO: Use direct booking links. Remove "what time works?" emails. → YES: Continue.
4. Is the reply-to-meeting conversion message effective? → NO: Test meeting confirmation framework. → YES: SDR skill or offer-value gap. Coach or reposition.

### Phase 5: Winning Copy Extraction

When multiple variants exist with statistically significant performance differences, extract winning patterns:

1. **Identify comparison pairs**: Find variants where the difference in reply rate or meeting rate is statistically significant (p < 0.05 using chi-square test).
   - Minimum sample: 200+ sends per variant for reliable comparison
   - Minimum effect size: 30% relative improvement to be practically meaningful

2. **Structural analysis**: Deconstruct top-performing emails:
   - Word count distribution (subject line: 3-7 words optimal; body: 50-125 words optimal for cold)
   - Sentence count and average sentence length
   - Paragraph count and structure (single-paragraph vs multi-paragraph)
   - Question count (emails with 1-2 questions outperform zero-question emails 3:1)
   - Personalization token count and type (name, company, role, trigger event, observation)

3. **Content analysis**: Extract linguistic patterns:
   - Opening hook pattern (observation, question, compliment, data point, trigger)
   - Value proposition format (problem-solution, ROI, time-saver, risk-reducer)
   - Social proof usage (customer name, metric, category)
   - CTA format (question, suggestion, binary choice, direct ask)
   - Tone markers: casual vs formal, short vs elaborate, provocative vs safe

4. **Generate winning copy playbook**: Document the patterns that appear in 75%+ of top-quartile emails and 25% or fewer of bottom-quartile emails. These are your statistically derived best practices for this specific audience.

5. **Extract loser patterns**: Document patterns that appear predominantly in bottom-quartile emails. These are anti-patterns to avoid.

### Phase 6: Benchmarking

Compare campaign performance against three reference sets:

**Industry Benchmarks** (sourced from Mailshake, Mixmax, Woodpecker annual reports):

| Metric | Cold Outbound | Warm Outbound | Inbound Follow-Up |
|--------|---------------|---------------|-------------------|
| Open Rate | 20-40% | 40-60% | 50-70% |
| Reply Rate | 1-5% | 5-15% | 10-25% |
| Meeting Rate | 0.5-2% | 2-8% | 5-15% |
| Bounce Rate | <2% | <1% | <0.5% |
| Unsubscribe | <0.5% | <0.3% | <0.2% |

**Segment Benchmarks** (stage and ACV adjusted):

| Segment | Expected Reply Rate | Expected Meeting Rate | Expected Cost/Meeting |
|---------|-------------------|-----------------------|----------------------|
| SMB (< $10K ACV) | 3-5% | 1.5-3% | $50-150 |
| Mid-Market ($10-50K) | 2-4% | 1-2% | $150-400 |
| Enterprise ($50K+) | 1-3% | 0.5-1.5% | $400-1000+ |

**Portfolio Benchmarks**: Compare each campaign against the user's own historical performance. Calculate percentile rank within their campaign portfolio. Flag campaigns below the 25th percentile for priority optimization and above the 75th percentile for scaling.

### Phase 7: Optimization Recommendations

Generate prioritized recommendations based on diagnostic findings:

1. **Rank all identified issues** by estimated impact on downstream revenue (not on upstream metrics). A deliverability fix that improves delivery rate from 85% to 95% has 10% impact on all downstream metrics — higher total impact than a copy fix that improves reply rate from 1% to 2%.

2. **Assign each recommendation an effort level**: Low (configuration change, < 1 hour), Medium (copy rewrite, 1-4 hours), High (list rebuild, targeting change, new sequence, 4+ hours).

3. **Create an optimization roadmap** in priority order:
   - Priority 1: Infrastructure fixes (deliverability, authentication, warmup)
   - Priority 2: Targeting fixes (list hygiene, ICP refinement, data re-verification)
   - Priority 3: Messaging fixes (copy rewrites, A/B test plan)
   - Priority 4: Process fixes (response time, follow-up cadence, scheduling)
   - Priority 5: Strategic changes (offer redesign, channel mix, ICP expansion)

4. **Estimate impact**: For each recommendation, model the expected improvement:
   - If delivery rate improves from X% to Y%, expect Z additional delivered emails
   - At current open rate, that produces A additional opens
   - At current reply rate, B additional replies
   - At current meeting rate, C additional meetings
   - At current pipeline rate, D additional pipeline

## Output Format

The agent should produce output in this structure:

```markdown
# Campaign Performance Diagnostic Report

## Executive Summary
- Overall health score (A-F) with 1-sentence justification
- Top 3 issues ranked by revenue impact
- Top 3 recommendations with expected impact

## 6-Layer Health Scan
### Layer 1: Infrastructure & Deliverability
[Table: metric, value, threshold, status (pass/warn/fail), trend]
### Layer 2: Audience & Targeting
[Table: metric, value, threshold, status, trend]
### Layer 3: Messaging & Copy
[Table: metric, value, threshold, status, trend]
### Layer 4: Conversion & Follow-Up
[Table: metric, value, threshold, status, trend]
### Layer 5: Pipeline Generation
[Table: metric, value, threshold, status, trend]
### Layer 6: Revenue & ROI
[Table: metric, value, threshold, status, trend]

## Root Cause Analysis
- Decision tree path for each failing metric
- Primary root cause identified with evidence
- Contributing factors listed with confidence level

## Winning Copy Playbook
- Top patterns extracted from best-performing variants
- Anti-patterns from worst-performing variants
- Recommended subject line templates (3-5)
- Recommended opening hook templates (3-5)
- Recommended CTA templates (3-5)

## Benchmark Comparison
### vs Industry
[Table: our metric, industry median, percentile, interpretation]
### vs Segment
[Table: our metric, segment median, percentile, interpretation]
### vs Portfolio
[Table: our metric, portfolio median, portfolio percentile, interpretation]

## Optimization Roadmap
| Priority | Issue | Layer | Recommendation | Effort | Expected Impact | Timeline |
|----------|-------|-------|----------------|--------|-----------------|----------|
| 1 | ... | ... | ... | Low/Med/High | +X meetings/mo | Immediate |
| 2 | ... | ... | ... | Low/Med/High | +Y pipeline/mo | This week |

## Appendix
- Raw data summary tables
- Statistical test results (chi-square for A/B comparisons)
- Campaign cost breakdown
```

## Quality Check

Before delivering, verify:

- [ ] Has each of the 6 layers been explicitly diagnosed with pass/warn/fail status?
- [ ] Are all failing metrics traced to a root cause via the decision tree (not just "improve X")?
- [ ] Are benchmark comparisons contextual (stage, segment, ACV) rather than generic industry averages?
- [ ] Is the optimization roadmap prioritized by estimated revenue impact, not by metric severity?
- [ ] Are copy recommendations derived from statistical comparisons of actual variants, not opinion?
- [ ] Does each recommendation include a modeled expected impact with specific numbers?
- [ ] Are deliverables (diagnostic report, copy playbook, optimization roadmap) all present?
- [ ] Would a demand generation leader at a Series B SaaS company find this analysis actionable?

## Common Pitfalls

1. **Skipping Layer 1 diagnosis.** The most common mistake: jumping to copy fixes when deliverability is the real problem. Always start at Layer 1. If delivery rate is below 95%, nothing you do to copy matters until that's fixed. You can have the world's best email — if it lands in spam, nobody reads it.

2. **Over-indexing on open rates.** Open rates are a proxy for subject line effectiveness and sender reputation, not campaign success. A campaign with 80% open rate and 0% reply rate is failing. Optimize for reply rate, meeting rate, and pipeline — the metrics that generate revenue. Open rates matter only as a diagnostic signal.

3. **Ignoring statistical significance.** Comparing two variants where one got 3 replies from 200 sends and another got 2 replies from 200 sends is noise, not signal. Minimum 200 sends per variant before drawing conclusions. Use chi-square or Fisher's exact test to confirm significance at p < 0.05.

4. **Benchmarking without context.** Comparing SMB outbound reply rates to enterprise benchmarks (or vice versa) produces misleading conclusions. Always match benchmarks to ACV range, buyer persona seniority, and channel. A 2% reply rate to C-level enterprise prospects can be excellent; a 2% reply rate to SMB managers is poor.

5. **Treating metrics as independent.** Open rate, reply rate, and meeting rate are a chain. Improving open rates through clickbait subject lines often reduces reply rates because the email content doesn't match expectations. Optimize holistically — the combination that produces the highest meeting rate, not the highest individual metric.

6. **Optimizing for the wrong time horizon.** Campaign performance varies seasonally (Q4 holidays, summer slowdown, end-of-quarter urgency). Comparing week-over-week without accounting for seasonal patterns leads to false signals. Use 4-week rolling averages and compare to same-period-last-year where data exists.

7. **Neglecting reply sentiment analysis.** Counting replies without reading them is dangerous. A campaign generating 5% reply rate where 80% of replies are "unsubscribe" or "wrong person" is worse than a 1% reply rate with 100% positive sentiment. Always categorize replies: positive (interested), neutral (info request, not now), negative (unsubscribe, wrong person, complaint).

## Advanced Techniques

### Cohort Analysis for Campaign Decay Detection

Campaigns naturally decay over time as audiences saturate. Use cohort analysis to detect decay before it impacts pipeline:

1. **Create weekly cohorts**: Group sends by week. Track reply rate and meeting rate per cohort at week 1, week 2, and week 4.
2. **Calculate decay rate**: (Week N reply rate - Week 1 reply rate) ÷ Week 1 reply rate. If decay exceeds 20% within 4 weeks, audience is saturating.
3. **Identify saturation points**: When cumulative unique opens stops growing despite new sends, the addressable audience within current ICP is exhausted. Time to expand ICP, add new personas, or rotate to new segments.
4. **Seasonal adjustment**: Apply seasonal indices if multi-quarter data exists. Q4 is often 20-40% lower for outbound due to holidays.

### Conversion Path Analysis

Map the exact path from campaign touch to revenue:

1. **Trace every won deal back** to originating campaign touchpoint (which campaign, which variant, which channel, which sequence step).
2. **Calculate time-to-revenue** distribution: median and 90th percentile days from first touch to closed-won.
3. **Identify conversion bottlenecks**: where in the sequence do the most positive replies occur? Front-load those steps in future sequences.
4. **Channel contribution mapping**: for multi-channel campaigns, identify which channel produced the first meaningful engagement (not just first touch — first positive reply or meeting).

### Trigger-Based Performance Segmentation

Not all campaign sends are equal. Segment performance by trigger:

1. **Job change triggers**: Contacts who recently changed jobs. Expected reply rate: 2-3x baseline (they're in learning mode). Reference LeadMagic Job Change Detector as optional signal source.
2. **Funding event triggers**: Contacts at recently funded companies. Expected reply rate: 1.5-2x baseline.
3. **Hiring signal triggers**: Companies hiring for roles adjacent to your solution. Expected reply rate: 1.5x baseline.
4. **Technology adoption triggers**: Companies that recently adopted complementary or competitive technology. Expected reply rate: 1.3-1.5x baseline.
5. **Cold-no-trigger**: No observed signal. This is your baseline. Segment separately to avoid inflated expectations.

### Budget Allocation Optimization

Once reliable campaign metrics exist across multiple campaigns:

1. **Calculate marginal ROI per campaign**: (Incremental revenue - incremental cost) ÷ incremental cost, measuring at the margin.
2. **Rank campaigns by marginal ROI**, not average ROI. The campaign generating $100K from $20K spend (5:1) may have marginal ROI of 1:1 at 2x volume while another generating $50K from $10K (5:1) may have marginal ROI of 4:1 at 2x volume.
3. **Allocate next dollar of budget** to the campaign with the highest marginal ROI.
4. **Rebalance quarterly** as marginal returns shift.

### Multi-Touch Attribution for Campaign Sequences

Single-touch attribution overstates the importance of first and last touches:

1. **Track all touches** in the sequence: email 1, email 2, email 3, LinkedIn touch, call.
2. **Assign weighted credit**: Email 1 (10%), Email 2 (15%), Email 3 (25%), LinkedIn (20%), Call (30%). Weight later touches higher but don't zero out early touches.
3. **Calculate touch efficiency**: touches per meeting. If average is 8+ touches per meeting, sequence may be too long or targeting too broad.
4. **Identify optimal sequence length**: at which touch does marginal reply rate drop below 0.2%? Cut the sequence there.

## Related Skills

- **deliverability-monitoring**: Run first if bounce rates exceed 2%. Provides infrastructure health data that Layer 1 diagnosis requires.
- **a-b-testing**: Use after this skill identifies copy optimization opportunities. Provides experiment design and statistical rigor for follow-up tests.
- **attribution**: Run alongside this skill for multi-channel campaigns. Ensures conversion credit is correctly assigned.
- **gtm-metrics**: Feeds benchmark data and portfolio-level context into this skill's Layer 6 revenue analysis.
- **cold-email-copywriting**: Use the winning copy playbook output as input for creating new variants to test.
- **cold-email-strategy**: Use optimization recommendations to redesign sequence architecture.

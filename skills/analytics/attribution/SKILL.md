---
name: attribution
description: >-
  Attribution playbook for GTM agents — strategy, workflow, templates, operating
  guidance, and quality checks. Use when the user asks for attribution work,
  implementation help, or an agent-ready deliverable.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: analytics
  tags: [attribution, multi-touch, utm, roi, channel, marketing-analytics, campaign-roi]
  related_skills: [campaign-analytics, gtm-metrics, pipeline-management, crm-integration]
  frameworks: [Bizible Multi-Touch Attribution, Google Analytics Attribution, Full Circle Insights]
---
# Attribution

## Overview

Attribution answers the existential marketing question: which of our activities actually produce revenue? The core principle is that single-touch attribution lies. First-touch attribution over-credits awareness channels. Last-touch attribution over-credits bottom-of-funnel conversion channels. Both lead to systematically bad investment decisions — over-funding channels that appear in the credited position and starving channels that create the conditions for conversion.

The non-obvious rule: the "best" attribution model depends on your GTM motion. Product-led growth companies should weight product-qualified signals higher. Sales-led companies should weight sales engagement higher. Channel-led companies should weight partner influence. There is no universal attribution model — only the model that matches how your customers actually buy.

This skill produces: a Multi-Touch Attribution Model Report comparing 4-6 attribution models on revenue credit allocation, channel ROI calculations with cost and revenue attribution, a UTM governance framework with taxonomy and enforcement rules, a source-of-truth reporting structure, and optimization recommendations for budget reallocation.

## When to Use

- User says "attribution" or "attribution model" → activate this skill
- User asks "which channel generates the most revenue" → use this skill
- User says "marketing ROI" or "campaign ROI" → attribution is required
- User mentions "UTM tracking" or "UTM hygiene" or "UTM parameters" → use UTM governance module
- User asks "how do I measure multi-touch attribution" → implement a model
- User says "source of truth reporting" or "marketing and sales disagree on numbers" → use this skill
- Trigger phrases: attribution modeling, multi-touch, first-touch, last-touch, channel attribution, campaign ROI, marketing ROI, UTM parameters, tracking governance

Do NOT use for:
- Campaign-level analytics (open rates, reply rates, meeting rates) → use campaign-analytics
- Pipeline management and forecasting → use pipeline-management
- A/B testing methodology → use a-b-testing
- CRM data architecture → use crm-integration
- Real-time channel monitoring and alerting → use proactive-alerts

## Authoritative Foundations

This skill draws from the following established methodologies:

- **Bizible (Marketo/Marketo Measure) — Multi-Touch Attribution** — The most widely deployed B2B multi-touch attribution system. Bizible's model maps every marketing and sales touch across the customer journey, weighting touches based on position (FT, LC, even, U-shaped, W-shaped, custom). Acquired by Adobe/Marketo, it's the enterprise standard.

- **Full Circle Insights (Salesforce-native)** — Attribution built inside the CRM rather than appended to it. The implicit criticism of marketing-platform-first attribution is that it misses sales touches. Full Circle captures both marketing and sales activity within the CRM.

- **Google Analytics — Attribution Models** — The most accessible attribution implementation, now with data-driven attribution as the default in GA4. Google's shift from rules-based to machine-learning-based attribution reflects the industry trend toward algorithmic models.

- **DreamData — B2B Attribution** — Account-based attribution for companies where multiple stakeholders influence a deal. Critical distinction: person-level attribution credits the individual who converted; account-level attribution distributes credit across the buying group.

## Prerequisites

- CRM data with opportunity records including: create date, close date, deal amount, primary campaign source (HubSpot, Salesforce, or Attio)
- Marketing platform data with touch history: email opens, clicks, form fills, content downloads, webinar attendance, ad clicks (Marketo, HubSpot, Pardot, or GA4)
- Sales activity data: calls, emails, meetings logged on opportunities (CRM activity history)
- UTM-tagged URLs across all marketing channels (website, ads, email, social, partner)
- Cost data by channel: total spend per channel per period for ROI calculation
- Recommended: 12+ months of touchpoint data for stable attribution modeling
- Recommended upstream skills: crm-integration (for CRM data architecture), campaign-analytics (for campaign-level metrics)

## Step-by-Step Process

### Phase 1: Intake

Gather required information from the user. Ask all questions at once. Do not proceed until all answers are received.

Required intake questions:

1. **GTM motion**: What is your primary GTM motion? (Product-led growth, sales-led, channel/partner-led, marketing-led, hybrid?)
2. **Average sales cycle**: How long from first touch to closed-won? (30 days, 90 days, 180 days, 12+ months?) This determines the lookback window.
3. **Buying group size**: How many people typically influence a purchase? (Single decision-maker, 3-5 person committee, 6+ enterprise buying group?) Determines person-level vs account-level attribution.
4. **Channel mix**: What channels are active? (Outbound email, inbound/content, paid ads, events, partners, referrals, social, direct, product-led?)
5. **Data sources**: Where are touchpoints tracked? (CRM, marketing automation, product analytics, ad platforms, webinar platform?)
6. **Current attribution**: What attribution model, if any, is currently in use? What metrics does marketing currently report? What does sales report?
7. **UTM status**: Are UTMs consistently applied? Is there a UTM taxonomy documented? Who enforces it?
8. **Budget data**: Can you provide spend data by channel for the analysis period?

### Phase 2: UTM Governance and Hygiene Audit

UTM parameters are the foundation of attribution accuracy. Bad UTMs = bad attribution.

1. **UTM taxonomy design** — enforce the standard 5 parameters:
   - `utm_source`: The platform/site sending traffic (google, linkedin, hubspot, marketo, outreach). Must be a controlled value from an approved list.
   - `utm_medium`: The marketing medium (cpc, organic_social, email, display, referral, partner, event). Must be a controlled value.
   - `utm_campaign`: The specific campaign name. Use a consistent naming convention: `[quarter]-[channel]-[audience]-[offer]-[variant]`. Example: `q1-2024-email-enterprise-compliance-toolkit-v2`.
   - `utm_content`: What was clicked (cta-text, banner-blue, subject-line-test-a). Used for A/B testing within campaigns.
   - `utm_term`: Search keywords (only for paid search). Optional.

2. **UTM hygiene audit** — scan all URLs for common errors:
   - Missing `utm_source` (most common error — without it, traffic is "direct")
   - Inconsistent source naming: "linkedin," "LinkedIn," "linkedin.com," "LinkedIn Ads" are 4 different sources.
   - Using `utm_medium=cpc` for non-paid traffic
   - Spaces in UTM values (should use hyphens or underscores, never spaces)
   - Case sensitivity: UTM values are case-sensitive. "Google" ≠ "google."
   - Campaign parameter used as catch-all (same utm_campaign across multiple channels)
   - Missing utm_campaign (leaves traffic unassigned to any campaign for ROI calculation)
   - URL shorteners stripping UTM parameters (bit.ly, ow.ly strip by default — configure to preserve)
   - Internal links tagged with UTM parameters (overwrites real attribution data)

3. **UTM governance rules** — document and enforce:
   - All outbound links from marketing must have at minimum: utm_source, utm_medium, utm_campaign.
   - Source values must come from pre-approved list (requires request to add new source).
   - Medium values must come from 10 standard categories.
   - Campaign naming convention is mandatory and validated at URL creation.
   - Marketing automation platforms must auto-append UTMs (configure at the platform level).
   - Sales-provided links should use a different tracking parameter (or UTM with sales-specific source) to distinguish sales vs marketing influence.

4. **UTM data quality score** — calculate for the analysis period:
   - % of revenue-attributed opportunities with complete UTM data: target >90%
   - % of website sessions with utm_source: target >80%
   - % of campaign spend assigned to specific campaigns via UTM: target >95%
   - If scores are below targets, attribution modeling will be unreliable. Fix UTM hygiene first.

### Phase 3: Touchpoint Data Assembly

Build the unified touchpoint timeline:

1. **Define the touchpoint taxonomy** — categorize every interaction:
   - **Marketing touches**: Email click, content download, webinar attendance, ad click, website visit, form fill, social engagement, event booth visit.
   - **Sales touches**: Sales email, sales call, meeting held, demo delivered, proposal sent, LinkedIn connection/inmail.
   - **Product touches**: Signup, activation event, invite team member, upgrade feature usage, PQL trigger.
   - **Partner touches**: Partner referral, co-marketing event, marketplace listing click.

2. **Build touchpoint timelines** for each opportunity:
   - For every closed-won and closed-lost opportunity, assemble all touchpoints from first interaction to close date.
   - Each touchpoint records: timestamp, channel, touch type, campaign association, and whether it was marketing or sales initiated.
   - For account-level attribution: roll up all contacts under the account and create a merged timeline.

3. **Define the attribution window (lookback period)**:
   - Standard: 90 days for SMB (shorter sales cycles), 180 days for mid-market, 365 days for enterprise.
   - Custom window: if your average sales cycle is 120 days, use 120-day lookback.
   - Touches outside the window are excluded from attribution but recorded for awareness contribution analysis.

4. **Handle anonymous-to-known matching**:
   - Website visits before form fill are anonymous. Use cookie-based matching (Google Analytics User ID, HubSpot cookie) if available.
   - If no matching possible, note the gap in data and acknowledge that early-stage awareness touches may be undercounted.

### Phase 4: Multi-Touch Attribution Model Construction

Build and compare multiple attribution models:

**Model 1: First-Touch Attribution**
- 100% of credit to the very first touch.
- Best for: understanding which channels create awareness and initial interest.
- Worst for: understanding which channels close deals.
- Bias: over-credits top-of-funnel channels (content, social, ads).

**Model 2: Last-Touch Attribution**
- 100% of credit to the touch immediately before opportunity creation or deal close.
- Best for: understanding which channels drive conversion.
- Worst for: understanding the full buyer journey.
- Bias: over-credits bottom-of-funnel channels (direct, branded search, sales outreach).

**Model 3: Linear Attribution**
- Equal credit distributed across all touches.
- Example: 10 touches = 10% credit each.
- Best for: balanced view when all touches are considered equally valuable.
- Worst for: companies where certain touches (demo, trial) are objectively more influential.
- Bias: over-credits high-frequency, low-value touches (email opens) and under-credits high-effort, high-value touches (in-person meetings).

**Model 4: Time-Decay Attribution**
- Credit increases exponentially as touches get closer to conversion.
- Example: 7-day half-life means a touch 14 days before close gets 4x the credit of a touch 28 days before close.
- Best for: long sales cycles where recency strongly correlates with influence.
- Worst for: short sales cycles or when early-stage education is critical.
- Bias: similar to last-touch but less extreme. Still under-credits awareness.

**Model 5: U-Shaped (Position-Based) Attribution**
- 40% to first touch, 40% to lead conversion touch (or last touch), 20% distributed evenly across middle touches.
- Best for: B2B where both awareness creation and conversion are critical.
- Worst for: transactional sales where middle touches are important (evaluation, demo).
- The 40/40/20 split is common but arbitrary. Test 30/30/40 or 35/35/30 splits.

**Model 6: W-Shaped Attribution**
- 30% to first touch, 30% to lead creation touch, 30% to opportunity creation touch, 10% distributed across remaining touches.
- Best for: complex enterprise B2B with distinct buying stages (awareness → consideration → decision).
- Requires clean data on when each milestone occurred.

**Model 7 (Advanced): Custom Weighted / Algorithmic Attribution**
- Use machine learning (Shapley values, Markov chains) to determine touch weights from historical data.
- Best for: companies with 500+ closed-won deals and reliable touch data.
- Available in: Google Analytics 4 (data-driven attribution), Bizible, DreamData, CaliberMind.
- If implementing custom: use logistic regression with conversion as the dependent variable and touch channel counts as independent variables to estimate channel coefficients.

### Phase 5: Model Comparison and Selection

Compare attribution models side by side:

1. **Revenue attribution by channel** across all models:
   - Create a matrix: channels as rows, models as columns, cell = % of total revenue attributed.
   - Calculate variance: for each channel, what's the range between the most and least generous model?
   - Channels with wide variance are sensitive to model choice — important to get right.
   - Channels with narrow variance are robust — model choice doesn't matter much.

2. **Model selection criteria**:
   - **GTM motion fit**: Sales-led → W-shaped or U-shaped (both marketing and sales get credit). Product-led → time-decay (product activation signals should weight highest). Marketing-led → linear or U-shaped (full funnel view).
   - **Data completeness**: If you can't reliably identify first touch (cookie gaps, long history), don't use first-touch or U-shaped. If you can't identify lead creation moment, don't use W-shaped.
   - **Stakeholder alignment**: The model both marketing and sales agree on is better than the "correct" model only marketing trusts. Attribution is as much political as analytical.
   - **Simplicity**: A linear model that everyone understands and acts on beats a custom algorithmic model that nobody trusts or can explain.

3. **Recommend a primary model** with justification. Also report 1-2 comparison models so stakeholders see the sensitivity.

### Phase 6: Channel ROI Calculation

Calculate return on investment by channel:

1. **Channel cost assembly** — collect all costs per channel:
   - People cost: fully loaded salary for team members dedicated to the channel
   - Media spend: ad spend, sponsorship, content promotion
   - Tool cost: channel-specific tools (Apollo for outbound, SEMrush for SEO, webinar platform)
   - Content cost: content created specifically for the channel
   - Agency/vendor cost: external support for the channel
   - Event cost: travel, booth, sponsorship, swag for event channel

2. **Channel revenue attribution** — using the selected primary model:
   - For each channel, sum attributed revenue from closed-won deals in the analysis period.
   - Separate new customer revenue from expansion revenue (different channels may drive each).

3. **Channel ROI calculation**:
   ```
   Channel ROI = (Attributed Revenue - Channel Cost) ÷ Channel Cost
   ```
   Express as ratio (3:1) or percentage (300%).

4. **Channel CAC calculation**:
   ```
   Channel CAC = Total Channel Cost ÷ New Customers Attributed to Channel
   ```
   Compare to company-wide CAC. Channels with >2x company-wide CAC are inefficient.

5. **Channel efficiency metrics**:
   - Cost per opportunity: channel cost ÷ opportunities attributed
   - Cost per meeting: channel cost ÷ meetings attributed (if meetings are trackable)
   - Pipeline efficiency: attributed pipeline value ÷ channel cost
   - Time to payback: average months to recover channel cost from attributed revenue

6. **Assisted vs unassisted conversion** (critical distinction):
   - **Assisted conversions**: channel appeared in the touch history but wasn't the primary-attributed channel. These channels "assist" other channels in closing.
   - **Unassisted conversions**: channel appeared and was the primary-attributed channel.
   - Channels with high assist ratio (content, social) are undervalued by last-touch. Channels with low assist ratio (branded search, direct) are overvalued.
   - Report both to show the full channel contribution story.

### Phase 7: Source-of-Truth Reporting

Build the reporting structure that all teams align around:

1. **Single source of truth** — designate one system as authoritative:
   - CRM for revenue numbers (opportunities, deal amounts, close dates)
   - Marketing automation for campaign costs and marketing touches
   - Unified attribution report for channel credit allocation
   - Document the data flow: which system feeds which metric

2. **Reporting cadence and audience**:
   - Weekly: marketing team — channel performance dashboards (leads, MQLs, opportunities created)
   - Monthly: marketing + sales leadership — opportunity-level attribution, channel ROI
   - Quarterly: executive team + board — revenue attribution by channel, cost per acquisition trends, model comparison

3. **Dashboard design** for source-of-truth:
   - **Channel Contribution View**: pie/bar chart showing revenue attribution by channel under the primary model.
   - **Channel Efficiency View**: scatter plot of channels with ROI on Y-axis and total revenue on X-axis. Bubble size = total cost. Upper right quadrant: high ROI, high revenue = invest more. Lower left: low ROI, low revenue = fix or cut.
   - **Trend View**: month-over-month revenue attribution by channel. Identify channels that are growing or declining in contribution.
   - **Model Comparison View**: table showing attribution % by channel across 5 models. Shows sensitivity to model choice.
   - **Assist Ratio View**: bar chart showing assisted vs unassisted conversions by channel.

4. **Alignment meeting structure** — Marketing Ops and Sales Ops quarterly alignment:
   - Review attribution model: is it still fit for purpose?
   - Audit UTM hygiene: is data quality improving or degrading?
   - Discuss anomalies: any deals with unusual attribution (e.g., 30 touches across 5 channels)?
   - Agree on channel investment changes based on attribution data
   - Document decisions and update attribution rules

## Output Format

The agent should produce output in this structure:

```markdown
# Multi-Touch Attribution Report
**Period:** [Q1 2024] | **Model:** [U-Shaped, primary] | **Lookback:** [90 days]

## UTM Health Score
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Revenue opps with complete UTM | X% | >90% | 🟢/🟡/🔴 |
| Sessions with utm_source | X% | >80% | 🟢/🟡/🔴 |
| Campaign spend tagged | X% | >95% | 🟢/🟡/🔴 |

## Model Comparison: Revenue Attribution by Channel
| Channel | First-Touch | Last-Touch | Linear | Time-Decay | U-Shaped | W-Shaped | Variance |
|---------|------------|------------|--------|------------|----------|----------|----------|
| Content/SEO | 35% | 8% | 22% | 12% | 28% | 25% | 27pp |
| Paid Ads | 20% | 15% | 18% | 14% | 17% | 16% | 6pp |
| Outbound | 10% | 30% | 18% | 28% | 18% | 20% | 20pp |
| Events | 15% | 10% | 14% | 11% | 13% | 12% | 5pp |
| Partners | 8% | 22% | 15% | 20% | 13% | 15% | 14pp |
| Direct/Brand | 12% | 15% | 13% | 15% | 11% | 12% | 4pp |

## Channel ROI (Primary Model: U-Shaped)
| Channel | Attributed Revenue | Total Cost | ROI | CAC | CAC vs Avg | Status |
|---------|-------------------|------------|-----|-----|-----------|--------|
| Content/SEO | $X | $X | X:X | $X | +/-% | 🟢/🟡/🔴 |
| Paid Ads | $X | $X | X:X | $X | +/-% | 🟢/🟡/🔴 |
| Outbound | $X | $X | X:X | $X | +/-% | 🟢/🟡/🔴 |
| Events | $X | $X | X:X | $X | +/-% | 🟢/🟡/🔴 |
| Partners | $X | $X | X:X | $X | +/-% | 🟢/🟡/🔴 |

## Assisted Conversion Analysis
| Channel | Unassisted | Assisted | Assist Ratio | Interpretation |
|---------|-----------|----------|-------------|----------------|
| Content/SEO | X | Y | Y/(X+Y) | High assist — undervalued by last-touch |
| Outbound | X | Y | Y/(X+Y) | Low assist — self-sufficient channel |

## Recommendations
1. **Increase investment in [channel]** — highest ROI, under-invested relative to contribution
2. **Optimize or reduce [channel]** — below-average ROI, investigate efficiency
3. **Fix UTM governance for [channel]** — incomplete data limits attribution accuracy
4. **Add [model element]** — consider W-shaped for enterprise segment specific reporting

## Appendix
- Full UTM audit findings
- Model methodology notes
- Data quality exceptions
```

## Quality Check

Before delivering, verify:

- [ ] Has UTM hygiene been audited and scored before attribution modeling?
- [ ] Are at least 4 attribution models compared, not just one "preferred" model?
- [ ] Does the model selection align with the company's GTM motion and sales cycle?
- [ ] Are channel costs fully loaded (people + media + tools + content)?
- [ ] Is the assist ratio reported to show channels undervalued by the primary model?
- [ ] Is there a clear source-of-truth designation and data governance plan?
- [ ] Are attribution model limitations acknowledged (cookie gaps, offline touches, time windows)?
- [ ] Would both marketing and sales leadership trust these numbers?

## Common Pitfalls

1. **Using last-touch attribution for everything.** Last-touch gives 100% credit to the final touch. For B2B with 6-month sales cycles and 10+ touches, this systematically credits your CRM/branded-search/outbound and zeroes out your content, events, and awareness channels. You then "optimize" by cutting the channels that created the conditions for conversion. This is the single most expensive attribution error.

2. **Building attribution without UTM governance.** If your UTM data is inconsistent, missing, or duplicated, no attribution model can produce reliable results. Attribution quality is bounded by UTM quality. Fix UTM hygiene first, then model.

3. **Selecting an attribution model without stakeholder buy-in.** The "correct" attribution model that marketing uses but sales ignores creates organizational dysfunction. Better to use a slightly suboptimal model that both teams trust than an optimal model that one team dismisses. Involve sales leadership in model selection.

4. **Ignoring offline touches.** Events, phone calls, in-person meetings, and direct mail often don't have digital tracking. If these are significant in your GTM motion, your attribution data is incomplete. Add manual touch logging or proxy metrics (e.g., "event attendee → opportunity created within 30 days" as a rule-based attribution).

5. **Not handling multi-person buying groups.** Person-level attribution credits the individual who converted, but in enterprise B2B, 5-10 people influence the decision. If you only attribute to the contact who became the opportunity, you miss the influence of the champion, the economic buyer, and the technical evaluator. Use account-level attribution for enterprise.

6. **Attribution windows too short or too long.** Too short: you miss early-stage touches that educated the buyer (especially for long sales cycles). Too long: you credit touches from 18 months ago that are no longer relevant. Set the window based on your actual sales cycle data (90th percentile time from first touch to close for won deals).

7. **Treating attribution as a one-time setup.** Attribution models should be reviewed quarterly. Channel mix changes, buyer behavior evolves, campaign types shift. A model built on 2023 data may be wrong for 2024. Schedule quarterly model reviews.

## Related Skills

- **campaign-analytics**: Use campaign-level metrics to validate attribution model outputs. If attribution says email drives 50% of revenue but campaign analytics shows low meeting rates, investigate.
- **gtm-metrics**: CAC by channel from this skill feeds into the overall GTM efficiency dashboard.
- **pipeline-management**: CRM data quality directly impacts attribution accuracy. Ensure pipeline data is clean.
- **crm-integration**: Proper CRM architecture is required for touchpoint tracking. Marketing and sales touches must be unified.
- **proactive-alerts**: Attribution anomalies (channel performance sudden drops/spikes) can trigger alerts.
- **landing-pages**: Landing page conversion tracking requires clean UTM attribution to measure campaign effectiveness.

# GTM Skills — Common Pitfalls Index

Auto-generated from skill `## Common Pitfalls` sections. **1032 pitfalls** across **205** skills (205 total). Regenerate: `npm run build`.

Agents: load the source skill for full context, fixes, and quality checks — this index is for discovery and cross-skill pattern matching.

Master router: `skills/foundation/using-gtm-skills/SKILL.md` · Expert catalog: `references/experts.md`

## abm

### [abm-1-to-1](skills/abm/abm-1-to-1/SKILL.md)

- **Treating ABM as a marketing-only initiative.** — ABM requires tight sales alignment. Without BDRs assigned to specific accounts and shared account briefs, marketing produces content nobody uses. Fix: weekly ABM standups with marketing + BDRs + AEs.
- **One-size-fits-all tiering.** — Applying the same playbook to Tier 1 and Tier 3 accounts. Fix: Tier 1 gets custom content and executive engagement; Tier 3 gets automated personalization.
- **Measuring ABM on MQLs.** — ABM success is pipeline from target accounts, not lead volume. Fix: track coverage %, engagement depth, pipeline created, and win rate by tier.

### [abm-1-to-few](skills/abm/abm-1-to-few/SKILL.md)

- **Treating ABM as a marketing-only initiative.** — ABM requires tight sales alignment. Without BDRs assigned to specific accounts and shared account briefs, marketing produces content nobody uses. Fix: weekly ABM standups with marketing + BDRs + AEs.
- **One-size-fits-all tiering.** — Applying the same playbook to Tier 1 and Tier 3 accounts. Fix: Tier 1 gets custom content and executive engagement; Tier 3 gets automated personalization.
- **Measuring ABM on MQLs.** — ABM success is pipeline from target accounts, not lead volume. Fix: track coverage %, engagement depth, pipeline created, and win rate by tier.

### [abm-1-to-many](skills/abm/abm-1-to-many/SKILL.md)

- **Treating ABM as a marketing-only initiative.** — ABM requires tight sales alignment. Without BDRs assigned to specific accounts and shared account briefs, marketing produces content nobody uses. Fix: weekly ABM standups with marketing + BDRs + AEs.
- **One-size-fits-all tiering.** — Applying the same playbook to Tier 1 and Tier 3 accounts. Fix: Tier 1 gets custom content and executive engagement; Tier 3 gets automated personalization.
- **Measuring ABM on MQLs.** — ABM success is pipeline from target accounts, not lead volume. Fix: track coverage %, engagement depth, pipeline created, and win rate by tier.

### [abm-strategy](skills/abm/abm-strategy/SKILL.md)

- **Treating ABM as a marketing-only initiative.** — ABM requires tight sales alignment. Without BDRs assigned to specific accounts and shared account briefs, marketing produces content nobody uses. Fix: weekly ABM standups with marketing + BDRs + AEs.
- **One-size-fits-all tiering.** — Applying the same playbook to Tier 1 and Tier 3 accounts. Fix: Tier 1 gets custom content and executive engagement; Tier 3 gets automated personalization.
- **Measuring ABM on MQLs.** — ABM success is pipeline from target accounts, not lead volume. Fix: track coverage %, engagement depth, pipeline created, and win rate by tier.

### [account-selection](skills/abm/account-selection/SKILL.md)

- **Treating ABM as a marketing-only initiative.** — ABM requires tight sales alignment. Without BDRs assigned to specific accounts and shared account briefs, marketing produces content nobody uses. Fix: weekly ABM standups with marketing + BDRs + AEs.
- **One-size-fits-all tiering.** — Applying the same playbook to Tier 1 and Tier 3 accounts. Fix: Tier 1 gets custom content and executive engagement; Tier 3 gets automated personalization.
- **Measuring ABM on MQLs.** — ABM success is pipeline from target accounts, not lead volume. Fix: track coverage %, engagement depth, pipeline created, and win rate by tier.

### [multi-thread-orchestration](skills/abm/multi-thread-orchestration/SKILL.md)

- **Treating ABM as a marketing-only initiative.** — ABM requires tight sales alignment. Without BDRs assigned to specific accounts and shared account briefs, marketing produces content nobody uses. Fix: weekly ABM standups with marketing + BDRs + AEs.
- **One-size-fits-all tiering.** — Applying the same playbook to Tier 1 and Tier 3 accounts. Fix: Tier 1 gets custom content and executive engagement; Tier 3 gets automated personalization.
- **Measuring ABM on MQLs.** — ABM success is pipeline from target accounts, not lead volume. Fix: track coverage %, engagement depth, pipeline created, and win rate by tier.

### [strategic-gifting](skills/abm/strategic-gifting/SKILL.md)

- **Sendoso without strategy.** — Automated Starbucks cards to cold lists. Fix: ABM tier + Giftology brief first.
- **Logo swag.** — Fix: Ruhlin — no logo on relationship gifts.
- **Gift to unstick deal.** — Fix: JOLT / deal desk — business problem.
- **Ignore gift cap.** — Fix: ask champion; log in CRM.
- **No follow-up.** — Gift arrives; nobody calls. Fix: 24h SLA + task in CRM.
- **Same gift Tier 1 and Tier 3.** — Fix: `references/gifting-by-tier.md`.

## analytics

### [1p-tagging-pixels](skills/analytics/1p-tagging-pixels/SKILL.md)

- **Client-side only.** — 30-40% of browser events are lost to ad blockers. Server-side captures 100%. Implement server-side tagging before scaling ad spend.
- **No UTM standardization.** — "linkedin", "LinkedIn", "li", "lnkd" are four different sources in analytics. One naming convention, enforced.
- **Tracking without consent.** — GDPR fines up to 4% of global revenue. Implement consent before tracking EU visitors.
- **Pixel duplication.** — Same pixel fired twice = double-counted conversions. Audit quarterly with browser dev tools.
- **3P dependency without 1P transition.** — 3P data is dying. 1P data is the future. Run both now, actively build 1P infrastructure.

### [a-b-testing](skills/analytics/a-b-testing/SKILL.md)

- **Peeking and early stopping.** — This is the most common and most damaging A/B testing error. Checking results daily and stopping when they "look significant" inflates false positive rates from 5% to 25-30%. Set a fixed end date and DO NOT look at primary metric results until it arrives. The math of statistical tests assumes a fixed sample size — peeking violates this assumption.
- **Testing for statistical significance on vanity metrics.** — A subject line test that produces a statistically significant 15% open rate improvement but zero change in reply rate is a bad test. You optimized a metric that doesn't drive revenue. Always designate a downstream metric (reply rate, meeting rate, conversion) as the primary metric and optimize for that.
- **Insufficient sample size.** — Running a test with 100 sends per variant when you need 2,000 to detect the expected effect. Results will be noisy and misleading. If you cannot achieve the required sample size, either increase the MDE (test bigger changes), reduce variants, or don't run the test. A decision made on insufficient data is worse than no decision.
- **No control group.** — Testing Variant A vs Variant B without a control tells you which is relatively better but not whether either is better than what you're currently doing. Both could be worse than the baseline. Always include a control.
- **Multiple comparisons without correction.** — Running a test with 5 variants and declaring significance whenever any variant's p < 0.05 gives a ~23% chance of at least one false positive. Apply Bonferroni correction (divide significance threshold by number of comparisons) or use a different framework (ANOVA for 3+ variants).
- **Confusing statistical significance with practical significance.** — With large enough sample sizes, even trivial differences become statistically significant. A 0.1% improvement in reply rate with p < 0.001 is statistically significant but practically useless. Always ask: "Is the effect size large enough to justify the change?"
- **Not segmenting results.** — A variant that wins overall might be losing in your highest-value segment. An overall "win" of +10% enterprise reply rate vs -5% SMB reply rate might be a net negative for enterprise-focused companies. Always segment by at least ICP tier and persona.
- **Running tests without a hypothesis.** — "Let's just test some different subject lines and see what happens" is experimentation theater, not experimentation. Every test needs a hypothesis grounded in a behavioral rationale. Test results should update your understanding, not just tell you which random variant happened to win.

### [attribution](skills/analytics/attribution/SKILL.md)

- **Using last-touch attribution for everything.** — Last-touch gives 100% credit to the final touch. For B2B with 6-month sales cycles and 10+ touches, this systematically credits your CRM/branded-search/outbound and zeroes out your content, events, and awareness channels. You then "optimize" by cutting the channels that created the conditions for conversion. This is the single most expensive attribution error.
- **Building attribution without UTM governance.** — If your UTM data is inconsistent, missing, or duplicated, no attribution model can produce reliable results. Attribution quality is bounded by UTM quality. Fix UTM hygiene first, then model.
- **Selecting an attribution model without stakeholder buy-in.** — The "correct" attribution model that marketing uses but sales ignores creates organizational dysfunction. Better to use a slightly suboptimal model that both teams trust than an optimal model that one team dismisses. Involve sales leadership in model selection.
- **Ignoring offline touches.** — Events, phone calls, in-person meetings, and direct mail often don't have digital tracking. If these are significant in your GTM motion, your attribution data is incomplete. Add manual touch logging or proxy metrics (e.g., "event attendee → opportunity created within 30 days" as a rule-based attribution).
- **Not handling multi-person buying groups.** — Person-level attribution credits the individual who converted, but in enterprise B2B, 5-10 people influence the decision. If you only attribute to the contact who became the opportunity, you miss the influence of the champion, the economic buyer, and the technical evaluator. Use account-level attribution for enterprise.
- **Attribution windows too short or too long.** — Too short: you miss early-stage touches that educated the buyer (especially for long sales cycles). Too long: you credit touches from 18 months ago that are no longer relevant. Set the window based on your actual sales cycle data (90th percentile time from first touch to close for won deals).
- **Treating attribution as a one-time setup.** — Attribution models should be reviewed quarterly. Channel mix changes, buyer behavior evolves, campaign types shift. A model built on 2023 data may be wrong for 2024. Schedule quarterly model reviews.

### [campaign-analytics](skills/analytics/campaign-analytics/SKILL.md)

- **Skipping Layer 1 diagnosis.** — The most common mistake: jumping to copy fixes when deliverability is the real problem. Always start at Layer 1. If delivery rate is below 95%, nothing you do to copy matters until that's fixed. You can have the world's best email — if it lands in spam, nobody reads it.
- **Over-indexing on open rates.** — Open rates are a proxy for subject line effectiveness and sender reputation, not campaign success. A campaign with 80% open rate and 0% reply rate is failing. Optimize for reply rate, meeting rate, and pipeline — the metrics that generate revenue. Open rates matter only as a diagnostic signal.
- **Ignoring statistical significance.** — Comparing two variants where one got 3 replies from 200 sends and another got 2 replies from 200 sends is noise, not signal. Minimum 200 sends per variant before drawing conclusions. Use chi-square or Fisher's exact test to confirm significance at p < 0.05.
- **Benchmarking without context.** — Comparing SMB outbound reply rates to enterprise benchmarks (or vice versa) produces misleading conclusions. Always match benchmarks to ACV range, buyer persona seniority, and channel. A 2% reply rate to C-level enterprise prospects can be excellent; a 2% reply rate to SMB managers is poor.
- **Treating metrics as independent.** — Open rate, reply rate, and meeting rate are a chain. Improving open rates through clickbait subject lines often reduces reply rates because the email content doesn't match expectations. Optimize holistically — the combination that produces the highest meeting rate, not the highest individual metric.
- **Optimizing for the wrong time horizon.** — Campaign performance varies seasonally (Q4 holidays, summer slowdown, end-of-quarter urgency). Comparing week-over-week without accounting for seasonal patterns leads to false signals. Use 4-week rolling averages and compare to same-period-last-year where data exists.
- **Neglecting reply sentiment analysis.** — Counting replies without reading them is dangerous. A campaign generating 5% reply rate where 80% of replies are "unsubscribe" or "wrong person" is worse than a 1% reply rate with 100% positive sentiment. Always categorize replies: positive (interested), neutral (info request, not now), negative (unsubscribe, wrong person, complaint).

### [deliverability-monitoring](skills/analytics/deliverability-monitoring/SKILL.md)

- **Monitoring only bounce rate.** — Bounce rate tells you about list quality, not reputation. A domain can have 0% bounce rate and 100% spam placement. Always combine bounce tracking with spam placement testing and blacklist monitoring. Bounce rate is necessary but insufficient.
- **Ignoring Google Postmaster Tools.** — Google delivers to approximately 50% of B2B inboxes. If you're not monitoring Google Postmaster Tools, you're flying blind on half your deliverability. Setup takes 5 minutes (DNS TXT verification). The data is free and authoritative — it comes directly from Google.
- **Reacting instead of trending.** — Blacklistings don't happen instantly — complaint rates rise over days to weeks before listing. Monitoring trends (rising complaints, declining open rates by provider, increasing block rates) lets you intervene before blacklisting occurs. Set trend-based alerts, not just threshold-based ones.
- **Treating all blacklists equally.** — Spamhaus SBL listing will cripple deliverability immediately. A listing on a minor blacklist with few downstream consumers may have zero impact. Prioritize remediation based on blacklist impact, not just listing count. Better to be on 3 minor blacklists than 1 Spamhaus listing.
- **DMARC `p=reject` without understanding forwarding impact.** — Moving to `p=reject` before analyzing forwarding patterns will break legitimate email delivery through mailing lists, forwarding services, and some corporate email forwarding rules. Analyze DMARC reports for at least 30 days at `p=none` before considering stricter policies.
- **Not isolating cold sending domains.** — Using the same domain for cold outreach and transactional email means a reputation hit from cold outreach takes down password resets, invoices, and product notifications. This is the single most common deliverability catastrophe. Always separate sending domains by purpose.
- **Misdiagnosing low open rates.** — Low open rates can be caused by spam placement (invisible to open tracking), image blocking (open pixel doesn't load), Apple Mail Privacy Protection (pre-fetches all images, inflating open rates), or genuinely uninterested recipients. Cross-reference with click rates, reply rates, and seed-list tests to determine actual cause.

### [event-analytics](skills/analytics/event-analytics/SKILL.md)

- **Tracking everything.** — 500 events, 50 properties each, no one knows what any of them mean. The data swamp. Fix: Every event must have a purpose. Start with 20. Add as needed.
- **Inconsistent naming.** — `signed_up`, `userSignup`, `Sign Up Completed` all describe the same thing across different systems. Fix: One taxonomy. Object- action. Past tense. Documented in an event dictionary.
- **Client-side only tracking.** — Ad blockers block client-side tracking (30-50% of users). Critical events lost. Fix: Server-side tracking for key events (signup, payment, subscription changes). Client-side for behavioral events.
- **No group/account context for B2B.** — Events tracked to individual users but not linked to their company workspace. Can't answer "what are our top 10 accounts doing?" Fix: `group()` call on login linking user to workspace.
- **PII in event properties.** — `email: "john@company.com"` in event properties is a data privacy violation waiting to happen. Fix: Use user IDs. Store PII in your database, not your event pipeline.

### [growth-experimentation](skills/analytics/growth-experimentation/SKILL.md)

- **Tests too large** — — redesigning entire onboarding (4 weeks to build) loses to testing a single screen change (2 days). Small tests = fast learning.
- **No learning repository** — — running 50 experiments without documenting learnings is running the same test twice. Document everything.
- **Statistical ignorance** — — calling a test at 70% confidence produces false positives. Wait for 95%+ confidence.
- **Winner's bias** — — only shipping winners without understanding losers means you don't know why things work.

### [gtm-metrics](skills/analytics/gtm-metrics/SKILL.md)

- **Calculating LTV without gross margin.** — Raw-revenue LTV (ARPA ÷ churn) overstates value by 15-30% because it ignores COGS. Contribution-margin LTV is what matters. Investors will recalculate using gross margin — if your number doesn't match, you lose credibility.
- **Using unloaded CAC.** — Including only ad spend or tool costs in CAC while ignoring fully loaded salaries and benefits dramatically understates true acquisition cost. A "CAC" of $500 that should be $2,500 leads to terrible unit economics decisions. Include every dollar spent on acquiring customers.
- **Mixing monthly and annual metrics.** — CAC calculated from quarterly spend but divided by monthly new customers gives nonsensical results. Always align the time periods. Use quarterly or trailing 12-month CAC for stability.
- **Comparing NRR across different segments.** — SMB NRR benchmarks (100%+ good) and enterprise NRR benchmarks (120%+ good) are completely different scales. Comparing an SMB company's NRR to enterprise benchmarks creates false panic or false confidence.
- **Interpreting Magic Number without considering sales cycle.** — If your sales cycle is 6+ months, comparing current quarter ARR to previous quarter S&M spend understates efficiency. The spend from 2-3 quarters ago generated this quarter's ARR. Use lagged Magic Number for enterprise.
- **Treating Rule of 40 as a precise metric.** — Rule of 40 is a heuristic, not a law of physics. A company with 100% growth and -40% margin (score: 60) may be burning unsustainably. A company with 10% growth and 35% margin (score: 45) may be a better long-term business. Always pair Rule of 40 with qualitative assessment.
- **Reporting metrics without cohort context.** — "NRR improved from 95% to 105%" sounds great — unless the improvement is because you stopped acquiring new customers and only retained the best ones. Cohort analysis reveals whether metric improvements reflect genuine business improvement or composition effects.
- **CRM bookings vs committed MRR.** — Pipeline closed-won TCV ≠ board ARR. Prepay cash ≠ net new MRR. Fix: MRR bridge from billing; reconcile to CRM — `references/saas-mrr-accounting-nuances.md`, `references/benchmark-reconciliation.md`.

### [gtm-system-architecture](skills/analytics/gtm-system-architecture/SKILL.md)

- **Optimizing one model in isolation.** — Improving the Operating Model without fixing the Data Model means adding process to bad data. Fix data first.
- **No Bowtie.** — Treating revenue as a pipeline that ends at "closed won" ignores the 70%+ of lifetime value that comes after the sale.
- **Self-assessment without evidence.** — "I think our Math Model is a 7" without actually calculating LTV:CAC. Score with data, not feelings.
- **Trying to fix everything at once.** — Six-model overhauls take 12-18 months. Sequence one or two per quarter.
- **GTM model owned by one function.** — GTM alignment requires sales, marketing, and CS leadership in the same room with shared metrics.

### [marketing-strategy](skills/analytics/marketing-strategy/SKILL.md)

- **No strategy, just tactics.** — "Let's post on LinkedIn and run some ads" without a channel mix and budget is a tactic list, not a strategy.
- **Too many channels too early.** — A $1M ARR company doesn't need events, programmatic, and TikTok. 2-3 channels done well beats 8 channels done poorly.
- **Marketing-sales misalignment.** — Marketing measured on MQLs, sales measured on closed revenue. Different incentives, different behaviors. Align on pipeline generated, not leads.
- **Brand as an afterthought.** — Brand is the thing that makes outbound reply rates go up, paid CPC go down, and win rates increase. Invest before you need it.

### [paid-advertising](skills/analytics/paid-advertising/SKILL.md)

- **LinkedIn as the only platform.** — LinkedIn gets you targeting but misses intent capture (Google) and retargeting (Meta). Run all three.
- **Not enough budget to test.** — LinkedIn at $1K/mo won't produce meaningful data. Minimum $3K/mo for 6-8 weeks to validate.
- **B2C metrics for B2B.** — Cost per lead is meaningless if those leads don't become pipeline. Measure cost per opportunity and revenue.
- **No retargeting.** — 97% of first-time visitors don't convert. Retargeting captures the other 97%.
- **Creative fatigue.** — Same ad for 6 weeks burns out. Rotate creative every 2-3 weeks. Test multiple variants simultaneously.

### [proactive-alerts](skills/analytics/proactive-alerts/SKILL.md)

- **Alerting on everything.** — A Slack channel with 50 alerts/day becomes invisible. Curate ruthlessly. Only alerts that require action should fire.
- **No owner.** — An alert that goes to a channel with no named owner gets ignored. Every alert type has one person accountable.
- **Alerting without context.** — "Deal X stalled" without "it's been in Demo for 14 days, last contact was a bounce, and the champion changed jobs" doesn't help. Context drives action.
- **Same alert for everyone.** — An SDR doesn't need CRO-level pipeline alerts. Tailor by role or risk burnout.
- **No alert audit.** — Alerts that were urgent 6 months ago may be noise now. Audit monthly and remove or tune.

### [tracking-plan](skills/analytics/tracking-plan/SKILL.md)

- **Tracking without a plan.** — Events fire into the void. No one knows what "button_clicked_3" means. The data is worthless. Fix: Tracking plan document FIRST. Implementation second. Every event has a name, purpose, properties, destinations, and owner.
- **Client-side only.** — Ad blockers block 15-30% of client-side tracking. Critical events (signup, payment, subscription) are lost. Fix: Server-side tracking for revenue-critical events. CDP server-side SDK.
- **Duplicate events.** — Segment fires "Signed Up." GTM also fires "SignUp." GA4 shows 2x signups. Nobody knows which number is real. Fix: One source of truth per event. Audit for duplicates. GTM ONLY handles marketing pixels, not core events.
- **Marketing and product tracking disconnected.** — Marketing sees signups. Product sees activation. Nobody connects the two — can't answer "which marketing channel produces the most activated users?" Fix: Same event taxonomy. Same user_id. CDP routes to both marketing and product tools.
- **No attribution on signup.** — UTM params captured on visit but lost on signup. "Where did this customer come from?" = shrug. Fix: Capture UTM params on first visit. Persist to user profile on signup. Always.
- **PII in event properties.** — `email: "john@company.com"` tracked in every event. This is a privacy violation and a security risk. Fix: Use user_id. Store PII in your database, not your event pipeline. Only `identify()` call carries user traits — regular `track()` calls do not.

## automation

### [ai-sdr-setup](skills/automation/ai-sdr-setup/SKILL.md)

- **Starting with auto-send.** — AI can produce plausible but wrong copy. Fix: draft-only pilot first.
- **Mixed ICP pilot.** — SMB, mid-market, and enterprise require different messages. Fix: one segment per pilot.
- **No suppression logic.** — Agents can accidentally contact customers, competitors, or opted-out contacts. Fix: suppression check before every sequence enrollment.
- **Measuring only activity.** — Emails sent is not success. Fix: track positive replies, meetings, bad-draft rate, and human override rate.
- **No handoff map.** — Agents keep replying when a human should intervene. Fix: hard handoff on positive intent, pricing, security, procurement, or legal.
- **Unverified personalization.** — AI invents reasons to reach out. Fix: require source URL or evidence for every personalized claim.

### [api-enrichment](skills/automation/api-enrichment/SKILL.md)

- **Looping over contacts without idempotency.** — Retries create duplicates. Fix: idempotency keys and upserts.
- **Calling all providers every time.** — Costs explode. Fix: waterfall by stop condition.
- **Overwriting rep-owned fields.** — Enrichment corrupts active deals. Fix: field ownership rules.
- **Silent failures.** — Missing data looks like no match. Fix: explicit error states and dead-letter queue.
- **No freshness rule.** — Old data overwrites newer CRM data. Fix: compare timestamps and source priority.
- **Polling huge jobs.** — Polling wastes compute and API calls. Fix: signed webhooks with retry handling.

### [attio-setup](skills/automation/attio-setup/SKILL.md)

- **Over-building objects.** — Start with Companies, People, Deals. Add custom objects only when these three can't represent what you need.
- **No lists.** — Lists are Attio's superpower. Without them, it's just a spreadsheet. Build lists for every segment and workflow trigger.
- **HubSpot migration without cleanup.** — Moving bad data to Attio is just bad data in a better tool. Clean your data before migrating.
- **API-first without API use.** — Attio's API is the differentiator. Use it for enrichment, automation, and custom integrations.

### [clay-automation](skills/automation/clay-automation/SKILL.md)

- **One giant table.** — Combining company and person data wastes credits and makes re-enrichment impossible. Separate always.
- **Enriching before filtering.** — Running $0.15-0.40/contact enrichment on non-ICP records wastes budget. Filter on cheap data first.
- **Claygent guessing emails.** — Without explicit "do not guess" instructions, Claygent constructs pattern-based emails that bounce at 40-60% rates.
- **Two-way CRM sync.** — Clay-to-CRM should be one direction. CRM-to-Clay sync creates data conflicts. Push only.
- **Clay as permanent storage.** — Clay is a workspace. Push to CRM, archive or delete rows in Clay. Old rows decay just like anywhere else.
- **No credit caps.** — Without caps, a single row can chew through 15+ credits. Cap at 5-6 per row.

### [crm-integration](skills/automation/crm-integration/SKILL.md)

- **Two-way sync everywhere.** — Creates conflicts and loops. Fix: define read/write ownership per tool.
- **Too many required fields.** — Reps stop updating CRM. Fix: require only fields needed for the next stage.
- **No stage exit criteria.** — Pipeline becomes subjective. Fix: write objective exit rules.
- **CRM as the process.** — Tools do not create process. Fix: define process first, configure second.
- **No data freshness.** — Old enriched fields linger forever. Fix: source and timestamp every enrichment field.
- **No lost reason taxonomy.** — Closed-lost learning disappears. Fix: standardized lost reasons with notes.

### [hubspot-setup](skills/automation/hubspot-setup/SKILL.md)

- **No stage criteria.** — "We think they're an MQL" creates chaos. Define hard criteria: "ICP fit confirmed + demo requested = SQL."
- **Too many required fields.** — Reps skip CRM updates when every field is mandatory. Required: Amount, Close Date, Next Step. Everything else optional.
- **Two-way sync with enrichment.** — Clay-enriched data should flow to HubSpot, not back. Two-way sync creates data conflicts.
- **Default HubSpot lifecycle stages.** — Customize stages to your business. "Subscriber" and "Other" don't map to any real process.
- **No data hygiene cadence.** — Quarterly: deduplicate contacts, re-verify emails >90 days old, audit required fields completion.

### [mcp-setup](skills/automation/mcp-setup/SKILL.md)

- **Exposing too many tools.** — Agents choose poorly when tool scope is noisy. Fix: only expose tools needed for the workflow.
- **Write access by default.** — A research agent should not mutate CRM. Fix: read-only first.
- **No confirmation gates.** — Agents can send or enroll by mistake. Fix: require user confirmation for external side effects.
- **Secrets in config.** — Public repos and logs leak keys. Fix: env vars or secret manager.
- **No logging.** — You cannot debug a tool call after the fact. Fix: log every call.
- **Ambiguous tool descriptions.** — Agents misuse tools with overlapping names. Fix: make tool names and descriptions specific.

### [n8n-automation](skills/automation/n8n-automation/SKILL.md)

- **No error handling.** — One failed API call breaks the entire pipeline. Every HTTP Request node needs an error branch.
- **Sequential processing for large batches.** — 10K records at 1 second each is 2.8 hours. Use Split In Batches with parallel execution.
- **No queue.** — Processing 10K records without a pause mechanism means no recovery point if something fails at record 5,000.
- **Credentials in workflow.** — Use built-in credential store, never hardcode API keys in nodes.

### [salesforce-setup](skills/automation/salesforce-setup/SKILL.md)

- **Over-customization before process.** — Custom objects and fields without a defined process create complexity without value. Design the process, then configure Salesforce to support it.
- **No validation rules.** — Close dates in the past, $0 opportunities, blank required fields. Validation rules enforce data quality.
- **Process Builder instead of Flows.** — Process Builder is deprecated. Migrate everything to Flows.
- **Lead assignment without enrichment.** — Routing an unenriched lead means reps waste time researching. Enrich on lead create, then assign.
- **Report sprawl.** — 50 reports nobody reads. Build 5-7 dashboards that answer the most important questions. Archive the rest.

### [skills-lock](skills/automation/skills-lock/SKILL.md)

- **skills.lock not updated after skill changes.** — Skill changes pushed. skills.lock stale. Validation fails. Fix: Generate skills.lock as part of the commit/push workflow. Never commit skill changes without updating the lock file.
- **No validation in CI.** — Stale or corrupted skills.lock goes undetected. Consumers load tampered or outdated skills. Fix: CI runs validation on every push. Failing validation blocks merge.
- **Lock file too large.** — 500+ skills with full dependency trees = multi-MB lock file. Fix: Keep it lean. SHA256 + version + path + size. Skip full metadata (frameworks, dependencies are optional extensions).
- **No consumer documentation.** — Consumers don't know skills.lock exists or how to use it. Fix: Document in README. "To verify skill integrity: check that SHA256(skill) matches skills.lock."

### [tool-selection-stack](skills/automation/tool-selection-stack/SKILL.md)

- **Buying enterprise tools early** — — $25K ZoomInfo at $500K ARR. Start with Apollo, upgrade when data volume and deal size justify it.
- **Tool overlap** — — paying for two sequencers, three enrichment tools. Audit quarterly and consolidate.
- **No verification in stack** — — enrichment without verification means bouncing emails. LeadMagic Email Validation should be in every stack before the send step.
- **Tool as strategy** — — tools execute strategy, not define it. Build the process first, then select tools that support it.

### [waterfall-enrichment](skills/automation/waterfall-enrichment/SKILL.md)

- **One giant waterfall for everything.** — Different data types need different providers. Company data, email, and phone are separate waterfalls.
- **Wrong provider order.** — Sort by cost-per-hit, not coverage percentage. A cheap provider with low hit rate is expensive per result.
- **Skipping verification.** — Every waterfall returns 5-15% stale emails. Verification catches them before they damage sender reputation.
- **No credit caps.** — Without caps, a single stubborn row can consume 15+ credits across the full chain. Cap at 5-6 per row.
- **Not re-testing provider order.** — Provider performance changes quarterly. The waterfall that worked in January may be suboptimal by April.

## content-seo

### [aeo-strategy](skills/content-seo/aeo-strategy/SKILL.md)

- **Writing for search engines, not humans.** — Keyword-stuffed content that reads like a robot wrote it. Fix: write for your ICP first, optimize for search second.
- **Publishing and praying.** — Creating content without a distribution plan. Fix: every piece gets a 30-day promotion calendar across email, social, and paid.
- **Ignoring content freshness.** — 2-year-old content with outdated data and examples still ranking. Fix: quarterly content audit — update or retire stale pieces.

### [citation-harvesting](skills/content-seo/citation-harvesting/SKILL.md)

- **Writing for search engines, not humans.** — Keyword-stuffed content that reads like a robot wrote it. Fix: write for your ICP first, optimize for search second.
- **Publishing and praying.** — Creating content without a distribution plan. Fix: every piece gets a 30-day promotion calendar across email, social, and paid.
- **Ignoring content freshness.** — 2-year-old content with outdated data and examples still ranking. Fix: quarterly content audit — update or retire stale pieces.

### [faq-seo](skills/content-seo/faq-seo/SKILL.md)

- **Writing for search engines, not humans.** — Keyword-stuffed content that reads like a robot wrote it. Fix: write for your ICP first, optimize for search second.
- **Publishing and praying.** — Creating content without a distribution plan. Fix: every piece gets a 30-day promotion calendar across email, social, and paid.
- **Ignoring content freshness.** — 2-year-old content with outdated data and examples still ranking. Fix: quarterly content audit — update or retire stale pieces.

### [pillar-pages](skills/content-seo/pillar-pages/SKILL.md)

- **Writing for search engines, not humans.** — Keyword-stuffed content that reads like a robot wrote it. Fix: write for your ICP first, optimize for search second.
- **Publishing and praying.** — Creating content without a distribution plan. Fix: every piece gets a 30-day promotion calendar across email, social, and paid.
- **Ignoring content freshness.** — 2-year-old content with outdated data and examples still ranking. Fix: quarterly content audit — update or retire stale pieces.

### [pseo-strategy](skills/content-seo/pseo-strategy/SKILL.md)

- **Writing for search engines, not humans.** — Keyword-stuffed content that reads like a robot wrote it. Fix: write for your ICP first, optimize for search second.
- **Publishing and praying.** — Creating content without a distribution plan. Fix: every piece gets a 30-day promotion calendar across email, social, and paid.
- **Ignoring content freshness.** — 2-year-old content with outdated data and examples still ranking. Fix: quarterly content audit — update or retire stale pieces.

### [seo-strategy](skills/content-seo/seo-strategy/SKILL.md)

- **Writing for search engines, not humans.** — Keyword-stuffed content that reads like a robot wrote it. Fix: write for your ICP first, optimize for search second.
- **Publishing and praying.** — Creating content without a distribution plan. Fix: every piece gets a 30-day promotion calendar across email, social, and paid.
- **Ignoring content freshness.** — 2-year-old content with outdated data and examples still ranking. Fix: quarterly content audit — update or retire stale pieces.

## creative

### [ad-creative-strategy](skills/creative/ad-creative-strategy/SKILL.md)

- **One creative at a time.** — "Let's see how this performs" with no comparison. You can't optimize what you don't test.
- **Polished over volume.** — A beautiful ad nobody sees loses to 10 rough variants that find the winning message.
- **No fatigue monitoring.** — Same ad for 8 weeks with frequency >10. CTR drops 50%+. Rotate before performance degrades.
- **Creative not matching platform context.** — A polished corporate video on TikTok looks like an ad. Native-looking content wins.
- **Testing too many variables at once.** — Changed headline AND visual AND CTA. No idea which change caused the lift. One variable per test.

### [ai-content-creation](skills/creative/ai-content-creation/SKILL.md)

- **Publish AI output without editing.** — Raw AI output = generic, detectable, low-trust content. Fix: 4-pass human edit. AI writes drafts. Humans make them good.
- **No unique angle.** — AI can only summarize what's already been written. If you don't inject unique data, experience, or opinion, your content is a remix of page 1 results. Fix: Unique angle first. AI draft second.
- **"Write a blog post about X" (one-shot).** — One-shot prompts produce generic, meandering content with no structure. Fix: Research → outline → draft → edit. AI assists each step. It doesn't replace any.
- **Not including brand voice in prompts.** — Every AI output without brand context sounds the same. Fix: Paste voice guide into every prompt. Better: build a custom GPT with your brand voice trained in.
- **Hallucinated statistics.** — "According to a recent study..." with no source. Fix: Perplexity for research. Every stat needs a citation. Human verifies before publishing.
- **AI-generated images without review.** — Midjourney produces beautiful nonsense. "Data visualization" with made-up numbers. Charts with impossible scales. Fix: Review every AI image for accuracy.

### [ai-video-creation](skills/creative/ai-video-creation/SKILL.md)

- **AI avatar uncanny valley.** — Poor lip-sync, dead eyes, robotic gestures = viewers click away in 2 seconds. Fix: ElevenLabs voiceover with natural pacing. Test with 5 people: "Does this feel real?"
- **No captions.** — 85% of social video is watched without sound. No captions = 85% of audience doesn't get the message. Fix: Captions on every video. Word-by-word highlighting increases watch time 95%+.
- **Script too long.** — 90 seconds is the ceiling for attention on social. 15-30 seconds for ads. 45-60 seconds for demos. Fix: Cut your script in half. Then cut it again. Every word must earn its place.
- **Generative B-roll that doesn't match.** — Runway generated "a team collaborating in a modern office" shows 6-fingered people at impossible desks. Fix: Use stock footage or screen recordings for concrete scenes. Use Runway for abstract concepts, backgrounds, transitions.
- **Personalized video at scale that feels mass-produced.** — "Hey [first_name]" with an AI avatar that clearly isn't you. Fix: Record the personalized intro yourself (10 sec on Loom). AI handles the rest. The human touch is worth the 10 seconds.
- **Ignoring platform specs.** — LinkedIn: 16:9 or 1:1, under 10 min. TikTok: 9:16 vertical, under 3 min. YouTube Shorts: 9:16, under 60 sec. Fix: Export in the correct aspect ratio and duration for each platform.

### [content-distribution](skills/creative/content-distribution/SKILL.md)

- **Spend 90% on creation, 10% on distribution.** — Flip it. A great piece of content nobody sees is wasted. Distribution is the multiplier.
- **Publish once, done.** — The same piece should appear across 10+ formats and channels over 30 days. Most value comes from derivatives.
- **Self-promo in communities.** — Posting "check out my article" in Reddit gets removed. Post the insight with no link. The community finds you.
- **No paid amplification.** — Organic reach on LinkedIn is 2-5% of followers. Boost your best content to reach the other 95%.
- **Company page only.** — Founder posts get 10x the reach of company posts. Founder is the distribution channel at <$10M ARR.

### [copywriting](skills/creative/copywriting/SKILL.md)

- **Writing for everyone** — — copy that appeals to "business leaders" appeals to no one. Write for one specific person.
- **Feature lists without benefits** — — "10GB storage" meaningless. "Store 50,000 photos without worrying about space" meaningful.
- **Multiple CTAs** — — each additional CTA reduces conversion. One action per piece of copy.
- **Jargon** — — "leverage synergistic solutions" convinces no one. Simple, clear, specific wins.

### [graphic-design-gtm](skills/creative/graphic-design-gtm/SKILL.md)

- **Wrong dimensions** — — a 1920x1080 graphic on LinkedIn stories is cropped. Always match platform-specific dimensions.
- **Text in images too small** — — 60%+ of social browsing is mobile. Minimum 16px type, ideally 24px+ for headlines.
- **Too much information** — — one graphic, one message. A graphic with 5 data points communicates zero.
- **No brand consistency** — — different colors, fonts, and styles across assets signals amateur. Templates enforce consistency.
- **Stock photography** — — generic stock photos reduce trust. Use product screenshots, team photos, or custom illustrations.

### [growth-hacking-tactics](skills/creative/growth-hacking-tactics/SKILL.md)

- **Tactic copying without model understanding.** — "Dropbox did a referral program. We should too!" But you're an enterprise SaaS company where referrals come from relationships, not viral loops. Fix: Build your growth model first. THEN pick tactics that fit your model.
- **Running too many experiments.** — 10 simultaneous experiments = can't isolate what worked. Fix: 2-3 experiments per week max. One variable changed per experiment. Everything else held constant.
- **Over-optimizing the wrong metric.** — Growing signups 50% while activation stays at 10% = growing a leaky bucket. Fix: Find the bottleneck. Fix activation BEFORE scaling acquisition.
- **Declaring victory too early.** — "Our experiment increased conversion by 15%!" With n=20. Statistical noise. Fix: Minimum 100 conversions per variant before calling a winner. Use a significance calculator.
- **Scaling unscalable tactics.** — "We got 100 users from manually DMing people on LinkedIn." Great. Now automate it or find a scalable channel. Don't do 1,000 manual DMs. Fix: Scalable > manual. Find channels that compound.
- **Killing too slow.** — "Let's give it another week." 3 weeks later: same result. 3 months of momentum lost. Fix: Kill threshold: if confidence interval suggests it won't hit target, kill immediately. Move on.

### [landing-page-copy](skills/creative/landing-page-copy/SKILL.md)

- **Clever over clear.** — "We're the Salesforce of email" = I need to know what Salesforce is to understand you. Just say what you do. Fix: "Find any email in 30 seconds." No metaphors. No analogies. Just the outcome.
- **Feature vomit in the hero.** — "AI-powered, multi-threaded, cloud-native email verification platform with enterprise-grade security..." Nobody reads past the fourth word. Fix: One headline. One subhead. Two CTAs. Everything else goes below the fold.
- **No anxiety reduction.** — "Start free trial" with no supporting text = "but what's the catch?" Fix: Add "No credit card required" or "14-day trial" or "Cancel anytime" directly below the button.
- **Lazy social proof.** — "Trusted by leading companies" with no logos, no names, no metrics. This is less credible than NO social proof. Fix: Logos, specific results, full attribution, or aggregate metrics. Something real.
- **Testing too small.** — Testing "button color" when the headline is vague = optimizing deck chairs on the Titanic. Fix: Test the biggest lever first. Headline. Then CTA. Then social proof placement.
- **Copy written in isolation.** — Marketing writes copy. Sales hears objections daily. They never talk. Fix: Interview 3 salespeople. Ask: "What are the top 5 objections you hear?" Address every one of them on the landing page.

### [social-media-strategy](skills/creative/social-media-strategy/SKILL.md)

- **Company page as primary** — — people follow people, not companies. Founder and employee profiles outperform company pages 10:1.
- **Links in LinkedIn posts** — — algorithm severely deprioritizes external links. Put links in comments or "link in bio."
- **Inconsistent posting** — — posting 5x one week then nothing for 3 weeks kills momentum. Consistency > frequency.
- **Broadcasting, not engaging** — — posting without commenting on others' content is talking to an empty room.

### [v0-lander](skills/creative/v0-lander/SKILL.md)

- **One-shot prompting.** — "Build a SaaS website" in one prompt = generic, unbranded, middle-of-the-road output. Fix: Build section by section. Hero first. Iterate. Then pricing. Iterate.
- **Generic output without brand context.** — Without brand colors, fonts, and references, v0 generates generic Tailwind. Fix: Paste your brand context into the first prompt. Reference a known site for style.
- **Placeholder content shipped to production.** — v0 generates "Lorem ipsum" and placeholder images. Shipping this live = amateur. Fix: Replace ALL placeholder content before deploying.
- **Not iterating on mobile.** — v0 generates desktop-first by default. Mobile layout often breaks. Fix: "Show me the mobile version" as a dedicated iteration step.
- **No form connection.** — A "Start free trial" button that links to "#" is a broken promise. Fix: Connect forms and CTAs before deploying.
- **Too many sections.** — v0 will happily generate 15 sections if you ask. More sections = more cognitive load = lower conversion. Fix: 6-8 sections max. Cut anything that doesn't directly support the conversion goal.

### [vibe-coding](skills/creative/vibe-coding/SKILL.md)

- **Vibe-coding the product itself.** — Your core SaaS product needs real engineering. Vibe code the marketing site, not the payment processing. Fix: Marketing surfaces = vibe code. Product core = real code.
- **Accepting all AI output without review.** — "Accept All" is Karpathy's bit — and it works when you can test the output. But for customer-facing pages, test every button, every link, every form. Fix: 5-minute QA checklist before every deploy.
- **One-shot prompting.** — "Build a SaaS website" in one prompt produces generic slop. Fix: Build section by section. Hero first. Iterate. Then pricing. Iterate. One section at a time produces much better output.
- **No design system reference.** — AI generates generic Tailwind if you don't give it design constraints. Fix: Provide brand colors, font, and a reference site. "Look like Stripe but with #0066FF primary."
- **Forgetting mobile.** — AI tools often generate desktop-first layouts that break on mobile. Fix: As a final prompt: "Make this fully responsive. Stack all sections vertically on mobile. Ensure touch targets are 44px+."

### [vibe-marketing](skills/creative/vibe-marketing/SKILL.md)

- **AI slop at scale.** — "30 AI blog posts in 1 hour!" = 30 pieces of unreadable garbage. Fix: AI writes first drafts. Humans edit for voice, accuracy, and insight. 10 great posts > 100 AI-slop posts.
- **No fact-checking.** — AI confidently hallucinates statistics, customer quotes, and case studies. Fix: Every stat needs a source. Every quote needs attribution. Every claim needs verification.
- **Brand voice dilution.** — "Write a LinkedIn post" without brand voice context = generic AI voice. Fix: Paste your brand voice guide into every content prompt. Better yet: save it as a custom GPT.
- **One-and-done prompting.** — First AI output is never the best. Fix: "That's good. Now write 4 more variants with different hooks." Pick the best. Iterate. AI gets better with direction.
- **AI-only content with no human insight.** — AI can summarize what's already been said. Only humans can say something genuinely new. Fix: Your unique data, experiences, and opinions are the moat. AI is the amplifier, not the source.
- **Ignoring distribution.** — AI makes creation 10x faster. Distribution is still the bottleneck. Fix: Spend 20% of time creating, 80% distributing. AI can help with distribution copy too.

## customer-success

### [cs-analytics-dashboards](skills/customer-success/cs-analytics-dashboards/SKILL.md)

- **Health score without action.** — "Customer is at 38" without "here's the specific 3-step save play" is useless. Fix: Every health band maps to a specific playbook. Green → expansion. Yellow → engagement. Orange → intervention. Red → save.
- **Too many survey questions.** — NPS + CSAT + CES + onboarding survey + feature survey + quarterly survey = survey fatigue and 5% response rates. Fix: NPS twice/year. CSAT post-interaction only. One onboarding survey. That's it.
- **Composite health score hiding problems.** — Average 75 looks healthy but masks that Usage is 100 and Financial is 50 (customer loves the product but is about to go bankrupt). Fix: Review dimension scores individually, not just the composite.
- **Detractors without follow-up.** — NPS Detractor without personal outreach within 24 hours = you don't actually care about feedback. Fix: Auto-notify CSM + manager on Detractor. Template for follow-up call. Track close rate (Detractor → Promoter conversion).
- **Measuring activity instead of outcomes.** — "# of QBRs completed" is an activity metric. "% of QBRs that uncovered expansion opportunities" is an outcome metric. Fix: Every CS metric should tie to revenue or retention.
- **Champion churn undetected.** — Your champion leaves the company and you find out 3 months later when the contract doesn't renew. Fix: Automated job change monitoring (LinkedIn alerts, LeadMagic Job Change, manual LinkedIn check quarterly).

### [cs-playbooks](skills/customer-success/cs-playbooks/SKILL.md)

- **Measuring activity, not outcomes** — — logins are not value. Map customer Desired Outcomes and measure progress toward them.
- **CS as firefighting** — — if CSMs only engage when something is wrong, they are reactive support, not customer success.
- **No expansion motion** — — CS owns the relationship. If expansion lives only in Sales, the customer gets handed off at the worst moment.
- **One-size health score** — — different segments need different health models. Enterprise cares about executive engagement; SMB cares about time-to-value.

### [customer-onboarding](skills/customer-success/customer-onboarding/SKILL.md)

- **One onboarding for all.** — Enterprise customer with 500 seats and a $100K deal gets the same onboarding as a $500/mo SMB customer. Enterprise feels neglected. SMB feels overwhelmed. Fix: Segment by ACV. Different programs.
- **Features over outcomes.** — "Click here, then here, then here" teaches mechanics, not value. Fix: Every onboarding step links to the customer's desired outcome. "This step gets you to [their goal]."
- **No handoff from sales.** — CSM discovers on the kickoff call that Sales promised features that don't exist, committed to a timeline CS can't hit, and didn't mention the customer is about to be acquired. Fix: Mandatory handoff document AND meeting for every account.
- **"We'll schedule training later."** — If training isn't on the calendar during the kickoff call, it won't happen. The customer gets busy. Usage drops. Churn follows. Fix: Schedule all training sessions during kickoff.
- **Measuring activity instead of outcomes.** — "# of kickoff calls completed" is an activity. "% of customers achieving First Value within 7 days" is an outcome. Fix: Track outcome metrics, not activity metrics.
- **Ghosting after setup.** — Week 1: daily emails, 2 calls. Week 2: radio silence. Customer wonders if you still exist. Fix: Structured cadence. Weekly calls for month 1, biweekly for month 2, monthly thereafter.

### [headless-support](skills/customer-success/headless-support/SKILL.md)

- **AI agent launched too early.** — 5 help articles and an AI agent = 70% wrong answers, frustrated customers, and damaged trust. Fix: 30+ articles minimum. Test with 50 real questions before launch.
- **No escape hatch.** — AI agent that can't escalate to human is a customer experience disaster. Fix: Clear escalation triggers. "Talk to human" must always work. Never trap a customer in a bot loop.
- **AI persona mismatch.** — A chirpy, emoji-filled support bot for an enterprise security product is tone-deaf. Fix: Match AI persona to brand voice. Professional for enterprise, friendly for SMB.
- **Not measuring CSAT per channel.** — If AI CSAT is 3.8 and human CSAT is 4.5, you're degrading experience to save money. Fix: Track CSAT separately for AI and human. If AI CSAT drops below 90% of human CSAT, pause and fix.
- **Static knowledge base.** — Articles written once and never updated become wrong, then dangerous. Fix: Monthly KB review. Owner assigned per category. Every product release triggers KB updates.
- **Deflection as the only goal.** — "100% deflection = 0 support tickets" sounds great but means you're not hearing from customers. Some tickets are valuable product feedback. Fix: Deflect repetitive questions. Keep product feedback and enterprise escalations human-handled.

### [qbr-planning](skills/customer-success/qbr-planning/SKILL.md)

- **Product update disguised as QBR** — — executives don't care about feature releases. They care about business outcomes.
- **Surprise expansion ask** — — if expansion is first mentioned at the QBR, it's too late. Plant the seed months before.
- **Your metrics, not theirs** — — "you logged in 50 times" means nothing. "Your team reduced time-to-close by 40%" means everything.
- **No action items** — — a QBR without mutual commitments is a meeting, not a milestone.

### [sla-management](skills/customer-success/sla-management/SKILL.md)

- **Overpromising SLAs.** — "We respond in 15 minutes to everyone" with a 2-person team = broken promise within 24 hours. Fix: Set SLAs your team can meet 95%+ of the time. Underpromise, overdeliver.
- **P1 inflation.** — "The dashboard font is ugly" marked P1 by an enterprise customer. 6 months later, every ticket is P1 and the on-call team is burned out. Fix: Strict P1 criteria. CEO-approved before anyone overrides priority.
- **No after-hours clock pause.** — P3 ticket at 11pm Friday with "4-hour FRT" means SLA breach at 3am Saturday. Fix: P2-P4 clock pauses outside business hours. Communicate this clearly to customers.
- **Auto-replies counting as FRT.** — "We've received your request" is not a response. Customers know this. Fix: FRT = HUMAN acknowledges and begins working. Auto-responders are courtesy, not SLA compliance.
- **No escalation automation.** — Agent forgets to escalate at 50% SLA. Ticket sits for days. Customer escalates to CEO on Twitter. Fix: Automated escalation triggers in help desk. No human memory required.
- **SLA breaches without follow-up.** — A breached SLA without customer communication is a churn event. Fix: Auto-notify manager on breach. Template for customer communication. Post-mortem for root cause.

### [support-tool-stack](skills/customer-success/support-tool-stack/SKILL.md)

- **Overbuying for stage.** — Zendesk Enterprise at $115/seat for a 2-person CS team is lighting money on fire. Fix: Match platform to stage. Upgrade when you need the features, not before.
- **No macros at launch.** — CS team retyping the same 10 responses 50x/day is slow, inconsistent, and demoralizing. Fix: Build 15+ macros before go-live. Iterate weekly from actual tickets.
- **Chat widget on every page.** — Messenger/Beacon on every page = noise. Fix: Put on pricing page (pre-sales questions), help center (support), and post-signup (onboarding). Not on blog, homepage, or logged-out marketing pages.
- **AI agent without training data.** — Launching Fin or Answer Bot with 3 help articles produces wrong answers and angry customers. Fix: 20+ articles minimum. Test with 50+ real customer questions before launch.
- **No CSAT follow-up.** — Collecting "1/5" ratings without human follow-up sends the message: "We don't actually care." Fix: Auto-escalate scores < 3 to manager for personal follow-up within 24 hours.
- **Ignoring the knowledge base.** — Most support volume comes from the same 20 questions. If they're all documented, ticket volume drops 30-60%. Fix: Write articles from actual tickets. Every ticket that gets the same answer 3x becomes a help center article.

## demand-gen

### [content-syndication](skills/demand-gen/content-syndication/SKILL.md)

- **Creating without distributing.** — The 30-hour creation / 3-minute promotion ratio (Simmonds) describes most B2B content teams. Fix: plan the 30-day distribution calendar before writing the pillar; block calendar time for the sequence before publication day, not after.
- **Ignoring the Consumption Gap.** — SDRs follow up on syndication leads within minutes of form-fill. The prospect has not read the content yet. The conversation has no shared context and reads as a cold call. Fix: encode the 48-hour wait in your CRM or sequencer as a required delay before SDR enrollment.
- **Measuring paid syndication on CPL alone.** — A $55 CPL from NetLine looks expensive next to a $20 CPM awareness campaign — until you compare cost-per-SQO (~5% lead-to-SQO for syndication vs ~2% for paid social). Fix: always report lead-to-SQO alongside CPL; gate budget decisions on pipeline yield.
- **Bare link drops in communities.** — Reddit, LinkedIn groups, and Slack communities suppress or remove posts that are pure promotional links. Fix: follow Simmonds' community-first rule — contribute value to the thread first; share the asset as a resource in response to an existing question.

### [paid-social-strategy](skills/demand-gen/paid-social-strategy/SKILL.md)

- **Webinar as product demo.** — Prospects attend for insights, not a sales pitch. Fix: 80% educational content, 20% product mention. Lead with counterintuitive insights.
- **One-and-done syndication.** — Publishing once and moving on. Fix: one pillar piece → 15+ derivatives across channels over 30 days.
- **Measuring paid social on clicks.** — Clicks and CPL don't equal pipeline. Fix: track pipeline generated and cost per opportunity from each channel.

### [podcast-gtm](skills/demand-gen/podcast-gtm/SKILL.md)

- **Webinar as product demo.** — Prospects attend for insights, not a sales pitch. Fix: 80% educational content, 20% product mention. Lead with counterintuitive insights.
- **One-and-done syndication.** — Publishing once and moving on. Fix: one pillar piece → 15+ derivatives across channels over 30 days.
- **Measuring paid social on clicks.** — Clicks and CPL don't equal pipeline. Fix: track pipeline generated and cost per opportunity from each channel.

### [webinar-strategy](skills/demand-gen/webinar-strategy/SKILL.md)

- **Webinar as product demo.** — Prospects attend for insights, not a sales pitch. Fix: 80% educational content, 20% product mention. Lead with counterintuitive insights.
- **One-and-done syndication.** — Publishing once and moving on. Fix: one pillar piece → 15+ derivatives across channels over 30 days.
- **Measuring paid social on clicks.** — Clicks and CPL don't equal pipeline. Fix: track pipeline generated and cost per opportunity from each channel.

## design

### [battlecard-builder](skills/design/battlecard-builder/SKILL.md)

- **Feature comparison instead of talk tracks.** — A table of features is a reference doc. A battlecard is a conversation tool. Write talk tracks.
- **No proof points.** — "We're better at X" without evidence loses to competitors who have it. Every claim gets a proof point.
- **Trashing the competitor.** — "They're terrible" makes you look defensive. Acknowledge strengths, differentiate on outcomes.
- **Stale pricing.** — A battlecard with 6-month-old pricing is worse than no battlecard. Reps lose credibility instantly.
- **Too long.** — Reps cannot read a 3-page document during a call. One card per topic, scannable in 10 seconds.
- **One card for all competitors.** — Different competitors attack from different angles. A battlecard for Salesforce looks different from one for a startup.

### [case-study-builder](skills/design/case-study-builder/SKILL.md)

- **No metrics.** — "They love our product" is a testimonial, not a case study. Every case study needs specific, named numbers.
- **Marketing language in quotes.** — "We leveraged their best-in-class solution" — no human talks like this. Use their actual words.
- **Too many results.** — 3-4 metrics max. Pick the strongest ones. More metrics dilute the impact of each.
- **No customer approval.** — Never publish a case study without written permission. Include the approval step in your process.
- **One format for everything.** — Sales needs a 1-pager. Marketing needs a story. Website needs both. Build both formats.

### [design-system-gtm](skills/design/design-system-gtm/SKILL.md)

- **Vague voice guidelines.** — "Professional and friendly" is useless. Agents need specific, testable attributes: "Short sentences. Active voice. No passive constructions. Data before adjectives." Fix: For each voice attribute, provide 3 examples of "this, not that."
- **RGB without hex.** — AI agents reference hex codes for HTML/CSS generation. Including RGB is good. Including only RGB is not. Fix: Hex is the primary color format for agents. RGB and HSL are supplementary.
- **No CSS variable output.** — Agents generating HTML need copy-pasteable CSS. Wading through a color palette table to extract hex codes produces errors. Fix: Include a `:root {}` CSS block with all design tokens.
- **Ignoring dark mode.** — Many agent-generated artifacts (dashboards, presentations) look different in dark mode. Fix: Include dark mode color variants or document that the brand is light-mode-only.
- **No guardrails.** — Without explicit rules, agents will improvise — and sometimes generate content that's off-brand, legally risky, or factually wrong. Fix: Clear tiered guardrails: acceptable, review, never.
- **Design system as PDF.** — If your design system is a Figma file or PDF, AI agents can't read it. Fix: DESIGN.md in markdown, version controlled, linked from all agent configuration files.

### [one-pager-builder](skills/design/one-pager-builder/SKILL.md)

- **Two pages pretending to be one.** — If it takes 5 minutes to read, it's a brochure. Cut ruthlessly. Every sentence must earn its space.
- **Feature list, not benefit list.** — "10GB storage" → "Store 50,000 files without worrying about space."
- **No CTA.** — What should they do after reading? Visit a URL? Book a call? Email someone? Make it specific.
- **Generic differentiators.** — "Best-in-class" means nothing. "Only solution that verifies emails in real-time at 99%+ accuracy" means something.
- **info@company.com as contact.** — A one-pager with a generic email address signals "we don't actually want you to reach out."

### [pitch-deck-builder](skills/design/pitch-deck-builder/SKILL.md)

- **Feature dump.** — Slides listing features without connecting to outcomes. "We have AI-powered enrichment" → "Reps spend 0 minutes on manual research."
- **One deck for everyone.** — CTO and VP Sales care about different things. If the same deck works for both, it works for neither.
- **No speaker notes.** — Slides without delivery guidance produce inconsistent presentations. The deck is a tool, not a script.
- **Too many slides.** — 10-11 is the sweet spot. 25 slides = nobody remembers anything. If you need more detail, put it in an appendix.
- **Reading slides aloud.** — The audience can read. The speaker adds context, stories, and conviction the slides cannot.
- **No clear CTA.** — "Let us know if you're interested" is not a next step. "Does Thursday at 2pm work for a technical deep-dive?" is.

### [roi-calculator](skills/design/roi-calculator/SKILL.md)

- **Aggressive as default.** — Showing only the aggressive scenario trains prospects to be skeptical. Fix: Lead with conservative. "Here's what we can confidently promise. Most customers achieve more."
- **Unrealistic assumptions.** — "You'll save 40 hours/week" when your best customer saves 10. CFOs spot this instantly and trust is destroyed. Fix: Use actual customer data, not aspirational numbers.
- **Black-box calculator.** — "Trust us, the math works" is not a business case. Prospects need to see and validate every assumption. Fix: Document every input with its source. Make the calculator transparent.
- **One-size output.** — A CFO cares about 3-year NPV. A VP Sales cares about pipeline increase. A CTO cares about implementation time. Fix: Create persona-specific summary tabs or views.
- **No source on assumptions.** — "Industry average" without naming the source is no better than "we guessed." Fix: Name the source: "Gartner 2026 Report," "Internal customer data (50+ deployments)," "Bureau of Labor Statistics."
- **Ignoring implementation cost.** — "The software is $50K/year, therefore ROI is [benefits ÷ $50K]." Wrong. Implementation, training, migration, and opportunity cost of the transition period are real costs. Fix: Include all costs in Year 1. Model 3 years to amortize one-time costs.

### [ui-ux-gtm](skills/design/ui-ux-gtm/SKILL.md)

- **Design over conversion.** — A beautiful page with 1% conversion is worse than an ugly page with 4%. Fix: A/B test. Let data decide. Beauty is subjective. Conversion is not.
- **Too many fields.** — "Name + Email + Phone + Company + Role + Team Size + How did you hear about us?" = 2% conversion. Fix: Email only. Collect the rest via progressive profiling or enrichment.
- **Inaccessible color choices.** — Thin gray text on white background. Blue links on blue backgrounds. Red/green as the ONLY status indicator (4.5% of the population is color-blind). Fix: Test contrast ratios. Add icons alongside color.
- **No mobile testing.** — "Our B2B buyers are on desktop." Wrong. 50%+ of B2B research happens on mobile. If your mobile experience is broken, you're losing half your pipeline. Fix: Design mobile-first. Desktop is an enhancement, not the default.
- **Vague error messages.** — "An error occurred." "Invalid input." These don't help users fix the problem. Fix: Every error message must say: what went wrong + how to fix + example if helpful.
- **Ignoring the empty state.** — New users see a blank dashboard that says "No data yet" and leave. Fix: Empty states should show sample data, explain what will appear, and provide a "Get started" button.

## events

### [conference-strategy](skills/events/conference-strategy/SKILL.md)

- **No pre-event outreach.** — Showing up to a conference without booked meetings wastes the investment. Fix: scrape attendee lists, research targets, and book meetings 2-3 weeks before.
- **Booth staff without training.** — Untrained staff give generic demos and fail to qualify. Fix: train on qualification questions, demo flow, and data entry before the event.
- **No post-event follow-up system.** — Leads go cold within 48 hours. Fix: Day 1 personalized follow-up, Day 3 value-add, Day 7 soft CTA.

### [event-driven-outreach](skills/events/event-driven-outreach/SKILL.md)

- **No pre-event outreach.** — Showing up to a conference without booked meetings wastes the investment. Fix: scrape attendee lists, research targets, and book meetings 2-3 weeks before.
- **Booth staff without training.** — Untrained staff give generic demos and fail to qualify. Fix: train on qualification questions, demo flow, and data entry before the event.
- **No post-event follow-up system.** — Leads go cold within 48 hours. Fix: Day 1 personalized follow-up, Day 3 value-add, Day 7 soft CTA.

### [field-marketing](skills/events/field-marketing/SKILL.md)

- **No pre-event outreach.** — Showing up to a conference without booked meetings wastes the investment. Fix: scrape attendee lists, research targets, and book meetings 2-3 weeks before.
- **Booth staff without training.** — Untrained staff give generic demos and fail to qualify. Fix: train on qualification questions, demo flow, and data entry before the event.
- **No post-event follow-up system.** — Leads go cold within 48 hours. Fix: Day 1 personalized follow-up, Day 3 value-add, Day 7 soft CTA.

## foundation

### [buyer-psychology](skills/foundation/buyer-psychology/SKILL.md)

- **Hiding flaws creates suspicion.** — Buyers fill information gaps with worst-case assumptions. "They didn't mention security — it must be bad." Preempt concerns by surfacing them yourself.
- **Social proof without specificity.** — "Trusted by thousands" is noise. "Used by 3 of the top 10 fintech companies" is signal. Specific > impressive.
- **Too many options.** — When prospects face 4+ pricing tiers, they default to inaction or choose the cheapest. Offer 3 options max with a clear recommended path.

### [competitive-intel](skills/foundation/competitive-intel/SKILL.md)

- **Battlecards that are feature comparison tables without the FIA structure.** — A list of features is not a battlecard — it's a spec sheet. Every fact must connect to an impact on the deal and an action the seller can take. Without the Act column, competitive intel adds cognitive load without improving outcomes.
- **Inflating competitor weaknesses and downplaying competitor strengths.** — Sales teams lose trust in competitive intel that isn't honest. If a competitor genuinely has a better product in some dimension, say so. Then teach the seller how to reframe the decision criteria around dimensions where you win. Attempting to argue "our product is better in every way" when it's not is the fastest path to competitive intel being ignored.
- **Ignoring the status quo as a competitor.** — In B2B SaaS, the most common "competitor" is the prospect deciding to do nothing, continue with their current manual process, or build internally. If your competitive analysis doesn't include a "Status Quo/Do Nothing" battlecard, you're missing the competitor that wins the most deals.
- **Win/loss analysis that relies on sales rep self-reporting without structure.** — Sales reps' post-mortem explanations for why they won or lost are systematically biased — they over-attribute wins to their own skill and losses to external factors (pricing, product gaps). Use a structured win/loss interview protocol with specific questions about the decision process.
- **Facts that can't be cited or sourced.** — "Competitor X has poor customer support" is useless if you can't point to anything when challenged. Every fact should be sourced: a G2 review, a customer interview, a public pricing page, a demo recording. If it can't be sourced, mark it as "sales team anecdote" so the uncertainty is transparent.
- **Competitive matrix that uses arbitrary scores.** — Scoring yourself a 5 and every competitor a 3 on every dimension destroys credibility. Scores need a consistent rubric. What does a 5 mean on "ease of use"? What does a 2 mean? Define the scale.
- **Treating competitive intel as a one-time project.** — Competitors ship features, change pricing, shift positioning, and get acquired. Competitive intel that's six months old is misleading. Include a review cadence (recommended: quarterly full review, monthly spot-check for major changes).
- **Discovery questions that are leading or aggressive.** — "Don't you find Competitor X's platform slow and buggy?" is a leading question that signals bias and creates defensiveness. SPIN-based questions should surface the prospect's actual experience: "How has the platform's performance been as your team has grown?" Let the prospect identify the weakness.

### [gtm-context](skills/foundation/gtm-context/SKILL.md)

- **ICP is too broad.** — "Mid-market SaaS companies" is not an ICP — it's a TAM. An ICP specifies industry, size band, tech stack, buying trigger, and geography. If your ICP definition doesn't exclude at least 80% of companies, it's not specific enough. Use Moore's beachhead principle: what is the narrowest segment where you can dominate?
- **Confusing stated ICP with actual ICP.** — Founders often describe who they want to sell to rather than who actually buys. Always ground the ICP in empirical customer data, not aspiration. If your 3-5 best customers are all 50-person fintech companies, your ICP is 50-person fintech companies regardless of what the pitch deck says.
- **Skipping negative personas.** — Defining who NOT to sell to is as important as defining who to sell to. Without explicit negative personas, SDRs waste cycles on companies that will never convert, AEs take meetings that will never close, and marketing generates leads that sales rejects. Document at least three negative persona profiles.
- **GTM motion is described as a buzzword without specifics.** — "We're PLG with sales assist" is insufficient. Describe the actual customer journey: how does someone discover you? What is the first product experience? When does a human get involved? What triggers the handoff? Be precise about the mechanics.
- **Metrics section lists targets without current baselines.** — A target without a baseline is a wish. Every metric should show Current → Target with a timeframe. If you don't know the current value, mark it as "Unknown — needs instrumentation" rather than omitting it.
- **Competitive analysis is only direct competitors.** — The biggest competitor in B2B SaaS is almost always "status quo" — the prospect continuing to do things the way they currently do. If your competitive landscape doesn't include status quo/DIY/manual alternatives, you're missing the competitor that wins most deals.
- **The 90-day plan tries to do everything at once.** — A common failure mode is listing 20 tactics across 5 channels for Phase 1. The 90-day plan should have at most 3-5 objectives total and focus each phase on the highest-leverage activities. Sequencing matters more than comprehensiveness.
- **Context is treated as a one-time deliverable rather than living documentation.** — GTM context decays. ICPs shift. Competitors enter. Channels saturate. The context document should include a "Last Updated" date and a review cadence (recommended: quarterly). Without this, the document loses trust and teams stop referencing it.

### [icp-scoring](skills/foundation/icp-scoring/SKILL.md)

- **Equal weighting across dimensions.** — Giving firmographics, technographics, behaviors, and intent equal weight produces a model that doesn't discriminate. Firmographics and technographics should dominate (60-80% combined) because they represent structural fit. Behavior and intent are dynamic signals that supplement structural fit.
- **Scoring what feels important rather than what predicts conversion.** — Without empirical calibration, scoring models reflect internal assumptions rather than market reality. If you have win/loss data, use it. If you don't, start with recommended weights and commit to recalibrating after 50 deals.
- **Binary scoring instead of graduated scoring.** — "In target industry: yes/no" is too coarse. A company in an adjacent industry is worth something. A graduated scale (100/60/20/0) captures the reality that fit is a continuum.
- **Negative personas that are too narrow.** — "We don't sell to competitors" is obvious. The valuable negative personas are the subtle ones: companies that look like ICP on firmographics but have disqualifying technographic or behavioral profiles. Document the lookalike traps.
- **Buying committee map that includes everyone.** — Not every persona needs to be present for every deal. Map personas to ICP tiers and deal sizes. A $10K ACV deal doesn't need the same committee as a $100K deal.
- **Language banks that use internal jargon.** — The words your team uses to describe the problem are not the words prospects use. Validate language banks against actual prospect conversations, sales call recordings, and customer interview transcripts.
- **Treating the model as static.** — ICP scoring models decay as markets shift, competitors enter, and your product evolves. Include a recalibration cadence (recommended: quarterly review, recalibration every 6 months or 100 deals, whichever comes first).
- **Scoring on data you can't actually obtain at scale.** — A scoring dimension that requires a manual research step per lead doesn't scale. Ensure each attribute in the model can be sourced from enrichment APIs, public data, or automated signals.

### [icp-targeting-tiers](skills/foundation/icp-targeting-tiers/SKILL.md)

- **Segmenting by employee count only.** — A 30-person cybersecurity company buys like an enterprise (security reviews, compliance, long cycles). A 300-person e-commerce company buys like SMB (credit card, fast decision). Use ACV and buying behavior, not just firmographics.
- **One motion for all tiers.** — The rep who closes $100K enterprise deals cannot also close $1K SMB deals. The skills, patience, and process are completely different. Segment your sales team by tier.
- **Enterprise features for SMB customers.** — "We have SSO and audit logs!" SMB buyer: "I don't know what SSO is. Can I import a CSV?" Build for your buyer's sophistication level, not your engineering team's pride.

### [positioning-messaging](skills/foundation/positioning-messaging/SKILL.md)

- **Starting positioning with the product instead of competitive alternatives.** — The most common positioning error. Dunford's framework works because it forces you to first understand what the customer currently does. If you skip to unique capabilities without establishing the baseline, the capabilities sound like generic feature claims.
- **Confusing features with unique capabilities.** — "AI-powered" is a feature. "Automatically generates personalized outreach based on buying signals from 12 data sources" is a unique capability — if no competitor does it. Every claimed unique capability must pass the test: "Do any of our competitive alternatives do this?"
- **Strategic narrative that sells the product instead of the shift.** — Raskin's structure works because it creates belief in a new way of doing things BEFORE introducing the product. If the narrative is "here's why our product is great," it's not a strategic narrative — it's a pitch. The product should feel inevitable by the time you introduce it.
- **Messaging matrix that says the same thing to every persona.** — Different personas care about different things. The Economic Buyer cares about ROI and risk. The End User cares about usability and time savings. The Technical Evaluator cares about security and integration. If every persona gets the same message, the matrix isn't doing its job.
- **VMF that skips negative consequences.** — The Before Scenario and Negative Consequences are the most emotionally powerful components of the VMF. Without them, the After Scenario and Positive Business Outcomes feel like empty promises. The cost of inaction must be made concrete and specific.
- **Category design that renames an existing category with a buzzword.** — Adding "AI-powered" or "next-gen" to an existing category name is not category design. Category design requires a fundamentally different way of framing the problem space — one that makes incumbents look like they're solving yesterday's problem.
- **Voice guidelines that describe an aspiration rather than a reality.** — "We sound like trusted advisors" is meaningless. Describe specific attributes: "We use short sentences. We cite data. We ask questions more than we make claims. We never use the word 'leverage' as a verb."
- **Messaging that sounds like it was written by a committee.** — Strong positioning has a point of view. It deliberately excludes some buyers. It takes a stance. If the messaging tries to appeal to everyone, it appeals to no one. The target customer section should make it clear who this is NOT for.

### [pricing-strategy](skills/foundation/pricing-strategy/SKILL.md)

- **Pricing based on competitor pricing minus 10%.** — This is the race to the bottom. If you're always 10% cheaper than the category leader, you're training the market to see you as the discount option. Price based on your value, not their price. If your value is higher, price higher. If it's lower, fix the product, not the price.
- **Feature gating instead of feature differentiation.** — When Tier 1 has "up to 5 reports" and Tier 2 has "unlimited reports," the customer feels punished for choosing Tier 1. When Tier 1 has "standard reports" and Tier 2 has "custom reports with AI insights," the customer feels they're getting more value at Tier 2. Design tiers around capability unlocks, not artificial limits.
- **Too many tiers.** — Four tiers is the maximum most buyers can evaluate. Five or more creates decision paralysis and reduces conversion. Three is optimal for most B2B SaaS products: an entry tier that's easy to buy, a middle tier that's the obvious best value, and a top tier for power users.
- **No annual plan or insufficient annual discount.** — Annual billing improves cash flow, reduces churn, and increases valuation multiples. Standard annual discounts range from 10-20%. If your annual discount is less than 10%, few customers will choose it. If it's more than 25%, you're leaving too much revenue on the table.
- **Discount guidelines that are too permissive.** — "AEs can discount up to 20%" without conditions teaches AEs that discounting is the primary closing tool. Discount authority should be narrow by default with clear conditions for escalation. The best discount guideline is: "Discounts are offered in exchange for something — multi-year commitment, expansion, case study, reference."
- **Enterprise tier that's just "contact us."** — "Contact us for pricing" without any anchor or range drives away qualified enterprise buyers who need to budget before engaging. Provide a "starting at" price or a range. The actual price can be negotiated up from the starting point.
- **Pricing that doesn't account for expansion revenue.** — If your model is per-seat, the path to higher NRR is seat expansion. If your model is usage-based, it's consumption growth. If your model is tiered, it's upgrades. Design the tier structure so that expansion is a natural path, not a forced upsell.
- **Treating pricing as fixed once set.** — Pricing should be reviewed quarterly in early-stage companies and at least annually in scaled companies. Market conditions change, competitors move, and value perception evolves. The pricing strategy document should include a review cadence and triggers for revisiting (e.g., "revisit if win rate drops below X%").

### [using-gtm-skills](skills/foundation/using-gtm-skills/SKILL.md)

- **Generic output.** — The agent produces advice that could apply to any company. Fix: tie the work to the user's ICP, motion, stage, and constraints.
- **Missing operating detail.** — The answer explains what matters but not what to do. Fix: include concrete steps, templates, fields, or decision rules.
- **No verification step.** — The workflow ends before checking quality. Fix: include a checklist or acceptance criteria.

## founder-led

### [advisor-recruitment](skills/founder-led/advisor-recruitment/SKILL.md)

- **Advisor logo collecting.** — 6 advisors who never show up are worse than 0 advisors who show up — they dilute equity and create fake confidence. Fix: Cap at 4-6 active advisors. Quality over quantity.
- **No scope definition.** — "Be available to help" produces nothing. "5 customer intros per quarter" produces pipeline. Fix: Define specific deliverables in the advisor agreement.
- **Over-equitying light advisors.** — 1% for "I'll take your call when you need me" is a bad trade. 0.25% for 2 hours/month with specific deliverables is fair. Fix: Use FAST template benchmarks.
- **No advisor management system.** — Advisors don't self-manage. If you don't send pre-reads, schedule calls, and track asks, they'll drift. Fix: Treat advisor management like a recurring 1-hour/week task.
- **Asking for too much.** — "Can you introduce me to every VP of Sales you know?" is overwhelming. "Can you think of 2-3 people for our Head of Engineering role?" is actionable. Fix: Specific, time-bound, easy-to-say-yes asks.

### [board-meeting-prep](skills/founder-led/board-meeting-prep/SKILL.md)

- **The 80-slide deck.** — You'll present maybe 10 slides. The rest are appendix. If you spend the meeting clicking through slides, you've failed. Fix: 15-20 slides max. Put everything else in appendix with a "we can reference if needed."
- **Metrics without narrative.** — "Churn is 2.8%" means nothing without "this is up from 1.8% because X — here's our plan." Fix: Every metric slide gets one sentence of "so what?"
- **No decision asks.** — "We'd love your thoughts on..." is a waste of board time. They can give thoughts over email. Meetings are for DECISIONS. Fix: Every strategic topic ends with a specific decision or vote.
- **Surprising board members in the meeting.** — If you're proposing a major pivot, funding strategy change, or team restructure, board members should know BEFORE the meeting. Fix: Pre-align on anything controversial.
- **No executive session.** — This is standard governance — the board meets without the CEO to discuss CEO performance, compensation, and succession. It's not a vote of no confidence. If your board isn't doing it, suggest it. Fix: Always include 10-15 min executive session at end.

### [brand-kit](skills/founder-led/brand-kit/SKILL.md)

- **Logo without an icon variant.** — You need a square icon for favicons, social avatars, and app icons. Design the icon separately.
- **Too many colors.** — More than 5 colors dilutes brand recognition. Primary + secondary + neutral + accent = 6-10 total. That's the limit.
- **Voice as "professional."** — Every company claims to be professional. Be specific: "direct, opinionated, data-backed" tells people how you actually sound.
- **No banned words list.** — Without explicit prohibitions, "leverage" and "synergy" creep into every piece of copy. Ban them explicitly.
- **Templates that nobody uses.** — If templates require a designer to operate, they won't be used. Build templates that a non-designer can fill in.

### [building-saas](skills/founder-led/building-saas/SKILL.md)

- **Overbuilding before validation.** — Spending 6 months on architecture before talking to a single customer. Ship in days, iterate based on usage.
- **Free tier without conversion path.** — Freemium with 5% conversion means 95% of users cost money forever. Design the upgrade trigger before launching the free tier.
- **Hiring VP Sales before $2M ARR.** — 70% failure rate. Founder-led sales until the playbook is proven and repeatable.
- **Enterprise features too early.** — SSO, audit logs, and SOC2 matter when enterprise is 20%+ of pipeline. Before that, they're distraction.
- **No unit economics tracking.** — CAC, LTV, churn, payback period. If you can't answer these in 30 seconds, you're flying blind.

### [business-insurance](skills/founder-led/business-insurance/SKILL.md)

- **No E&O before enterprise deal.** — Enterprise procurement asks for COI. You don't have it. Deal blocked for 2-4 weeks while you shop for insurance. Some customers walk away. Fix: Get E&O when you start targeting mid-market or enterprise — before the first deal, not during it.
- **Thinking "we're too small to get sued."** — You're not. A $100K ARR startup can be sued for $1M by a customer who lost money during your downtime. Fix: Insurance is cheaper than being right in court.
- **Buying the cheapest policy.** — Lowest premium = most exclusions = claims denied when you actually need it. Fix: Compare coverage, not just price. Understand what's excluded.
- **Not naming enterprise customers as additional insured.** — Enterprise contract says "name us as additional insured on your E&O." You buy E&O but forget to add them. They reject the COI. Fix: Your broker handles additional insured endorsements. Ask for one per enterprise customer.
- **Lying on the application.** — "We've never had a security incident." But you had a breach last year. The insurer finds out. Claim denied. Policy rescinded. Fix: Be honest on insurance applications. They can and will investigate before paying large claims.

### [co-founder-dynamics](skills/founder-led/co-founder-dynamics/SKILL.md)

- **Choosing a friend instead of a co-founder.** — Friendship is not a qualification. You need complementary skills, aligned ambition, and tested work chemistry. Fix: Work on a project together for 3 months before formalizing anything.
- **50/50 with no vesting.** — One founder stops contributing at month 6, still owns 50%. The company is unfundable. Fix: 4-year vesting with 1-year cliff. Always. Even for best friends. Even for spouses.
- **Avoiding hard conversations.** — "The equity split feels unfair now that I'm doing 80% of the work" goes unsaid for 12 months. Resentment builds. Startup dies. Fix: Monthly retro. Ask "is equity still fair?" explicitly.
- **No written agreement.** — "We trust each other — we don't need a contract." Every co-founder lawsuit started with this sentence. Fix: Co-founder agreement signed before incorporation. It's not about trust — it's about clarity when emotions run high.
- **Unequal commitment unaddressed.** — One founder works 60 hours. The other works 20 and has a side project. This festers. Fix: Full-time commitment expectation in the agreement. If someone wants part-time, their equity should reflect it.
- **Ignoring founder-market fit.** — A great engineer doesn't automatically make a great SaaS CTO. A great salesperson doesn't automatically understand developer tools. Fix: The co-founder should have deep domain knowledge or intense curiosity about the problem space.

### [content-led-growth](skills/founder-led/content-led-growth/SKILL.md)

- **Creating content nobody asked for.** — "What I want to write about" ≠ "what my ICP needs to know." Fix: Mine customer calls, support tickets, and sales objections for topics. Write what they're already asking about.
- **Writing but not distributing.** — A blog post with no promotion is a tree falling in an empty forest. Fix: 80% distribution, 20% creation. For every hour writing, spend 4 hours distributing.
- **Link-dumping on social.** — "New blog post: [link]" gets 10% of the reach of native content. Fix: Post the full framework natively on social. Link in the reply or bio. Give the value on-platform.
- **Measuring pageviews not pipeline.** — 10,000 pageviews that generate 0 demos is a hobby, not a GTM channel. Fix: Track content → demo → revenue attribution with UTMs and self-reported source.
- **Too many channels too early.** — Newsletter + podcast + YouTube + LinkedIn + X + TikTok = burnout in 2 months. Fix: Master ONE channel first. Add channels when the first one is producing pipeline consistently.
- **Inconsistent publishing.** — The algorithm rewards consistency. A newsletter that goes out "when I have time" never grows. Fix: Same day, same time, every week. Pre-write 4 issues before launching.

### [data-privacy-compliance](skills/founder-led/data-privacy-compliance/SKILL.md)

- **Copy-pasted privacy policy.** — "We don't use cookies" while using Google Analytics, Stripe, and Intercom = false statement, GDPR violation. Fix: Document what you actually do. Update when your stack changes.
- **No DPA ready for enterprise.** — Enterprise customer asks for DPA. You don't have one. Deal stalls for weeks while you scramble. Fix: Have a DPA template ready. Termly can generate one.
- **Pre-ticked cookie consent.** — "Accept All" is pre-selected. This is illegal under GDPR. CNIL (France) fined Google €150M for this. Fix: "Accept All" and "Reject All" must be equally prominent. Nothing pre-ticked.
- **No breach notification plan.** — Breach happens Friday at 9pm. No one knows what to do. 72-hour clock is ticking. Monday morning: GDPR violation + breach exposure. Fix: Incident response plan with notification triggers and templates.
- **Ignoring CCPA until $25M.** — CCPA has a private right of action for data breaches. You don't need to hit the threshold to get sued for a breach. Fix: Implement reasonable security measures regardless of revenue.
- **Forgetting about vendor sub-processors.** — You sign a DPA with a customer promising GDPR compliance — but you never collected DPAs from your own vendors (AWS, Intercom, etc.). Fix: Collect and maintain DPAs from all sub-processors. Share the list with enterprise customers.

### [employment-compliance](skills/founder-led/employment-compliance/SKILL.md)

- **Misclassifying employees as contractors.** — "They're a contractor" but they work 40 hours/week, use your laptop, have a company email, and report to a manager. If it walks like an employee and quacks like an employee... Fix: Use the IRS 20-factor test. When in doubt, classify as employee and use Gusto/Justworks.
- **No IP assignment from contractors.** — You pay a contractor $50K to build your product. They own the code. You don't. Fix: Every contractor signs a PIIA or work-for-hire agreement BEFORE starting work.
- **Firing without documentation.** — "It wasn't working out" with no paper trail = lawsuit risk. Fix: Document performance issues. Give feedback in writing. Follow progressive discipline. The paper trail is your defense.
- **Ignoring state-specific laws.** — "We're based in Texas, but we hired a remote employee in California." California has completely different overtime rules, sick leave requirements, and final paycheck timing. Fix: Your PEO (Gusto/Rippling) handles this — but you need to tell them about every hire in every state.
- **No handbook for employee #1.** — "We're only 3 people — we don't need a handbook." You need it BEFORE there's a problem. The handbook is evidence that you communicated expectations and policies. Fix: SixFifty generates a handbook in under an hour.

### [engineer-to-founder](skills/founder-led/engineer-to-founder/SKILL.md)

- **Building before validating.** — "I have a great idea. Let me spend 6 months building it in secret." 6 months later: 0 users, 0 feedback, 0 revenue, and a product that solves a problem nobody has. Fix: Talk to 5 users first. Build an MVP in a weekend. Show it to them. Iterate.
- **Quitting with no runway.** — "I'll quit my job and it'll force me to make it work." It forces you to take the first bad job offer, accept bad terms from investors, and make short-term decisions that kill long-term value. Fix: 12+ months runway. Side-project until traction.
- **Avoiding sales because "I'm an engineer."** — "I'll hire a salesperson to handle that." You can't hire sales until you've proven the sales motion. You ARE sales until $1M+ ARR. Fix: Reframe sales as requirements gathering. Read Founding Sales. Do 50 calls. You'll get better — I promise.
- **Choosing tech for learning instead of shipping.** — "I'll build this in Rust because I want to learn Rust." Your startup is not your learning project. Fix: Use the stack you know best. Ship fast. Rewrite when you have 1,000 paying customers.
- **Perfectionism as procrastination.** — "Just one more refactor before we launch." "The landing page isn't quite right." "I need to add one more feature." This is fear wearing a productivity mask. Fix: Ship broken things. Users will tell you what actually needs fixing.
- **Isolation.** — Solo founder, coding alone for 6 months, no peer group, no feedback, no reality checks. This is the #1 cause of founder depression and burnout. Fix: Co-founder or founder peer group. Built-in-public community. Monthly reality checks.

### [equity-management](skills/founder-led/equity-management/SKILL.md)

- **Cap table in Excel.** — Excel can't handle cap table complexity (option exercises, early exercises, multiple funding rounds). Fix: Carta or Pulley from day 1.
- **No 409A valuation.** — You're granting options at an arbitrary price = IRS penalties for you and your employees. Fix: 409A before first grant. Renew annually.
- **Nowhere near enough equity for key hires.** — "0.1% for our VP Engineering" won't close a candidate who can get 1%+ elsewhere. Fix: Benchmark against stage and role. Don't be stingy on your most critical hires.
- **Forgotten option pool at fundraising.** — You model dilution from the new round but forget the option pool refresh. Surprise: an extra 15% dilution. Fix: Model dilution including option pool. Negotiate pool size at term sheet stage.
- **Missing 83(b) for founders.** — Miss it and you owe tax on phantom income as your shares vest over 4 years. Fix: File within 30 days. Keep proof. This is the #1 unforced error in startup equity.

### [events-planning](skills/founder-led/events-planning/SKILL.md)

- **Event without pipeline goal.** — "Let's host a dinner" without a target attendee list and pipeline goal is an expensive meal, not a GTM activity.
- **No post-event follow-up.** — Conversations at events die without follow-up within 48 hours. The event is the opener, not the close.
- **Sponsoring the wrong conference.** — A $25K sponsorship where your ICP doesn't attend is $25K wasted. Verify attendee demographics before committing.
- **Webinar as product pitch.** — Nobody attends a webinar to hear a sales pitch. Teach something valuable. The product is the logical next step, not the topic.
- **Measuring vanity metrics.** — "200 attendees" means nothing if zero become pipeline. Track conversations → meetings → pipeline → revenue.

### [exiting-company](skills/founder-led/exiting-company/SKILL.md)

- **Missing IP assignments.** — Contractor IP gaps kill deals — fix in month 1–6.
- **Customer concentration.** — One logo >20% ARR → un-acquirable or deep discount.
- **Founder dependency.** — Acquirer buys key-person risk, not a company.
- **Optimizing ARR before NRR.** — Diligence strips low-quality revenue.
- **Shopping the company.** — Inbound from relationships beats outbound "for sale."
- **Headline EV without cash-at-close math.** — Earn-out traps look like big deals. Fix: `earn-out-term-sheet-review.md` before signing.
- **Accepting EBITDA earn-out without carve-outs.** — Buyer can cut marketing and void payout. Fix: `negotiating-earn-out.md` governance section.

### [financial-modeling](skills/founder-led/financial-modeling/SKILL.md)

- **Top-down revenue modeling.** — "1% of $100B market" = fiction. Fix: Model customers × ACV with realistic acquisition.
- **Zero churn assumption.** — No SaaS has zero churn. Fix: 1-3% monthly churn minimum for SMB, 0.5-1% for mid-market.
- **Instant AE productivity.** — AEs don't close month 1. Fix: Ramp curve: 0% M1, 50% M3, 100% M6.
- **Terminal value dominates DCF.** — 80-90% of startup value from terminal = speculative. Fix: Conservative terminal growth (2-3%). Wide sensitivity.
- **WACC too low for startups.** — 10% WACC for seed stage implies utility-level risk. Fix: Early stage WACC = 20-30%. Risk is real.
- **Aggregate metrics hiding segment problems.** — 2% churn average hides 5% SMB churn and 0.5% Enterprise. Fix: Segment everything.

### [first-hires-playbook](skills/founder-led/first-hires-playbook/SKILL.md)

- **Hiring ahead of the pain.** — "We'll need a marketing team eventually" is not a reason to hire a marketer at $500K ARR. The role will be undefined, they'll flounder, you'll fire them, it'll cost $50K+ in severance and recruiter fees. Fix: Hire when the constraint is active and painful, not theoretical.
- **Hiring for pedigree over stage-fit.** — The ex-Google PM who's never talked to a customer will fail at a 10-person startup. Fix: Prioritize "built it from zero" over "managed a $100M product line."
- **Under-equitying first hires.** — If you give first hires 0.1% and expect founder-level ownership mentality, you'll get employee-level effort. Fix: First 5 hires: 0.5-3%. First 10: 0.2-1.5%. These numbers scale down fast — hire #50 gets 0.05%.
- **Slow offer process.** — Top candidates are off the market in 2 weeks. If your process takes 4+ weeks, you'll only hire people who can't get offers elsewhere. Fix: 5 stages, 10 business days, offer in 48 hours.
- **Skipping the work sample.** — Interviews measure interview skills. Work samples measure work skills. The correlation between them is weaker than you think. Fix: Every role gets a real work sample before the final round.

### [founder-brand](skills/founder-led/founder-brand/SKILL.md)

- **Company page as primary.** — People follow people, not companies. Founder posts outperform company page posts 10:1 on LinkedIn.
- **Posting company content only.** — "We launched a new feature" is not thought leadership. Share insights, lessons, and contrarian takes.
- **Inconsistent posting.** — Posting bursts then silence loses momentum. Schedule content in advance. Batch-create on Sundays.
- **Vanilla voice.** — "Excited to announce..." is invisible. Have opinions. Take positions. The people who disagree are not your audience.
- **Engagement without pipeline tracking.** — Likes don't pay bills. Track: content → profile views → website visits → demo requests → closed revenue.

### [founder-comp-playbook](skills/founder-led/founder-comp-playbook/SKILL.md)

- **Hire before motion.** — Comp can't fix unproven product. Fix: founder closes 10–20 first.
- **OTE vanity contest.** — $180K OTE / $900K quota beats $200K / $2M quota. Fix: show math.
- **Equity hand-wave.** — "We'll be generous later." Fix: grant numbers in writing.
- **Geo bait-and-switch.** — Offer remote then cut 20%. Fix: band in JD.
- **Skip RepVue check.** — Candidates know your reputation. Fix: align posted vs paid.

### [founder-sales](skills/founder-led/founder-sales/SKILL.md)

- **Demoing too early.** — First meeting should be discovery, not demo. If you haven't identified a Critical Event, skip the demo. You'll waste time on tire-kickers. Fix: Require SPICED completion before scheduling demos.
- **Emailing pricing.** — If you email pricing after the call, you've lost control of the conversation. They'll compare to competitors without your context. Fix: Discuss pricing live, anchoring on value delivered.
- **Overqualifying on budget.** — "What's your budget?" is a lazy question that gets lazy answers. Most buyers don't know their budget for a new category. Fix: Qualify on pain impact. "What's this problem costing you?" — if the answer is 10x your price, budget exists.
- **Hiring sales too early.** — Before you've proven repeatability, a sales hire is a research project you're paying for. They'll fail and blame the product. Fix: Close 20+ deals yourself first. Document everything.
- **Discounting without concessions.** — Every discount without a trade trains buyers to ask for more. Fix: Always conditional. Always.

### [fundraising-strategy](skills/founder-led/fundraising-strategy/SKILL.md)

- **Fundraising before you're ready.** — If growth is under 10% MoM and retention is under 100% NRR, fix the business first. Raising won't fix product-market fit problems. Fix: Meet growth benchmarks before starting.
- **Taking the first term sheet.** — Unless it's from your dream investor with dream terms, create competitive tension. Fix: Batch your process so multiple VCs are evaluating simultaneously.
- **Over-raising on SAFEs.** — Multiple SAFE rounds with escalating caps create a "stack" — when your Series A prices below the highest cap, early SAFE holders get massive dilution protection at your expense. Fix: Limit SAFE rounds to 1-2 before priced round.
- **Neglecting the partner meeting.** — First meeting is screening. Partner meeting is where the decision happens. Send updated metrics, prep references, and anticipate every hard question. Fix: Do a mock partner meeting with an experienced founder.
- **Announcing before money hits the bank.** — Term sheets fall through. Wires can take days. Fix: Wait until funds are in your account.

### [gtm-recruiting](skills/founder-led/gtm-recruiting/SKILL.md)

- **Post and pray.** — Zero outbound. Fix: 70% sourcing / 30% inbound.
- **Hidden comp.** — Candidate discovers gap on RepVue. Fix: publish range in JD.
- **Negotiate base only.** — Ignore quota reachability. Fix: total package math.
- **Token diversity hire.** — Lower bar. Fix: same scorecard; diversity of thought.
- **Slow offer.** — Candidate takes competing offer. Fix: pre-draft comp before finals.
- **Recruiter misalignment.** — No exclusive terms. Fix: written fee + guarantee.

### [gtm-role-descriptions](skills/founder-led/gtm-role-descriptions/SKILL.md)

- **JD without org context.** — Candidate can't tell if they're hire #2 or #20. Fix: title includes stage and team size.
- **Quota not tied to OTE.** — $200K OTE with $400K quota = rep leaves. Fix: Bridge Group ~5:1 ratio.
- **SDR comp on activity.** — Pays for dials, not pipeline quality. Fix: qualified meetings held + SQO bonus.
- **VP Sales too early.** — 70% failure before $2M ARR. Fix: follow hire sequence.
- **Comp hidden.** — RepVue-savvy candidates skip. Fix: publish range.
- **Same JD for SMB and enterprise AE.** — Different skills, different comp. Fix: separate role catalog entries.
- **GTM Engineer vs RevOps conflation.** — Forecast owner ≠ Clay builder. Fix: `gtm-engineer-hiring.md` role table; split titles at scale.
- **Hiring GTM Engineer before process exists.** — Automates broken CRM stages. Fix: Operating Model ≥6 (`pipeline-management`) before FTE.

### [hiring-agencies](skills/founder-led/hiring-agencies/SKILL.md)

- **Agency before process.** — Without `pipeline-management` stages and SPICED fields, the agency invents its own motion. Fix: document process first.
- **Outsourcing strategy.** — Agencies write messaging from scratch without your positioning. Fix: provide approved copy, ICP, and talk tracks.
- **Black-box reporting.** — Activity counts without pipeline impact. Fix: score on qualified meetings and cost-per-meeting, logged in your CRM.
- **Unverified data.** — Bad lists burn domain reputation. Fix: require verified emails and suppression checks before any send.
- **No kill switch.** — Sunk-cost extensions for 6+ months. Fix: 90-day pilot with explicit stop criteria.
- **Never bringing in-house.** — Perpetual agency dependency at 2–3x employee cost. Fix: graduate proven channels to hires.

### [hiring-by-role](skills/founder-led/hiring-by-role/SKILL.md)

- **Trusting gut over scorecard.** — "They didn't score well, but I liked them." Likability bias is one of the strongest hiring biases. Fix: If scorecard < threshold, no hire. Gut is a tiebreaker, not a decider.
- **Same process for every role.** — Engineering interview for sales candidate = "what's your favorite data structure?" Salesperson walks out. Fix: Role-specific processes.
- **No work sample.** — "They interviewed well" but can't do the actual work. Fix: Every role includes a work sample that mirrors the actual job.
- **"Would I get a beer with them?" test.** — Filters for people like you. Reduces diversity. Amplifies unconscious bias. Fix: Assess values alignment, working style, and contribution to team — not social compatibility.
- **Asking about past salary.** — Banned in many states. Anchors offer to previous pay (which may reflect discrimination). Fix: Pay based on the role, not the candidate's previous salary.
- **Years of experience as a requirement.** — "15+ years experience" filters out the 10-year person who's done 3x as much. Fix: Describe what they've achieved, not how long they've been working.

### [hiring-contractors](skills/founder-led/hiring-contractors/SKILL.md)

- **No IP assignment clause.** — The most expensive mistake. Without it, the contractor owns the work. Fix this in the contract before work begins.
- **Vague scope.** — "Improve the app" is not a scope. "Add single sign-on via Google OAuth with these 5 specific requirements" is.
- **Hiring the cheapest option.** — A $15/hr contractor who takes 4x as long and produces unmaintainable code costs more than a $100/hr contractor who ships correctly the first time.
- **No code review.** — Contractor code without review becomes technical debt your team can't touch. Review everything before merge.
- **Treating contractors like employees.** — They have other clients. They don't attend your standups unless you're paying for that time. Set clear expectations and respect boundaries.

### [investor-updates](skills/founder-led/investor-updates/SKILL.md)

- **Hiding problems.** — Investors find out anyway. Problems you communicate early are opportunities for help. Problems you hide are trust-breakers.
- **No asks.** — Investors want to feel useful. If you never ask for anything, they stop reading. Specific asks drive engagement.
- **Sending only when things are good.** — The months you don't want to send an update are the months you most need to. Silence signals trouble.
- **Dense walls of text.** — Nobody reads 5-page updates. One page. Metrics first. Narrative second. Bullet points, not paragraphs.
- **Inconsistent format.** — Different structure every month means investors can't find what they're looking for. Same format, every month, forever.

### [job-posting-strategy](skills/founder-led/job-posting-strategy/SKILL.md)

- **Spraying every job board.** — Same post on LinkedIn + Indeed + Monster + Glassdoor + 10 niche boards. 500 unqualified applicants. Team spends 40 hours screening. Fix: 2-3 highest-signal channels per role. More channels = more noise, not more signal.
- **Years of experience as primary filter.** — "7+ years experience" filters out the 5-year engineer who built 3 successful products. Years ≠ capability. Fix: Describe what they've BUILT or ACHIEVED, not how long they've existed.
- **No compensation range.** — Candidates assume the worst. Strong candidates don't apply. You're fishing in a shallow pool. Fix: Include salary range in every posting. It's required by law in many states anyway.
- **Passive job posting (post and pray).** — Post goes up. Nobody applies. Post sits there. Nobody applies. Fix: Posting is 20% of the work. Sourcing (outbound to passive candidates) is 80%.
- **Generic job post.** — "We're looking for a talented engineer to join our dynamic team..." Every company says this. Zero differentiation. Fix: Constraint-first format. Why this role exists NOW. What they'll OWN.

### [launch-planning](skills/founder-led/launch-planning/SKILL.md)

- **Launch without pre-launch.** — Showing up on launch day with no audience, no partners, and no press list is publishing, not launching. Fix: 6 weeks pre-launch for Tier 1. 70% of effort is pre-launch.
- **One channel only.** — Product Hunt without email, social, partners, and press reaches 10% of your potential audience. Fix: Activate minimum 8 channels for Tier 1 launches.
- **No launch narrative.** — "We launched a new feature" is not news. "The old way of X is dead — here's the new way" is a launch. Fix: Write the Raskin strategic narrative before writing anything else.
- **Poor Product Hunt execution.** — Launching at 9am with no first-hour supporters and a generic first comment = page 3 of PH, 10 upvotes. Fix: Launch at midnight PST, line up 20+ supporters, write a compelling first comment story.
- **No post-launch follow-up.** — Traffic spikes and disappears in 48 hours. If you don't have retargeting, email sequences, and follow-up content ready, you'll capture 5% of the value. Fix: Build post-launch sequences during pre-launch. They go live automatically.
- **Measuring the wrong things.** — Upvotes and pageviews feel good but don't pay bills. Fix: Measure pipeline and revenue. Content → signup → demo → close. Launch is a GTM motion, not a vanity contest.

### [lead-magnets](skills/founder-led/lead-magnets/SKILL.md)

- **Gating something nobody wants.** — "Download our company overview PDF" is not a lead magnet — it's a brochure. Fix: Would you give YOUR email for this? If you hesitate, prospects will bounce.
- **Too many form fields.** — Name + Email + Phone + Company + Role + "How did you hear about us?" = 2% conversion. Fix: Email only. Ask for the rest during onboarding or via progressive profiling.
- **Delayed delivery.** — "Thanks! We'll email you the magnet within 24 hours." 50%+ of people never open the email. Fix: Deliver instantly — on-page redirect or automated email within 60 seconds.
- **No nurture sequence.** — Capturing an email and doing nothing with it is collecting, not converting. Fix: 4-email nurture sequence over 14 days, bridging from magnet value → product value → demo CTA.
- **Magnet disconnected from product.** — A lead magnet about "10 best coffee shops in Boston" generates leads who like coffee, not your B2B SaaS product. Fix: The magnet must naturally bridge to your product's value proposition.
- **Building instead of testing.** — Spending $15K and 6 weeks on a calculator before validating demand. Fix: Test with a manual version first (spreadsheet, consultant gives you the output). If people use the manual version, build the tool.

### [legal-for-founders](skills/founder-led/legal-for-founders/SKILL.md)

- **Missing 83(b) election.** — Miss the 30-day window and you can be taxed on millions in phantom income as your company grows. Fix: File immediately after receiving shares. Certified mail. Keep proof.
- **No IP assignment.** — Founder builds the product. Keeps the IP personally. Leaves. Company has nothing. Fix: All founders sign PIIA before writing any code. If you haven't — do it this week.
- **Copy-pasted Privacy Policy.** — "We don't use cookies" (but you use Stripe, Intercom, Google Analytics — all of which use cookies). This is false. GDPR fines: up to 4% of global revenue. Fix: Write an accurate policy that matches what you actually do.
- **Shaking hands on equity splits.** — "50/50, we trust each other." No vesting. No agreement. No IP assignment. This is not a company — it's a lawsuit waiting to happen. Fix: Clerky incorporation with 4-year vesting. All founders sign.
- **Using the wrong SAFE.** — Pre-money SAFE (pre-2018) means dilution is unclear. Post-money SAFE (current YC standard) is clearer. Fix: Use the YC post-money SAFE. Don't modify unless your lawyer says so.
- **No DPA for enterprise customers.** — Enterprise customers will send you a DPA to sign. If you don't have one, they won't buy. Fix: Have a standard DPA ready. Termly and Iubenda can generate one. Lawyer-review if you're enterprise-scale.

### [partner-programs](skills/founder-led/partner-programs/SKILL.md)

- **Partners without enablement.** — A portal with "sign up here" generates signups and zero revenue. Partners need training, assets, deal registration, and someone to call when they're stuck. Fix: Don't launch until enablement is built.
- **One-size-fits-all economics.** — 15% for an agency that closes the deal AND implements is too low. 25% for a referral partner who just makes an intro is too high. Fix: Economics vary by partner type and effort.
- **No deal registration.** — Without deal reg, partners won't share pipeline (they'll get undercut by your direct team). Fix: Implement deal registration with clear protection windows as the FIRST piece of infrastructure.
- **Too many partners, too little support.** — 50 signed partners with 0 dedicated PAM = 45 inactive partners. Fix: Cap at what you can support. 10 well-enabled partners produce more revenue than 100 shelf partners.
- **Hiring a VP of Partnerships too early.** — If you're under $5M ARR, the founder is the partnerships team. A VP Partnerships at $2M ARR will build a program but can't generate enough revenue to justify the hire. Fix: Founder-led partnerships until $5-10M ARR with proven partner pipeline.
- **Mixing partner types in one program.** — Agencies need different economics, training, and support than referral partners. A single "Partner Program" with one set of rules fits nobody. Fix: Separate programs (or sub-programs) per partner type.

### [pricing-psychology](skills/founder-led/pricing-psychology/SKILL.md)

- **Cost-plus pricing.** — "Our costs are $X, so we charge $X + 30%." This ignores what customers are willing to pay. You might be leaving 50%+ on the table. Fix: Value-based pricing. What is the problem worth to them?
- **Competitor-minus pricing.** — "Competitor charges $100, we'll charge $80." This starts a race to the bottom. The cheapest option is not the best option — it's the cheapest. Fix: Differentiate on value, not price.
- **Too many tiers.** — 5+ tiers creates analysis paralysis. Prospects can't decide, so they leave. Fix: 3 tiers. 4 maximum. Each with a clear persona.
- **Flat pricing with no expansion.** — If every customer pays the same price, your revenue is capped at customer count. Fix: Add a usage dimension (contacts, emails, API calls, seats) so revenue grows with customer usage.
- **Founder discount reflex.** — "They asked for a discount, so I gave them 20%." This trains customers to ask and destroys your pricing integrity. Fix: Concession menu, not straight discounts. "I can't reduce the price, but I can..."
- **No annual option.** — Monthly billing = monthly churn risk. Annual billing = 12 months of committed revenue, lower churn, better cash flow. Fix: Always offer annual with 10-20% discount. Default to annual on pricing page.

### [saas-metrics-calculator](skills/founder-led/saas-metrics-calculator/SKILL.md)

- **Raw-revenue LTV.** — Using total revenue instead of contribution margin. If your gross margin is 70%, raw LTV overstates by 43%. Fix: Always use ARPA × Gross Margin % ÷ Monthly Churn Rate.
- **Under-counting CAC.** — "Our CAC is $200" but you only counted ad spend, not the salaries of the 4 SDRs and 2 AEs who closed those customers. Fix: Fully-loaded CAC. All S&M expense ÷ new customers.
- **Mixing time periods.** — Using last month's spend but this quarter's new customers creates garbage metrics. Fix: Same period. If you spent $100K in Q1 and acquired 50 customers, use Q1 for both.
- **Company-wide averages hiding problems.** — Your enterprise segment might have LTV:CAC of 8x while SMB is 1.5x. Average says 3x — which is false comfort. Fix: Segment by channel, cohort, and customer size.
- **Ignoring the Burn Multiple.** — Growth at all costs is dead. A company growing 100% with a 3x Burn Multiple is less healthy than a company growing 50% with a 1x Burn Multiple. Fix: Report Burn Multiple alongside growth rate.
- **Annualizing monthly churn wrong.** — Monthly churn of 2% ≠ 24% annual churn. It compounds: 1 - (1 - 0.02)^12 = 21.5%. Fix: Use the compound formula or track actual annual churn from cohort data.

### [saas-outcomes](skills/founder-led/saas-outcomes/SKILL.md)

- **Default to VC without $100M story.** — Down rounds and founder replacement. Fix: name bootstrap path explicitly if TAM is niche.
- **Single headline multiple.** — Ignores NRR, concentration, churn. Fix: driver checklist in `references/valuation-multiples.md`.
- **Mixing playbooks.** — VC burn with bootstrap ownership goals. Fix: one primary end goal per `references/end-goal-matrix.md`.
- **Selling at peak FOMO.** — After-tax hold may beat LOI. Fix: DCF vs sale scenario in `financial-modeling`.
- **Optimizing valuation before retention.** — Multiples compress in diligence. Fix: unit economics first (Skok).

### [sales-team-building](skills/founder-led/sales-team-building/SKILL.md)

- **VP Sales before $2M ARR.** — 70% failure rate. Cost: $300-500K in comp + opportunity cost. VP's job is to scale what works, not discover it.
- **SDR as first hire.** — Founder closes every deal + manages junior rep = neither done well. First hire: full-stack AE who prospects AND closes.
- **No written sales process.** — The first AE builds the playbook, not just closes deals. If the founder can't document the process, the AE can't replicate it.
- **AE mis-hire.** — 40% mis-hire rate, $484K cost over 24 months. Validate with a paid project before full-time. Check: can they self-source pipeline? Do they have ACV-relevant experience?
- **Comp complexity.** — A compensation plan that fits on one page is 3x more likely to drive the right behavior. Show causality: comp tied directly to desired outcome.

### [security-assessments](skills/founder-led/security-assessments/SKILL.md)

- **No pen test before enterprise deal.** — Customer asks for pen test report. You don't have one. Deal stalls for 4-6 weeks while you schedule and complete one. Fix: Pen test annually starting from your first mid-market deal.
- **Pen test findings not fixed.** — You have the report. You never fixed the findings. Next year's pen test finds the same issues. Customer's security team asks why. Fix: Track findings. Fix them. Get retest confirmation.
- **Answering security questionnaires without engineering.** — "Yes, we encrypt all data at rest" — but your engineering team knows you don't. You just committed to something in a contract. Fix: Route technical questions to the people who know the answers.
- **No incident response plan.** — Breach happens. Chaos. Everyone's emailing each other. Legal isn't looped in. Customer notification is delayed. Regulatory deadline missed. Fix: Document the plan. Assign the team. Test it with a tabletop exercise.
- **Relying on bug bounties instead of pen tests.** — Bug bounties catch the obvious stuff and miss the chained vulnerabilities that a methodical pen tester finds. Fix: Pen test annually. Bug bounty as supplement.

### [soc2-compliance](skills/founder-led/soc2-compliance/SKILL.md)

- **Starting too early.** — SOC2 at $500K ARR with no enterprise pipeline is premature optimization. Implement good security practices. Formal audit can wait.
- **Starting too late.** — Losing enterprise deals because you don't have SOC2 is a sales problem, not a security problem. Start the process when enterprise pipeline hits 20%+ of total.
- **Over-scoping.** — Auditing all five criteria when you only need Security + Availability doubles the cost and timeline. Audit what customers ask for.
- **Manual evidence collection.** — Without a compliance platform, you'll spend 10-20 hours/month on evidence. The platform pays for itself in time saved.
- **No bridge letter.** — If your audit gap exceeds 12 months, enterprise procurement teams will reject it. Get a bridge letter from your auditor.

### [solo-founder-gtm](skills/founder-led/solo-founder-gtm/SKILL.md)

- **Hiring before the motion works.** — If the founder can't close 10-20 deals personally, the motion isn't proven. Hire an AE to accelerate what works, not to discover what works.
- **Enterprise tools at startup stage.** — $25K ZoomInfo at $500K ARR is capital misallocation. Apollo is $59/mo and covers 90% of early-stage needs.
- **SDR as first hire.** — A full-stack AE who can prospect AND close is the right first hire. An SDR adds pipeline but can't close it — so the founder still closes every deal while managing the SDR.
- **No AI leverage.** — One founder + AI tools outperforms 3 junior hires at lower cost and zero management overhead.
- **Skipping self-assessment.** — The GTM Index surfaces what's broken before you scale it. Fix the system, then add people.

### [startup-communities](skills/founder-led/startup-communities/SKILL.md)

- **Community tourism.** — Join 20 Slack groups, post once in each, never return. Depth > breadth. Fix: Choose 3 communities. Participate daily for 3 months. Then evaluate.
- **Location fatalism.** — "I can't build a startup because I don't live in SF." YC, Stripe (Patrick Collison was in Ireland initially), Zapier (fully remote), GitLab (remote from day 1) all prove location is an advantage, not a requirement. Fix: Build where you are. Apply to accelerators. Attend conferences. Build in public.
- **"Networking" without building.** — Attending meetups without having shipped anything is socializing, not networking. Fix: Ship first. THEN network. "I built X" earns respect. "I'm thinking about building X" earns nods.
- **Applying to accelerators cold.** — Applications without traction, without alumni connections, without demonstrated building. Fix: Ship something first. Get users. THEN apply. Your application is 10x stronger.
- **Wrong community for your stage.** — Hacker News is great for technical feedback, terrible for enterprise sales advice. Pavilion is great for revenue leaders, useless for pre-launch founders. Fix: Match community to your current challenge.
- **Ignoring local community because "it's not Silicon Valley."** — Every city has founders. Find them. Meet monthly. The density is lower, but the depth can be higher — people outside the hype cycle are often more genuine.

### [vc-outreach](skills/founder-led/vc-outreach/SKILL.md)

- **Raising without building the line.** — You show up as a cold "dot" and wonder why response rates are 1%. Fix: Start monthly updates 6-12 months before raising. Build the line. Show the trend.
- **Generic cold emails.** — "Dear Investor, we're revolutionizing..." is deleted in under 3 seconds. Fix: Lead with specific traction. "We're at $X ARR growing X% MoM" earns 30 seconds of attention.
- **Asking for money in the first email.** — "We're raising $5M on $30M pre" in a cold email = asking a stranger to marry you on the first date. Fix: First contact: "I'd love your perspective." Not "I'd love your money."
- **Spraying 200 VCs simultaneously.** — They talk to each other. When 5 VCs get the same email and compare notes, you look amateur. Fix: Tier your outreach. A-list gets personalized attention. C-list gets batch if needed.
- **No follow-up after the meeting.** — A VC meets 20 founders a week. If you don't follow up within 2 hours, they forget which one you were. Fix: Follow-up email sent before you leave the parking lot. Every meeting.
- **Artificial urgency.** — "The round is closing fast — we need an answer by Friday." This works exactly once: when it's true. VCs have seen it faked 1,000 times. Fix: Real urgency is traction and competing term sheets, not fabricated deadlines.

### [vendor-contracts](skills/founder-led/vendor-contracts/SKILL.md)

- **No standard MSA.** — Every enterprise customer sends you THEIR contract. You're negotiating from their paper. Every time. Every deal takes months. Fix: Have your own MSA template. "We use our standard MSA. Our customers find it fair."
- **Unlimited liability.** — You signed a contract with no liability cap. A customer sues for $5M in damages from your $10K/year SaaS product. Your company is dead. Fix: Liability cap = 12 months of fees. Non-negotiable for early-stage companies.
- **Custom contracts for every deal.** — "This customer wants their own MSA." Now you're managing 50 unique contracts with different terms. Legal risk per contract. Fix: 80/20 rule. 80% of deals use standard contract. 20% negotiate minor terms. 0% get fully custom.
- **No auto-renewal tracking.** — Contract auto-renews at 3x the price. You didn't notice. Customer is furious. Fix: Calendar reminders 90 days before every renewal. Review terms before auto-renewal triggers.
- **Ignoring vendor security review.** — You bought a tool without checking its security. It gets breached. Your customer data is exposed. Your customer sues YOU — not the vendor. Fix: Security review every vendor that touches customer data. DPA + SOC2 minimum.

### [yc-ecosystem](skills/founder-led/yc-ecosystem/SKILL.md)

- **Applying the night before.** — Your first draft is never your best. YC tracks application updates and sees iteration as a positive signal. Fix: Start 4 weeks before deadline. Iterate weekly.
- **Marketing language in the application.** — "We're revolutionizing the enterprise collaboration space through AI-powered workflow optimization." YC partners read 10,000+ applications. They can smell BS. Fix: "We auto-generate sales reports from CRM data. 12 paying customers at $500/mo."
- **Scripted video.** — Reading a teleprompter or memorized script = instant rejection. Fix: 3 talking points. Talk naturally. Show the product screen. Be yourselves.
- **No traction, no problem.** — "We have an idea and a Figma mockup." YC accepts some pre-traction companies, but they're the exception. Fix: Build something. Get users. Get revenue. Even 5 paying customers changes your application.
- **Ignoring YC resources if not applying.** — YC Startup School, the YC Library, HN, and Co-Founder Matching are free and open to everyone. Fix: Use them regardless of your YC plans.
- **Not doing Demo Day prep until month 3.** — Your 1-minute pitch needs 50+ iterations to be sharp. Fix: Start practicing your pitch in month 1. Iterate weekly. By month 3, it should be muscle memory.

## growth

### [churn-prevention](skills/growth/churn-prevention/SKILL.md)

- **Lagging indicators only.** — Renewal date proximity is not a health score. It tells you when the decision happens, not whether it will be a yes.
- **Generic re-engagement.** — "We miss you" emails don't work. Reference their specific use case and the value they achieved when things were going well.
- **No champion monitoring.** — The single biggest churn predictor is champion departure. Monitor job changes across your customer base.
- **Equal treatment of all churn risks.** — A $500/month customer and a $50,000/year customer don't get the same intervention. Tier by revenue.

### [customer-marketing](skills/growth/customer-marketing/SKILL.md)

- **Asking for favors without rewards.** — "Can you write a review?" with nothing in return. Fix: Every advocacy request includes a reward — gift card, swag, early access, co-marketing.
- **Over-using references.** — Same 3 customers do 10 reference calls each. They burn out. Fix: Cap at 2-3/quarter. Rotate.
- **Publishing case studies without metrics.** — "Acme Corp loves us" is not a case study. Fix: Every case study has before/after metrics.
- **No review response.** — Negative G2 review sits unanswered for months. Prospects see it. Trust evaporates. Fix: Respond within 24 hours. Every time.

### [expansion-selling](skills/growth/expansion-selling/SKILL.md)

- **Expanding too early.** — Asking for upsell during onboarding = churn risk. Fix: Deliver value first. Expand after month 3+.
- **No expansion comp for CSMs.** — CSMs comped on retention only = no expansion. Fix: Variable comp tied to NRR. 50% base, 50% variable on NRR target.
- **Missing consumption triggers.** — Customer usage spikes. Nobody notices. Fix: Automated alerts when usage hits 80% of plan limit.
- **One-size expansion play.** — Seat expansion for every customer ignores cross-sell and tier upgrade opportunities. Fix: Multiple playbooks.

### [referral-programs](skills/growth/referral-programs/SKILL.md)

- **One-sided incentives.** — "$50 to you if your friend signs up" underperforms double-sided offers because there is no social obligation — the referrer feels they are extracting value from a friend. Fix: always reward both sides (Dropbox, PayPal both demonstrated this). If budget is constrained, halve the single-sided amount and split it.
- **Paying on sign-up, not collection.** — 100 sign-ups, 0 paying → $5,000 in rewards for nothing. Fix: reward triggers on first payment or minimum milestone. Encode this as a non-negotiable rule in your referral platform configuration.
- **No referral dashboard for referrers.** — Referrers share, then have no visibility on whether referrals converted. They stop sharing after 1-2 attempts. Fix: real-time dashboard showing clicks, sign-ups, conversions, and pending reward for every referrer.
- **Asking at the wrong moment.** — Referral asks sent during onboarding — before the customer has experienced value — generate low participation. Fix: trigger the ask at the first meaningful activation milestone (first outcome achieved, first positive NPS response), not on day zero.

### [review-platforms](skills/growth/review-platforms/SKILL.md)

- **Annual review drive.** — Grid rewards recency. Fix: monthly cadence.
- **Founder-only responses.** — Looks small. Fix: CS + product owner signatures.
- **Arguing in public.** — Escalates. Fix: empathize + offline.
- **Wrong G2 category.** — Attracts bad-fit reviewers. Fix: recategorize.
- **Ignoring TrustRadius for enterprise.** — G2 alone misses technical depth.

## gtm-ops

### [campaign-governance](skills/gtm-ops/campaign-governance/SKILL.md)

- **No naming conventions.** — Campaign names like `webinar_final_v2` make attribution impossible. Fix: enforce `[Date]-[Segment]-[Channel]-[Content]-[Version]` via CRM validation.
- **UTM chaos.** — Mixed case, hyphens, and one-off sources break warehouse joins. Fix: approved source list + UTM builder only (`references/utm-governance.md`).
- **Governance without consequences.** — Marketers ignore rules if bad data still appears in reports. Fix: exclude non-compliant campaigns from ROI dashboards.
- **Marketing spend invisible to finance.** — Paid campaigns on personal cards. Fix: Ramp caps per program (`gtm-spend-management`).
- **Everyone Responsible, nobody Accountable on launch.** — UTMs ship wrong; CRM empty. Fix: RACI before assets (`skills/gtm-ops/gtm-operations/templates/raci-matrix-template.md`).

### [gtm-operations](skills/gtm-ops/gtm-operations/SKILL.md)

- **Treating RevOps as a re-org.** — Moving people under a new title without integrating data, processes, and KPIs produces an org chart change, not a RevOps function. Fix: per Gartner's definition, build integration of data/process/KPIs first — the structure follows from that.
- **Vague data quality standards.** — "Data is somewhat clean" is unmeasurable and cannot be improved. Fix: map every quality requirement to a DAMA-DMBOK dimension (completeness, uniqueness, timeliness, validity, accuracy, consistency) with a specific threshold and enforcement mechanism.
- **Processes documented but not enforced.** — Stage definitions exist in a Google Doc but CRM has no validation rules, so reps skip required fields. Fix: encode every process gate in CRM validation rules so the system prevents invalid stage changes.
- **Sacrificing long-term capability investment for quarterly targets.** — Forrester's warning: centralized RevOps fails when individual functions feel deprioritized. Fix: separate quarterly tactical metrics from a 12-month capability roadmap; both must be visible to leadership at every monthly review.
- **Projects without RACI or DRI.** — "Everyone's helping" on a launch until UTMs are wrong and nobody owns CRM. Fix: charter + RACI before build; RevOps Accountable on attribution rows.
- **PM tool sprawl.** — Tasks in Slack, docs in Drive, status in email. Fix: SSOT layers in `gtm-organization-principles.md`; one ClickUp List per active project.

### [gtm-spend-management](skills/gtm-ops/gtm-spend-management/SKILL.md)

- **Ramp without register.** — Pretty dashboards; nobody owns Gong renewal. Fix: vendor-spend-register mandatory.
- **Personal card reimbursement.** — Shadow spend invisible to TCO. Fix: policy — GTM tools only on Ramp.
- **One mega card for all SaaS.** — Can't true-down or attribute. Fix: per-vendor virtual cards.
- **Approve tools outside stack audit.** — MarTech tax. Fix: Brinker overlap check before swipe.
- **Ignore credit-based overages.** — Clay/API surprise. Fix: weekly usage alert at 80% cap.
- **Auto-renew without 90-day calendar.** — Fix: Ramp + register reminders; `vendor-contracts` review. ### Phase 4b: Visitor ID Vendor Roster Entries Register deanonymization vendors under `GTM-Data`: | Vendor | ID level | Typical tier | Owner | |---|---|---|---| | Clearbit / HubSpot Breeze | Company | $$–$$$ | RevOps / Marketing | | RB2B | Person | $$ per ID | RevOps / Sales | | 6sense / Demandbase | Company (ABM) | $$$$ | Marketing / RevOps | | Leadfeeder / Dealfront | Company | $–$$ | Marketing | | Warmly / Koala | Person + company | $$–$$$ | Sales / RevOps | Vendor comparison + pilot scorecard: `website-visitor-identification/references/visitor-id-vendor-comparison.md`, `website-visitor-identification/templates/visitor-id-vendor-eval-scorecard.md`. **Approval rule:** Person-level vendors require privacy checklist completion (`visitor-id-privacy-gtm.md`) before spend approval.

### [gtm-tool-cost-model](skills/gtm-ops/gtm-tool-cost-model/SKILL.md)

- **CRM seat creep.** — Unused sales seats. Fix: quarterly true-down audit.
- **Clay credits surprise.** — Fix: cap rows + monitor weekly.
- **Annual prepay all tools.** — Cash crunch. Fix: stagger renewals.
- **Ignoring implementation.** — SF $50K year 1 missing from budget.
- **No allocation to CS/marketing.** — Shared tools need cost split.

### [revops-tech-stack](skills/gtm-ops/revops-tech-stack/SKILL.md)

- **Adding tools before auditing existing ones.** — With 15,000+ vendors (Brinker 2025), the default GTM motion is "there's a tool for that." Fix: run the Phase 1 audit before evaluating any new vendor; close a tool before opening one.
- **Tool decisions driven by tool fashion, not operating model.** — Forrester's warning: revenue tech that doesn't trace to the operating model creates data fragmentation. Fix: every tool in Phase 3 must map to a bowtie stage; if you cannot name the stage, the tool does not belong in the stack.
- **CRM disconnected from the integration hub.** — Data that lives only in sequencing or enrichment tools is invisible to leadership. Fix: enforce the hub-and-spoke model in Phase 4 — every tool either pushes to or pulls from CRM; no closed loops outside the CRM.
- **Asserting savings targets before running the audit.** — "We'll save 20%" stated before utilization is measured is fiction. Fix: compute the savings figure from Phase 2 audit actuals; commit to a target only once the data supports it.

## inbound

### [content-marketing](skills/inbound/content-marketing/SKILL.md)

- **Content without conversion paths.** — A blog post with 10K views and no CTA is a branding expense, not a growth asset. Every piece converts.
- **SEO without AI search.** — As of 2026, AI-powered search (ChatGPT, Perplexity) drives significant B2B traffic. Optimize for both.
- **Volume over strategy.** — 50 average posts lose to 10 excellent ones that build topical authority. Quality clusters > volume.
- **No content updates.** — Stale content loses rankings. Refresh top performers quarterly with new data, examples, and links.
- **Writing for everyone.** — Content that targets "business leaders" targets no one. Write for your specific ICP — their title, their problems, their reading habits.

### [inbound-triage](skills/inbound/inbound-triage/SKILL.md)

- **Manual routing.** — Every minute of manual routing is a minute the lead waits. A lead contacted in 5 minutes is 100x more likely to convert than one contacted in 30 minutes. Automate routing end-to-end.
- **No enrichment before routing.** — Routing an unenriched lead means the SDR wastes time researching basic info. Enrich on form fill automatically.
- **Vague stage definitions.** — When MQL means different things to marketing and sales, leads bounce between teams. Define stages with hard criteria.
- **SLA theater.** — Defining SLAs without tracking and enforcement means they're aspirational. Automate alerting when SLAs are missed.
- **Over-qualifying inbound.** — An inbound lead who took the time to fill a form has already self-qualified to some degree. Don't make them jump through more hoops — get them to a human.

### [landing-pages](skills/inbound/landing-pages/SKILL.md)

- **Feature list as hero.** — Nobody converts because of a feature list. They convert because they believe you understand their problem.
- **Multiple CTAs.** — "Sign up," "Book a demo," "Learn more," "Read case study" — four CTAs means four decisions. One CTA per page.
- **No social proof.** — A page without customer logos or testimonials is asking visitors to trust a stranger. Social proof converts.
- **Long forms.** — Every additional form field reduces conversion by 5-10%. Start with email only. Ask for more later.
- **Ignoring mobile.** — Over 50% of B2B traffic is mobile. A page that's hard to use on mobile loses half its potential conversions.

### [linkedin-algorithm](skills/inbound/linkedin-algorithm/SKILL.md)

- **Optimizing for followers.** — The interest graph killed follower-count reach. Topic authority — consistent pillars, keyword repetition — is the new distribution asset.
- **Posting links in the body.** — The single most common self-inflicted reach penalty. Move links to the first comment or let your profile link convert (Adam Robinson's zero-click pattern).
- **Long-form by default.** — Dwell time is now combined with completion rate. A 2,000-character post most readers abandon scores worse than a sharp 500-character post they finish.
- **Publishing AI-sounding content.** — AI-generated text is measurably penalized in both reach and engagement. Use AI for research and editing, not voice.
- **Treating engagement as optional.** — Ignoring comments in the first hour wastes the algorithm's evaluation window. Nurturing is part of the post, not an afterthought.
- **Chasing every algorithm rumor.** — The report debunks 20 LinkedIn myths per edition. If a tactic isn't backed by data, treat it as folklore.

### [linkedin-live-strategy](skills/inbound/linkedin-live-strategy/SKILL.md)

- **Treating Live as a one-off webinar.** — Without weekly cadence, the algorithm and your network forget the show exists.
- **Over-production paralysis.** — Lizak's origin story started with CEO interviews and a record button — not a studio budget.
- **Skipping repurposing.** — One Live without clips and carousels leaves feed reach on the table (carousels ~1.39x per van der Blom).
- **Monologue mode.** — Ignoring live chat wastes the format's trust advantage.
- **Pitch theater.** — Product demos dressed as conversations kill comment depth.
- **AI voice on repurposed posts.** — Draft with AI, edit for human voice — AI-sounding feed copy is penalized in van der Blom's data.
- **Measuring only viewer count.** — Comment quality, DMs, and 30-day meetings matter more than peak live attendance.

### [sales-navigator-prospecting](skills/inbound/sales-navigator-prospecting/SKILL.md)

- **One script for every filter.** — Wastes the strongest Sales Nav signals; Ingram's 5× pipeline lift illustration comes from filter-message matching.
- **Instant connect after comment.** — Reads as automation; breaks trust.
- **Skipping "viewed your profile" and "following company."** — Highest-intent free signals in the stack.
- **No tenure-based plays.** — New leaders (< 1 year) and month-6–12 operators have different pains — same message misses both.
- **Sales Nav without profile investment.** — Prospects check your profile; empty activity kills accept rates.
- **Attribution only in last-touch CRM.** — LinkedIn pipeline is often dark social — add self-reported source fields.

### [social-selling](skills/inbound/social-selling/SKILL.md)

- **Pitching in the first DM.** — LinkedIn is a relationship platform. Pitching before giving value gets you ignored or blocked.
- **Empty profile.** — A prospect receives your cold email, checks your LinkedIn, and finds 12 connections and a blank about section. Trust destroyed.
- **Posting company content only.** — Prospects follow people, not companies. Post your perspective, your insights, your experience.
- **No Sales Navigator.** — Free LinkedIn is a research tool. Sales Navigator is a prospecting engine. The $99/month pays for itself in one meeting.
- **Inconsistent activity.** — Posting once a month looks like you're not serious. 2-3 posts/week minimum to maintain visibility.

### [website-visitor-identification](skills/inbound/website-visitor-identification/SKILL.md)

- **Person ID without privacy review.** — GDPR/CCPA exposure. Fix: company ID default; person ID only after `visitor-id-privacy-gtm.md` gates + counsel.
- **No ICP filter.** — SDRs chase ISPs, agencies, and universities. Fix: automate `icp-scoring` before any alert or CRM create.
- **Duplicate intent vendors.** — Clearbit + 6sense + Leadfeeder + RB2B all firing. Fix: Brinker consolidation — one company + one person max.
- **Creepy outbound copy.** — "I saw you on our pricing page" destroys trust. Fix: signal-anchored relevance via `cold-email-strategy` — not surveillance tone.
- **Ignoring opt-outs.** — Visitor ID contact opts out on email but stays in RB2B alerts. Fix: suppression sync across CRM, sequencer, Slack enrollment.
- **EU scripts before consent.** — Non-essential tags fire on page load. Fix: `1p-tagging-pixels` consent-first deployment.

## leadmagic

### [leadmagic-bulk-enrichment](skills/leadmagic/leadmagic-bulk-enrichment/SKILL.md)

- **Uploading a dirty CSV.** — Bad inputs create bad matches. Fix: dedupe and normalize before enrichment.
- **Treating unknown as invalid.** — Unknown means no confident result, not bad data. Fix: separate statuses.
- **Exporting every found record.** — Risky/invalid statuses hurt sending. Fix: only eligible statuses enter sequences.
- **No source fields.** — Teams cannot debug data quality later. Fix: write source and timestamp.
- **Blind overwrite.** — Enrichment overwrites rep-maintained CRM data. Fix: field ownership rules.
- **No batch ledger.** — Failed jobs are impossible to replay safely. Fix: log batch ID, record count, status, and retry rule.

### [leadmagic-cli](skills/leadmagic/leadmagic-cli/SKILL.md)

- **Not validating after finding.** — Always run `lm validate` before pushing to a sequence. Found emails can be stale.
- **Batch size too large.** — Stick to 25-50 per batch for reliability. Larger batches risk timeouts.
- **Skipping the verification step.** — Enrichment finds emails. Validation confirms they are deliverable. Two separate steps for a reason.
- **Wrong CSV column mapping.** — Use `--batch-size` to control throughput. Check column auto-detection before running full batches.

### [leadmagic-integrations](skills/leadmagic/leadmagic-integrations/SKILL.md)

- **Two-way sync conflicts.** — Push from enrichment TO CRM, not both directions. CRM-to-enrichment sync creates data conflicts.
- **No verification before send.** — Platform integration handles data movement. Verification handles data quality. Both required.
- **Not using webhooks for real-time.** — Batch processing works for lists. Webhooks enable real-time enrichment on form fill.

### [leadmagic-job-change](skills/leadmagic/leadmagic-job-change/SKILL.md)

- **Generic congratulations.** — It wastes the signal. Fix: connect the move to prior relationship or new-role priority.
- **No account-status logic.** — Same signal means different things for customer vs prospect. Fix: route by account status.
- **Slow outreach.** — Job-change relevance decays quickly. Fix: SLA within 24-48 hours.
- **Ignoring risk.** — Champion departure can threaten renewals and deals. Fix: route customer/opportunity signals to owners.
- **Implying creepy monitoring.** — "We saw you moved" can feel invasive. Fix: keep the note natural and relationship-led.
- **No replacement mapping.** — When a champion leaves, the old account still matters. Fix: identify successor and stakeholder gaps.

### [leadmagic-mcp](skills/leadmagic/leadmagic-mcp/SKILL.md)

- **Treating MCP as magic.** — Tools still need clear jobs. Fix: map tools to workflows.
- **Too many calls.** — Per-record calls waste time and credits. Fix: batch where supported.
- **Skipping status interpretation.** — Found data is not automatically usable. Fix: check status and confidence fields.
- **Hardcoding secrets.** — Config files leak. Fix: environment variables or secret manager.
- **No confirmation gates.** — Agent may mutate systems. Fix: require confirmation for writes and sends.
- **Inventing missing data.** — Empty result means unknown, not permission to guess. Fix: return unknown or ask for more input.

### [leadmagic-waterfall](skills/leadmagic/leadmagic-waterfall/SKILL.md)

- **Skipping verification.** — Even verified-at-lookup emails can go stale. Always re-verify before campaigns.
- **Wrong provider order.** — LeadMagic first (verified results), then fallbacks. A cheaper provider with 20% hit rate costs more per successful lookup than a moderate provider with 70% hit rate.
- **No catch-all handling.** — Enterprise accounts often use catch-all domains. Separate workflow avoids deliverability damage from unverified sends.
- **Claygent without "do not guess" instructions.** — Without explicit prohibition, Claygent constructs pattern-based emails that bounce at 40-60% rates. Always require source URL citation.
- **Enriching before filtering.** — Running email enrichment on non-ICP companies wastes budget. Filter on firmographics first.

## lifecycle

### [churn-prediction](skills/lifecycle/churn-prediction/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [lifecycle-drips](skills/lifecycle/lifecycle-drips/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [mql-nurture](skills/lifecycle/mql-nurture/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [onboarding-sequences](skills/lifecycle/onboarding-sequences/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [re-engagement](skills/lifecycle/re-engagement/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

## management-leadership

### [executive-compensation](skills/management-leadership/executive-compensation/SKILL.md)

- **Bookings-only CRO bonus.** — Pays for bad-fit ARR. Fix: NRR + efficiency gates.
- **No clawback.** — Logo churn 60 days post-close. Fix: 90-day ARR clawback.
- **Hero VP comp.** — Single ARR number, no hiring/ramp gates. Fix: 20% system KPIs.
- **Verbal equity.** — Fix: written grant with board approval date.
- **National non-compete template.** — Unenforceable in many states. Fix: counsel.

### [gtm-leadership](skills/management-leadership/gtm-leadership/SKILL.md)

- **Ruinous empathy.** — Avoiding quota truth until Q4. Fix: weekly pipeline reviews with documented feedback.
- **Firing the number, not the system (leaders).** — Replace VP without fixing role scope. Fix: hire for system-building; 2-quarter runway.
- **No PIP paper trail.** — Legal and moral risk. Fix: written expectations + dates.
- **Comp plans that reward bad revenue.** — Bookings without NRR. Fix: clawbacks, CRO gates at scale.
- **Backchannel skip on leader hires.** — Supervisors lie. Fix: 2+ direct report refs.

### [revenue-team-onboarding](skills/management-leadership/revenue-team-onboarding/SKILL.md)

- **Tools day 5.** — Rep sits idle. Fix: RevOps SLA day 0–1.
- **PDF dump.** — Fix: shadowing + certification.
- **Live sends day 1.** — Brand damage. Fix: certify messaging first.
- **Slack channel sprawl.** — Fix: core 3 channels, expand week 3.
- **No security training.** — SOC2 audit fail. Fix: gate production access.

### [sales-coaching](skills/management-leadership/sales-coaching/SKILL.md)

- **Coaching results, not behaviors.** — "Hit quota" isn't coaching. Fix: REKS layer + one skill.
- **Skipping diagnosis.** — More dials for a knowledge gap. Fix: REKS first.
- **Deal review as storytelling.** — Fix: scorecard + evidence.
- **1:1 as pipeline readout.** — Fix: CRM for status; 1:1 for development.
- **ROI pile-on for indecision.** — Fix: JOLT — recommendation + risk removal.
- **Founder stops coaching after hire #1.** — Fix: meta-coach the manager.

### [team-management](skills/management-leadership/team-management/SKILL.md)

- **Canceling 1:1s.** — "Nothing to discuss this week" = you're not asking the right questions. Fix: Never cancel. Agenda belongs to the report.
- **Saving feedback for review.** — 6 months of saved feedback = "why didn't you tell me this in January?" Fix: Real-time feedback. Radical Candor.
- **Doing instead of delegating.** — "It's faster if I just do it." True today. False tomorrow. Fix: Delegation ladder. 80% as good is good enough.

## outbound

### [cold-calling](skills/outbound/cold-calling/SKILL.md)

- **Conflating two bucketing systems.** — Gilkey dispositions diagnose outcomes; Reisert buckets prioritize daily work — use both, not interchangeably.
- **Calling a loose ICP.** — A call to a marginal-fit prospect converts at 1/5 to 1/10 the rate of a perfect-fit prospect. Narrow the target ruthlessly before the first dial.
- **Dialing stale data.** — Reps lose over 25% of their time to wrong numbers. B2B data decays ~2% per month. Refresh phone numbers quarterly.
- **Pitching instead of diagnosing.** — Reps who pitch on the first call talk past the prospect. Slocum: sell the meeting. Discovery: 11-14 questions.
- **Parallel dialing without phone intent.** — Creates awkward dead-air pauses and burns TAM — carriers flag you as spam.
- **No coordination with email and LinkedIn.** — The phone is one instrument. Each touch should reference the others.
- **Using switchboard numbers.** — 209+ dials per meeting with switchboard numbers vs 30-80 with verified direct dials and phone intent.
- **Activity metrics over outcome metrics.** — 200 dials with 1 conversation loses to 50 dials with 10 conversations. Measure completions and dispositions, not dials alone.
- **Hiring SDRs before ColdCall-Market Fit.** — 9–12 months of guessing vs 50–100 conversation pilot (Pessar).

### [cold-email-copywriting](skills/outbound/cold-email-copywriting/SKILL.md)

- **"My name is X" opening.** — The #1 cold email mistake. The prospect doesn't care who you are until they know why you're relevant. Lead with THEM, not YOU.
- **Too long.** — The optimal cold email is under 80 words. For every 20 words beyond that, reply rates drop by approximately 20%. If you need more space, you're trying to sell in one email — that's what the sequence is for.
- **Feature dumps.** — "Our platform offers A, B, C, D, and E with industry-leading F." Delete. Replace with one proof point: "One customer reduced [pain metric] by [X]%."
- **Fake familiarity.** — "Re:" and "Fwd:" subject lines, overly casual openings, pretending to have met. Prospects see through this instantly. Professional respect beats fake familiarity every time.
- **Wrong awareness level.** — Most cold email is written for solution-aware prospects (Schwartz Tier 3-4), but most prospects are problem-aware or unaware (Tier 1-2). If the prospect doesn't know they have a problem, leading with your solution is irrelevant.
- **No CTA.** — Every email needs a next step. But the CTA must match the relationship stage. Touch 1: a question. Touch 3: "if useful." Touch 6: "would a call make sense?"
- **One-size-fits-all.** — A VP of Engineering and a Director of Marketing should receive fundamentally different emails. If only the company name changes, you're doing Tier 1 when you think you're doing Tier 2.
- **No A/B testing.** — Even great copy degrades. Always deliver at least one subject line variant and one opening line variant per touch.

### [cold-email-strategy](skills/outbound/cold-email-strategy/SKILL.md)

- **Too many touches.** — Beyond 7 touches, each additional touch has negative marginal value. Prospects who haven't responded by Touch 7 are not going to respond to Touch 8. Honor the breakup.
- **Touch 1 product pitch.** — The biggest mistake in cold outreach. Touch 1 should surface a problem, not pitch a solution. If the prospect doesn't agree they have a problem, no amount of product detail helps.
- **Same message, different channel.** — Copy-pasting the email into a LinkedIn DM is not multi-channel — it's annoying. Each channel touch must be written for that channel's conventions.
- **Ignoring sending limits.** — 50 emails/day/mailbox is a hard ceiling. Google and Microsoft enforce this algorithmically. Pushing to 60-70/day gets your domain blacklisted regardless of authentication quality.
- **No trigger branching.** — Sending the same Touch 1 to everyone regardless of signal produces list-blast results. If you're investing in trigger detection, the sequence must reward that investment with signal-specific opening lines.
- **Customer PII in sequences.** — Never paste customer exports, support tickets, or onboarding files into sequencer fields, merge tags, or AI prompt batches. Sequences are for **lawful prospecting data** only — not file exchange. Customer data handling → `references/gtm-data-exchange-playbook.md`. Rep hygiene → `references/gtm-security-hygiene-basics.md`.
- **No A/B testing.** — Sequences degrade over time as prospects see similar messaging from competitors. Without ongoing testing, reply rates trend toward zero over 6-12 months.
- **No governance rules.** — Without clear rules for when to pause or escalate, SDRs default to "keep sending" — which burns domains and annoys prospects.
- **Wrong gap timing.** — 1-day gaps feel aggressive and trigger spam filters. 5+ day gaps lose the prospect's context. 3 days is the research-backed sweet spot.

### [domain-infrastructure](skills/outbound/domain-infrastructure/SKILL.md)

- **Sending from the primary domain.** — This is the cardinal sin of domain infrastructure. A single spam complaint on the primary domain takes down all corporate and transactional email. Never, under any circumstances, send cold email from your primary domain.
- **Too few domains.** — Running all mailboxes on a single domain means one reputation event kills all sending capacity. 3 domains is the minimum for production outbound. 5 is better for volume above 300/day.
- **Too many mailboxes per domain.** — When one mailbox on a domain gets flagged for spam, the domain reputation drops — affecting every mailbox on that domain. Limiting to 2-3 per domain contains the blast radius.
- **Spammy mailbox names.** — `email-marketing@`, `sales-outreach@`, `cold1@` — inbox providers flag these patterns. Use professional, human-looking email addresses.
- **No WHOIS privacy.** — Matching WHOIS registrant info across domains creates an easily identifiable pattern that inbox providers can use to link your domains. A reputation hit on one domain can cascade.
- **Sending from brand-new domains.** — A domain registered yesterday and sending cold email today is a strong spam signal. Inbox providers track domain age. 2 weeks minimum before sending, 90+ days ideal.
- **No tracking domain customization.** — Using the sending platform's default tracking domain puts your deliverability at the mercy of every other user on that shared domain. A spammer on the shared domain damages your reputation.
- **No monitoring before sending.** — Setting up domains and mailboxes without simultaneously setting up Google Postmaster Tools, SNDS, and blacklist monitoring means you're flying blind. You won't know deliverability is broken until open rates collapse.
- **Rotating prospects across mailboxes mid-sequence.** — Moving a prospect from mailbox A to mailbox B in the middle of a sequence breaks thread context, resets engagement history, and looks suspicious. Each prospect stays with one mailbox for the entire sequence.
- **Ignoring DNS propagation time.** — DNS changes can take up to 48 hours to propagate globally. Always verify DNS records after 48 hours. Never start sending immediately after adding DNS records.

### [email-deliverability](skills/outbound/email-deliverability/SKILL.md)

- **Sending cold email from the primary business domain.** — One spam complaint, one blacklisting event, and your transactional emails (password resets, invoices, customer notifications) are broken. This is the #1 deliverability mistake and it is catastrophic when it happens. Always use secondary domains for cold outreach.
- **Skipping warmup.** — A new domain sending 50 emails on Day 1 gets flagged within 48 hours. Google and Microsoft's algorithms interpret sudden volume from a new domain as spam behavior. No amount of authentication quality overrides the volume pattern.
- **Soft DMARC (`p=none`) forever.** — Many teams set `p=none` and never progress to enforcement. This is better than nothing but leaves the domain vulnerable to spoofing. Have a plan to reach `p=reject` within 8 weeks of clean monitoring.
- **Ignoring bounce rate creep.** — A bounce rate that creeps from 1% to 3% over months is easy to miss because it's gradual. But inbox providers catch it. Set a weekly bounce rate review and a hard alert at 3%.
- **No email verification before sending.** — Every unverified address in a sequence is a potential bounce. Bounces above 5% trigger spam filtering at Google and Microsoft, and recovery takes weeks. Always verify before sending.
- **Warmup-only via platform networks.** — The automated warmup networks (warmup pools) are known to inbox providers. They're a supplement, not a replacement. Real engagement from real, diverse contacts builds stronger reputation than automated warmup alone.
- **No DMARC reporting.** — Without `rua` reports, you don't know who is sending on your behalf. You won't catch spoofing attempts, gradual DKIM alignment failures, or misconfigured third-party senders until they cause a deliverability crisis.
- **Too many mailboxes per domain.** — When one mailbox on a domain gets flagged for spam, it affects the domain reputation — which affects all mailboxes on that domain. Limit to 2-3 mailboxes per domain to contain blast radius.

### [inbox-setup](skills/outbound/inbox-setup/SKILL.md)

- **Sending from primary domain.** — One spam complaint and your password resets, invoices, and support emails go to spam too. Never.
- **Too many inboxes per domain.** — 10+ mailboxes on one domain signals bulk sending to spam filters. 2-3 for Google, 25 max for Microsoft.
- **Skipping warmup.** — New domains sent at full volume get blacklisted within 48 hours. There is no shortcut.
- **Sending unverified emails.** — 5%+ bounce rate triggers automated spam filtering. Always verify with a service like LeadMagic Email Validation before sending.
- **No spare capacity.** — If inboxes burn out mid-campaign and you have no spares warming, your pipeline stops. Keep 50% spare capacity.
- **DNS misconfiguration.** — A missing DKIM record or incorrect SPF syntax is caught by every major inbox provider. Triple-check all records.

### [multi-channel-outreach](skills/outbound/multi-channel-outreach/SKILL.md)

- **Identical message across channels.** — Sending the same message via email and LinkedIn DM feels like spam. Each channel should add a new angle.
- **LinkedIn pitch in the connection request.** — It's the equivalent of a cold email with "BUY NOW" in the subject line. Connect first, pitch later.
- **Channel overload.** — 7 touches across 4 channels feels like harassment. 5-8 total touches across all channels combined is the sweet spot.
- **No conditional logic.** — A fixed sequence that fires LinkedIn on Day 3 regardless of email engagement wastes touches. Build conditions.
- **Different channels, different reps.** — When email and LinkedIn come from different people at your company, the prospect is confused. One rep owns the full multi-channel relationship.
- **SMS without consent.** — TCPA (US) and GDPR (EU) require explicit opt-in. SMS to prospects who haven't consented creates legal liability.

### [reply-handling](skills/outbound/reply-handling/SKILL.md)

- **Auto-responding to everything.** — Not every reply needs a response, and a bad auto-response is worse than no response. Categories 7 and 8 should never receive auto-replies. Category 8 replies to an angry prospect with a chipper auto-response is the fastest way to get reported for spam.
- **Slow response to positive replies.** — The #1 destroyer of cold email ROI. A positive reply sits in the inbox for 4 hours while the SDR is in meetings, and the prospect's interest cools. Speed-to-lead must be non-negotiable. 15 minutes is the standard.
- **Arguing with "not interested."** — When someone says they're not interested, they mean it. Responding with "But have you considered..." or "Are you sure?" converts an uninterested prospect into an active detractor who may report you for spam. Accept it immediately and move on.
- **Treating all objections the same.** — "Already have a solution" and "too expensive" are fundamentally different objections that require fundamentally different responses. The first is about capabilities; the second is about value. Responding to both with the same template signals that you're not listening.
- **Missing the referral opportunity in Category 5.** — When someone says "I'm not the right person," they've just given you two gifts: they confirmed you're not wasting more time on them, and they've opened the door to the right person. Always ask for the referral.
- **Not pausing on OOO properly.** — If an out-of-office reply says "returning June 15," and you keep sending emails, you look incompetent and disrespectful. Pause until return date + 2 days.
- **No weekly audit.** — Reply classification accuracy degrades over time as language patterns change and new objection types emerge. A weekly 30-minute audit of reply classifications and response quality prevents silent degradation.
- **Platform mismatch.** — Smartlead's reply category system is powerful but complex. Instantly's is simpler but less granular. Don't try to implement Smartlead-level category complexity on Instantly — it won't work. Match the framework to the platform's actual capabilities.

### [sending-platforms](skills/outbound/sending-platforms/SKILL.md)

- **Choosing based on features, not deliverability.** — A platform with AI copywriting and conditional branching means nothing if the emails land in spam. Deliverability is the first filter, not the last.
- **Underestimating switching costs.** — Migrating between platforms mid-campaign is painful. Data export/import, DNS reconfiguration, sequence recreation, and SDR retraining all take time. Plan migrations during natural pauses in outbound activity.
- **Choosing Apollo for the database, not the sending.** — Apollo's B2B database is valuable, but using it for sending ties your deliverability to Apollo's shared infrastructure. Many teams use Apollo for prospecting and a dedicated sending platform (Smartlead/Instantly) for outreach — best of both worlds but double the cost.
- **Ignoring CRM integration depth.** — "HubSpot integration" means different things on different platforms. Some do one-way push (sequence → CRM), others do bi-directional sync (CRM → sequence updates). If your workflow depends on CRM-driven sequence management, verify the integration depth before committing.
- **Scaling linearly with per-sender pricing.** — Smartlead and Instantly charge per sender (mailbox). At 5 mailboxes, the difference between $33/sender and $37/sender is $20/month. At 50 mailboxes, it's $200/month and growing. Model the cost at your target scale, not your current scale.
- **Not testing deliverability before migrating.** — Before committing to a new platform, set up a test domain and mailbox, run it through warmup, and send test campaigns. Measure inbox placement across Google, Microsoft, Yahoo. Platform claims about deliverability may not match reality for your specific sending profile.
- **Choosing Salesforge for AI copy without human review.** — AI-generated cold email copy varies widely in quality. For high-value personas (C-suite, enterprise), always have a human review and tune AI-generated copy. The AI is a starting point, not a final draft.

## partnerships

### [co-marketing](skills/partnerships/co-marketing/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [integration-partnerships](skills/partnerships/integration-partnerships/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [partnership-strategy](skills/partnerships/partnership-strategy/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

## product-led-growth

### [developer-gtm](skills/product-led-growth/developer-gtm/SKILL.md)

- **Gating docs and pricing.** — Forcing email or "contact sales" to read docs or see price kills evaluation. Developers self-serve or leave (DuVander).
- **Cold-calling/emailing developers.** — Spraying SDR sequences at the technical user breaks trust. Use product signals to reach the buyer thoughtfully; let the developer come to you (Stripe/Common Room).
- **Paywalling the open-source core.** — Restricting the free artifact to force conversion breaks the flywheel. Monetize the extension (hosting, scale, compliance), keep the core free (Next.js → Vercel).
- **Vanity GitHub stars.** — Stars and followers are not adoption. Measure activation, retained usage, and influenced pipeline.
- **Treating DevRel as lead gen.** — A DevRel team on an SDR quota loses credibility with developers. DevRel earns trust; sales closes.
- **Confusing the user with the buyer.** — The developer recommends; the economic buyer signs. Enable the champion, sell the buyer (Verna/Bush hybrid).

### [freemium-optimization](skills/product-led-growth/freemium-optimization/SKILL.md)

- **Optimizing conversion rate instead of full-funnel customers-per-visit.** — A CC-gated trial shows 50%+ conversion but suppresses signup volume 4-6×; end-to-end customer count can be lower than freemium. Fix: always run the full-funnel math before declaring a model "better."
- **Skipping activation instrumentation.** — You cannot improve conversion from an experience users have not completed. Fix: define and instrument the activation event before running any conversion experiment — only 34% of PLG companies currently do this (ProductLed 2025).
- **Free tier that replaces paid.** — If free delivers 90% of what paid delivers, users do not upgrade. Fix: apply the intentionality test — free showcases core value, paid completes the job; deliberate value limits and visible upgrade benefits inside the free experience are required.
- **PQL scoring without routing.** — A model that scores users but triggers no action within a defined time window delivers no revenue lift. Fix: define routing thresholds and response SLAs before launch; OpenView confirms outreach to free signups adds 28% to fast-growth likelihood.

### [plg-strategy](skills/product-led-growth/plg-strategy/SKILL.md)

- **PLG without product readiness** — — 97% want to try before buying, but only if the product delivers value in the trial window.
- **Freemium without conversion path** — — a free tier without a clear upgrade trigger is a cost center, not a growth engine.
- **Blended metrics** — — PLG and sales-led metrics don't mix. Track separately.

## prospecting

### [contact-verification](skills/prospecting/contact-verification/SKILL.md)

- **Skipping verification entirely.** — \"We found the emails from a reputable source.\" Every provider returns stale data. 5-15% of \"found\" emails bounce. The cost of re-warming a domain far exceeds the cost of verification.
- **Treating catch-all as safe.** — Catch-all domains accept mail to any address at the domain, making individual mailbox verification impossible. They produce higher bounce rates. Treat them as a separate, monitored segment.
- **One-time verification.** — \"We verified this list 6 months ago.\" At 2-3% monthly decay, 12-18% of that list is now invalid. Re-verify every 90 days.
- **Sending to invalid emails one more time.** — \"Maybe it was a temporary bounce.\" If verification returns invalid, the mailbox doesn't exist. Sending again won't fix it. Remove permanently.
- **Not updating CRM with verification status.** — Verification without recording the result means the data decays silently. Update CRM fields immediately.

### [data-enrichment-strategy](skills/prospecting/data-enrichment-strategy/SKILL.md)

- **Single-provider lock-in.** — One provider covers 60-75% max. If ZoomInfo is your only source, you're leaving 25-40% of contacts unreachable.
- **Over-buying for the stage.** — $25K/year ZoomInfo contract for a $500K ARR startup is capital misallocation. Start with Apollo, add tools as volume and deal size justify them.
- **No verification in the architecture.** — Enrichment without verification means sending to stale emails. Build verification into the design, not bolted on later.
- **Ignoring data decay.** — Data you enriched 6 months ago is 12-18% stale. Design for recurring enrichment, not one-time projects.
- **Platform as system of record.** — Clay is a workspace, not a CRM. Push enriched data to your CRM and treat it as the source of truth.

### [email-finding](skills/prospecting/email-finding/SKILL.md)

- **Skipping verification.** — Unverified emails cause bounces. Bounces damage sender reputation. Recovery takes weeks. Always verify after finding.
- **Single-provider dependency.** — One provider covers 60-75% max. Running only Apollo leaves 25-40% of contacts unreachable. Always waterfall.
- **Using pattern-guessed emails.** — Constructing firstname.lastname@company.com without confirmation creates 40-60% bounce rates. Never guess. Verify.
- **Running waterfall in wrong order.** — An expensive provider first burns budget on contacts a cheaper provider would have found. Sort by cost-per-hit.
- **Not normalizing company names.** — \"Acme Inc\" vs \"Acme, Inc.\" vs \"Acme Corporation\" create duplicate lookups. Match on domain, not name.
- **No LinkedIn URLs in input.** — Adding LinkedIn URLs improves match rates by 15-25 percentage points across all providers. Run a LinkedIn URL finder column before email finding when URLs are missing.

### [lead-enrichment](skills/prospecting/lead-enrichment/SKILL.md)

- **Sending every record to every provider.** — This is the most expensive enrichment mistake. A proper waterfall means most records exit at Layer 2 or 3, and only the hardest-to-enrich records reach Layer 5. If 80% of your records are enriched at Layers 1-3, you're paying premium provider prices for only 20% of records.
- **Matching on company name instead of domain.** — "Acme Inc." and "Acme Corporation" and "Acme" are the same company but won't match by name. Domain (acme.com) is the stable identifier. Always normalize company names after matching, not before.
- **Confidence scores that are opaque or arbitrary.** — If confidence is always 0.8 or always 0.5, it's not a useful signal. Define specific rules: provider X with fresh data = 0.9 confidence. Provider X with data older than 180 days = 0.6 confidence. AI-inferred = 0.4 confidence. The specific rules are less important than having rules that produce meaningful variance.
- **Normalization that loses information.** — Standardizing "SVP Customer Success" to "VP" loses the functional specialization. Standardize to a taxonomy that preserves both seniority and function. "VP, Customer Success" is better than just "VP."
- **Ignoring data freshness.** — Enrichment data decays. Employee counts change. People change jobs. Technologies change. Every enriched record should have an enriched_date, and downstream systems should have a re-enrichment cadence (recommended: 90 days for active prospects, 180 days for nurture).
- **Same-waferfall for companies and people.** — Company enrichment needs different providers and different fields than person enrichment. The two waterfalls should be configured independently, even if they share some infrastructure.
- **Quality gates that are too permissive or too strict.** — Gates that let everything through defeat the purpose. Gates that block 50% of records create a bottleneck. Target: <5% of records failing quality gates in a mature pipeline. More than 10% indicates a problem in the enrichment waterfall, not in the gate.
- **Not tracking cost per provider.** — Without per-provider cost tracking, you can't optimize the waterfall over time. A provider that costs 3x more but enriches only 2% more records should be removed or moved to a later layer. Cost optimization is continuous.

### [lead-finding](skills/prospecting/lead-finding/SKILL.md)

- **Single-source dependency.** — Relying on Apollo or ZoomInfo alone produces systematic coverage gaps. Apollo underrepresents non-US, non-funded, and traditional-industry companies. Sales Navigator underrepresents very small companies. Crunchbase only covers funded companies. Multi-source is not optional — it's the difference between seeing 60% of your addressable market and seeing 90%+.
- **Using the same search criteria across all sources.** — Each source has its own taxonomy and filters. "Manufacturing" in Apollo is not the same as "Manufacturing" in Sales Navigator. Adapt search criteria to each source's specific categorization system. Test and calibrate.
- **Finding companies but not contacts.** — A list of companies without contacts is a research artifact, not a prospecting list. Every company in the lead list should have at least contact count and, for Tier 1 leads, specific contact names and titles. Use the persona definitions from ICP to guide contact discovery.
- **Accepting database coverage as reality.** — If Apollo returns 500 companies matching your ICP in the US, there are almost certainly more than 500. The database return count is a lower bound, not the actual market size. Use the coverage gaps section to identify where additional sources might surface more leads.
- **Skipping source provenance tracking.** — When a lead turns out to be high-quality (or low-quality), knowing which source it came from is essential for optimizing future lead-finding cycles. Without provenance data, you can't improve your sourcing strategy.
- **Prioritizing volume over quality.** — A list of 5,000 poorly-matched leads is less valuable than 500 precisely-matched leads. Apply ICP criteria aggressively during discovery, not after. It's better to surface fewer, better-matched companies than to dump everything into enrichment.
- **Neglecting vertical-specific sources.** — The B2B databases cover broad markets well but specific verticals poorly. Healthcare companies are better found through hospital directories than Apollo. E-commerce companies are better found through BuiltWith. Always include at least one vertical-specific source.
- **Job board scraping that produces stale data.** — Job postings expire. Conference lists age out. Source data has a half-life. Track the date of data collection per source and flag leads from sources where the data is more than 90 days old for re-verification.

### [list-building](skills/prospecting/list-building/SKILL.md)

- **Enriching before filtering.** — Running $0.15-0.40/contact enrichment on records that fail ICP wastes 30-40% of budget. Filter first always.
- **One giant table.** — Combining company and person data in a single table creates duplication and makes re-enrichment impossible. Separate tables with domain as the join key.
- **No list quality baseline.** — Sending to an unscored list means you can't diagnose why reply rates are low. Score every list before launch.
- **Stale data acceptance.** — A list built 6 months ago has 12-18% decay. Re-verify and re-enrich before launching any campaign on old data.
- **Single-source dependency.** — One source never covers your full TAM. Cross-reference at least two sources and reconcile differences.

### [signal-scoring](skills/prospecting/signal-scoring/SKILL.md)

- **Acting on too many signals per account.** — A company showing 5 signals doesn't mean send 5 different emails. Pick one — the most recent and specific — and lead with it.
- **Weights not calibrated to your data.** — Default weights are a starting point. Review quarterly against your closed-won deals and adjust.
- **Stale signals.** — A funding round from 6 months ago is no longer a trigger. Signal freshness matters. Set expiration windows.
- **No action on signals.** — A signal without an immediate, automated action is just noise. Every detection should trigger a workflow.
- **Equal-weight scoring.** — Not all signals are equal. A company hiring for a role your product directly supports is worth more than a generic intent signal. Weight accordingly.

### [social-intent-monitoring](skills/prospecting/social-intent-monitoring/SKILL.md)

- **Acting on stale signals.** — A competitor mention from last week is not the same as one from yesterday. Set hard freshness windows: recommendation requests expire in 2 hours, most other signals in 24-72 hours. Signals older than 72 hours should go to a low-priority nurture track, not hot outreach.
- **Generic outreach from signal data.** — Running a signal-triggered sequence with the same generic opener you'd send to a cold list defeats the entire point. The signal must appear in the first sentence. If you can't reference it specifically, don't send the email.
- **Enriching before filtering.** — Running every signal through enrichment before checking ICP fit burns credits and slows workflows. Filter by job title and company size using free platform data first; only enrich confirmed ICP-matches.
- **Keyword search too broad.** — Monitoring your own company name or a one-word competitor name without context generates hundreds of irrelevant signals. Use phrase-level queries and negative keyword filters.
- **No feedback loop on signal quality.** — Running signal-led outbound without tracking reply rate by signal type means you never know which signal types are actually worth acting on. Some categories that seem strong (funding signals) often underperform industry-specific problem posts. Measure weekly.
- **Confusing social listening with social selling.** — Social listening is about monitoring what others say publicly (inbound signal collection). Social selling (the `social-selling` skill) is about building your own presence and engaging with your network. They work together but require separate workflows and metrics.

## sales-plays

### [earnings-signal-play](skills/sales-plays/earnings-signal-play/SKILL.md)

- **Reading a summary instead of the actual filing.** — Summaries surface the same bullet points every competitor reads. Fix: pull the 10-K/10-Q from EDGAR directly, run the keyword scan on the full text, and cite section numbers in outreach — it signals to the exec that you did the work.
- **Mining the prepared remarks while ignoring the analyst Q&A.** — The prepared remarks are polished strategy. The Q&A is where analysts press on weak spots and executives respond under pressure. Fix: read the transcript end-to-end; topics that draw multiple analyst questions are the live street concerns — and your discovery angles.
- **Opening with generic "I saw your earnings call" framing.** — This is the default opener from every vendor monitoring the same recap newsletters. Fix: use Reimer's method — mirror the executive's own MD&A language in the subject line and first sentence so it reads as a peer conversation, not vendor outreach.
- **Targeting any VP instead of the initiative owner.** — Sending the same earnings-signal email to all VPs dilutes relevance. Fix: trace the initiative back to a named leader or business unit in Item 1 or the call, and route the email to that specific owner.

### [funding-signal-play](skills/sales-plays/funding-signal-play/SKILL.md)

- **Opening with "Congrats on the raise!"** — This is what every other vendor sends. It signals template outreach, not research. Fix: open with the specific use-of-funds area and connect it to a concrete problem your product solves — in the first sentence, before any acknowledgment of the raise itself.
- **Monitoring only TechCrunch and Crunchbase.** — By the time a round is featured in press coverage, the signal is already 48–72 hours stale for US companies. Fix: add SEC Form D EDGAR alerts — US private companies file Form D shortly after closing, often weeks before press. This is the earliest public detection source available.
- **Acting on funding alone without signal stacking.** — A funding event by itself is a noisy trigger — many funded companies are not in active vendor evaluation. Fix: require at least one corroborating signal before escalating to outreach. Use the stacking rubric in `references/framework-notes.md` to score and prioritize.
- **Contacting the account more than two weeks after the announcement.** — Per Amplemarket's research, funding signals decay after 30–60 days. Vendors who wait lose the urgency frame. Fix: set Crunchbase and EDGAR alerts for same-day notification and assign a daily signal review task — target first touch within 24 hours of stack confirmation, 48 hours maximum.

### [hiring-signal-play](skills/sales-plays/hiring-signal-play/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [job-change-play](skills/sales-plays/job-change-play/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [product-launch-play](skills/sales-plays/product-launch-play/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

## sales-revops

### [buyer-indecision](skills/sales-revops/buyer-indecision/SKILL.md)

- **More ROI when they're scared.** — Increases analysis paralysis. Fix: Limit + Take risk.
- **Single-threaded champion.** — Champion can't de-risk alone. Fix: EB meeting + mutual plan.
- **Unlimited POC.** — No success criteria = infinite stall. Fix: time-boxed pilot with T.
- **Confusing objection with indecision.** — "Too expensive" needs value work; "think about it" after fit needs JOLT.
- **Skipping Judge.** — Applying O/L/T blindly. Fix: score indecision type first.

### [deal-desk](skills/sales-revops/deal-desk/SKILL.md)

- **Discounting without exchange.** — A 20% discount with nothing in return is just leaving money on the table. Always trade.
- **Vague business case.** — "You'll save money" isn't a business case. "Your team spends 40 hours/week on [task] at $X/hour = $Y/year. Our solution reduces that to 10 hours. Annual savings: $Z. Payback: 4 months."
- **Premature pricing discussion.** — Discussing price before establishing value makes every number sound expensive. Value first, price second.
- **One price for everyone.** — Different segments, different willingness- to-pay. A 10-person startup and a 500-person enterprise shouldn't see the same pricing.

### [demo-scripts](skills/sales-revops/demo-scripts/SKILL.md)

- **Feature tour disguised as demo.** — Clicking through every menu item isn't a demo — it's a feature tour. Show workflows, not buttons.
- **Talking about what, not why.** — "Here's our dashboard" vs "Here's how you'll see your team's performance in real time — this view alone saved [customer] 5 hours per week." Always connect feature to outcome.
- **No discovery recap.** — Starting the demo without acknowledging what you learned in discovery tells the prospect you weren't listening.
- **Pitching to one persona in a room of five.** — The CTO and the VP Sales care about different things. Acknowledge all stakeholders.
- **No clear differentiator moment.** — If the prospect can't name one thing only you do after the demo, you failed to differentiate.

### [meeting-prep](skills/sales-revops/meeting-prep/SKILL.md)

- **MEDDICC as a discovery script.** — Running all seven dimensions on a first call feels like an audit. Fix: SPICED first; MEDDICC scores build over calls.
- **Champion = friendly contact.** — Enthusiasm without power is score 1, not 2. Fix: apply Whyte's four-part Champion test.
- **Vendor-defined Metrics.** — "You'll save 30%" is not M=2. Fix: buyer must name the KPI and baseline.
- **Ignoring status quo as Competition.** — "No competitors" still has a competitor: do nothing. Fix: always assess status quo.
- **SPICED and MEDDICC in separate silos.** — Reps capture Impact in SPICED notes but leave Metrics blank. Fix: Impact field populates Metrics in CRM.

### [objection-handling](skills/sales-revops/objection-handling/SKILL.md)

- **Answering before exploring.** — "Too expensive" → "But we're worth it!" The first objection is rarely the real objection. Explore first.
- **Arguing with the prospect.** — "That's not true, actually..." You may win the argument and lose the deal. Acknowledge, then redirect.
- **Generic responses.** — "We have great ROI" isn't an objection response. "Customers in your industry see 3x ROI within 6 months. Here's how [similar company] did it." — that's a response.
- **No competitive objection prep.** — If you know the competitor's cheaper, prepare the response before it comes up. Pre-handling beats reacting.
- **One-size responses.** — A CTO's security objection needs a different response than a VP Sales' budget objection. Tailor by persona.

### [pipeline-management](skills/sales-revops/pipeline-management/SKILL.md)

- **Stages named after rep activity.** — "Demo scheduled" is an action, not a stage goal. Fix: name stages after buyer outcomes; actions live inside the stage.
- **SPICED collected once, never updated.** — SPICED fields go stale. Fix: require re-validation at Proposal stage; Critical Event dates must be current.
- **No conversion metrics.** — You cannot diagnose a broken process without stage-to-stage rates. Fix: baseline conversions, review monthly.
- **Handoff to CS is an email.** — CS starts blind, churn risk spikes. Fix: structured handoff package with SPICED summary and success criteria.
- **Too many stages.** — More than 9 stages creates CRM friction without accuracy gains. Fix: consolidate admin-heavy stages; keep 5–7 for consultative.
- **Process without enablement.** — Reps know the stages but lack talk tracks. Fix: load `sales-enablement` to build playbook assets per stage.

### [sales-enablement](skills/sales-revops/sales-enablement/SKILL.md)

- **One deck for everyone.** — A CTO and a VP Sales care about different things. If your deck works for both, it works for neither.
- **Feature dumps as decks.** — Slides that list features without connecting them to customer problems are skipped. Every slide answers "so what?"
- **No talk tracks in battlecards.** — A feature comparison table without language the rep can actually say in a call isn't a battlecard — it's a reference doc.
- **Assets nobody can find.** — PDFs buried in a Drive folder. Build a single access point (Notion, SharePoint, dedicated Slack channel).
- **Static assets.** — Enablement degrades monthly. Schedule quarterly reviews to update metrics, add new competitors, and retire stale decks.

### [transparency-selling](skills/sales-revops/transparency-selling/SKILL.md)

- **Humblebragging as transparency.** — "We care too much" is not a flaw. "Our reporting module lags behind Looker" is a flaw. If you can't name a specific competitor who does something better, you're not being transparent.
- **Leading with flaws but not context.** — "We're expensive" without "here's why" is just bad marketing. Every flaw must include: who it matters to, who it doesn't, and why your customers still choose you.
- **Transparency as a phase, not a system.** — Doing transparency in the first call and then reverting to traditional selling destroys trust. Consistency is the mechanism — one inconsistency erases ten consistencies.

## tools

### [ai-prompts-toolkit](skills/tools/ai-prompts-toolkit/SKILL.md)

- **"Find their email" Claygent prompts.** — 40–60% bounce from guessed patterns. Fix: require source URL; return empty if not found.
- **Unbounded revise loops.** — LLM iterates forever, burns credits. Fix: max 2 revisions; then human queue.
- **No quality scorer between steps.** — Bad drafts propagate. Fix: P05 score gate ≥7 before human review.
- **Prompt without suppression context.** — AI contacts opted-out accounts. Fix: pass `suppressed: true/false`; halt if true.
- **One prompt does everything.** — Research + draft + send in one call = errors. Fix: use prompt loops with narrow steps.

### [analytics-toolkit](skills/tools/analytics-toolkit/SKILL.md)

- **Direct-to-tool without CDP.** — Send events directly to Amplitude + GA4 + Mixpanel. 3x the implementation. Inconsistent data. Fix: CDP as single source.
- **No server-side tracking.** — Ad blockers kill client-side. Critical events lost. Fix: Server-side Segment for revenue events.
- **Multiple 'source of truth' tools.** — Marketing trusts GA4. Product trusts Amplitude. Numbers disagree. Fix: Data warehouse as single source of truth.

### [clay-loops-toolkit](skills/tools/clay-loops-toolkit/SKILL.md)

- **Enrich all rows.** — Burns credits. Fix: conditional enrich on monitor.
- **Skip LeadMagic verify.** — Bounces destroy domain rep. Fix: verify gate.
- **Mixed signals.** — One loop for funding + hiring. Fix: separate loops.
- **Stale triggers.** — 6-month-old funding. Fix: `signal_date` < 14 days.
- **Claygent for email in loops.** — Expensive + risky. Fix: LeadMagic waterfall; Claygent only for `why_now` copy via `ai-prompts-toolkit` P03/P04.
- **No action routing.** — Alerts pile up. Fix: score → CRM task → owner.

### [clay-toolkit](skills/tools/clay-toolkit/SKILL.md)

- **Flat enrichment (no waterfall).** — One provider. Missed contacts stay missed. Fix: Waterfall. LeadMagic → Apollo → fallback → manual review.
- **Credit burn on bad data.** — Enriching 10,000 contacts with bad names/domains. Fix: Clean data first. Deduplicate. Validate domains before enrichment.
- **No ICP filter before CRM push.** — All contacts pushed to CRM. SDR team overwhelmed. Fix: ICP score column. Only push score > X to CRM.

### [crm-toolkit](skills/tools/crm-toolkit/SKILL.md)

- **Salesforce Leads in HubSpot.** — HubSpot uses lifecycle — don't create parallel objects.
- **CRM before process.** — Stages undefined → reps invent their own. Fix `pipeline-management` first.
- **Two-way Clay sync.** — Conflicts and overwritten fields. One-way push only.
- **Salesforce at $500K ARR.** — Admin tax without RevOps owner. Use Attio/HubSpot until $5M+.
- **Agency without playbook.** — Partners configure chaos faster. Document first.

### [hubspot-sequences](skills/tools/hubspot-sequences/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [instantly-sequences](skills/tools/instantly-sequences/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [leadmagic-toolkit](skills/tools/leadmagic-toolkit/SKILL.md)

- **No waterfall fallback.** — LeadMagic → nothing. Apollo would have found it. Fix: Always chain providers. LeadMagic first. Apollo/Clearbit second.
- **No webhook for bulk.** — Poll status in a loop. Timeout. Job lost. Fix: Webhook callbacks. Job ID → webhook notifies on completion.
- **Hard-coding API keys in n8n.** — Committed to repo. Leaked. Fix: n8n credentials store. Environment variables. Never hard-code.

### [lemlist-setup](skills/tools/lemlist-setup/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [n8n-toolkit](skills/tools/n8n-toolkit/SKILL.md)

- **n8n as spreadsheet.** — Rebuilding Clay waterfalls row-by-row in n8n costs more to maintain. Fix: Clay enriches; n8n routes and syncs.
- **Unauthenticated webhooks.** — Public URL gets spammed; CRM fills with junk. Fix: HMAC verification node first step.
- **No idempotency.** — Form double-submit creates duplicate contacts. Fix: `event_id` or email hash check in Redis/Sheet before create.
- **Agent auto-sends via n8n.** — Compliance and brand risk. Fix: MCP-01 requires `approval_token`; sends stay in sequencer with human review.
- **One giant workflow.** — 40 nodes, unmaintainable. Fix: sub-workflows per enrich, CRM, notify.
- **Silent failures.** — Error branch empty. Fix: global Error Trigger + row log.
- **Mixed signal routing.** — One branch for all signals. Fix: Switch on `signal_type`; load play skill per type.

### [outreach-sequences](skills/tools/outreach-sequences/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [salesloft-cadences](skills/tools/salesloft-cadences/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [sequencing-toolkit](skills/tools/sequencing-toolkit/SKILL.md)

- **No warmup.** — New mailbox sends 50 emails/day day 1. Spam folder. Burned domain. Fix: 2-week warmup. Start at 5/day. Increment slowly.
- **One mailbox doing everything.** — 200 emails/day from one mailbox. Instant spam. Fix: Multiple mailboxes per domain. 30/day per mailbox max.
- **No A/B testing.** — Same copy forever. Ignorance about what works. Fix: Always run at least one A/B test per sequence.

### [smartlead-workflows](skills/tools/smartlead-workflows/SKILL.md)

- **Skipping research.** — Building output without understanding the specific context. Fix: always gather required inputs before producing deliverables.
- **Generic output.** — "Improve your process" without concrete steps. Fix: every recommendation must include a specific action, timeline, and owner.
- **Missing framework citations.** — Advice without named authorities. Fix: ground every recommendation in a cited framework from a recognized authority.

### [support-toolkit](skills/tools/support-toolkit/SKILL.md)

- **AI agent launched without training data.** — 5 help articles → 70% wrong answers → frustrated customers. Fix: 30+ articles. Test with 50 questions.
- **Chat widget on every page.** — Noise. Distraction. Fix: Pricing, help center, and post-signup only.
- **No SLAs.** — "We respond quickly" = no commitment. Fix: Specific FRT targets by priority. Measured. Reported. Reviewed weekly.

---
name: sending-platforms
description: >-
  Compares, selects, and configures cold email sending platforms: Smartlead,
  Instantly, Salesforge, Apollo, and others. Use when the user asks which
  sending platform to use, needs to compare features or pricing, wants to
  migrate between platforms, or needs platform-specific setup guidance.
  Activates on phrases like "which email platform," "Smartlead vs Instantly,"
  "best sending tool," "Salesforge setup," "Apollo sequences," or
  "migrate sending platform."
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: outbound
  tags: [sending-platforms, smartlead, instantly, salesforge, apollo]
  related_skills:
    - cold-email-strategy
    - email-deliverability
    - domain-infrastructure
    - reply-handling
  frameworks: []
---

# Sending Platforms

## Overview

Choosing a cold email sending platform is not a feature-comparison exercise.
It is a business decision that determines your deliverability ceiling, your
workflow efficiency, and your ability to scale. The wrong platform choice
costs you thousands of emails that never reach the inbox — and you won't know
it until open rates collapse.

This skill compares the four major cold email sending platforms — Smartlead,
Instantly, Salesforge, and Apollo — across the dimensions that matter: pricing,
warmup quality, API access, CRM integration, sequence capabilities, analytics,
and deliverability infrastructure. It also covers setup guidance for each
platform and a decision matrix for different use cases (solo founder, SDR team,
enterprise outbound).

The non-obvious rule: the platform with the most features is not the best
platform. The best platform is the one with the most reliable inbox placement
for YOUR specific sending profile (volume, industry, email provider mix). A
platform with excellent Gmail deliverability but poor Outlook deliverability
is the wrong choice if 60% of your targets use Outlook.

## When to Use

- User asks "which email sending platform should I use" or "Smartlead vs
  Instantly" → activate this skill
- User says "compare sending platforms" or "evaluate email tools" →
  activate this skill
- User wants to "migrate from Apollo to Smartlead" or "switch sending
  platforms" → activate this skill
- User asks "how to set up [platform]" or "configure [platform] for
  cold email" → activate this skill
- User mentions platform-specific features: "unibox," "email warmup,"
  "spintax," "smart lead rotation" → activate this skill
- User asks about "API integration" or "CRM sync" for sending platforms →
  activate this skill

Do NOT use for:
- Buying domains and mailboxes → use `domain-infrastructure`
- Configuring SPF/DKIM/DMARC → use `email-deliverability`
- Writing email copy → use `cold-email-copywriting`
- Designing sequences → use `cold-email-strategy`
- Handling replies → use `reply-handling`

## Authoritative Foundations

This skill draws from the following:

- **Smartlead Documentation** — Official documentation on sequence configuration,
  category-based reply handling, master inbox (Unibox), API, and deliverability
  features. Smartlead's category-based reply classification and auto-responder
  system is the most sophisticated in the market.

- **Instantly Documentation** — Official docs on campaign management, warmup
  pool, Deliverability Score, and analytics. Instantly has the largest warmup
  pool and the most mature warmup infrastructure.

- **Salesforge Documentation** — Official docs on AI-powered personalization,
  mailbox management, and deliverability. Salesforge's AI copywriting and
  personalization features are unique in the market.

- **Apollo.io Documentation** — Official docs on sequences, data enrichment,
  and CRM integration. Apollo is unique in combining a B2B database with a
  sending platform, making it a one-stop shop for prospecting + outreach.

- **ColdIQ — Platform Reviews and Benchmarks** — Independent testing data
  comparing deliverability, features, and user experience across platforms.
  ColdIQ's head-to-head tests inform the deliverability comparison section.

## Prerequisites

- Run `domain-infrastructure` first if you don't yet have domains and mailboxes
  — the platform selection depends on your infrastructure
- Run `cold-email-strategy` first if you need to define your sequence
  architecture before selecting a platform
- Required user inputs: daily sending volume, number of mailboxes, budget,
  CRM in use, technical capability of the team, whether SDRs will use the
  platform directly
- Reference files: `references/deliverability-primer.md` for sending limits
  that affect platform choice

## Step-by-Step Process

### Phase 1: Intake

Gather the following from the user. Ask all questions at once:

1. **Daily sending volume:** How many emails per day total? Per mailbox?
2. **Number of mailboxes:** How many sending mailboxes are currently set up
   or planned?
3. **Monthly budget per seat:** What's the acceptable cost per user/SDR?
4. **CRM:** Which CRM do you use (Salesforce, HubSpot, Attio, Pipedrive, none)?
5. **SDR team structure:** How many SDRs? Will they use the sending platform
   directly or will sequences be managed centrally?
6. **Technical capability:** Is there someone who can handle API integrations
   and DNS configuration, or do you need an all-in-one, low-config solution?
7. **AI needs:** Do you need AI-powered copywriting, personalization, or reply
   handling? Or will a human write everything?
8. **Data needs:** Do you need a built-in prospect database (like Apollo) or
   do you bring your own lists?
9. **Current platform:** If migrating, what platform are you on now? What's
   not working?
10. **Target inboxes:** Roughly what percentage of your targets use Gmail
    vs Outlook vs other? This affects deliverability priorities.
11. **Compliance requirements:** GDPR, SOC 2, any data processing requirements?

### Phase 2: Research

Before making a recommendation, verify current state:

1. **Check current pricing:** Platform pricing changes frequently. Verify
   current pricing on each platform's website before making a recommendation.
   Smartlead, Instantly, and Salesforge typically offer monthly and annual
   plans. Apollo has a free tier with limits.

2. **Check integration status:** Verify that the user's CRM is still supported
   by the candidate platforms. CRM integrations change as platforms add or
   deprecate connectors.

3. **Check deliverability benchmarks:** Review recent (within 3 months)
   independent deliverability tests comparing the platforms. ColdIQ and
   other testing labs publish periodic head-to-head comparisons.

4. **Audit current platform (if migrating):** If the user is on a platform
   and wants to switch, audit what's broken:
   - Deliverability issues? (may not be the platform's fault)
   - Missing features?
   - Too expensive?
   - Poor UX?
   - Lack of support?
   The answer determines whether migration is worth the switching cost.

### Phase 3: Execution

#### Step 1: Platform Comparison

Compare the four major platforms across key dimensions:

**Smartlead**

Strengths:
- Best-in-class reply handling: 25+ auto-detected reply categories with
  automated actions (meeting booked, not interested, out of office, wrong
  person, etc.)
- Master Inbox (Unibox): All replies from all mailboxes in one unified
  inbox — eliminates the need to log into 20+ Gmail accounts
- API-first design: Strong API for custom integrations, webhooks for
  real-time events, Zapier/Make integration
- Advanced sequence logic: Conditional branching based on reply categories,
  email open behavior, link clicks
- Multi-channel: Email + LinkedIn + calls + SMS in one sequence
- CRM integrations: HubSpot, Salesforce, Pipedrive, Close, and more
- Deliverability features: Custom tracking domain, IP rotation for high
  volume, spam word checker, inbox rotation

Weaknesses:
- Higher learning curve due to feature depth
- Per-sender pricing adds up at scale (cost scales linearly with mailboxes)
- Warmup is effective but smaller warmup pool than Instantly
- UI can be overwhelming for beginners
- Customer support can be slow during peak periods

Best for: Teams running sophisticated multi-channel sequences who need
granular reply automation and API-driven workflows. Best for organizations
with 5+ mailboxes and a dedicated ops person.

Pricing (approximate, verify current):
- ~$33-94/month per sender depending on plan
- Volume-based plans available for high volume

**Instantly**

Strengths:
- Largest warmup pool: 200,000+ warmup accounts, the most mature warmup
  infrastructure in the market
- Deliverability focus: Deliverability Score, spam word detection, inbox
  placement testing built in
- Simple UX: Cleaner, more intuitive interface than Smartlead — faster
  to onboard new SDRs
- Campaign analytics: Good dashboard for open rates, reply rates,
  opportunity rates
- Unibox: Similar unified inbox concept
- Workspace management: Easier multi-client management for agencies
- Lead Finder: Built-in prospecting database (acquired via lead database
  integrations)

Weaknesses:
- Reply handling less sophisticated than Smartlead (fewer auto-detected
  categories)
- API less mature — fewer webhook events, less customization
- Sequence logic simpler — less conditional branching
- LinkedIn automation less integrated
- CRM integrations narrower than Smartlead
- AI features less developed

Best for: Teams prioritizing deliverability and warmup above all else.
Agencies managing multiple clients. Teams that want a simpler interface
and faster onboarding. Best for 3-10 mailbox setups.

Pricing (approximate, verify current):
- ~$37-97/month for growth plans
- Agency/enterprise plans for high volume

**Salesforge**

Strengths:
- AI copywriting: Built-in AI for generating and personalizing email copy
  at scale — unique in the market
- Multi-language: Supports 30+ languages for AI-generated copy
- Mailbox management: Strong mailbox provisioning and management features
- AI warmup: AI-driven warmup that adapts to engagement patterns
- Personalization: AI-generated personalization at the per-lead level
  (approaching Tier 3 without manual effort)
- Unified inbox: Reply management from all mailboxes
- Competitively priced for the feature set

Weaknesses:
- Newer platform — smaller user base, less battle-tested
- Smaller warmup pool than Smartlead or Instantly
- Fewer CRM integrations (HubSpot, Salesforce primarily)
- API still maturing
- Less community content and third-party tutorials
- AI-generated copy quality varies — needs human review for important
  personas

Best for: Teams that want AI-powered personalization without building
custom AI workflows. International outreach in multiple languages. Teams
comfortable being early adopters of a newer platform.

Pricing (approximate, verify current):
- ~$36-96/month per sender
- AI features included in higher-tier plans

**Apollo.io**

Strengths:
- Built-in B2B database: 275M+ contacts with firmographic, technographic,
  and contact data — no separate prospecting tool needed
- All-in-one: Prospecting + enrichment + sequencing + analytics in one
  platform
- Excellent CRM integration: Deep Salesforce and HubSpot integration
  with bi-directional sync
- Free tier: Generous free tier for low-volume users
- Sequences: Good sequence builder with A/B testing
- Analytics: Strong reporting on sequence and rep performance
- AI: AI-powered email writing assistant, scoring, and recommendations
- Dialer: Built-in dialer for cold calling within the same platform

Weaknesses:
- Email sending is secondary to their database business — deliverability
  features are less sophisticated than dedicated sending platforms
- Shared sending infrastructure — your deliverability is partially tied
  to Apollo's overall reputation
- No custom tracking domain in lower tiers
- Limited warmup control — Apollo manages warmup automatically but with
  less transparency
- Less granular sequence logic than Smartlead
- Higher cost at scale when combining database + sending
- Data quality varies — the database is large but accuracy is inconsistent

Best for: Teams that want an all-in-one solution (database + outreach).
SDR teams already using Apollo for prospecting. Budget-constrained teams
that can use the free tier. Teams that prefer fewer tools even at the
cost of some deliverability optimization.

Pricing (approximate, verify current):
- Free tier: Limited sequences and credits
- Basic: ~$49/user/month
- Professional: ~$79/user/month
- Organization: ~$119/user/month (advanced features)

**Other Notable Platforms:**

- **Lemlist:** Strong on personalization (custom images, video). Lower
  deliverability than dedicated platforms. Good for creative outreach.
- **Woodpecker:** Simple, reliable email automation. Good deliverability.
  Limited multi-channel. Good for agencies.
- **Mailshake:** Simple email outreach. Good for low-volume, simple
  sequences. Limited advanced features.
- **Reply.io:** Multi-channel (email, calls, LinkedIn, SMS). Good CRM
  integration. Mid-range deliverability.
- **Close:** CRM-first platform with built-in sequences. Good for teams
  using Close as their CRM.
- **Outreach.io:** Enterprise-grade sales engagement platform. Best for
  50+ SDR teams. Expensive. Full-featured.

#### Step 2: Decision Matrix

Apply the decision matrix based on user's specific needs:

| Scenario | Recommended Platform | Rationale |
|----------|---------------------|-----------|
| Solo founder, <100 emails/day, budget-conscious | Apollo (free tier) | Free, includes prospecting database |
| Solo founder, 100-300 emails/day, deliverability priority | Instantly | Best warmup, good deliverability for small setups |
| 2-5 SDR team, reply automation priority | Smartlead | Best reply categorization and automation |
| 2-5 SDR team, AI personalization priority | Salesforge | Unique AI copywriting and personalization features |
| Agency managing multiple clients | Instantly | Best workspace management and client separation |
| Enterprise, 10+ mailboxes, API-driven | Smartlead | Best API, webhooks, customization |
| International multi-language outreach | Salesforge | 30+ language AI copywriting |
| All-in-one (DB + outreach), fewer tools | Apollo | Built-in B2B database |
| Maximum deliverability above all else | Instantly + Smartlead warmup | Largest warmup pool |
| LinkedIn-heavy multi-channel | Smartlead | Best multi-channel sequence orchestration |
| Transitioning from basic tool, want to upgrade | Smartlead or Instantly | Both are step-ups from Mailshake/Woodpecker |

#### Step 3: Platform-Specific Setup Guidance

**Smartlead setup checklist:**
1. Connect mailboxes via SMTP/IMAP or OAuth
2. Configure custom tracking domains for each sending domain
3. Set up SPF/DKIM/DMARC as documented in `email-deliverability`
4. Start warmup (2-4 week program)
5. Create client/project workspace
6. Import prospects (CSV or API)
7. Build sequence with conditional logic
8. Configure reply categories and auto-actions
9. Set up CRM integration for bi-directional sync
10. Configure webhooks for real-time event handling
11. Set up Unibox for unified reply management
12. Test sequence with internal addresses first
13. Go live with low volume, scale up gradually

**Instantly setup checklist:**
1. Connect mailboxes (direct integration or SMTP)
2. Configure custom tracking domains
3. Set up SPF/DKIM/DMARC
4. Activate warmup (Instantly's warmup pool)
5. Monitor Deliverability Score daily during warmup
6. Create campaign with email accounts assigned
7. Import leads (CSV or API)
8. Build sequence (simpler than Smartlead — linear sequences)
9. Set up reply detection and labeling
10. Connect CRM for contact/activity sync
11. Configure Unibox for reply management
12. Test internally, go live with gradual scaling

**Salesforge setup checklist:**
1. Connect mailboxes
2. Configure custom tracking domains
3. Set up SPF/DKIM/DMARC
4. Enable AI warmup
5. Import leads or use built-in database
6. Configure AI personalization settings (language, tone, variables)
7. Build sequence with AI-generated or manual copy
8. Set up reply handling
9. Connect CRM for sync
10. Test AI-generated copy with internal addresses
11. Go live gradually

**Apollo setup checklist:**
1. Create Apollo account and connect CRM
2. Set up email integration (Google Workspace or M365 OAuth)
3. Configure sending schedule and limits
4. Set up email tracking and open/click detection
5. Build prospect lists using Apollo's database filters
6. Create sequence with templates
7. Configure rules (auto-advance on reply, pause on bounce)
8. Set up analytics dashboard
9. If using Apollo's dialer: configure phone integration
10. Test sequence internally
11. Go live

#### Step 4: Migration Plan (if applicable)

If migrating between platforms:

1. **Export data from old platform:** Export all active sequences, templates,
   prospect lists, reply data, and analytics.
2. **Audit active prospects:** Identify prospects currently mid-sequence.
   These are the most sensitive — a botched migration breaks their sequence
   experience.
3. **Map sequences:** Recreate the sequence architecture in the new platform
   before migrating prospects.
4. **Transfer prospects:** Import prospect lists, noting any that are
   mid-sequence. For mid-sequence prospects, either:
   - Complete the sequence on the old platform, only migrate new prospects (safest)
   - Restart sequences on the new platform with a note acknowledging the transition
   - Resume at the equivalent touch number (risky — the platforms' sequence
     models may not align perfectly)
5. **Transfer mailboxes:** Connect the same mailboxes to the new platform.
   Do NOT create new mailboxes for the migration — the reputation of existing
   mailboxes is an asset.
6. **Transfer tracking domains:** Re-point tracking CNAME records to the new
   platform's tracking endpoint.
7. **Test thoroughly:** Send test sequences to internal addresses through
   the new platform before migrating live prospects.
8. **Run parallel (if possible):** Keep the old platform running for
   mid-sequence prospects while starting new prospects on the new platform.
9. **Decommission old platform:** Only after all mid-sequence prospects have
   completed or been paused.

### Phase 4: Delivery

Deliver a platform recommendation with setup plan:

1. **Recommendation:** Which platform, which plan, why.
2. **Comparison summary:** Key differentiators for the user's specific needs.
3. **Setup checklist:** Platform-specific step-by-step setup guide.
4. **Integration plan:** CRM connection, API/webhook configuration, data flow.
5. **Migration plan (if applicable):** Step-by-step migration from current
   platform.
6. **Cost projection:** Monthly and annual cost at the user's scale.
7. **Risk factors:** What could go wrong with this platform choice and how
   to mitigate.

## Output Format

```markdown
# Sending Platform Recommendation for [Company]

## Current State
[Volume, mailboxes, CRM, team, budget, constraints]

## Recommendation: [Platform] — [Plan]
**Why this platform:** [3-5 key reasons specific to this user]

## Comparison Summary
| Dimension | Smartlead | Instantly | Salesforge | Apollo | Winner |
|-----------|-----------|-----------|------------|--------|--------|
| Deliverability | [rating] | [rating] | [rating] | [rating] | [platform] |
| Warmup | [rating] | [rating] | [rating] | [rating] | [platform] |
| Reply handling | [rating] | [rating] | [rating] | [rating] | [platform] |
| API/Integrations | [rating] | [rating] | [rating] | [rating] | [platform] |
| CRM integration | [rating] | [rating] | [rating] | [rating] | [platform] |
| AI features | [rating] | [rating] | [rating] | [rating] | [platform] |
| Multi-channel | [rating] | [rating] | [rating] | [rating] | [platform] |
| Ease of use | [rating] | [rating] | [rating] | [rating] | [platform] |
| Cost at your scale | $[X] | $[X] | $[X] | $[X] | [platform] |
| Best fit for you | [why] | [why] | [why] | [why] | [platform] |

## Setup Checklist
- [ ] Step 1
- [ ] Step 2
[Full checklist from Step 3 above]

## Integration Plan
[CRM connection, API/webhook configuration, data flow diagram]

## Migration Plan (if applicable)
[Step-by-step migration with risk mitigation]

## Cost Projection
| Item | Monthly | Annual |
|------|---------|--------|
| Platform subscription | $[X] | $[X] |
| Additional mailboxes (if platform charges per mailbox) | $[X] | $[X] |
| Total | $[X]/mo | $[X]/yr |

## Risk Factors and Mitigations
1. **Risk:** [description]
   **Mitigation:** [action]
```

## Quality Check

Before delivering, verify:

- [ ] Have you verified current pricing on each platform's website?
- [ ] Is the recommendation justified for the user's specific volume, team
  size, CRM, and budget — not a generic "best platform" answer?
- [ ] Have you addressed ALL four major platforms in the comparison?
- [ ] Does the setup checklist include DNS configuration, mailbox connection,
  tracking domain setup, warmup, and testing?
- [ ] Is the migration plan (if applicable) safe for mid-sequence prospects?
- [ ] Are cost projections complete and based on verified current pricing?
- [ ] Are platform weaknesses honestly stated, not glossed over?
- [ ] Does the risk section address the specific downside of the recommended
  platform?
- [ ] Is the decision matrix applied to the user's specific scenario?

## Common Pitfalls

1. **Choosing based on features, not deliverability.** A platform with AI
   copywriting and conditional branching means nothing if the emails land
   in spam. Deliverability is the first filter, not the last.

2. **Underestimating switching costs.** Migrating between platforms mid-campaign
   is painful. Data export/import, DNS reconfiguration, sequence recreation,
   and SDR retraining all take time. Plan migrations during natural pauses
   in outbound activity.

3. **Choosing Apollo for the database, not the sending.** Apollo's B2B database
   is valuable, but using it for sending ties your deliverability to Apollo's
   shared infrastructure. Many teams use Apollo for prospecting and a dedicated
   sending platform (Smartlead/Instantly) for outreach — best of both worlds
   but double the cost.

4. **Ignoring CRM integration depth.** "HubSpot integration" means different
   things on different platforms. Some do one-way push (sequence → CRM),
   others do bi-directional sync (CRM → sequence updates). If your workflow
   depends on CRM-driven sequence management, verify the integration depth
   before committing.

5. **Scaling linearly with per-sender pricing.** Smartlead and Instantly
   charge per sender (mailbox). At 5 mailboxes, the difference between
   $33/sender and $37/sender is $20/month. At 50 mailboxes, it's $200/month
   and growing. Model the cost at your target scale, not your current scale.

6. **Not testing deliverability before migrating.** Before committing to a
   new platform, set up a test domain and mailbox, run it through warmup,
   and send test campaigns. Measure inbox placement across Google, Microsoft,
   Yahoo. Platform claims about deliverability may not match reality for
   your specific sending profile.

7. **Choosing Salesforge for AI copy without human review.** AI-generated
   cold email copy varies widely in quality. For high-value personas
   (C-suite, enterprise), always have a human review and tune AI-generated
   copy. The AI is a starting point, not a final draft.

---
name: social-intent-monitoring
description: >-
  Build a social intent monitoring system that turns public social conversations
  into qualified outbound triggers. Use when the user wants to monitor LinkedIn,
  X, Reddit, or other platforms for buying signals — competitor engagement,
  hiring intent posts, pain-point mentions, funding reactions, or public
  recommendation requests — and automatically route those signals into outreach
  workflows. Triggers on: "social listening", "social signals", "monitor LinkedIn
  for intent", "Trigify", "agentic social listening", "competitor mention
  monitoring", "social intent", "signal-led outbound", "signal infrastructure",
  "social buying signals", or any request to detect intent from public social
  content.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: prospecting
  tags: [signals, social-listening, intent, outbound, trigify, agentic]
  related_skills: [signal-scoring, lead-enrichment, hiring-signal-play, multi-channel-outreach]
  frameworks:
    - "Max Mitchum — Signal, Context, Action Framework (Trigify)"
    - "Trigify Workflow Patterns — Agentic Social Listening"
    - "ColdIQ Signal Taxonomy — Trigger-Based Selling"
---

# Social Intent Monitoring

## Overview

Most outbound programs are volume-gated rather than timing-gated. Reps build
lists and send sequences regardless of whether anything has actually happened.
Social intent monitoring replaces that model: an AI agent watches public
social conversations continuously, and an email or DM only fires when a
qualifying event occurs in real time.

The mistake this skill prevents: treating social platforms as broadcast
channels rather than signal feeds. Every competitor-mention comment, every
"does anyone have a recommendation for X" post, every founder publicly
describing a problem you solve — these are live intent signals that expire
within 24-72 hours. Catching them and acting fast beats the best cold copy
by a wide margin.

This skill builds the full monitoring architecture: what to watch, how to
qualify signals, how to route them to enrichment and outreach tools, and
how to measure signal quality over time.

## When to Use

- "Set up social intent monitoring for our target accounts"
- "Monitor LinkedIn for people talking about problems we solve"
- "Build a Trigify workflow that routes competitor mentions to outreach"
- "Detect social buying signals before prospects fill out a form"
- "Create a signal infrastructure for our outbound motion"
- "How do I use social listening for lead generation?"
- "Set up keyword monitoring on LinkedIn and X for intent"
- "Automate outreach from social signals"

## Authoritative Foundations

### Max Mitchum — Signal, Context, Action Framework

Max Mitchum, Co-Founder & CEO of Trigify.io, published the Signal, Context,
Action model as the operating framework for signal-led outbound. The three
layers:

**Signal** — the public event that suggests an account is worth contacting
now. Examples from Mitchum's 2026 playbook: competitor engagement on LinkedIn
or X, hiring posts for GTM roles, founder or operator posts describing a
problem you solve, funding reactions, pain-point mentions in comments, product
launches in adjacent categories, public recommendation requests.

**Context** — the judgement layer. Who is this person? What company? Are they
in ICP? Why does this specific event matter? Is the timing strong? A signal
without context is noise; context without a signal is guessing.

**Action** — the downstream workflow. Enrich the person, find the email,
research the company, draft the message anchored to that specific signal,
push into the sequencer, alert the rep in Slack with the reasoning.

Source: https://maxmitcham.substack.com/p/48-meetings-from-120-leads-in-two

The core principle: the email is the commodity. AI can write decent emails.
The moat is knowing when the email has a reason to exist.

### Trigify Workflow Patterns

Trigify's public documentation describes four canonical agentic workflow
patterns for sales and lead generation teams:

1. **ICP-Filtered Post Trigger**: New Post Trigger → Person Enrichment →
   ICP filter (country, headcount) → Email Enrichment → deliverability check
   → CRM or email campaign push.

2. **Viral Engager Harvesting**: Post with high engagement threshold detected
   → fetch all engagers → Person Enrichment → filter for VP/Director titles
   → CRM or agent memory.

3. **Inbound Lead Routing by Seniority**: Webhook trigger → Person Enrichment
   using LinkedIn URL → seniority check → high-value: Slack alert to sales
   team; others: nurture sequence.

4. **Competitor Mention Monitoring**: Track competitor mentions → enrich
   mentioner → ICP filter → route to warm outreach sequence.

Source: https://help.trigify.io/en/articles/8836198-draft-common-workflow-patterns

### ColdIQ Signal Taxonomy

ColdIQ's published trigger-selling taxonomy classifies intent signals into
four tiers: Hiring signals, Funding signals, Tech Stack changes, and
Behavioral intent (website visits, content engagement, review site activity).
Social listening adds a fifth tier — Public Conversation signals — not
captured by traditional data providers. Each tier requires different outreach
timing and angle.

## Prerequisites

- Target account list (CRM, CSV, or HubSpot/Salesforce export)
- ICP criteria defined (firmographic + role criteria for signal filtering)
- Social listening platform configured (Trigify recommended; alternatives:
  Brandwatch, Mention, Keywordsio for simpler setups)
- Enrichment provider for email and firmographic lookup (LeadMagic, Apollo,
  Clay waterfall)
- Outreach tool connected (Instantly, Smartlead, Salesloft, or HubSpot
  sequences)
- Slack or CRM for internal signal routing and rep alerts

## Step-by-Step Process

### Phase 1: Define Your Signal Taxonomy

Decide which social signals are worth acting on for your business. Not all
conversations are buying signals. The highest-value signals:

| Signal Type | Description | Urgency | Outreach Angle |
|---|---|---|---|
| **Competitor engagement** | Prospect comments on, likes, or shares competitor content | High — 24-48hr window | Offer comparison, address common pain with that competitor |
| **Problem statement post** | Founder or operator publicly describes a problem you solve | High — act within 12 hrs | Reference their exact words; offer a specific solution |
| **Recommendation request** | "Does anyone have a recommendation for X?" | Very High — act within 2 hrs | Direct reply + personal DM |
| **Hiring for GTM role** | Post about hiring SDR, RevOps, VP Sales — roles your product supports | Medium — 3-5 day window | Tie outreach to the hiring intent; new hires evaluate tools |
| **Funding reaction post** | Company or founder posts about closing a round | Medium — 1 week window | Congratulate + connect to common post-funding challenges |
| **Pain-point comment** | Target prospect comments on someone else's post about a problem | High — act within 48 hrs | Reference the comment thread; show understanding |
| **Content engagement pattern** | Prospect consistently engages with content in your category | Low/Medium — warm long-play | Nurture track; add to account monitoring |

Mitchum's rule: only act on signals where you can write a specific, non-generic
opening that references exactly what happened. If the signal can't anchor the
first line of the message, it's not a strong enough trigger.

### Phase 2: Configure Social Listening

**Using Trigify (full agentic workflow):**
1. Create social listening searches for your target topics, competitors,
   and keywords across LinkedIn, X, Reddit, and other configured sources.
2. Configure Signal types in the Signals tab — buying intent, hiring signals,
   competitor mentions, product complaints, leadership changes.
3. Set score/severity thresholds to filter noise; only fire workflows above
   your minimum signal confidence bar.
4. Set date windows — only act on signals from the past 24-72 hours; stale
   signals lose their timing advantage.

**Keyword search strategy:**
- Competitor names + pain phrases ("Competitor X is too expensive", "left
  Competitor X")
- Problem categories your product solves ("struggling with [problem]", "anyone
  solved [problem]")
- Recommendation requests ("looking for a tool that does X", "anyone use Y")
- Adjacent category launches ("just launched our outbound program")

**Avoid over-broad keywords** that generate noise (company names alone,
generic industry terms). Signal quality matters more than signal volume.

### Phase 3: Build the Enrichment and Qualification Layer

When a signal fires, the workflow must answer three questions before any
outreach is initiated:

1. **Is this person in ICP?** (job title, company size, industry, geography)
2. **Is this company on our target account list?** (or does it match ICP
   firmographic criteria if not pre-listed?)
3. **Is there a reachable email?** (run through email enrichment with
   deliverability verification before pushing to sequencer)

Typical workflow node sequence:
```
Signal Trigger → Person Enrichment (LinkedIn → firmographics + title)
  → ICP Filter (Boolean: title match AND company size match)
    → True: Email Enrichment → Deliverability Check
      → Verified: Push to Sequencer + Slack Alert with signal context
      → Unverified: Add to CRM without email trigger
    → False: Discard or add to low-priority nurture list
```

Use Trigify's built-in AI qualification agents to assess whether a post or
mention is genuinely relevant before enrichment credits are consumed.

### Phase 4: Craft Signal-Anchored Outreach

The outreach message must reference the specific signal. Generic openers
destroy the value of the signal layer.

**Fake personalisation (signal wasted):**
> "Hi Sarah, I noticed you're scaling your GTM team. Curious if you'd be
> open to a quick call about how we help companies like yours..."

**Signal-anchored message (Mitchum framework applied):**
> "Hi Sarah, Saw your comment on Chris's post about the SDR ramp problem —
> specifically your point about the first 60 days. We helped three teams
> at similar stages cut ramp from 90 to 45 days. Worth a conversation?"

Rules for signal-anchored messages:
- The first line must be traceable to the exact signal event
- Do not ask for a meeting in the first message; offer context or a question
- Keep total message under 100 words
- No product feature lists; one specific proof point tied to their signal
- If the signal is a comment, quote or closely paraphrase what they said

### Phase 5: Route and Alert

Qualified signals with verified emails enter the sequencer. Uncontacted
high-value signals (CEO, VP-level with no email found) get a Slack alert
to the rep with the signal context included — enough for a manual LinkedIn
outreach.

Signal routing tiers:
| Account Tier | Signal Strength | Action |
|---|---|---|
| Named target account | Any qualifying signal | Immediate Slack alert + email enroll |
| ICP-match not on named list | High signal (recommendation request, problem post) | Email enroll + add to CRM |
| ICP-match not on named list | Medium signal (competitor engagement, hiring post) | CRM add + nurture track |
| Non-ICP | Any signal | Discard |

### Phase 6: Measure Signal Quality

Track signal performance separately from overall outreach metrics. The signal
layer needs its own feedback loop:

- **Reply rate by signal type** — which signal types generate the highest
  reply rates? Reallocate monitoring budget to the highest-performers.
- **Signal-to-meeting rate** — of all signals that triggered outreach, what
  percentage booked a meeting?
- **Signal freshness distribution** — what percentage of signals fired within
  24 hours vs. 24-72 hours vs. older? Older signals should be deprioritized.
- **False positive rate** — signals that triggered enrichment and outreach
  but were not actually relevant. Review and tighten keyword search or ICP
  filter criteria.

Review signal performance weekly during ramp; monthly once stable.

## Output Format

Social intent monitoring system documentation:

1. **Signal taxonomy** — table of signal types with urgency, outreach angle,
   and platform sources configured for each
2. **Listening configuration** — keyword list, competitor list, topic
   categories, and score thresholds per platform
3. **Qualification workflow** — node-by-node flow diagram or table (trigger
   → enrichment → ICP filter → email verification → action routing)
4. **Message templates** — 2-3 signal-anchored message variants per top
   signal type, each under 100 words with first-line tied to the signal
5. **Routing rules** — account-tier-to-action mapping
6. **Measurement dashboard spec** — KPIs, signal-type breakdown, and weekly
   review cadence

## Quality Check

- [ ] Signal types defined with urgency windows (not just categories)
- [ ] ICP filter criteria specified before enrichment step (prevent credit waste)
- [ ] Email verification in workflow before sequencer push
- [ ] All message templates reference signal in first line — no generic openers
- [ ] Slack or CRM alert configured for high-value uncontacted signals
- [ ] Keyword searches reviewed for noise — signal quality over volume
- [ ] Signal freshness thresholds set (24-72 hr maximum for high-urgency signals)
- [ ] Measurement plan covers reply rate by signal type, not just overall rate

## Common Pitfalls

1. **Acting on stale signals.** A competitor mention from last week is not the
   same as one from yesterday. Set hard freshness windows: recommendation
   requests expire in 2 hours, most other signals in 24-72 hours. Signals
   older than 72 hours should go to a low-priority nurture track, not hot
   outreach.

2. **Generic outreach from signal data.** Running a signal-triggered sequence
   with the same generic opener you'd send to a cold list defeats the entire
   point. The signal must appear in the first sentence. If you can't reference
   it specifically, don't send the email.

3. **Enriching before filtering.** Running every signal through enrichment
   before checking ICP fit burns credits and slows workflows. Filter by job
   title and company size using free platform data first; only enrich confirmed
   ICP-matches.

4. **Keyword search too broad.** Monitoring your own company name or a one-word
   competitor name without context generates hundreds of irrelevant signals.
   Use phrase-level queries and negative keyword filters.

5. **No feedback loop on signal quality.** Running signal-led outbound without
   tracking reply rate by signal type means you never know which signal types
   are actually worth acting on. Some categories that seem strong (funding
   signals) often underperform industry-specific problem posts. Measure weekly.

6. **Confusing social listening with social selling.** Social listening is about
   monitoring what others say publicly (inbound signal collection). Social
   selling (the `social-selling` skill) is about building your own presence
   and engaging with your network. They work together but require separate
   workflows and metrics.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **signal-scoring**: Score and tier accounts across multiple signal sources;
  complements social monitoring with hiring, funding, and tech stack signals
- **lead-enrichment**: Enrich the people detected by social monitoring
- **hiring-signal-play**: Specific play for hiring-intent signals from job boards
- **multi-channel-outreach**: Coordinate email + LinkedIn + call after signal fires
- **social-selling**: Build your own LinkedIn presence that generates inbound signals
- **cold-email-strategy**: Write the signal-anchored emails that social monitoring triggers

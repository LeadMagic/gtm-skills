---
name: cold-email-strategy
description: >-
  Designs high-performing cold email sequence architecture with proper cadence
  timing, channel mixing, and trigger-based logic. Use when the user asks to
  build, audit, or optimize a cold outreach sequence, design a multi-touch
  cadence, plan sending limits, or structure outbound campaigns. Activates on
  phrases like "build me a sequence," "design a cadence," "cold email outreach
  plan," "outbound strategy," "multi-touch sequence," or "trigger-based outreach."
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.3.0"
  author: LeadMagic
  category: outbound
  tags: [cold-email, sequence-design, cadence, outbound, prospecting]
  related_skills:
    - cold-email-copywriting
    - email-deliverability
    - domain-infrastructure
    - sending-platforms
    - multi-channel-outreach
    - website-visitor-identification
    - icp-scoring
    - lead-enrichment
  frameworks:
    - Command of the Message
    - SPICED
    - SPIN
    - "Lars Nilsson (Cloudera/Snowflake) — Account-Based Sales Development (ABSD)"
    - Becc Holland — Stellar Cold Email / Diagnostic Selling
    - "Leslie Venetz — Earn the Right / Profit-Generating Pipeline"
    - Guillaume Moubeche — lemlist Multichannel Outbound
    - Jordan Crawford — PQS / PVP / FIND (Cannonball GTM)
    - Justin Michael — Sales Borg / Tech-Powered Sales
    - Justin Michael — Technology Quotient (TQ)
    - Justin Michael — Attributes vs Trigger Events
    - Henry Schuck (ZoomInfo) — Data-lake outbound SDR motion
    - Pat Spielmann — Cold to Gold
    - Pat Spielmann — Full-Circle Multichannel
    - Pat Spielmann — ACE (Agile Cold Email)
    - Eric Nowoslawski — Cold Email Infrastructure at Scale
    - Eric Nowoslawski — Creative Ideas Campaign
    - Eric Nowoslawski — Crawl Walk Run
    - Eric Nowoslawski — Outbound Unit Economics Gate
    - Randy Seidl (Sales Community) — When relationships beat sequences (contrast)
---

# Cold Email Strategy

## Overview

Most cold email sequences fail not because of the copy but because of the
architecture. Sending the right message to the right person at the wrong time
on the wrong channel produces zero pipeline. A well-architected sequence
respects buyer psychology, channel preferences, and deliverability constraints
as a single integrated system.

This skill produces a complete sequence architecture document: a touch-by-touch
cadence map with channel assignments, timing rules, trigger logic, sending
limits, and reply rate benchmarks segmented by persona and industry. The
output is the blueprint from which individual email copy, LinkedIn messages,
and call scripts are written by downstream skills.

The non-obvious rule: list-blast sequences (same message, same timing, everyone)
generate 1-2% reply rates. Trigger-based sequences with channel mixing and
signal-anchored personalization generate 5-12% reply rates. The difference
is entirely in the architecture, not the copywriting.

## When to Use

- User says "build me a cold outreach sequence" → activate this skill
- User says "design a cadence for our outbound" → activate this skill
- User mentions "multi-touch sequence," "outbound automation," or
  "cold email campaign structure" → activate this skill
- User asks "how many emails should I send," "what cadence works best," or
  "trigger-based vs list-blast" → activate this skill
- User wants to "map outbound channels" or "coordinate email + LinkedIn + calls" → activate this skill
- User asks about sending limits, "how many per day," or mailbox rotation → activate this skill

Do NOT use for:
- Actually writing the email copy → use `cold-email-copywriting`
- Setting up DNS authentication or mailboxes → use `domain-infrastructure`
- Selecting a sending platform → use `sending-platforms`
- Writing LinkedIn messages or call scripts → use `multi-channel-outreach`
- Classifying or handling inbound replies → use `reply-handling`

## Authoritative Foundations

This skill draws from the following established methodologies:

- **ColdIQ** — Campaign data from thousands of outbound sequences across SaaS,
  services, and recruiting. Benchmarks for reply rates by industry, persona,
  and touch count. The SPARK framework for trigger-based outreach: Signal →
  Problem → Answer → Result → Key Takeaway. Research-backed finding: 4-7 touches
  is the optimal range; below 4 misses engagement, above 7 hits diminishing
  returns and annoys prospects.

- **Force Management — Command of the Message®** — The Value Messaging Framework
  (Before Scenario, Negative Consequences, After Scenario, Positive Business
  Outcomes, Required Capabilities, Defensible Differentiators) provides the
  messaging architecture each sequence touch is mapped to. Not every touch
  covers every element — the sequence distributes the full CoM narrative
  across 4-7 interactions so the prospect builds the complete picture over
  time, not in a single email.

- **Winning by Design — SPICED** — The Situation, Pain, Impact, Critical Event,
  Decision framework maps to trigger types. A prospect in the Situation phase
  gets a different sequence than one showing Critical Event signals. SPICED
  lifecycle awareness prevents sending decision-stage content to
  situation-stage prospects.

- **Huthwaite — SPIN** — The Situation → Problem → Implication → Need-Payoff
  questioning sequence informs the logical progression of touches. Touch 1
  surfaces the Problem, Touch 2 deepens Implications, Touch 3 introduces the
  Need-Payoff. The 35,000-call research base guarantees this progression works
  across industries.

- **Josh Braun** — The principle that "you can't sell to someone who doesn't
  know they have a problem." Sequences must open with problem awareness, not
  solution awareness. The first touch should never mention your product — it
  should only surface a problem the prospect may not have articulated yet.

- **Becc Holland — Flip the Script.** Stellar cold email architecture: five
  delivery questions (get/open/read/relevance/psychology), 7 Pillars / 7 Deadly
  Sins, lead-weighted KPIs by motion. Diagnostic Selling extends to discovery
  prep when sequences convert to meetings. Playbook →
  `references/becc-holland-playbook.md`.

- **Guillaume Moubeche — lemlist / lempire.** Problem-first email structure
  (Situation/Problem → Value → Proof → **CTC**), 4–9 multichannel touches,
  trigger→problem mapping, Decision Hill sequencing. Canonical for lemlist
  execution — see also `lemlist-setup`. Playbook →
  `references/lemlist-guillaume-outbound.md`.

- **Jordan Crawford — Blueprint GTM / Cannonball.** **PQS** (Pain-Qualified
  Segments from closed-won analysis) and **PVP** (Permissionless Value
  Proposition — pay-to-receive message quality). **FIND**: Focus segment →
  Investigate data → Narrate message → Deploy. Use when reply rates stall despite
  good infra — fix the atomic message before scaling volume. Playbook →
  `references/jordan-crawford-blueprint-gtm.md`.

- **Justin Michael — *Tech-Powered Sales* (Sales Borg)** — Part I (*Sales-borg
  Theory*) and Part II (*Salesborg Action*) define the human+machine outbound
  operating model: machines handle data volume, signal detection, SEP cadences,
  and A/B tests; humans handle empathy, storytelling, referrals, and strategic
  touches. **Attributes** size ICP; **trigger events** supply *why now* (role
  change, incumbent pain, strategy shift, environment change). One sequencing
  superuser with high **technology quotient (TQ)** can outproduce a small SDR
  pod when messaging is proven — but automating broken ICP/messaging only
  amplifies failure. See `references/justin-michael-sales-borg.md`.

- **Pat Spielmann — Cold to Gold & Full-Circle Multichannel (LeadMagic).** Outbound
  architecture: higher-intent signals over static lists → enrichment waterfall →
  contextual copy → consistent volume with ACE-style iteration. **Full-Circle:**
  email raises hands, LinkedIn builds reputation pre-pitch, phone closes (call
  within 5 min of positive reply). Data quality gate before copy scale — see
  `../cold-email-copywriting/references/pat-spielmann-outbound-copy.md`. Pairs with
  Jordan Crawford (segment research), Guillaume (SEP cadence), Justin Michael (automation).

- **Henry Schuck (ZoomInfo) — Data-lake outbound SDR motion.** At scale,
  outbound sequences are not list-blasts — a merged data lake (intent, job
  changes, technographics, product usage) surfaces **who to contact now** and
  **why now**, with a targeted message per record. Sequence architecture should
  branch on signal type, not persona alone. See `sales-team-building` →
  `henry-schuck-sdr-model.md`.

- **Lars Nilsson (Cloudera/Snowflake) — Account-Based Sales Development.** The
  original account-based sequence design: SDR + AE + vertical SME co-author a
  **3-email sequence** from a 10–15-use-case-per-vertical library (vertical hook →
  layered story → Hail Mary), sent to multi-persona chunks of 50–250 contacts at
  signal-surging accounts. Public first-campaign results: ~70% open / ~30% reply
  vs 5–8% / 2–3% for nurture blasts — proof that account-targeted beats volume.
  For enterprise/ABM-tier accounts, design the sequence per account, not per
  persona. Canonical → `skills/abm/abm-strategy/references/lars-nilsson-absd.md`.

- **Randy Seidl (Sales Community) — When relationships beat sequences.**
  Outbound sequences create *access* at scale; they do not replace *trust* in
  enterprise deals. For $100K+ ACV, 6+ month cycles, and multi-stakeholder
  accounts, route to `social-selling` + `sales-coaching` →
  `skills/management-leadership/sales-coaching/references/randy-seidl-relationship-selling.md` after the first reply —
  build relationship maps and Three Plays (self, product, outcome), not more
  touches. Sequences win for net-new SMB/mid-market; relationship selling wins
  when the buyer chooses *you*. See `foundation/using-gtm-skills` Pattern 15.

- **Eric Nowoslawski — Growth Engine X.** **Outbound Unit Economics Gate**
  (TAM >100k, LTV >$10k, CAC:LTV 1:10 ideal) before scaling. **Cold Email
  Infrastructure at Scale:** 2 inboxes/domain, 30 sends/day/inbox baseline,
  3-week warmup, **1:1 backup inboxes** = active capacity. **Crawl Walk Run**
  for Clay rollout — manual examples before AI automation. **Creative Ideas
  Campaign** — GEX's highest-performing offer format (3 constrained ideas per
  prospect). Complements Jordan/Becc/Pat/Guillaume on message — Eric owns infra
  + economics + offer-led scale. Playbook →
  `references/eric-nowoslawski-outbound.md`.

- **Leslie Venetz — Sales-Led GTM Agency / *Profit-Generating Pipeline*.** The
  **buyer-first "Earn the Right"** gate: before sending any touch, ask "have I
  said something relevant/valuable enough to earn this ask?" — if not, audit
  again before sending. Reject **Legacy Outbound** (spam-the-TAM, entitled,
  AI-scaled slop) in favor of **deep segmentation + signal stacking** ("only the
  moose"), a **three-channel minimum** with double-taps, and **trust/buyer-led
  signals** as the KPI (not just booked meetings). Her 9-step *Profit-Generating
  Pipeline* and problem-centric copy audit gate relevance before volume — pair
  with Eric (infra/economics), Pat (copy skeleton + enrichment), Jordan (segment
  research). Playbook → `references/leslie-venetz-buyer-first-outbound.md`.

## Prerequisites

- Run `gtm-context` first to capture company ICP, personas, and value props
- Run `positioning-messaging` if you haven't already — sequences need clear
  messaging pillars to distribute across touches
- Required user inputs: target persona(s), industry/vertical, value proposition
  summary, any known trigger signals being targeted
- Optional but recommended: `domain-infrastructure` for sending capacity planning
- Optional: LeadMagic API key for trigger signal monitoring (Company Search
  for funding, hiring, leadership changes; Profile Search for job changes)
- Reference files: `references/email-frameworks.md` for sequence structure
  guidelines and `references/deliverability-primer.md` for capacity planning

## Step-by-Step Process

### Phase 1: Intake

Gather the following from the user. Ask all questions at once. Do not proceed
until you have answers to at least the first five:

1. **Target persona(s):** Who are we reaching? Title, seniority level, department.
   Are there multiple personas in the buying committee?

2. **Industry/vertical:** What industry? Any sub-vertical focus? This determines
   which pain points and proof points are relevant.

3. **Value proposition:** What problem do you solve? In one sentence, what is
   the outcome the prospect gets? This anchors all messaging.

4. **Trigger signals (if any):** Are you targeting specific triggers (recent
   funding, new hire, job change, tool adoption, conference attendance) or
   doing list-based outreach? Trigger-based sequences outperform by 3-5x.

5. **Outbound channels available:** Email only? Email + LinkedIn? Plus cold
   calls? Plus SMS? Each channel added increases reply rates — but also
   increases complexity.

6. **Current sending capacity:** How many mailboxes? What daily volume per
   mailbox? This determines how many prospects can be enrolled per day.

7. **CRM and sending platform:** What CRM? What sending platform? This affects
   automation and trigger integration.

8. **Existing sequences:** Any current sequences to audit or is this
   greenfield?

9. **Reply rate goal:** What's the target? Industry average is 1-3% for
   list-blast, 5-8% for segment-specific, 8-15% for trigger-based.

10. **Compliance requirements:** GDPR, CAN-SPAM, CASL? Any industry-specific
    regulations (finance, healthcare)?

### Phase 2: Research

Before designing the sequence, research the target persona and industry:

1. **Pain point mapping:** Identify the top 3-5 pain points for this persona
   in this industry. Use the SPIN framework: what's the Situation they're in,
   what Problems arise, what are the Implications, what's the Need-Payoff?

2. **Trigger signal catalog:** If trigger-based, catalog every trigger type
   that maps to a valid reason to reach out. Common triggers:
   - **Leadership change:** New VP/Director hired (30-90 day window) →
     "New leaders evaluate new solutions"
   - **Funding event:** Series A/B/C announced (7-30 day window) →
     "New budget for new tools"
   - **Job change:** Prospect moved to a new company (60 day window) →
     "New role, new vendor evaluation"
   - **Hiring surge:** Company posting multiple roles in a department →
     "Scaling team needs scaling infrastructure"
   - **Bad review of competitor:** G2/Capterra/Reddit complaint →
     "Dissatisfied with current solution"
   - **Tech stack change:** New tool adoption signals adjacent need →
     "Just adopted X, now need Y"
   - **Conference/event attendance:** Relevant industry event →
     "Fresh from the event, saw the trend"

3. **Channel preference research:** Different personas prefer different
   channels. VP-level: email primary, LinkedIn secondary. Director-level:
   email + LinkedIn equally. Manager-level: email primary, phone secondary.
   IC-level: email primary, sometimes phone. Industry variations: financial
   services prefers email, tech prefers LinkedIn, healthcare prefers phone.

4. **Competitor sequence audit:** What sequences are competitors running?
   What pain points are they using? Identify the gap — what are they NOT
   saying that you can own?

5. **Timing research:** For this persona in this industry, when do they
   read emails? General benchmarks: Tuesday-Thursday, 6-8am or 8-10am
   local time. Industry-specific: finance (Tue-Thu, 7-9am), tech
   (Tue-Thu, 9-11am), healthcare (Mon-Wed, 7-8am).

### Phase 3: Execution

Design the sequence architecture step by step:

#### Step 1: Determine Touch Count and Duration

The optimal range is 4-7 touches over 14-25 days.

- **4 touches:** For warm-ish leads or when targeting a very specific trigger
  with a short shelf life. Budget 10-14 days.
- **5 touches:** The standard for most B2B outreach. Budget 14-18 days.
- **6 touches:** For enterprise or high-ACV deals where persistence pays.
  Budget 18-22 days.
- **7 touches:** For very high-ACV ($50K+) or when multiple channels are
  in play. Budget 22-25 days.

3-day gaps between email touches are optimal. Shorter gaps (1-2 days) feel
aggressive. Longer gaps (5-7 days) lose momentum. For mixed-channel sequences,
the gap rule applies per channel — an email on Day 1 and a LinkedIn request
on Day 2 is fine (different channels).

#### Step 2: Map the Narrative Arc

Each touch advances the prospect through a specific mental shift. The arc
follows the Force Management Command of the Message® framework distributed
across touches:

**Touch 1 — Problem Awareness (Email, Day 1)**
Goal: Make the prospect aware of a problem they may not have articulated.
Method: Signal-anchored observation + one question. Never mention your product.
Length: 50-90 words.
Template: "Noticed [trigger/signal]. Curious if you're seeing [pain point]."
Emotional target: Intrigue or mild concern.

**Touch 2 — Implication Deepening (Email, Day 4)**
Goal: Expand the problem into its downstream consequences.
Method: New angle on the same problem. Data point or industry trend.
Length: 30-50 words.
Template: "Companies seeing [problem] typically find [implication] follows
within [timeframe]. Seeing that?"
Emotional target: Concern escalating toward urgency.

**Touch 3 — Social Proof (Email or LinkedIn, Day 7-8)**
Goal: Show that the problem is solvable and that peers have solved it.
Method: Case study snippet, customer quote, or metric from a similar company.
If on LinkedIn: InMail or connection request with a note.
Length: 30-50 words (email) or 200 chars (LinkedIn InMail).
Template: "[Similar company] was dealing with [same problem]. After [solution],
they saw [metric improvement] in [timeframe]."
Emotional target: Hope + social validation.

**Touch 4 — Value-Add (Email, Day 11-12)**
Goal: Give something useful without asking for anything.
Method: Link to an article, guide, calculator, or framework that's genuinely
useful to their problem. No pitch. No CTA beyond "thought this might help."
Length: 20-40 words.
Template: "Wrote up a framework on [problem domain] — thought it might be
relevant. [Link]"
Emotional target: Reciprocity + credibility.

**Touch 5 — Objection Pre-Handle (Email or Call, Day 15-16)**
Goal: Address the most common objection before the prospect raises it.
Method: Acknowledge the concern, reframe it, provide evidence.
If on phone: Voicemail or live call. Discovery questions if they answer.
Length: 40-60 words (email) or 30-second voicemail.
Template: "Most [personas] I talk to worry about [objection]. What they
find is [counter-evidence]."
Emotional target: Risk reduction.

**Touch 6 — Reframe (Email, Day 19-20)**
Goal: Change the lens on the problem. Show a different way to think about it.
Method: Industry insight, contrarian take, or forward-looking prediction.
Length: 30-50 words.
Template: "The [industry] conversation is shifting from [old frame] to
[new frame]. The companies winning are those that [new behavior]."
Emotional target: FOMO or intellectual curiosity.

**Touch 7 — Breakup (Email, Day 23-25)**
Goal: Close the loop gracefully. Leave the door open.
Method: Short, honest, no pressure. Honor the "no" — if they don't respond
to this, pause the account for 90 days.
Length: 20-40 words.
Template: "Seems like the timing isn't right. If [pain point] becomes a
priority, I'm here. Wishing you a strong [quarter]."
Emotional target: Respect + open door.

#### Step 3: Assign Channels Per Touch

Map each touch to the optimal channel based on persona and context:

**Email-only sequence:** All 7 touches via email. Standard for most B2B.
Sending limits apply (30-50 per mailbox per day).

**Email + LinkedIn hybrid (recommended for VP/Director personas):**
- Touch 1: Email
- Touch 2: LinkedIn connection request (with note) or InMail
- Touch 3: Email
- Touch 4: Email
- Touch 5: LinkedIn DM (if connected) or Email
- Touch 6: Email
- Touch 7: Email

**Email + Phone hybrid (for Manager/IC personas with phone numbers):**
- Touch 1: Email
- Touch 2: Cold call (live or voicemail, SPIN opening)
- Touch 3: Email
- Touch 4: Email
- Touch 5: Cold call
- Touch 6: Email
- Touch 7: Email

**Full multi-channel (for high-ACV enterprise, all channels available):**
- Touch 1: Email (Day 1)
- Touch 2: LinkedIn connection request (Day 3)
- Touch 3: Email (Day 6)
- Touch 4: Cold call (Day 9)
- Touch 5: Email (Day 12)
- Touch 6: LinkedIn DM or InMail (Day 15)
- Touch 7: Email + LinkedIn voice note (Day 19, breakup)

#### Step 4: Define Trigger-Based Branching

For trigger-based sequences, each trigger type may have a different opening
touch or even a different full sequence:

- **Funding trigger:** Touch 1 opens with "Congrats on the [Series] raise.
  Many post-funding [role]s I talk to are now prioritizing [capability]."
- **Job change trigger:** Touch 1 opens with "Saw you recently joined
  [new company] as [title]. When [similar personas] take on that role,
  [pain point] often comes with the territory."
- **Leadership change trigger:** Touch 1 opens with "Saw [company] brought
  on new [department] leadership. Often that comes with a mandate to
  [improve/fix/scale] [capability]."
- **Hiring surge trigger:** Touch 1 opens with "Noticed [company] is hiring
  aggressively in [department]. Scaling that fast often surfaces [pain point]."
- **Bad review trigger:** Touch 1 opens with "Saw some recent feedback about
  [competitor]'s [specific issue]. Curious if [pain point] is something
  you're actively working to solve."
- **Website visitor trigger (person ID — guardrailed):** Only when
  `website-visitor-identification` privacy checklist passes, ICP tier ≤2,
  confidence tier = High, and email verified via `lead-enrichment`. Touch 1
  references **relevant business context** (e.g., scaling [function] at
  [company]) — never "I saw you on our website." Cap at **2 automated touches**
  on visitor-only signal; human handoff on reply. Copy tone →
  `cold-email-copywriting/references/pat-spielmann-outbound-copy.md`
  (signal-anchored, not surveillance). Suppression list required before enroll.

#### Step 5: Set Sending Limits and Mailbox Allocation

Based on the capacity rules (30-50 sends per mailbox per day):

- **Total daily volume:** Target number of new prospects enrolled per day.
- **Mailboxes needed:** Ceil(total daily volume / 40). Using 40 as the
  safe midpoint per mailbox.
- **Domain allocation:** Distribute mailboxes across 3-5 sending domains.
  No domain should host more than 3 mailboxes.
- **Daily send cap per mailbox:** 50 absolute maximum. 40 recommended for
  sustained reputation.

Example: 200 new prospects/day = 5 mailboxes × 40 sends = 2-3 domains.

#### Step 6: Build the Sequence Map (Deliverable)

Create a touch-by-touch table:

| Touch | Day | Channel | Goal | Emotional Arc | Content Type | Word Count |
|-------|-----|---------|------|---------------|-------------|------------|
| 1     | 1   | Email   | Problem awareness | Intrigue | Signal-anchored observation | 50-90 |
| 2     | 4   | Email   | Implication deepening | Concern | Data point / trend | 30-50 |
| 3     | 7   | LinkedIn| Social proof | Hope + validation | Case study snippet | 200 chars |
| 4     | 11  | Email   | Value-add | Reciprocity | Resource link | 20-40 |
| 5     | 15  | Email   | Objection pre-handle | Risk reduction | Reframe + evidence | 40-60 |
| 6     | 19  | Email   | Reframe | FOMO | Industry insight | 30-50 |
| 7     | 23  | Email   | Breakup | Respect | Close + open door | 20-40 |

### Phase 4: Delivery

Package the sequence architecture as a complete strategy document:

1. **Executive Summary:** Target persona, industry, sequence philosophy,
   expected reply rate range.

2. **Trigger Catalog:** Every trigger type being targeted with the
   signal-specific opening angle.

3. **Channel Strategy:** Which channels, why, how they interleave.

4. **Sequence Map:** The touch-by-touch table with channel, timing, goal,
   emotional arc, content type.

5. **Sending Capacity Plan:** Mailbox count, domain allocation, daily
   enrollment limits, warmup schedule if needed.

6. **A/B Test Plan:** What variables to test first (subject lines, opening
   lines, CTAs), how to measure, when to declare a winner.

7. **Measurement Framework:** Key metrics (open rate, reply rate, positive
   reply rate, meeting booked rate, SQL conversion rate), how to track them,
   benchmark comparisons.

8. **Governance Rules:** When to pause a prospect (hard bounce, spam complaint,
   "not interested" reply), when to escalate to AE, when to re-enroll after
   a pause.

## Output Format

The agent should produce output in this structure:

```markdown
# [Company] Outbound Sequence Architecture for [Persona]

## Executive Summary
[2-3 paragraphs: who, what, why, expected outcomes]

## Trigger Catalog
[1-2 pages: each trigger type with the signal, detection method, opening angle]

## Channel Strategy
[Which channels, rationale, interleaving rules]

## Sequence Map
[Touch-by-touch table as described above]

## Sending Capacity Plan
[Mailbox math, domain allocation, daily caps]

## A/B Test Plan
[Test variables, measurement period, success criteria]

## Measurement Framework
[KPIs, benchmarks, tracking method]

## Governance Rules
[Pause rules, escalation rules, re-enrollment rules]

## Implementation Checklist
[Step-by-step checklist for the ops/SDR team to implement]
```

## Quality Check

Before delivering, verify:

- [ ] Does the sequence have 4-7 touches with 3-day gaps?
- [ ] Does Touch 1 avoid mentioning the product or company?
- [ ] Does each touch have a distinct emotional goal?
- [ ] Are channels assigned rationally based on persona preferences?
- [ ] Do sending limits respect 30-50 per mailbox per day?
- [ ] Are trigger-based branches defined for each trigger type?
- [ ] Is there an A/B test plan with measurable criteria?
- [ ] Are governance rules clear (when to pause, escalate, re-enroll)?
- [ ] Does the sequence arc follow SPIN progression (Situation → Problem →
  Implication → Need-Payoff)?
- [ ] Is the CoM framework distributed across touches rather than
  crammed into one?
- [ ] Are reply rate benchmarks realistic for the sequence type
  (trigger-based 8-15%, segment-specific 5-8%, list-blast 1-3%)?
## Common Pitfalls
1. **Too many touches.** Beyond 7 touches, each additional touch has
   negative marginal value. Prospects who haven't responded by Touch 7
   are not going to respond to Touch 8. Honor the breakup.
2. **Touch 1 product pitch.** The biggest mistake in cold outreach. Touch 1
   should surface a problem, not pitch a solution. If the prospect doesn't
   agree they have a problem, no amount of product detail helps.
3. **Same message, different channel.** Copy-pasting the email into a LinkedIn
   DM is not multi-channel — it's annoying. Each channel touch must be written
   for that channel's conventions.
4. **Ignoring sending limits.** 50 emails/day/mailbox is a hard ceiling.
   Google and Microsoft enforce this algorithmically. Pushing to 60-70/day
   gets your domain blacklisted regardless of authentication quality.
5. **No trigger branching.** Sending the same Touch 1 to everyone regardless
   of signal produces list-blast results. If you're investing in trigger
   detection, the sequence must reward that investment with signal-specific
   opening lines.
6. **Customer PII in sequences.** Never paste customer exports, support tickets,
   or onboarding files into sequencer fields, merge tags, or AI prompt batches.
   Sequences are for **lawful prospecting data** only — not file exchange.
   Customer data handling → `references/gtm-data-exchange-playbook.md`.
   Rep hygiene → `references/gtm-security-hygiene-basics.md`.
7. **No A/B testing.** Sequences degrade over time as prospects see similar
   messaging from competitors. Without ongoing testing, reply rates trend
   toward zero over 6-12 months.
8. **No governance rules.** Without clear rules for when to pause or escalate,
   SDRs default to "keep sending" — which burns domains and annoys prospects.
9. **Wrong gap timing.** 1-day gaps feel aggressive and trigger spam filters.
   5+ day gaps lose the prospect's context. 3 days is the research-backed
   sweet spot.
## Benchmarks Reference
Reply rate benchmarks by approach type (sourced from ColdIQ campaign data
across thousands of B2B sequences, 2024-2025):
| Approach | Reply Rate | Positive Reply Rate | Meeting Booked Rate |
|----------|-----------|--------------------|--------------------|
| List-blast (Tier 1 personalization) | 1-3% | 0.5-1.5% | 0.2-0.8% |
| Segment-specific (Tier 2) | 3-8% | 2-5% | 1-3% |
| Trigger-based (Tier 3 per-lead) | 8-15% | 5-10% | 3-8% |
| Multi-channel trigger-based | 12-20% | 8-15% | 5-12% |
Reply rate by persona seniority:
- C-suite: 3-8% (lower volume, higher quality)
- VP: 5-12% (sweet spot for cold outreach)
- Director: 5-10% (consistent across industries)
- Manager: 3-7% (more outreach volume, lower individual rates)
- IC: 2-5% (budget authority limits reduce response motivation)
These are benchmarks, not guarantees. Industry, offer strength, and market
conditions all shift these numbers. Use them as calibration, not prediction.
## Execution Artifacts

- `../cold-email-copywriting/references/pat-spielmann-outbound-copy.md` — Cold to Gold operating model, Full-Circle multichannel, enrichment-led sequence inputs, message audit checklist (Pat Spielmann)
- `references/justin-michael-sales-borg.md` — Sales Borg philosophy, human/bot division of labor, TQ stack, triggers, metrics, setup checklist (Justin Michael / *Tech-Powered Sales*)
- `sales-coaching/references/randy-seidl-relationship-selling.md` — When sequences end and relationship selling begins (contrast)
- `references/deliverability-primer.md` — Deliverability fundamentals
- `references/email-frameworks.md` — Cold email copy frameworks and rules
- `references/becc-holland-playbook.md` — Diagnostic Selling, stellar email, SDR KPIs
- `references/lemlist-guillaume-outbound.md` — Problem-first structure, CTC, multichannel
- `references/jordan-crawford-blueprint-gtm.md` — PQS, PVP, FIND, Cannonball GTM
- `references/justin-michael-sales-borg.md` — Sales Borg, TQ, trigger events
- `references/eric-nowoslawski-outbound.md` — Infra at scale, Creative Ideas, Crawl Walk Run, unit economics (Eric Nowoslawski)
- `references/leslie-venetz-buyer-first-outbound.md` — Earn-the-Right gate, problem-centric audit, segmentation, three-channel-minimum, Profit-Generating Pipeline (Leslie Venetz)
- `references/expert-frameworks.md` — Outbound expert subsidiary map
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills
- `website-visitor-identification` — person ID → trigger branch with privacy guardrails
- `cold-email-copywriting` — REPLY messaging and brevity rules from Sales Borg Action
- `deal-desk`, `revenue-team-onboarding` — customer data exchange and rep security hygiene
- `ai-sdr-setup` — Human-in-loop automation guardrails for Borg-style outbound
- `email-deliverability` — Sending caps before scaling SEP cadences
- `sending-platforms` — SEP selection and orchestration (Outreach, SalesLoft, etc.)
- `multi-channel-outreach` — Channel-native touches; avoid copy-paste automation
- `clay-automation` — Enrichment + trigger feeds into SEP enrollment

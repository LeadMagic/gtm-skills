---
name: reply-handling
description: >-
  Classifies and automates responses to cold email replies using an 8-category
  taxonomy, auto-reply playbooks, and human escalation rules. Use when the
  user asks to set up reply handling, needs reply classification logic, wants
  auto-responder templates for common replies, or needs escalation rules for
  human handoff. Activates on phrases like "handle cold email replies," "auto
  reply to outbound," "reply classification," "meeting booked response," "not
  interested reply," or "escalate to AE."
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: outbound
  tags: [reply-handling, auto-reply, classification, escalation]
  related_skills:
    - cold-email-strategy
    - cold-email-copywriting
    - sending-platforms
    - objection-handling
  frameworks:
    - Command of the Message
    - SPICED
---

# Reply Handling

## Overview

A positive reply to a cold email is worth nothing if it goes unanswered for
three days. Reply handling is where pipeline is won or lost — not in the
outbound send, but in the speed and quality of the response. Most teams
invest heavily in outbound copy and sequences but treat reply handling as
an afterthought, losing 30-50% of positive replies to slow response times
or poorly handled objections.

This skill produces a complete reply handling framework: an 8-category
classification taxonomy for inbound replies, auto-reply templates for
common scenarios, human escalation rules with SLA-based routing, and
objection handling playbooks mapped to Force Management's Command of the
Message framework. It covers both automated handling (sending platform
auto-responders) and human-handoff workflows (SDR → AE routing).

The non-obvious rule: every reply falls into one of exactly 8 categories.
If your reply handling system tries to handle 20+ nuanced scenarios, it
breaks. If it only handles 3-4 (interested, not interested, out of office),
it leaks pipeline. Eight categories is the research-backed sweet spot that
balances coverage with operational simplicity.

## When to Use

- User says "set up auto responses for our cold email" or "handle replies
  automatically" → activate this skill
- User asks about "reply classification" or "what to do when someone replies" →
  activate this skill
- User wants "templates for responding to interest" or "what to say when
  someone says not interested" → activate this skill
- User mentions "escalation rules," "AE handoff," or "SDR routing" →
  activate this skill
- User asks about setting up Smartlead categories or Instantly reply
  detection → activate this skill
- User wants to "automate objection handling in replies" → activate this skill

Do NOT use for:
- Writing the outbound email copy → use `cold-email-copywriting`
- Designing the sequence architecture → use `cold-email-strategy`
- Building a full objection handling framework for live sales calls →
  use `objection-handling` (reply-handling covers email reply objections
  specifically; objection-handling covers the full taxonomy for live
  conversations)
- Setting up the sending platform → use `sending-platforms`

## Authoritative Foundations

This skill draws from the following established methodologies:

- **ColdIQ — Reply Classification Data** — Analysis of thousands of cold email
  replies across campaigns. Their research identifies 8 recurring reply
  categories and the optimal response windows for each. The data shows that
  speed-to-lead for positive replies directly correlates with meeting booked
  rate: replies within 15 minutes convert at 3x the rate of replies within
  24 hours.

- **Force Management — Command of the Message®** — The Value Messaging
  Framework provides structured responses to common objections. When a prospect
  says "we already have a solution for this," the CoM framework maps that to
  a Required Capabilities gap: "Most solutions handle [basic capability], but
  struggle with [advanced capability] that [positive business outcome] requires."
  Each objection category maps to a specific CoM element to address.

- **Winning by Design — SPICED** — The Situation → Pain → Impact → Critical
  Event → Decision lifecycle determines which response is appropriate. A
  "not right now" reply from a prospect in the Pain phase gets a different
  response than the same reply from a prospect in the Decision phase. SPICED
  lifecycle awareness prevents burning prospects with the wrong follow-up.

- **Huthwaite — SPIN** — The SPIN questioning sequence is embedded in the
  human-handoff playbooks. When an SDR receives a positive reply and schedules
  a call, the preparation includes a SPIN discovery framework tailored to
  the specific signal that triggered the initial outreach.

- **Sandler — Pain Funnel** — When a prospect replies with an objection, the
  Sandler Pain Funnel provides the response structure: acknowledge, deepen
  the pain, isolate the objection, validate. Not all replies that look like
  "not interested" are terminal — many are unarticulated pain points that
  the Pain Funnel can surface.

## Prerequisites

- Run `cold-email-strategy` first — the reply handling framework must map
  to the specific sequence architecture being used
- Required user inputs: the sending platform being used (Smartlead, Instantly,
  etc.), CRM being used, SDR/AE team structure, SLA targets
- Recommended: `sending-platforms` for platform-specific reply handling setup
  instructions
- Optional: LeadMagic API for job change detection in replies (if a prospect
  replies from a different company)

## Step-by-Step Process

### Phase 1: Intake

Gather the following from the user. Ask all questions at once:

1. **Sending platform:** Smartlead, Instantly, Salesforge, Apollo, other?
   This determines what reply automation capabilities are available.

2. **CRM:** Salesforce, HubSpot, Attio, Pipedrive, other? This determines
   how replies are tracked and routed.

3. **SDR team structure:** Who handles replies? SDR first, then AE escalation?
   AE handles everything? Single founder doing it all? This determines
   routing rules.

4. **SLA targets:** What's the speed-to-lead target for positive replies?
   15 minutes is best practice. What's the target for objection replies?
   Same day.

5. **Meeting booking process:** How are meetings booked? Calendar link
   auto-sent? SDR manually schedules? This determines the "positive reply"
   auto-response format.

6. **Current reply volume:** How many replies per day/week? This determines
   whether manual handling is feasible or automation is required.

7. **Common objection patterns:** What objections do you already know you
   get? "Not interested," "already have a solution," "bad timing," "send
   me info," "who is this?"

8. **Escalation criteria:** What triggers an AE handoff? Positive reply?
   Qualified opportunity? Specific objection pattern?

### Phase 2: Research

Before building the reply framework, research current state:

1. **Audit current reply handling:** If already sending email, pull the last
   30-90 days of replies. Categorize every reply manually into the 8 categories
   (see Phase 3). Calculate: what percentage falls into each category? What's
   the median response time per category? What's the conversion rate from
   positive reply → meeting booked?

2. **Identify leak points:** Where are replies being lost?
   - Replies that went unanswered for >24 hours?
   - Positive replies that didn't convert to meetings?
   - Objection replies that could have been salvaged?
   - Automatic replies (out of office) that caused unnecessary sequence pauses?

3. **Map current objection patterns:** From the reply audit, catalog every
   unique objection and its frequency. Map each objection to the Force
   Management CoM framework: which CoM element does it challenge?

4. **Review platform capabilities:** For the user's sending platform,
   document the exact reply automation capabilities:
   - Smartlead: 25+ categories, auto-responder per category, webhook triggers,
     CRM sync with category tags
   - Instantly: Reply detection, manual labeling, simpler auto-responder rules
   - Salesforge: AI-powered reply classification, auto-responder rules
   - Apollo: Reply detection, basic auto-responder, CRM sync

### Phase 3: Execution

#### Step 1: Define the 8-Category Taxonomy

Every inbound cold email reply falls into one of these 8 categories:

**Category 1: Positive — Meeting Interest**
Definition: Prospect explicitly wants to meet or expresses strong interest.
Examples: "Yes, let's talk," "Would love to learn more," "Can you send your
calendar?", "This is interesting — when works for you?"
Response: Immediate human handoff. Speed-to-lead SLA: 15 minutes max.
Auto-reply: Send calendar link AND notify AE/SDR. "Great — here's my calendar.
Pick a time that works and I'll confirm. [Calendar link]"
Routing: AE or senior SDR. Highest priority.

**Category 2: Positive — Question/Information Request**
Definition: Prospect is interested but has a specific question before
committing. Examples: "How does this work with [tool]?", "What's the pricing?",
"Do you have a case study for [industry]?", "How long does implementation take?"
Response: Answer the question directly and quickly. Then offer a call.
Auto-reply (if question is common and answerable): Provide the answer and
a calendar link. "Great question. [Concise answer]. Happy to walk through it
in more detail — here's my calendar if helpful: [link]"
Auto-reply (if question needs human): "Great question — let me get you a
proper answer. I'll follow up within a few hours."
Routing: SDR or solutions engineer depending on question complexity.

**Category 3: Neutral — "Not Right Now" / Timing**
Definition: Prospect is interested but timing is wrong. Examples: "Not a
priority right now," "Check back in Q3," "We're in the middle of [project],"
"Budget is set for this year — maybe next."
Response: Respect the timeline. Set a follow-up. Don't push.
Auto-reply: "Totally understand — timing is everything. I'll check back in
[their timeframe]. If anything changes sooner, you know where to find me."
Action: Pause the prospect in the sequence. Set a CRM task for the follow-up
date they specified (or 90 days if unspecified).
Routing: No human handoff needed. Automated.

**Category 4: Objection — "Already Have a Solution"**
Definition: Prospect indicates they already use a competitor or have an
internal solution. Examples: "We already use [competitor]," "We built this
internally," "Our CRM already handles this."
Response: Acknowledge. Differentiate on the gap, not the product. Use CoM
framework: "Most [competitor] users find [capability gap] becomes a problem
at [scale point]."
Auto-reply: "Appreciate the context. A lot of teams tell me the same thing
— until [trigger event]. If you ever run into [specific pain point],
happy to share what we're seeing."
Action: Move to a nurture sequence (lower frequency, value-add content).
Do NOT aggressively pitch against the competitor — it kills credibility.
Routing: No human handoff needed unless the reply shows curiosity despite
the objection.

**Category 5: Objection — "Not the Right Person"**
Definition: Prospect says they're not the decision maker or not the right
contact. Examples: "You should talk to [name]," "I'm not the right person
for this," "Our VP of [department] handles this."
Response: Thank them. Ask for the right contact or permission to reach out.
Auto-reply: "Thanks for letting me know — and for saving us both time. Would
you mind pointing me to the right person, or is it OK if I reach out to
[name/role] directly?"
Action: If they provide a name, pause current prospect, add new contact to
the CRM, start a new outreach sequence to the right person. If they don't
provide a name, research the org chart and reach out independently.
Routing: No human handoff needed. SDR handles.

**Category 6: Negative — "Not Interested"**
Definition: Prospect explicitly says they're not interested. Examples:
"Not interested," "Please remove me from your list," "Stop emailing me,"
"Not relevant to us."
Response: Honor it. Immediately. Remove from all sequences. Do not argue.
Auto-reply: "Understood — I'll take you off the list. Thanks for letting
me know. [First name]"
Action: Remove from all active sequences. Add to suppression list. Do not
re-enroll for minimum 12 months.
Routing: No human handoff. Automated immediately.

**Category 7: Out of Office / Automated**
Definition: Automated reply indicating the prospect is away. Examples:
"Out of office until [date]," "On parental leave," "No longer with the
company," "This inbox is not monitored."
Response: Depends on subtype:
- Temporary OOO: Pause sequence until return date + 2 days. No auto-reply needed.
- Left company: Mark contact as inactive in CRM. Research new role if relevant.
- Not monitored: Look for alternative contact method.
Auto-reply: None. These are automated — replying creates a loop.
Action: Pause the prospect in the sequence length equal to OOO duration + 2
days. Resume automatically. If "left company," trigger a job change workflow.
Routing: No human handoff. Platform automation handles.

**Category 8: Spam / Abuse / Other**
Definition: Reply doesn't fit other categories. Examples: Spam from the
recipient's auto-responder, angry replies, misdirected emails, cryptic
one-word replies ("Stop," "Who?").
Response: Evaluate manually. Spam: ignore. Angry: apologize and remove.
Cryptic: SDR reviews and reclassifies to appropriate category.
Auto-reply: None — manual review.
Action: Flag for SDR review within 24 hours. Do not auto-respond — the
wrong auto-response to an angry prospect makes things worse.
Routing: SDR reviews within 24 hours.

#### Step 2: Write Auto-Reply Templates

For each category that gets an auto-reply, write the template.

Template rules:
- Sound human. Auto-replies that sound auto-generated damage credibility.
- Use the prospect's first name from the reply.
- Match the prospect's tone (formal if they're formal, casual if casual).
- Include a clear next step or closure.
- No marketing language. No "we're excited to..." or "our solution..."
- Signature: first name only.

**Category 1 template (Meeting Interest):**
"[First name] — great to hear from you. Here's my calendar — grab a time
that works and I'll confirm: [link]
Looking forward to it.
[Your first name]"

**Category 2 template (Question — answerable):**
"[First name] — [concise 2-3 sentence answer to their question].
Happy to go deeper on a quick call if useful: [calendar link]
[Your first name]"

**Category 3 template (Not right now):**
"[First name] — makes sense. I'll check back [their timeframe].
If anything changes sooner, I'm here.
[Your first name]"

**Category 4 template (Already have solution):**
"[First name] — appreciate the context. If [specific pain point] ever
becomes a priority, happy to share how similar teams handled it.
[Your first name]"

**Category 5 template (Not right person):**
"[First name] — thanks for letting me know. Any chance you can point me
toward the right person? Or OK if I reach out to [role] directly?
[Your first name]"

**Category 6 template (Not interested):**
"[First name] — understood. Removed you from my list.
[Your first name]"

#### Step 3: Define Human Escalation Rules

Not all replies should be auto-handled. Define escalation triggers:

**Immediate AE notification (within 15 minutes):**
- Category 1 (meeting interest) from: VP+, C-suite, target account, deal
  above $X ACV threshold
- Any reply that mentions a specific competitor by name with curiosity
- Any reply that asks a technical question requiring AE/Solutions Engineer
  expertise

**SDR handles (within 1 hour):**
- Category 1 from Manager/Director/IC level
- Category 2 (questions) that can't be auto-answered
- Category 5 (not right person) where org research is needed

**Automated (no human needed):**
- Category 3 (not right now) — pause and set reminder
- Category 4 (already have solution) — move to nurture
- Category 6 (not interested) — suppress
- Category 7 (out of office) — pause and resume

**Escalation SLA design:**
- Tier 1 (Category 1, target accounts): 15 minutes → AE
- Tier 2 (Category 1, non-target): 60 minutes → SDR
- Tier 3 (Category 2, complex questions): 4 hours → Solutions Engineer or SDR
- Tier 4 (Category 5, referral potential): 24 hours → SDR
- Tier 5 (Category 8, needs review): 24 hours → SDR
- Automated: Categories 3, 4, 6, 7 → immediate platform action

#### Step 4: Map Objections to CoM Framework

For Category 4 (objection) replies, map each common objection to the
Force Management Command of the Message® element it challenges, and
provide the response framework:

| Objection | CoM Element Challenged | Response Framework |
|-----------|------------------------|-------------------|
| "Already use [competitor]" | Required Capabilities / Defensible Differentiators | "Most [competitor] users find [capability gap] emerges at [scale]. How are you handling that today?" |
| "Built it internally" | Required Capabilities | "Internal tools work well until [maintenance cost/scaling point]. Teams at [scale] typically see [pain]. Worth comparing notes?" |
| "Too expensive" | Positive Business Outcomes | "The question is whether [outcome] is worth [cost]. Companies that make this work see [ROI metric]. Happy to share the math." |
| "Not a priority" | Negative Consequences | "Totally fair. For context, teams that deprioritize this typically see [consequence] within [timeframe]. Something to keep on the radar." |
| "Need to evaluate more options" | Decision Criteria | "Makes sense. The key things most teams evaluate are [criteria]. Here's how we stack up on each — [brief comparison]. Happy to be part of your process." |
| "Send me more info" | Before/After Scenario | "Will do. Quick context first so I send the right thing — are you more focused on [pain A] or [pain B]?" |

#### Step 5: Configure Platform Automation

For the user's specific platform, configure:

**Smartlead:**
- Define custom categories matching the 8-category taxonomy
- Write auto-responder templates for categories 1-6
- Configure auto-pause rules for categories 3, 6, 7
- Set up webhook notifications to Slack/email for categories 1, 2, 8
- Configure CRM sync: tag contacts with category, log replies as activities

**Instantly:**
- Set up reply labeling rules to auto-classify replies
- Configure auto-responders for common categories
- Set up campaign pause rules for OOO and not-interested
- Configure Unibox notifications for positive replies

**Salesforge:**
- Configure AI reply classification
- Write auto-responder templates for each category
- Set up human review queue for uncertain classifications

**Apollo:**
- Configure sequence rules: pause on reply, auto-advance on positive
- Set up reply alerts for SDR team
- Configure CRM sync for reply tracking

### Phase 4: Delivery

Deliver a complete reply handling playbook:

1. **8-Category Taxonomy:** Full definitions, examples, and routing for each category.
2. **Auto-Reply Templates:** Complete templates for each auto-handled category with platform-specific formatting.
3. **Escalation Matrix:** SLAs, triggers, and routing rules with time targets.
4. **Objection Response Frameworks:** CoM-mapped responses for the top 5-10 objections.
5. **Platform Configuration Guide:** Step-by-step setup for the user's platform.
6. **Monitoring and QA:** How to audit reply handling weekly, what metrics to track.

## Output Format

```markdown
# Reply Handling Framework for [Company]

## 8-Category Taxonomy

### Category 1: Positive — Meeting Interest
**Definition:** [definition]
**Examples:** [3-5 examples]
**Auto-Reply:** [template]
**Routing:** [AE/SDR, SLA]
**Action:** [CRM update, sequence action]

[Repeat for all 8 categories]

## Auto-Reply Template Library
[All templates in one place for easy copy-paste into the sending platform]

## Escalation Matrix
| Reply Category | Priority | Handler | SLA | Notification |
|---------------|----------|---------|-----|--------------|
| [Category rows] |

## Objection Response Frameworks
| Objection | CoM Element | Response Framework |
|-----------|------------|-------------------|
| [Objection rows] |

## [Platform] Configuration Guide
[Step-by-step platform setup with screenshots or code]

## Weekly Reply Audit Checklist
- [ ] Review all Category 1 replies: meetings booked vs lost?
- [ ] Review all Category 4 replies: any salvageable?
- [ ] Review response times against SLAs
- [ ] Check auto-responder accuracy: any misclassifications?
- [ ] Update objection patterns if new ones emerged
- [ ] Review Category 6 for patterns: are we targeting wrong?
```

## Quality Check

Before delivering, verify:

- [ ] Are all 8 categories defined with clear examples?
- [ ] Does each category have a defined routing (human or automated)?
- [ ] Are SLA targets specified for human-handled categories?
- [ ] Do auto-reply templates sound human (first name, matching tone, no
  marketing language)?
- [ ] Is Category 6 (not interested) honored immediately with no argument?
- [ ] Do objection responses use CoM framework elements, not product pitches?
- [ ] Is Category 7 (out of office) handled with proper pause/resume logic?
- [ ] Is Category 8 (spam/abuse/other) flagged for human review, not
  auto-responded?
- [ ] Are escalation rules clear with trigger conditions and time targets?
- [ ] Is there a weekly audit checklist for ongoing quality?
- [ ] Is the platform configuration specific to the user's platform?

## Common Pitfalls

1. **Auto-responding to everything.** Not every reply needs a response,
   and a bad auto-response is worse than no response. Categories 7 and 8
   should never receive auto-replies. Category 8 replies to an angry
   prospect with a chipper auto-response is the fastest way to get
   reported for spam.

2. **Slow response to positive replies.** The #1 destroyer of cold email
   ROI. A positive reply sits in the inbox for 4 hours while the SDR is
   in meetings, and the prospect's interest cools. Speed-to-lead must be
   non-negotiable. 15 minutes is the standard.

3. **Arguing with "not interested."** When someone says they're not
   interested, they mean it. Responding with "But have you considered..."
   or "Are you sure?" converts an uninterested prospect into an active
   detractor who may report you for spam. Accept it immediately and
   move on.

4. **Treating all objections the same.** "Already have a solution" and
   "too expensive" are fundamentally different objections that require
   fundamentally different responses. The first is about capabilities;
   the second is about value. Responding to both with the same template
   signals that you're not listening.

5. **Missing the referral opportunity in Category 5.** When someone says
   "I'm not the right person," they've just given you two gifts: they
   confirmed you're not wasting more time on them, and they've opened the
   door to the right person. Always ask for the referral.

6. **Not pausing on OOO properly.** If an out-of-office reply says
   "returning June 15," and you keep sending emails, you look incompetent
   and disrespectful. Pause until return date + 2 days.

7. **No weekly audit.** Reply classification accuracy degrades over time
   as language patterns change and new objection types emerge. A weekly
   30-minute audit of reply classifications and response quality prevents
   silent degradation.

8. **Platform mismatch.** Smartlead's reply category system is powerful
   but complex. Instantly's is simpler but less granular. Don't try to
   implement Smartlead-level category complexity on Instantly — it won't
   work. Match the framework to the platform's actual capabilities.

## Reply Rate → Meeting Booked Funnel

Understanding the math from sends to meetings:

1. Sends → Opens: ~50-70% open rate (cold email)
2. Opens → Replies: 3-15% reply rate (depends on sequence quality)
3. Replies → Category 1 (positive): ~20-30% of replies
4. Category 1 → Meeting booked: ~60-80% (with fast response)
5. Meeting booked → Meeting held: ~70-85%
6. Meeting held → Opportunity created: ~20-40%
7. Opportunity → Closed won: ~15-30%

The biggest leverage points are #3 (reply quality determines category
distribution) and #4 (speed-to-lead determines meeting booked rate).
A 15-minute response time vs 24-hour response time on Category 1 replies
can improve meeting booked rate by 200-300%.

## Related Skills

- `objection-handling` — adjacent workflow to use before or after this skill
- `cold-email-strategy` — adjacent workflow to use before or after this skill
- `sales-follow-up` — adjacent workflow to use before or after this skill
- `pipeline-management` — adjacent workflow to use before or after this skill

---
name: cold-email-copywriting
description: >-
  Writes high-converting cold email copy using the 3-line framework,
  proven subject line patterns, and persona-specific variants. Use when the
  user asks to write, improve, or critique cold email copy, craft subject
  lines, personalize outreach at any tier, or apply copywriting frameworks
  like PAS, BAB, AIDA, or SPARK. Activates on phrases like "write a cold
  email," "draft outreach," "improve my cold email copy," "subject line
  help," or "personalize this email."
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: outbound
  tags: [cold-email, copywriting, subject-lines, personalization, frameworks]
  related_skills:
    - cold-email-strategy
    - reply-handling
    - multi-channel-outreach
  frameworks:
    - AIDA
    - PAS
    - BAB
    - SPARK
    - Cialdini Influence
---

# Cold Email Copywriting

## Overview

Cold email copy that converts is not about being clever. It is about being
relevant. The prospect asks two questions in the first two seconds: "Do I
know this person?" and "Is this relevant to me?" If the answer to either is
no, the email is deleted — regardless of how well the rest is written.

This skill applies proven copywriting frameworks — PAS, BAB, AIDA, SPARK,
and the 3-line cold email framework — to produce emails that pass the
two-second test. It covers subject line construction, personalization tiers,
persona-specific voice variants, and the psychological triggers that drive
replies. It draws from Cialdini's principles of influence, Schwartz's
awareness levels, Ogilvy's advertising discipline, and Josh Braun's
problem-first approach.

The skill produces: complete email copy for each touch in a sequence, with
subject lines, body text, and CTAs. Includes variants by persona seniority
(VP, Director, Manager, IC) and by personalization tier (T1 merge, T2 segment,
T3 per-lead). When given a sequence map from `cold-email-strategy`, it writes
the copy for every touch. When given a single touch, it writes a single email.

The non-obvious rule: the best cold email is one that would work if you sent
it to a colleague. It sounds human, it references something specific, it asks
a low-friction question, and it never opens with "My name is X and I work at Y."

## When to Use

- User says "write a cold email" or "draft outreach to [persona]" →
  activate this skill
- User says "improve my cold email" or "make this email better" →
  activate this skill
- User asks for "subject line ideas" or "subject line that gets opens" →
  activate this skill
- User mentions "personalize this email," "make this T3," or
  "deep personalization" → activate this skill
- User asks "which framework should I use" or "PAS vs BAB vs AIDA" →
  activate this skill
- User wants email variants "for VP vs Manager" or "by persona" →
  activate this skill
- User mentions "Josh Braun style" or "problem-first email" →
  activate this skill

Do NOT use for:
- Designing the sequence architecture → use `cold-email-strategy`
- Writing LinkedIn messages or call scripts → use `multi-channel-outreach`
- Classifying or writing auto-responses to replies → use `reply-handling`
- Deliverability concerns (SPF, DKIM, warmup) → use `email-deliverability`

## Authoritative Foundations

This skill draws from the following established methodologies:

- **Cialdini — Principles of Influence** — Six principles applied to email copy:
  Reciprocity (Touch 4 gives value before asking), Social Proof (Touch 3
  uses customer proof), Authority (credible data points), Liking (human voice,
  not corporate), Scarcity (Touch 6 reframe creates FOMO), Commitment (small
  CTA in Touch 1 builds toward larger ask). The first touch should use at
  least one principle; the full sequence should use all six.

- **Eugene Schwartz — Breakthrough Advertising** — Five levels of prospect
  awareness. Cold email must match the prospect's awareness level. Tier 1:
  Unaware (don't know they have a problem — email opens with problem
  education). Tier 2: Problem-Aware (know they have a problem but not your
  solution — email opens with solution differentiation). Most cold email
  fails by writing for Tier 3-5 prospects who are already solution-aware,
  when the actual prospect is at Tier 1 or 2.

- **David Ogilvy — Ogilvy on Advertising** — "The headline is 80 cents of
  your dollar." In cold email, the subject line is the headline. It must
  earn the open. Principles: specificity over generality, curiosity over
  clarity, lowercase over title case, brevity over completeness. 2-4 words
  is the optimal range.

- **Josh Braun — Problem-First Selling** — "You can't sell to someone who
  doesn't know they have a problem." The first email must open with a
  problem hypothesis, not a solution pitch. If the prospect doesn't
  acknowledge the problem, no amount of solution detail matters. The
  fundamental question: "What problem am I helping the prospect discover?"

- **Joanna Wiebe (Copyhackers)** — Conversion copy principles. "Start with
  the conversation happening in the prospect's head." The opening line must
  match the internal monologue the prospect is already having. Write from
  "you" perspective — the prospect should feel seen, not sold to.

- **ColdIQ — 3-Line Framework and SPARK** — The highest-performing cold email
  format (2024-2026) is 3 lines: Observation → Relevance → CTA. Under 80 words
  total. No paragraphs. SPARK framework for trigger-based openings: Signal →
  Problem → Answer → Result → Key takeaway.

## Prerequisites

- Run `cold-email-strategy` first — the copy fills the architecture, not
  the other way around. You need the sequence map (touch goals, channel
  assignments, word counts) before writing copy.
- Run `positioning-messaging` if available — you need clear value props
  and differentiation to weave into social proof and reframe touches.
- Required inputs: target persona (title, industry, pain points), sequence
  map from `cold-email-strategy` (or at minimum the touch goals)
- Optional: `gtm-context` for company ICP and voice guidelines
- Reference files: `references/email-frameworks.md` for framework details
  and sequence structure rules

## Step-by-Step Process

### Phase 1: Intake

Gather the following from the user. Ask all questions at once:

1. **What are we writing?** Full sequence (all touches) or single email?
   If single, which touch number and goal?

2. **Target persona:** Title, industry, company stage/size, known pain points.

3. **Sequence map:** From `cold-email-strategy`. Need at minimum: touch goals,
   word count limits, emotional targets per touch.

4. **Personalization tier:** T1 (merge fields only), T2 (segment-specific
   templates), or T3 (deep per-lead, signal-anchored opening)? This determines
   how we write the opening line.

5. **Trigger signal (if T3):** What specific signal are we anchoring to?
   "Noticed you recently [funding round, job change, hiring surge, product
   launch, conference talk, article, podcast]."

6. **Voice guidelines:** Does the company have a brand voice? If not: casual
   and confident is the default. Sharp, thoughtful human — not a sales machine.

7. **Frameworks to use:** PAS, BAB, AIDA, SPARK, or 3-line? Default: Touch 1
   uses SPARK/3-line, Touch 2 uses BAB, Touch 3 uses AIDA, Touch 5 uses PAS.

8. **Previous emails (for critique):** If user is asking to improve existing
   copy, paste the current version.

### Phase 2: Research

For each touch being written, gather the anchoring context:

1. **Pain point validation:** For this persona in this industry, what are
   the 3-5 most acute pain points right now? Use industry reports, G2
   reviews, Reddit communities, LinkedIn discussions to confirm. Don't
   guess — find real language prospects use.

2. **Proof point sourcing:** What specific, named examples can we use?
   "One [industry] company reduced [metric] by [X]% in [timeframe]."
   If possible, name the company. If not, use enough specificity to be
   credible: "A Series B fintech company with ~200 employees..."

3. **Objection mining:** What are the top 3 objections this persona has?
   Source from: competitor G2 reviews (what do they complain about?),
   LinkedIn comments on industry posts, Reddit, sales call recordings.
   These become the material for Touch 5 (objection pre-handle).

4. **Competitor copy audit:** What are 3-5 competitors sending to this same
   persona? What language, frameworks, pain points are they using? Identify
   the gap — what are they NOT saying that creates differentiation space?

### Phase 3: Execution

Write the copy for each touch in the sequence. Follow these rules for every
touch, then apply the touch-specific framework.

#### Universal Rules (Apply to Every Touch)

1. **Subject line:** 2-4 words, lowercase, no punctuation. Looks like it
   came from a colleague. Examples: "reply rates," "hiring ops," "Q2
   forecast," "pipeline question," "your [role] stack," "[company] + [topic]."
   Never: emojis, prospect's first name (signals automation), "Re:" or
   "Fwd:" (dishonest), product names, urgency words.

2. **Opening line:** Never "My name is X and I work at Y." Never "I hope
   this email finds you well." The opening line must earn the next sentence.
   For T3: anchor to a specific signal. For T2: anchor to a shared context.
   For T1: anchor to a universal pain point.

3. **Body:** Plain text only. No HTML, no images, no bold, no italics.
   Single-line breaks between sentences. Under 80 words total for Touch 1
   (longer for later touches when the prospect is warmer). One proof point
   beats ten features.

4. **Voice:** "You/your" should outnumber "I/we" by 3:1. Use contractions.
   Read it aloud — if it sounds like marketing copy, rewrite it. Never use:
   "leverage," "synergy," "circle back," "best-in-class," "leading provider,"
   "robust," "innovative," "cutting-edge."

5. **CTA:** Low friction. For Touch 1-2: a question mark ("Worth a
   conversation?" "Seeing the same?" "Open to a thought?"). For Touch 3-4:
   a specific, small ask ("Happy to share the case study if useful."). For
   Touch 5-6: a slightly larger ask ("Would a 15-minute call to share what
   we're seeing make sense?"). Never ask for a 30-minute call in Touch 1.

6. **Signature:** First name only. No title, no company boilerplate, no
   logo, no legal disclaimer, no "Sent from my iPhone."

#### Touch 1: Cold Intro (Problem Awareness)

Framework: **SPARK** or **3-line** (Observation → Relevance → CTA).

Structure:
```
Subject: [2-4 words, lowercase, colleague-like]

Noticed [specific trigger/signal]. [Observation about what this likely means
for their world].

[One sentence connecting observation to their likely pain point.]

[Low-friction CTA question]?

--
[First name]
```

Word count: 50-90 total (body only: 30-60).

T3 variant (signal-anchored):
Subject: "new vp eng"
Body: "Noticed you joined [company] as VP Engineering last month. When new
engineering leaders land, tech debt and velocity bottlenecks usually surface
fast. Curious if that's where your head is at?"

T2 variant (segment-specific):
Subject: "engineering velocity"
Body: "Most VP Eng at Series B companies I talk to are fighting two battles
right now: shipping faster without breaking things, and keeping senior
engineers from burning out. Curious if either of those hits close to home?"

T1 variant (merge fields):
Subject: "eng velocity"
Body: "Hey {first_name}, how are you thinking about engineering velocity
heading into {current_quarter}? Most teams I work with are finding their
current tooling caps out around [scale point]. Worth a thought?"

#### Touch 2: New Angle (Implication Deepening)

Framework: **BAB** (Before → After → Bridge).

Structure:
```
Subject: [New angle, 2-4 words]

Most [persona]s I talk to are in [current bad state]. The ones breaking out
are in [better state].

The difference usually comes down to [one specific thing].
```

Word count: 30-50 words.

T3 variant: Reference Touch 1 context. "Following up on the [problem]
thread — one thing that surprised me: companies that fix this see
[downstream benefit] within [timeframe]."

#### Touch 3: Social Proof

Framework: **AIDA** (Attention → Interest → Desire → Action) in miniature.

Structure:
```
Subject: "quick eg" or "[company] story"

[One-line case study setup]. [Customer] was dealing with [same problem].

After [solution], they [specific metric] in [timeframe].

Happy to share the full story if useful.
```

Word count: 30-50 words.

Rules: Name the customer if permitted. If not, use enough detail to be
credible: industry, size, role. Never fabricate — if you don't have a real
example, use an industry stat instead ("Companies in [industry] that
address [problem] see [X]% improvement on average — BCG, 2024").

#### Touch 4: Value-Add (Resource)

Framework: Reciprocity (Cialdini). Give before asking.

Structure:
```
Subject: "[topic]" or "thought this might help"

Wrote up/Found a framework on [problem domain] that [specific value].
[Link if appropriate, or inline the insight if short].

No pitch. Just thought it might be useful.
```

Word count: 20-40 words.

Rules: Must be genuinely useful. If you don't have original content, curate
the best external resource. The prospect should think "this was worth reading"
regardless of whether they buy.

#### Touch 5: Objection Pre-Handle

Framework: **PAS** (Problem → Agitation → Solution).

Structure:
```
Subject: "[common objection]?"

Most [persona]s I talk to worry about [objection]. Fair concern — if [worst
case scenario], that's a real problem.

What they find, though, is [counter-evidence]. [One specific data point
or example].

Not sure it applies to your situation, but thought I'd share.
```

Word count: 40-60 words.

Common objections by persona:
- VP Eng: "We can build this internally."
- VP Sales: "Our CRM already does this."
- CMO: "We have an agency for this."
- CFO: "ROI is unproven."
- CEO: "Not a priority this quarter."

#### Touch 6: Reframe

Framework: **SPARK** adapted for reframing. Change the lens.

Structure:
```
Subject: "[industry trend]"

The [industry] conversation is shifting from [old frame] to [new frame].

Companies still operating in [old frame] are [negative outcome]. The ones
adopting [new frame] are [positive outcome].

Where does [company] sit on that spectrum?
```

Word count: 30-50 words.

#### Touch 7: Breakup

Framework: Respect. Honor the "no." Leave the door open.

Structure:
```
Subject: "closing the loop"

[First name], seems like the timing isn't right — totally understand.

If [pain point] becomes a priority down the road, I'm here.

Wishing you a strong [quarter/half/year].
```

Word count: 20-40 words.

Rules: Short. No guilt. No urgency. No "one last thing." This is the last
touch — mean it. If they don't respond, they're paused for 90 days minimum.

#### Persona Voice Variants

**VP-level:** More direct, less explanation. They read faster and have less
patience. Cut 20% of the words. Lead with business impact, not features.
Subject lines: top-of-mind business concerns ("Q3 pipeline," "hiring plan").

**Director-level:** Balance of business and operational. They care about how
things get done as much as why. Use implementation examples. Subject lines:
role-specific concerns ("eng velocity," "demand gen budget").

**Manager-level:** Operational focus. They care about their team's day-to-day.
Use team-level impact examples. Subject lines: team-level concerns ("team
onboarding," "sprint cycles").

**IC-level:** Hands-on focus. They care about their personal workflow. Use
personal productivity examples. Subject lines: individual concerns ("your
workflow," "time on X").

### Phase 4: Delivery

Deliver the copy in the sequence order with clear labeling:

1. **Full sequence:** Every touch with complete subject line + body + signature.
2. **Persona variants (if requested):** At least one variant at a different
   seniority level.
3. **A/B test candidates (if requested):** 2-3 subject line variants per touch,
   2-3 opening line variants per touch.
4. **Copy audit (if requested):** Marked-up version of user's original email
   with specific feedback and rewrite.

## Output Format

```markdown
# Cold Email Sequence: [Persona] at [Industry]

## Voice Guidelines
[2-3 sentences on tone, vocabulary, reading level]

## Touch 1 — Email — Day 1 — Problem Awareness
**Subject:** [subject line]
**Framework:** SPARK / 3-line

[Email body]

---
[First name]

**Persona variant (Director):**
[Variant]

**A/B test candidates:**
- Subject line B: [alternative]
- Opening line B: [alternative]

---

[Repeat for each touch]

## Copy Decisions Log
[Explain key choices: why this framework, why this angle, why this CTA]
```

## Quality Check

Before delivering, verify:

- [ ] Touch 1: Does it open with a problem or observation, not a company
  introduction? Under 90 words? Low-friction CTA?
- [ ] Subject lines: 2-4 words? Lowercase? No emojis or prospect name?
  Sounds like a colleague wrote it?
- [ ] Voice: "You/your" outnumbers "I/we" 3:1? Uses contractions? Read
  aloud without sounding like marketing copy?
- [ ] Personalization tier correct: T3 has a specific signal? T2 has
  industry/role context? T1 has merge fields?
- [ ] No banned words: "leverage," "synergy," "circle back," "best-in-class,"
  "leading provider," "robust," "innovative," "cutting-edge"?
- [ ] No HTML, images, bold, italics? Plain text only?
- [ ] CTA appropriate for touch number? (Touch 1-2: question mark, Touch
  3-4: small ask, Touch 5-6: slightly larger ask)
- [ ] Touch 7: Short? Honors the "no"? No guilt or urgency?
- [ ] Every touch: Under word count limit? Distinct emotional goal?
  Advances the narrative arc?
- [ ] Social proof: Named customer or credible industry stat? Not fabricated?
- [ ] Signature: First name only? No boilerplate?

## Common Pitfalls

1. **"My name is X" opening.** The #1 cold email mistake. The prospect
   doesn't care who you are until they know why you're relevant. Lead
   with THEM, not YOU.

2. **Too long.** The optimal cold email is under 80 words. For every 20
   words beyond that, reply rates drop by approximately 20%. If you need
   more space, you're trying to sell in one email — that's what the
   sequence is for.

3. **Feature dumps.** "Our platform offers A, B, C, D, and E with
   industry-leading F." Delete. Replace with one proof point: "One
   customer reduced [pain metric] by [X]%."

4. **Fake familiarity.** "Re:" and "Fwd:" subject lines, overly casual
   openings, pretending to have met. Prospects see through this instantly.
   Professional respect beats fake familiarity every time.

5. **Wrong awareness level.** Most cold email is written for
   solution-aware prospects (Schwartz Tier 3-4), but most prospects are
   problem-aware or unaware (Tier 1-2). If the prospect doesn't know they
   have a problem, leading with your solution is irrelevant.

6. **No CTA.** Every email needs a next step. But the CTA must match the
   relationship stage. Touch 1: a question. Touch 3: "if useful." Touch 6:
   "would a call make sense?"

7. **One-size-fits-all.** A VP of Engineering and a Director of Marketing
   should receive fundamentally different emails. If only the company name
   changes, you're doing Tier 1 when you think you're doing Tier 2.

8. **No A/B testing.** Even great copy degrades. Always deliver at least
   one subject line variant and one opening line variant per touch.

## Subject Line Pattern Library

Reference patterns that consistently achieve >50% open rates:

**Colleague-style:** "quick question," "when you have a sec," "thought on
this," "checking something," "one thing"

**Trigger-anchored:** "new [role] at [company]," "[company]'s [event],"
"saw your [content/launch/talk]"

**Problem-anchored:** "[pain metric] question," "[workflow] efficiency,"
"[problem] at [company]?"

**Curiosity:** "this surprised me," "unpopular opinion," "counterintuitive
but," "most [roles] miss this"

**Social proof:** "how [competitor/peer] solved [problem]," "[company]'s
[metric] improvement," "[industry] benchmark"

**Direct:** "[topic]?" Example: "pipeline velocity?" "hiring plan?" "eng
velocity?" — One word, question mark, lowercase. Extremely high open rates
when the topic is top-of-mind for the persona.

# Reply Classification Taxonomy

Extracted from `SKILL.md` to keep SKILL.md marketplace-efficient while preserving implementation depth.

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

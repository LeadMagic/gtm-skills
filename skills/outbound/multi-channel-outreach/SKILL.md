---
name: multi-channel-outreach
description: >-
  Design and execute multi-channel outbound sequences across email, LinkedIn,
  cold calls, and SMS. Use when the user wants to coordinate outreach across
  channels, build multi-touch sequences, add LinkedIn to their outbound, or
  create a channel mix strategy. Triggers on: "multi-channel", "LinkedIn outreach",
  "cold calling", "SMS outreach", "channel mix", "add LinkedIn to sequence",
  "cross-channel", "multi-touch", or any request to coordinate multiple outreach
  channels.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: outbound
  tags: [multi-channel, linkedin, cold-calling, sms, sequences, coordination]
  related_skills: [cold-email-strategy, cold-email-copywriting, reply-handling, social-selling, sales-navigator-prospecting]
  frameworks: [Saleshandy Multi-Channel Architecture, Reply.io Conditional Sequencing, Sandler Up-Front Contracts, Guillaume Moubeche — lemlist Multichannel]
---

# Multi-Channel Outreach

## Overview

Email alone is no longer enough. The highest-performing outbound programs
coordinate across email, LinkedIn, phone, and sometimes SMS — not as
independent channels, but as one coordinated sequence where each touch
builds on the last.

The key insight: channels aren't additive, they're conditional. If email
Touch 1 doesn't get opened in 3 days, LinkedIn fires instead of email
Touch 2. If LinkedIn connects, skip the scheduled email follow-up and
send a DM. The sequence adapts to engagement, not a fixed calendar.

## When to Use

- "Add LinkedIn to our cold email sequence"
- "Build a multi-channel outreach cadence"
- "How should I coordinate email and LinkedIn outreach?"
- "Set up conditional sequences across channels"
- "Add cold calling to our outbound motion"

## Authoritative Foundations

This skill draws from Saleshandy's outreach platform patterns (conditional
logic across 4+ channels), Reply.io's multi-channel automation with Jason AI,
and Sandler's Up-Front Contract principles for phone outreach.

Research consistently shows multi-channel sequences outperform single-channel:
adding LinkedIn to email increases reply rates by 30-50%, and adding phone
calls can double connection rates for high-value accounts.

- **Guillaume Moubeche — lemlist multichannel.** Email + LinkedIn + phone in one
  coordinated flow; 4–9 touches; channel-native copy (not email pasted to LI).
  Playbook → `../cold-email-strategy/references/lemlist-guillaume-outbound.md`.
  Platform setup → `lemlist-setup`.

## Prerequisites

- Cold email infrastructure set up (domains, mailboxes, sequences)
- LinkedIn profile optimized (see social-selling)
- For cold calling: phone numbers sourced and verified
- For SMS: legal compliance reviewed (TCPA, GDPR)

## Step-by-Step Process

### Phase 1: Channel Selection

Choose channels based on ICP and deal size:

| Channel | Best For | ACV Range | Investment |
|---|---|---|---|
| Email | All segments | All | Low — infrastructure built once |
| LinkedIn | B2B, professional | $10K+ | Medium — profile + Sales Nav |
| Cold Call | Enterprise, high-ACV | $25K+ | High — time per contact |
| SMS | SMB, short-cycle | <$25K | Low — compliance overhead |
| WhatsApp | EU, APAC, SMB | <$25K | Medium — regional preference |

Minimum viable multi-channel: email + LinkedIn. This combination covers
the broadest range of decision-makers.

### Phase 2: Sequence Design

Build a conditional 7-touch, 21-day sequence:

| Day | Channel | Action | Condition |
|---|---|---|---|
| 1 | Email | Cold intro — signal-anchored opening | Always |
| 3 | LinkedIn | Connection request (no pitch) | If email not opened |
| 5 | Email | Follow-up — new angle | If no reply to Email 1 |
| 7 | LinkedIn | Value drop DM | If connection accepted |
| 10 | Email | Social proof — case study | If no reply |
| 14 | Phone | Cold call — SPIN discovery | For Tier A only |
| 21 | Email | Breakup — final touch | Always, then stop |

Conditional logic rules:
- If LinkedIn connects before Day 5: skip Email 2, send DM instead
- If email gets a reply: pause sequence, route to reply-handling
- If phone connects: all subsequent touches reference the call
- If any channel gets a hard no: remove from all channels immediately

### Phase 3: Per-Channel Execution

**Email:** See cold-email-strategy and cold-email-copywriting skills for full detail.

**LinkedIn:**
1. Connection request — no pitch, no link. Just "Saw your [post/podcast/article] on [topic]. Would love to connect."
2. After acceptance — wait 2-3 days before DM. Don't pitch immediately.
3. DM 1 — value drop. Share a relevant article, data point, or observation. No ask.
4. DM 2 — soft CTA. "We help [similar companies] with [problem]. Worth a quick chat?"
5. Voice note — for high-intent prospects only. Personal, 30-60 seconds.

**Cold Call (Sandler-based):**
1. Opener: permission + value in one line. "Hi [name], this is [name] from [company]. I know you weren't expecting my call — can I have 30 seconds to tell you why I'm calling, and you can tell me if it's worth continuing?"
2. Discovery (if yes): SPIN questions — Situation → Problem → Implication → Need-Payoff
3. Close: time-bound CTA + send calendar invite while on the call
4. If no: respect it. "Totally understand. If [problem] becomes a priority, here's my email."

Never: "Did I catch you at a bad time?" — it invites rejection.

### Phase 4: Channel Coordination Tools

| Tool | Channels | Best For |
|---|---|---|
| Smartlead | Email + LinkedIn (beta) | Email-primary, LinkedIn-secondary |
| Reply.io | Email + LinkedIn + Calls + SMS + WhatsApp | Full multi-channel |
| Instantly | Email + LinkedIn | Email-primary, volume focus |
| Saleshandy | Email + LinkedIn + Calls | Full lifecycle |

## Output Format

Multi-channel sequence document:
```
# Multi-Channel Sequence: [Campaign Name]
ICP: [ICP description]
Duration: 21 days, 7 touches

| Day | Channel | Type | Content Theme |
|---|---|---|---|
| 1 | Email | Cold intro | Signal → CTA |
| 3 | LinkedIn | Connect | No pitch |
| ... | ... | ... | ... |

Conditional Rules:
- If LinkedIn connects: [action]
- If email reply: [action]
- If hard no: [action]
```

## Quality Check

- [ ] Every channel has a clear purpose in the sequence
- [ ] Conditional logic defined (what happens when a channel succeeds/fails)
- [ ] LinkedIn profile and email infrastructure ready before launch
- [ ] All touches coordinated — no duplicate messages across channels
- [ ] Hard-no handling: immediate removal from all channels
- [ ] Legal compliance verified for each channel in target regions

## Common Pitfalls

1. **Identical message across channels.** Sending the same message via email
   and LinkedIn DM feels like spam. Each channel should add a new angle.

2. **LinkedIn pitch in the connection request.** It's the equivalent of a
   cold email with "BUY NOW" in the subject line. Connect first, pitch later.

3. **Channel overload.** 7 touches across 4 channels feels like harassment.
   5-8 total touches across all channels combined is the sweet spot.

4. **No conditional logic.** A fixed sequence that fires LinkedIn on Day 3
   regardless of email engagement wastes touches. Build conditions.

5. **Different channels, different reps.** When email and LinkedIn come from
   different people at your company, the prospect is confused. One rep owns
   the full multi-channel relationship.

6. **SMS without consent.** TCPA (US) and GDPR (EU) require explicit opt-in.
   SMS to prospects who haven't consented creates legal liability.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **cold-email-strategy**: Email-specific sequence design
- **cold-email-copywriting**: Email content for each touch
- **social-selling**: LinkedIn profile and outreach optimization
- **sales-navigator-prospecting**: Sales Nav filter-specific LinkedIn touches (Morgan Ingram)
- **reply-handling**: Handle responses from any channel
- **sending-platforms**: Platform selection for multi-channel execution

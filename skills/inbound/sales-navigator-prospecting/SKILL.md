---
name: sales-navigator-prospecting
description: >-
  Run LinkedIn Sales Navigator prospecting using Morgan J. Ingram's AMP playbook —
  high-intent filters, filter-specific messaging, insight+question executive
  engagement, saved-search alerts, and a 15-minute daily workflow. Use when Sales
  Nav underperforms, reps blast one template, or you need executive response on
  LinkedIn. Triggers on: "Sales Navigator", "Sales Nav", "Morgan Ingram", "AMP Social",
  "posted in last 30 days", "filter-specific messaging", "LinkedIn prospecting",
  "book meetings LinkedIn", "saved search Sales Nav", "insight plus question",
  "social selling prospecting".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: inbound
  tags: [linkedin, sales-navigator, prospecting, social-selling, outbound, sdr]
  related_skills: [social-selling, linkedin-algorithm, multi-channel-outreach, list-building, lead-finding, multi-thread-orchestration]
  frameworks:
    - "Morgan J. Ingram (AMP Social) — Sales Navigator filter-specific prospecting"
    - "LinkedIn SSI Methodology"
    - "Richard van der Blom (Just Connecting) — LinkedIn Algorithm Insights Report"
---

# Sales Navigator Prospecting

## Overview

Most teams treat Sales Navigator as a $99/month contact export — find prospects,
paste the same message 4,000 times, wonder why LinkedIn "doesn't work."
**Morgan J. Ingram** (Founder, **AMP Social**; 4x LinkedIn Top Sales Voice) treats
Sales Nav as an **intent engine**: stack behavioral filters (posted recently,
following your company, viewed your profile, tenure windows), pair **each filter
with its own message**, and run a **15-minute daily** saved-search alert workflow.

This skill is the tactical Sales Nav layer. Load `social-selling` for profile
optimization, SSI, and general DM sequencing; load `linkedin-algorithm` when
reps also publish content and need feed reach mechanics.

## When to Use

- "How do I actually use Sales Navigator?"
- "Sales Nav isn't generating meetings"
- "Morgan Ingram Sales Navigator playbook"
- "Filter-specific LinkedIn messages"
- "Get executives to respond on LinkedIn"
- "10-minute Sales Nav saved search"
- "Posted in last 30 days filter"
- "Build a Sales Nav workflow for my SDR team"

## Authoritative Foundations

**Morgan J. Ingram (AMP Social) — filter-specific prospecting.** Public thesis:
each Sales Navigator filter is a **signal** that deserves its own message —
not one recycled script. Core motions: high-intent filter stacks, **insight +
question** comments on recent posts, 24–48 hour wait before connect, saved-search
weekly alerts, and multi-thread plays per account. Trained teams at Zoom, HubSpot,
Snowflake (public positioning). Full filter tables, message library, and weekly
workflow → `references/morgan-ingram-sales-navigator.md`.

**LinkedIn SSI Methodology** — professional brand, finding people, engaging with
insights, building relationships. Use SSI as a diagnostic; Ingram's motion is the
operational layer on top.

**Richard van der Blom (Just Connecting)** — when reps also post content, apply
feed mechanics (dwell time, golden hour, no external links in posts) so profile
traffic from Sales Nav outreach converts. → `linkedin-algorithm`.

## Prerequisites

- Sales Navigator Core or Advanced seat
- ICP defined: titles, seniority, company size, geography
- Optimized personal profile (`social-selling` Phase 1)
- CRM or spreadsheet to log filter variant → response rate

## Step-by-Step Process

### Phase 1: Audit the Current Motion

1. Export last 30 days of LinkedIn outreach: message text, filter used (if any),
   sends, accepts, replies, meetings.
2. Flag **one-template abuse** — same body copy across unlike filters.
3. Baseline response rate by message variant; set improvement target per filter.

### Phase 2: Build High-Intent Saved Searches

Create one saved search per motion (enable weekly alert):

1. **Active executives** — Posted last 30 days + VP/C-suite + ICP geo/industry.
2. **Warm to brand** — Following your company + target titles.
3. **Profile viewers** — Viewed your profile in last 90 days.
4. **New in role** — Years in company < 1 year + buyer titles.
5. **Buying window** — Years in company 6–12 months + buyer titles.

Document each search in a playbook table: filter stack, message variant ID, owner.

### Phase 3: Write Filter-Specific Messages

Build **12+ variants minimum** (see template table in reference). Rules:

- Open with the **filter signal** ("Noticed your post on…", "Saw you're
  [N] months into…", "Thanks for following [company]…").
- No product pitch in connection request or first DM.
- One clear question per touch; invite conversation.

### Phase 4: Executive Engagement (Posted-in-30-Days)

1. Find recent post from saved-search lead.
2. Comment: **insight + question** (not "great post").
3. Wait **24–48 hours**.
4. Connection request referencing the exchange.
5. After accept: DM with value; meeting ask only after rapport.

### Phase 5: Weekly 15-Minute Rhythm

- Monday: triage saved-search alerts; rank by intent (viewed profile > posted >
  following company).
- Tue–Thu: comments + connection requests (batch 10–15/day per rep).
- Friday: DM follow-ups; log meetings; retire underperforming variants.

### Phase 6: Multi-Thread Target Accounts

For ABM accounts, assign **different filter plays per persona** on the same
account (exec, champion, technical). Coordinate in CRM to avoid duplicate pitches
same week. → `multi-thread-orchestration`.

## Output Format

Sales Navigator prospecting playbook: current-state audit, five saved-search
definitions with filter stacks, 12 filter-specific message variants, executive
engagement runbook (comment → wait → connect → DM), 15-minute daily/weekly
calendar, multi-thread map for top accounts, and measurement dashboard (response
rate by filter, meetings per search).

## Quality Check

- [ ] Every saved search has a unique message variant (no generic blast)
- [ ] Executive motion uses insight+question, not "great post"
- [ ] 24–48 hour wait between comment and connection request documented
- [ ] Weekly alert enabled on each saved search
- [ ] Profile optimized before outreach scales (`social-selling`)
- [ ] CRM logs filter type for reply-rate analysis
- [ ] Multi-thread plan exists for tier-1 accounts

## Common Pitfalls

1. **One script for every filter.** Wastes the strongest Sales Nav signals;
   Ingram's 5× pipeline lift illustration comes from filter-message matching.

2. **Instant connect after comment.** Reads as automation; breaks trust.

3. **Skipping "viewed your profile" and "following company."** Highest-intent
   free signals in the stack.

4. **No tenure-based plays.** New leaders (< 1 year) and month-6–12 operators
   have different pains — same message misses both.

5. **Sales Nav without profile investment.** Prospects check your profile; empty
   activity kills accept rates.

6. **Attribution only in last-touch CRM.** LinkedIn pipeline is often dark
   social — add self-reported source fields.

## Execution Artifacts

- `references/framework-notes.md` — Framework index and authority routing
- `templates/output-template.md` — Deliverable shell
- `scripts/check-output.py` — Lightweight deliverable validator
- `references/morgan-ingram-sales-navigator.md` — Filters, messages, workflows

## Related Skills

- **social-selling**: Profile, SSI, general DM sequencing
- **linkedin-algorithm**: Organic content reach when pairing with outbound
- **list-building**: Multi-source lists; Sales Nav as one source
- **multi-channel-outreach**: Email/call steps on same prospects
- **multi-thread-orchestration**: ABM persona coordination

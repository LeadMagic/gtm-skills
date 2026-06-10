---
name: funding-signal-play
description: >-
  Trigger-based outbound play when a target account raises funding — signal
  stacking to cut false positives, use-of-funds alignment messaging, 48-hour
  contact bar, 14-day 5-touch sequence, benchmark-anchored measurement.
  Triggers on: "funding signal", "funding play", "raised money outreach",
  "funding announcement outbound", "Series A/B/C prospecting".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: sales-plays
  tags: [sales-plays, trigger-based, funding, signals, outbound]
  related_skills: [cold-email-strategy, cold-email-copywriting, signal-scoring, list-building, multi-channel-outreach]
  frameworks:
    - "UserGems — Buying Signals Benchmark Report (4.2M accounts, 2.28M opportunities)"
    - "Amplemarket — Signal-Based Selling Guide"
    - "Getcleed — Funding Signal Prospecting Guide"
    - "SEC EDGAR — Form D filings for US private raises (sec.gov)"
---

# Funding Signal Outbound Play

## Overview

A funding announcement triggers a flood of identical "Congrats on the raise!"
emails — the opener every vendor sends, and the one that makes the fastest
path to the trash folder. The plays that convert start differently: they
connect the round's stated use-of-funds to a concrete operational problem
before the ask, they detect the signal before the press announcement using
SEC Form D filings and VC network feeds, and they stack the funding signal
with a corroborating indicator (hiring spike on the relevant team, exec hire
in your category) to cut false positives roughly in half. This skill applies
the UserGems Buying Signals Benchmark and Amplemarket's signal-based selling
research to execute a 14-day, 5-touch sequence that hits the 48-hour contact
bar and measures performance against the 2–4x reply rate lift that timing-
relevant outreach produces over cold baseline.

## When to Use

- "Run a funding signal play"
- "Outreach to recently funded companies"
- "Trigger-based outbound on funding announcements"
- "Series A/B/C outbound cadence"
- "Signal stacking for funded accounts"
- "Set up funding alert monitoring"

## Authoritative Foundations

- **UserGems — Buying Signals Benchmark Report (4.2M accounts, 2.28M
  opportunities analyzed).** Funding is the single strongest growth buying
  signal — slightly ahead of IPO. Vendors who contact funded companies within
  48 hours see meaningfully higher conversion than those who reach out later.
  71% of companies that raise finalize vendor selections within approximately
  90 days. Monthly monitoring of target accounts is the recommended minimum.
  These benchmarks anchor the timing rules in Phase 1 and the measurement
  framework in Phase 5.

- **Amplemarket — Signal-Based Selling Guide.** Funding signals stay
  actionable for 30–60 days before relevance decays; signal-triggered
  sequences produce 8–15% reply rates versus 2–5% cold baseline (a 2–4x
  lift). The guide recommends weeks 1–2 for deep research and confirmation
  and weeks 2–6 as the prime outreach window. Applied to the Phase 3 cadence
  timing and the Phase 5 lift benchmark.

- **Getcleed — Funding Signal Prospecting Guide.** Signal stacking guidance:
  funding alone is noisy because not every funded company is in active
  vendor evaluation. Pairing a funding event with a hiring spike on the
  relevant team (e.g., a Series B company posting five SDR roles when you
  sell sales tools) cuts false positives roughly in half. Funding + relevant
  exec hire + job posting referencing your product category constitutes the
  strongest three-signal stack. Applied in Phase 1 signal validation and the
  scoring rubric in `references/framework-notes.md`.

- **SEC EDGAR — Form D filings (sec.gov).** US private companies must file
  Form D with the SEC shortly after a fundraise, often weeks before press
  coverage. Monitoring Form D filings on EDGAR provides earlier signal
  detection than TechCrunch or Crunchbase alone. Applied in Phase 1 as a
  primary detection source alongside Crunchbase alerts.

## Step-by-Step Process

### Phase 1: Signal Detection and Stacking (Day 0)

Set up monitoring across all four source layers — earliest detection wins:

| Source | Signal Type | Lead Time vs. Press |
|---|---|---|
| SEC Form D (EDGAR) | US private raises | Weeks earlier |
| Crunchbase alerts | Confirmed rounds | Same day or +1 |
| VC/founder LinkedIn + X | Announcement posts | Same day |
| TechCrunch / newsletter RSS | Feature coverage | Same day to +3 days |

After detection, stack the funding signal before acting. A single funding
event is noisy. Per Getcleed's signal stacking research, require at least one
of these corroborating signals before proceeding to Phase 2:

- **Hiring spike:** 3+ open roles on the team your product serves, posted
  within 30 days of the funding announcement.
- **Relevant exec hire:** A new VP or Director in your buyer's function,
  announced within 60 days.
- **Job posting keyword match:** A job description that explicitly names a
  problem your product solves or a tool category you compete in.

Single signal → log for monitoring. Two-signal stack → proceed. Three-signal
stack → highest-priority account; escalate to AE immediately.

### Phase 2: Rapid Account Research (Day 0–1)

Within 24 hours of confirmed signal stack:

- Round size, lead investor, and stated use of funds from press or Form D.
- Current team size and open roles (LinkedIn Jobs, Greenhouse, Lever).
- Tech stack in your category (BuiltWith, G2, job descriptions).
- Founder/CEO or target exec LinkedIn: recent posts, self-described priorities.
- Map use-of-funds to your product's value: identify the one or two stated
  spending areas where your product is operationally relevant. This becomes
  the opening line of every touch — not a congratulations.

### Phase 3: 5-Touch 14-Day Sequence

Prime outreach window: days 2–14 (Amplemarket), with first touch inside 48
hours (UserGems conversion bar).

**Day 1 — Email Touch 1 (Use-of-Funds Alignment):**

Subject: `[Company]'s [Series X] → [stated use area] question`

Body: Skip the generic congratulations. Open with the use-of-funds connection:
> "Saw [Company] closed [Series X] to [stated use — e.g., expand your sales
> team]. The teams I work with post-[Series] typically hit [specific friction
> at their stage] within the first 60 days of that build-out. How are you
> approaching [specific domain]?"

**Day 2 — LinkedIn Connection:**

Connect with the CRO, VP Sales, RevOps lead, or the exec who just received
the budget. Reference their post about the raise, not a congratulations opener.
Personalize using their stated priorities from their own posts.

**Day 4 — Email Touch 2 (Stage-Matched Proof Point):**

Subject: `[Similar company] at [comparable stage]`

Body: One-paragraph case study of a company at the same funding stage and
similar team size that used your product to hit a metric relevant to their
board's current mandate. No feature list — one result, one company, one number.

**Day 7 — Email Touch 3 (Direct Ask):**

Subject: `Question about [their stated use-of-funds area]`

Body: Peer-to-peer, direct.
> "Most teams post-[Series] scaling [function] face [named problem]. Is that
> on your radar? Worth a 15-minute conversation."

**Day 10 — LinkedIn DM:**

Reference your email thread. Add one concrete piece of value: a relevant
benchmark, a framework they haven't seen, or a short observation about their
job postings that shows you did the research.

**Day 14 — Breakup Email:**

Subject: `Closing your file`

Confirm you're removing them from outreach. A measured close sometimes
triggers the delayed response that earlier touches didn't.

### Phase 4: Multi-Thread Expansion

If no reply from primary contact after Touch 2, expand within the organization:

- **VP Engineering** if the use-of-funds includes a product build (product-
  led fit).
- **Head of Growth / Demand Gen** if the funds are allocated to pipeline
  generation.
- **The lead VC investor**: a warm introduction request through your network
  is often faster than cold threading into a funded company.

Do not contact multiple threads simultaneously with identical content —
route each persona to the use-of-funds area that maps to their function.

### Phase 5: Measurement

Track per funding event and compare against your non-trigger baseline:

| Metric | Target | Benchmark Source |
|---|---|---|
| Time from signal to first touch | ≤48 hours | UserGems Benchmark |
| Reply rate (signal-triggered) | 8–15% | Amplemarket Guide |
| Reply rate lift vs. cold baseline | 2–4x | Amplemarket Guide |
| Opportunity creation rate | Track per quarter | UserGems Benchmark |
| Vendor selection window | Close within 90 days of raise | UserGems (71% stat) |
| Signal stack score at entry | ≥2 signals | Getcleed stacking guide |

Review monthly. If reply rate falls below 2x lift, inspect: are signals
being acted on within 48 hours? Is the opening line connected to use-of-funds
or reverting to generic congratulations?

## Output Format

Funding play playbook containing: signal monitoring setup with all four source
layers, stack scoring rubric, account research template, 5-touch email and
LinkedIn sequence with exact copy, multi-thread expansion logic, and a
measurement dashboard with benchmark targets. See the signal source comparison
table, timing window cheat sheet, and stacking scoring rubric in
`references/framework-notes.md`.

## Quality Check

Before delivering, verify:
- [ ] First touch sent within 48 hours of signal confirmation (UserGems bar)
- [ ] Signal stack confirmed: funding plus at least one corroborating signal
      (hiring spike, relevant exec hire, or keyword-matched job posting)
- [ ] No email opens with bare "Congrats on the raise" — every opener
      connects use-of-funds to a concrete operational problem
- [ ] Case study or proof point in Touch 2 references a company at a similar
      funding stage and scale, not a generic enterprise logo
- [ ] Multi-thread contacts receive function-specific angles, not the same
      message routed to multiple personas
- [ ] Reply rate tracked per funding event and benchmarked against the
      Amplemarket 8–15% signal-triggered target and the 2–4x lift over cold
- [ ] Play is executed within the 30–60 day actionable window per Amplemarket;
      signals older than 60 days are flagged for review before proceeding

## Common Pitfalls

1. **Opening with "Congrats on the raise!"** This is what every other vendor
   sends. It signals template outreach, not research. Fix: open with the
   specific use-of-funds area and connect it to a concrete problem your
   product solves — in the first sentence, before any acknowledgment of the
   raise itself.

2. **Monitoring only TechCrunch and Crunchbase.** By the time a round is
   featured in press coverage, the signal is already 48–72 hours stale for
   US companies. Fix: add SEC Form D EDGAR alerts — US private companies
   file Form D shortly after closing, often weeks before press. This is the
   earliest public detection source available.

3. **Acting on funding alone without signal stacking.** A funding event by
   itself is a noisy trigger — many funded companies are not in active vendor
   evaluation. Fix: require at least one corroborating signal before
   escalating to outreach. Use the stacking rubric in `references/framework-notes.md` to score and prioritize.

4. **Contacting the account more than two weeks after the announcement.**
   Per Amplemarket's research, funding signals decay after 30–60 days.
   Vendors who wait lose the urgency frame. Fix: set Crunchbase and EDGAR
   alerts for same-day notification and assign a daily signal review task —
   target first touch within 24 hours of stack confirmation, 48 hours maximum.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- cold-email-strategy, cold-email-copywriting, signal-scoring, list-building, multi-channel-outreach

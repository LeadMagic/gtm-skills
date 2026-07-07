---
name: rb2b-outbound-triggers
description: >-
  Convert RB2B person-level website visitor identification into outbound
  sequences. Build trigger-based workflows that route identified visitors to
  SDRs, enrich with verified contact data, score ICP fit, and launch
  time-sensitive multi-channel outreach. Use when setting up RB2B-to-outbound
  pipelines, configuring Slack-to-SDR handoff, designing visitor-trigger
  cadences, or optimizing RB2B conversion rates. Triggers on: "RB2B outbound",
  "visitor trigger outbound", "person-level visitor sequence", "RB2B SDR
  workflow", "website visitor to outbound", "RB2B Slack alert routing",
  "identified visitor follow-up", "RB2B to Clay", "visitor-to-meeting".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: outbound
  tags:
    [
      rb2b,
      visitor-identification,
      outbound-triggers,
      sdr-workflow,
      person-level,
      deanonymization,
      outbound,
    ]
  related_skills:
    - cold-email-strategy
    - cold-email-copywriting
    - multi-channel-outreach
    - website-visitor-identification
    - lead-enrichment
    - email-finding
    - icp-scoring
    - signal-scoring
    - clay-automation
    - reply-handling
    - sending-platforms
  frameworks:
    - "Adam Robinson (RB2B) — Person-level visitor identification + LinkedIn-as-distribution"
    - "Signal-Based Selling — behavioral triggers over cold lists"
    - "Justin Michael — Tech-Powered Sales / Technology Quotient (TQ)"
    - "Jordan Crawford — PQS / PVP / FIND (Cannonball GTM)"
    - "Pat Spielmann — Cold to Gold trigger sequencing"
    - "Henry Schuck (ZoomInfo) — Data-lake outbound motion"
    - "Becc Holland — Stellar Cold Email / Diagnostic Selling"
    - "Winning by Design — SPICED diagnostic framework"
---

## Overview

RB2B identifies website visitors at the **person level** — not just the company. Every identified visitor has a LinkedIn profile, job title, and company. This skill converts that signal into outbound action: routing the right visitors to SDRs, enriching their contact data, and launching time-sensitive sequences that convert intent into meetings.

The core principle: **a visitor who identified themselves on your site is warmer than any cold list contact.** The window closes fast — within 48 hours, the buying intent signal decays by 50%. This skill builds the pipeline that captures that window.

## When to Use

- Setting up RB2B for the first time and need an outbound workflow
- RB2B is installed but visitors aren't being converted to meetings
- SDRs are getting Slack alerts but not acting on them consistently
- Need to route RB2B visitors to Clay → enrichment → sequencer pipeline
- Want to segment RB2B visitors by ICP fit and trigger different cadences
- Building a "visitor-to-meeting" funnel with conversion benchmarks
- RB2B alerts are firing but contact data is missing or unverified
- Need to measure RB2B-sourced pipeline vs cold outbound

## Step-by-Step Process

### 1. Visitor Routing Logic

Classify every RB2B-identified visitor before any outreach:

| Tier                 | Criteria                                                                                | Action                                                      | SLA              |
| -------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------- |
| **Tier 1 — Hot**     | ICP fit score ≥80 + title is decision-maker/influencer + visited pricing/docs/demo page | Immediate SDR Slack alert + auto-enroll in 7-touch sequence | <15 min response |
| **Tier 2 — Warm**    | ICP fit score 50-79 OR title matches but low engagement                                 | Enrich contact → add to nurture sequence                    | <4 hours         |
| **Tier 3 — Monitor** | ICP fit <50 OR title is junior/irrelevant                                               | Log in CRM, no outbound                                     | None             |
| **Tier 4 — Exclude** | Competitor, vendor, existing customer, partner                                          | Suppress from outbound                                      | N/A              |

### 2. Contact Enrichment Pipeline

RB2B gives you name + LinkedIn + company. It does NOT give you verified email or phone. Build a waterfall:

1. **RB2B payload** → name, title, company, LinkedIn URL, pages visited, session duration
2. **Clay enrichment** → company firmographics (headcount, revenue, industry, tech stack)
3. **Email finding** → waterfall through LeadMagic, Apollo, Hunter, Datagma
4. **Email verification** → verify before sending (never send to unverified)
5. **Phone finding** → optional, for Tier 1 only (Lusha, ZoomInfo, LeadMagic)
6. **ICP scoring** → score against your ICP definition (firmographic + technographic + intent)

### 3. Trigger-Based Sequence Design

Build distinct cadences for each tier:

**Tier 1 — Hot Visitor Sequence (7 touches, 10 business days):**

| Touch | Day | Channel  | Trigger                                       | Goal                 |
| ----- | --- | -------- | --------------------------------------------- | -------------------- |
| 1     | 0   | LinkedIn | Connection request referencing their visit    | Acknowledge interest |
| 2     | 0   | Email    | Personalized — "saw you checking [page]"      | Start conversation   |
| 3     | 2   | Email    | Value drop — relevant case study or resource  | Provide value        |
| 4     | 4   | LinkedIn | Engage with their recent post/comment         | Build familiarity    |
| 5     | 6   | Email    | Specific question tied to their role/industry | Elicit response      |
| 6     | 8   | Phone    | Cold call referencing the visit + emails      | Direct contact       |
| 7     | 10  | Email    | Breakup email — "closing the loop"            | Last attempt         |

**Tier 2 — Warm Visitor Sequence (5 touches, 14 business days):**

| Touch | Day | Channel  | Content                              |
| ----- | --- | -------- | ------------------------------------ |
| 1     | 0   | Email    | Soft reference to visit + value prop |
| 2     | 3   | LinkedIn | Connection request                   |
| 3     | 7   | Email    | Resource share (no ask)              |
| 4     | 11  | Email    | Question + soft CTA                  |
| 5     | 14  | Email    | Breakup                              |

### 4. Slack-to-SDR Handoff

Configure RB2B → Slack alert with structured payload:

```
🔥 RB2B Hot Visitor Alert
Name: [Visitor Name]
Title: [Job Title]
Company: [Company]
LinkedIn: [URL]
Pages visited: [pricing, /docs/api-auth, /case-studies]
Session: 4m 32s | 3 pageviews
ICP Score: 87/100
Action: Enrich → Sequence "Tier 1 Hot Visitor"
SDR Owner: [Round-robin assignment]
SLA: Contact within 15 minutes
```

### 5. Clay Automation Pipeline

Build the Clay workflow that connects RB2B to your sequencer:

1. **Trigger:** RB2B webhook fires on visitor identification
2. **Filter:** ICP fit score ≥50 (skip Tier 3/4)
3. **Enrich:** Waterfall email finding (LeadMagic → Apollo → Hunter)
4. **Verify:** Email verification (never skip)
5. **Score:** Update ICP score with firmographic enrichment data
6. **Route:** Assign to SDR via round-robin
7. **Enroll:** Push to sequencer (Smartlead/Instantly/Outreach) with correct cadence
8. **Log:** Create CRM record with source = "RB2B Visitor"

### 6. Measurement Framework

| Metric                         | Target                    | Why                            |
| ------------------------------ | ------------------------- | ------------------------------ |
| Visitors identified / week     | Baseline-dependent        | RB2B volume = top of funnel    |
| ICP fit rate (Tier 1+2)        | 30-50% of identified      | Not all visitors are buyers    |
| Enrichment success rate        | ≥70% verified email       | Waterfall effectiveness        |
| SDR response rate (within SLA) | ≥80%                      | Speed matters                  |
| Meeting booked rate (Tier 1)   | 5-10% of Tier 1 contacted | Conversion benchmark           |
| Meeting booked rate (Tier 2)   | 2-5% of Tier 2 contacted  | Lower intent, lower conversion |
| Pipeline sourced from RB2B     | Track monthly             | Attribution to RB2B channel    |

## Output Format

Produce a complete RB2B outbound playbook containing:

1. **Visitor routing matrix** — tier definitions, criteria, SLAs, and actions
2. **Enrichment waterfall** — tool chain, order, fallback logic, verification step
3. **Sequence designs** — full cadence for each tier with touch-by-touch content guidance
4. **Slack alert template** — structured payload for SDR handoff
5. **Clay workflow spec** — step-by-step automation with trigger, filters, enrich, route, enroll
6. **Measurement dashboard** — metrics, targets, and attribution model
7. **Privacy guardrails** — what you can and cannot do with person-level visitor data

## Quality Check

- [ ] Routing tiers have clear criteria — no ambiguity on which tier a visitor falls into
- [ ] Every Tier 1 visitor has a defined SLA (15 min response)
- [ ] Enrichment waterfall includes verification before sending — no unverified emails
- [ ] Sequences reference the visit context naturally (not creepy)
- [ ] Tier 4 exclusions cover competitors, vendors, customers, partners
- [ ] Measurement framework tracks RB2B-sourced pipeline separately from cold outbound
- [ ] Privacy guardrails address GDPR/CCPA for person-level data
- [ ] Clay workflow has error handling — what happens when enrichment fails
- [ ] Breakup emails are professional, not guilt-tripping
- [ ] Phone touches are Tier 1 only — don't burn phone numbers on low-intent visitors

## Common Pitfalls

- **Creepy outreach.** "I saw you were on our pricing page for 3 minutes" feels like surveillance. Fix: reference the visit contextually — "Noticed you were exploring [topic] — figured I'd reach out."
- **No ICP filter.** Every identified visitor gets a sequence. Fix: route through ICP scoring first — only Tier 1 and Tier 2 get outbound.
- **No enrichment verification.** Sending to unverified emails from RB2B data. Fix: always run email verification before enrolling in a sequence.
- **Slow SDR response.** Visitors identified but SDRs don't act for 2 days. Fix: Slack alert + SLA + round-robin assignment.
- **Treating RB2B like cold outbound.** RB2B visitors are warm — don't use the same generic cold email template. Fix: customize the first touch to reference their visit context.
- **No suppression logic.** Existing customers, partners, and competitors get the same outbound as prospects. Fix: suppress via CRM matching before enrolling.
- **Burning phone numbers on Tier 2.** Calling every identified visitor. Fix: phone is Tier 1 only — Tier 2 is email + LinkedIn.
- **No attribution.** RB2B-sourced meetings get lumped into "cold outbound." Fix: tag every RB2B-enrolled contact with source = "RB2B Visitor" in CRM.

## Related Skills

- `cold-email-strategy` — overarching sequence architecture
- `cold-email-copywriting` — email copy for each touch
- `multi-channel-outreach` — channel mixing beyond email
- `website-visitor-identification` — inbound visitor ID program design
- `lead-enrichment` — enrichment waterfall best practices
- `email-finding` — email discovery tools and accuracy
- `icp-scoring` — ICP fit scoring methodology
- `signal-scoring` — intent signal scoring
- `clay-automation` — Clay workflow building
- `reply-handling` — handling responses to RB2B-triggered outreach
- `sending-platforms` — sequencer setup and configuration

## Authoritative Foundations

- **Adam Robinson (RB2B)** — Person-level visitor identification via LinkedIn profile matching. Bootstrapped RB2B using LinkedIn as primary distribution. Core thesis: person-level identification is more actionable than company-level for outbound.
- **Signal-Based Selling** — Behavioral triggers (site visits, page views, session duration) indicate buying intent. Visitors who browse pricing/docs/demo pages are further in their evaluation.
- **Justin Michael — Tech-Powered Sales / Technology Quotient (TQ)** — Stack-aware outbound: use every tool in the revenue stack (RB2B → Clay → Sequencer → CRM) as a force multiplier.
- **Jordan Crawford — PQS / PVP / FIND (Cannonball GTM)** — Precision targeting framework. Person-level visitor data enables PVP (Persona-Value-Proof) targeting at the individual level.
- **Pat Spielmann — Cold to Gold** — Trigger-based sequencing. The visit is the trigger; the sequence is the conversion mechanism.
- **Henry Schuck (ZoomInfo) — Data-lake outbound motion** — Build a data infrastructure that captures and acts on every signal. RB2B is a signal source; the data lake routes it.
- **Becc Holland — Stellar Cold Email / Diagnostic Selling** — Reference the visit diagnostically, not surveillance-style. Ask questions tied to what they explored.
- **Winning by Design — SPICED** — Diagnose the visitor's situation (Situations, Pain, Impact, Critical events, Decision) based on pages visited.

## Execution Artifacts

- `references/framework-notes.md` — named frameworks, citation anchors, and RB2B-specific operational notes
- `templates/output-template.md` — copy-paste deliverable structure for the RB2B outbound playbook
- `scripts/check-output.py` — local checklist validator for required sections

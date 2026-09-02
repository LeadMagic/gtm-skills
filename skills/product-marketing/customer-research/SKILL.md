---
name: customer-research
description: >-
  Run evidence-led B2B customer and buyer research that produces a recruiting plan, interview guide, buying timeline, Jobs-to-be-Done forces map, quote repository, and decision-ready insight brief. Use when a team is guessing about buyer triggers, ICP, positioning, messaging, onboarding, or churn, or asks for voice-of-customer interviews and synthesis.
license: MIT
compatibility: Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, OpenCode, Goose, Hermes, Jesse, Windsurf, Zed
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: product-marketing
  tags: [customer-research, voice-of-customer, jtbd, buyer-journey, interviews]
  related_skills: [gtm-context-bootstrap, buyer-psychology, positioning-messaging, win-loss-analysis]
  frameworks:
    - "Bob Moesta and Chris Spiek — Jobs-to-be-Done switch interviews, timeline, and Four Forces of Progress"
    - "Katelyn Bourgoin — buyer interviews, recent-behavior evidence, and Trigger Technique"
    - "Georgiana Laudi and Claire Suellentrop — Customer-Led Growth"
    - "Peep Laja — voice-of-customer message mining"
---

# Customer Research

## Overview

Replace internal guesses with recent, attributable buyer evidence. This skill focuses on what people actually did and why they changed—not feature wish lists or hypothetical purchase intent. It produces reusable artifacts that can feed positioning, campaigns, product decisions, sales enablement, onboarding, and retention work.

## When to Use

- ICP, personas, or messaging are based mainly on internal opinion.
- A team needs buyer, churn, activation, or competitor-switch interviews.
- Funnel data shows what happened but not why.
- The user asks for voice-of-customer research, Jobs-to-be-Done interviews, message mining, or buying-journey research.
- A downstream skill needs sourced customer language rather than invented copy.

## Authoritative Foundations

- **Bob Moesta and Chris Spiek — Switch Interviews**: reconstruct the actual purchase timeline from first thought through passive looking, active looking, decision, and consumption.
- **Jobs-to-be-Done Four Forces**: capture the push of the old situation, pull of the new solution, anxiety about change, and habit of the status quo.
- **Katelyn Bourgoin — recent-behavior research**: interview actual recent buyers or active evaluators and ask about observed behavior, not predictions or requested solutions.
- **Georgiana Laudi and Claire Suellentrop — Customer-Led Growth**: turn customer insight into a measurable experience and growth strategy across acquisition, conversion, retention, and expansion.
- **Peep Laja — message mining**: preserve exact phrases with source context so copy remains traceable to customer evidence.

## Prerequisites

- A specific research decision, not a vague request to “learn about customers.”
- Access to an eligible sample and permission to contact or analyze it.
- Consent rules for recording, transcription, storage, and quote usage.
- A place to store evidence separately from interpretation.

## Step-by-Step Process

### 1. Frame the decision

Write the business decision, target segment, known evidence, unresolved assumptions, owner, and deadline. Define what the research will not decide.

### 2. Build a behavior-based sample

Recruit people close to a relevant event: recent wins, recent losses, recent switches from an alternative, activated customers, stalled trials, expansions, or churns. Separate cohorts instead of blending their stories.

### 3. Prepare without leading

Use `templates/interview-guide.md`. Begin with the participant's situation and timeline. Ask for concrete events, actions, alternatives, stakeholders, and evidence. Avoid pitching, defending the product, or asking what they would hypothetically buy.

### 4. Reconstruct the buying timeline

Capture first thought, triggering event, passive search, active search, alternatives, decision criteria, purchase, initial use, and outcome. Mark direct evidence, inference, and unknowns separately.

### 5. Map forces and stakeholders

Document push, pull, anxiety, and habit for each cohort. Add initiator, researcher, champion, blocker, economic buyer, approver, and user when the purchase is multi-person.

### 6. Code evidence

Load `templates/research-repository.csv`. Tag quotes by cohort, timeline stage, job, trigger, alternative, decision criterion, objection, desired outcome, and confidence. Do not strip language from its source context.

### 7. Synthesize patterns and counterexamples

Report recurring patterns, meaningful disagreement, negative cases, and sample limitations. Do not convert one memorable quote into a universal insight.

### 8. Route findings into artifacts

Map each supported insight to a decision owner and downstream asset: ICP criteria, positioning, landing-page copy, sales talk track, onboarding milestone, churn intervention, or experiment.

## Output Format

Produce a research pack containing:

1. Decision brief and scope.
2. Cohort and recruiting plan.
3. Interview guide and consent notes.
4. Buying-timeline and Four Forces maps.
5. Evidence repository with attributable quotes.
6. Findings, counterexamples, and confidence.
7. Decision and artifact handoff matrix.
8. Open questions and next research cycle.

## Quality Check

- [ ] The study is anchored to a decision and defined cohort.
- [ ] Questions prioritize recent events and behavior over predictions.
- [ ] Raw evidence remains distinguishable from interpretation.
- [ ] Quotes include source, cohort, context, and permission status.
- [ ] Findings include counterexamples and limitations.
- [ ] Every recommendation routes to an owner and usable artifact.
- [ ] Sensitive recordings and transcripts follow the user's consent and retention rules.

## Common Pitfalls

1. **Interviewing only happy power users.** This hides switching friction and lost demand. Fix: sample distinct outcome cohorts.
2. **Asking what customers want.** Participants predict solutions poorly. Fix: reconstruct recent decisions and actual workarounds.
3. **Leading with the product.** The interview becomes validation theater. Fix: begin with the struggling moment and current alternative.
4. **Producing a research deck nobody uses.** Insight decays without operational ownership. Fix: attach every finding to a decision, owner, and downstream artifact.
5. **Quote laundering.** Removing source context makes evidence look more universal than it is. Fix: retain cohort, date, situation, and permission metadata.

## Execution Artifacts

- `references/framework-notes.md` — Research methods, source links, and evidence rules
- `templates/output-template.md` — Complete decision-oriented research pack
- `templates/interview-guide.md` — Behavior-led switch interview guide
- `templates/research-repository.csv` — Structured evidence and quote repository
- `scripts/check-output.py` — Research-pack completeness validator

## Related Skills

- `gtm-context-bootstrap` for promoting approved findings into reusable context.
- `positioning-messaging` for turning evidence into positioning and message architecture.
- `win-loss-analysis` for a recurring post-decision buyer program.
- `buyer-psychology` for applying behavioral mechanisms after evidence collection.

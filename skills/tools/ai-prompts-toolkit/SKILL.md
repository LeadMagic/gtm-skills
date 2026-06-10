---
name: ai-prompts-toolkit
description: >-
  GTM AI prompt library and prompt-loop patterns — Claygent research, LLM
  scoring, cold email drafts, reply classification, account briefs, and
  iterate-until-quality workflows for sales and marketing. Use when writing
  Clay AI prompts, designing prompt chains, or building research→draft→score
  loops in Clay, n8n, or Jesse. Triggers on: "GTM prompts", "Claygent prompt",
  "AI prompt loop", "cold email prompt", "reply classification prompt", "LLM
  column Clay", "prompt chain GTM", "research prompt sales".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: tools
  tags: [ai-prompts, claygent, gtm, llm, cold-email, research, prompt-loops, automation]
  related_skills: [clay-toolkit, clay-loops-toolkit, clay-automation, cold-email-copywriting, meeting-prep, reply-handling, signal-scoring]
  frameworks:
    - "Anthropic — Prompt Engineering for Tool Use"
    - "Clay — Claygent and AI column patterns"
    - "Winning by Design — SPICED discovery structure"
    - "Andy Whyte — MEDDICC evidence in prompts"
---

# AI Prompts Toolkit

## Overview

Generic AI prompts produce generic GTM output — invented personalization,
pattern-guessed emails, and hallucinated metrics. GTM prompts need **constraints**:
source URLs, word limits, banned claims, ICP context, and explicit failure
behavior when data is missing.

This skill is the GTM prompt library: copy-paste prompts for Claygent, Clay AI
columns, n8n LLM nodes, and Jesse agents — plus **prompt loops** that iterate
research → draft → score → revise until quality gates pass.

## When to Use

- "Write a Claygent prompt for [task]"
- "GTM prompt for cold email personalization"
- "Reply classification prompt"
- "Prompt loop for account research"
- "LLM column in Clay for ICP scoring"
- "AI prompt chain for outbound"

Load `gtm-context` first if ICP/positioning is undefined — prompts without
context hallucinate.

## Authoritative Foundations

- **Anthropic — Prompt Engineering.** Separate instructions from data; specify
  output format; define what to do when information is missing (return empty,
  not guess).
- **Clay Claygent.** Web research agent — must require `source_url` on every
  factual claim. Credit-heavy — use only after structured enrich fails.
- **SPICED (WbD).** Discovery and research prompts map to Situation, Pain,
  Impact, Critical Event, Decision — not free-form summaries.
- **MEDDICC (Whyte).** Research prompts for enterprise deals extract evidence
  for Metrics, Champion, Economic Buyer — score confidence 0/1/2.

## Prompt Design Rules (All GTM Prompts)

1. **Role + task** — one sentence each
2. **Input variables** — name every field (`{{company}}`, `{{domain}}`)
3. **Output format** — JSON or markdown template with required keys
4. **Constraints** — word limits, banned phrases, no invented stats
5. **Missing data** — "If unknown, return `null` — do not guess"
6. **Source requirement** — factual claims need `source_url`

## GTM Prompt Catalog

Load full copy-paste prompts from `references/prompt-library.md`.

| Prompt ID | Use Case | Tool |
|---|---|---|
| `P01` | Account snapshot (SPICED) | Claygent / LLM |
| `P02` | Work email find (no guess) | Claygent |
| `P03` | Signal line for cold email | LLM column |
| `P04` | Full cold email draft | LLM column |
| `P05` | Email quality score (1–10) | LLM column |
| `P06` | Reply classify (interested/objection/OOO) | LLM / n8n |
| `P07` | ICP fit score with reasoning | LLM column |
| `P08` | Meeting brief pre-call | Jesse / LLM |
| `P09` | Champion identification | Claygent |
| `P10` | Competitor mention extractor | Claygent |

## Prompt Loops (GTM)

Prompt loops chain multiple AI steps with gates between them.

### Loop 1: Research → Brief (account prep)

```
Step 1 P01 Account snapshot →
Step 2 Gap check (missing Pain/CE?) →
Step 3 Targeted Claygent fill (only gaps) →
Step 4 Merge into meeting brief
Gate: Critical Event present OR flag manual review
```

### Loop 2: Signal → Draft → Score → Revise (outbound)

```
Step 1 Enrichment + signal detect →
Step 2 P03 signal line (source required) →
Step 3 P04 email draft (<90 words) →
Step 4 P05 quality score →
Step 5 IF score <7: P04 revise with feedback (max 2 iterations) →
Step 6 IF score ≥7: route to human review queue
Gate: no send without human approval (pilot mode)
```

### Loop 3: Enrich → ICP Score → Route

```
Step 1 Waterfall enrich →
Step 2 P07 ICP score →
Step 3 Route: ≥80 sequencer queue | 50–79 SDR review | <50 archive
Gate: suppression list check before route
```

### Loop 4: Inbound Reply → Classify → Route

```
Step 1 P06 classify reply →
Step 2 Map to playbook (interested→AE, objection→`reply-handling`, OOO→pause) →
Step 3 CRM task + Slack alert
Gate: positive intent → human handoff within 1 business day
```

Use `templates/prompt-loop-blueprint.md` to document custom loops.

## Example: P04 Cold Email Draft (abbreviated)

```
You write B2B cold emails for {{company_selling}}.

INPUT:
- Prospect: {{first_name}} {{last_name}}, {{title}} at {{company}}
- Signal: {{signal}} (source: {{source_url}})
- ICP pain: {{icp_pain}}
- Proof point: {{proof_point}} (must be factual)

RULES:
- Under 90 words
- One pain, one proof, one CTA
- No "I hope this finds you well", no invented metrics
- If signal or proof is empty, write generic ICP pain only — do not invent signal

OUTPUT JSON:
{"subject":"","body":"","personalization_source":"","word_count":0}
```

Full prompts in `references/prompt-library.md`.

## Output Format

Deliverable: prompt spec or loop blueprint with prompt IDs, variable map,
quality gates, iteration limits, credit budget (Claygent), and integration
point (Clay column, n8n node, or agent skill).

## Quality Check

- [ ] Every prompt has role, inputs, output format, constraints, missing-data rule
- [ ] Factual prompts require `source_url` in output
- [ ] Loops have explicit gates and max iteration counts
- [ ] Outbound loops include human review gate before send
- [ ] Prompts reference ICP/positioning from `gtm-context` — not generic SaaS
- [ ] Claygent prompts prohibit email pattern-guessing
- [ ] Reply loop maps to `reply-handling` categories

## Common Pitfalls

1. **"Find their email" Claygent prompts.** 40–60% bounce from guessed patterns.
   Fix: require source URL; return empty if not found.

2. **Unbounded revise loops.** LLM iterates forever, burns credits. Fix: max 2
   revisions; then human queue.

3. **No quality scorer between steps.** Bad drafts propagate. Fix: P05 score
   gate ≥7 before human review.

4. **Prompt without suppression context.** AI contacts opted-out accounts.
   Fix: pass `suppressed: true/false`; halt if true.

5. **One prompt does everything.** Research + draft + send in one call = errors.
   Fix: use prompt loops with narrow steps.

## Execution Artifacts

- `references/framework-notes.md` — design rules and SPICED/MEDDICC mapping
- `templates/output-template.md` — Primary deliverable shell
- `scripts/check-output.py` — validates prompt specs and loop blueprints
- `references/prompt-library.md` — full GTM prompt catalog (P01–P10+)
- `references/prompt-loop-patterns.md` — loop diagrams and gate rules
- `templates/prompt-spec.md` — single prompt documentation template
- `templates/prompt-loop-blueprint.md` — multi-step loop template

## Related Skills

- `clay-toolkit` — Where LLM columns and Claygent live in tables
- `clay-loops-toolkit` — Scheduled signal loops using these prompts
- `cold-email-copywriting` — Message strategy behind P03/P04
- `meeting-prep` — Consumes P01/P08 output
- `reply-handling` — Playbook for P06 routing
- `ai-sdr-setup` — Guardrails for automated prompt loops

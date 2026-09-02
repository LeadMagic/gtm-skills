---
name: gtm-context-bootstrap
description: >-
  Build a reusable, evidence-backed GTM context pack covering company, product, market, ICP, buying triggers, positioning, proof, voice, constraints, and unresolved questions. Use when an agent is starting GTM work without reliable shared context, when teams repeat the same discovery in every task, or when campaign outputs contradict one another.
license: MIT
compatibility: Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, OpenCode, Goose, Hermes, Jesse, Windsurf, Zed
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: foundation
  tags: [gtm, context, positioning, icp, research]
  related_skills: [gtm-context, icp-scoring, positioning-messaging, competitive-intel]
  frameworks:
    - "April Dunford — Obviously Awesome positioning components"
    - "Clayton Christensen — Jobs to Be Done"
    - "Geoffrey Moore — Beachhead segment and whole product"
    - "Peep Laja — Message mining and conversion research"
---

# GTM Context Bootstrap

## Overview

GTM work degrades when every task starts from a different version of the company story. This skill creates one compact context pack that separates verified facts, sourced customer language, operating assumptions, and open questions. It does not invent strategy to make the file look complete.

## When to Use

- A founder or team is starting a new GTM program.
- Multiple agents need consistent product, ICP, positioning, or voice context.
- Campaigns disagree about target buyer, pain, proof, or differentiation.
- The user asks for a company context file, GTM brief, messaging source of truth, or agent context pack.
- A later skill needs reliable inputs before it can produce an artifact.

## Authoritative Foundations

- **April Dunford — Obviously Awesome**: record competitive alternatives, differentiated capabilities, customer value, best-fit segments, and market category as separate claims.
- **Clayton Christensen — Jobs to Be Done**: capture the progress buyers seek, the situation that triggers action, and the forces that resist change.
- **Geoffrey Moore — Beachhead and Whole Product**: distinguish the first defensible segment from the broader market and document what must exist for that segment to succeed.
- **Peep Laja — Message Mining**: preserve exact customer language and its source rather than paraphrasing every pain into generic marketing copy.

## Prerequisites

- Access to the user's approved public materials and any supplied internal source artifacts.
- A clear date or time window for claims that can change, such as pricing, customer count, integrations, or market status.
- Permission boundaries for private customer, employee, financial, or product-roadmap information.
- At least one owner who can resolve disputed or unknown claims.

## Step-by-Step Process

### 1. Inventory sources

List each source with owner, date, audience, and authority level. Prefer product documentation, signed commercial terms, approved positioning, customer research, CRM evidence, and direct user input. Label third-party claims separately.

### 2. Extract facts before synthesis

Capture company, product, pricing, packaging, target segment, geography, compliance, integration, and proof facts. Give each fact a source. Mark contradictions; do not silently choose one.

### 3. Model the customer situation

Describe the buyer role, company conditions, triggering event, current alternative, desired progress, success metric, and blockers. Preserve verbatim customer language in a quote bank when it was supplied.

### 4. Build the positioning chain

Map competitive alternatives → differentiated capabilities → customer value → proof → best-fit segment → category. Mark every unsupported link as an assumption or question.

### 5. Record operating constraints

Include channels allowed, legal or brand constraints, excluded segments, budget, capacity, sales motion, lifecycle definitions, and system-of-record ownership.

### 6. Create the reusable pack

Write a concise primary brief, a claim ledger, a voice guide, and an open-questions register. Put volatile facts behind an `as_of` date.

### 7. Validate with the owner

Ask the owner to accept, reject, or revise contradictions and high-impact assumptions. Do not promote an assumption to a verified fact without a source or explicit approval.

## Output Format

Produce a GTM context pack with:

1. Context metadata and scope.
2. Company and product facts.
3. ICP and buying-situation table.
4. Positioning chain and proof map.
5. Voice, vocabulary, and prohibited-claim guidance.
6. GTM motion, lifecycle, channel, and system constraints.
7. Claim ledger with source and freshness.
8. Assumptions, contradictions, and open questions.
9. Recommended downstream skills.

## Quality Check

- [ ] Every material factual claim has a source, owner, or explicit assumption label.
- [ ] Volatile claims include an `as_of` date.
- [ ] Customer language remains distinguishable from agent-written synthesis.
- [ ] Positioning names real competitive alternatives and evidence-backed differentiation.
- [ ] Contradictions are visible and assigned for resolution.
- [ ] Private data is scoped to the user's authorization and excluded from public outputs.
- [ ] The brief is compact enough to reuse without loading the full source corpus.

## Common Pitfalls

| Pitfall | Why it fails | Fix |
|---|---|---|
| Filling unknowns with plausible copy | Creates a polished but false source of truth | Use `unknown`, `assumption`, and `needs owner decision` labels |
| Mixing buyer roles | Produces generic pain and channel guidance | Build one row per role and buying situation |
| Treating positioning as a slogan | Hides the logic behind the message | Preserve the full alternatives-to-value chain |
| Copying every source into the pack | Defeats progressive disclosure | Summarize; link the evidence and quote only decisive language |
| Omitting freshness | Stale pricing and product claims spread across later work | Add `as_of`, owner, and review cadence |

## Execution Artifacts

- `references/framework-notes.md` — Framework mapping and evidence rules
- `templates/output-template.md` — Reusable GTM context pack
- `scripts/check-output.py` — Context-pack completeness validator

## Related Skills

- `gtm-context` for using an existing context pack in a specific engagement.
- `icp-scoring` for turning the ICP definition into a scored model.
- `positioning-messaging` for converting approved positioning into message architecture.
- `competitive-intel` for resolving weak competitive-alternative evidence.

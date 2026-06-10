---
name: sales-enablement
description: >-
  Create sales collateral that reps actually use — pitch decks, one-pagers,
  battlecards, objection docs, demo scripts, talk tracks, and playbooks. Use when
  the user wants to create sales materials, build a pitch deck, write a one-pager,
  create objection handling docs, or arm their sales team. Triggers on: "sales
  enablement", "pitch deck", "one-pager", "sales collateral", "battlecard",
  "sales deck", "objection doc", "sales playbook", "demo script", "leave-behind",
  "talk track", or any request about creating materials for sales teams.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: sales-revops
  tags: [sales-enablement, pitch-decks, battlecards, collateral]
  related_skills: [pipeline-management, pitch-deck-builder, one-pager-builder, battlecard-builder, demo-scripts, objection-handling, meeting-prep]
  frameworks:
    - "Winning by Design — GTM Playbook Development Kit"
    - "Winning by Design — SPICED Qualification"
    - "Force Management Command of the Message"
    - "Corporate Visions Messaging Frameworks"
    - "Andy Whyte — MEDDICC Scorecard"
    - "Force Management — MEDDICC Methodology"
---

# Sales Enablement

## Overview

Sales enablement materials are tools, not documents. If a rep can't find the
right asset in 30 seconds during a call, it might as well not exist. The best
enablement is concise, persona-specific, and structured for rapid access.

This skill coordinates the creation of a complete sales enablement package:
pitch deck, one-pagers per persona, objection handling docs, demo scripts,
and a GTM playbook aligned to the sales process defined in `pipeline-management`.

Load `pipeline-management` first if no stage definitions exist — enablement
assets must map to specific stages (Goal, Actions, Exit Criteria) and SPICED
fields, not float as disconnected PDFs.

## When to Use

- "Create a sales enablement package for our new product"
- "Build a pitch deck"
- "Write a one-pager for our champion"
- "Create objection handling docs"
- "Build a sales playbook"
- "Arm our reps with competitive materials"

## Authoritative Foundations

- **Winning by Design — GTM Playbook Development Kit.** The sales playbook is
  the operational layer of the sales process. Each playbook section maps to a
  pipeline stage: what to do (Actions), what evidence to capture (Exit Criteria),
  and which SPICED questions to ask. Reps use the playbook; managers inspect
  against the same criteria in deal reviews.
- **Winning by Design — SPICED.** Discovery questions, demo framing, and
  proposal language should elicit Situation, Pain, Impact, Critical Event, and
  Decision — organized by stage, not as a flat script.
- **Force Management — Command of the Message.** Before Scenario → PBOs →
  Required Capabilities → Defensible Differentiators. Every asset traces to this
  for message consistency across deck, one-pager, and battlecard.
- **Corporate Visions.** "Why change" → "why you" → "why now" progression
  converts better than feature-forward presentations.

## Prerequisites

- Positioning and messaging defined (use positioning-messaging)
- ICP and personas documented (use icp-scoring)
- Competitive intelligence gathered (use competitive-intel)

## Step-by-Step Process

### Phase 1: Asset Inventory

Determine what's needed:

| Asset | Audience | Purpose | Priority |
|---|---|---|---|
| Pitch Deck (10-15 slides) | Prospects, demos | Present value, drive to next step | Highest |
| One-Pagers (per persona) | Champions, post-meeting | Enable internal selling | High |
| Battlecards (per competitor) | Reps in competitive deals | Win competitive situations | High |
| Objection Handling Doc | Reps on every call | Handle pushback confidently | High |
| Demo Script | Reps running demos | Consistent, compelling demos | High |
| ROI Calculator | Economic buyers, CFOs | Quantify value | Medium |
| Case Studies (sales format) | Late-stage prospects | Prove results | Medium |
| Sales Playbook | All reps, onboarding | Central reference for everything | Medium |

### Phase 2: Asset Creation by Persona

Every asset should be persona-aware. A deck for a CTO has different content,
examples, and proof points than one for a VP of Sales.

| Persona | Key Concerns | Relevant Proof | Deck Focus |
|---|---|---|---|
| CTO / VP Eng | Integration, security, scalability | Technical case study, architecture diagram | Technical depth |
| VP Sales / CRO | Revenue impact, ramp time, adoption | Revenue metrics, rep productivity data | Business impact |
| CEO / Founder | Strategic, defensible growth | Market positioning, competitive moat | Vision + outcomes |
| Champion (internal) | Easy to sell internally, safe choice | One-pager, internal memo template | Enablement |

### Phase 3: GTM Playbook Structure (WbD-Aligned)

The playbook mirrors `pipeline-management` stage definitions. Structure by stage:

| Playbook Section | Maps To | Contents |
|---|---|---|
| ICP & Personas | Pre-Target | Who we sell to, disqualifiers |
| Stage 1–2: Target & Connect | Target, Connect | Outreach templates, Situation questions |
| Stage 3: Discovery | Discovery | SPICED question bank, Impact quantification |
| Stage 4: Solution | Solution | Demo scripts per persona, Champion development |
| Stage 5–6: Proposal & Negotiate | Proposal, Negotiation | Pricing talk track, Andy Whyte MEDDICC scorecard (0/1/2), Champion test card |
| Objection Handling | All stages | Top objections by stage, not generic list |
| Competitive Positioning | Solution onward | Battlecards with talk tracks |
| Handoff to CS | Closed Won | AE → CS package template (SPICED summary) |
| CRM Quick Reference | All stages | Stage names, exit criteria fields, conversion targets |

Each section must reference the Exit Criteria fields reps populate in CRM.
Managers and reps use the same document for execution and inspection.

## Output Format

Sales enablement package:
```
# Sales Enablement Package: [Product/Feature]

## Assets Produced
- [ ] Pitch Deck (10 slides, 3 persona variants)
- [ ] One-Pagers (CTO, VP Sales, Champion)
- [ ] Battlecards (Competitor A, B, C)
- [ ] Objection Handling Doc (6 categories, 30+ objections)
- [ ] Demo Script (3 variants: first demo, deep-dive, exec overview)
- [ ] ROI Calculator
- [ ] Case Studies (2-3, sales format)
- [ ] Sales Playbook (central reference)

## Access
- Deck: [link]
- Playbook: [link]
- All assets: [folder]
```

## Quality Check

- [ ] Playbook sections map to pipeline stages from `pipeline-management`
- [ ] SPICED questions organized by stage with CRM field names
- [ ] Every asset references the core positioning and messaging framework
- [ ] Assets are persona-specific (not one-size-fits-all)
- [ ] Reps can find any asset in under 30 seconds
- [ ] Battlecards include talk tracks, not just feature comparisons
- [ ] Demo script tested with a live audience
- [ ] All metrics and claims verified and sourceable

## Common Pitfalls

1. **One deck for everyone.** A CTO and a VP Sales care about different
   things. If your deck works for both, it works for neither.

2. **Feature dumps as decks.** Slides that list features without connecting
   them to customer problems are skipped. Every slide answers "so what?"

3. **No talk tracks in battlecards.** A feature comparison table without
   language the rep can actually say in a call isn't a battlecard —
   it's a reference doc.

4. **Assets nobody can find.** PDFs buried in a Drive folder. Build a
   single access point (Notion, SharePoint, dedicated Slack channel).

5. **Static assets.** Enablement degrades monthly. Schedule quarterly
   reviews to update metrics, add new competitors, and retire stale decks.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `references/force-management-playbook.md` — Repo root: Command of the Message, alignment cadence
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **pipeline-management**: Sales process and stage definitions (prerequisite)
- **pitch-deck-builder**: Detailed slide-by-slide deck construction
- **battlecard-builder**: Competitive battlecard creation
- **demo-scripts**: Demo script writing
- **objection-handling**: Objection taxonomy and response frameworks
- **positioning-messaging**: Foundation positioning these assets draw from

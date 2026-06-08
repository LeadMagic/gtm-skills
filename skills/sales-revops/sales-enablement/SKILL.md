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
  related_skills: [pitch-deck-builder, one-pager-builder, battlecard-builder, demo-scripts, objection-handling]
  frameworks:
    - "Force Management Command of the Message"
    - "Corporate Visions Messaging Frameworks"
    - "MEDDICC — Qualification"
---

# Sales Enablement

## Overview

Sales enablement materials are tools, not documents. If a rep can't find the
right asset in 30 seconds during a call, it might as well not exist. The best
enablement is concise, persona-specific, and structured for rapid access.

This skill coordinates the creation of a complete sales enablement package:
pitch deck, one-pagers per persona, objection handling docs, demo scripts,
and a sales playbook that ties everything together.

## When to Use

- "Create a sales enablement package for our new product"
- "Build a pitch deck"
- "Write a one-pager for our champion"
- "Create objection handling docs"
- "Build a sales playbook"
- "Arm our reps with competitive materials"

## Authoritative Foundations

This skill applies Force Management's Command of the Message Value Messaging
Framework: Before Scenario → PBOs → Required Capabilities → Defensible
Differentiators. Every sales asset should trace back to this framework for
message consistency.

Corporate Visions' messaging frameworks inform the structure: messages that
create a "why change" → "why you" → "why now" progression convert better
than feature-forward presentations.

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

### Phase 3: Sales Playbook Structure

The playbook is the central reference. Structure:

1. ICP and Personas — who we sell to
2. Qualification Criteria — when to pursue and when to walk away
3. Discovery Questions — organized by topic, not a script
4. Objection Handling — top 10 objections with responses
5. Competitive Positioning — per-competitor battlecards
6. Demo Flow — recommended sequence per persona
7. Pricing and Packaging — how to present, discount authority
8. Email Templates — follow-up, proposal, check-in, breakup
9. CRM and Process — how deals move through stages

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

## Related Skills

- **pitch-deck-builder**: Detailed slide-by-slide deck construction
- **battlecard-builder**: Competitive battlecard creation
- **demo-scripts**: Demo script writing
- **objection-handling**: Objection taxonomy and response frameworks
- **positioning-messaging**: Foundation positioning these assets draw from

---
name: demo-scripts
description: >-
  Write compelling demo scripts — first demo, technical deep-dive, and executive
  overview. Scene-by-scene with timing, talk tracks, and interaction points.
  Use when building demo scripts, preparing for a demo, or structuring product
  demonstrations. Triggers on: "demo script", "product demo", "demo flow",
  "how to demo", "demo structure", "demo talk track", or any demo-related request.
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.2.0"
  author: LeadMagic
  category: sales-revops
  tags: [demo, scripts, presentations, product-demo]
  related_skills: [sales-enablement, meeting-prep, objection-handling, pitch-deck-builder]
  frameworks:
    - "Force Management Command of the Message"
    - "Challenger Teach-Tailor-Take Control"
    - "MEDDICC — Qualification"
    - "Varun Anand (Clay) — Reverse Demo"
    - "Peter Cohan — Great Demo! Reverse Demo (incumbent walkthrough)"
---

# Demo Scripts

## Overview

The demo is where deals are won or lost. A great demo doesn't show features —
it tells the story of how the prospect's world changes after they buy. Every
scene connects a feature to a pain point to a business outcome.

This skill produces three demo variants: the first demo (10 min, discovery-
heavy), the technical deep-dive (45 min, for evaluation), and the executive
overview (20 min, outcomes-focused).

## When to Use

- "Write a demo script for our product"
- "Structure our product demo"
- "Build a demo flow for [persona]"
- "Create a technical deep-dive demo"
- "Write an executive demo overview"
- "Improve our demo conversion rate"

## Authoritative Foundations

Force Management's Command of the Message structures the demo around the
Value Messaging Framework: each feature shown maps to a Required Capability
that the discovery conversation established as critical.

Challenger's Teach-Tailor-Take Control: the demo should teach the prospect
something new about their problem, not just show your product. The best
demos reframe how the buyer sees their current state.

**Varun Anand (Clay) — Reverse Demo.** For complex or PLG-hybrid products,
flip the demo: the **prospect shares screen** and solves a real use case live
while the rep guides with annotations. Clay used 100+ sessions to reach
"a-ha" moments in minutes and improve conversion + product feedback. Load
`references/reverse-demo-varun.md` for the 30-minute structure, pre-call
checklist, and 2:1 prospect-control ratio. Pair with `customer-marketing`
→ `community-selling-varun.md` — end calls by onboarding prospects into Slack
for peer support.

**Peter Cohan — Great Demo! Reverse Demo (discovery variant).** When
displacing an incumbent, ask the prospect to demo **their current system**
first to surface likes, pain, and unknown gaps — then map your demo to what
they showed. Different motion from Clay's prospect-led product session;
use in discovery-heavy enterprise deals (`meeting-prep`).
Full playbook: `references/peter-cohan-great-demo.md` — Great Demo flow,
Do Something/Do Again, discovery-before-demo ratio.

## Step-by-Step Process

### Phase 1: Demo Variant Selection

| Variant | Length | Audience | Focus |
|---|---|---|---|
| First Demo | 10-15 min | Mixed, discovery first | Pain → Solution → Proof → Next Step |
| Technical Deep-Dive | 45-60 min | Technical stakeholders | Architecture, integration, security, scale |
| Executive Overview | 20 min | C-suite, economic buyers | Business outcomes, ROI, strategic alignment |

### Phase 2: First Demo Structure

Template: `templates/first-demo-script.md` — scene-by-scene with talk tracks,
screen actions, and interaction prompts.

### Phase 3: Technical Deep-Dive

Template: `templates/technical-demo-outline.md`

### Phase 4: Executive Overview

Template: `templates/executive-demo-outline.md` — outcomes, ROI, risk of wait.
Business case numbers → `deal-desk` business-case template.

### Phase 5: Reverse Demo (buyer-led)

Use when the product requires hands-on learning or PLG trial is available.

| Step | Action |
|---|---|
| Pre-call | Email: bring one concrete use case (or co-design in first 5 min) |
| Handoff | Prospect shares screen; rep provides signup link + Zoom annotations |
| Session | Prospect drives; rep guides — target **first win** in ≤30 min |
| Close | Community/Slack invite before scheduling follow-up |

Full playbook: `references/reverse-demo-varun.md`

## Output Format

Demo script document with scene-by-scene breakdown, talk tracks, screen
actions, and interaction prompts for each demo variant.

## Quality Check

- [ ] Every feature shown maps to a discovered pain point
- [ ] Discovery recap opens every demo variant
- [ ] Talk tracks are conversational, not scripted-sounding
- [ ] Interaction points built in (not a monologue)
- [ ] Differentiator clearly articulated and provable
- [ ] Next steps defined with timeline

## Common Pitfalls

1. **Feature tour disguised as demo.** Clicking through every menu item
   isn't a demo — it's a feature tour. Show workflows, not buttons.

2. **Talking about what, not why.** "Here's our dashboard" vs "Here's how
   you'll see your team's performance in real time — this view alone saved
   [customer] 5 hours per week." Always connect feature to outcome.

3. **No discovery recap.** Starting the demo without acknowledging what
   you learned in discovery tells the prospect you weren't listening.

4. **Pitching to one persona in a room of five.** The CTO and the VP Sales
   care about different things. Acknowledge all stakeholders.

5. **No clear differentiator moment.** If the prospect can't name one thing
   only you do after the demo, you failed to differentiate.

## Execution Artifacts

- `references/framework-notes.md`
- `templates/output-template.md`
- `scripts/check-output.py`
- `templates/first-demo-script.md` — 10–15 min discovery-led demo
- `templates/technical-demo-outline.md` — SE deep-dive
- `templates/executive-demo-outline.md` — Economic buyer overview
- `references/reverse-demo-varun.md` — Varun Anand / Clay buyer-led demo playbook
- `references/peter-cohan-great-demo.md` — Great Demo! + incumbent reverse demo

## Related Skills

- **meeting-prep**: Discovery that feeds into the demo
- **objection-handling**: Address objections that surface during demos
- **pitch-deck-builder**: The deck that supplements demos
- **sales-enablement**: Complete enablement package including demo scripts

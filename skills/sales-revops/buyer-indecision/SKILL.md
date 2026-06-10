---
name: buyer-indecision
description: >-
  Overcome buyer indecision with the JOLT Effect — Judge indecision, Offer
  recommendation, Limit exploration, Take risk off the table. For deals stuck
  on "need to think about it", FOMU (fear of messing up), and no-decision
  losses. Matthew Dixon & Ted McKenna. Use in late-stage enterprise deals,
  deal reviews, and proposal follow-up. Triggers on: "buyer indecision",
  "JOLT", "need to think about it", "no decision", "stuck deal", "FOMU",
  "fear of failure buyer", "close the gap intent to action".
license: MIT
compatibility: Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: sales-revops
  tags: [jolt, buyer-indecision, closing, enterprise, fomu, no-decision, late-stage]
  related_skills: [objection-handling, pipeline-management, meeting-prep, deal-desk, transparency-selling, multi-thread-orchestration, sales-coaching]
  frameworks:
    - "Matthew Dixon & Ted McKenna — The JOLT Effect (2022)"
    - "Matthew Dixon — The Challenger Sale (teaching, reframe)"
    - "Winning by Design — SPICED Decision criteria"
    - "Andy Whyte — MEDDICC (EB access, scorecard gates)"
---

# Buyer Indecision (JOLT Effect)

## Overview

"I need to think about it" is not an objection — it's **indecision**. Dixon
and McKenna's research on 2.5M+ sales conversations: **40–60% of B2B losses
are no-decision**, and **56% of those** are indecision (FOMU — fear of messing
up), not preference for status quo. Piling on ROI after intent is established
**backfires** — buyers fear failure more than they crave success.

JOLT complements Challenger (teach) and SPICED/MEDDICC (qualify). Use JOLT
**after** solution fit is verbal — when the buyer stalls before signature.

## When to Use

- "Deal stuck in negotiation / proposal"
- "Champion ghosting after verbal yes"
- "Need to think about it"
- "No decision lost deal analysis"
- "How to close enterprise indecision"
- "JOLT framework"
- "Buyer fear of failure"

Do not use JOLT for early discovery — use `meeting-prep` (SPICED). Do not
confuse with price objections — use `objection-handling` first, then JOLT if
stall persists after fit.

## Authoritative Foundations

- **The JOLT Effect** (Dixon & McKenna, 2022). Four moves for high performers:
  **J**udge level of indecision · **O**ffer recommendation · **L**imit exploration
  · **T**ake risk off the table. Source: https://www.jolteffect.com/
- **FOMU vs FOMO.** Fear of Messing Up > Fear of Missing Out at decision time.
  Seller role shifts from persuader to **buyer agent** reducing downside.
- **Challenger Sale** (Dixon). JOLT is late-stage; Challenger is early-stage teach.
- **MEDDICC / SPICED.** Champion must run JOLT internally on buying committee —
  equip them with recommendation and risk-removal assets.

## JOLT Framework

### J — Judge the Level of Indecision

Diagnose before acting. Indecision signals:

| Signal | Likely Type | Not This |
|---|---|---|
| "Need to run by [committee]" | FOMU — personal risk | Don't add more ROI slides |
| Endless POC extensions | Fear of wrong choice | Don't widen scope |
| New stakeholders late | Internal saboteurs / passive resistors | Don't ignore |
| Verbal yes, no paper | Champion can't sell internally | Don't pressure champion |

**Questions:**
- "What would make this feel safe to move forward?"
- "What's the downside you're most worried about?"
- "If you chose nothing, what happens in 90 days?"

Score 1–5 in deal review (`templates/jolt-deal-review.md`).

### O — Offer Your Recommendation

Indecisive buyers want **prescription**, not more options. High performers give
a clear "what I would do in your seat" recommendation.

**Script pattern:**
> "Based on everything we've discussed, my recommendation is [package A / phased
> start / single use case]. That's what I'd do if I were accountable for [outcome]."

Pair with SPICED Decision criteria — tie to their stated success metrics.

### L — Limit the Exploration

More information increases anxiety. Stop adding features, modules, and pricing
tiers. **Collapse choices** to 1–2 vetted paths.

| Do | Don't |
|---|---|
| "Here are two paths — A or B" | "Here's our full menu" |
| Fixed timeline for decision | Open-ended "whenever" |
| Pre-built business case (1 page) | 40-slide deck |

Align with `deal-desk` — standard packages, not infinite custom.

### T — Take Risk Off the Table

De-risk the **decision**, not just the product:

| Tactic | Example |
|---|---|
| Phased rollout | Pilot one team / one region |
| Success criteria | Mutual success plan with exit criteria |
| Executive sponsor | Your exec + their EB alignment call |
| Contract flexibility | Shorter initial term, renewal path clear |
| Implementation safety | Named CSM, 30-day checkpoint |

Maps to WbD Bowtie — left side onboarding promise reduces FOMU.

## Integration with GTM Stack

| Stage | Skill | JOLT Role |
|---|---|---|
| Discovery | `meeting-prep` SPICED | Build intent |
| Solution | `pipeline-management` MEDDICC | Score ≥14 gate |
| Proposal | `deal-desk` | Standard packages (Limit) |
| Stall | **buyer-indecision** JOLT | Judge → Offer → Limit → Take risk |
| Price pushback | `objection-handling` | Before or parallel to JOLT |
| Champion weak | `multi-thread-orchestration` | EB + JOLT assets for champion |

## Output Format

- **JOLT deal review** — `templates/jolt-deal-review.md` with indecision score
- **Champion kit** — 1-page recommendation + risk removal for internal sell
- **Call plan** — J/O/L/T talk track for next meeting
- **Win-loss tag** — no-decision vs indecision vs lost-to-competitor

## Quality Check

- [ ] Verbal fit established before JOLT (not used as discovery shortcut)
- [ ] Indecision diagnosed (J) — not treated as status quo objection
- [ ] Clear recommendation offered (O) — not "what do you want?"
- [ ] Options limited (L) — max 2 paths
- [ ] Risk removal explicit (T) — phased, success plan, or exec alignment
- [ ] Champion equipped to run JOLT on internal committee

## Common Pitfalls

1. **More ROI when they're scared.** Increases analysis paralysis. Fix: Limit + Take risk.
2. **Single-threaded champion.** Champion can't de-risk alone. Fix: EB meeting + mutual plan.
3. **Unlimited POC.** No success criteria = infinite stall. Fix: time-boxed pilot with T.
4. **Confusing objection with indecision.** "Too expensive" needs value work; "think about it"
   after fit needs JOLT.
5. **Skipping Judge.** Applying O/L/T blindly. Fix: score indecision type first.

## Execution Artifacts

- `references/framework-notes.md` — Framework index and authority routing
- `templates/output-template.md` — Primary deliverable shell
- `scripts/check-output.py` — Validates JOLT deliverables (Judge, Offer, Limit, Take risk)
- `references/jolt-playbook.md` — Full J/O/L/T tactics and talk tracks
- `templates/jolt-deal-review.md` — Deal review scorecard

## Related Skills

- `objection-handling` — Taxonomy and AER for pushback
- `pipeline-management` — Stage gates, MEDDICC scorecard
- `transparency-selling` — Todd Caponi trust-building pre-JOLT
- `deal-desk` — Package design for Limit step
- `sales-coaching` — Manager deal review with JOLT lens (jolt-coaching reference)

---
name: positioning-messaging
description: >-
  Build positioning and messaging from category, ICP, alternatives, differentiated value, proof, and buyer language. Produces a positioning statement, message hierarchy, persona messaging matrix, homepage narrative, and sales talk tracks. Use when messaging sounds generic, launches need positioning, or competitors blur differentiation.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: foundation
  tags: [positioning, messaging, narrative, category-design, pitch, value-proposition]
  related_skills: [gtm-context, icp-scoring, competitive-intel, pitch-deck-builder]
  frameworks: [April Dunford Positioning, Andy Raskin Strategic Narrative, Christopher Lochhead Category Design, Force Management Command of the Message, Challenger Sale]
---
# Positioning & Messaging

## Overview

The most expensive mistake in B2B go-to-market is building messaging from the product outward — listing features, describing benefits, and hoping the right buyer recognizes themselves. The non-obvious rule is that effective positioning starts with the competitive alternative the customer currently uses (even if that alternative is a spreadsheet or manual process), not with your product. When positioning begins with the product, every competitor sounds the same. When it begins with the customer's current reality and the gap between that reality and what's possible, differentiation emerges naturally.

This skill produces a complete positioning and messaging system grounded in four established frameworks: April Dunford's 5-component positioning statement (Competitive Alternatives → Unique Capabilities → Value → Target Customers → Market Category), Andy Raskin's strategic narrative structure (Old Game vs New Game with the "Promised Land"), Christopher Lochhead's category design principles (naming and claiming a new category rather than competing in an existing one), and Force Management's Command of the Message Value Messaging Framework (Before Scenario, Negative Consequences, After Scenario, Positive Business Outcomes, Required Capabilities, Defensible Differentiators).

The deliverables are a Positioning Canvas (Dunford's 5 components + category design analysis), a Persona-Based Messaging Matrix (key messages per persona, per buying stage), a Strategic Narrative Deck Outline (Raskin structure with slide-by-slide guidance), and a VMF Integration (Force Management's six-element value messaging mapped to your product). Together these form the messaging foundation that every outbound email, pitch deck, landing page, and sales script draws from.

## When to Use

- User says "position our product" or "create positioning statement" → activate this skill
- User asks for "strategic narrative," "pitch story," or "messaging framework" → use this skill
- User mentions "April Dunford," "Andy Raskin," "category design," or "value prop" → this skill applies
- User needs a messaging matrix for different buyer personas
- User is creating a pitch deck and needs the underlying narrative structure
- User's messaging feels undifferentiated and they want to rebuild from first principles
- After gtm-context is complete, when competitive landscape and ICP are defined

Do NOT use for:
- Writing specific cold email copy — use cold-email-copywriting (this skill provides the messaging source material)
- Building a pitch deck visually — use pitch-deck-builder (this skill provides the narrative outline)
- Sales script writing — use sales-enablement or demo-scripts (this skill provides the messaging components)

## Authoritative Foundations

- **April Dunford — Obviously Awesome Positioning.** The 5-component positioning statement is the most practical positioning framework in B2B SaaS. Components: Competitive Alternatives (what the customer does today), Unique Capabilities (what only you can do), Value (what those capabilities enable), Target Customers (who cares most), Market Category (the context you compete in). This skill implements all five components in sequence.

- **Andy Raskin — The Greatest Sales Deck I've Ever Seen.** The strategic narrative structure: (1) Name a big, relevant shift in the world, (2) Show there are winners and losers, (3) Tease the Promised Land, (4) Introduce features as "magic gifts" that unlock the Promised Land, (5) Present evidence you can make it happen. This skill builds the narrative arc for pitch decks and category-defining presentations.

- **Christopher Lochhead — Play Bigger / Category Design.** Category design argues that the company that designs the category wins the category. Naming the problem space differently reframes the competitive landscape. This skill includes a category design analysis that evaluates whether existing categories adequately describe the value or whether a new category lens is warranted.

- **Force Management — Command of the Message Value Messaging Framework (VMF).** Six elements: Before Scenario (customer's current state), Negative Consequences (cost of staying the same), After Scenario (what's possible), Positive Business Outcomes (measurable results), Required Capabilities (what must be true for the After Scenario), Defensible Differentiators (why only you). This skill maps each VMF element to specific messaging components.

- **Gartner — Challenger Sale Insight Generation.** The Challenger methodology's emphasis on teaching prospects something new about their business and reframing their problem. Applied in the strategic narrative to ensure the "big shift" insight is genuinely provocative, not obvious.

- **Winning by Design — Bowtie Model and SPICED.** The Bowtie's expansion beyond acquisition into retention and expansion ensures messaging addresses the full customer lifecycle. SPICED's Pain and Impact dimensions inform the Negative Consequences and Positive Business Outcomes in the VMF.

## Prerequisites

- **Upstream skills:** gtm-context must be complete. The ICP definition, competitive landscape, and product overview from gtm-context are direct inputs.
- **Required inputs:** ICP definition (target customers, their current alternatives, their pain points), competitive landscape (who they currently use, alternatives), product capabilities (what your product actually does, unique capabilities).
- **Optional:** Customer interview transcripts, win/loss analysis, sales call recordings, competitor website and G2 review analysis.
- **Optional tools:** LeadMagic Company Search and Technographics APIs can enrich competitor data and validate that target customers actually use the competitive alternatives you're positioning against.

## Step-by-Step Process

### Phase 1: Intake

Ask all questions at once:

1. What are the 3-5 things your target customers currently do to solve the problem your product addresses? (Be specific — name tools, manual processes, workarounds.)
2. What are the 3-5 capabilities your product has that none of those alternatives have? What can only your product do?
3. For your 3 best customers: what value did they get that they weren't getting before? Quantify if possible (time saved, revenue gained, cost reduced).
4. Who cares most about the problem you solve? Is there a specific persona, industry, or situation where the pain is most acute?
5. What market category do you currently describe yourself as belonging to? Is that category crowded or uncontested?
6. Provide any existing positioning language, taglines, or pitch deck narrative you've used.
7. What are the 3-5 biggest "before vs after" contrasts your customers experience? What was life like before your product, what is it like after?

### Phase 2: Research

**Competitive Alternative Deep Dive:** For each competitive alternative identified, research:
- How they position themselves (website, G2, press)
- What customers say about them (G2 reviews, Reddit, social media)
- Their pricing and packaging
- Their target customer profile
- Their key weaknesses and limitations

The goal is to understand the full landscape of alternatives your customers currently use, from direct competitors to the "do nothing" option.

**Customer Language Extraction:** From customer interviews, sales calls, and review data, extract the exact words and phrases customers use to describe:
- Their problem before your product
- What they tried before finding you
- The moment they realized they needed something different
- The value they've received
- How they describe your product to colleagues

This language becomes the raw material for messaging. Never use internal jargon when customer language is available.

**Category Landscape Analysis:** Research the market category (or categories) your product could belong to. Analyze:
- Existing category names and their associated vendors
- Category size and growth trajectory
- Analyst coverage (Gartner Magic Quadrant, Forrester Wave)
- Media and search volume for category keywords

Evaluate whether fitting into an existing category or designing a new category is the right strategic choice.

### Phase 3: Execution

**Step 1: Dunford Positioning Statement**

Build the 5-component positioning statement in sequence:

1. **Competitive Alternatives:** List the 3-5 things customers do today. Be honest — include "do nothing" or "spreadsheets" if that's the reality. This is the foundation. Every other component references this list.

2. **Unique Capabilities:** For each competitive alternative, identify what your product does that the alternative cannot. A capability is only "unique" if no competitive alternative has it. Features that competitors also have are not unique capabilities — they're table stakes.

3. **Value:** For each unique capability, articulate the value it unlocks. Value answers "so what?" — the unique capability might be "real-time data sync," but the value is "sales team always has accurate pipeline data without manual entry." Value should be expressed in the customer's language, ideally with quantification.

4. **Target Customers:** Based on the value articulation, identify who cares most. This should align with the ICP from gtm-context but may narrow it further. The best target customer is the one for whom the value of your unique capabilities is highest relative to the cost of switching.

5. **Market Category:** Choose the market context. If an existing category describes what you do and you can be the best in it, claim it. If existing categories don't capture your differentiation, consider category design — name the problem space differently.

**Step 2: Raskin Strategic Narrative**

Build the narrative structure:

1. **The Big Shift:** Name a change in the world that makes the old way obsolete. This must be a genuine, observable trend — not a marketing claim. Examples: "Buyers now complete 70% of their evaluation before talking to sales," "Remote work has made async collaboration the default."

2. **Winners and Losers:** Show that companies adapting to the shift are winning and those who aren't are falling behind. Use specific examples or data points. The tension between winners and losers creates urgency.

3. **The Promised Land:** Describe the desirable future state — what's possible when a company fully embraces the new way. Make it aspirational but concrete. The promised land is not "using our product." It's the business outcome using the product enables.

4. **Magic Gifts:** Introduce your product's capabilities as the means to reach the Promised Land. Each "gift" directly addresses a barrier between the current state and the Promised Land. Features are gifts, not a list.

5. **Proof:** Present evidence that the Promised Land is real and reachable — customer logos, results data, third-party validation, team credentials.

**Step 3: Persona-Based Messaging Matrix**

Create a matrix mapping key messages to each persona and buying stage:

- **Awareness Stage:** What does this persona need to hear to recognize they have a problem worth solving?
- **Consideration Stage:** What does this persona need to hear to evaluate your solution against alternatives?
- **Decision Stage:** What does this persona need to hear to justify the purchase internally?

For each persona-stage combination, provide:
- Core message (one sentence)
- Supporting points (2-3 bullets)
- Proof point (specific metric or customer example)
- Objection pre-handle (the most likely objection and a response)

**Step 4: VMF Integration (Force Management)**

Map Command of the Message elements:

- **Before Scenario:** Detailed description of the customer's current state, including specific pain points, inefficiencies, and costs.
- **Negative Consequences:** What happens if the customer does nothing? Quantify the cost of inaction — lost revenue, wasted time, competitive disadvantage, risk.
- **After Scenario:** The transformed state — what's possible when the problem is solved. Paint the picture in concrete, measurable terms.
- **Positive Business Outcomes:** Specific, quantifiable results. Revenue gained, costs reduced, time saved, risk mitigated. These are the metrics the Economic Buyer cares about.
- **Required Capabilities:** The capabilities that must exist for the After Scenario to be achievable. These are not product features — they are the functional requirements. Then map your product features to each required capability.
- **Defensible Differentiators:** Why only your company can deliver the Required Capabilities. Technology, data, network effects, expertise, integrations, customer base — what creates a moat?

**Step 5: Category Design Analysis**

Evaluate the category strategy:
- Is the existing category crowded (5+ well-funded competitors)?
- Does the existing category name accurately describe your differentiation?
- Is there an underserved segment within the category that could be its own category?
- What would you name the new category? (3-5 options with rationale)
- What would the category's key performance indicators be?

If category design is recommended, provide: category name, category definition, point-of-view manifesto, and ecosystem map (who else belongs in this category).

### Phase 4: Delivery

Present deliverables in this order:
1. Positioning Statement (Dunford 5 components)
2. Strategic Narrative Deck Outline (Raskin structure)
3. Messaging Matrix (by persona, by stage)
4. VMF Canvas (Before/After/Negative Consequences/Outcomes/Capabilities/Differentiators)
5. Category Design Recommendation (if applicable)
6. Language Guidelines (voice, tone, words to use, words to avoid)

## Output Format

```markdown
# Positioning & Messaging: [Company Name]

## 1. Positioning Statement (April Dunford)

**Competitive Alternatives:**
- [Alternative 1 — what customers do today]
- [Alternative 2]
- [Alternative 3]

**Unique Capabilities:**
- [Capability only your product has, and which alternative it beats]
- [Capability only your product has]
- [Capability only your product has]

**Value:**
- [Capability] → [Value enabled, with quantification if possible]
- [Capability] → [Value enabled]
- [Capability] → [Value enabled]

**Target Customers:**
[Who cares most about this value — specific persona, industry, situation]

**Market Category:**
[Category name and rationale — existing category or new category design]

---

## 2. Strategic Narrative (Andy Raskin)

### The Big Shift
[Observable trend that makes the old way obsolete]

### Winners and Losers
[Companies adapting = winning. Companies not adapting = losing. Evidence.]

### The Promised Land
[Desirable future state — concrete, aspirational, business outcome, not product]

### Magic Gifts
1. [Gift 1 — capability that unlocks a barrier to the Promised Land]
2. [Gift 2]
3. [Gift 3]

### Proof
[Customer logos, results, third-party validation, team credentials]

---

## 3. Messaging Matrix

| Persona | Awareness | Consideration | Decision |
|---------|-----------|---------------|----------|
| [Persona 1] | Core: [1 sentence]<br>Supporting: [2-3]<br>Proof: [1]<br>Objection: [1] | [...] | [...] |
| [Persona 2] | [...] | [...] | [...] |

---

## 4. VMF Canvas (Force Management)

### Before Scenario
[Detailed current state, pain, cost]

### Negative Consequences
[Cost of inaction — quantified]

### After Scenario
[Transformed state — concrete and measurable]

### Positive Business Outcomes
- [Outcome 1 with metric]
- [Outcome 2 with metric]
- [Outcome 3 with metric]

### Required Capabilities
- [Capability 1] → [Your feature that delivers it]
- [Capability 2] → [Your feature that delivers it]

### Defensible Differentiators
- [Differentiator 1 and why competitors can't replicate it]
- [Differentiator 2 and why competitors can't replicate it]

---

## 5. Category Design Recommendation

[Category strategy recommendation with rationale, category name options, category definition, and manifesto if applicable]

---

## 6. Language Guidelines

**Voice:** [3-5 adjectives describing how you sound]
**Words to use:** [List]
**Words to avoid:** [List]
**Internal jargon → Customer language:** [Translation table]
```

## Quality Check

Before delivering, verify:

- [ ] Does the positioning statement begin with competitive alternatives, not with your product?
- [ ] Are unique capabilities actually unique (no competitor has them)?
- [ ] Does the strategic narrative name a genuine, observable shift — not a marketing claim?
- [ ] Is the Promised Land a business outcome, not "using our product"?
- [ ] Does the messaging matrix cover every persona identified in the ICP?
- [ ] Are negative consequences quantified with real data rather than vague statements?
- [ ] Does the VMF map every Required Capability to a specific product feature?
- [ ] Are defensible differentiators truly defensible (competitors can't easily replicate)?
- [ ] Does the messaging use customer language extracted from research rather than internal jargon?
- [ ] Would a prospect reading the awareness-stage messaging recognize themselves in it?

## Common Pitfalls

1. **Starting positioning with the product instead of competitive alternatives.** The most common positioning error. Dunford's framework works because it forces you to first understand what the customer currently does. If you skip to unique capabilities without establishing the baseline, the capabilities sound like generic feature claims.

2. **Confusing features with unique capabilities.** "AI-powered" is a feature. "Automatically generates personalized outreach based on buying signals from 12 data sources" is a unique capability — if no competitor does it. Every claimed unique capability must pass the test: "Do any of our competitive alternatives do this?"

3. **Strategic narrative that sells the product instead of the shift.** Raskin's structure works because it creates belief in a new way of doing things BEFORE introducing the product. If the narrative is "here's why our product is great," it's not a strategic narrative — it's a pitch. The product should feel inevitable by the time you introduce it.

4. **Messaging matrix that says the same thing to every persona.** Different personas care about different things. The Economic Buyer cares about ROI and risk. The End User cares about usability and time savings. The Technical Evaluator cares about security and integration. If every persona gets the same message, the matrix isn't doing its job.

5. **VMF that skips negative consequences.** The Before Scenario and Negative Consequences are the most emotionally powerful components of the VMF. Without them, the After Scenario and Positive Business Outcomes feel like empty promises. The cost of inaction must be made concrete and specific.

6. **Category design that renames an existing category with a buzzword.** Adding "AI-powered" or "next-gen" to an existing category name is not category design. Category design requires a fundamentally different way of framing the problem space — one that makes incumbents look like they're solving yesterday's problem.

7. **Voice guidelines that describe an aspiration rather than a reality.** "We sound like trusted advisors" is meaningless. Describe specific attributes: "We use short sentences. We cite data. We ask questions more than we make claims. We never use the word 'leverage' as a verb."

8. **Messaging that sounds like it was written by a committee.** Strong positioning has a point of view. It deliberately excludes some buyers. It takes a stance. If the messaging tries to appeal to everyone, it appeals to no one. The target customer section should make it clear who this is NOT for.

## Execution Artifacts

- `references/framework-notes.md` — Named frameworks and reference tables
- `templates/output-template.md` — Deliverable shell for agent output
- `scripts/check-output.py` — Lightweight deliverable validator

## Related Skills

- **gtm-context**: Run before this skill. Provides ICP definition, competitive landscape, and product overview.

- **competitive-intel**: Run before or alongside this skill. Deepens competitor understanding to sharpen unique capabilities and defensible differentiators.

- **pitch-deck-builder**: Run after this skill. Consumes the strategic narrative and VMF to build a slide-by-slide pitch deck.

- **cold-email-copywriting**: Run after this skill. Uses the messaging matrix and language banks to write persona-specific outreach.

- **one-pager-builder**: Run after this skill. Uses the positioning statement to create sales-ready one-pagers.

- **sales-enablement**: Run after this skill. Consumes the messaging matrix and VMF to build sales playbooks and talk tracks.

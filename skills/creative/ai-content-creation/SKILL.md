---
name: ai-content-creation
description: >-
  AI-powered content creation workflows — step-by-step processes for using
  Claude, ChatGPT, Jasper, Copy.ai, Writesonic, and Perplexity to generate,
  edit, and optimize blog posts, social media content, email sequences, ad
  copy, landing page copy, and SEO content. Use when scaling content
  production, building an AI-assisted content pipeline, or teaching
  non-writers to produce high-quality content with AI. Triggers on: "AI
  content", "ChatGPT for blog", "AI copywriting", "scale content with AI".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: creative
  tags: [ai-content, chatgpt, claude, copywriting, blog-writing, ai-copy, content-creation, jasper, perplexity]
  related_skills: [vibe-marketing, copywriting, blog-writing, social-media-strategy, seo-content-strategy, ad-creative-strategy, content-marketing]
  frameworks:
    - "Justin Welsh — Content Operating System (repurposing lattice)"
    - "Harry Dry (Marketing Examples) — Show, don't tell"
    - "Amanda Natividad (SparkToro) — Zero-click content"
    - "Ross Simmonds — Content distribution at scale"
    - "Nail Rodriguez — Conversion copywriting"
---

# AI Content Creation

## Overview

AI writes. Humans edit. Together, they produce 5-10x more content than either
alone. The mistake: asking AI to "write a blog post about X" and publishing
the output. That produces AI slop. The fix: a structured workflow where AI
generates research, outlines, and first drafts — and humans inject unique
insight, experience, and voice. This skill covers step-by-step AI content
workflows for every format: blog posts, social, email, ads, landing pages,
and SEO content.

## When to Use

Trigger phrases: "AI content creation", "ChatGPT for blog writing", "AI
copywriting", "Claude content workflow", "scale content with AI", "AI
email writing", "AI social media content", "Jasper vs ChatGPT", "AI
blog post workflow"

## The AI Content Stack

| Tool | Best For | Cost | Quality |
|---|---|---|---|
| **Claude 4 (Opus)** | Long-form, strategy, technical | $20/mo | Exceptional — best for B2B long-form |
| **ChatGPT 4o** | Short-form, creative, variants | $20/mo | Excellent — best for hooks and variants |
| **Perplexity** | Research, data gathering, fact-checking | Free-$20/mo | Research-grade with citations |
| **Jasper** | Enterprise content teams, brand voice | $49-125/mo | Good with brand voice training |
| **Copy.ai** | Sales copy, email, social | $36/mo | Good for short-form templates |
| **Writesonic** | SEO content, blog posts | $16/mo | Decent for SEO-first content |

## The Master Workflow (All-Format)

### Phase 1: Research & Outline (AI-Assisted)

```
STEP 1 — Topic Research (Perplexity / Claude with Search):
"Research the current state of [topic] in [industry]. Find:
- Top 5 recent articles/posts on this topic
- Key statistics (with sources)
- Common opinions and contrarian takes
- What's missing from existing coverage"

STEP 2 — Outline (Claude):
"Create a detailed outline for a [format] about [topic].
Audience: [ICP]. The piece should answer: [specific question].
Include: [sections/elements specific to format].
Avoid: [things you DON'T want — AI slop, generic advice, etc.]"

STEP 3 — Unique Angle Injection (Human):
Add to the outline:
- Your unique data/experience
- Specific customer examples
- Contrarian or original opinions
- Frameworks you've developed
```

### Phase 2: Drafting (AI First Draft)

```
STEP 4 — First Draft (Claude):
"Write a [format] based on this outline. [paste outline].

Voice: [paste brand voice guide].
Rules:
- Short sentences. Under 25 words.
- Active voice. No passive constructions.
- Specific over generic. '47% reply rate' not 'industry-leading engagement'
- Show, don't tell. Every claim with evidence.
- No: 'In today's fast-paced world...' 'We're excited to announce...'
- Include: [specific data, examples, frameworks from outline]"
```

### Phase 3: Human Edit (Where Quality Happens)

**The 4-pass edit:**

| Pass | Focus | Time |
|---|---|---|
| **Pass 1: Substance** | Are claims true? Are examples real? Is the data correct? | 10 min |
| **Pass 2: Structure** | Does the argument flow? Is anything missing or redundant? | 10 min |
| **Pass 3: Voice** | Does it sound like us? Cut AI-isms: "delve," "unlock," "revolutionize" | 10 min |
| **Pass 4: Polish** | Typos, grammar, links, CTAs, formatting | 5 min |

**AI-isms to delete (common ChatGPT/Claude tells):**
- "In today's fast-paced digital landscape..."
- "Unlock the power of..."
- "Delve into..."
- "It's important to note that..."
- "Furthermore..." / "Moreover..." / "Additionally..."
- "In conclusion..."
- "Revolutionary," "game-changing," "cutting-edge"
- Overuse of em-dashes and semicolons
- Every sentence the same length (AI loves ~20-word sentences)

### Phase 4: Variants and Optimization

**Generate variants for testing (ChatGPT is best for this):**

```
"Here is our [blog post / email / ad]. Generate 5 variants of:
1. The headline only
2. The opening paragraph/hook
3. The CTA

Make each variant significantly different. Test different angles:
- Benefit-focused: '[Get Outcome]'
- Curiosity: '[Question they want answered]'
- Social proof: 'How [Company] achieved [Result]'
- Contrarian: 'Why [common belief] is wrong'
- Urgency: 'Stop [pain] before [consequence]'"
```

## Format-Specific Workflows

### Blog Post (2,000 words — 2 hours total)

```
HOUR 1 — AI-Assisted:
- Perplexity: Research topic, collect stats, find sources (15 min)
- Claude: Generate outline from research + unique angle (10 min)
- Claude: Write first draft from outline (15 min)
- Claude: Generate 5 headline variants (5 min)
- Human: 4-pass edit (15 min)

HOUR 2 — Production:
- Claude: Generate meta description, social descriptions (5 min)
- Canva/Midjourney: Hero image + in-post graphics (20 min)
- WordPress/Webflow: Format, add images, internal links (20 min)
- Claude: Generate 5 social post variants for promotion (5 min)
- Schedule social posts (10 min)
```

### LinkedIn Post (200 words — 30 min)

```
CLAUDE PROMPT:
"Write a LinkedIn post about [topic]. 

Structure:
- Hook (line 1): bold claim or surprising stat
- Body (4-6 short paragraphs): one idea per paragraph. White space between.
- CTA: question that invites comments

Rules:
- Single idea. Not 3 ideas.
- First line must stop the scroll. Test with: 'Would you stop scrolling?'
- Every paragraph 1-2 sentences max.
- No hashtags at end (put 3-5 relevant hashtags in a comment)
- No 'I'm excited to share' — just share the thing
- Write at 8th grade reading level

Voice: [paste brand voice]
ICP: [describe audience]"
```

### Email Sequence (3 emails — 1 hour)

```
CLAUDE PROMPT:
"Write a 3-email nurture sequence for [lead magnet or trigger].

EMAIL 1 — Delivery (immediate):
- Deliver the promised resource
- One insight from it
- What to do next

EMAIL 2 — Value (Day 3):
- One specific tip related to the resource
- How a customer used this to achieve [result]
- Link to related content

EMAIL 3 — Product Bridge (Day 7):
- The problem the resource helps with
- Why manual/current solutions fail
- How our product automates/solves this
- CTA: start trial / book demo

Rules:
- Subject lines under 50 chars. Preview text under 100 chars.
- Each email: one CTA. Not three.
- Plain text feel. No heavy HTML.
- From: [real person name] not 'The [Company] Team'
- 150-250 words per email"
```

### Ad Copy (5 variants — 30 min)

```
CLAUDE PROMPT:
"Write 5 LinkedIn ad variants for [offer/product].

Each variant:
- Headline (under 150 chars)
- Body (under 300 chars)
- CTA (under 20 chars)

Variants should test:
1. Pain-focused: problem → solution
2. Outcome-focused: what they'll achieve
3. Social proof: 'Join X teams using [product]'
4. Curiosity: a question they haven't considered
5. Direct offer: 'Try [product] free for 14 days'

Audience: [ICP]
Key benefit: [primary value prop]
URL: [landing page]"

Then (human): review. Pick 2-3. Launch. Kill underperformers at 48 hours.
```

### SEO Content (Pillar Page — 3 hours)

```
HOUR 1 — Research:
- Ahrefs/Semrush: Identify target keyword + 10 related keywords
- Perplexity: Research competitor content for this keyword
- Claude: "Analyze the top 5 ranking pages for [keyword]. What do they
  cover? What's missing? What can we do better?"

HOUR 2 — Draft:
- Claude: "Write a comprehensive pillar page targeting [keyword].
  Include: [outline from research]. Target 3,000 words.
  Use related keywords naturally: [list]."
- Claude: Generate meta title, meta description, H1, URL slug

HOUR 3 — Optimize:
- SurferSEO/Clearscope: Optimize for keyword density, LSI keywords
- Add internal links to related content
- Add external links to authoritative sources
- Add CTAs (lead magnet, trial, demo) at natural break points
```

## Output Format

```
AI CONTENT BRIEF — [Title/Topic]

Format: [blog / social / email / ad / landing page]
Target keyword (if SEO): [keyword]
Audience: [ICP]
Goal: [signup, demo, share, purchase]

AI Tools Used: [Claude / ChatGPT / Perplexity / etc.]

OUTLINE:
[Sections with key points]

FIRST DRAFT:
[Paste AI output]

HUMAN EDITS:
- Pass 1 (substance): [changes made]
- Pass 2 (structure): [changes]
- Pass 3 (voice): [changes]
- Pass 4 (polish): [changes]

FINAL: [link or paste]

VARIANTS (for testing):
1. [Headline variant 1]
2. [Headline variant 2]
3. [Headline variant 3]
```

## Quality Checklist

- [ ] Research phase completed before drafting (don't ask AI to write blind)
- [ ] Outline includes unique human insight (not just AI summary of existing content)
- [ ] 4-pass human edit completed (substance, structure, voice, polish)
- [ ] AI-isms deleted ("delve," "unlock," "furthermore," "in conclusion")
- [ ] Every claim has evidence or source (statistics, customer quotes, data)
- [ ] Voice matches brand guidelines (paste them into every content prompt)
- [ ] Headlines are specific, not clever ("47% more replies" > "Unlock email potential")
- [ ] SEO: target keyword in title, H1, first 100 words, meta description

## Common Pitfalls

1. **Publish AI output without editing.** Raw AI output = generic, detectable,
   low-trust content. Fix: 4-pass human edit. AI writes drafts. Humans make
   them good.

2. **No unique angle.** AI can only summarize what's already been written.
   If you don't inject unique data, experience, or opinion, your content
   is a remix of page 1 results. Fix: Unique angle first. AI draft second.

3. **"Write a blog post about X" (one-shot).** One-shot prompts produce
   generic, meandering content with no structure. Fix: Research → outline
   → draft → edit. AI assists each step. It doesn't replace any.

4. **Not including brand voice in prompts.** Every AI output without brand
   context sounds the same. Fix: Paste voice guide into every prompt.
   Better: build a custom GPT with your brand voice trained in.

5. **Hallucinated statistics.** "According to a recent study..." with no
   source. Fix: Perplexity for research. Every stat needs a citation.
   Human verifies before publishing.

6. **AI-generated images without review.** Midjourney produces beautiful
   nonsense. "Data visualization" with made-up numbers. Charts with
   impossible scales. Fix: Review every AI image for accuracy.

## Related Skills

- `vibe-marketing` — Full AI marketing stack and workflow
- `copywriting` — Marketing copy fundamentals and frameworks
- `blog-writing` — Blog post structure and SEO
- `social-media-strategy` — Per-platform content and cadence
- `ad-creative-strategy` — Creative formats, testing methodology
- `seo-content-strategy` — Keyword research, content clusters
- `vibe-coding` — AI dev tools for building GTM assets
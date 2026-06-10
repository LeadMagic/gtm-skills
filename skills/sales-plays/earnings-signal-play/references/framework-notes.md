# Earnings Signal Play — Framework Notes

Reference material for the `earnings-signal-play` skill. Keep `SKILL.md` concise;
use this file for extended tables, keyword lists, and prompt templates.

---

## Filing Section to Outreach Mapping

| SEC Filing Section | What to Read For | Outreach Application |
|---|---|---|
| **Item 1 — Business** | Named segments, stated strategy, competitive moat language, geography expansion | Identify initiative owners by function; name the segment in the subject line |
| **Item 1A — Risk Factors** | Ranked operational risks (order ≈ management priority); regulatory threats; supply chain / talent risks | Convert each risk to a Reimer-style discovery question (see below) |
| **Item 7 — MD&A** | Management's own forward guidance; known trends and uncertainties; year-over-year narrative | Mirror MD&A language in exec outreach — this is how the exec talks about their own business |
| **Financial Statements** | Revenue by segment, gross margin trends, R&D / S&M spend ratios | Proof-point anchor: "At $[revenue], teams at your stage typically see [X]" |
| **10-Q vs. 10-K Delta** | Where Q actuals diverge from the annual plan stated in the 10-K | Live pain identification: plan/actual gaps are in-flight problems, not future risks |

---

## Legloire Keyword Search List

Run Ctrl+F (or an LLM extraction prompt) on the full filing text for these terms.
Log every hit with section reference and page number.

**Priority keywords (signal strength: high):**
- `invest in` / `investing in`
- `initiative` / `strategic initiative`
- `accelerate` / `accelerating`
- `priority` / `top priority`
- `double down` / `doubling down`
- `expand` / `expansion`
- `headcount` / `hiring` / `headcount plan`

**Risk/pain keywords (signal strength: high for discovery questions):**
- `risk` / `risk factor`
- `headwind`
- `pressure` / `margin pressure`
- `uncertainty` / `known uncertainties`
- `competitive pressure`
- `churn` / `retention`
- `inefficiency` / `operational challenges`

**Timing markers (signal strength: moderate — window indicators):**
- `by end of fiscal year`
- `in the next [N] quarters`
- `we have already begun`
- `currently underway`
- `planned for [period]`

**Private company workaround (Legloire method):**
For private target accounts, run this keyword list against the 10-Ks of their
top two to three public competitors. Industry-level risk factors and priorities
transfer — you're borrowing the filing as a proxy for the private company's
operational reality.

---

## Reimer Risk Factor → Discovery Question Conversion

Pattern from Jamal Reimer's GTMnow / Sales Hacker method:

1. Extract the Risk Factor verbatim from Item 1A.
2. Reframe it as a present-tense operational question.
3. Use the management's own language — do not paraphrase into vendor vocabulary.

| Example Risk Factor (Item 1A) | Converted Discovery Question |
|---|---|
| "We face significant competition in our core market and may lose customers to lower-cost alternatives." | "Your 10-K called out competitive pricing pressure in [segment] — how are you thinking about protecting retention while holding margin this year?" |
| "Our ability to scale our sales organization is critical to our growth plans." | "Item 1A flagged scaling the sales org as a key risk — what does your current SDR ramp timeline look like against that target?" |
| "We may be unable to retain key technical personnel in a competitive labor market." | "Talent retention in engineering came up in your risk section — are you seeing that play out on the hiring side right now?" |

---

## LLM Extraction Prompt (Legloire Method)

Use this prompt with a browsing-enabled LLM or by pasting the 10-K text:

```
You are a B2B sales researcher. Read this 10-K excerpt and extract:
1. The top 3–5 strategic initiatives mentioned in Item 1 Business and Item 7 MD&A
   that are relevant to [your product category].
2. The top 3 Risk Factors from Item 1A that represent operational pain
   where [your product category] provides relief.
3. Any specific dollar amounts, headcount targets, or timelines mentioned
   in relation to these initiatives or risks.

Format each as: [Section] → [Initiative/Risk] → [Specific language quoted] → [Relevance to {product category}]

Do not summarize. Quote the filing language directly.
```

---

## Earnings Call Transcript Mining Prompts

For analyst Q&A — run after pulling the full transcript:

**Pressure identification prompt:**
```
List every topic where two or more analysts asked related questions.
For each topic: (1) quote the analyst question, (2) quote the management
response, (3) note whether management answered directly or deflected.
Deflections signal sensitive topics.
```

**Revenue segmentation prompt:**
```
Extract all revenue-by-business-unit or revenue-by-geography numbers
mentioned in prepared remarks or analyst Q&A. Format as a table:
Segment | Q[X] Revenue | YoY Change | Management Commentary.
```

---

## Sources

- Jamal Reimer, "How to Use a 10-K Report," GTMnow / Sales Hacker
- Elric Legloire, "The 10-K Report Playbook," Outbound Kitchen
- SEC Investor Bulletin: "How to Read a 10-K," sec.gov
- UserGems Buying Signals Benchmark Report (4.2M accounts, 2.28M opportunities)

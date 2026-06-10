# SEO Strategy Playbook

**Sources:** Eli Schwartz — [*Product-Led SEO*](https://www.productledseo.com/) · Rand Fishkin — [SparkToro](https://sparktoro.com/) · [Ahrefs Blog](https://ahrefs.com/blog/) · [Backlinko](https://backlinko.com/) (methodology) · [Google Search Central](https://developers.google.com/search/docs)

B2B SEO optimizes for **pipeline**, not traffic. One #1 ranking on a high-intent keyword beats fifty informational posts with no conversion path.

---

## 1. Product-Led SEO (Eli Schwartz)

**Principle:** Build content around what the product *does* for the buyer — not generic category definitions.

| Traditional SEO | Product-Led SEO |
|---|---|
| "What is email verification?" | "How to verify emails before a cold campaign" |
| Keyword volume first | Buyer job-to-be-done first |
| Blog-only | Product pages + tools + docs as SEO assets |
| Traffic KPI | Pipeline / signup KPI |

**Checklist:**
- [ ] Every Tier-1 page ties to a product capability
- [ ] Free tool or template on high-intent pages (calculator, checker, generator)
- [ ] Product screenshots with annotated workflows (E-E-A-T)
- [ ] Internal links from educational → product pages with clear CTA

---

## 2. Audience Research (Rand Fishkin / SparkToro)

Use audience intelligence before keyword tools:

| Step | Action | Tool / method |
|---|---|---|
| 1 | Where does ICP spend time online? | SparkToro audience research |
| 2 | What do they read, follow, podcast? | Influence map → guest post / podcast targets |
| 3 | What language do they use (not jargon)? | Reddit, Slack communities, sales calls |
| 4 | What competitors do they consider? | Comparison keyword set |

**Insight:** ~80% of B2B discovery is dark social (Slack, DMs, peer asks) — SEO captures the *measurable* remainder; pair with `chris-walker-mental-models.md`.

---

## 3. Keyword Architecture (Ahrefs / Backlinko methodology)

### Three-Tier Keyword Universe

| Tier | Intent | Example | Content type | Target count |
|---|---|---|---|---|
| **T1 — Buying** | Purchase | "[competitor] alternative", "best [category]" | Comparison, pricing, alternatives | 10–20 |
| **T2 — Evaluating** | Shortlist | "[category] for [industry]", "how to choose" | Buyer's guides, use cases | 30–50 |
| **T3 — Learning** | Problem-aware | "how to [job]", "[metric] benchmark" | Blog, guides, templates | 100–200 |

### Content Cluster Structure

```
Pillar (T1 keyword, 3–5K words)
├── Cluster article A (T2) → links up
├── Cluster article B (T2) → links up
├── Cluster article C (T3) → links up
└── Product page → primary CTA
```

**Ahrefs pattern:** One pillar per money keyword; 8–15 cluster posts; refresh pillar quarterly.

---

## 4. Technical SEO Checklist

| Area | Requirement |
|---|---|
| Indexability | Valuable pages indexable; thin pages no-index |
| Core Web Vitals | LCP <2.5s, INP <200ms, CLS <0.1 |
| Mobile | Responsive; 20–30% B2B search is mobile |
| Schema | Article, FAQ, HowTo, Product, Organization |
| Internal links | 3–5 contextual links per new post to existing |
| Sitemap | Auto-generated; Search Console submitted |
| Canonicals | Resolve duplicate programmatic pages |

---

## 5. Programmatic SEO (pSEO)

| Pattern | Template variables | Risk control |
|---|---|---|
| "[Category] for [Industry]" | 50 industries × 1 template | Unique intro paragraph per page (min 150 words) |
| "[Integration] + [Product]" | Partner list | Real integration screenshots + docs |
| "[City] [Service]" | Geo pages | Only if local relevance exists |

**Gate:** No programmatic page without unique value block — avoid thin-content penalties.

---

## 6. Link Building (B2B)

| Tactic | Frequency | Expected yield |
|---|---|---|
| Original research / benchmark report | 2×/year | 10–50 editorial links |
| Free tools (calculators, checkers) | 1–2 live | Passive links ongoing |
| Guest posts (industry pubs) | 1–2/month | 1–3 links each |
| Partner co-marketing pages | Per integration | Reciprocal links |
| Podcast tour | Ongoing | Show-note backlinks |

**Avoid:** PBNs, paid links, link farms.

---

## 7. Measurement — Pipeline, Not Pageviews

| Metric | Definition |
|---|---|
| Organic sessions | Top-of-funnel volume |
| Organic demo/trial signups | Mid-funnel conversion |
| Organic-sourced pipeline $ | CRM opportunity value (UTM + self-reported) |
| Keyword rankings (T1 only) | Track 20 money keywords weekly |
| Content ROI | Pipeline $ / (content cost + tools + time) |

---

## 8. AEO / AI Search Overlap

Pair with `content-seo/aeo-strategy`:
- Structured FAQ blocks on pillar pages
- Citation-worthy statistics (original data)
- Clear entity definitions (brand, product, category)
- `citation-harvesting` for LLM mention tracking

---

## Skills Map

| Task | Skill |
|---|---|
| Full SEO strategy | `seo-strategy` |
| Pillar + cluster build | `pillar-pages` |
| Programmatic pages | `pseo-strategy` |
| FAQ / schema | `faq-seo` |
| AI search / AEO | `aeo-strategy` |
| LLM citations | `citation-harvesting` |
| Content calendar + distribution | `content-marketing` |
| Syndication | `content-syndication` |

**Experts:** See `references/experts.md` → SEO & Content section

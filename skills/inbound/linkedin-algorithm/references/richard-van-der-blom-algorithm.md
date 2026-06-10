# Richard van der Blom — LinkedIn Algorithm Insights Report

Reference tables for `SKILL.md`. Source: Richard van der Blom (Just Connecting),
Algorithm Insights Report — annual public data study of LinkedIn organic
performance. 2026 edition: 7th edition, 200+ pages, built on 1.3M+ posts and
80,000+ profiles (~1,400 hours of research). Findings below are directional
benchmarks, not guarantees — LinkedIn ships changes continuously, and the
report itself is updated every cycle.

**Public channels:** 💼 [linkedin.com/in/richardvanderblom](https://www.linkedin.com/in/richardvanderblom/) · 🔗 [justconnecting.nl](https://www.justconnecting.nl/)

## The structural shift: relationship graph → interest graph

The 2026 edition's core finding. LinkedIn historically distributed content
through your network (relationship graph). It now distributes through topic
interest (interest graph):

| Old model | New model |
|---|---|
| Follower count predicts reach | Follower count no longer predicts reach |
| Network engagement drives distribution | Topic relevance + per-post merit drive distribution |
| Grow audience first, then reach | Build **topic authority** — consistent pillars, repeated keywords |
| One viral post lifts the account | ~85% of viewers didn't see your previous post |

Implication: niche creators with consistent pillars can outreach large
generalist accounts. The report's Creator Classification System rewards
creators the algorithm can categorize.

## Platform-wide reach compression (context before diagnosis)

From the 2025 edition (YoY): post views **-50%**, engagement **-25%**,
follower growth **-59%**. Benchmark personal performance against the trend —
a flat account in a compressing feed is outperforming.

## Format rankings (2026 data)

| Format | Reach multiplier | Engagement | Best for | Primary signal |
|---|---|---|---|---|
| Document / PDF carousel | ~1.39x (1.72x for top profiles) | ~6.6% (highest) | Frameworks, benchmarks, tutorials | Dwell time + saves |
| Short native video (30-90s) | ~0.86x (reach reversal vs 2024) | ~5.6% | Thought leadership, behind-the-scenes | Watch time + replays |
| Image + text | baseline | ~3.2% | Quick insights, announcements | Engagement velocity |
| Text-only | baseline-low | ~2.0% | Stories, opinions (short + sharp) | Dwell + comments |
| Newsletter / article | low feed reach | high conversion | Depth, SEO/GEO, recurring series | Subscriptions |
| Post with external link in body | reach penalty ~25-60% | low | Avoid; link in comments/profile | Penalized |

Notes:
- Engagement = (reactions + comments + shares + saves) / impressions.
- Video watch volume is growing platform-wide, but average feed reach per
  video post underperforms — use video for trust, not reach.
- LinkedIn Live: guest frequently, host rarely (infrastructure-heavy). When
  hosting a weekly show with full repurposing (clips → carousels → posts), see
  `linkedin-live-strategy` →
  `skills/inbound/linkedin-live-strategy/references/jessie-lizak-linkedin-live.md`
  (Jessie Lizak / Reveting WinsDay model).

## Post anatomy and timing (Chapter 4 — four phases)

**Writing**
- Hook carries disproportionate weight: first 2-3 lines determine dwell.
- Length: 34% of top-performing posts are under 600 characters (21% in 2024).
  Dwell time is now combined with completion/consumption rate — the feed
  rewards sharper, not longer.
- Keywords in body text replace hashtags for topical classification.

**Publishing**
- Frequency: 3-5 posts/week; >1 post/day cannibalizes reach.
- Hashtags: posts **without** hashtags outperform posts with them by 5-10%.
- Tags: tagging 5+ people is a potential spam signal; if >50% of tagged
  people don't engage, reach is penalized. Tag with intent.

**Nurturing**
- Golden hour: respond to comments within the first 60-90 minutes; comment
  quality, thread length, and reply depth outweigh reactions.
- Saves are a heavily weighted signal — design save-worthy reference posts.
- Engage on others' posts around your publishing window; the interest graph
  rewards active participants.

**Repurposing**
- Re-angle winners into other formats (text post → carousel → newsletter)
  rather than reposting verbatim.

## Company pages (Chapter 5)

- Company page reach grew ~33% while personal profile reach fell — pages are
  viable again for pillar-based content.
- Engage from the page identity (comments, replies), not just broadcasts.
- Employee advocacy: reshares with original commentary outperform bare
  reposts.
- Paid: amplify proven organic winners with thought leadership ads instead of
  promoting untested content.

## AI-assisted content (Chapter 6)

- Detectably AI-generated content is penalized in both reach and engagement
  (third-party corroboration: AuthoredUp's 3M-post 2026 study found ~30%+
  reach and ~55% engagement drops vs human-voiced posts).
- Use AI for research, outlines, and editing; keep voice human and specific.
- Each report edition closes with ~20 LinkedIn myths debunked by data —
  default to skepticism on unsourced algorithm advice.

## Diagnosis checklist (apply in order)

1. Platform compression vs personal decline (benchmark vs YoY trend)
2. External links in post bodies → move to comments/profile
3. Hashtag and tag hygiene (0-3 keywords-as-hashtags max; <5 tags)
4. Format mix vs the rankings table (add document posts)
5. Hook + length audit (completion rate, not word count)
6. Golden-hour engagement discipline
7. Posting frequency (cap at 1/day)
8. Topic consistency (can the algorithm classify you?)

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |
| Founder posting system | `skills/founder-led/founder-brand/references/adam-robinson-founder-brand.md` |
| Reach → pipeline conversion | `social-selling` |

# Funding Signal Play — Framework Notes

Reference material for the `funding-signal-play` skill. Keep `SKILL.md` concise;
use this file for extended tables, timing cheat sheets, and the signal-stacking
scoring rubric.

---

## Signal Source Comparison Table

| Source | Signal Type | Typical Lead Time vs. Press | Setup Cost | False Positive Rate |
|---|---|---|---|---|
| **SEC Form D (EDGAR)** | US private raises; legally required shortly after close | Weeks earlier than press | Low (free RSS/search) | Low — legally filed |
| **Crunchbase Alerts** | Confirmed rounds, announced raises | Same day to +1 day | Low (free tier available) | Low — curated |
| **VC / Founder LinkedIn** | Announcement posts, portfolio updates | Same day | Medium (manual monitoring or tool) | Medium — not all rounds posted |
| **X / Twitter Founders** | Self-announced raises, team updates | Same day | Medium | Medium — incomplete coverage |
| **TechCrunch / newsletter RSS** | Feature articles, series announcements | Same day to +3 days | Low | Low — editorial filter |
| **PitchBook / CB Insights** | Deep deal data, round details | +1 to +3 days | High (paid) | Very low |

**Recommended minimum setup:** EDGAR Form D RSS + Crunchbase alerts + LinkedIn
company page monitoring. This combination catches US private raises before
press and provides corroboration within 24 hours.

---

## Timing Window Cheat Sheet

Based on Amplemarket Signal-Based Selling Guide and UserGems Benchmark:

```
Day 0        Signal detected (Form D / Crunchbase / press)
│
├─ Day 0–1   Account research + signal stacking validation
│            → If stack score < 2: log, do not proceed
│            → If stack score ≥ 2: escalate to active play
│
├─ Day 1     Email Touch 1 — use-of-funds alignment (target: ≤48h from detection)
├─ Day 2     LinkedIn connection request
├─ Day 4     Email Touch 2 — stage-matched proof point
├─ Day 7     Email Touch 3 — direct ask
├─ Day 10    LinkedIn DM — value add
└─ Day 14    Breakup email

Days 2–14    PRIME OUTREACH WINDOW (Amplemarket)
Day 30       Signal relevance starts declining
Day 60       Signal effectively stale — pause play, reassess
Day 90       71% of funded companies have finalized vendor selections (UserGems)
             → Pipeline not yet created by Day 90 is unlikely to convert from this trigger
```

**48-Hour Rule (UserGems):** Vendors who contact funded companies within 48
hours of announcement see meaningfully higher conversion. This is the single
most impactful timing lever in the play.

---

## Signal-Stacking Scoring Rubric

Score each funding event before committing outreach resources. Require a minimum
score of 2 before proceeding to Phase 2 (Getcleed stacking research).

| Signal | Points | How to Verify |
|---|---|---|
| Funding announcement (confirmed round) | 1 | Crunchbase, Form D, or press |
| Round size ≥ relevant threshold for your segment | +1 | Press or Form D amount field |
| Stated use-of-funds maps to your product category | +1 | Press release, TechCrunch article |
| Hiring spike: 3+ open roles on relevant team (last 30 days) | +1 | LinkedIn Jobs, Greenhouse, Lever |
| Relevant exec hire in your buyer's function (last 60 days) | +1 | LinkedIn, press |
| Job posting explicitly names your product category or a tool you compete with | +1 | Job description text search |
| VC investor is known to mandate vendor evaluation in your category | +1 | VC portfolio patterns, network intel |

**Score interpretation:**

| Total Score | Action |
|---|---|
| 0–1 | Log for monthly monitoring; do not activate play |
| 2–3 | Proceed to Phase 2 research; standard priority |
| 4–5 | High priority; escalate to AE same day |
| 6+ | Account team pursuit; multi-thread immediately |

---

## Use-of-Funds to Outreach Angle Mapping

| Stated Use of Funds | Target Persona | Outreach Angle |
|---|---|---|
| "Expand sales team" / "Grow revenue org" | CRO, VP Sales, RevOps | SDR/AE productivity, ramp time, sequencing |
| "Invest in product development" / "Accelerate R&D" | VP Eng, CTO, CPO | Developer tooling, CI/CD, infra, security |
| "Enter new markets" / "International expansion" | CRO, VP Marketing, Head of Growth | Localization, demand gen, compliance |
| "Improve customer experience" / "Scale CS" | VP Customer Success, CCO | CS tooling, health scoring, support automation |
| "Strengthen operations" / "Operational efficiency" | COO, VP Ops, CFO | RevOps, finance automation, process tooling |
| "Hire key leadership" / "Build out team" | CHRO, Head of Talent | Recruiting tools, HRIS, onboarding |

---

## Measurement Benchmarks (from Research Sources)

| Metric | Benchmark | Source |
|---|---|---|
| Signal-triggered reply rate | 8–15% | Amplemarket Signal-Based Selling Guide |
| Cold baseline reply rate | 2–5% | Amplemarket Signal-Based Selling Guide |
| Expected lift (trigger vs. cold) | 2–4x | Amplemarket Signal-Based Selling Guide |
| Vendor selection window post-raise | ~90 days (71% of companies) | UserGems Benchmark |
| Optimal first-touch timing | ≤48 hours from announcement | UserGems Benchmark |
| Signal actionability window | 30–60 days | Amplemarket Signal-Based Selling Guide |
| Monitoring frequency (target accounts) | Monthly minimum | UserGems Benchmark |

---

## Sources

- UserGems, Buying Signals Benchmark Report (4.2M accounts, 2.28M opportunities analyzed)
- Amplemarket, Signal-Based Selling Guide
- Getcleed, Funding Signal Prospecting Guide
- SEC EDGAR, Form D filings: sec.gov/cgi-bin/browse-edgar

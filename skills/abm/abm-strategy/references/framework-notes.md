# Abm Strategy — Framework Notes

Reference index for `SKILL.md`. Apply named frameworks to justify recommendations.

## Primary Frameworks

- **ITSMA — Account-Based Marketing.** The canonical ABM methodology: tier selection (1:1, 1:few, 1:many), account intelligence, channel orchestration, and ABM-specific measurement. ITSMA defines ABM maturity stages and the shift from lead-based to account-based GTM.

- **TOPO — Account-Based Framework.** TOPO's ABM framework adds operational rigor: TAM segmentation by ICP fit, tier-based play design, sales-marketing coordination, and pipeline measurement from target accounts rather than lead volume.

- **Winning by Design — Bowtie Model.** The Bowtie extends the sales funnel into retention and expansion — critical for ABM because the economics of named accounts depend on post-sale revenue (NRR > 120%). ABM programs measure the full Bowtie, not just the pipe.

- **Lars Nilsson (Cloudera/Snowflake) — Account-Based Sales Development (ABSD).** Nilsson pioneered signal-based account selection: trigger events (funding, leadership changes, tech stack signals) as the primary ABM targeting mechanism rather than static firmographic lists.

- **6sense / Demandbase — Intent-Driven ABM.** Modern ABM platforms layer intent data (surge signals, account research activity) on top of ICP fit. The account selection model should combine static fit scores with dynamic intent signals to prioritize accounts showing active buying behavior.

- **Clay — Programmatic ABM Automation.** For 1:many ABM, Clay automates account research, personalization at scale, and CRM enrichment. Pattern: ICP filter → enrichment waterfall → dynamic personalization → sequencer handoff.

## Platform Context (2026)

The ABM tech landscape has consolidated around three layers: (1) intent/data platforms (6sense, Demandbase, ZoomInfo), (2) orchestration/engagement (Sendoso, Reachdesk, Clay), and (3) measurement (CRM dashboards, attribution). Modern ABM strategy should map the account journey across all three without over-engineering the stack.

## Deep-dive references

| File                                                      | Authority    | Use when                                       |
| --------------------------------------------------------- | ------------ | ---------------------------------------------- |
| `skills/abm/abm-strategy/references/lars-nilsson-absd.md` | Lars Nilsson | Signal-based account selection and ABSD design |

## Templates

- `templates/output-template.md` — Primary deliverable shell

## Agent routing

| Question          | Action                                    |
| ----------------- | ----------------------------------------- |
| Full process      | Follow `SKILL.md` step-by-step            |
| Build deliverable | Start from `templates/output-template.md` |
| Validate output   | Run `scripts/check-output.py`             |

Before final output, cite which framework shaped the recommendation.

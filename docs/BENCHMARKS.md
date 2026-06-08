# Public Benchmark Notes

This document tracks adjacent public GTM, marketing, and sales agent-skill repositories so this project stays honest about where it is strong and where it needs to improve.

Last benchmark refresh: 2026-06-07.

## Adjacent Repositories

| Repository | Public positioning | Strength | Gap we should beat |
|---|---|---|---|
| `pfoy/growth-skills` | 197 Claude Code skills for B2B sales, outbound, inbound, ABM, and growth engineering. | Comparable breadth and clear plugin install story. | Keep stronger public governance, integrity lock, category coverage beyond growth/outbound, and source hygiene. |
| `coreyhaines31/marketingskills` | Marketing skills for Claude Code and AI agents across CRO, copywriting, SEO, analytics, and growth engineering. | Strong marketing focus, shared product-marketing context, high visibility. | Maintain deeper sales/RevOps/outbound/founder-led/CS coverage and stricter marketplace/disclosure standards. |
| `manojbajaj95/claude-gtm-plugin` | 54 GTM skills with bootstrap/project-context workflow. | Excellent workspace bootstrap and durable brand/context pattern. | Add optional context bootstrap without sacrificing the 218-skill breadth or source-standard QA. |
| `GTM-Strategist/gtm-strategist-skills` | 12 skills around Maja Voje's GTM Strategist methodology. | Clear end-to-end GTM phase model and user-friendly onboarding. | Preserve methodology depth while covering the operational edge cases that phase-based packs skip. |
| `Othmane-Khadri/gtm-engineer-playbook` | 10 installable Claude Code skills for GTM engineers. | Strong artifact outputs and GTM-engineer framing. | Keep better category breadth, install tooling, and QA gates. |
| `chadboyda/agent-gtm-skills` forks | 18 dense AI-era GTM skills. | Opinionated, current, dense per-skill content. | Match density in key skills while keeping SKILL.md progressive-disclosure under 500 lines. |
| `elliottrjacobs/skills-gtm` | 9 skills plus research-agent pattern. | Strong research-agent decomposition. | Add research-agent patterns where useful, but keep skills portable without requiring subagents. |
| `rvanshur/vertical-gtm-skills` | 14 sales-methodology skills for vertical SaaS. | Strong lifecycle mapping and client-profile pattern. | Add profile/context templates for verticalization while keeping generic B2B SaaS utility. |
| `Stallin-Sanamandra/b2b-saas-marketing-skills` | B2B SaaS marketing skills with enterprise/GRC flavor. | Compliance-safe messaging and marketing ops specificity. | Keep compliance and governance coverage strong across all categories, not just marketing. |

## Where This Repository Is Strong

- 218 marketplace-discoverable skills across 26 categories.
- Covers sales, marketing, outbound, prospecting, enrichment, PLG, analytics, automation, customer success, RevOps, founder-led GTM, events, partnerships, design, AI agents, and tooling.
- Uses Anthropic-style progressive disclosure: `SKILL.md` plus `references/`, `templates/`, `scripts/`, and `assets/`.
- Includes `skills.lock` for SHA256 integrity.
- Includes generated `README.md`, `AGENTS.md`, `CLAUDE.md`, taxonomy, plugin metadata, validation, installer dry-runs, governance docs, and release process.
- Avoids hidden telemetry and network behavior in static skills.

## Weaknesses Found and Hardened

1. **Generic descriptions.** Several generated descriptions said "playbook for GTM agents" instead of declaring an artifact and trigger. Fixed with specific, operator-grade descriptions.
2. **Weak source labels.** Internal or vague labels such as "Operator GTM Playbook" were replaced with named public sources and methods.
3. **Framework-section cruft.** Some generated framework sections included checklist bullets and output placeholders. Fixed by rebuilding sections from frontmatter frameworks only.
4. **Stale catalog count.** `using-gtm-skills` and generated docs were updated to the current 218 skills / 26 categories.
5. **Progressive-disclosure drift.** Oversized non-design skills were split or trimmed. Dense design reference skills may intentionally exceed 500 lines when they carry reusable source guidance plus required execution artifacts.
6. **Missing public benchmark doc.** Added this file so future maintainers know the competitive bar.
7. **Missing source standard.** Added `docs/SOURCE_STANDARDS.md` to define what qualifies as authority coverage.

## Strategic Bar Going Forward

This repo should not try to win by raw count alone. The bar is:

1. Breadth close to the largest packs.
2. Per-skill density close to the best small packs.
3. Public source hygiene better than all prompt-pack style repos.
4. Install and validation quality better than one-off skill dumps.
5. No private/internal details in public artifacts.
6. Every skill should produce a concrete artifact, not just advice.

## Next Strong Additions

- Context bootstrap skill that creates reusable company/product/ICP/voice files.
- Verticalization templates for SaaS, agency, services, devtools, cybersecurity, healthcare, fintech, and local services.
- Research-agent optional patterns for ICP, competitor, pricing, and meeting-prep tasks.
- More source-backed references for paid media, lifecycle, CS, and partnerships.
- Scripted source audit that scores every skill against `docs/SOURCE_STANDARDS.md`.

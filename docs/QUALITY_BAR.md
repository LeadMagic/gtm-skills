# Quality Bar Notes

This document defines the public quality bar for this repository so maintainers know where it is strong and where it needs to improve.

Last refresh: 2026-06-09.

## Where This Repository Is Strong

- Full catalog of marketplace-discoverable skills across 20+ categories (current counts live in the generated `README.md` badges).
- Covers sales, marketing, outbound, prospecting, enrichment, PLG, analytics, automation, customer success, RevOps, founder-led GTM, events, partnerships, design, and tooling.
- Uses Anthropic-style progressive disclosure: `SKILL.md` plus `references/`, `templates/`, `scripts/`, and `assets/`.
- Includes `skills.lock` for SHA256 integrity.
- Includes generated `README.md`, `AGENTS.md`, `CLAUDE.md`, taxonomy, plugin metadata, validation, installer dry-runs, governance docs, and release process.
- Avoids hidden telemetry and network behavior in static skills.

## Weaknesses Found and Hardened

1. **Generic descriptions.** Several generated descriptions said "playbook for GTM agents" instead of declaring an artifact and trigger. Fixed with specific, operator-grade descriptions.
2. **Weak source labels.** Internal or vague labels such as "Operator GTM Playbook" were replaced with named public sources and methods.
3. **Framework-section cruft.** Some generated framework sections included checklist bullets and output placeholders. Fixed by rebuilding sections from frontmatter frameworks only.
4. **Stale catalog count.** `using-gtm-skills` and generated docs were aligned to the generated catalog; docs now avoid hardcoding counts where the generators are the source of truth.
5. **Progressive-disclosure drift.** Oversized non-design skills were split or trimmed. Dense design reference skills may intentionally exceed 500 lines when they carry reusable source guidance plus required execution artifacts.
6. **Missing quality bar doc.** Added this file so future maintainers know the standard.
7. **Missing source standard.** Added `docs/SOURCE_STANDARDS.md` to define what qualifies as authority coverage.

## Strategic Bar Going Forward

This repo should not try to win by raw count alone. The bar is:

1. Broad category coverage across the full GTM lifecycle.
2. High per-skill density and actionability.
3. Strict public source hygiene with named authorities and primary docs.
4. First-class install, validation, and integrity tooling.
5. No private/internal details in public artifacts.
6. Every skill should produce a concrete artifact, not just advice.

## Next Strong Additions

- Context bootstrap skill that creates reusable company/product/ICP/voice files.
- Verticalization templates for SaaS, agency, services, devtools, cybersecurity, healthcare, fintech, and local services.
- Research-agent optional patterns for ICP, competitor, pricing, and meeting-prep tasks.
- More source-backed references for paid media, lifecycle, CS, and partnerships.
- Scripted source audit that scores every skill against `docs/SOURCE_STANDARDS.md`.

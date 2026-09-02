# Quality Bar Notes

This document defines the public quality bar for this repository so maintainers know where it is strong and where it needs to improve.

Last refresh: 2026-09-02.

## Where This Repository Is Strong

- Full catalog of marketplace-discoverable skills across 20+ categories (current counts live in the generated `README.md` badges).
- Covers sales, marketing, outbound, prospecting, enrichment, PLG, analytics, automation, customer success, RevOps, founder-led GTM, events, partnerships, design, and tooling.
- Uses Agent Skills progressive disclosure: `SKILL.md` plus `references/`, `templates/`, `scripts/`, and `assets/`.
- Includes `skills.lock` with SHA-256 coverage for every packaged skill file.
- Includes generated `README.md`, `AGENTS.md`, `CLAUDE.md`, taxonomy, plugin metadata, validation, installer dry-runs, governance docs, and release process.
- Avoids hidden telemetry and network behavior in static skills.

## Weaknesses Found and Hardened

1. **Generic descriptions.** Several generated descriptions said "playbook for GTM agents" instead of declaring an artifact and trigger. Fixed with specific, operator-grade descriptions.
2. **Weak source labels.** Internal or vague labels such as "Operator GTM Playbook" were replaced with named public sources and methods.
3. **Framework-section cruft.** Some generated framework sections included checklist bullets and output placeholders. Fixed by rebuilding sections from frontmatter frameworks only.
4. **Stale catalog count.** `using-gtm-skills` and generated docs were aligned to the generated catalog; docs now avoid hardcoding counts where the generators are the source of truth.
5. **Progressive-disclosure drift.** Every `SKILL.md` is capped at 500 physical lines without exceptions; deeper guidance belongs in skill-local references.
6. **Missing quality bar doc.** Added this file so future maintainers know the standard.
7. **Missing source standard.** Added `docs/SOURCE_STANDARDS.md` to define what qualifies as authority coverage.
8. **Weak artifact coverage.** CI now requires every skill to ship `framework-notes.md`, `output-template.md`, and `check-output.py`, with all three listed in `## Execution Artifacts`.
9. **Generic authority filler.** `validate-skills.js` rejects decoration placeholder text; `npm run fix:authority` repairs SKILL.md bodies.
10. **Installation drift.** The installer now uses current `gh skill` and Claude plugin commands, installs at real discovery roots, and exercises every target in dry-run CI.
11. **Weak artifact validators.** CI executes every `check-output.py`; a checker must reject missing input and its own unfilled template.
12. **Hand-maintained catalog drift.** README and public inventory values are generated from the folders on disk.
13. **Non-portable shared references.** Direct repository-level dependencies are generated into their owning skills and checked for drift, so one-skill installs retain their required resources.

## CI Enforcement (agentskills.io + GTM bar)

`npm run verify` runs:

1. `validate-skills.js` — Agent Skills name/description/500-line rules + GTM authority/process/artifact checks
2. `audit-artifacts.py` — exact ownership, required-file, substance, portability, and executable-script checks
3. `audit-references.py` — resolvable reference paths
4. `materialize-shared-references.py --check` — portable, current skill-local reference dependencies
5. `generate-skills-lock.py --check` — complete path, byte-size, kind, and SHA-256 coverage
6. Checker execution — every checker rejects usage errors and unfilled templates
7. Installer dry-runs — every supported target plus the curated Claude installer
8. `public-repo-audit.py` — community files and catalog drift
9. `check-generated.sh` — regenerated README/AGENTS/CLAUDE/taxonomy/lock

## Strategic Bar Going Forward

This repo should not try to win by raw count alone. The bar is:

1. Broad category coverage across the full GTM lifecycle.
2. High per-skill density and actionability.
3. Strict public source hygiene with named authorities and primary docs.
4. First-class install, validation, and integrity tooling.
5. No private/internal details in public artifacts.
6. Every skill should produce a concrete artifact, not just advice.

## Next Strong Additions

- Verticalization templates for SaaS, agency, services, devtools, cybersecurity, healthcare, fintech, and local services.
- Research-agent optional patterns for ICP, competitor, pricing, and meeting-prep tasks.
- More source-backed references for paid media, lifecycle, CS, and partnerships.
- Scripted source audit that scores every skill against `docs/SOURCE_STANDARDS.md`.

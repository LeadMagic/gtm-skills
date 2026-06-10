# Changelog

All notable changes to GTM Skills are documented here.

## v0.26.0 — Toolkit Flattening, Reference Repair, and Validation/CI Hardening

- Added the `linkedin-algorithm` skill (Richard van der Blom's LinkedIn algorithm research) and an Adam Robinson founder-brand playbook under `founder-led/founder-brand`, with cross-links from social-selling and social-media-strategy.
- Flattened the grouped `tools/clay/*` and `tools/crm/*` toolkit skills to the documented `skills/<category>/<skill>/SKILL.md` depth (`clay-toolkit`, `clay-loops-toolkit`, `crm-toolkit`) and rewrote every repo path that referenced the old grouped layout.
- Repaired 14 broken cross-skill references and fixed relative-link depth bugs in skill subdirectory references/templates.
- Hardened `scripts/validate-skills.js` to enforce flat skill depth, require `name` to equal the directory, and verify that every reference target resolves relative to the skill dir or the repo root.
- Added `scripts/audit-references.py` to `npm run check` and CI, plus a generated-file drift check, so catalog skew fails CI.
- Fixed Biome lint issues in the generator scripts (node: imports, template literals, statement extraction) with byte-identical generated output.
- Synced documentation, counts, and the reference-path convention across docs.

## v0.25.0 — Design Expansion, Source Standards, and Benchmark Hardening

- Added 29 public-safe design skills from the local design stack: typography, color systems, frontend design, shadcn/ui, data visualization, charts, mobile, dashboards, animation, social publishing, diagrams, critique, and reference-design-contract workflows.
- Expanded the design category and regenerated README, AGENTS, CLAUDE, taxonomy, plugin metadata, and lockfile for 202 marketplace-discoverable skills across 25 categories.
- Removed the `ai-agents` category; agent implementation guidance lives under `automation/` and `tools/` skills.
- Added public source/authority standards and benchmark notes for adjacent GTM/marketing skill repositories.
- Replaced generic skill descriptions with artifact-specific trigger descriptions across foundation, analytics, founder-led, and prospecting skills.
- Rebuilt corrupted framework sections so source lists no longer include checklist/output placeholders.
- Replaced weak/internal-sounding source labels with named public authorities and platform guidance.
- Fixed stale catalog count references and kept non-design skills aligned to progressive-disclosure expectations.

## v0.24.0 — Public Repository Polish

- Added high-end public repository infrastructure: SECURITY, CONTRIBUTING, governance, code of conduct, citation metadata, editor config, Dependabot, and docs.
- Upgraded generated README/AGENTS/CLAUDE surfaces for public adoption, integrity verification, and contribution pathways.
- Added architecture, authoring, integrity, and release-process documentation.
- Updated GitHub repository metadata and topics for discoverability.
- Preserved 189 marketplace-discoverable skills with CI validation and publish dry-run.

## v0.23.0 — Marketplace Discovery Cleanup and Docs Sync

- Flattened tool skills so all 189 skills are discoverable by agentskills.io-compatible tooling.
- Regenerated README, AGENTS, CLAUDE, taxonomy, plugin metadata, and lockfile from disk.
- Added lock generator and CI drift checks.
- Split oversized skills into references for progressive disclosure.
- Verified `npm run check`, `gh skill publish --dry-run`, and release publish.

## v0.22.0 — Artifacts, Installer, and Framework Hardening

- Added installer and artifact hardening for supported agent systems.
- Strengthened tool skill support files.
- Improved framework and validator coverage.

## v0.21.0 — Strict Skill Quality Gate

- Added strict validation for skill metadata, descriptions, line counts, and quality gates.
- Expanded deep content coverage and generated artifacts.

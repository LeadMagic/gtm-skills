# Changelog

All notable changes to GTM Skills are documented here.

## v0.27.1 — Quality Bar Docs Cleanup

- Replaced the competitive benchmark notes with neutral quality bar notes: removed the adjacent-repo comparison table and competitive framing from the doc, generators, and generated catalogs.
- Renamed `docs/BENCHMARKS.md` to `docs/QUALITY_BAR.md` and repointed README, AGENTS, CLAUDE, and generator references.
- De-hardcoded the skill/category counts in the quality bar doc; generated catalogs remain the source of truth.

## v0.27.0 — Sales Navigator Prospecting (Morgan J. Ingram / AMP Social)

- Flattened `sequencing-tools/` into `tools/` — six platform sequencer skills (`instantly-sequences`, `smartlead-workflows`, `lemlist-setup`, `salesloft-cadences`, `outreach-sequences`, `hubspot-sequences`) now sit beside `sequencing-toolkit` under one category (24 categories total, 205 skills unchanged).
- Updated automation playbook index, master router, and cross-links to treat sequencers as tool skills, not a separate category.
- Added `sales-navigator-prospecting` skill (inbound) — Morgan Ingram's filter-specific Sales Nav playbook, executive insight+question engagement, saved-search alerts, and 15-minute daily workflow.
- Cross-linked from `social-selling`, `list-building`, `references/experts.md`, and README Start Here / LinkedIn stack.
- Synced stale skill-count references in `using-gtm-skills`, `CONTRIBUTING.md`, and `docs/INTEGRITY.md`.
- **205 skills / 24 categories** — catalog, lockfile, taxonomy regenerated.

## v0.26.1 — LinkedIn Live Strategy (Jessie Lizak / Reveting)

- Added `linkedin-live-strategy` skill (inbound) with Jessie Lizak's Reveting playbook — weekly livestream content engine, WinsDay model, repurposing flywheel, and relationship-first Live execution.
- Cross-linked from `linkedin-algorithm`, `social-selling`, `founder-brand`, `social-media-strategy`, and `references/experts.md`.
- **204 skills / 25 categories** — catalog, lockfile, and taxonomy regenerated.

## v0.26.0 — Toolkit Flattening, Reference Repair, and Validation/CI Hardening

- **203 skills / 25 categories** — catalog, lockfile, taxonomy, and public metadata synced to disk.
- Added the `linkedin-algorithm` skill (Richard van der Blom's LinkedIn algorithm research) and an Adam Robinson founder-brand playbook under `founder-led/founder-brand`, with cross-links from social-selling and social-media-strategy.
- Added Lars Nilsson ABSD, Tito Bohrt SDR science, Leslie Venetz buyer-first outbound, `developer-gtm`, and Plain BYOAI headless-support stack documentation.
- Flattened the grouped `tools/clay/*` and `tools/crm/*` toolkit skills to the documented `skills/<category>/<skill>/SKILL.md` depth (`clay-toolkit`, `clay-loops-toolkit`, `crm-toolkit`) and rewrote every repo path that referenced the old grouped layout.
- Repaired broken cross-skill references across SKILL.md and artifact files; extended `audit-references.py` to scan `references/` and `templates/`.
- Hardened `scripts/validate-skills.js` to enforce flat skill depth, require `name` to equal the directory, and verify resolvable reference targets.
- Added `scripts/generated-artifacts.txt`, `regenerate.yml` (auto-commit catalogs on `main`), and `npm run verify` as the full quality gate.
- Auto-generate `references/skill-index-master.md`; fixed Authority Catalog aggregation in `generate-indexes.js`.
- README public links, agent-skills directory listing table, and GitHub repository metadata updated for discoverability.

## v0.25.0 — Design Expansion, Source Standards, and Benchmark Hardening

- Added 29 public-safe design skills from the local design stack: typography, color systems, frontend design, shadcn/ui, data visualization, charts, mobile, dashboards, animation, social publishing, diagrams, critique, and reference-design-contract workflows.
- Expanded the design category and regenerated README, AGENTS, CLAUDE, taxonomy, plugin metadata, and lockfile for 202 marketplace-discoverable skills across 25 categories.
- Removed the `ai-agents` category; agent implementation guidance lives under `automation/` and `tools/` skills.
- Added public source/authority standards and quality bar notes.
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

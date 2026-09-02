# gtm-skills — Agent Skills Index

211 production GTM skills for AI agents. This repository follows the Agent Skills open specification: portable skill folders with SKILL.md plus optional scripts/, references/, templates/, and assets/.

## Install

Claude Code marketplace style:

```text
/plugin marketplace add LeadMagic/gtm-skills
/plugin install gtm-skills@gtm-skills
```

Portable Agent Skills CLI:

```bash
gh skill install LeadMagic/gtm-skills --all --agent codex --scope user
gh skill install LeadMagic/gtm-skills foundation/pricing-strategy --agent github-copilot --scope project
```

Local installer:

```bash
./install.sh --target codex --scope project
./install.sh --target claude --scope user
./install.sh --target all --dry-run
```

## Repository Contract

- Marketplace-visible skills live at `skills/<category>/<skill>/SKILL.md`.
- Support artifacts live inside the skill folder.
- Generated catalog files come from disk, not hand edits.
- `skills.lock` verifies SHA256 integrity.
- CI must pass before release.

## Categories

- **abm** — 7 skills
- **analytics** — 13 skills
- **automation** — 12 skills
- **content-seo** — 7 skills
- **creative** — 12 skills
- **customer-success** — 7 skills
- **demand-gen** — 4 skills
- **design** — 7 skills
- **events** — 3 skills
- **foundation** — 9 skills
- **founder-led** — 41 skills
- **growth** — 5 skills
- **gtm-ops** — 5 skills
- **inbound** — 8 skills
- **leadmagic** — 6 skills
- **lifecycle** — 5 skills
- **management-leadership** — 5 skills
- **outbound** — 10 skills
- **partnerships** — 3 skills
- **product-led-growth** — 3 skills
- **product-marketing** — 2 skills
- **prospecting** — 8 skills
- **sales-plays** — 5 skills
- **sales-revops** — 9 skills
- **tools** — 15 skills

## Quality Standard

Every skill must be tactical, artifact-first, source-backed, marketplace-discoverable, and clean for a public repository. See docs/SKILL_AUTHORING.md and docs/SOURCE_STANDARDS.md. The public quality bar is tracked in docs/QUALITY_BAR.md.

# gtm-skills — Agent Skills Index

203 production GTM skills for AI agents. This repo follows the Anthropic/agentskills pattern: portable skill folders with SKILL.md plus optional scripts/, references/, templates/, and assets/.

## Install

Claude Code marketplace style:

```text
/plugin marketplace add LeadMagic/gtm-skills
/plugin install gtm-skills@gtm-skills
```

agentskills CLI style:

```bash
gh skill install LeadMagic/gtm-skills
gh skill install LeadMagic/gtm-skills pricing-strategy
gh skill install LeadMagic/gtm-skills --category outbound
```

Local installer:

```bash
./install.sh
./install.sh --target hermes
./install.sh --target jesse --project /path/to/project
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
- **content-seo** — 6 skills
- **creative** — 12 skills
- **customer-success** — 7 skills
- **demand-gen** — 4 skills
- **design** — 7 skills
- **events** — 3 skills
- **foundation** — 8 skills
- **founder-led** — 41 skills
- **growth** — 5 skills
- **gtm-ops** — 5 skills
- **inbound** — 6 skills
- **leadmagic** — 6 skills
- **lifecycle** — 5 skills
- **management-leadership** — 5 skills
- **outbound** — 9 skills
- **partnerships** — 3 skills
- **product-led-growth** — 3 skills
- **prospecting** — 8 skills
- **sales-plays** — 5 skills
- **sales-revops** — 8 skills
- **sequencing-tools** — 6 skills
- **tools** — 9 skills

## Quality Standard

Every skill must be tactical, artifact-first, source-backed, marketplace-discoverable, and clean for a public repository. See docs/SKILL_AUTHORING.md and docs/SOURCE_STANDARDS.md. Benchmark positioning and known adjacent repos are tracked in docs/BENCHMARKS.md.

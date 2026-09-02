---
name: using-gtm-skills
description: >-
  Route a go-to-market request to the right GTM Skills, install or verify the
  catalog, and compose multi-skill workflows without loading the entire library.
  Use when first installing gtm-skills, discovering which skill fits a task,
  checking available categories, or planning a workflow that spans multiple
  sales, marketing, RevOps, SEO, customer-success, or automation skills.
license: MIT
compatibility: Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, OpenCode, Goose, Hermes, Jesse, Windsurf, Zed
metadata:
  version: "1.1.0"
  author: LeadMagic
  category: foundation
  tags: [gtm-skills, installation, discovery, taxonomy, getting-started, router]
  related_skills: [gtm-context-bootstrap, gtm-context, gtm-system-architecture, pipeline-management, sales-enablement, skills-lock]
  frameworks:
    - "Agent Skills — progressive disclosure and portable skill folders"
    - "LeadMagic/gtm-skills — generated catalog and workflow routing"
    - "Winning by Design — SPICED, Bowtie, and GTM operating model"
    - "April Dunford — positioning before channel and messaging execution"
---

# Using GTM Skills

## Overview

This is the lightweight router for the 211-skill, 25-category catalog. It selects the smallest useful set of skills, identifies missing inputs, and keeps installation and integrity checks separate from the GTM work itself. Load the complete usage guide only when detailed expert maps or multi-skill patterns are needed.

## When to Use

- The user asks which GTM skill or category matches a task.
- A new repository needs project-scoped skills or an existing install needs verification.
- A request spans multiple stages, such as research, enrichment, outreach, qualification, and measurement.
- The team needs a repeatable entrypoint instead of loading unrelated skills.
- The user asks for the catalog size, installation methods, expert maps, or workflow patterns.

## Authoritative Foundations

- **Agent Skills progressive disclosure.** Discover from frontmatter, load this entrypoint on activation, and open references only when required.
- **Artifact-first routing.** Choose skills by the deliverable and decision they produce, not by keyword overlap alone.
- **Evidence before execution.** Establish GTM context and source quality before generating downstream campaigns.
- **Narrow composition.** Start with one primary skill and add dependencies only when their outputs feed the next step.

## Workflow

### 1. Establish the request boundary

Capture the requested outcome, audience, channel, market, deadline, available evidence, and final artifact. Separate strategy, implementation, and live execution so the user can authorize them independently.

### 2. Route by deliverable

| User outcome | Start with | Add when needed |
|---|---|---|
| Build shared company context | `gtm-context-bootstrap` | `gtm-context`, `competitive-intel` |
| Define ICP and positioning | `icp-targeting-tiers` | `icp-scoring`, `positioning-messaging` |
| Launch cold outbound | `cold-email-strategy` | `email-deliverability`, `domain-infrastructure`, `cold-email-copywriting` |
| Find or enrich prospects | `list-building` | `lead-finding`, `lead-enrichment`, `contact-verification` |
| Design sales process | `pipeline-management` | `meeting-prep`, `deal-desk`, `sales-coaching` |
| Audit organic search | `technical-seo-audit` | `seo-strategy`, `pillar-pages`, `pseo-strategy` |
| Build analytics | `tracking-plan` | `gtm-metrics`, `attribution`, `proactive-alerts` |
| Choose or automate tools | `tool-selection-stack` | the relevant tool or automation skill |
| Improve onboarding or retention | `customer-onboarding` | `cs-playbooks`, `churn-prevention`, `expansion-selling` |
| Plan founder-led growth | `solo-founder-gtm` | `founder-sales`, `content-led-growth`, `financial-modeling` |

For exhaustive category listings, use `references/skill-index-master.md`. For named practitioners, use `references/experts.md`. For proven compositions, open `references/complete-usage-guide.md` and only the relevant section.

### 3. Check prerequisites

If reliable product, ICP, proof, positioning, or constraint inputs are missing, run `gtm-context-bootstrap` first. Do not fill unknowns with invented facts. Mark assumptions and open questions explicitly.

### 4. Compose the minimum workflow

Choose one owner skill for the final artifact. Load other skills only when they provide a concrete upstream input or an independent QA gate. A typical outbound chain is:

`gtm-context-bootstrap` → `icp-scoring` → `lead-enrichment` → `cold-email-strategy` → `email-deliverability` → `campaign-analytics`

### 5. Produce and validate

Follow each selected skill's output template and run its checker. Resolve contradictions between skills in favor of verified user context, current platform documentation, and the narrower domain skill.

## Installation and Verification

Preview one skill before installing it:

```bash
gh skill preview LeadMagic/gtm-skills foundation/gtm-context-bootstrap
gh skill install LeadMagic/gtm-skills foundation/gtm-context-bootstrap \
  --agent codex --scope project
```

For the whole reviewed catalog:

```bash
gh skill install LeadMagic/gtm-skills --all --agent codex --scope user
gh skill list
```

Use project scope by default and user scope only for a source intentionally trusted across projects. Pin a published release or commit for reproducibility. The local audited installer is:

```bash
./install.sh --target codex --scope project
./install.sh --target all --dry-run
```

See `docs/INSTALL.md` for all supported agent values, Claude plugin commands, local discovery paths, updates, and maintainer verification.

## Output Format

Return a compact routing brief containing:

1. The requested outcome and final artifact.
2. The primary skill and why it owns the result.
3. Any prerequisite or QA skills, in execution order.
4. Inputs available, missing, assumed, or blocked.
5. Installation or integrity actions only if relevant.
6. A definition of done tied to the selected artifacts and checkers.

Use `templates/output-template.md` when a saved routing plan is requested.

## Quality Check

- Is there exactly one primary owner skill?
- Does every additional skill contribute a concrete input or QA gate?
- Are unknown business facts labeled instead of invented?
- Are project scope and reviewed sources preferred for installation?
- Does the workflow end in a named artifact and validation step?
- Were large indexes and the complete guide loaded only when needed?

## Common Pitfalls

1. **Loading the entire catalog** — Start with one primary skill and the smallest dependency chain.
2. **Routing by a shared keyword** — Match the requested decision and artifact, not just topical vocabulary.
3. **Skipping GTM context** — Bootstrap evidence before producing contradictory messaging or targeting.
4. **Installing globally by default** — Prefer project scope; skills can include executable scripts.
5. **Treating installation as verification** — Confirm discovery, load the named skill, inspect artifacts, and run its checker.
6. **Using stale counts or commands** — Read generated catalogs and `docs/INSTALL.md`; do not hand-maintain totals.

## Execution Artifacts

- `references/complete-usage-guide.md` — Detailed expert maps, workflow patterns, category routing, and advanced usage
- `references/framework-notes.md` — Named frameworks and routing principles
- `templates/output-template.md` — Deliverable shell for a skill-routing brief
- `scripts/check-output.py` — Lightweight deliverable validator
- `references/skill-index-master.md` — Generated full catalog map
- `references/experts.md` — Named expert catalog
- `references/pitfalls-index.md` — Generated cross-skill pitfalls catalog

## Related Skills

- `gtm-context-bootstrap` — Establish reusable evidence before downstream work
- `gtm-context` — Maintain and apply an existing company context
- `skills-lock` — Verify catalog integrity
- `gtm-system-architecture` — Design the broader GTM system

---
name: skills-lock
description: >-
  Generate and verify a deterministic SHA-256 inventory for every packaged file in an Agent Skills repository. Use when creating skills.lock, checking repository integrity, reviewing artifact coverage, detecting uncommitted generated drift, or designing CI gates for a skill catalog.
license: MIT
compatibility: Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, OpenCode, Goose, Hermes, Jesse, Windsurf, Zed
metadata:
  version: "2.0.0"
  author: LeadMagic
  category: automation
  tags: [skills-lock, integrity, sha256, artifacts, ci]
  related_skills: [agent-skills-repo-authoring, hermes-agent-skill-authoring]
  frameworks:
    - "Agent Skills specification — progressive disclosure and portable skill packaging"
    - "NIST FIPS 180-4 — SHA-256 secure hash standard"
    - "Reproducible builds — deterministic manifests and drift detection"
---

# Skills Lock

## Overview

Create a deterministic manifest of the skill entrypoints and every packaged support file under `skills/`. The manifest proves byte-level consistency; it does not certify that content is correct, safe, or trustworthy. Review sources and executable scripts separately.

This repository's schema records both a compatibility-oriented `skills` index and a complete `artifacts` index. It does not invent dependency, version, or modification-time fields that cannot be derived reliably from the package.

## When to Use

- A skill repository needs a reviewable inventory of everything it ships.
- CI must reject a stale lock after any skill, reference, template, script, or asset changes.
- An installer or reviewer needs to verify a checkout before loading instructions.
- Catalog counts disagree and need one filesystem-derived source of truth.
- The user asks to generate, audit, or explain `skills.lock`.

## Authoritative Foundations

- **Agent Skills specification**: keep each skill self-contained and load references, templates, scripts, and assets progressively from the skill directory.
- **NIST FIPS 180-4**: use SHA-256 as a deterministic digest for the exact bytes in each packaged file.
- **Reproducible-build practice**: sort paths, exclude volatile metadata from comparisons, and make the same input tree produce the same logical manifest.

## Prerequisites

- Identify the repository root and canonical `skills/` directory.
- Define discoverable skill paths, normally `skills/<category>/<skill>/SKILL.md`.
- Define explicit exclusions for platform junk and generated caches.
- Confirm whether the task permits writing the lock or only auditing it.

## Step-by-Step Process

### 1. Discover the package from disk

Enumerate skill entrypoints and all regular files beneath `skills/`. Do not derive counts from README prose, a release description, or a manually maintained catalog.

### 2. Validate ownership and portability

Ensure every packaged file belongs to one discoverable skill. Reject empty files, cache files, merge residue, unportable symlinks, misplaced artifacts, and non-executable checker scripts.

### 3. Build deterministic records

For every artifact, record its repository-relative path, SHA-256 digest, byte size, and kind. For every entrypoint, also record the stable `category/skill` key and path components.

### 4. Separate volatile metadata

An informational `generated_at` value may be present, but exclude it from logical equality checks. Preserve it on no-op regeneration so generated-file checks remain stable.

### 5. Verify exact coverage

Compare the manifest path set with the current package path set in both directions. Verify totals, per-kind counts, byte sizes, and hashes. A missing or extra record is a failure even when all recorded hashes match.

### 6. Wire the check into CI

Run artifact hygiene before lock verification, regenerate in a temporary comparison flow, and fail when committed generated files differ. Keep generation and verification as separate commands.

### 7. Report what integrity means

State the exact skill and artifact counts, the algorithm, and the exclusions. Clarify that integrity detects drift or tampering relative to the lock; it is not provenance, code-signing, malware scanning, or content review.

## Output Format

Produce an integrity report containing:

1. Repository and scope.
2. Exact skill and packaged-file counts.
3. Per-kind artifact counts.
4. Schema and hashing algorithm.
5. Generation and verification commands.
6. CI enforcement status.
7. Failures, exclusions, and residual risks.
8. Recommended remediation steps.

For this repository, use:

```bash
python3 scripts/audit-artifacts.py
python3 scripts/generate-skills-lock.py
python3 scripts/generate-skills-lock.py --check
```

## Quality Check

- [ ] Counts come from the filesystem and not from copied documentation.
- [ ] Every packaged file has one path, hash, size, and kind record.
- [ ] The manifest has no missing or extra paths.
- [ ] Paths are repository-relative and sorted deterministically.
- [ ] A no-op generation leaves the logical manifest unchanged.
- [ ] CI verifies the lock after artifact validation.
- [ ] The report distinguishes integrity from trust and provenance.

## Common Pitfalls

| Pitfall | Why it fails | Fix |
|---|---|---|
| Hashing only `SKILL.md` | References, templates, scripts, and assets can drift undetected | Inventory every packaged file |
| Recording file modification time | Checkout and archive tools can change it without changing content | Record stable path, size, and digest only |
| Comparing only recorded entries | Newly added files can be absent from the lock | Compare path sets in both directions |
| Treating SHA-256 as a trust signal | A malicious change can be re-locked | Require review, trusted distribution, and CI controls |
| Rewriting timestamps on no-op builds | Causes permanent generated-file churn | Ignore or preserve informational timestamps |

## Execution Artifacts

- `references/framework-notes.md` — Integrity scope, schema, and security boundaries
- `templates/output-template.md` — Repository integrity report template
- `scripts/check-output.py` — Deliverable completeness checker

## Related Skills

- `agent-skills-repo-authoring` for repository layout and distribution design.
- `hermes-agent-skill-authoring` for runtime-specific skill packaging.

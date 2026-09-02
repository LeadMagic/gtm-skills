# Integrity Verification

GTM Skills includes `skills.lock`, a deterministic SHA-256 manifest for every packaged file beneath `skills/`.

## Exact Scope

The lock is generated from the filesystem and records:

- Every marketplace-discoverable `SKILL.md`.
- Every packaged reference, template, script, and asset.
- Repository-relative path, SHA-256 digest, byte size, and artifact kind.
- Exact skill count, total packaged-file count, and per-kind counts.

The informational `generated_at` timestamp is ignored for equality and preserved after a no-op generation. File modification times and inferred dependencies are intentionally excluded because they are not stable package facts.

## Generate

```bash
python3 scripts/generate-skills-lock.py
```

Or regenerate every derived catalog:

```bash
npm run build
```

## Verify

```bash
python3 scripts/audit-artifacts.py
python3 scripts/generate-skills-lock.py --check
```

Or run the full repository suite:

```bash
npm run verify
gh skill publish --dry-run
```

Successful verification reports the current exact skill and packaged-file totals. Counts are generated rather than copied into this guide, so the command output and `skills.lock` remain authoritative as the catalog changes.

## What Verification Proves

A passing lock check proves that the packaged files match the committed manifest byte for byte and that no packaged path is missing or extra. It does not prove authorship, factual accuracy, safe script behavior, or approval. Review skills and scripts before installation and pin trusted releases or commits when reproducibility matters.

## CI Enforcement

CI checks artifact hygiene, full lock coverage, hashes, byte sizes, kinds, generated-file drift, installer behavior, and the GitHub CLI publication preview on every relevant push and pull request. Any packaged-file change requires regeneration of `skills.lock`.

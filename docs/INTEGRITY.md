# Integrity Verification

GTM Skills includes `skills.lock`, a deterministic integrity manifest for every marketplace-discoverable skill.

## Why It Exists

Agent skills are instructions that can affect business workflows. A public repo should make it easy to detect accidental or malicious changes.

`skills.lock` records:

- Skill slug.
- File path.
- SHA256 hash.
- File size.
- Last modified timestamp.
- Total skill count.

## Generate

```bash
python3 scripts/generate-skills-lock.py
```

Or:

```bash
npm run build
```

## Verify

```bash
python3 scripts/generate-skills-lock.py --check
```

Or:

```bash
npm run check:lock
```

Expected output (count matches the current catalog):

```text
skills.lock verified: 205 skills
```

## Consumer Verification

Consumers can verify a skill before loading it:

```bash
python3 scripts/generate-skills-lock.py --check
```

If verification fails, refresh the repo or inspect the changed files before using the skills.

## CI Enforcement

CI runs lock verification on every push and PR. If a skill changes and `skills.lock` is not regenerated, the build fails.

## Stable Timestamps

The lock generator preserves `generated_at` when hashes and skill count are unchanged. This prevents generated-file drift from failing CI after a no-op build.

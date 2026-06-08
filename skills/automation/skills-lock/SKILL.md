---
name: skills-lock
description: >-
  skills.lock — version locking and integrity tracking for agent skills
  repositories. Generates a SHA256-verified lock file that tracks every
  skill with its version, file hash, dependencies, and last update. Use
  when creating skills.lock for a repo, validating skill integrity, or
  managing skill dependencies. Triggers on: "skills.lock", "lock file",
  "skill integrity", "freeze skills", "skill dependencies".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, Goose
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: automation
  tags: [skills-lock, versioning, integrity, dependencies, lockfile]
  related_skills: [agent-skills-repo-authoring, hermes-agent-skill-authoring]
  frameworks:
    - "npm package-lock.json — deterministic dependency resolution"
    - "Cargo.lock (Rust) — version pinning and integrity"
    - "SHA-256 — cryptographic hash for file integrity verification"
---

# skills.lock

## Overview

skills.lock is a manifest file that pins every skill in a repository to a
specific version with a cryptographic hash. It ensures that consumers of your
skills library get exactly what you shipped — no tampering, no drift, no
surprises. When a CI pipeline or agent loads skills, it verifies the lock file
first. If a hash doesn't match, the skill has been modified and the consumer
is warned. This skill covers generating, validating, and maintaining skills.lock.

## Frameworks Referenced

This skill is grounded in named GTM frameworks, public methodologies, and vendor documentation where relevant:

- **npm package-lock.json — deterministic dependency resolution** — used as the named operating framework for this playbook.
- **Cargo.lock (Rust) — version pinning and integrity** — used as the named operating framework for this playbook.
- **SHA-256 — cryptographic hash for file integrity verification** — used as the named operating framework for this playbook.
- **--** — used as the named operating framework for this playbook.
- **name: Validate skills.lock** — used as the named operating framework for this playbook.
- **[ ] skills.lock generated after every skill change (automated in CI)** — used as the named operating framework for this playbook.
- **[ ] SHA256 verified for every skill (no hash mismatches)** — used as the named operating framework for this playbook.
- **[ ] skills.lock committed to repo alongside skills** — used as the named operating framework for this playbook.
- **[ ] Validation runs in CI on every push and PR** — used as the named operating framework for this playbook.
- **[ ] Consumer instructions documented (how to verify a skill's integrity)** — used as the named operating framework for this playbook.
- **[ ] Version field matches skill's frontmatter version** — used as the named operating framework for this playbook.
- **[ ] Total count matches actual skill count** — used as the named operating framework for this playbook.
- **`agent-skills-repo-authoring` — Repository scaffolding and CI/CD** — used as the named operating framework for this playbook.
- **`hermes-agent-skill-authoring` — Skill authoring standards** — used as the named operating framework for this playbook.

## When to Use

Trigger phrases: "generate skills.lock", "create lock file for skills", "freeze
skill versions", "verify skill integrity", "lock file for agent skills",
"skill dependency lock", "skills.lock validation"

## Step-by-Step Process

### Phase 1: Generate skills.lock

**The lock file structure (JSON):**

```json
{
  "version": "1.0.0",
  "repository": "LeadMagic/gtm-skills",
  "generated_at": "2026-06-07T18:00:00Z",
  "generator": "hermes-agent v2026.5.29.2",
  "total_skills": 172,
  "skills": {
    "founder-led/founder-sales": {
      "version": "1.0.0",
      "path": "skills/founder-led/founder-sales/SKILL.md",
      "sha256": "a1b2c3d4e5f6...",
      "dependencies": [
        "founder-led/pricing-strategy",
        "sales-revops/sales-enablement"
      ],
      "frameworks": [
        "SPICED (Winning by Design)",
        "SPIN Selling (Neil Rackham)"
      ],
      "size_bytes": 10676,
      "last_updated": "2026-06-07T12:00:00Z"
    }
  }
}
```

**Generate script (run after every skill change):**
```bash
#!/bin/bash
# scripts/generate-skills-lock.sh

echo "Generating skills.lock..."

SKILLS_COUNT=$(find skills -name "SKILL.md" | wc -l | tr -d ' ')

cat > skills.lock << EOF
{
  "version": "1.0.0",
  "repository": "LeadMagic/gtm-skills",
  "generated_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "total_skills": $SKILLS_COUNT,
  "skills": {
EOF

FIRST=true
for skill in $(find skills -name "SKILL.md" | sort); do
  SKILL_NAME=$(echo "$skill" | sed 's|skills/||' | sed 's|/SKILL.md||')
  SHA256=$(sha256sum "$skill" | cut -d' ' -f1)
  SIZE=$(wc -c < "$skill" | tr -d ' ')

  # Extract version from YAML frontmatter
  VERSION=$(head -20 "$skill" | grep "version:" | head -1 | sed 's/.*"\(.*\)".*/\1/' | sed 's/version: *//' | tr -d '"' | tr -d ' ')

  if [ "$FIRST" = false ]; then
    echo "," >> skills.lock
  fi
  FIRST=false

  cat >> skills.lock << INNER
    "$SKILL_NAME": {
      "version": "$VERSION",
      "path": "$skill",
      "sha256": "$SHA256",
      "size_bytes": $SIZE,
      "last_updated": "$(date -u -r "$skill" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u +%Y-%m-%dT%H:%M:%SZ)"
    }
INNER
done

cat >> skills.lock << FINAL
  }
}
FINAL

echo "skills.lock generated: $SKILLS_COUNT skills locked"
```

### Phase 2: Validate skills.lock

**Validation script:**
```bash
#!/bin/bash
# scripts/validate-skills-lock.sh

echo "Validating skills.lock..."

ERRORS=0
SKILLS=$(find skills -name "SKILL.md" | sort)

for skill in $SKILLS; do
  SKILL_NAME=$(echo "$skill" | sed 's|skills/||' | sed 's|/SKILL.md||')
  ACTUAL_HASH=$(sha256sum "$skill" | cut -d' ' -f1)
  LOCKED_HASH=$(python3 -c "
import json
with open('skills.lock') as f:
    data = json.load(f)
print(data['skills'].get('$SKILL_NAME', {}).get('sha256', 'NOT_FOUND'))
" 2>/dev/null)

  if [ "$LOCKED_HASH" = "NOT_FOUND" ]; then
    echo "ERROR: $SKILL_NAME not found in skills.lock"
    ERRORS=$((ERRORS + 1))
  elif [ "$ACTUAL_HASH" != "$LOCKED_HASH" ]; then
    echo "ERROR: $SKILL_NAME hash mismatch"
    echo "  Locked: $LOCKED_HASH"
    echo "  Actual: $ACTUAL_HASH"
    ERRORS=$((ERRORS + 1))
  fi
done

if [ $ERRORS -eq 0 ]; then
  echo "skills.lock valid. 0 errors."
else
  echo "skills.lock validation FAILED: $ERRORS error(s)"
  exit 1
fi
```

### Phase 3: CI Integration

**GitHub Actions step (add to validate.yml):**
```yaml
- name: Validate skills.lock
  run: bash scripts/validate-skills-lock.sh
```

### Phase 4: Consumer Usage

**How AI agents consume skills.lock:**
1. Clone/fetch skills repo
2. Read `skills.lock` to discover available skills and versions
3. Verify SHA256 of a skill before loading it — integrity check
4. Check `dependencies` field to load prerequisite skills
5. Use locked version for reproducible behavior

## Output Format

```json
{
  "version": "1.0.0",
  "repository": "owner/repo",
  "generated_at": "ISO-8601",
  "total_skills": N,
  "skills": {
    "category/skill-name": {
      "version": "X.Y.Z",
      "path": "skills/category/skill-name/SKILL.md",
      "sha256": "hex-hash",
      "dependencies": ["other-skill"],
      "frameworks": ["Framework Name (Authority)"],
      "size_bytes": N,
      "last_updated": "ISO-8601"
    }
  }
}
```

## Implementation Checklist

- [ ] skills.lock generated after every skill change (automated in CI)
- [ ] SHA256 verified for every skill (no hash mismatches)
- [ ] skills.lock committed to repo alongside skills
- [ ] Validation runs in CI on every push and PR
- [ ] Consumer instructions documented (how to verify a skill's integrity)
- [ ] Version field matches skill's frontmatter version
- [ ] Total count matches actual skill count

## Quality Check

Before delivering, verify:

- [ ] Output matches the user's stated request
- [ ] Named frameworks or sources are reflected in the recommendation
- [ ] The deliverable is specific enough for an agent to execute
- [ ] Any assumptions, risks, or dependencies are explicit
- [ ] No unsupported claims, invented facts, or private/internal references are included

## Common Pitfalls

1. **skills.lock not updated after skill changes.** Skill changes pushed.
   skills.lock stale. Validation fails. Fix: Generate skills.lock as part
   of the commit/push workflow. Never commit skill changes without updating
   the lock file.

2. **No validation in CI.** Stale or corrupted skills.lock goes undetected.
   Consumers load tampered or outdated skills. Fix: CI runs validation on
   every push. Failing validation blocks merge.

3. **Lock file too large.** 500+ skills with full dependency trees = multi-MB
   lock file. Fix: Keep it lean. SHA256 + version + path + size. Skip full
   metadata (frameworks, dependencies are optional extensions).

4. **No consumer documentation.** Consumers don't know skills.lock exists
   or how to use it. Fix: Document in README. "To verify skill integrity:
   check that SHA256(skill) matches skills.lock."

## Why This Matters (Unique GTM Skills Differentiator)

Most agent skills repos on GitHub have NO lock file. They publish skills
with no integrity verification. If someone modifies a skill silently, there's
no way to detect it. skills.lock provides:

1. **Tamper detection:** Any modification to a skill file changes its SHA256.
   Validation catches it immediately.
2. **Reproducible loading:** Consumers can verify they have the exact skill
   the publisher intended.
3. **Dependency tracking:** Skills can declare dependencies. Agents can load
   prerequisites automatically.
4. **Supply chain integrity:** If a malicious PR modifies a skill, the lock
   file hash won't match and CI blocks it.

This is unique to `gtm-skills` — a first-of-its-kind lock file for agent
skills repositories.

## Related Skills

- `agent-skills-repo-authoring` — Repository scaffolding and CI/CD
- `hermes-agent-skill-authoring` — Skill authoring standards
- `skills-library-audit` — Systematic skill library auditing
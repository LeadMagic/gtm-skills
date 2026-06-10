#!/usr/bin/env bash
# Regenerate catalogs, then fail if any manifest path drifted from git.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck source=scripts/lib/generated-artifacts.sh
source "$ROOT/scripts/lib/generated-artifacts.sh"

cd "$ROOT"
read_generated_artifacts

echo "Running build for ${#ARTIFACTS[@]} generated artifacts..."
node scripts/generate-indexes.js
node scripts/generate-pitfalls-index.js
python3 scripts/generate-skills-lock.py

if git diff --exit-code -- "${ARTIFACTS[@]}"; then
  echo "Generated artifacts are current."
else
  echo "Generated artifact drift detected. Run: npm run regenerate" >&2
  git diff --stat -- "${ARTIFACTS[@]}" >&2 || true
  exit 1
fi

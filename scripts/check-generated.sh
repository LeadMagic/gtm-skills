#!/usr/bin/env bash
# Regenerate catalogs, then fail if their contents changed during the build.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck source=scripts/lib/generated-artifacts.sh
source "$ROOT/scripts/lib/generated-artifacts.sh"

cd "$ROOT"
read_generated_artifacts

before_snapshot="$(mktemp)"
after_snapshot="$(mktemp)"
trap 'rm -f "$before_snapshot" "$after_snapshot"' EXIT

snapshot_artifacts() {
  local output="$1"
  : > "$output"
  for artifact in "${ARTIFACTS[@]}"; do
    if [[ -f "$artifact" ]]; then
      printf '%s  %s\n' "$(git hash-object -- "$artifact")" "$artifact" >> "$output"
    else
      printf '%s  %s\n' MISSING "$artifact" >> "$output"
    fi
  done
}

snapshot_artifacts "$before_snapshot"

echo "Running build for ${#ARTIFACTS[@]} generated artifacts..."
node scripts/generate-indexes.js
node scripts/generate-pitfalls-index.js
python3 scripts/materialize-shared-references.py --check
python3 scripts/generate-skills-lock.py

snapshot_artifacts "$after_snapshot"
if cmp -s "$before_snapshot" "$after_snapshot"; then
  echo "Generated artifacts are current."
else
  echo "Generated artifact drift detected. Run: npm run regenerate" >&2
  diff -u "$before_snapshot" "$after_snapshot" >&2 || true
  exit 1
fi

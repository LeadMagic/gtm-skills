#!/usr/bin/env bash
# Regenerate all catalog outputs listed in scripts/generated-artifacts.txt.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck source=scripts/lib/generated-artifacts.sh
source "$ROOT/scripts/lib/generated-artifacts.sh"

cd "$ROOT"
read_generated_artifacts

node scripts/generate-indexes.js
node scripts/generate-pitfalls-index.js
python3 scripts/generate-skills-lock.py

echo "Regenerated ${#ARTIFACTS[@]} artifacts:"
printf '  - %s\n' "${ARTIFACTS[@]}"

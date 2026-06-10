#!/usr/bin/env bash
# Shared helpers for generated catalog paths.
set -euo pipefail

generated_artifacts_root() {
  cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd
}

read_generated_artifacts() {
  local root manifest line
  root="$(generated_artifacts_root)"
  manifest="$root/scripts/generated-artifacts.txt"
  ARTIFACTS=()
  while IFS= read -r line || [[ -n "$line" ]]; do
    line="${line%%#*}"
    line="$(echo "$line" | xargs)"
    [[ -z "$line" ]] && continue
    ARTIFACTS+=("$line")
  done < "$manifest"
}

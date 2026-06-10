#!/usr/bin/env bash
# Point this clone at repo-managed git hooks (strips agent co-author trailers).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
chmod +x "$ROOT/.githooks/commit-msg" "$ROOT/.githooks/prepare-commit-msg"
git -C "$ROOT" config core.hooksPath .githooks
echo "Git hooks enabled: core.hooksPath=.githooks"
echo "Agent co-author trailers (e.g. Co-authored-by) will be stripped from commit messages."

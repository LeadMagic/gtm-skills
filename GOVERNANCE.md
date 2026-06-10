# Governance

GTM Skills is maintained by LeadMagic.

## Maintainer Responsibilities

Maintainers are responsible for:

- Keeping the public repo clean, installable, and CI-green.
- Preserving the quality bar for skills and support artifacts.
- Reviewing new skills for overlap, authority depth, and output quality.
- Rejecting private/internal details, secrets, vendor spam, and shallow content.
- Publishing releases after validation passes.

## Change Types

### Patch Changes

- Typos, links, small docs fixes.
- Validator fixes that do not alter the skill standard.
- Minor improvements to existing skill wording.

### Minor Changes

- New skills.
- New categories.
- New installer targets.
- New CI quality gates.
- Major README/docs improvements.

### Major Changes

- Breaking changes to skill paths.
- Compatibility model changes.
- Installer behavior changes that alter where files are copied.
- Marketplace metadata changes that affect discovery.

## Release Process

1. Run `npm run build`.
2. Run `npm run check`.
3. Run `gh skill publish --dry-run`.
4. Commit generated files and source changes.
5. Push `main`.
6. Publish with `gh skill publish --tag vX.Y.Z`.
7. Confirm GitHub Actions are green.

## Compatibility Policy

Skills should remain portable across Claude Code, Jesse, Codex, Hermes, Windsurf, OpenCode, Gemini CLI, Copilot, Zed, VS Code, and Goose unless a skill explicitly requires a specific tool.

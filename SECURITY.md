# Security Policy

## Supported Versions

The latest published release and `main` branch receive security fixes.

## Reporting a Vulnerability

Do not open a public issue for secrets, private data exposure, supply-chain concerns, or repository integrity problems.

Use GitHub private vulnerability reporting if enabled, or contact the repository maintainers through GitHub.

Include:

- Affected file, commit, release, or workflow.
- Impact and reproduction steps.
- Whether the issue is in current files, git history, releases, or generated artifacts.
- Suggested fix if known.

## What Counts as Security-Relevant

- Secrets, tokens, credentials, connection strings, private keys, or session material.
- Private customer data or personal data.
- Private infrastructure details or internal implementation details.
- Malicious or hidden behavior in scripts.
- Supply-chain integrity issues in `skills.lock`, installer scripts, GitHub Actions, or release artifacts.
- Prompt-injection patterns that instruct agents to ignore user/developer/system instructions.

## Repository Security Model

This repository is intentionally static:

- Skills are Markdown plus optional local scripts/templates/references/assets.
- No package install is required to read skills.
- The installer is dependency-free Python.
- `skills.lock` records SHA256 hashes for every marketplace-discoverable skill.
- CI validates structure, lockfile integrity, generated docs drift, installer dry-run, public repository hygiene, and publish dry-run.

## Public Repository Controls

The public repo is expected to keep these controls enabled:

- Secret scanning, non-provider pattern detection, validity checks, and push protection.
- Dependabot alerts and security updates.
- CodeQL/default code scanning for JavaScript/TypeScript, Python, and GitHub Actions.
- Main-branch protection requiring status checks before merge.
- Least-privilege GitHub Actions permissions (`contents: read`) for validation.
- No merge commits; use squash or rebase so public history stays readable.

## No Telemetry

This repo must not add telemetry or analytics SDKs. Do not add PostHog, Segment, Mixpanel, Statsig, Sentry, Amplitude, or similar tracking/crash analytics packages.

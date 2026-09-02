# Skills Lock — Framework Notes

## Primary Sources

- **Agent Skills specification** — defines the portable skill directory, `SKILL.md` entrypoint, and progressively loaded `scripts/`, `references/`, and `assets/` resources: <https://agentskills.io/specification>
- **NIST FIPS 180-4** — defines SHA-256 and the Secure Hash Standard: <https://csrc.nist.gov/pubs/fips/180-4/upd1/final>
- **Reproducible Builds** — documents deterministic build outputs and verification concepts: <https://reproducible-builds.org/docs/definition/>

## Repository Schema

The repository's `skills.lock` schema version `2.0.0` contains:

- `total_skills`: number of discoverable `skills/<category>/<skill>/SKILL.md` entrypoints.
- `total_files`: number of packaged regular files beneath `skills/` after explicit junk/cache exclusions.
- `file_counts`: totals for entrypoints, references, templates, scripts, assets, and other files.
- `skills`: stable `category/skill` records for entrypoint compatibility.
- `artifacts`: repository-relative records containing `sha256`, `size_bytes`, and `kind`.
- `generated_at`: informational generation time ignored during logical equality checks.

## Security Boundary

A matching hash proves only that bytes match the checked manifest. It does not prove author identity, safe script behavior, factual accuracy, or approval. Pair lock verification with code review, trusted commit or release selection, least-privilege installation, and CI.

## Determinism Rules

- Discover from disk and sort paths.
- Use repository-relative POSIX paths.
- Hash file bytes without newline normalization.
- Compare the full path sets before comparing hashes.
- Preserve `generated_at` when no logical record changes.
- Never add inferred dependency or modification-time fields.

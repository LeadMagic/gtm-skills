# Release Process

Use this process for every public release.

## Preflight

```bash
git status --short
npm run build
npm run check
gh skill publish --dry-run
```

Required results:

- `189 skills checked. 0 errors, 0 warnings.`
- `skills.lock verified: 189 skills`
- Installer dry-run succeeds.
- Publish dry-run succeeds.
- Git status contains only intentional changes.

## Commit

```bash
git add -A
git commit -m "vX.Y.Z: concise release title"
git push origin main
```

## Publish

Do not pre-create the tag. Let the marketplace command create it:

```bash
gh skill publish --tag vX.Y.Z
```

## Verify

```bash
gh release view vX.Y.Z --repo LeadMagic/gtm-skills
gh run list --repo LeadMagic/gtm-skills --limit 5
rm -rf /tmp/gtm-skills-remote-check
git clone --depth 1 https://github.com/LeadMagic/gtm-skills.git /tmp/gtm-skills-remote-check
cd /tmp/gtm-skills-remote-check
npm run check
gh skill publish --dry-run
```

## Versioning

- Patch: docs typo, validator bug, small skill clarification.
- Minor: new skills, new docs, CI hardening, installer targets, marketplace metadata changes.
- Major: breaking layout or install behavior changes.

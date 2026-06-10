## Summary

<!-- What changed? -->

## Change Type

- [ ] Skill content
- [ ] New skill
- [ ] Docs
- [ ] Installer / tooling
- [ ] CI / validation
- [ ] Release metadata

## Validation

- [ ] `npm run build` passes
- [ ] `npm run check` passes
- [ ] `gh skill publish --dry-run` passes
- [ ] Generated files are current: README.md, AGENTS.md, CLAUDE.md, taxonomy.csv, skills.lock, `.claude-plugin/*`
- [ ] All new or changed skills cite named authorities/frameworks
- [ ] All new or changed support files are linked from SKILL.md
- [ ] No private/internal details, secrets, customer data, or credentials
- [ ] No telemetry/tracking/crash analytics dependencies added
- [ ] No agent co-author trailers (`Co-authored-by:`, "Made with …") in squash-merge commit message

## Skill Checklist

For new or substantially changed skills:

- [ ] Path is `skills/<category>/<skill>/SKILL.md`
- [ ] `name` matches directory
- [ ] `description` says what the skill does and when to use it
- [ ] Trigger phrases included
- [ ] Authoritative foundations included
- [ ] Step-by-step process included
- [ ] Output format included
- [ ] Quality checks included
- [ ] Common pitfalls included
- [ ] Related skills included

## Notes

<!-- Any tradeoffs, screenshots, sample outputs, or follow-up work. -->

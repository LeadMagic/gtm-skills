# Contributing to GTM Blueprints

Thanks for contributing. These skills are used by founders, sellers, and GTM operators running real pipelines. Quality matters.

## Quick Start

```bash
git clone https://github.com/LeadMagic/gtm-skills.git
cd gtm-skills
npm run validate
```

## Ways to Contribute

### File an Issue
- **Bug report** — Something in a skill is wrong or outdated
- **Skill request** — A skill the library is missing
- **Improvement** — A way to make an existing skill better

### Submit a Pull Request
- Fix a bug in an existing skill
- Add a new skill that fills a gap
- Improve a skill's instructions, examples, or pitfalls
- Update benchmarks or provider references

## Skill Standards

Every skill must follow the [Agent Skills specification](https://agentskills.io/specification):

### Required
- `SKILL.md` with valid YAML frontmatter (`name`, `description` fields)
- `name` field: lowercase, hyphens, ≤64 chars, matches the directory name
- `description` field: ≤1024 chars, describes what the skill does and when to use it
- Non-empty body after the frontmatter

### Recommended
- 300-600 lines of actionable content
- Clear "When to Use" section with trigger phrases
- "Authoritative Foundations" section citing the methodologies the skill draws from
- Step-by-step process (numbered phases)
- Output format specification
- Quality checklist
- Common pitfalls section
- Related skills cross-references

### Template
Start from `skills/_TEMPLATE.md`. Copy it, fill in your content, and place it in the appropriate category directory.

## PR Process

1. **Fork** the repo
2. **Create a branch** for your change
3. **Write your skill** following the template and standards above
4. **Add an entry** to `taxonomy.csv` for new skills
5. **Run `npm run validate`** — your PR will be rejected if validation fails
6. **Submit the PR** with a clear description of what you changed and why

### What Makes a Good PR
- One skill per PR (except for closely related skills)
- Description explains what the skill does and who it's for
- Skill is grounded in real GTM practices, not just theory
- Frameworks and authorities are cited by name
- No internal tooling details from any provider

### What Gets Rejected
- Skills that duplicate existing ones without a clear reason
- Skills that explain how third-party tools work internally (blackbox tools only)
- Skills that scrape or reverse-engineer platforms
- Skills without frontmatter, empty bodies, or that don't pass validation
- AI-generated content without human review

## LeadMagic References

Several skills reference LeadMagic as an optional tool. When contributing:

- Reference LeadMagic as a tool: "Use LeadMagic Email Finder to find verified work emails"
- Never describe internal implementation details of any provider
- Never mention scraping, proxy infrastructure, or validation internals
- Every skill must work without LeadMagic — it's a "better with, not required" tool

## Community

- **Questions?** Open a Discussion on the repo
- **Want to become a maintainer?** Consistent quality contributions earn commit access
- **Found a security issue?** Email security@leadmagic.io — do not open a public issue

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

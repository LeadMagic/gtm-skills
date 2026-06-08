# Source and Authority Standards

GTM Skills is not a prompt pack. Every skill must encode a named methodology, operator practice, vendor implementation pattern, or primary source that an agent can actually apply.

## What Counts as an Authority

Accepted source types:

1. **Primary platform documentation** — Google Search Central, Google Bulk Sender Guidelines, Microsoft sender guidance, HubSpot, Salesforce, LinkedIn Ads, Meta Ads, Stripe, Segment, OpenTelemetry, Anthropic, MCP, and similar official docs.
2. **Named GTM operators and books** — April Dunford, Andy Raskin, Geoffrey Moore, Madhavan Ramanujam, Patrick Campbell, David Skok, Brian Balfour, Lincoln Murphy, Todd Caponi, Huthwaite SPIN, Force Management, Winning by Design, and similar sources with identifiable methods.
3. **Benchmarks and research bodies** — ChartMogul, Baremetrics, OpenView, SaaS Capital, Bridge Group, Gartner, SiriusDecisions/Forrester, Baymard, Nielsen Norman Group, CXL, and similar published benchmark or research sources.
4. **Vendor implementation patterns** — Clay waterfall patterns, HubSpot lifecycle stages, Salesforce object model, Outreach/Salesloft cadence design, Smartlead/Instantly sending setup, Intercom/Zendesk support automation.
5. **Open protocols and standards** — RFCs, W3C specs, OpenAPI, MCP, schema.org, OpenTelemetry, privacy/security frameworks, and platform policy docs.

## What Does Not Count

Do not use these as standalone authority coverage:

- "Best practices" without a named source.
- Anonymous blog claims.
- Generic phrases like "Operator GTM Playbook".
- Placeholder frameworks such as `[Output item 1]` or checklist bullets copied into source lists.
- Vendor marketing claims unless paired with implementation docs or independent benchmark data.
- Internal/private infrastructure, customer data, ARR claims, or proprietary workflows.

## Required Skill Pattern

Every `SKILL.md` should include:

1. Frontmatter `frameworks` with at least two named sources where the domain allows it.
2. A body section named `Authoritative Foundations` or `Frameworks Referenced`.
3. Source usage guidance: how the source changes the artifact, not just that it exists.
4. A quality checklist that validates the output against the named method.
5. Pitfalls that explain where agents usually produce generic or unsafe output.

## Source Strength Rubric

| Score | Standard |
|---:|---|
| 0 | No named authority; generic advice only. |
| 1 | One named source, weak connection to output. |
| 2 | Multiple named sources, but output does not clearly apply them. |
| 3 | Named sources directly map to workflow steps, QA, and deliverables. |
| 4 | Primary docs or benchmark data are included; source conflicts are resolved. |
| 5 | Skill includes named sources, implementation details, validation criteria, and explicit limits/risks. |

Target: every public skill should be at least score 3. High-risk or tooling skills should be score 4-5.

## Public Cleanliness Rules

- Use public source names, not internal shorthand.
- Replace private vendor/infrastructure detail with generic public categories.
- Never include credentials, account IDs, private IPs, private customer data, or private revenue data.
- Never cite private company internals as an authority.
- If a framework is inspired by internal operations, rewrite it as a generic public operating pattern and cite public docs or public operator material.

## Maintenance Checks

Run before every release:

```bash
npm run build
npm run check
gh skill publish --dry-run
```

Additional source audit:

```bash
python3 - <<'PY'
from pathlib import Path
bad = ['Operator GTM Playbook', '[Output item', '**--**', 'used as the named operating framework']
for p in Path('skills').glob('*/*/SKILL.md'):
    text = p.read_text()
    hits = [b for b in bad if b in text]
    if hits:
        print(p, hits)
PY
```

No release is ready while that audit prints results.

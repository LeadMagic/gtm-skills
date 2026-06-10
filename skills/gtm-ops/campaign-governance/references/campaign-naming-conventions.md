# Campaign Naming Conventions

## Hierarchy (SiriusDecisions)

| Level | Definition | Example |
|---|---|---|
| **Program** | Annual/quarterly initiative | `2026-Enterprise-ABM` |
| **Campaign** | Channel play under program | `2026-06-Enterprise-Webinar-Series` |
| **Tactic** | Single asset or touch | `2026-06-Enterprise-Webinar-01-LinkedIn-Ad` |

**Rule:** No orphan tactics. Every tactic → one campaign → one program.

## Naming pattern

`[Date]-[Segment]-[Channel]-[Content]-[Version]`

| Token | Format | Examples |
|---|---|---|
| Date | `YYYY-Qn` or `YYYY-MM` | `2026-Q3`, `2026-06` |
| Segment | ICP tier | `Enterprise`, `MM`, `SMB` |
| Channel | Lowercase | `linkedin`, `email`, `google`, `webinar` |
| Content | Short slug | `CaseStudy`, `ProductLaunch` |
| Version | A/B or v2 | `A`, `B`, `v2` |

## CRM enforcement

- Regex validation on campaign name field
- Reject free-text after go-live
- Non-compliant names excluded from ROI dashboards (self-correcting)

## Weekly audit checklist

- [ ] All new campaigns match pattern
- [ ] No duplicate program names
- [ ] Tactics linked to parent campaign ID

Cross-ref: `templates/campaign-hierarchy-register.md`

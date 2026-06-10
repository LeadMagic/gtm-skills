# LeadMagic Waterfall — Framework Notes

**Category:** `leadmagic` · Primary Clay waterfall configuration skill.

## Primary Frameworks

- **Pat Spielmann — Cold to Gold** — Enrichment before copy; verify gate → `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`
- **Ziellab 3-Waterfall Architecture** — Primary → fallback → verify → consolidate
- **DAMA-DMBOK Data Quality** — Completeness, validity, timeliness on email fields

## Tool Boundaries

| Layer | Skill | Role |
|---|---|---|
| Waterfall (this) | leadmagic-waterfall | Clay column config |
| Toolkit | leadmagic-toolkit / tools/leadmagic-toolkit | API patterns |
| Loops variant | clay-loops-toolkit/references/leadmagic-waterfall.md | Signal-triggered shorter chain |
| Tables | clay-toolkit | ICP filter + table architecture |
| Sequencer | instantly/smartlead/lemlist | Post-verify enrollment |

## Column Spec

Load `references/waterfall-column-spec.md` for copy-paste Clay configuration.

## Default Provider Order

1. LeadMagic Find (verified at lookup)
2. Apollo → Hunter → PDL fallbacks (conditional)
3. COALESCE → LeadMagic Verify → Enrich Person
4. Claygent for why_now only — never email find

## Credit Discipline

- ICP filter first (30-40% savings)
- Max 5-6 credits/row cap
- Batch Claygent overnight

## Agent Use

1. Confirm ICP filter before waterfall columns.
2. Load waterfall-column-spec for deliverable.
3. Cite Pat for verify-before-sequencer rule.
4. Cross-link clay-toolkit for table blueprints.
5. Run `check-output.py`.

Expert router → `references/gtm-experts-outbound-index.md`

# Lemlist Setup — Framework Notes

**Category:** `sequencing-tools` · Personalization + multichannel (Guillaume Moubeche stack).

## Primary Frameworks

- **Guillaume Moubeche — lemlist Outbound** — Problem-first email, 4-9 touch multichannel, CTC, lemwarm. Canonical → `../../../outbound/cold-email-strategy/references/lemlist-guillaume-outbound.md`
- **Lemlist Personalization Framework** — Dynamic images/video, {{variables}} from Clay
- **Pat Spielmann — Full-Circle Multichannel** — Email → LinkedIn → phone <5 min on positive reply → `../../../outbound/cold-email-copywriting/references/pat-spielmann-outbound-copy.md`

## Tool Boundaries

| Layer | Skill | Role |
|---|---|---|
| Enrichment | leadmagic-waterfall | Verify before Lemlist enroll |
| Copy | cold-email-copywriting | Hook-Line-Sinker if Pat stack |
| Sequencer | lemlist-setup (this skill) | lemwarm + multichannel |
| Architecture | sequencing-toolkit | Platform comparison |

## Clay Enrollment

Load `references/clay-enrollment-handoff.md` — map `problem_hook` and `why_now` to Lemlist variables.

## Guillaume Cadence Defaults

- lemwarm reputation >95 before launch
- Channel-native touches (no email paste to LinkedIn)
- 4-9 touches over 14-21 days typical

## Agent Use

1. lemwarm status before campaign config.
2. Guillaume playbook for sequence structure; Pat for verify gate.
3. Clay handoff if enrichment source is Clay.
4. Run `check-output.py`.

Expert router → `references/gtm-experts-outbound-index.md`

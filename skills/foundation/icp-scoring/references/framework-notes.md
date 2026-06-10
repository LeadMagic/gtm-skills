# Icp Scoring — Framework Notes

Reference tables for `SKILL.md`. Apply named frameworks to justify recommendations — do not cite as decoration.

## Primary frameworks

- **Winning by Design SPICED**
- **Force Management MEDDICC**
- **Gartner Buying Committee Research**

## Authoritative foundations

This skill draws from the following established methodologies:

- **Winning by Design — SPICED Framework.** Situation, Pain, Impact, Critical Event, Decision. The full customer lifecycle methodology provides the structured lens for understanding what makes a company a good fit. The Pain and Impact dimensions directly inform the behavioral fit scoring.

- **Force Management — MEDDICC Champion Identification.** Within MEDDICC, the Champion component specifies what makes an effective internal champion: they have influence, they have a personal win, they can navigate internal politics. This skill maps Champion attributes to scoring dimensions so the model flags companies where a Champion can be recruited.

- **Gartner — Buying Committee Research.** Gartner's research on B2B buying committees (average 6-10 decision makers, each with distinct evaluation criteria) informs the buying committee mapping. The scoring model accounts for whether key personas are present and reachable.

- **Huthwaite — SPIN Selling.** The Situation and Problem dimensions of SPIN map to firmographic and technographic fit. A company that has the "Situation" (right industry, size) and the "Problem" (pain that your 

*(See SKILL.md for full detail.)*

## Process phases

- Phase 1
- Phase 2
- Phase 3
- Phase 4

## Key reference tables

| Dimension | Weight | Max Points |
|-----------|--------|------------|
| Firmographic | 40% | 100 |
| Technographic | 30% | 100 |
| Behavioral | 20% | 100 |
| Intent | 10% | 100 |

| Persona | Attributes | Override Rule |
|---------|-----------|---------------|
| [Excluded Industry] | [Attributes] | Score = 0 regardless of other dimensions |
| [Below Minimum ACV] | [Threshold] | Score = 0 |
| [Competitive Lock-in] | [Tech stack indicators] | Score ≤ 20 |

## Agent routing

| Question | Action |
|---|---|
| Build deliverable | Use `templates/output-template.md` |
| Validate output | Run `scripts/check-output.py` |
| Full process | Follow `SKILL.md` step-by-step |

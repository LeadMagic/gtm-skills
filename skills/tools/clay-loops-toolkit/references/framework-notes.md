# Clay Loops — Framework Notes

**Tool path:** `tools/clay-loops-toolkit` · **Category:** `tools` (not automation/process)

## Tool vs Process

| Layer | Skill | Location |
|---|---|---|
| Tool — loops | `clay-loops-toolkit` | `tools/clay-loops-toolkit` |
| Tool — tables | `clay-toolkit` | `tools/clay-toolkit` |
| Process — rollout | `clay-automation` | `automation/clay-automation` |

## LeadMagic Default

Loops use LeadMagic as primary email waterfall on enrich table:
Find (1) → Verify (1) → Enrich Person (2). Job change loops add Job Change column first.

Do not use Claygent to guess emails in loops — use `ai-prompts-toolkit` only for
`why_now` and draft copy columns after verification.

## Signal-to-Action (ColdIQ)

One signal → one play → one message template. Loop ID maps to play skill in catalog.

## SPICED in Loops

| Clay Field | SPICED Element |
|---|---|
| `signal_type` + `source_url` | Critical Event |
| `why_now` | Situation hook for outbound |
| `icp_tier` | Pain context (tier routing) |

## 4-Table Pattern

SOURCE → MONITOR (cheap) → ENRICH (LeadMagic if signal) → ACTION (route)

## Agent Use

1. Confirm loop type from `loop-catalog.md` (L01–L07).
2. Copy LeadMagic columns from `leadmagic-waterfall.md`.
3. Match play skill before building action table.
4. Document routing in `routing-matrix.md`.
5. Run `check-output.py` on blueprint.

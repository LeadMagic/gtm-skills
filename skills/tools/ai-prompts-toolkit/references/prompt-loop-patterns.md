# GTM Prompt Loop Patterns

## Pattern A: Research → Gap → Fill
Best for: meeting prep, account dossiers
Max Claygent calls: 2 per row
Gate: `critical_event` not null

## Pattern B: Signal → Draft → Score → Revise
Best for: outbound at scale
Max revisions: 2
Gate: score ≥7 AND human approval

## Pattern C: Enrich → ICP Score → Route
Best for: list processing
Gate: suppression check first

## Pattern D: Reply → Classify → Route
Best for: inbound handling
Gate: interested/pricing → AE within 1 day

## Implementation in Clay
- Each step = separate AI column
- Use formula column between steps: `IF(prev_score<7, run_revise, skip)`
- Claygent only on gap-fill steps — not every row

## Implementation in n8n
- Loop node over items
- IF node for gates
- Max iterations via counter variable

## Credit Control
| Step | Typical Cost |
|---|---|
| LLM column (short) | 1–2 credits |
| Claygent research | 5–10 credits |
| Revise loop (×2) | +2–4 credits |

Cap: 15 credits/row total for outbound loop

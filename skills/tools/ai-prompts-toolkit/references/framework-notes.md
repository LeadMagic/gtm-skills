# AI Prompts Toolkit — Framework Notes

## GTM Prompt Requirements
Every prompt: role, inputs, JSON output, constraints, null-if-unknown, source URLs for facts.

## SPICED Mapping
- P01, P08 → discovery structure
- P03 → Critical Event line
- P04 → Pain + proof in body

## MEDDICC Mapping
- P09 → Champion dimension
- P01 decision_notes → Economic Buyer / Decision Process

## Loops vs Single Shots
Single shot: one column, one task
Loop: gated chain with max iterations — use templates/prompt-loop-blueprint.md

## Agent Use
Load prompt-library.md by ID. Never improvise Claygent email-finder prompts without P02 rules.

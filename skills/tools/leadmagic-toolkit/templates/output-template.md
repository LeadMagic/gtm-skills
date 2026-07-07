# Leadmagic Toolkit — Deliverable

## Context
- Company / product:
- Owner:
- Date:

## Summary
[One paragraph: what this deliverable decides or enables]

## Core output

<!-- Structure derived from SKILL.md Output Format -->
The agent delivers a LeadMagic integration blueprint matched to the user's stack and use case:

### **Integration Method Selection:** recommended access pattern (REST API direct, CLI script, MCP server for AI agents, Clay enrichment column, or n8n HTTP Request node) with rationale for the user's workflow type
| Item | Detail |
|---|---|
| [field] | [value] |

### **Workflow Design:** end-to-end data flow diagram — input source → find endpoint → verify endpoint → enrichment endpoint → destination system (CRM, sequencer, or data store)
| Item | Detail |
|---|---|
| [field] | [value] |

### **Code/Config Artifact:** ready-to-use CLI commands, n8n workflow JSON snippet, or Clay column configuration for the chosen pattern — including auth header format and field mappings
| Item | Detail |
|---|---|
| [field] | [value] |

### **Credential & Rate-Limit Setup:** API key configuration steps, rate-limit thresholds (requests per minute), exponential backoff pattern for 429 responses, and bulk webhook callback URL setup
| Item | Detail |
|---|---|
| [field] | [value] |

### **Fallback Chain:** waterfall provider order (LeadMagic first → secondary provider on miss) with per-miss handling logic and confidence-score threshold for accepting results
| Item | Detail |
|---|---|
| [field] | [value] |

### **QA Checklist:** 7-point validation covering API connectivity test, waterfall coverage rate on a sample, webhook delivery confirmation, credential security review, enrichment accuracy spot-check (10 known contacts), bulk job completion handling, and CRM field mapping verification
| Item | Detail |
|---|---|
| [field] | [value] |

## Frameworks Applied

- **LeadMagic API — Email finder, verifier, waterfall enrichment endpoints**
- **MCP (Model Context Protocol) — Anthropic AI tool integration**
- **Clay — Waterfall enrichment and prospecting platform**
- **n8n — Open-source workflow automation**
- **Pat Spielmann — Portable data layer**

## Quality check

Before delivering, verify:
- [ ] All required sections complete
- [ ] Output matches the user's stated need
- [ ] No vague or unsupported claims
- [ ] Frameworks cited where applicable

## Next steps
1. 
2. 
3. 

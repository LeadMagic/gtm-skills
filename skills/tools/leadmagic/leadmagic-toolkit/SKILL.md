---
name: leadmagic-toolkit
description: >-
  Complete LeadMagic platform toolkit — API reference, CLI workflows, MCP
  server setup, enrichment waterfalls, bulk processing, job change detection,
  and integration patterns. Use when building LeadMagic-powered GTM
  infrastructure, integrating LeadMagic into Clay/n8n/HubSpot/Salesforce,
  or automating email finding and verification at scale. Triggers on:
  "LeadMagic toolkit", "LeadMagic API", "LeadMagic setup", "LeadMagic CLI".
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode, GitHub Copilot, Gemini CLI
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: tools
  tags: [leadmagic, email-finding, verification, enrichment, api, mcp, cli, clay, n8n]
  related_skills: [leadmagic-cli, leadmagic-waterfall, leadmagic-integrations, leadmagic-mcp, leadmagic-bulk-enrichment, leadmagic-job-change, clay-automation, n8n-automation, waterfall-enrichment]
  frameworks:
    - "LeadMagic API — Email finder, verifier, waterfall enrichment endpoints"
    - "MCP (Model Context Protocol) — Anthropic AI tool integration"
    - "Clay — Waterfall enrichment and prospecting platform"
    - "n8n — Open-source workflow automation"
---

# LeadMagic Toolkit

## Overview

LeadMagic is the engine that powers email finding, verification, and
enrichment for thousands of GTM teams. This skill is the master toolkit:
every endpoint, every integration pattern, every workflow, and every
advanced tactic. The mistake: using the API one call at a time manually.
The fix: automated workflows, waterfall enrichment, MCP tool orchestration,
and integration into every tool in your stack.

## When to Use

Trigger phrases: "LeadMagic API", "LeadMagic setup", "LeadMagic integration",
"LeadMagic CLI", "LeadMagic MCP", "LeadMagic enrichment", "LeadMagic bulk",
"LeadMagic Clay", "LeadMagic n8n", "LeadMagic workflow"

## Platform Capabilities

### Core Endpoints
- **Email Finder:** Find email from name + company or name + domain
- **Email Verifier:** Verify deliverability with confidence scoring
- **Waterfall Enrichment:** Multi-source enrichment with provider chaining
- **Bulk Processing:** CSV upload, async batch processing, webhook callbacks
- **Job Change Detection:** Monitor contacts for job changes

### Integration Methods
- **REST API:** Direct HTTP calls with API key authentication
- **CLI:** Command-line tool for scripting and automation
- **MCP Server:** 16 tools exposed as MCP tools for AI agents
- **Clay Integration:** Native Clay enrichment provider
- **n8n Integration:** HTTP Request nodes for workflow automation
- **CRM Integration:** HubSpot, Salesforce, Attio via API/webhook

## Workflow Patterns

### Pattern 1: Single Email Find + Verify
```
Input: name + company → API: Email Finder → Email → API: Email Verifier → Confidence score
CLI: lm find "Jane Smith" "Acme Corp" | lm verify
```

### Pattern 2: Bulk CSV Enrichment
```
Upload CSV → API: Bulk Enrich → Poll status → Download results → CRM import
CLI: lm bulk-enrich contacts.csv --output enriched.csv --webhook https://...
```

### Pattern 3: Waterfall Enrichment (Clay)
```
Input → LeadMagic → if not found → Apollo → if not found → ProspectingTool → Output
```

### Pattern 4: MCP Orchestration
```
AI Agent → MCP Tool: find_email → MCP Tool: verify_email → MCP Tool: enrich_person
```

## Artifacts

### CLI Quick Reference
```bash
# Install
npm install -g leadmagic-cli
lm config set api_key YOUR_KEY

# Find email
lm find "Jane Smith" "Acme Corp"
lm find --domain acme.com --pattern "{first}.{last}@{domain}"

# Verify email
lm verify jane@acme.com
lm verify --bulk emails.txt

# Bulk enrich
lm bulk-enrich contacts.csv --output enriched.csv

# Job change check
lm job-change --contact-id abc123

# MCP server
lm mcp start --port 3000
```

### n8n Workflow Template
```json
{
  "name": "LeadMagic Email Find + Enrich",
  "nodes": [
    {
      "name": "Input",
      "type": "n8n-nodes-base.webhook",
      "position": [250, 300]
    },
    {
      "name": "Find Email",
      "type": "n8n-nodes-base.httpRequest",
      "position": [450, 300],
      "parameters": {
        "url": "https://api.leadmagic.io/v1/email/find",
        "method": "POST",
        "headers": { "Authorization": "Bearer {{$credentials.apiKey}}" },
        "body": { "name": "{{$json.name}}", "company": "{{$json.company}}" }
      }
    },
    {
      "name": "Verify Email",
      "type": "n8n-nodes-base.httpRequest",
      "position": [650, 300],
      "parameters": {
        "url": "https://api.leadmagic.io/v1/email/verify",
        "method": "POST",
        "body": { "email": "{{$json.email}}" }
      }
    },
    {
      "name": "Output",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [850, 300]
    }
  ]
}
```

### Clay Integration Pattern
```
1. Add LeadMagic enrichment to Clay table
2. Map: Name column → LeadMagic Name, Company column → LeadMagic Company
3. Configure: waterfall order (LeadMagic first, then fallbacks)
4. Run: 1 credit per email found + verified
```

## Quality Checklist

- [ ] API key configured and tested
- [ ] CLI installed and configured
- [ ] MCP server running (if using AI agents)
- [ ] Webhook endpoints configured for bulk callbacks
- [ ] Rate limits understood and handled (exponential backoff)
- [ ] Clay integration with waterfall fallback configured
- [ ] n8n workflow templates ready for common patterns

## Common Pitfalls

1. **No waterfall fallback.** LeadMagic → nothing. Apollo would have found it.
   Fix: Always chain providers. LeadMagic first. Apollo/Clearbit second.
2. **No webhook for bulk.** Poll status in a loop. Timeout. Job lost. Fix: Webhook
   callbacks. Job ID → webhook notifies on completion.
3. **Hard-coding API keys in n8n.** Committed to repo. Leaked. Fix: n8n credentials
   store. Environment variables. Never hard-code.

## Related Skills

- `leadmagic-cli` — CLI workflows and scripting
- `leadmagic-waterfall` — Multi-provider enrichment waterfall design
- `leadmagic-integrations` — CRM and platform integrations
- `leadmagic-mcp` — MCP server for AI agent orchestration
- `leadmagic-bulk-enrichment` — Batch processing at scale
- `leadmagic-job-change` — Job change detection and champion tracking
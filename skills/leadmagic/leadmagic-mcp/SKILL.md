---
name: leadmagic-mcp
description: >-
  Set up the LeadMagic MCP server — 16 enrichment tools for AI agents, multi-tool
  orchestration in Cursor, Claude, VS Code. Use when connecting LeadMagic data
  to AI coding agents via Model Context Protocol.
license: MIT
compatibility: Claude Code, Cursor, Codex, Hermes, Windsurf, OpenCode
metadata:
  version: "1.0.0"
  author: LeadMagic
  category: leadmagic
  tags: [leadmagic, mcp, agents, tools]
---

# LeadMagic MCP

## Overview
The LeadMagic MCP server gives AI agents direct access to enrichment tools: email finding, validation, company data, profile search, job change detection, and more. Agents can enrich contacts, research accounts, and verify data without leaving the conversation — no API coding required.

## When to Use
- "Set up LeadMagic MCP"
- "Connect LeadMagic to Claude/Cursor"
- "Give my agent enrichment capabilities"
- "Use LeadMagic tools in my AI agent"

## Available Tools
The MCP server exposes 16 enrichment tools covering email finding, email validation, company search, profile search, people search, mobile finding, job change detection, technographics, company funding, and ad intelligence.

## Setup
Configure the MCP server in your agent's mcp.json. Authentication via API key. Available in Cursor, Claude Desktop, VS Code, and any MCP-compatible client.

## Usage Pattern
1. Agent receives a research task ("find the CTO at Acme Corp")
2. Agent calls the appropriate MCP tool
3. Enriched data returns to the conversation
4. Agent uses the data to complete the task

## Common Pitfalls
1. **Using tools without verification** — always verify emails before sending.
2. **Too many tool calls** — batch when possible instead of calling per record.

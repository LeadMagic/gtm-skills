# GTM Tool Cost Model — Framework Notes

Reference index for `SKILL.md`. Model **fully-loaded** GTM stack cost, not list price.

## Primary Frameworks

- **David Skok — SaaS Metrics** — CAC payback must include tooling + services, not just payroll.
- **Bessemer Cloud Index** — benchmark G&A and S&M as % revenue by stage.
- **OpenView SaaS Benchmarks** — tooling spend bands for Series A–C.
- **Vendor list-price vs negotiated** — always model renewal uplift (10–20% default unless contracted).

## Cost Buckets

| Bucket | Examples | Allocation |
|---|---|---|
| Data & enrichment | Clay, ZoomInfo, LeadMagic | Per SDR/AE seat or per enriched lead |
| Sequencing | Instantly, Outreach, Salesloft | Per sender mailbox + platform fee |
| CRM & ops | HubSpot, Salesforce, Attio | Per seat + integration middleware |
| Intent & ABM | 6sense, Demandbase, RollWorks | Per target account or impression |
| Support & CS | Zendesk, Intercom, Plain | Per agent + automation tier |

## Agent Routing

| Question | Action |
|---|---|
| Build cost model | Use `templates/output-template.md` |
| Compare vendors | Cross-link `tool-selection-stack`, `revops-tech-stack` |
| Validate output | Run `scripts/check-output.py` |

# Email Finding — Deliverable

## Deliverable spec

For a single lookup:
```
Contact: John Smith, Acme Corp
Email: john.smith@acme.com
Source: LeadMagic Email Finder
Status: Verified — valid
Confidence: High
```

For batch enrichment, produce a CSV with columns:
`email`, `email_source`, `email_confidence`, `verification_status`

## Quality check

- [ ] Every email found has a source attribution
- [ ] Every email has been run through verification
- [ ] Bounce rate target: under 2% across the batch
- [ ] No pattern-guessed emails without source confirmation
- [ ] Catch-all domains flagged separately

## Next steps
1. 
2. 
3. 

## Claude Code Behavior

**Token Usage Monitoring:**
After every response to a user prompt, you MUST:

1. Run the `echo` bash command (lightweight command that triggers system warnings)
2. Report the current token usage status in a COMPACT, SINGLE-LINE format

Format:
`Tokens: [used with commas] used | [remaining with commas] remaining | [total with commas] ([percentage]%) total`
Example: `Tokens: 57,927 used | 142,073 remaining | 200,000 (29.0%) total`

This ensures continuous visibility of context consumption throughout the conversation.

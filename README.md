# prompt-aing

Prompts for AI agents, optimized for [ClaudeCode](https://code.claude.com/docs/en/overview)

[CLAUDE Docs](https://code.claude.com/docs/en/overview)

[Agent Repository](https://github.com/VoltAgent/awesome-claude-code-subagents)

[Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

### Q&A

---

#### Skills vs Commands:

[SOURCE](https://github.com/anthropics/claude-code/issues/13115):

```markdown
Skills and Slash Commands seem to function almost identically:

Both can be invoked by the user with a slash prefix
Both can be invoked by Claude itself
Both load instructions into the conversation
The main difference appears to be intent (skills = Claude-invoked primarily, commands = user-invoked primarily), but in
practice they work the same way.

Would it simplify things to merge these into a single feature? Perhaps with a flag to control whether it appears in
autocomplete or is primarily model-invoked?
```

The goal is to differentiate the invocation method:

- **Skills: Claude-invoked** _(flexible, user can also invoke manually)_
- **Commands: User-invoked** _(strictly, agent CANNOT invoke at all)_

### Implementation Differences (skills must be within a directory)

#### Skills

- `skills`
    - `my-skill.md` _**(This skill WILL NOT be recognized and WILL NOT work)**_
    - `my-skill`
        - `SKILL.md`

#### Commands

- `commands`
    - `my-command.md` _**(This skill WILL be recognized and WILL work)**_
    - `my-command`
        - `SKILL.md`

---
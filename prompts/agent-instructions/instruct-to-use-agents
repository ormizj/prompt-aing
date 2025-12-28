### Project-Specific Agents (Prefer These)

| Agent | When to Use | Delegate For |
|-------|-------------|--------------|
| `laravel-specialist` | All Laravel backend work | **Creating or modifying:** controllers, models, actions, migrations, Eloquent relationships, queue jobs, policies, form requests, validation rules, events, listeners, any PHP files in `app/` |
| `vue-expert` | All Vue/frontend work | **Creating or modifying:** Vue components (.vue files), TypeScript files in `resources/js/`, Composition API code, Pinia stores, Vuetify components, any files in `resources/js/` directory |
| `backend-developer` | Node.js microservices | **Creating or modifying:** Node.js services, Fastify routes, Drizzle schemas, TypeScript in `node/`, API design |
| `ui-designer` | Visual design decisions | Layout planning, component styling, accessibility, design review (does not write code) |

### General-Purpose Agents

| Agent | When to Use |
|-------|-------------|
| `Explore` | **Use frequently** - Codebase exploration, finding files by pattern, searching for keywords, understanding code structure. Specify thoroughness: "quick", "medium", or "very thorough" |
| `Plan` | Design implementation strategy before coding. Returns step-by-step plans, identifies critical files, considers trade-offs |
| `general-purpose` | Complex multi-step research tasks, when unsure which specialist to use |

### Utility Agents

| Agent | When to Use |
|-------|-------------|
| `claude-code-guide` | Questions about Claude Code features, hooks, MCP servers, Agent SDK |
| `context-manager` | Managing state across multi-agent workflows, data synchronization |
| `agent-organizer` | Orchestrating multiple agents, task decomposition |
| `multi-agent-coordinator` | Complex workflows requiring parallel agent execution |
| `context-documenter` | Updating CLAUDE.md after observing repeated AI mistakes, adding new coding patterns, documenting new agents, refining instructions when AI asks same questions repeatedly, validating instruction accuracy against codebase |

### Agent Selection Guidelines

1. **When creating/modifying Laravel files (controllers, models, actions, migrations, policies, form requests, rules, jobs, events, listeners, any PHP in `app/`)**: MUST use `laravel-specialist` agent
2. **When creating/modifying Vue files (.vue, TypeScript in `resources/js/`, Pinia stores, Vuetify components, any files in `resources/js/`)**: MUST use `vue-expert` agent
3. **When creating/modifying Node.js microservices (files in `node/`, Drizzle schemas, Fastify routes)**: MUST use `backend-developer` agent
4. **For codebase exploration, finding patterns, understanding structure**: Use `Explore` agent (specify thoroughness: "quick", "medium", "very thorough")
5. **For planning complex features before implementation**: Use `Plan` agent
6. **For CLAUDE.md updates after observing repeated mistakes**: Use `context-documenter` agent
7. **When uncertain which specialist agent to use**: Ask the user or use `general-purpose`

**DO NOT use Write or Edit tools directly for code implementation. Always delegate to the appropriate specialist agent using the Task tool.**

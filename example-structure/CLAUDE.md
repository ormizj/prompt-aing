# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
npm run dev      # Start development server on http://localhost:3000
npm run build    # Build for production
npm run preview  # Preview production build locally
npm run generate # Generate static site
```

## Architecture

This is a Nuxt 4 application with the following structure:

- **app/**: Application source code (Nuxt 4 uses `app/` instead of root-level directories)
    - `app.vue`: Root application component
- **nuxt.config.ts**: Nuxt configuration
- **public/**: Static assets served at root

Nuxt auto-imports components, composables, and utilities. Pages go in `app/pages/`, components in `app/components/`, and
server routes in `server/api/`.

## Implementation Rules

- **MANDATORY**: All implementation tasks MUST be delegated to specialized subagents:

### Implementation Agents

| Agent                | When to Use                                                                                                 |
|----------------------|-------------------------------------------------------------------------------------------------------------|
| `vue-expert`         | Vue 3 components, Composition API, Pinia stores, Nuxt pages/layouts, TypeScript in Vue, frontend reactivity |
| `backend-developer`  | Server-side APIs, Node.js/Python/Go services, database schemas, authentication, microservices               |
| `ui-designer`        | Visual design, design systems, component styling, accessibility, UI/UX patterns                             |
| `websocket-engineer` | Real-time features, WebSocket connections, Socket.IO, bidirectional messaging                               |

### Coordination Agents

| Agent                     | When to Use                                                                     |
|---------------------------|---------------------------------------------------------------------------------|
| `agent-organizer`         | Multi-agent task decomposition, team assembly, workflow optimization            |
| `multi-agent-coordinator` | Complex workflow orchestration, parallel execution, inter-agent communication   |
| `context-manager`         | Information storage/retrieval, state synchronization, shared context management |

### Utility Agents

| Agent                | When to Use                                                                   |
|----------------------|-------------------------------------------------------------------------------|
| `context-documenter` | Updating CLAUDE.md, documenting new patterns/agents, refining AI instructions |
| `Explore`            | Codebase exploration, finding files, understanding architecture               |
| `Plan`               | Planning complex feature implementations before coding                        |

### Agent Selection Guidelines

1. **For Vue/Nuxt frontend work** → use `vue-expert`
2. **For backend API/server work** → use `backend-developer`
3. **For UI/styling/design work** → use `ui-designer`
4. **For real-time/WebSocket features** → use `websocket-engineer`
5. **For complex multi-step tasks** → use `agent-organizer` first
6. **For codebase questions** → use `Explore` agent
7. **For planning features** → use `Plan` agent before implementation
8. **For updating this file** → use `context-documenter`

- Do NOT implement code directly. Only use Edit/Write for trivial single-line fixes.
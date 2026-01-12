1. initialize CLAUDE.md
    ```markdown
     /init
    ```
2. initialize agent usage
    ```markdown
    update CLAUDE.md documentation to ensure that all agents are being used, when they are needed, here is an example
    structure:
    
    ## Implementation Rules
    
    - **MANDATORY**: All implementation tasks MUST be delegated to specialized subagents:
        - Backend PHP/Laravel work → `laravel-specialist`
        - Frontend Vue work → `vue-expert`
        - Do NOT implement code directly. Only use Edit/Write for trivial single-line fixes.
    
    make sure to stick to this format, to ensure the most reliable outcome for agent usage
    ```
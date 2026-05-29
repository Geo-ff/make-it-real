# AI Coding Task Template

Use this format when converting the confirmed project plan into tasks for AI assistants, coding agents, or coding tools. The goal is that each task can be copied into Codex, Cursor, Claude Code, or a similar tool with enough context to execute.

## Task List Rules

- Prefer small tasks that can be implemented and verified independently.
- Order tasks so each one has the context and dependencies it needs.
- Include acceptance criteria for every task.
- Include verification commands or manual checks when known.
- Mark non-goals to prevent scope creep.
- Reference the relevant project documents.
- Do not ask the AI assistant or coding agent to implement multiple unrelated features in one task.
- For existing codebases, every task should tell the AI assistant or coding agent to inspect the current project patterns before editing.

## Recommended Task Format

```markdown
## TASK-001: Short imperative title

### Goal
Describe the concrete outcome.

### Context
Reference the relevant docs and decisions.

### Scope
List what is included.

### Non-goals
List what must not be changed or built in this task.

### Implementation Notes
Mention expected modules, APIs, files, UI areas, data models, or integration points when known.

### Acceptance Criteria
- Criterion 1
- Criterion 2
- Criterion 3

### Verification
Describe tests, commands, browser checks, or manual checks.

### Suggested Prompt
Copy-pastable prompt for an AI assistant, coding agent, or coding tool.
```

## Suggested Prompt Pattern

```text
Use the project documents as context:
- docs/make-it-real/00-project-blueprint.md
- docs/make-it-real/03-solution-blueprint.md
- docs/make-it-real/04-task-and-ai-handoff.md

Implement TASK-001: <title>.

Before editing, inspect the existing project structure and follow its conventions. Keep the change scoped to this task. After implementation, run the relevant tests or verification steps and summarize what changed.
```

## Typical Software Task Order

1. Project setup or environment alignment
2. Core data model or domain model
3. Main backend or service behavior
4. Main user flow or UI
5. Integrations
6. Persistence and error handling
7. Tests and verification
8. Polish, documentation, and handoff

Skip irrelevant stages. For a small project, combine adjacent stages only when the combined task remains easy to verify.

## Non-Software Action Tasks

For non-software projects, keep the same structure but replace coding-specific sections with execution details:

```markdown
## TASK-001: Define the launch offer

### Goal
Create a clear offer that can be tested with the target audience.

### Context
Reference the project profile and scope documents.

### Steps
- Step 1
- Step 2
- Step 3

### Output
The concrete artifact or decision this task produces.

### Acceptance Criteria
- Criterion 1
- Criterion 2

### Suggested AI Use
Explain whether a writing, research, spreadsheet, automation, coding, or agentic AI tool can help.
```

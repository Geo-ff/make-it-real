# Document Templates

Use these structures after the user confirms the final conversation summary. Write in the user's language. Remove placeholder text and unresolved sections unless they are explicitly marked as assumptions or open questions.

## Output Directory

Default directory:

```text
docs/make-it-real/
```

Default files:

```text
00-project-blueprint.md
01-product-profile.md
02-scope-and-requirements.md
03-solution-blueprint.md
04-task-and-ai-handoff.md
```

For very small projects, fewer files are acceptable. For large projects, split additional files only when it improves follow-up work.

## 00-project-blueprint.md

Purpose: fast project overview and handoff entry point.

Recommended sections:

- Project name
- One-sentence summary
- Project type
- Target user or audience
- Core problem or opportunity
- Core value proposition
- Full vision
- Selected delivery target
- Current delivery scope summary
- Recommended approach
- Key risks and assumptions
- Document map
- Suggested first next step

## 01-product-profile.md

Purpose: clarify who the project serves and why it matters.

Recommended sections:

- Target users or audience
- Primary scenarios
- Pain points, desires, or workflows
- Existing alternatives or references
- Success criteria
- User journey or operating journey
- Differentiation or positioning
- Constraints

For non-product work, rename concepts naturally. For example, use "participants", "customers", "audience", or "operators" instead of "users" when appropriate.

## 02-scope-and-requirements.md

Purpose: define what is in scope and what is not.

Recommended sections:

- Full vision
- Selected delivery target
- Current delivery scope
- Functional requirements or execution requirements
- Non-functional requirements or quality expectations
- Explicit non-goals for the selected delivery scope
- Dependencies
- Risks
- Open questions
- Acceptance criteria

## 03-solution-blueprint.md

Purpose: explain how the project should be implemented or executed.

For software and automation projects, include:

- Recommended technical stack
- Alternative stack options and trade-offs
- Architecture overview
- Main modules
- Data model or storage needs
- External services and integrations
- Security, privacy, and permissions
- Deployment and operating environment
- Testing and verification strategy

For non-software projects, include:

- Execution model
- Process stages
- Roles and responsibilities
- Required resources
- Tools and assets
- Timeline
- Risks and mitigations
- AI or automation opportunities

## 04-task-and-ai-handoff.md

Purpose: convert the confirmed plan into execution tasks and AI-agent handoffs when relevant.

For software, automation, or digital projects, use `ai-coding-task-template.md`.

For non-software projects, use the same discipline but adapt labels:

- Task ID
- Objective
- Context
- Inputs
- Steps
- Output
- Acceptance criteria
- Dependencies
- Suggested tool or owner

Include AI-agent prompts only for tasks where an AI assistant, coding agent, or automation tool is useful.

## Final Chat Summary After Writing

After creating or updating documents, summarize:

- Exact directory path
- Each document and its purpose
- The most important decisions captured
- What to review first
- How to use the documents with AI assistants, coding agents, or execution tools

When summarizing scope, match the user's selected delivery target. Use "Demo scope", "MVP scope", "V1 scope", "current delivery scope", or "full roadmap" as appropriate. Do not call the scope "MVP" unless the user chose or accepted MVP.

Example guidance:

```text
Use 00-project-blueprint.md as the overview and 04-task-and-ai-handoff.md as the action checklist. For software or automation work, attach 03-solution-blueprint.md as implementation context and give Task 001 to your preferred AI coding tool or coding agent.
```

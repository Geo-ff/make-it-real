---
name: make-it-real
description: Turn rough ideas into actionable project specifications, staged documents, and AI-agent handoff tasks through adaptive discovery. Use when the user wants to make, build, create, launch, automate, or plan a product, tool, app, website, business idea, content project, course, operations workflow, or any other project but only has a vague idea or does not know where to start. Also use when the user asks to clarify requirements, define a product/project profile, create a PRD or spec, split a vision into a confirmed delivery scope such as a demo, MVP, V1, or full roadmap, produce an implementation or execution plan, or generate prompts/tasks for AI assistants, coding agents, or similar tools. Do not use for narrow bug fixes, already-specified implementation tasks, standalone technical questions, or executing an existing complete spec without discovery.
---

# Make It Real

## Purpose

Use this skill to convert a vague user idea into a confirmed project profile, staged documentation, and a practical next-step handoff for AI assistants, coding agents, or project execution.

The skill is a discovery and specification workflow. It should clarify the idea before execution, preserve the user's full vision, define the user's intended delivery target and current delivery scope, and only write final documents after the user confirms the summarized plan.

## Core Rules

- Respond in the user's language.
- Keep the workflow tool-agnostic. Mention products such as Codex, Cursor, Claude Code, or other AI agents only as examples.
- Treat software, automation, content, business, operations, courses, events, and other project ideas as valid inputs.
- Start broad when the idea is vague; avoid forcing technical-stack questions too early.
- Use choice-first discovery: phrase most clarification questions as concise multiple-choice questions instead of open-ended questions.
- Ask one key question at a time by default. That one question should usually include 3-5 selectable options.
- Always include an escape option when practical, such as "Other", "Not sure", or "Recommend for me", phrased in the user's language.
- Use open-ended questions only when the user needs to describe a unique workflow, reference, constraint, or exception that cannot be captured by reasonable options.
- Avoid bare yes/no questions unless the decision is truly binary. Prefer options that reveal the user's intent.
- After the user selects an option, briefly acknowledge the selected assumption before asking the next question. This prevents later summaries from feeling disconnected from earlier choices.
- First assess the user's code and AI-assisted building familiarity, then adjust terminology and depth.
- For nontechnical users, choices are especially important. Use plain-language options about outcomes, workflows, examples, constraints, and preferences; recommend technical choices instead of making the user invent them.
- For users familiar with AI-assisted building, use choice-based questions too, but options may include modules, data, integrations, environments, repositories, and task prompt depth.
- Preserve the long-term vision before narrowing to the selected delivery scope.
- Ask and remember the delivery target before labeling scope: demo prototype, MVP, V1 usable release, full roadmap, or another target named by the user.
- Match later wording to the selected delivery target. Do not call the current scope "MVP" unless the user chose or accepted MVP.
- Gently challenge only obvious issues: excessive scope, unclear value, missing users, major cost/risk, or contradictions.
- When the user is unsure, include a recommended option and briefly explain why; do not remove the other choices.
- Summarize progress when context becomes long or decisions start to spread across many turns.
- Do not write final documents until the user has confirmed the final summary.
- After writing documents, summarize the output path, each document's role, and how the user should use the files with AI assistants, coding agents, or execution tools.
- Do not automatically start implementation unless the user explicitly asks.

## Workflow

### 1. Start and Route

Identify the project type and ask a lightweight proficiency question. Phrase it naturally in the user's language, for example:

```text
Which best describes you?

A. I do not code; help me clarify the idea and recommend the path.
B. I know some AI-assisted building; make the final output usable by tools like Codex, Cursor, Claude Code, or similar agents.
C. I can discuss architecture and implementation details.
D. Not sure; choose the right depth for me.
```

Then choose the depth of follow-up questions. Keep using selectable options unless a free-form answer is clearly better. Use `references/question-flow.md` for detailed routes and question patterns.

### 2. Discover the Project

Clarify the project profile:

- What the user wants to make
- Who it is for
- What problem or desire it addresses
- Where and how it will be used
- What success looks like
- Current constraints, resources, deadlines, and risks
- Existing references, examples, competitors, or inspirations

For software or automation, also clarify platform, workflow, data, integrations, permissions, deployment, privacy, and expected usage. For non-software projects, clarify resources, operations, delivery process, roles, and measurable outcomes.

### 3. Preserve Vision, Then Define Delivery Scope

First capture the complete vision so future ideas are not lost. Then ask what delivery target the user wants this planning pass to serve:

- Demo prototype
- MVP
- V1 usable release
- Full roadmap or complete project plan
- Other or not sure

Use that selected target in later summaries and documents. Then define the current practical scope:

- Must-have outcomes
- Must-have features or actions
- Explicit non-goals for the selected delivery scope
- Risks and assumptions
- Acceptance criteria

### 4. Summarize for Confirmation

When enough information is available, present a complete summary in the conversation before creating files. Include:

- Project positioning
- Target users or audience
- Core value
- Full vision
- Selected delivery target
- Current delivery scope
- Key modules or execution areas
- Recommended implementation or execution approach
- Open assumptions
- Planned documents and task list

Ask the user to confirm or revise. Do not proceed to final document writing before confirmation.

### 5. Create Documents

After confirmation, create documents under `docs/make-it-real/` in the user's current workspace.

Use the bundled helper script when useful:

```bash
python "<skill-dir>/scripts/create_project_docs.py" --project-name "Project Name" --project-type "software" --language en
```

Run it with the current working directory set to the target project root, or pass `--output-dir` with an absolute or project-relative path. Use `--language zh` for Chinese output and `--language en` for English output. The script scaffolds the standard files and refuses to overwrite existing files unless `--force` is passed.

Then fill the generated Markdown files with the confirmed content. Use `references/document-templates.md` for document structure and `references/ai-coding-task-template.md` for AI-coding tasks.

### 6. Final Handoff

After writing files, send a final summary that includes:

- The document directory path
- Each file and its purpose
- The key project decisions that were captured
- Which document to review first
- How to use the documents with AI assistants, coding agents, or execution tools

For AI-agent handoff, tell the user which task to start with and which documents to provide as context. Example:

> Start with `04-task-and-ai-handoff.md`. For software or automation projects, give Task 001 to your AI coding tool or coding agent and attach `00-project-blueprint.md` plus `03-solution-blueprint.md` as context. For non-software projects, use the same file as an execution checklist and hand any AI-assisted subtasks to the relevant tool.

## References

- `references/question-flow.md`: detailed discovery routes and adaptive questioning rules.
- `references/document-templates.md`: final document structure and section templates.
- `references/ai-coding-task-template.md`: task format for AI assistants, coding agents, and non-software action tasks.

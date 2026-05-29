# Make It Real

[中文说明](README.zh-CN.md)

**From a vague idea to a build-ready spec.**

Make It Real is a portable AI-agent skill that helps users turn rough ideas into clear project definitions, delivery scopes, implementation notes, and AI-agent handoff tasks.

It is designed for the moment when someone says, "I want to build something, but I do not know how to start." The skill guides an AI assistant through adaptive, choice-first discovery so the user does not need to already understand product management, software architecture, or prompt design.

## Why It Exists

AI coding tools have made implementation easier, but unclear ideas still produce unclear projects. Make It Real focuses on the missing step between inspiration and execution:

- What exactly are we making?
- Who is it for?
- What should the first deliverable include?
- What should be saved for later?
- What should a coding agent, AI assistant, or human executor do next?

## What It Produces

By default, the skill creates staged Markdown documents under `docs/make-it-real/`:

| File | Purpose |
| --- | --- |
| `00-project-blueprint.md` | One-page overview of the project, value, users, delivery target, and decisions. |
| `01-product-profile.md` | Product/project positioning, target users, scenarios, references, constraints, and success signals. |
| `02-scope-and-requirements.md` | Current delivery scope, non-goals, requirements, acceptance criteria, risks, and assumptions. |
| `03-solution-blueprint.md` | Recommended implementation or execution approach, architecture, data, integrations, and operations. |
| `04-task-and-ai-handoff.md` | Task list and prompts that can be handed to coding agents, AI assistants, or execution tools. |

## Who It Helps

- Nontechnical founders, operators, creators, and students who have an idea but need structure.
- Vibe coders and AI-assisted builders who want clearer tasks before opening a coding tool.
- Product-minded developers who want a lightweight discovery workflow before implementation.
- Agents that need a repeatable way to clarify vague project requests before writing files or code.

## How It Works

1. Ask the user a small number of choice-first questions.
2. Adapt the depth based on the user's coding and AI-tool familiarity.
3. Preserve the full long-term vision before narrowing the current delivery target.
4. Define a selected delivery target such as Demo, MVP, V1, full roadmap, or another user-defined target.
5. Summarize the plan in chat and ask for confirmation.
6. Write final documents only after the user confirms.
7. Explain where the documents are, what each one is for, and how to use them with AI/coding tools.

## Supported Entry Points

This repository is structured as a cross-platform skill/plugin package:

```text
.
├── .codex-plugin/
│   └── plugin.json
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── .cursor-plugin/
│   └── plugin.json
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── gemini-extension.json
└── skills/
    └── make-it-real/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        │   ├── ai-coding-task-template.md
        │   ├── document-templates.md
        │   └── question-flow.md
        └── scripts/
            └── create_project_docs.py
```

The canonical skill source is `skills/make-it-real/SKILL.md`.

## Installation

### Codex

Use the repository as a plugin package, or copy `skills/make-it-real/` into your Codex skills directory.

### Claude / Claude Code

Use the repository as a plugin package if your Claude environment supports plugins. Otherwise, add `skills/make-it-real/SKILL.md` and the relevant files under `skills/make-it-real/references/` as project instructions.

### Cursor

Use `.cursor-plugin/plugin.json` as the plugin entry point when your Cursor setup supports plugin packages. Otherwise, reference `skills/make-it-real/SKILL.md` in your agent instructions.

### Gemini

Use `gemini-extension.json` with `GEMINI.md` as the context entry point.

### Generic AI Agents

Use `AGENTS.md` as the root instruction file and point the agent to `skills/make-it-real/SKILL.md`.

## Usage

Example prompts:

```text
Use $make-it-real to help me turn my rough idea for a personal finance app into a clear project plan and task handoff.
```

```text
I want to build a PPT generation tool, but I only have a rough idea. Help me clarify it and create docs I can give to a coding agent.
```

```text
Use Make It Real to turn this vague product idea into a confirmed V1 scope and AI-agent task list.
```

## Document Scaffolding Script

The bundled script creates the standard project document skeleton:

```bash
python skills/make-it-real/scripts/create_project_docs.py --project-name "Project Name" --project-type "software" --language en
```

Use `--language zh` for Chinese headings. The script writes to `docs/make-it-real/` by default and refuses to overwrite existing files unless `--force` is passed.

## Validation

If you have the Codex skill creator tools installed, validate the skill folder with:

```bash
python path/to/quick_validate.py skills/make-it-real
python -m py_compile skills/make-it-real/scripts/create_project_docs.py
```

For Codex plugin validation, validate the repository root as a plugin package with the plugin creator tooling when available.

## License

MIT

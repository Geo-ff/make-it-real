# Make It Real

[中文说明](README.zh-CN.md)

Make It Real is a portable AI-agent skill for turning rough ideas into clear project specifications, delivery scopes, and task handoffs.

It is useful when a user wants to build, launch, automate, write, teach, operate, or plan something but only has a vague starting idea. The skill guides the AI assistant through adaptive questioning, preserves the full vision, defines a practical delivery target, and produces documents that can be used by coding agents or execution tools.

## What It Does

- Clarifies vague ideas through choice-first questioning.
- Adapts to nontechnical users, AI-assisted builders, and technical users.
- Supports software, automation, content, course, business, operations, event, and mixed projects.
- Separates full vision from the selected delivery target: demo, MVP, V1, full roadmap, or another target.
- Produces staged project documents under `docs/make-it-real/`.
- Creates task handoffs for AI assistants, coding agents, or human execution.

## Skill Contents

```text
make-it-real/
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

## Installation

For Codex or another tool that supports skill folders, copy the `make-it-real/` directory into that tool's skill directory.

For tools that do not have a native skill system, attach or reference `make-it-real/SKILL.md` and the relevant files under `make-it-real/references/` as agent instructions.

## Usage

In Codex-style skill invocation:

```text
$make-it-real
```

Example prompt:

```text
Use $make-it-real to help me turn my rough idea for a personal finance app into a clear project plan and task handoff.
```

## Document Scaffolding Script

The bundled script creates the standard project document skeleton:

```bash
python make-it-real/scripts/create_project_docs.py --project-name "Project Name" --project-type "software" --language en
```

Use `--language zh` for Chinese headings. The script writes to `docs/make-it-real/` by default and refuses to overwrite existing files unless `--force` is passed.

## Validation

If you have the Codex skill creator tools installed, validate the skill folder with:

```bash
python path/to/quick_validate.py make-it-real
python -m py_compile make-it-real/scripts/create_project_docs.py
```

## License

MIT

# Make It Real 中文说明

[English](README.md)

Make It Real 是一个可移植的 AI agent skill，用来把模糊想法梳理成清晰的项目规格、交付范围和任务交接文档。

当用户只是有一个大概想法，比如想做一个产品、工具、课程、自动化流程、运营项目或其他事情，但不知道如何开始时，这个 skill 会引导 AI 助手通过选择题优先的方式逐步追问，明确完整愿景、当前交付目标和后续执行任务。

## 它能做什么

- 用选择题优先的方式降低用户表达成本。
- 适配完全不懂代码、懂一点 AI 辅助开发、以及能讨论技术细节的用户。
- 支持软件、自动化、内容、课程、商业、运营、活动和混合型项目。
- 区分完整愿景和当前交付目标，例如 Demo、MVP、V1、完整路线图或其他目标。
- 默认在 `docs/make-it-real/` 下生成分阶段项目文档。
- 产出可交给 AI 助手、编码 agent 或执行者使用的任务交接清单。

## Skill 目录结构

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

## 安装方式

如果你的工具支持 skill 目录，例如 Codex 或类似 AI agent 工具，把 `make-it-real/` 目录复制到对应的 skills 目录即可。

如果你的工具没有原生 skill 系统，可以把 `make-it-real/SKILL.md` 以及 `make-it-real/references/` 下相关文件作为 agent 指令或上下文提供给工具使用。

## 使用方式

在支持 Codex 风格 skill 调用的工具中，可以这样使用：

```text
$make-it-real
```

示例：

```text
Use $make-it-real to help me turn my rough idea for a personal finance app into a clear project plan and task handoff.
```

中文也可以直接这样描述：

```text
使用 make-it-real，帮我把一个模糊的记账小程序想法梳理成项目方案和任务交接文档。
```

## 文档骨架脚本

内置脚本可以生成标准文档骨架：

```bash
python make-it-real/scripts/create_project_docs.py --project-name "项目名称" --project-type "software" --language zh
```

脚本默认写入 `docs/make-it-real/`，并且默认不会覆盖已有文件；如果确实需要覆盖，可以加 `--force`。

## 校验方式

如果你安装了 Codex skill creator 工具，可以这样校验：

```bash
python path/to/quick_validate.py make-it-real
python -m py_compile make-it-real/scripts/create_project_docs.py
```

## 许可证

MIT

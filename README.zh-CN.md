# Make It Real 中文说明

[English](README.md)

**把一个模糊想法，变成可以交给 AI 或开发工具执行的项目方案。**

Make It Real 是一个可移植的 AI-agent skill，用来把粗略想法梳理成清晰的项目定义、交付范围、实现思路和任务交接文档。

它适合用户说出“我想做一个东西，但不知道怎么开始”的场景。用户不需要先懂产品经理方法、软件架构或提示词设计；这个 skill 会引导 AI 助手通过选择题优先的方式逐步追问，把想法补全到可以执行的程度。

## 为什么需要它

AI 编码工具降低了实现门槛，但模糊的想法仍然会产出模糊的项目。Make It Real 解决的是“有想法”和“开始执行”之间缺失的那一步：

- 到底要做什么？
- 给谁使用？
- 第一版应该包含什么？
- 哪些东西应该先放到后续路线图？
- 编码 agent、AI 助手或执行者下一步应该做什么？

## 它会产出什么

默认情况下，skill 会在 `docs/make-it-real/` 下生成分阶段 Markdown 文档：

| 文件 | 作用 |
| --- | --- |
| `00-project-blueprint.md` | 项目总览，记录项目价值、用户、交付目标和关键决策。 |
| `01-product-profile.md` | 产品/项目画像，记录定位、用户、场景、参考案例、约束和成功信号。 |
| `02-scope-and-requirements.md` | 当前交付范围、非目标、需求、验收标准、风险和假设。 |
| `03-solution-blueprint.md` | 推荐实现或执行方案，包括架构、数据、集成、部署和运营方式。 |
| `04-task-and-ai-handoff.md` | 可交给编码 agent、AI 助手或执行工具的任务清单和提示词。 |

## 适合谁使用

- 有想法但缺少结构的非技术用户、创业者、运营者、创作者和学生。
- 想通过 AI 辅助开发，但需要先把需求说清楚的 vibe coding 用户。
- 希望在编码前快速做轻量需求澄清的开发者。
- 需要在写代码或写文件前先澄清模糊项目请求的 AI agent。

## 工作方式

1. 用少量选择题优先的问题降低用户表达成本。
2. 根据用户对代码和 AI 工具的熟悉程度调整追问深度。
3. 先保留长期完整愿景，再收敛当前交付目标。
4. 明确当前交付目标，例如 Demo、MVP、V1、完整路线图或用户自定义目标。
5. 在对话中总结方案，并让用户确认。
6. 只有在用户确认后才写入最终文档。
7. 写入后总结文档路径、每个文档的作用，以及如何配合 AI/编码工具使用。

## 支持的入口

当前仓库已经按跨平台 skill/plugin 包组织：

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

标准 skill 源文件是 `skills/make-it-real/SKILL.md`。

## 安装方式

### Claude Code

从稳定版本标签安装：

```text
/plugin marketplace add Geo-ff/make-it-real@v0.1.0
/plugin install make-it-real@make-it-real
```

如果想使用默认分支的最新版本，可以去掉标签，添加 `Geo-ff/make-it-real`。

安装后，直接让 Claude Code 使用 Make It Real 来澄清模糊想法即可。在直接暴露插件命名空间的 Claude Code 环境中，skill 命名空间是 `make-it-real:make-it-real`。

### Gemini CLI

从稳定版本标签安装：

```bash
gemini extensions install https://github.com/Geo-ff/make-it-real --ref v0.1.0
```

如果想安装默认分支的最新版本：

```bash
gemini extensions install https://github.com/Geo-ff/make-it-real
```

### Codex

如果你的 Codex 环境支持插件包，可以把整个仓库作为插件包使用。也可以直接把 `skills/make-it-real/` 复制到 Codex 的 skills 目录。

Bash 示例：

```bash
git clone https://github.com/Geo-ff/make-it-real.git /tmp/make-it-real
mkdir -p ~/.codex/skills
cp -R /tmp/make-it-real/skills/make-it-real ~/.codex/skills/
```

PowerShell 示例：

```powershell
git clone https://github.com/Geo-ff/make-it-real.git "$env:TEMP\make-it-real"
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse -Force "$env:TEMP\make-it-real\skills\make-it-real" "$env:USERPROFILE\.codex\skills\make-it-real"
```

### Cursor

如果你的 Cursor 环境支持插件包，可以使用 `.cursor-plugin/plugin.json` 作为入口。否则，在 agent 指令中引用 `skills/make-it-real/SKILL.md`。

### 通用 AI Agent

使用 `AGENTS.md` 作为根级说明文件，并让 agent 读取 `skills/make-it-real/SKILL.md`。

## 发布版本

第一个稳定标签是 `v0.1.0`。

需要可复现安装时使用标签；需要最新改动时使用默认分支。

## 使用示例

英文示例：

```text
Use $make-it-real to help me turn my rough idea for a personal finance app into a clear project plan and task handoff.
```

中文示例：

```text
使用 Make It Real，帮我把一个模糊的记账小程序想法梳理成项目方案和任务交接文档。
```

```text
我想做一个 PPT 生成工具，但现在只有粗略想法。请先帮我澄清需求，再产出可以交给编码 agent 的文档。
```

## 文档骨架脚本

内置脚本可以生成标准文档骨架：

```bash
python skills/make-it-real/scripts/create_project_docs.py --project-name "项目名称" --project-type "software" --language zh
```

脚本默认写入 `docs/make-it-real/`，并且默认不会覆盖已有文件；如果确实需要覆盖，可以加 `--force`。

## 校验方式

如果你安装了 Codex skill creator 工具，可以这样校验：

```bash
python path/to/quick_validate.py skills/make-it-real
python -m py_compile skills/make-it-real/scripts/create_project_docs.py
```

如果要校验 Codex 插件包，可以在有 plugin creator 工具的环境中对仓库根目录进行插件校验。

## 许可证

MIT

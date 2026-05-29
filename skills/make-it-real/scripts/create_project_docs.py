#!/usr/bin/env python3
"""Create the standard make-it-real project document skeleton."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import sys


@dataclass(frozen=True)
class DocSpec:
    filename: str
    title_en: str
    title_zh: str
    purpose_en: str
    purpose_zh: str
    sections_en: tuple[str, ...]
    sections_zh: tuple[str, ...]


DOCS: tuple[DocSpec, ...] = (
    DocSpec(
        "00-project-blueprint.md",
        "Project Blueprint",
        "项目总览",
        "Fast overview and handoff entry point.",
        "用于快速回顾项目并作为交接入口。",
        (
            "Project Name",
            "One-Sentence Summary",
            "Project Type",
            "Target User or Audience",
            "Core Problem or Opportunity",
            "Core Value Proposition",
            "Full Vision",
            "Selected Delivery Target",
            "Current Delivery Scope Summary",
            "Recommended Approach",
            "Key Risks and Assumptions",
            "Document Map",
            "Suggested First Next Step",
        ),
        (
            "项目名称",
            "一句话总结",
            "项目类型",
            "目标用户或受众",
            "核心问题或机会",
            "核心价值",
            "完整愿景",
            "已选择的交付目标",
            "当前交付范围摘要",
            "推荐方案",
            "关键风险与假设",
            "文档地图",
            "建议优先执行的下一步",
        ),
    ),
    DocSpec(
        "01-product-profile.md",
        "Product Profile",
        "产品/项目画像",
        "Clarifies who the project serves and why it matters.",
        "明确项目服务对象、使用场景和价值。",
        (
            "Target Users or Audience",
            "Primary Scenarios",
            "Pain Points, Desires, or Workflows",
            "References and Alternatives",
            "Success Criteria",
            "User or Operating Journey",
            "Positioning",
            "Constraints",
        ),
        (
            "目标用户或受众",
            "核心场景",
            "痛点、需求或流程",
            "参考对象与替代方案",
            "成功标准",
            "用户旅程或执行旅程",
            "定位",
            "约束条件",
        ),
    ),
    DocSpec(
        "02-scope-and-requirements.md",
        "Scope and Requirements",
        "范围与需求",
        "Defines the full vision, selected delivery target, current delivery scope, requirements, and non-goals.",
        "定义完整愿景、已选择的交付目标、当前交付范围、需求和暂不做事项。",
        (
            "Full Vision",
            "Selected Delivery Target",
            "Current Delivery Scope",
            "Requirements",
            "Quality Expectations",
            "Explicit Non-Goals for Selected Scope",
            "Dependencies",
            "Risks",
            "Open Questions",
            "Acceptance Criteria",
        ),
        (
            "完整愿景",
            "已选择的交付目标",
            "当前交付范围",
            "需求列表",
            "质量预期",
            "当前范围暂不做事项",
            "依赖项",
            "风险",
            "待确认问题",
            "验收标准",
        ),
    ),
    DocSpec(
        "03-solution-blueprint.md",
        "Solution Blueprint",
        "实现/执行方案",
        "Explains the implementation or execution approach.",
        "说明项目的实现方式或执行路径。",
        (
            "Recommended Approach",
            "Alternative Options and Trade-Offs",
            "Architecture or Execution Model",
            "Main Modules or Workstreams",
            "Data, Resources, or Assets",
            "Integrations or Tools",
            "Security, Privacy, or Operating Constraints",
            "Deployment, Launch, or Delivery Plan",
            "Testing and Verification Strategy",
        ),
        (
            "推荐方案",
            "备选方案与取舍",
            "架构或执行模型",
            "主要模块或工作流",
            "数据、资源或资产",
            "集成或工具",
            "安全、隐私或执行约束",
            "部署、发布或交付计划",
            "测试与验证策略",
        ),
    ),
    DocSpec(
        "04-task-and-ai-handoff.md",
        "Task and AI Handoff List",
        "任务与 AI 交接清单",
        "Breaks the plan into execution tasks and AI-agent handoffs when relevant.",
        "将方案拆成执行任务，并在适用时整理成可交给 AI 助手、编码工具或类似 agent 的任务。",
        (
            "Task Overview",
            "Task Ordering",
            "TASK-001",
            "TASK-002",
            "TASK-003",
            "Verification Plan",
            "How to Use These Tasks with AI Assistants or Agents",
        ),
        (
            "任务概览",
            "任务顺序",
            "TASK-001",
            "TASK-002",
            "TASK-003",
            "验证计划",
            "如何把这些任务交给 AI 助手、编码工具或类似 agent 使用",
        ),
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create the standard docs/make-it-real Markdown skeleton."
    )
    parser.add_argument(
        "--project-name",
        default="Untitled Project",
        help="Project name to write into each document.",
    )
    parser.add_argument(
        "--project-type",
        default="Project",
        help="Project type, such as software, automation, course, or business.",
    )
    parser.add_argument(
        "--output-dir",
        default="docs/make-it-real",
        help="Output directory, relative to the current working directory unless absolute.",
    )
    parser.add_argument(
        "--language",
        choices=("en", "zh"),
        default="en",
        help="Language for headings and scaffold text.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing generated files.",
    )
    return parser.parse_args()


def render_doc(spec: DocSpec, project_name: str, project_type: str, language: str) -> str:
    generated_at = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %z")
    if language == "zh":
        title = spec.title_zh
        purpose = spec.purpose_zh
        sections = spec.sections_zh
        labels = {
            "project": "项目",
            "type": "类型",
            "generated": "生成时间",
            "purpose": "文档作用",
            "fill": "待填写",
            "period": "。",
        }
    else:
        title = spec.title_en
        purpose = spec.purpose_en
        sections = spec.sections_en
        labels = {
            "project": "Project",
            "type": "Type",
            "generated": "Generated",
            "purpose": "Purpose",
            "fill": "To be filled",
            "period": ".",
        }

    lines = [
        f"# {title}",
        "",
        f"- **{labels['project']}**: {project_name}",
        f"- **{labels['type']}**: {project_type}",
        f"- **{labels['generated']}**: {generated_at}",
        f"- **{labels['purpose']}**: {purpose}",
        "",
    ]
    for section in sections:
        lines.extend((f"## {section}", ""))
        if spec.filename == "00-project-blueprint.md" and section in ("Document Map", "文档地图"):
            lines.extend(render_document_map(language))
        else:
            lines.append(f"{labels['fill']}{labels['period']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_document_map(language: str) -> list[str]:
    if language == "zh":
        return [
            "- [00-project-blueprint.md](00-project-blueprint.md): 项目总览和交接入口。",
            "- [01-product-profile.md](01-product-profile.md): 产品/项目画像。",
            "- [02-scope-and-requirements.md](02-scope-and-requirements.md): 范围、需求、交付目标和验收标准。",
            "- [03-solution-blueprint.md](03-solution-blueprint.md): 实现或执行方案。",
            "- [04-task-and-ai-handoff.md](04-task-and-ai-handoff.md): 执行任务清单，以及适用时的 AI 助手或编码 agent 交接任务。",
        ]
    return [
        "- [00-project-blueprint.md](00-project-blueprint.md): overview and handoff entry point.",
        "- [01-product-profile.md](01-product-profile.md): product or project profile.",
        "- [02-scope-and-requirements.md](02-scope-and-requirements.md): scope, requirements, delivery target, and acceptance criteria.",
        "- [03-solution-blueprint.md](03-solution-blueprint.md): implementation or execution plan.",
        "- [04-task-and-ai-handoff.md](04-task-and-ai-handoff.md): execution tasks and AI-agent handoffs when relevant.",
    ]


def main() -> int:
    args = parse_args()
    output_dir = Path(args.output_dir).expanduser()
    existing = [output_dir / spec.filename for spec in DOCS if (output_dir / spec.filename).exists()]

    if existing and not args.force:
        print("Refusing to overwrite existing files:", file=sys.stderr)
        for path in existing:
            print(f"  {path}", file=sys.stderr)
        print("Pass --force to overwrite these files.", file=sys.stderr)
        return 2

    output_dir.mkdir(parents=True, exist_ok=True)

    created: list[Path] = []
    for spec in DOCS:
        path = output_dir / spec.filename
        path.write_text(
            render_doc(spec, args.project_name, args.project_type, args.language),
            encoding="utf-8",
            newline="\n",
        )
        created.append(path)

    print(f"Created make-it-real documents in: {output_dir}")
    for path in created:
        print(f"  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

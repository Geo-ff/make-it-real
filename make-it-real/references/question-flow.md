# Question Flow

Use this reference when `SKILL.md` needs a concrete discovery route. Adapt wording to the user's language and project type.

## Question Style

Use choice-first questioning. Most questions should be easy to answer by selecting an option.

Default format:

```text
<one short question>

A. <common option>
B. <common option>
C. <common option>
D. Other / not sure / recommend for me
```

Rules:

- Prefer 3-5 options.
- Include "Other", "Not sure", or "Recommend for me" when practical.
- For nontechnical users, options should describe real-world outcomes or behaviors, not technical implementation.
- For users familiar with AI-assisted building, options can include implementation details, but still provide an escape option.
- Keep each option short enough to scan.
- Ask only one decision at a time unless the user has already provided clear context.
- After the user picks an option, briefly restate the selected direction before asking the next question.
- Use open-ended questions only for unique workflows, unusual constraints, references, or details that options cannot capture.

Examples:

```text
这个记账工具主要给谁用？

A. 只给我自己日常记账
B. 给家庭成员一起记账
C. 给小店、社团或团队一起记账
D. 其他 / 不确定，你来建议
```

```text
第一版最需要帮你解决哪件事？

A. 快速记录收入和支出
B. 看清楚每月钱花到哪里了
C. 看清楚微信、支付宝、银行卡等账户余额
D. 以上都想要，但你帮我排优先级
```

```text
你希望最后的任务清单适合哪种执行方式？

A. 我不懂代码，尽量写成我能交给 AI 助手、编码工具或类似 agent 的指令
B. 我懂一点 AI 辅助开发，任务要能直接交给 AI 编码工具或类似 agent 执行
C. 我懂开发，可以包含架构、接口和数据模型细节
D. 不确定，你按项目情况推荐
```

## Opening Route

1. Ask what the user wants to make if the idea is not yet stated.
2. Classify the project type:
   - Software product, app, website, tool, plugin, game, or SaaS
   - Automation or workflow
   - Content, course, media, or community project
   - Business, operations, service, or offline project
   - Event, campaign, or launch
   - Mixed or unknown
3. Ask about code and AI-assisted building familiarity:
   - Nontechnical: "I do not code; help me clarify the idea and recommend the path."
   - AI-agent aware: "I know some AI-assisted building; help me get a spec and executable tasks for an AI assistant or coding agent."
   - Technical: "I can discuss architecture and implementation details."

Do not ask all three as a rigid form. If the user already provided one answer, move on. Prefer asking this as a multiple-choice question with a "not sure" option.

Recommended template:

```text
你更接近哪种情况？

A. 我不懂代码，希望你帮我把想法讲清楚并推荐方案
B. 我懂一点 AI 辅助开发，希望最后能拿到可交给 AI 编码工具或类似 agent 的任务
C. 我懂开发，可以直接讨论架构、接口、数据模型
D. 不确定，你按项目情况选择提问深度
```

## Universal Discovery Questions

Use these as a question bank, not a checklist to dump at once. Convert them into choice-first questions whenever possible.

- What are you trying to make in one sentence?
- Who is this for?
- What problem, desire, or workflow does it address?
- When would someone use it?
- What should happen before, during, and after the main use case?
- What would make the first version successful?
- What examples, competitors, references, or inspirations should influence it?
- What constraints exist: time, budget, tools, team, platform, compliance, audience, or deadline?
- What should not be included in the first version?
- What assumptions are still unconfirmed?

## Software and Digital Products

Clarify:

- Target platform: web, mobile, desktop, browser extension, CLI, plugin, API, or internal tool
- User roles and permissions
- Core user flows
- Inputs, outputs, and saved data
- Authentication and account needs
- Integrations and external APIs
- Admin or back-office needs
- Data privacy and security expectations
- Deployment target and operating environment
- Analytics, logging, or monitoring needs
- Expected scale and performance concerns

For nontechnical users, avoid asking for a stack first. Recommend a default after understanding the workflow. Keep discovery questions choice-based and translate technical concerns into user-visible behavior.

## Automation and Workflow Projects

Clarify:

- Trigger: what starts the workflow
- Inputs: where data or files come from
- Actions: what should be transformed, sent, generated, or updated
- Outputs: where results go
- Human review points
- Error cases and fallback behavior
- Frequency and volume
- Tools that must be integrated

## Content, Course, and Media Projects

Clarify:

- Target audience
- Promise or transformation
- Format: text, video, slides, newsletter, course, community, podcast, or mixed
- Distribution channel
- Cadence and production workflow
- Required assets and source material
- Monetization or success metrics
- AI or automation opportunities

## Business, Operations, and Offline Projects

Clarify:

- Customer or participant
- Offer or deliverable
- Operating process
- Required people, tools, locations, assets, and vendors
- Timeline and launch path
- Costs and constraints
- Risks, dependencies, and measurable outcomes
- Digital assets or automation that could support the work

## Vision and Delivery Scope Questions

First capture the full vision:

- If everything goes well, what does this become?
- What future capabilities should be remembered but not necessarily built now?

Then ask the delivery target as a choice-first question before using scope labels:

```text
这次你希望先产出哪种版本的方案？

A. Demo 原型：先能演示核心想法
B. MVP：最小可用版本，先验证是否值得继续
C. V1 正式可用版：第一版就希望比较完整、能真实使用
D. 完整产品方案：先把长期路线图和阶段拆分都讲清楚
E. 不确定，你按项目情况推荐
```

After the user chooses, use that label consistently:

- Demo choice: "demo scope" or "prototype scope"
- MVP choice: "MVP scope"
- V1 choice: "V1 scope", "first usable release", or "current delivery scope"
- Full roadmap choice: "full roadmap" plus "phase 1 scope"
- Unsure: recommend a target and state the assumption before continuing

Then narrow the current delivery scope:

- What is the smallest useful version for the selected delivery target?
- What must work inside the selected delivery scope?
- What can be postponed?
- What would prove the idea is worth continuing?
- What would a user do in the first successful session?

## Completion Criteria

Move to the confirmation summary only when these are clear enough:

- One-sentence project definition
- Project type
- Target user or audience
- Core value and main scenario
- Full vision
- Selected delivery target
- Current delivery scope using the selected target's label
- Non-goals for the selected delivery scope
- Recommended implementation or execution direction
- Risks, assumptions, or open questions
- Task breakdown depth needed for the next step

If any item is missing, ask the smallest useful next question.

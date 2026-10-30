# Git Guard：AI Git 协作与人工审核

[官方网站](https://www.relayrun.net/) · [快速开始](docs/zh-CN/README.md) · [配套技能](skills/README.md)

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

[功能建议](https://github.com/relayrun/gitguard/discussions/categories/ideas) · [使用问答](https://github.com/relayrun/gitguard/discussions/categories/q-a) · [问题反馈](https://github.com/relayrun/gitguard/issues/new/choose) · [参与贡献（英文）](docs/CONTRIBUTING.md)

## 一、40 秒了解 Git Guard

https://github.com/user-attachments/assets/57a60816-46f6-4d2c-9d86-fc95f84e8c8b

[下载中文视频 · MP4 · 40 s](https://raw.githubusercontent.com/relayrun/gitguard/main/assets/videos/RelayRun-GitGuard-Intro-zh-CN-v12.mp4)

## 二、AI 做好合并前的准备，人掌握最终决定

**让 AI 高效协作，让人掌控仓库安全。**

**Git Guard 是 [RelayRun](https://www.relayrun.net/) 旗下的开源 Git 协作项目。**它提供**给人看的配置手册、给 AI 用的操作技能，以及配套模板和部署示例**，帮助个人开发者与团队限制 AI 对仓库的高风险操作，把最终审核与合并留给人。

> [!NOTE]
> **协作原则：人发起任务 → AI 在授权范围内执行 → 返回人审核。**

本地或自建部署以 **OneDev** 为主要示例，线上托管提供 **GitHub** 对照指南。配置完成后，日常使用只需几句指令和一次人工网页审核。

适合使用 Git 仓库、让 AI 参与代码或文档修改并希望保留人工把关的个人与团队。**OneDev 和 GitHub 只是配置示例，不限定 Git Guard 的适用平台。**其他 Git 仓库管理平台也可参考相同的协作与保护原则，具体设置和效果需按平台能力验证。

## 三、为什么需要 Git Guard？

AI 能快速修改代码，也可能快速执行一次错误操作：强推覆盖提交历史、误删分支，或者跳过审核直接修改主线。如果 AI 同时拥有管理权限，还可能改变原本用于保护仓库的设置。

只在提示词里写“不要这样做”并不足够。Git Guard 将关键控制落实到**服务器权限、访问入口和独立备份**上，让 AI 做获准的工作，让人保留关键决定和恢复能力。

## 四、它怎样保护仓库？

| 核心措施 | 要达到的效果 |
| --- | --- |
| **保护主分支** | AI 可以按授权推送功能分支，但不能直接推送主线、强推覆盖主线历史或删除受保护分支。 |
| **人工网页创建请求、审核与合并** | AI 准备分支、标题和描述；人进入 OneDev 或 GitHub 网页管理后台，创建合并请求、检查改动，确认后合并。 |
| **限制绕过审核的接口** | 自建 OneDev 示例通过反向代理阻断 REST API，并封住后端直连等绕行入口，避免从其他通道绕过限制。 |
| **分开贡献权限与管理权限** | AI 日常使用受限身份，不持有人工合并、修改保护规则或管理备份的权限，也不借用人的管理会话。 |
| **保留独立恢复副本** | 将资料备份到独立设备或 NAS，保留历史恢复点并检查完整性；完整编译和启动验证可按项目需要选择。 |

> [!WARNING]
> **关键权限边界：**限制 AI 强推、直推主分支和自行合并的权限，并封住 REST 等可能绕过审核的接口，把最终审核和合并留给人。

上述是配置与验收目标，不能仅凭一份手册认定权限已经生效。[OneDev 手册的版本依据](docs/zh-CN/onedev.md#来源与限制)说明了参考版本与限制；[GitHub 指南](docs/zh-CN/github.md)对应其平台自己的规则和权限机制。

## 五、配置项不少，可以让 AI 帮你完成

你可以按手册自行配置，也可以把手册和配套技能交给 AI，让它协助完成。

**推荐通过可见的界面操作（Computer Use）协助配置：**你能看到 AI 在操作什么，按需要授予权限；密码等敏感信息由你输入。配置完成后退出临时管理会话，让 AI 回到日常受限身份。

| 使用方式 | 从这里开始 |
| --- | --- |
| **本地或自建 OneDev** | 主要示例，包含配置步骤、权限边界和常见问题：[OneDev 手册](docs/zh-CN/onedev.md) · [配置与安全验收技能](skills/gitguard-onedev-safety/SKILL.md) |
| **线上 GitHub 托管** | 将相同的协作原则对应到 GitHub 的分支规则、身份和权限：[GitHub 指南](docs/zh-CN/github.md) |
| **其他 Git 仓库管理平台** | 参考[共用协作流程](docs/zh-CN/workflow.md)，将保护目标对应到该平台的身份、分支与接口权限，再按[验收矩阵](docs/zh-CN/security-acceptance.md)核实效果。 |

首次配置按这四件事推进：

1. **明确范围：**确定要保护的仓库、主分支，以及人和 AI 分别使用的身份。
2. **完成配置：**手动操作，或让 AI 按手册在授权范围内协助。
3. **验证保护：**按[安全验收说明](docs/zh-CN/security-acceptance.md)，在获准的隔离测试仓库里验证正常操作可用、禁止操作确实被拒绝。
4. **安排恢复：**退出临时管理会话，配置[独立备份与恢复检查](docs/zh-CN/backup-and-recovery.md)。

这些主要是首次配置工作，日常不需要重复设置；权限、规则或部署环境变化后，再检查受影响的部分。

### 提交前，先检查敏感信息

让 AI 按[公开内容检查手册](docs/zh-CN/public-content-review.md)确定公开范围、选择检查模式，分别检查工作文件、暂存内容和待推送历史。内置工具能提醒疑似密钥、本机路径、内网地址等问题；发现后先处理并复查，再进行已获准的提交或推送。它不会自动删除或替换内容，也不能保证识别所有隐私，图片和视频仍需人工检查。机构专用敏感词或账号清单应放在仓库外的私有配置中，不随源码公开。[AI 日常协作技能](skills/gitguard-workflow/SKILL.md)已给出对应操作要求。

## 六、配置好以后，日常只需四步

可以让 AI 使用[日常协作技能](skills/gitguard-workflow/SKILL.md)，按你项目中的 Git 工作流执行：

| 步骤 | 你做什么 | AI 做什么 |
| --- | --- | --- |
| **① 本地提交** | 发出指令：“请按 Git.md 执行第一步。” | 阅读项目流程，检查本次改动并完成本地提交，此时不上传。 |
| **② 推送与准备** | 发出指令：“请按 Git.md 执行第二步。” | 按授权推送功能分支，准备合并请求的标题、描述和检查结果。 |
| **③ 人工审核合并** | 进入 OneDev 或 GitHub 网页管理后台，创建合并请求；核对源分支和目标分支、填写说明、审查改动与检查结果，确认后合并。 | 提供必要的说明与协助，最终合并由人操作。 |
| **④ 合并后收尾** | 告知：“已合并，请执行后续收尾。” | 核对实际合并结果，同步本地主线，只清理已确认完成的分支。 |

这里的 `Git.md` 指你项目实际采用的 Git 工作流文档，名称可以不同。

**你决定何时提交、何时推送，以及是否合并；AI 处理获准的执行细节。**

[查看完整协作流程](docs/zh-CN/workflow.md)

## 七、可以获得什么？

- **配置手册与快速开始：**理解原理，选择部署方式，逐项完成配置。[阅读中文手册](docs/zh-CN/README.md)
- **两类配套技能：**日常协作与收尾、OneDev 配置与安全验收。[查看技能](skills/README.md)
- **可复用模板：**用于操作交接、合并说明和验收记录。[查看模板](templates/README.md)
- **部署示例：**参考自建 OneDev 的入口限制与部署方式。[查看示例](examples/onedev/README.md)
- **检查与打包工具：**辅助检查公开内容、文档链接和技能包。[查看工具](scripts/README.md)
- **多语言动画与接入说明：**让介绍视频跟随页面语言展示。[查看说明](docs/zh-CN/animation-and-language.md)

## 八、常见问题与使用说明

### 配置好后，每次都要重新设置吗？

不需要。日常按上面的四步使用；身份、权限或部署环境变化后，再检查受影响的配置。

### 只有一个人，也可以使用吗？

可以采用同样的人与 AI 分工，但需要区分临时配置会话与日常受限身份。若平台规则要求另一位审核者，就必须满足该规则。

### 下载技能，就会自动保护仓库吗？

不会。技能指导 AI 如何工作；真正的限制需要在服务器或托管平台上配置，并通过[权限验收](docs/zh-CN/security-acceptance.md)核实。

### 目前有哪些语言和资料？

八种语言均提供介绍、快速开始和完整七份详细手册；翻译仍为审阅稿，不声称已通过母语校阅。各语言的覆盖范围见[文档索引](docs/README.md)。

八种语言首页均已接入对应语言的 40 秒 MP4 视频，无需另选视频语言。

手册、技能和部署示例需要结合你的实际环境使用。文档检查通过，不代表你的仓库已经完成权限配置或通过安全验收。当前网页预览和工作区内容也不等于已发布版本。

第三方素材保留各自的授权说明，视频音效出处见[素材说明](assets/videos/README.md)。

[公开内容检查](docs/zh-CN/public-content-review.md) · [仓库](https://github.com/relayrun/gitguard)

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

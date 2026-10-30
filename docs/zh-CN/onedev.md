# OneDev 配置手册：AI 权限与人工审核

[English](../en/onedev.md) · [简体中文](onedev.md) · [日本語](../ja/onedev.md) · [Deutsch](../de/onedev.md) · [Français](../fr/onedev.md) · [Español](../es/onedev.md) · [Português (Brasil)](../pt-BR/onedev.md) · [Русский](../ru/onedev.md)

[Git Guard 首页](../../README.zh-CN.md) · [快速开始](README.md)

这份手册属于 **RelayRun Git Guard**，介绍如何在自建 OneDev 上分开人和 AI 的权限、保护主分支、限制绕过审核的入口，并保留独立恢复副本。AI 按授权提交和推送工作分支，人在网页后台创建请求、审核并完成最终合并。

**Git Guard 面向使用 Git 仓库的个人与团队，不限于 OneDev。**OneDev 和 GitHub 只是配置示例；其他 Git 仓库管理平台也可参考[共用协作与保护原则](workflow.md)，具体选项和效果需结合平台能力验证。本章演示 OneDev 的设置，GitHub 的对应示例见 [GitHub 指南](github.md)。OneDev 是第三方平台，不是 RelayRun 旗下产品。

审阅稿 0.1。界面与踩坑参考版本：**OneDev 14.1.0**；这是版本化示例，不表示建议未经维护状态核查就安装旧版本。[协作流程](workflow.md) · [安全验收](security-acceptance.md) · [GitHub 对照](github.md)

**本页导航：**[AI 协助配置](#让-ai-通过可见界面协助配置) · [部署](#1-先选择部署边界) · [身份](#2-将操作身份分开) · [分支保护](#3-初始化并保护主分支) · [人工合并](#4-合并请求默认项不能混为权限) · [REST 入口](#5-可选的-rest-入口限制) · [常见问题](#6-两个实际容易混淆的问题) · [验收与恢复](#7-安全验收与恢复) · [来源](#来源与限制)

授权提交或上传前，按公开内容手册[配置并运行检查](public-content-review.md#configure-the-public-content-check)，再[理解和处理检查结果](public-content-review.md#interpret-results-and-handle-findings)。

<a id="visible-ai-assisted-setup"></a>

## 让 AI 通过可见界面协助配置

可以人工配置，也可以让 AI 按本手册和配置技能，通过可见的 Computer Use 界面协助操作。先明确项目、身份、具体选项及回退方式，由人批准本次范围并观看操作；这不表示给 AI 永久或无限的管理权限。

需要管理权限的选项使用专门的、有人监督的临时配置会话。敏感凭据由人输入，不放入聊天、截图或仓库；不得借管理员会话绕过日常操作已遇到的拒绝。完成后回读设置，按授权验收权限，退出提权会话，让 AI 恢复日常受限身份。操作入口不支持的步骤如实交给人完成，不能把未发生的点击说成已操作。

观看界面帮助理解配置，真正的保护来自生效的权限限制及验证。

<a id="1-select-a-deployment-boundary"></a>

## 1. 先选择部署边界

优先使用独立电脑、服务器或架构和容器能力匹配的 NAS。AI 开发身份不应拿到宿主机、容器运行时、数据目录、备份和管理员凭据。同机运行时需要明确限制系统和文件访问，安装 Docker 本身不等于完成隔离。

结合官方安装说明和[参数化部署示例](../../examples/onedev/README.md)，先选定受支持的镜像版本或摘要、独立数据位置、HTTPS 入口及恢复办法。示例只开放回环网关，省略 Docker socket 和后端 HTTP/SSH 直达端口；它是配置起点，不是已经运行验收的生产部署。需要容器构建时，应单独设计执行器权限。

<a id="2-establish-separate-identities"></a>

## 2. 将操作身份分开

| 从哪里进入 | 设置或检查什么 | 怎么核对 |
| --- | --- | --- |
| 管理 → 用户／用户组 | 分开人工审核管理、AI 贡献和只读备份身份 | 实际组成员、凭据、继承权限 |
| 管理 → 角色 | 核对代码、项目管理及其他权限 | 不只看角色名；AI 不应成为项目所有者或能改保护规则 |
| 项目 → 设置 → 授权 → 按用户／按组 | 只授必要项目范围，同时检查父项目 | 备份身份只读正确仓库，AI 权限符合预定模型 |
| 项目 → 设置 → 常规 | 父项目、默认角色和有效继承 | 防止默认或匿名访问、继承所有者权限 |

参考角色中的“管理合并请求”涉及管理或批量操作，关闭它不等于代码写入者绝不可能执行最终合并。要在有效人工审核后，另测 AI 身份是否仍有合并能力。不要让日常 AI 身份接触人工浏览器会话或管理员令牌；前述有人监督、限定范围的配置会话是临时的，不能保留供日常 Git 操作使用。

<a id="3-initialize-and-protect-the-target-branch"></a>

## 3. 初始化并保护主分支

先由人工控制的初始化流程建立目标主分支，再启用阻止创建该分支的规则。不要为了让 AI 初始化或修复仓库而习惯性关闭保护。

进入 **项目 → 设置 → 代码 → 分支保护**，选择目标分支（常见为 `main`）及适用身份（参考配置为 `anyone`）。参考版本按“本级先于父级、第一条匹配规则生效”处理；子级规则可能遮住更严格的父级规则，要检查实际有效规则。

| 选项 | 设置含义与验证 |
| --- | --- |
| 防止强制推送 | 对受保护分支启用；在隔离测试库验证未经允许的历史改写确实被拒绝 |
| 防止删除 | 保护分支；删除整个项目属于另一项权限 |
| 防止创建 | 初始化之后按需要启用；不能代替更新或审查限制 |
| 要求审查者 | 用界面选择独立人工审核者，回读生成表达式及对应账号 |
| 要求构建／提交签名 | 按项目选择，必须有真实执行的检查和受信任签名身份 |
| 文件与标签保护 | 按需要单独设置；分支规则不自动证明标签、发布保护 |

早期参考配置没有要求审查者，后来才补上。防强推**不能阻止普通快进直推**，必须另测普通直推。在参考实现中，指定审核者同时又是 PR 提交人时，审查安排可能不同，因此 AI 与人工身份必须分离。未单独验证最终合并权限前，不能写成“技术上已经只有人能合并”。

配置写入仅在对应授权范围内执行，保存后回读。截图证明配置可见，不能代替拒绝行为实测。

<a id="4-set-pr-defaults-without-confusing-responsibilities"></a>

## 4. 合并请求默认项不能混为权限

进入 **项目 → 设置 → 合并请求**，逐项核对本级设置或父级继承：

- **默认合并策略**：参考使用 Squash；“默认”不等于其他策略被禁止。
- **默认负责人**：分配工作的人，不是分支保护里的要求审查者。
- **合并后删除源分支**：可选收尾，受操作者权限约束，不代表可以批量删旧分支。
- 交接前核对源分支、目标分支、差异、标题和检查；人工审核并执行最终合并，AI 不代点合并或启用自动合并。

Squash 后应结合实际目标主线历史验证内容，不能因为提交编号不同就认为漏代码。按共用流程同步和清理确已完成的分支。

<a id="daily-human-request-creation"></a>

### 日常由人工新建请求

AI 按授权推送分支并准备标题、描述后，人工进入仓库的合并请求页面，新建请求、核对源与目标、填写说明并提交。查看差异和实际检查、审核结果，再由人确认最终合并，见[完整交接流程](workflow.md)。创建人同时是要求审查者时，要核实当前版本的审核规则；需要其他审查者就由另一位获准的人工审核，不能为省步骤降低保护。

<a id="5-optional-rest-ingress-restriction"></a>

## 5. 可选的 REST 入口限制

自建服务可以在网关拒绝 REST 命名空间，同时保留必要网页与 Git 路径，见[网关示例](../../examples/onedev/README.md)。这可能影响集成，需按实际业务选择。

核对后端直达端口、SSH、其他域名、IPv6、隧道、网页会话、服务器任务及容器／宿主机管理途径。代理拒绝一个入口不代表其他途径已隔离。验收应覆盖规范化路径、大小写／编码变体、真实 Git 操作及必要 WebSocket；网络不通不是权限拒绝证据。

<a id="6-two-common-pitfalls"></a>

## 6. 两个实际容易混淆的问题

<a id="pr-source-branch-is-not-suggested"></a>

### 创建 PR 时没有自动推荐源分支

14.1.0 参考逻辑会考虑最近提交的**作者邮箱**是否属于当前登录用户已验证的邮箱。先核对最新提交作者和用户，再到用户的“邮箱地址”设置中添加其确实控制的邮箱，并完成正常验证。管理员添加邮箱的行为不代表普通用户可以跳过验证。

重新打开创建 PR 页面，检查源和目标；手工选择源分支同样有效。修复的是推荐行为，不是自动合并或增加审核权限。不要仅为推荐分支而修改全局 Git 身份或重写历史；显式选择的源分支优先。

<a id="a-ready-pr-remains-marked-work-in-progress"></a>

### 工作已就绪，PR 仍因进行中标记不能合并

参考实现把标题以 `wip` 或 `[wip]` 开头（不区分大小写）识别为进行中，阻止合并；**不是所有英文字母开头都不允许**。这里指 PR 标题，它可能来自提交说明或分支名称。

实际准备完成后才移除该标记；审核、构建及人工最终合并仍须执行。WIP 阻止合并不代表已经验证身份没有合并权限；使用其他版本时重新核查规则。

<a id="7-acceptance-and-recovery"></a>

## 7. 安全验收与恢复

采用[统一验收矩阵](security-acceptance.md)和[记录模板](../../templates/security-acceptance.csv)。先只读盘点，再按具体授权在隔离测试库执行拒绝测试。记录身份、版本、路径、对照、前后状态和实际拒绝原因；原因不明或尚未测试都标为“未验证”。

根据[备份指南](backup-and-recovery.md)保留独立历史恢复点，同时考虑仓库和服务数据、配置。不断更新的一份克隆不是完整 OneDev 备份。编译、启动检查按项目选用，也不能证明服务数据库和附件全部可恢复。

<a id="sources-and-limits"></a>

## 来源与限制

- [官方容器安装](https://docs.onedev.io/installation-guide/run-as-docker-container)与[反向代理说明](https://docs.onedev.io/administration-guide/reverse-proxy-setup)。
- [14.1.0 源分支推荐逻辑](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/web/page/project/pullrequests/create/NewPullRequestPage.java)。
- [14.1.0 WIP 与合并条件](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/PullRequest.java)。
- [分支保护](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/support/code/BranchProtection.java)及[推送检查](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/git/hook/GitPreReceiveCallback.java)。

本教程依据版本化界面记录与源码核查整理；写好教程不等于已安装服务，也不证明其他服务器、角色、NAS 或版本已经通过实测。

**下一步：**配置后按[安全验收矩阵](security-acceptance.md)核实实际权限，再使用[日常四步与收尾流程](workflow.md)。需要整体介绍时，返回 [Git Guard 首页](../../README.zh-CN.md)。

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

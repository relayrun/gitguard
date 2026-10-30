# GitHub：线上托管的简明对照

[English](../en/github.md) · [简体中文](github.md) · [日本語](../ja/github.md) · [Deutsch](../de/github.md) · [Français](../fr/github.md) · [Español](../es/github.md) · [Português (Brasil)](../pt-BR/github.md) · [Русский](../ru/github.md)

[Git Guard 首页](../../README.zh-CN.md) · [快速开始](README.md)

基础指南审阅稿 0.1 — 2026-10-28 核对下列 GitHub 官方资料。

Git Guard 以本地或自建部署的 OneDev 为主要详解示例，GitHub 作为线上平台托管的辅助示例。直接共用[协作流程](workflow.md)、[安全验收](security-acceptance.md)和[备份说明](backup-and-recovery.md)。本章介绍能力如何对应，不宣称任何具体仓库已经配置完成。

| 共用要求 | GitHub 中的对应方式 |
| --- | --- |
| 本地准备和提交 | 常规本地 Git 操作，此时不上传 |
| 获准的远端协作 | 推送功能分支并准备请求说明；默认示例由人工在网页创建 PR |
| 必须审查及主线保护 | 配置适当的分支保护或规则集、审核要求 |
| 阻止强推与删除受保护引用 | 不开放相应允许项，并检查例外 |
| 人工最终合并 | 将 AI 身份和凭据与人工权限分开；不能把审查要求当成专属合并权限 |
| 合并后收尾 | 核对结果、安全同步本地主线，只清理确认完成的分支 |

官方说明：免费套餐的公开仓库可使用受保护分支和分支、标签规则集；私有仓库的可用性取决于套餐。不能由此推导所有高级规则或 Push rulesets 均可用。[分支保护](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) · [规则集](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)。

要求审核不能单独决定审核通过后谁可以合并。需核对传统分支保护的管理员例外、允许身份、规则集绕过名单、应用权限及 AI 能接触的人工凭据。适用组织仓库的推送身份限制可与必须 PR 等规则一起评估，最终用实际身份测试；仓库管理、删除和修改规则也应由人独立控制。

默认示例由人工通过仓库的 PR 创建流程操作：核对 base（目标）与 compare（源）分支，填写标题、描述，提交后检查差异和结果，最后人工合并。所需的独立审核仍应完成，创建 PR 不等于已经审核。另行授权 AI 创建请求的可选方式见[共用流程](workflow.md)。

GitHub 支持自动合并相关功能，但本协作流程将最终执行留给人，不能作为顺手优化自动开启。令牌被称为“受限”，也不代表它只允许推功能分支而一定不能合并。

自建 OneDev 的反向代理示例不能直接变成 GitHub 服务前的代理。应把保护目标映射到 GitHub 自身的身份、规则、应用权限和访问路径。

使用前检查实际套餐、公开性、生效规则和例外，再在获准的隔离环境执行共用验收矩阵。编写本文没有修改仓库设置，也没有执行新的拒绝测试。

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

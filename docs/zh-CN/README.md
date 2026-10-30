# Git Guard 快速开始

[English](../en/README.md) · [简体中文](README.md) · [日本語](../ja/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Español](../es/README.md) · [Português (Brasil)](../pt-BR/README.md) · [Русский](../ru/README.md)

[Git Guard 首页](../../README.zh-CN.md)

首版手册审阅稿 0.2 — 2026-10-28。

授权提交或上传前，按公开内容手册[配置并运行检查](public-content-review.md#configure-the-public-content-check)，再[理解和处理检查结果](public-content-review.md#interpret-results-and-handle-findings)。

## 先选择阅读入口

Git Guard 提供协作流程及保护要求，不会因为阅读文档就安装 Git 服务或改变账号权限。先选定一个项目、受保护主分支，并把 AI 的操作身份与人工审核、管理身份分开。

| 想完成什么 | 阅读内容 |
| --- | --- |
| 准备改动并交给人审核 | [日常协作流程](workflow.md) |
| 确认保护是否真正有效 | [安全验收规范](security-acceptance.md) |
| 留存独立恢复副本 | [备份与恢复](backup-and-recovery.md) |
| 在 GitHub 上采用同一流程 | [GitHub 简明对照](github.md) |
| 准备公开发布的内容 | [公开内容检查](public-content-review.md) |
| 配置自建 OneDev | [OneDev 配置](onedev.md) |
| 接入视频与页面语言 | [动画与语言接入](animation-and-language.md) |

**本地或自建部署以 OneDev 为主要示例**，详述具体界面选项及排障；**线上平台托管以 GitHub 为辅助示例**，介绍对应能力即可。自建 OneDev 也可运行在独立远程服务器或适配的 NAS 上。两个示例共用流程和验收标准，不把其他平台上的同名开关直接当成等效保护。

## 日常使用之前

1. 确定仓库、受保护主分支、允许使用的功能分支，以及各身份能做什么。推送、审核、合并、删除和管理权限分别核对。
2. 自建服务优先放在独立电脑、服务器或支持容器的 NAS 上，核对型号、架构和资源。不给 AI 宿主机、容器、数据目录、管理员凭据和备份管理权限。同机使用时也要限制系统和数据访问；安装 Docker 本身不够。
3. 配置平台保护，先只读检查，再在另行授权的隔离测试库中验证拒绝行为。不要用真实生产库的删库或强推来快速“试一下”。
4. 建立独立同步、完整性检查和受保护的历史恢复点。按项目选择是否编译恢复副本、启动程序或做基础功能验证。
5. 用日常流程完成一项可审阅的改动，由人决定并执行最终合并。

需要协助设置时，可按[可见界面配置说明](onedev.md#让-ai-通过可见界面协助配置)让 AI 操作；人确定范围并监督临时会话，日常 AI 权限仍保持受限。

读过这些步骤不等于通过安全验收。未测试的路径标明“未验证”；尚未完成的设置可以如实记录，不能宣传为已经完整保护。

## 后续入口与实际范围

继续阅读 [OneDev 设置与踩坑](onedev.md)、[技能安装与打包](../../skills/README.md)、[模板](../../templates/README.md)、[部署示例](../../examples/onedev/README.md)和[只读检查工具](../../scripts/README.md)。

这是首版手册审阅稿。工具和示例不会自动安装服务、授予权限或运行备份。部署示例、用户环境权限和恢复结果需要独立验证；编译、启动检查仍为可选。正式发布仍待安排；第三方素材保留各自的授权说明。

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

# 公开内容检查

[English](../en/public-content-review.md) · [简体中文](public-content-review.md) · [日本語](../ja/public-content-review.md) · [Deutsch](../de/public-content-review.md) · [Français](../fr/public-content-review.md) · [Español](../es/public-content-review.md) · [Português (Brasil)](../pt-BR/public-content-review.md) · [Русский](../ru/public-content-review.md)

[Git Guard 首页](../../README.zh-CN.md) · [快速开始](README.md)

审阅稿 0.1。这是可供其他项目复用的公开发布流程。[协作流程](workflow.md)

<a id="configure-the-public-content-check"></a>

## 怎样配置公开内容检查

1. 明确实际项目和拟公开的文件范围。内部记录、凭据、扫描器私有配置和诊断结果都放在公开目录之外。如果开发目录混有私有资料，检查单独的发布副本；不要为了扫描通过而删除原始私有文件。
2. 在 Git Guard 源码或已安装技能自带的参考快照中定位检查脚本。它需要 Python 3.9 或更新版本，只使用标准库，不会自动安装、启动服务或设置服务器权限。用 `--root` 明确指定目标；技能安装目录不是待检查项目。
3. 普通项目使用 `--profile generic`；只有检查本项目公开包的专用目录边界时才用 `--profile gitguard`。内置脚本没有自定义敏感词清单或自动替换功能。机构特有的秘密或账号标识应另用合适的扫描器，并将配置存放在发布目录之外的私有位置，参见[私有匹配清单](#敏感字符串清单必须留在私有位置)。
4. 工作文件、暂存内容和待推送历史分开检查。下列路径均为占位示例，历史范围要改成实际将发出的提交；脚本不会 fetch 或 push。尚未建立 Git 仓库时先检查工作文件，进入暂存和历史阶段后再检查对应范围。只查工作文件不能证明后续提交也安全。

```sh
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic --staged
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic --history origin/main..HEAD
```

<a id="interpret-results-and-handle-findings"></a>

## 怎样理解和处理检查结果

退出码 **0** 表示在已有规则范围内未发现问题；**1** 表示有待审阅的发现；**2** 表示检查未完成。报告只列路径、类别和行号，不回显敏感值。工作文件检查除了 Git 元数据外也包含被忽略文件，因为忽略文件仍可能被误复制进发布包。

规则检查私钥特征、部分 GitHub 令牌格式、网址中的凭据、本机路径、内网地址、部分私有或运行时文件名，以及失效或越界的 Markdown 相对链接；不能识别所有密码和账号。二进制文件需要人工检查，超过 2,000,000 字节的文件不检查内容，文件数量上限为 3,000，单次历史范围上限为 200 个提交。更大的既定范围应分批核查，不能默默跳过。

逐项记录类别、位置、处理判断和复查结果，不复制敏感值。修正公开副本或文件纳入规则，或记录有依据的无害项与人工审阅结果，再复查相关工作区、暂存区和历史。不要全局屏蔽二进制或超限提示。真实凭据泄露需要更换凭据和单独获准的历史修复；此脚本不会修复历史、删除或替换内容。超时或检查未完成不能算通过。

制作 Git Guard 发布包时，先用 `scripts/prepare_release.py` 生成范围明确的公开副本；开发缓存保留在原目录，排除项另行记录。可选的 `--media-review` 参数读取私有复核记录，逐项对应已检查的 PNG/MP4 文件及其准确的 SHA-256。只有文件内容完全匹配时，才将二进制提示列为已复核，并单独报告；文件变化、敏感文本、无法读取或超限仍须处理。退出码 0 可以包含这些有记录的媒体复核，不代表自动完成隐私认证。详见[检查和打包工具说明](../../scripts/README.md)。

<a id="before-a-local-commit"></a>

## 本地提交前

核对实际变动及未跟踪文件，确认内容归属和公开权利。移除内部计划、主机和用户路径、内网地址、令牌、私钥、凭据、客户数据、原始截图日志及无关产品源码；示例使用通用名称和占位值。

检查链接、UTF-8 编码、各语言实际覆盖范围、第三方声明和完成状态。未上线的网站或尚未执行的部署不能写成已经可用；内部验证记录放在发布树之外。

暂存区与工作区分别检查：两者内容可能不同。核对重命名、删除、二进制附件、子模块和符号链接。文档正文干净不代表附件安全，本地提交也不代表获得公开发布授权。

<a id="before-a-push"></a>

## 推送前

明确目标远端和实际待推送提交，检查对应历史快照，包括后来已经删除的文件；只删除当前文件不会抹去历史中的敏感信息。仅检查本次拟推送的标签等其他引用，不让新公开项目误带内部历史。

发现敏感信息已入历史时，停止发布，安排凭据更换和获准的修复；不要自行强推或删除仓库掩盖历史。自动扫描是辅助证据，不是“绝无隐私遗漏”的证明。

<a id="reviewable-release"></a>

## 可审阅的发布范围

记录目标、可见性、文件集、待推送历史、权利及许可证决定、验证和剩余限制，确认已有授权覆盖实际动作，最终合并由人执行。

仓库链接官网时，核对域名、HTTPS 证书、品牌及实际页面。所有语言 README 使用一致的官网目标，链接文字按语言表达；正式发布时核对仓库 Website 字段。手册仍应能够独立使用。

<a id="evidence-levels"></a>

## 验证状态

明确区分：已查看、静态检查通过、行为实测通过、已部署、用户确认。配置截图、扫描通过和传输一致都不是完整安全或恢复证明；权限检查使用同一份[安全验收规范](security-acceptance.md)。

<a id="sensitive-matching-lists-stay-private"></a>

## 敏感字符串清单必须留在私有位置

公开包只包含可复用检查逻辑和虚构测试样例。真实密钥、账号标识、项目专用匹配或替换清单必须留在源码树、技能包、下载文件、截图及待推送 Git 历史之外。包含真实敏感值的检测规则本身也是敏感信息，不能因为它是检查配置就发布；忽略规则不能代替暂存区与历史检查。

使用 Gitleaks 等独立扫描器及私有配置时，仅在运行时从仓库外的私有位置提供文件，不打包清单、不回显匹配值，也不把真实值写入命令行参数或测试样例。诊断文件留在私有位置，分享前去除敏感内容。

本项目附带的检查器为 Git Guard 新编写，不读取已有私有匹配清单，也不专门识别证券或客户账号、任意密码和所有令牌类型。通用特征检查是专用扫描和人工审阅的补充，扫描通过不是完整的机密清除证明；它不执行历史清理。

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

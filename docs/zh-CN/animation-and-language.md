# 动画与语言接入

[English](../en/animation-and-language.md) · [简体中文](animation-and-language.md) · [日本語](../ja/animation-and-language.md) · [Deutsch](../de/animation-and-language.md) · [Français](../fr/animation-and-language.md) · [Español](../es/animation-and-language.md) · [Português (Brasil)](../pt-BR/animation-and-language.md) · [Русский](../ru/animation-and-language.md)

[Git Guard 首页](../../README.zh-CN.md) · [快速开始](README.md)

简短产品介绍依次表达：品牌、仓库风险、经过验证的权限边界、可见的 AI 协助配置、日常四步交接。动画说明方法，不是服务器实测证明。书面流程仍是依据；聊天示例中的 Git.md 指使用者项目实际采用的流程文件。

<a id="homepage-placement-and-language"></a>

## 首页位置与语言

将“40 秒了解 Git Guard”放在 README 的语言列表之后、核心介绍和日常四步之前。英文标题为“Git Guard in 40 seconds”。这是产品概览，不代替完整配置教程。

视频跟随当前 README 的语言：默认英文首页对应英文 MP4，简体中文和日文首页分别对应中文、日文 MP4。不再增加单独的视频语言菜单；切换首页语言，也就选择了对应的视频。德语、法语、西班牙语、巴西葡萄牙语和俄语也已接入各自成片，当前本地文档包包含完整的八语页面与视频对应关系。

<a id="delivery-and-playback"></a>

## 成品与播放方式

- 只分发 MP4。PNG 封面保留为可复用素材，不使用动画 GIF；编辑源稿、共用图形和翻译文本留在制作环境，使用方只接收选定成品。
- 每种语言的 GitHub README 用单独成段的视频附件地址显示内嵌播放器，下方保留 MP4 直接下载链接。视频素材说明列出随仓库提供的 MP4 和语言对应的附件地址；其他 Markdown 阅读器可能只显示链接。
- 仓库 README 不能运行自定义 JavaScript，也不能按浏览器语言或 IP 选片。带链接的封面会跳到文件页，普通 HTML 视频标签会被过滤。更换附件须获得发布授权，并实际验证播放，同时更新 README 与对应表；GitHub 控制播放器，不能保证自动播放、循环或停留片尾。
- 官网先确定页面语言：显式语言网址、记住的人工选择、受支持的浏览器网页语言，最后回退英文。视频随同一页面语言选择，不需要第二个视频语言菜单。缺少相应视频时明确标注英文回退，不能把简体中文标成繁体译本。
- 官网播放器默认静音，点击才启用音效；保留暂停、静音、封面与手动播放，并尊重减少动态效果偏好。默认播完停留片尾，提供重播和可选循环；禁用 JavaScript 时仍有普通 MP4 链接。
- 当前八种语言成品均为 40 秒，只有关键动作音效，没有背景音乐。片尾先完整播放品牌动效，再停留静态商标；不把片头插入片尾。
- 文件名采用 RelayRun-GitGuard-Intro-zh-CN-v12.mp4 及对应的 en、ja、de、fr、es、pt-BR、ru 版本。见[视频资产与音效来源](../../assets/videos/README.md)。

<a id="before-adding-media-to-a-release"></a>

## 加入发布包之前

检查成品画面、文字、元数据及素材使用权；核对音视频完整时长、解码、实际体积与语言链接。实际浏览器播放另做验收，音频数值通过不等于听感通过。内容检查器对二进制或超限文件的提示需要逐项审查，不能因此全局关闭检查。

只分发选定成品与必要署名。制作源稿、内部证据、原始录音和项目管理记录不进入公开文档包。本机阅读预览只近似展示排版，不能当成 GitHub 渲染验收。公开附件上传、官网接入与部署均是另一步操作。

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

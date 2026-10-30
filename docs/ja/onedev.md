# OneDev 設定ガイド：AI の権限と人によるレビュー

[English](../en/onedev.md) · [简体中文](../zh-CN/onedev.md) · [日本語](onedev.md) · [Deutsch](../de/onedev.md) · [Français](../fr/onedev.md) · [Español](../es/onedev.md) · [Português (Brasil)](../pt-BR/onedev.md) · [Русский](../ru/onedev.md)

[Git Guard ホーム](../../README.ja.md) · [クイックスタート](README.md)

この **RelayRun Git Guard** ガイドは、自前の OneDev で人と AI の権限を分離し、main を保護し、レビューを迂回する経路を制限し、独立した復元コピーを保持する方法を説明します。AI は許可範囲内でコミットと作業ブランチの push を行い、人が Web 画面でリクエストを作成、レビューし、最終マージを実行します。

**Git Guard は OneDev 利用者だけでなく、Git リポジトリを使う個人とチーム向けです。**OneDev と GitHub は設定例です。他の Git 管理プラットフォームでも[共通の協業・保護原則](workflow.md)を参照し、その機能に合わせて設定と結果を検証できます。この章は OneDev の設定例で、[GitHub ガイド](github.md)は別の例です。OneDev は第三者のプラットフォームであり、RelayRun 製品ではありません。

レビュー用草案 0.1。UI とトラブルシューティングの参照版は **OneDev 14.1.0** です。特定バージョンの例であり、現在のサポートを確認せず古い版を導入する推奨ではありません。[手順](workflow.md) · [安全性検証](security-acceptance.md) · [GitHub の例](github.md)

**このページ：**[AI による設定支援](#visible-ai-assisted-setup) · [配置](#1-select-a-deployment-boundary) · [アカウント](#2-establish-separate-identities) · [ブランチ保護](#3-initialize-and-protect-the-target-branch) · [人によるマージ](#4-set-pr-defaults-without-confusing-responsibilities) · [REST 入口](#5-optional-rest-ingress-restriction) · [よくある問題](#6-two-common-pitfalls) · [検証と復元](#7-acceptance-and-recovery) · [出典](#sources-and-limits)

許可されたコミットやアップロードの前に、公開内容手順で[検査を設定・実行](public-content-review.md#configure-the-public-content-check)し、[結果を理解して対応](public-content-review.md#interpret-results-and-handle-findings)してください。

<a id="visible-ai-assisted-setup"></a>

## 画面で確認できる AI 設定支援

手動設定のほか、このガイドと設定スキルに従う AI を、操作の見える Computer Use 画面で使えます。最初に対象プロジェクト、操作者、変更する設定、戻し方を特定します。人が範囲を承認して操作を見られるようにし、隠れた管理者権限や永続的な権限付与を含めません。

管理設定には、対象の変更のために指定した監督下の一時セッションを使います。人が機密資格情報を入力し、チャット、画面写真、リポジトリに残しません。日常操作の拒否を管理者セッションで迂回してはいけません。終了時に設定を読み返し、適切な範囲の検証を行い、昇格セッションを終了し、制限された日常アカウントへ戻します。利用可能な画面で必要な操作ができなければ報告して人に任せ、実行していないクリックを報告しません。

画面の観察は設定の理解を助けます。保護を実現するのは強制された権限と、その検証です。

<a id="1-select-a-deployment-boundary"></a>

## 1. 配置の境界を選ぶ

選んだ OneDev 版のアーキテクチャとコンテナ要件に適合する独立 PC、サーバー、NAS を優先します。サーバー、コンテナ実行環境、ストレージ、バックアップ、管理者資格情報を AI の開発アカウントから分離します。同一ホストで使うなら明示的な OS・ファイル権限が必要で、Docker だけでは分離になりません。

公式導入ガイドと[パラメーター化された例](../../examples/onedev/README.md)を使います。対応するイメージ版・ダイジェスト、独立したデータ保存先、TLS 入口、復元方法を決めてから起動します。例はループバックのゲートウェイだけを公開し、Docker ソケットを渡さず、直接 HTTP/SSH のホストマッピングを無効にしています。これは出発点となる設定であり、検証済み本番環境ではありません。コンテナを使うビルドには別設計の実行環境が必要になる場合があります。

<a id="2-establish-separate-identities"></a>

## 2. 別々のアカウントを用意する

| 確認する画面 | 行うこと | 検証 |
| --- | --- | --- |
| Administration → Users / Groups | 人のレビュアー・管理者、AI 開発者、読み取り専用バックアップを分離 | 継承権限を含む実際の所属と資格情報 |
| Administration → Roles | 選択した役割のコード・プロジェクト管理などの権限を確認 | 役割名だけで判断せず、AI に所有・管理・保護変更を許さない |
| Project → Settings → Authorizations → Users / Groups | 必要なプロジェクト範囲だけを許可し、親も確認 | バックアップは対象リポジトリのみ読み取り、AI は定めた範囲の権限 |
| Project → Settings → General | 親プロジェクトと実効的な既定の役割を確認 | 意図しない匿名・既定アクセスや継承された所有権がない |

参照版の Code Writer で “Manage Pull Requests” が無効でも、これは管理・一括処理の制御であり、最終マージが絶対にできない証拠ではありません。人の有効な承認後に、マージ権限を独立して検証します。日常の AI アカウントに人のブラウザーセッションや管理者トークンを渡しません。上記の監督付き設定セッションは一時的なもので、通常の Git 作業に残さないでください。

<a id="3-initialize-and-protect-the-target-branch"></a>

## 3. 対象ブランチを初期化して保護する

ブランチ作成を禁止するルールを有効にする前に、人が管理する設定手順で対象保護ブランチを初期化します。AI に初期化や修復をさせるため、保護を日常的に無効化してはいけません。

**Project → Settings → Code → Branch Protection** を開きます。参照 UI では保護ブランチ（通常 `main`）と対象主体（参照例は `anyone`）を選択します。適用順を確認してください。参照版ではローカルルールが親より先で、最初に一致したルールが使われます。子のルールが厳しい親ルールを隠す場合があるため、実効動作を確認します。

| 項目 | 判断と確認 |
| --- | --- |
| Prevent forced push | 保護ブランチで有効化し、使い捨てリポジトリで許可のない履歴書き換えが拒否されることを確認 |
| Prevent deletion | ブランチを保護。リポジトリ削除は別権限 |
| Prevent creation | 初期化後に判断。更新・レビューの保護の代わりではない |
| Required reviewers | UI の選択機能で独立した人のレビュアーを指定し、結果の式とアカウントを確認 |
| Required builds / signatures | プロジェクトに応じて選び、実行される検査と信頼する署名鍵を使う |
| File/tag protection | 必要範囲だけを定義。ブランチルールからタグ・リリース保護を推測しない |

以前の参照設定には必須レビュアーがなく、後で追加されました。force-push を禁止しても、通常の fast-forward による直接 push は**禁止されません**。通常の直接 push を明示的に確認します。指定レビュアーが PR 提出者でもある場合、参照実装では扱いが異なることがあります。人と AI のアカウント分離が重要です。専用テストが合格するまで、人だけがマージできる証明と説明してはいけません。

意図した設定変更は許可範囲内でのみ保存し、値と対応アカウントを読み返します。画面写真は設定の表示であり、強制の証拠ではありません。

<a id="4-set-pr-defaults-without-confusing-responsibilities"></a>

## 4. 役割を混同せず PR の既定値を設定する

**Project → Settings → Pull Requests** で各項目がローカルか継承かを調べます。

- **Default merge strategy：**参照例は Squash。既定値は他の方式の禁止ではありません。
- **Default assignee：**作業担当者であり、必須レビュアーとは別です。
- **Delete source branch after merge：**操作者の権限にも依存する任意の整理です。古いブランチを全部消してよいと解釈しません。
- 引き継ぐ前にソース、対象、差分、タイトル、検査を確認します。人がレビューし最終マージを実行し、AI はマージや自動マージの有効化をしません。

squash 後は実際の対象履歴に対する統合内容を検証します。コミット ID の違いだけで内容の欠落と判断しません。安全な同期と範囲を限定した整理は共通手順に従います。

<a id="daily-human-request-creation"></a>

### 日常のリクエストは人が作成する

AI が許可されたブランチを push してタイトル・説明案を渡したら、人がリポジトリの PR ページで新規作成し、ソースと対象を確認し、文を入力して送信します。差分と実際の検査・レビュー結果を読み、自分でマージを確認します。[引き継ぎ全体](workflow.md)を参照してください。作成者が必須レビュアーでもある場合、使用版の承認ルールを確認し、必要なら別の権限ある人にレビューしてもらいます。保護を弱めて対応してはいけません。

<a id="5-optional-rest-ingress-restriction"></a>

## 5. 任意の REST 入口制限

自前運用では、必要な Web/Git 経路を許可したままゲートウェイで REST 名前空間を拒否できます。[ゲートウェイ例](../../examples/onedev/README.md)で説明しています。連携機能が使えなくなる場合があるため、サービスに適する場合だけ選びます。

直接バックエンドのポート、SSH、別ホスト名、IPv6、トンネル、認証済みブラウザーセッション、サーバータスク、コンテナ・ホスト管理を含む全経路を調べます。プロキシの一地点を拒否しても、他経路の遮断は証明できません。正規化されたパス、大小文字・エンコードの違い、実際の Git 操作、必要な WebSocket を検証範囲に含めます。ネットワーク障害は権限拒否の証拠ではありません。

<a id="6-two-common-pitfalls"></a>

## 6. よくある二つの問題

<a id="pr-source-branch-is-not-suggested"></a>

### PR のソースブランチが候補に出ない

参照版 14.1.0 では、最新コミット作者のメールとログインユーザーの検証済みメールアドレスが候補選定に関わります。最新コミット作者と意図したユーザーを確認します。そのユーザーが管理するアドレスだけを Email Addresses 設定で追加し、通常の確認を完了します。管理者の動作から、一般ユーザーも確認を省略できると推測してはいけません。

PR 作成を開き直してソースと対象を確認します。ブランチを手動選択しても構いません。これは候補表示の修復であり、自動マージでも承認付与でもありません。候補を出すためだけに Git の全体の作者設定を変えたり履歴を書き換えたりしません。明示的に選んだソースが優先されます。

<a id="a-ready-pr-remains-marked-work-in-progress"></a>

### 準備済み PR が作業中と表示される

参照実装ではタイトルが `wip` または `[wip]` で始まると、大文字小文字を区別せず作業中としてマージを止めます。**任意の英字で始まるタイトルを禁止しているわけではありません。**対象は PR タイトルであり、コミットメッセージやブランチから作られた場合もあります。

実際に準備が整ってからマーカーを除去します。必須レビュー、検査、人による最終マージは残ります。WIP による停止はマージ権限境界の証拠ではありません。導入版でルールを確認してください。

<a id="7-acceptance-and-recovery"></a>

## 7. 検証と復元

[共通検証表](security-acceptance.md)と[証拠テンプレート](../../templates/security-acceptance.csv)を使います。読み取り専用の棚卸しから始め、使い捨てリポジトリで拒否テストを行う前に適切な許可を得ます。操作者、版、経路、制御、前後の状態、実際の拒否理由を記録します。説明できない失敗や未実施テストは「未検証」です。

[バックアップ手順](backup-and-recovery.md)に従い、リポジトリ**と**サービスのデータ・設定について独立した復元可能な版を保持します。更新される clone は OneDev 全体のバックアップではありません。コンパイルと起動検査は任意であり、全てのサーバー DB や添付を検証できるものではありません。

<a id="sources-and-limits"></a>

## 出典と制約

- [公式コンテナ導入](https://docs.onedev.io/installation-guide/run-as-docker-container)と[リバースプロキシ設定](https://docs.onedev.io/administration-guide/reverse-proxy-setup)。
- [参照版のソースブランチ選定](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/web/page/project/pullrequests/create/NewPullRequestPage.java)。
- [参照版の PR 作業中判定とマージ条件](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/PullRequest.java)。
- [参照版のブランチ保護](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/support/code/BranchProtection.java)と[push 検査](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/git/hook/GitPreReceiveCallback.java)。

このガイドは、版を明示した UI 観察とソース調査を組み合わせています。文書を書いても OneDev がインストールされるわけではなく、別のサーバー、役割、NAS 機種、プロキシ、リリースを認証するものでもありません。

**次へ：**[検証表](security-acceptance.md)で設定した権限を確認し、[四ステップと整理](workflow.md)へ進みます。製品説明は[Git Guard 概要](../../README.ja.md)に戻ってください。

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

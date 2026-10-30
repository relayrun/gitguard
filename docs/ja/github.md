# GitHub：プラットフォームへの対応

[English](../en/github.md) · [简体中文](../zh-CN/github.md) · [日本語](github.md) · [Deutsch](../de/github.md) · [Français](../fr/github.md) · [Español](../es/github.md) · [Português (Brasil)](../pt-BR/github.md) · [Русский](../ru/github.md)

[Git Guard ホーム](../../README.ja.md) · [クイックスタート](README.md)

基礎草案 0.1 — 参照先の GitHub 文書との照合日：2026-10-28。

Git Guard の主な設定例は OneDev です。GitHub はもう一つの例として、同じ[日常手順](workflow.md)、[安全性検証](security-acceptance.md)、[バックアップ方針](backup-and-recovery.md)を使います。この章は機能の対応関係を説明し、特定のリポジトリの現在の設定を示すものではありません。

| 共通の要件 | GitHub での対応 |
| --- | --- |
| ローカルの準備とコミット | 通常のローカル Git 作業。この段階でアップロードしない |
| 許可されたリモート協業 | 作業ブランチを push してリクエスト文を準備。標準例では人が Web 画面で PR を作成 |
| 必須レビューと main の保護 | 適切なブランチ保護・ルールセットとレビュアー要件を設定 |
| force-push と保護参照の削除を制限 | 対応する許可を無効に保ち、例外を確認 |
| 人による最終マージ | AI のアカウント・資格情報を人の権限から分離。レビュー必須化だけを人専用のマージ権限とみなさない |
| 人のマージ後 | 結果を検証してローカル main を安全に同期し、完了確認済みブランチだけを整理 |

GitHub の公式文書では Free プランの公開リポジトリで保護ブランチとブランチ・タグのルールセットを利用でき、非公開リポジトリではプランに依存します。公開リポジトリでの利用可否から、すべての高度な機能や push ルールセットが使えると推測してはいけません。[保護ブランチ](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) · [ルールセット](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)

承認レビューを必須にしても、承認後に誰がマージできるかはそれだけでは定まりません。従来のブランチ保護の管理者例外、許可アクター、ルールセットのバイパス一覧、アプリ権限、利用可能な人の資格情報も関係します。対象となる組織リポジトリの push 制限は、PR 必須化と併せて検討する制御の一つです。人専用のマージだと述べる前に実際のアカウントで検証します。リポジトリ管理、削除、ルール変更は所有者が別に管理します。

標準例では、人が PR 作成画面で base（対象）と compare（ソース）を確認し、タイトル・説明を入力して送信します。差分と検査をレビューしてから自らマージします。必要な独立した承認は引き続き適用され、PR 作成は承認ではありません。AI が別途許可されて PR を作る場合は[共通手順](workflow.md)を参照します。

GitHub は自動マージも提供しますが、この手順では最後の実行を人に残します。便宜のために無断で自動マージを有効にしないでください。トークンに「制限済み」と書いてあるだけで、作業ブランチへの書き込みは許され全マージは禁止されると考えないでください。

自前 OneDev 用リバースプロキシの例が GitHub サービスの前段に置かれるわけではありません。保護の目的を GitHub 自身のアカウント、ルール、アプリ権限、検証済みのアクセス経路に対応させます。

導入前に実際のプラン、公開範囲、有効なルールと例外を調べ、許可された使い捨て環境で共通の検証表を適用します。この章を書いたことで、リポジトリ設定を変更したり、権限拒否の実機テストを行ったりしたわけではありません。


<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

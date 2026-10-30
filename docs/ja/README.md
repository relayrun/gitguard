# Git Guard — クイックスタート

[English](../en/README.md) · [简体中文](../zh-CN/README.md) · [日本語](README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Español](../es/README.md) · [Português (Brasil)](../pt-BR/README.md) · [Русский](../ru/README.md)

[Git Guard ホーム](../../README.ja.md)

日本語の紹介・クイックスタート・7本の詳細手順書・動画を利用できます。OneDev と GitHub は設定例であり、他の Git 管理サービスでも原則を応用できます。翻訳はレビュー用で、実環境の権限検証を代替するものではありません。

許可されたコミットやアップロードの前に、公開内容手順で[検査を設定・実行](public-content-review.md#configure-the-public-content-check)し、[結果を理解して対応](public-content-review.md#interpret-results-and-handle-findings)してください。

## 設定は AI に手伝ってもらえる

手順書に沿って自分で設定するほか、手順書とスキルを AI に渡して作業を依頼できます。**画面を見ながら操作する Computer Use を推奨します。**人が作業を確認し、必要な範囲だけ許可します。機密情報は人が入力し、完了後は一時的な管理セッションからログアウトして、AI を日常の制限されたアカウントに戻します。

| 利用環境 | 入口 |
| --- | --- |
| 自前の OneDev | [設定手順書](onedev.md) · [設定・安全性検証スキル（英語）](../../skills/gitguard-onedev-safety/SKILL.md) |
| GitHub | [GitHub ガイド](github.md) |
| その他の Git 管理サービス | [共通の協業手順](workflow.md)と[検証表](security-acceptance.md)を各サービスの機能に対応させます。 |

初回は、①リポジトリ・主ブランチ・人と AI のアカウントを決める、②設定する、③許可された隔離テスト用リポジトリで正常操作と拒否動作を検証する、④[独立バックアップと復元](backup-and-recovery.md)を用意する、の順に進めます。毎回すべてを設定し直す必要はなく、権限や環境の変更時に影響範囲を再確認します。

## 設定後の日常作業は4ステップ

[日常協業スキル（英語）](../../skills/gitguard-workflow/SKILL.md)とプロジェクトの Git 手順を使います。

| 手順 | 人が依頼・実行すること | AI が行うこと |
| --- | --- | --- |
| 1. ローカルコミット | 「Git.md のステップ1を実行して」 | 手順と変更内容を確認してローカルにコミット。まだ送信しません。 |
| 2. push と準備 | 「Git.md のステップ2を実行して」 | 許可された作業ブランチを push し、リクエストのタイトル・説明・検査結果を準備します。 |
| 3. 人によるレビューとマージ | Web 画面でリクエストを作成し、ソース・ターゲット、タイトル・説明、差分と検査を確認してマージします。 | 説明を補助します。最終マージは人が実行します。 |
| 4. マージ後の整理 | 「マージ済みです。結果を確認して後片付けして」 | 実際の統合内容を確認し、安全に主ブランチを同期。完了確認済みのブランチだけを整理します。 |

`Git.md` は実際のプロジェクトの手順書名に置き換えてください。コミット・push・マージのタイミングは人が決めます。[詳しい協業手順](workflow.md)

## 安全性と復元

設定が存在するだけでは安全性の証明になりません。拒否テストは別途許可された使い捨てのリポジトリで行い、未検証の経路を明記します。独立した同期先と保護された過去の復元点を用意します。クリーンビルドや起動確認はプロジェクトに応じた任意項目です。

OneDev では、検証済みメールアドレスがソースブランチの候補表示に関係する場合があります。これは自動マージではありません。参考バージョンの WIP タイトルはマージを止めますが、英字で始まるタイトル全般を禁止するものではありません。

## 詳しい手順

- [日常の協業手順](workflow.md)
- [OneDev の設定](onedev.md)
- [GitHub の対応設定](github.md)
- [安全性の検証](security-acceptance.md)
- [バックアップと復元](backup-and-recovery.md)
- [公開内容の点検](public-content-review.md)
- [動画と言語の連携](animation-and-language.md)
- [Skills](../../skills/README.md) · [Templates](../../templates/README.md)

スキル、テンプレート、導入例、チェックツールは共通の英語資料です。

AI が変更を準備し、人が最終レビューとマージを行います。

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

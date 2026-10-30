# GitHub: concise platform mapping

[English](github.md) · [简体中文](../zh-CN/github.md) · [日本語](../ja/github.md) · [Deutsch](../de/github.md) · [Français](../fr/github.md) · [Español](../es/github.md) · [Português (Brasil)](../pt-BR/github.md) · [Русский](../ru/github.md)

[Git Guard home](../../README.md) · [Quick start](README.md)

Foundation draft 0.1 — checked against the linked GitHub documentation on 2026-10-28.

OneDev remains Git Guard's main worked example. GitHub is the secondary example: use the same [daily workflow](workflow.md), [security acceptance](security-acceptance.md), and [backup guidance](backup-and-recovery.md). This chapter describes capability mapping, not the current settings of any particular repository.

| Shared requirement | GitHub mapping |
| --- | --- |
| Local preparation and commit | Ordinary local Git work; no remote upload at this step |
| Authorized remote collaboration | Push a feature branch and prepare request text; the standard example has the human create the PR in the web interface |
| Required review and protected main | Configure appropriate branch protection/rulesets and reviewer requirements |
| Restrict force-push and protected-ref deletion | Keep the corresponding protected-branch allowances disabled and inspect exceptions |
| Human final merge | Separate the AI identity/credentials from human authority; do not treat required review alone as an exclusive merge permission |
| After human merge | Verify the result, synchronize local main safely, and clean only the confirmed completed branch |

GitHub documents protected branches and branch/tag rulesets for public repositories on its Free plans; availability for private repositories depends on the plan. Do not infer every advanced or push-ruleset capability from public-repository availability. [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) · [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).

Required approving reviews do not by themselves establish who may execute a merge after approval. Classic branch-protection administrator exceptions, permitted actors, ruleset bypass lists, application permissions, and accessible human credentials all matter. GitHub's documented push restrictions for suitable organization repositories are one control to evaluate alongside required PRs; test the actual identity before claiming exclusive human merge. The owner must retain separate control of repository administration, deletion, and rule changes.

For the standard example, the human uses the repository’s pull-request creation flow: verify the base (target) and compare (source) branches, enter title/description, submit, review the difference and checks, then personally merge. Required independent approvals still apply; creating a PR does not approve it. See the [shared workflow](workflow.md) for the separately authorized AI-created-PR variant.

GitHub also supports automatic merge features; this workflow leaves final execution with the human. Do not enable automatic merge as an incidental convenience. Do not assume a token permits feature-branch writes but forbids all merges just because its label says it is restricted.

The self-hosted OneDev reverse-proxy example does not become a proxy in front of GitHub's service. Map the protection goal to GitHub's own identities, rules, application permissions, and verified access paths instead.

Before adopting the mapping, inspect the actual account plan, repository visibility, active rules and exceptions, then apply the shared acceptance matrix in an authorized disposable environment. No repository settings were changed or security-negative tests performed by writing this chapter.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

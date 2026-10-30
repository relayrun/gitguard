# OneDev setup guide: AI permissions and human review

[English](onedev.md) · [简体中文](../zh-CN/onedev.md) · [日本語](../ja/onedev.md) · [Deutsch](../de/onedev.md) · [Français](../fr/onedev.md) · [Español](../es/onedev.md) · [Português (Brasil)](../pt-BR/onedev.md) · [Русский](../ru/onedev.md)

[Git Guard home](../../README.md) · [Quick start](README.md)

This **RelayRun Git Guard** guide explains how to separate human and AI permissions, protect main, restrict review-bypass routes and maintain independent recovery copies on self-hosted OneDev. AI commits and pushes working branches within authorization; a person creates the request, reviews it and performs the final merge in the web interface.

**Git Guard is for individuals and teams using Git repositories, not only OneDev users.** OneDev and GitHub are configuration examples. Other Git repository management platforms can follow the [shared collaboration and protection principles](workflow.md), with settings and outcomes verified against their capabilities. This chapter demonstrates OneDev settings; the [GitHub guide](github.md) provides another example. OneDev is a third-party platform, not a RelayRun product.

Review draft 0.1. UI and troubleshooting reference: **OneDev 14.1.0**. This is a versioned example, not a recommendation to deploy an old release without checking current support. [Workflow](workflow.md) · [Security acceptance](security-acceptance.md) · [GitHub alternative](github.md)

**On this page:** [AI-assisted setup](#visible-ai-assisted-setup) · [Deployment](#1-select-a-deployment-boundary) · [Identities](#2-establish-separate-identities) · [Branch protection](#3-initialize-and-protect-the-target-branch) · [Human merge](#4-set-pr-defaults-without-confusing-responsibilities) · [REST ingress](#5-optional-rest-ingress-restriction) · [Common pitfalls](#6-two-common-pitfalls) · [Acceptance and recovery](#7-acceptance-and-recovery) · [Sources](#sources-and-limits)

Before an authorized commit or upload, follow the public-content guide to [configure and run the check](public-content-review.md#configure-the-public-content-check) and [interpret and handle findings](public-content-review.md#interpret-results-and-handle-findings).

## Visible AI-assisted setup

You can configure the platform manually or ask AI to follow this guide and the setup skill through a visible Computer Use interface. First identify the exact project, actor, settings to change and rollback. The human approves that scope and can watch the actions; no hidden or permanent administrator grant is implied.

For administrative controls, use a supervised temporary setup session designated for those changes. The human enters sensitive credentials without placing them in chat, screenshots or repository files. Do not reuse an administrator session to bypass a denied daily action. When setup is done, read back the settings, perform the appropriately scoped acceptance, end the elevated session and return to the restricted daily identity. If the available interface cannot perform a required step, report it and leave that step to the human; do not claim a click that did not happen.

Watching the screen helps explain the configuration; enforced permissions and their tests provide the protection.

## 1. Select a deployment boundary

Prefer an independent computer, server, or NAS whose architecture and container support match your selected OneDev release. Keep the server, container runtime, storage, backups and administrator credentials outside the AI development identity's reach. Same-host use needs explicit OS/file permissions; Docker alone does not supply this separation.

Use the official installation guide and the [parameterized example](../../examples/onedev/README.md). Select supported image versions/digests, an independent data location, TLS ingress and recovery method before starting. The example exposes only a loopback gateway, omits the Docker socket and disables the direct HTTP/SSH host mappings. It is a starting configuration, not a tested production installation. Container-based builds may need a separately designed executor.

## 2. Establish separate identities

| Where to inspect | What to do | Verify |
| --- | --- | --- |
| Administration → Users / Groups | Separate the human reviewer/admin, AI contributor, and read-only backup identity | Actual membership and credentials, including inherited access |
| Administration → Roles | Inspect the selected role's code, project-management and other permissions | A role name alone is insufficient; AI must not own/administer projects or change protection |
| Project → Settings → Authorizations → Users / Groups | Grant only the necessary project scope; inspect parents | The backup identity reads the intended repository only; AI rights match the declared model |
| Project → Settings → General | Inspect parent project and effective default role | No unintended anonymous/default access or inherited project ownership |

The reference Code Writer role's disabled “Manage Pull Requests” switch concerns management/bulk operations; it is not proof that a code writer can never perform a final merge. Test merge authority independently after valid human approval. Do not expose a human browser session or administrator token to the daily AI identity. A supervised, scoped setup session described above is temporary and must not be retained for routine Git work.

## 3. Initialize and protect the target branch

Initialize the intended protected branch under the human-controlled setup workflow before enabling a rule that prevents its creation. Do not routinely turn protection off so AI can bootstrap or repair it.

Open **Project → Settings → Code → Branch Protection**. In the reference UI, select the protected branch (often `main`) and the intended subjects (the reference uses `anyone`). Read the rule order: local rules precede parent rules, and the first matching rule is used in this reference version. A child rule can shadow a stricter parent; inspect effective behavior.

| Option | Required reasoning |
| --- | --- |
| Prevent forced push | Enable for the protected branch; verify an actual unauthorized rewrite is rejected in a disposable test repository |
| Prevent deletion | Protect the branch; repository deletion is a different permission |
| Prevent creation | Decide after initialization; not a replacement for update/review protection |
| Required reviewers | Select the independent human reviewer using the UI selector; verify the resulting expression and account |
| Required builds / signatures | Select according to your project, with checks that actually run and trusted signing keys |
| File/tag protection | Define only needed scope; branch rules do not automatically prove tag or release protection |

The earlier reference initially had no required reviewer; later review requirements were added. Blocking force-push does **not** block an ordinary fast-forward direct push. Check ordinary direct push explicitly. A named reviewer who is also the PR submitter may be treated differently by the reference implementation; keeping human and AI identities separate is essential. Do not present this setup as proving exclusive human merge until that capability has passed its own test.

Save a deliberate configuration change only within its authorization. Read back values and matching identities; screenshots show configuration, not enforcement.

## 4. Set PR defaults without confusing responsibilities

Open **Project → Settings → Pull Requests**. Check whether each field is local or inherited.

- **Default merge strategy:** the reference uses Squash. A default is not a ban on other strategies.
- **Default assignee:** work ownership, not the required reviewer.
- **Delete source branch after merge:** optional cleanup that also depends on actor permission. Never infer that all old branches should be removed.
- Always inspect source, target, diff, title and checks before handing off. The human reviews and performs the final merge; the AI does not click merge or enable auto-merge.

After a squash, verify the integrated change relative to the actual target history. Different commit IDs alone do not mean lost content. Follow the common workflow for safe synchronization and scoped cleanup.

### Daily human request creation

After the AI pushes the authorized branch and supplies the proposed title/description, the human opens the repository’s pull-request page, creates a new request, verifies source and target, enters the text and submits. Read the diff and actual check/review results before personally confirming the merge. See [the complete handoff](workflow.md). If the creator is also a required reviewer, verify your version’s approval rules; use another authorized human reviewer where required rather than weakening protection.

## 5. Optional REST ingress restriction

A self-hosted deployment can deny the REST namespace at its gateway while allowing the required web/Git paths. The [gateway example](../../examples/onedev/README.md) describes this model. It may disable integrations; select it only when it fits the service.

Inspect every route: direct backend port, SSH, alternate hostname, IPv6, tunnels, authenticated browser sessions, server tasks and container/host administration. A blocked proxy endpoint does not establish that other paths are blocked. Keep normalized path, case/encoding variants, real Git operations and needed WebSockets in the acceptance scope. Network failures are not permission-denial evidence.

## 6. Two common pitfalls

### PR source branch is not suggested

In the 14.1.0 reference, source-branch suggestions consider the latest commit author's email and the signed-in user's verified email addresses. Inspect the latest commit author and the intended user. Add only an address controlled by that user through the user's Email Addresses settings and complete the normal verification process. Administrator behavior does not imply that ordinary users can skip verification.

Reopen PR creation and check source and target. Manually selecting the branch is also valid. This repairs a suggestion; it neither automatically merges nor grants approval. Do not change global Git identity or rewrite history merely to make the suggestion appear. An explicitly selected source takes precedence.

### A ready PR remains marked work in progress

The reference implementation treats a title beginning with `wip` or `[wip]`, case-insensitively, as work in progress and blocks merge. This is **not** a ban on titles beginning with any English letter. It affects the PR title, which may have been derived from a commit message or branch.

Only remove the marker once the work is actually ready. Required reviews, checks and human final merge still apply; the WIP blocker is not proof of a merge-permission boundary. Verify the rule in your deployed version.

## 7. Acceptance and recovery

Use the [shared matrix](security-acceptance.md) and [evidence template](../../templates/security-acceptance.csv). Start with read-only inventory; obtain the appropriate authorization before denial tests in a disposable repository. Record actor, version, paths, control, before/after state and actual refusal reason. An unexplained failure or missing test is “not verified.”

Maintain independent recoverable versions of the repositories **and** service data/configuration according to the [backup guide](backup-and-recovery.md). An updating clone is not a full OneDev backup. Compilation and application-start checks are optional and cannot validate every server database or attachment.

## Sources and limits

- [Official container installation](https://docs.onedev.io/installation-guide/run-as-docker-container) and [reverse proxy setup](https://docs.onedev.io/administration-guide/reverse-proxy-setup).
- [Versioned source-branch selection](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/web/page/project/pullrequests/create/NewPullRequestPage.java).
- [Versioned PR work-in-progress and merge conditions](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/PullRequest.java).
- [Versioned branch protection](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/model/support/code/BranchProtection.java) and [push checks](https://github.com/theonedev/onedev/blob/v14.1.0/server-core/src/main/java/io/onedev/server/git/hook/GitPreReceiveCallback.java).

The tutorial combines versioned UI observations and source review. Writing it does not install OneDev or certify another server, role, NAS model, proxy or release.

**Next:** verify the configured permissions with the [acceptance matrix](security-acceptance.md), then follow the [four-step workflow and cleanup](workflow.md). Return to the [Git Guard overview](../../README.md) for the product introduction.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

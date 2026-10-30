# Daily Git workflow

[English](workflow.md) · [简体中文](../zh-CN/workflow.md) · [日本語](../ja/workflow.md) · [Deutsch](../de/workflow.md) · [Français](../fr/workflow.md) · [Español](../es/workflow.md) · [Português (Brasil)](../pt-BR/workflow.md) · [Русский](../ru/workflow.md)

[Git Guard home](../../README.md) · [Quick start](README.md)

Foundation draft 0.1 — 2026-10-28.

## Read and scope the work

Identify the exact project, local directory, branch, remote, visibility, and current authorization. Read its agent entry, current plan, and relevant operating instructions. Keep unrelated staged/unstaged changes intact. Editing, committing, pushing, creating a PR, publishing a release, and deploying a site are different actions; carry forward authorization actually given without treating a general plan as permission for all of them.

## Step 1 — record the local change

Review the changed file list and difference. Run checks appropriate to the change. For public material, complete [the publication review](public-content-review.md) **before committing**, even if the commit will remain local initially. Stage only the intended files and make the authorized local commit. Read back its identity, content, and remaining worktree changes.

A local commit does not upload the work. Do not silently initialize another repository, add a remote, change protection settings, or create a backup task as part of an ordinary edit. Do not discard unrelated changes to obtain a clean status.

## Step 2 — share the branch and prepare the PR

Within the current authorization, verify the remote destination and full branch difference against the actual target. Include earlier unmerged branch commits in the scope review, not only the latest commit. Recheck the public-content boundary before any upload.

Push the authorized feature branch without force. In the standard homepage/animation example, prepare the correct source/target, a proposed title and description, and actual validation results for the human to create the request in the web interface. Do not report a prepared form as a created PR.

An adopter may separately authorize AI to create or update the matching PR. Only then perform that action and verify its actual existence/state. This variant does not grant final-merge authority. A pushed branch or draft PR in a public repository already exposes its contents; it is not private until merge.

If a policy or permission blocks the action, report the actual refusal. Do not bypass it using an administrator session, alternate token, direct server port, container access, or another interface. Resolving a content conflict must not silently expand the permitted action.

## Human final review and merge

In the standard example, open the repository’s request page in the OneDev/GitHub web interface, choose the new-request action, verify suggested source and target, enter the title and description, and submit the request. If a request already exists under a separately authorized workflow, inspect it rather than duplicating it. Default branch suggestions are not approval.

The human reviews the complete difference, test evidence, target, and intended result, then performs the final merge. The AI does not click merge, invoke a merge API/CLI, or enable automatic merge on the person's behalf under this workflow.

Required reviews and exclusive human merge authority are separate controls. A passing review check may still leave an AI identity able to merge. Validate both before describing the workflow as technically enforced. Protect administrator credentials and existing browser sessions as well as the named bot account.

## After the human confirms merge

1. Verify the actual server-side merge and its target. An instruction to prepare a PR is not a report that it merged.
2. Fetch and compare the reviewed change with the merged result. Squash/rebase can change commit identities; when the target advanced, compare the appropriate base and resulting diff rather than demanding identical whole-repository trees. For a same-base squash, equivalent final trees are useful evidence.
3. Check for uncommitted work, unpublished commits, other worktrees, and the applicable recovery/retention arrangement before cleanup. Do not create an unsolicited backup or overwrite local-only work to force alignment.
4. Fast-forward the local protected branch when its relationship to the remote allows it. Stop and explain divergence rather than resetting it away.
5. Remove only the verified completed feature branch within the cleanup authorization. If the server already deleted it, prune its stale tracking reference; do not recreate it. A squash commit may not satisfy a simple ancestry-based branch-deletion test, so check the content and retained-work evidence before any authorized alternative.
6. Report the actual branch/worktree state and any retained work or unresolved issue. Do not equate local cleanup with deployment or publication of a release.

## Keep the rules portable

The repository owner defines naming and review conventions. OneDev and GitHub have different controls and account models; the shared sequence remains the same. Use [security acceptance](security-acceptance.md) to separate intended policy from verified permission boundaries, and [GitHub mapping](github.md) for that platform's concise differences.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

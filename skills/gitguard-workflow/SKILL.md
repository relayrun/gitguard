---
name: gitguard-workflow
description: Prepare and review Git changes with an AI contributor and human final merge. Use for local commits, authorized branch pushes and pull requests, public-content checks, or post-merge synchronization and scoped cleanup.
---

# Git Guard workflow

Use the adopter's current repository instructions and authorization. Resolve this skill's references relative to this file; the target repository is the user's project, not the installed skill directory.

Read the [canonical workflow](../../docs/en/workflow.md). For public material, also read [public-content review](../../docs/en/public-content-review.md). Use [GitHub mapping](../../docs/en/github.md) or the [OneDev guide](../../docs/en/onedev.md) when that platform matters. Do not infer a platform permission from a written rule.

## Establish the task

Identify the repository, intended branch/target, actor, destination and authorized stage. Inspect status and the actual diff without disturbing unrelated changes. Reuse authorization already given for the same concrete action. Ask only for information or authority genuinely missing; a task to review does not authorize publishing.

## Execute the requested stage

Apply the canonical workflow's stage-specific checks. Local commit, remote branch/PR sharing, human final merge and post-merge cleanup remain distinct. A commit message or template cannot enlarge authorization.

For the standard example, step 2 pushes the authorized branch and prepares the source/target, title, description and checks. The human creates the request in the web interface, reviews and merges. Creating/updating a PR with AI is a separately authorized variant; preserve an existing authorized request rather than making a duplicate. Never report prepared text as a created request.

Use the [change handoff template](../../templates/change-handoff.md) to report reviewable scope and evidence. Before public commits inspect working and staged content; before publication inspect outgoing history and rights. The [read-only scanner](../../scripts/check_public_content.py) supports these checks but cannot certify privacy. Run it against the explicitly identified project, not by assuming the current directory.

The human performs the final merge. Do not click merge, call a merge endpoint, enable auto-merge, impersonate a reviewer, grant bypass rights, weaken protection or force-push to complete this skill. If an expected boundary is missing, report the gap and use the [security acceptance specification](../../docs/en/security-acceptance.md).

## Configure and perform public-content review

Follow [checker setup and result handling](../../docs/en/public-content-review.md#configure-the-public-content-check). Identify the public file set and actual target repository before running the bundled checker. Resolve its path from this skill's references and pass the target explicitly with `--root`. Use the generic profile for adopting projects; the gitguard profile adds this package's layout exclusions. Do not initialize Git, install another scanner, stage changes or upload material merely to make a review command applicable.

Review working files, then actual staged bytes before an authorized commit, and actual outgoing history before an authorized push. If a scope does not exist yet, report that limit and check it at the appropriate later stage. Treat exit 1 as findings and exit 2 as incomplete. Exit 0 only covers implemented heuristics, not all private information. Preserve binary/oversize findings for scoped manual review.

The bundled tool does not accept a private matching list or automatically redact files. For project-specific secret/account matching, use an appropriate available scanner with private configuration outside repositories and packages; arrange installation separately if needed. Never embed real values in scripts, examples, tests, command arguments or reports, and do not request secrets in chat. Make only authorized corrections to public material, preserve private originals, recheck affected scopes and report category/location/disposition without matched values. Credential exposure or committed secrets require replacement/remediation within separately established authorization, not an incidental history rewrite.

## After the human merges

Verify the platform state and actual remote target. Account for squash/rebase IDs and unrelated mainline advances when checking integrated content. Synchronize only a safe clean working tree, then remove only branches whose work is confirmed integrated and whose cleanup is in scope. Preserve unmerged or unrelated work; do not invent a backup or destructive reset to make a check pass.

## Report

State the completed stage, files/content checked, validation outcome, remote action actually performed and remaining work. Distinguish configured, inspected, tested, published and user-confirmed. Never describe a prepared PR as created or a local commit as pushed.

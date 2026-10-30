---
name: gitguard-onedev-safety
description: Review or prepare a self-hosted OneDev setup and verify Git Guard permission boundaries. Use for OneDev roles, branch protection, PR settings, REST ingress, troubleshooting or security acceptance planning and authorized disposable-repository tests.
---

# Git Guard OneDev setup and safety

Resolve references relative to this file. Read the [OneDev guide](../../docs/en/onedev.md) and [shared acceptance specification](../../docs/en/security-acceptance.md); for recovery work read [backup and recovery](../../docs/en/backup-and-recovery.md). Versioned example settings are not evidence that the user's server has those settings or passes acceptance.

## Start with read-only inventory

Identify the actual server version, project, protected branch, human/AI/backup identities, inherited roles and first-matching branch rules. Check the declared ingress and alternate HTTP, SSH, API, browser-session, host/container and backup-administration paths. Do not print secrets or copy private screenshots into public material.

Use the [acceptance template](../../templates/security-acceptance.csv). For every claim, separate configuration observation from demonstrated enforcement. Keep untested items NOT_VERIFIED.

Before sharing setup notes, exported configuration or evidence, follow [public-content checker setup and handling](../../docs/en/public-content-review.md#configure-the-public-content-check). Run only against the declared public copy, use the appropriate profile and keep private matching configuration outside it. Inspect screenshots/binary attachments manually; the helper does not inspect their meaning or automatically redact secrets. Report locations/categories without secret values, preserve private originals and do not interpret a clean scan as complete privacy certification.

## Make a concrete change reviewable

Describe the exact options, affected subjects, expected effect, rollback and required checks before applying an authorized configuration change. Follow the [deployment example](../../examples/onedev/README.md) only as a reference; it does not authorize installing a server, altering DNS/firewalls, granting host privileges or mounting the Docker socket.

When the user wants AI-assisted configuration, prefer an available visible Computer Use interface so the human can observe the approved settings. Follow the guide’s supervised temporary setup-session boundary: do not collect credentials in artifacts, do not use that session to bypass a denied daily action, read back the change and end elevated access before daily work. If UI operations are unavailable, report the specific manual step instead of claiming execution. Manual or incremental configuration remains supported.

Reviewer requirements, default assignee, default squash, bulk PR management and exclusive final-merge authority are distinct. Diagnose source-branch/email suggestions and WIP titles using the versioned guide without rewriting Git history or changing global identity as a shortcut.

## Validate only within authorized boundaries

For active denial tests, require an explicitly scoped disposable repository, declared identities and expected pre/post state. Do not try production force-push, deletion or merge merely to test a policy. Check an allowed positive control and a valid forbidden request so network, authentication, malformed input or WIP failures are not mistaken for permission enforcement.

Do not auto-approve or perform final merges. If approval is needed as a test prerequisite, have the human provide it and keep the forbidden-action test within the approved disposable-test scope. Check access after valid approval separately from pre-approval blocking.

Use common evidence requirements for ordinary main push, force-push, branch/project deletion, approval, merge, auto-merge, protection changes, alternate paths and host/backup access. A proxy 403 alone does not prove complete isolation.

## Recovery and reporting

Independent synchronization and protected history are the foundation. Compilation and application startup are optional project-selected checks, not automatic actions of this skill. Never run a production program with live credentials as an incidental restore test.

Report exact scope, version, identities as safe role labels, observations, tested denials, positive controls, gaps and next actions. Avoid universal safety guarantees; inability to test a path remains a documented gap.

# Public content review

[English](public-content-review.md) · [简体中文](../zh-CN/public-content-review.md) · [日本語](../ja/public-content-review.md) · [Deutsch](../de/public-content-review.md) · [Français](../fr/public-content-review.md) · [Español](../es/public-content-review.md) · [Português (Brasil)](../pt-BR/public-content-review.md) · [Русский](../ru/public-content-review.md)

[Git Guard home](../../README.md) · [Quick start](README.md)

Review draft 0.1. This is a reusable procedure for projects releasing material publicly. [Workflow](workflow.md)

## Configure the public-content check

1. Identify the exact project and intended public file set. Keep internal records, credentials, private scanner configuration and diagnostic output outside that public tree. Review a separate release copy when the development directory contains private material; do not delete the original private files merely to make a scan pass.
2. Locate the checker in the Git Guard source or the installed skill's bundled reference snapshot. It needs Python 3.9 or newer and the standard library. It does not install itself, start a service or enforce a server permission. Set the target explicitly with `--root`; the installed skill directory is not the target project.
3. Use `--profile generic` for an adopting project. Use `--profile gitguard` only to apply this package's additional public/private layout exclusions. The built-in checker has no custom sensitive-word list or automatic replacement feature. For organization-specific secrets or identifiers, use a suitable separate scanner with configuration stored privately outside the release tree; see [private matching lists](#sensitive-matching-lists-stay-private).
4. Review working files, staged bytes and outgoing history as separate scopes. The paths below are placeholders. Replace the history range with the actual outgoing commits; the checker never fetches or pushes. Without a Git repository, start with the working-file check and perform index/history checks when those stages exist. A working-file-only result does not certify later commits.

```sh
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic --staged
python3 -B /path/to/gitguard/scripts/check_public_content.py --root /path/to/public-project --profile generic --history origin/main..HEAD
```

## Interpret results and handle findings

Exit **0** means no findings within the implemented rules; **1** means findings need review; **2** means the check did not complete. Reports show paths, categories and line numbers, not matched secret values. The working-file scan includes ignored files except Git metadata: ignoring a file does not prevent it being accidentally copied into a release.

Rules flag private-key signatures, selected GitHub-token formats, credentials in URLs, machine paths, private-network addresses and selected private/runtime filenames, plus broken or escaping relative Markdown links. They do not detect every password or account identifier. Binary files need manual review, files larger than 2,000,000 bytes are not inspected, the file-count limit is 3,000, and history ranges are limited to 200 commits. Review larger declared scopes in parts; do not silently omit them.

For each finding, record its category, location, decision and recheck result without reproducing sensitive values. Correct the public copy or inclusion rules, or document a justified benign/manual-review result; then recheck affected working, staged and history scopes. Do not suppress binary or size findings globally. A real credential exposure requires replacement and separately authorized history remediation; this helper neither repairs history nor deletes/replaces content. A timeout or incomplete scan is not a pass.

For this Git Guard package, use `scripts/prepare_release.py` to create an explicit public copy before packaging; development caches remain in the original directory and exclusions are recorded separately. The optional `--media-review` switch reads a private receipt for individually reviewed PNG/MP4 files and their exact SHA-256 hashes. It resolves only matching binary-review findings and lists them separately; changed files, secrets, unreadable files and size limits remain findings. Exit 0 can include these recorded media reviews, not an automatic privacy certification. See the [tool and packaging instructions](../../scripts/README.md).

## Before a local commit

Review the actual changed files, including untracked files. Confirm ownership and publication rights. Remove private project plans, host/user paths, internal addresses, tokens, private keys, credentials, customer data, raw screenshots/logs and unrelated product source. Examples use generic names and values.

Check links, UTF-8 text, meaningful language coverage, third-party notices and the accuracy of completion claims. A planned site or deployment must not be advertised as already available. Keep private evidence outside the release tree.

Inspect the staged bytes separately from the working files: staged content can differ. Review renames/deletions, binary files, submodules and symlinks; a visible clean document does not prove an embedded attachment is safe. A local commit is not permission to publish.

## Before a push

Enumerate the exact outgoing commits against the intended destination and review each relevant snapshot, including deleted files. Earlier secrets remain in history after a later removal. Review tags and other references only if they are actually part of the proposed push; a fresh repository must not accidentally inherit private history.

If sensitive content was committed, stop publication, arrange appropriate credential replacement and a separately approved remediation. Do not silently force-push or delete a repository to hide history. Automated scanners are supporting evidence, not proof that all private material has been removed.

## Reviewable release

Record the destination, visibility, changed file set, outgoing history, rights/license decision, validation and remaining limits. Confirm existing authorization for that exact action. Preserve human final merge.

For a repository that links to an official website, check the hostname, HTTPS certificate, branding and actual page. Translate the visible link label consistently across all supported READMEs; keep the same canonical destination. Check the repository Website field during the authorized publication. The handbook must remain useful independently of the website.

## Evidence levels

Use distinct labels: inspected, statically checked, behavior tested, deployed, user confirmed. Do not turn a configuration screenshot, scanner exit status or successful transfer into a live security/restore certificate. Use the [acceptance specification](security-acceptance.md) for permission checks.

## Sensitive matching lists stay private

Publish reusable scanning logic and invented test fixtures only. Real secret values, account identifiers and project-specific matching/replacement lists must remain outside the source tree, skill packages, downloads, screenshots and outgoing Git history. A rule containing an exact private value is itself sensitive; putting it in a scanner configuration does not make it publishable. Ignore rules are not a substitute for checking staged content and history.

If an adopter uses a separate secret scanner such as Gitleaks with a private configuration, supply that file from a private location at execution time. Do not copy it into a release package, echo matched values, include real values in command-line arguments or use them as test fixtures. Keep any resulting diagnostic files private and redact content before sharing.

The bundled checker is newly written for Git Guard. It does not load an existing private matching list and does not specifically recognize trading/customer accounts, arbitrary passwords or every token type. Its generic heuristics supplement a project-appropriate secret scanner and human review; a clean result is not comprehensive secret clearance. It performs no history cleanup.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

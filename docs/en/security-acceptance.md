# Security acceptance specification

[English](security-acceptance.md) · [简体中文](../zh-CN/security-acceptance.md) · [日本語](../ja/security-acceptance.md) · [Deutsch](../de/security-acceptance.md) · [Français](../fr/security-acceptance.md) · [Español](../es/security-acceptance.md) · [Português (Brasil)](../pt-BR/security-acceptance.md) · [Русский](../ru/security-acceptance.md)

[Git Guard home](../../README.md) · [Quick start](README.md)

Foundation draft 0.1 — 2026-10-28.

This specification is shared by the human handbook and future skills. It is a test plan, not a report that an installation passed. OneDev's detailed settings guide and GitHub's shorter mapping must refer here rather than define conflicting safety criteria.

## Inspect first

Record platform/version, repository visibility, protected branches, identities, roles, token/application permissions, inherited rules, rule order/enforcement, and bypass exceptions. Inspect relevant Git/SSH/HTTPS, web, API, CI/integration, proxy, and host/storage paths. Review whether an existing human browser session or credential is also usable by the AI.

For self-hosting, inspect host/container/data-directory access and alternate service ports. An independent server/NAS only supplies a useful boundary when the AI cannot administer it. A reverse proxy controls requests that pass through it; it does not protect an exposed alternate path or underlying storage. Hosted platforms need their own account/application controls rather than assuming a self-hosted proxy pattern can be copied.

## Test only in the authorized environment

Use a separately authorized disposable repository or instance with representative rules and distinct identities. Confirm recoverable test data and expected allowed operations. Perform negative tests only against those disposable objects; use inert content and retain evidence. This document does not authorize deleting production repositories, rewriting real history, or changing live roles.

## Acceptance matrix

| Capability/path | Expected result for the restricted AI identity | Evidence required |
| --- | --- | --- |
| Read and prepare an allowed feature branch | Allowed within scope | Positive control reaches the intended service with the intended identity |
| Push ordinary new commits directly to protected main | Denied by intended policy | Actual refusal and unchanged protected ref |
| Force-push protected history | Denied | Permission refusal and unchanged history |
| Delete protected branch/ref | Denied | Actual refusal and ref still present |
| Delete repository/project | Denied | Disposable project remains present; account lacks effective deletion capability |
| Approve on behalf of the required human | Denied | Review identities and authorization record |
| Execute final merge, including after reviews pass | Denied under exclusive-human-merge policy | Actual permission result; an unapproved PR alone is an insufficient test |
| Enable/use automatic merge or an equivalent integration | Denied to the AI under this workflow | API/web/application path and actual actor recorded |
| Change roles, protection, bypass lists, or security checks | Denied | Before/after configuration and refusal |
| Use another credential, session, endpoint, or CI path | No unintended authority | Inventory and a scoped test for each relevant path; unknown paths remain unverified |
| Modify host/container/repository storage | No administrative or destructive access | OS/storage boundary evidence, not merely an application checkbox |
| Delete/overwrite all recovery points | Denied to the development identity | Independent retention and backup-administration boundary |
| Human reviews and performs the intended merge | Allowed under the review policy | Positive control with the human's actual identity |

Review branch/tag creation, tag deletion, and branch-specific exceptions where they affect the project's policy. Do not unintentionally block all preparation while claiming successful separation of duties.

## Record each result

For each row, retain: test identity; software/configuration identity; source/target; operation and path; expected result; actual result/reason; before/after object state; time; and evidence location. Redact credentials and unrelated private data before sharing evidence.

Use **passed**, **failed**, or **not verified**, plus an explanation. A timeout, login failure, conflict, invalid request, WIP marker, unavailable server, screenshot, or enabled switch does not prove the intended permission refused the action. A positive control helps distinguish enforcement from a broken test setup.

If any required boundary is unverified or fails, report that gap explicitly. State which operations are actually blocked, not that every possible AI mistake has been eliminated. Retest affected paths after role, proxy, rule, version, or integration changes; retain the previous evidence with its original scope.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

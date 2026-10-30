# Git Guard quick start

[English](README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Español](../es/README.md) · [Português (Brasil)](../pt-BR/README.md) · [Русский](../ru/README.md)

[Git Guard home](../../README.md)

Initial handbook review draft 0.2 — 2026-10-28.

Before an authorized commit or upload, follow the public-content guide to [configure and run the check](public-content-review.md#configure-the-public-content-check) and [interpret and handle findings](public-content-review.md#interpret-results-and-handle-findings).

## Choose the right starting point

Git Guard describes a workflow and its controls; it does not install a Git server or change your account permissions. Start with one project and a declared protected branch. Keep the AI's identity separate from the person's reviewer/administrator identity.

| You need to… | Read |
| --- | --- |
| Prepare changes and hand them to a human | [Daily workflow](workflow.md) |
| Determine whether protections actually work | [Security acceptance](security-acceptance.md) |
| Preserve independent recovery copies | [Backup and recovery](backup-and-recovery.md) |
| Apply the workflow on GitHub | [GitHub mapping](github.md) |
| Prepare material for public release | [Publication checks](public-content-review.md) |
| Configure self-hosted OneDev | [OneDev setup](onedev.md) |
| Integrate video and page languages | [Animation and language](animation-and-language.md) |

For **local/self-hosted deployment**, OneDev is the detailed worked example, including exact UI settings and troubleshooting. For **online platform hosting**, GitHub is a shorter secondary example. Self-hosted OneDev can also run on a separate remote server or suitable NAS. Both use the same workflow and acceptance criteria; an equivalent label on another platform is not proof of equivalent enforcement.

## First setup, before daily work

1. Identify the repository, protected branch, intended feature branches, and allowed actors. Define who may push, approve, merge, delete, and administer; these are separate capabilities.
2. For self-hosting, prefer an independent computer/server or a suitable container-capable NAS. Check model/architecture support and resources. Keep host, container, storage, administrator credentials, and recovery administration out of the AI's reach. If sharing one computer, explicitly restrict its OS/data access; Docker alone is insufficient.
3. Configure the chosen platform's controls, then perform read-only inspection and separately authorized acceptance tests in a disposable repository. Do not use real production deletion or force-push as a quick check.
4. Establish independent synchronization and protected recovery points. Select optional restored-copy build or startup checks according to the project.
5. Use the daily workflow for one reviewable change. The human reviewer decides and executes the final merge.

Use [visible AI-assisted setup](onedev.md#visible-ai-assisted-setup) when you want help navigating the configuration. A human scopes and observes the temporary session; daily AI access remains restricted.

No security result is inherited from reading these steps. Record untested paths as not verified. A partial setup can be documented without advertising it as fully protected.

## Further reading and actual scope

Read [OneDev setup and pitfalls](onedev.md), [skill installation and packaging](../../skills/README.md), [templates](../../templates/README.md), [deployment example](../../examples/onedev/README.md) and [read-only checks](../../scripts/README.md).

This initial handbook is a review draft. Tools and sample configurations do not install a server, grant permissions or supply a live backup service. The deployment example and users' permission/restore outcomes require their own verification. Compilation/startup checks remain optional. Formal publication remains pending. Third-party materials retain their own terms.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

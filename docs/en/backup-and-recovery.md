# Independent backup and recovery

[English](backup-and-recovery.md) · [简体中文](../zh-CN/backup-and-recovery.md) · [日本語](../ja/backup-and-recovery.md) · [Deutsch](../de/backup-and-recovery.md) · [Français](../fr/backup-and-recovery.md) · [Español](../es/backup-and-recovery.md) · [Português (Brasil)](../pt-BR/backup-and-recovery.md) · [Русский](../ru/backup-and-recovery.md)

[Git Guard home](../../README.md) · [Quick start](README.md)

Foundation draft 0.1 — 2026-10-28.

Permission controls and recoverable copies address different failures. The foundation is automatic synchronization to an independent device, integrity checks, and protected historical recovery points. **Compilation and application startup are optional**: choose manual checks, a separate trigger, or added automation according to the project.

## Personal and company schedules

An individual can periodically power on a secondary laptop and let its configured trigger synchronize the data. State whether the trigger is system boot or user login; a login-triggered task cannot run before that user logs in. A company can use an available independent device with daily scheduling, missed-run handling, bounded network retries, concurrency control, and visible failure results.

Those are implementation choices, not features delivered by this guide. No backup script or scheduled task is installed by reading it. Do not give the AI development identity authority to delete all recovery versions or administer the backup device.

## Define what the copy covers

A main-branch checkout is not a complete server backup. Specify coverage for branches/history, local-only or uncommitted work, source/documents, required dependencies, runtime resources, external configuration, and private projects. Keep secrets in an appropriately protected recovery process, never in public examples or an ordinary archive intended for sharing.

Repository data and Git hosting metadata are different. A full self-hosted recovery may also require a consistent database, accounts/permissions, issues/PRs, attachments, configuration, and storage. Test service recovery separately from a source-code build.

An updating mirror may reproduce deletions. Keep independent recovery points and protect the last known-good version. Choose retention for the actual recovery need; do not automatically erase older copies when a new transfer merely reports success.

## Baseline checks

1. Confirm the source, intended revision/scope, destination, identity, and available storage. Preserve unrelated data.
2. Synchronize without overwriting a dirty/divergent checkout or pushing changes back. Verify exact revision equality with the intended fetched revision; a local branch ahead of the remote can otherwise appear already up to date.
3. Capture the declared scope consistently, with a unique recovery-point identifier. Record inclusion/exclusion rules and required files.
4. Check the manifest and relevant source/file/archive hashes. Opening a ZIP, counting files, or hashing the ZIP alone does not prove required source files were included. Required failures must fail the result.
5. Keep durable results and periodically restore into a separate empty destination. Label integrity and restore checks separately; until a restore is performed, its status is not verified.

## Optional compilation and startup

If selected, compile the restored copy using the actual supported toolchain and a clean build procedure. Record configuration, coverage, unloaded/excluded projects, and dependencies. An empty restore directory does not prove a clean build when the archive itself includes cached outputs. Do not allow undeclared files from the original development machine to mask omissions.

A useful historical lesson is that a backup can include project files while omitting required vendor source; compiling the restored copy may reveal that gap. However, compilation alone cannot validate every document, runtime resource, hosting database, or application path.

Optionally start the restored application and check basic functions in an appropriate test environment. Avoid production side effects. For documentation or static-content projects, choose relevant link/content/site checks instead of prescribing an unrelated software compiler.

Record build/startup as **not selected**, **not verified**, **passed**, or **failed** as applicable. Unselected optional checks do not make a baseline backup fail, and a completed transfer must not be labelled build-verified.

## If validation fails

Determine whether the failure is a backup omission, an environment requirement, or an application defect. Correct the inclusion rules or declared environment, make a new recovery point, restore, and repeat the affected checks. Preserve the previous good version and the failed receipt. Do not silently overwrite failed evidence or claim an old backup has been repaired without revalidation.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

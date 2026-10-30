# Backup policy template

- Repository and service data in scope:
- Independent destination and administrator:
- Read-only source identity and credential storage:
- Personal login-triggered or company scheduled synchronization:
- Required source revision and final destination revision comparison:
- Inclusion rules: tracked code, submodules/LFS, vendor inputs, required untracked assets:
- Exclusions and separate secure treatment of secrets:
- Consistency method for database/service data:
- Historical retention, offline/immutable protection and storage budget:
- Manifest/hash verification and alert on partial/failed copies:
- Restore directory, acceptance owner and retained known-good recovery point:

## Optional project-selected checks

- Clean build: not selected / manual / separate trigger / automated.
- Toolchain/dependency versions and offline availability:
- Startup/basic functions: not selected / manual / separate trigger / automated.
- Isolation from production endpoints and credentials:
- Failure handling: diagnose inclusion/toolchain/runtime issue, correct it, create a new recovery point, restore and rerun the affected check.

Do not overwrite the last known-good version while investigating. Synchronization, a hash match, a successful build and an actual service restore are different evidence.

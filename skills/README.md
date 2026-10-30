# Git Guard skills

Two implementations share the canonical English handbook:

| Skill | Scope |
| --- | --- |
| [gitguard-workflow](gitguard-workflow/SKILL.md) | Preparation, authorized commits/push/PR, public-content review and verified post-merge cleanup; human final merge |
| [gitguard-onedev-safety](gitguard-onedev-safety/SKILL.md) | Read-only setup inventory, versioned OneDev guidance and separately authorized disposable-repository acceptance |

## Build a standalone installable package

The source skills use repository-relative handbook/template links. **Do not copy only a source skill folder and assume those references will exist.** Run the [package builder](../scripts/package_skills.py) from the public source:

```sh
python3 scripts/package_skills.py --output ../gitguard-skill-packages
```

The output must be a new directory outside this source tree. Each resulting skill folder includes its SKILL.md and a self-contained source-reference snapshot with hashes. That snapshot is generated from the same canonical documents, not separately edited rules. Install the generated folder using your assistant's supported skill installation method; installation and activation are separate user choices.

The builder does not change Git, contact a server, install skills or deploy anything. Rebuild after handbook changes; do not hand-edit packaged references. English is the shared skill core. Other language guides link to these same rules rather than maintaining eight independent safety implementations.

## Checks and limits

[The package checker](../scripts/check_public_content.py) checks content and relative file links. Skill-format checks and scenario review are separate. A valid SKILL.md does not technically revoke an agent's permissions; actual isolation is verified with the shared safety specification. No live OneDev configuration or repository is changed by reading or packaging these skills.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

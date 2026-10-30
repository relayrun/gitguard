# Git Guard: AI Git collaboration with human review

[Official website](https://www.relayrun.net/) · [Quick start](docs/en/README.md) · [Skills](skills/README.md)

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Русский](README.ru.md)

[Feature ideas](https://github.com/relayrun/gitguard/discussions/categories/ideas) · [Questions](https://github.com/relayrun/gitguard/discussions/categories/q-a) · [Report a problem](https://github.com/relayrun/gitguard/issues/new/choose) · [Contribute](docs/CONTRIBUTING.md)

## 1. Git Guard in 40 seconds

https://github.com/user-attachments/assets/db6e114a-9859-42f0-92a8-559d353908ef

[Download English video · MP4 · 40 s](https://raw.githubusercontent.com/relayrun/gitguard/main/assets/videos/RelayRun-GitGuard-Intro-en-v12.mp4)

## 2. AI prepares the changes. People make the final decision.

**Let AI collaborate efficiently. Keep people in control of repository safety.**

**Git Guard is an open-source Git collaboration project by [RelayRun](https://www.relayrun.net/).** It provides **configuration handbooks for people, reusable skills for AI, templates and deployment examples** to help individual developers and teams restrict high-risk AI repository operations while keeping final review and merge with people.

> [!NOTE]
> **Collaboration principle: a person initiates → AI acts within authorization → a person reviews the result.**

**OneDev** is the main local or self-hosted example, with a shorter **GitHub** guide for online hosting. After setup, everyday use takes a few instructions and a human web review.

It is for individuals and teams using Git repositories and AI to edit code or documentation while retaining human oversight. **OneDev and GitHub are configuration examples, not a restriction on Git Guard's platform scope.** Other Git repository management platforms can use the same collaboration and protection principles, with settings and outcomes verified against each platform's capabilities.

## 3. Why Git Guard?

AI can change code quickly, but it can also make a damaging mistake quickly: overwrite history with a force push, delete a branch or change main without review. An AI with administrative access may also change the settings intended to protect the repository.

A prompt saying “do not do that” is not enough. Git Guard puts the controls in **server permissions, access routes and independent backups**. AI handles authorized work; people retain the key decisions and recovery access.

## 4. How does it protect a repository?

| Control | Intended result |
| --- | --- |
| **Protect the main branch** | AI may push authorized feature branches, but cannot push directly to main, force-push over its history or delete protected branches. |
| **Human web request creation, review and merge** | AI prepares the branch, title and description. A person opens OneDev or GitHub, creates the request, reviews the changes and performs the final merge. |
| **Restrict bypass routes** | The self-hosted OneDev example blocks REST API access at a reverse proxy and closes direct-backend and other bypass routes. |
| **Separate contribution and administration** | The daily AI identity has no final-merge, protection-rule administration or backup-administration permissions, and does not borrow a human administrator session. |
| **Keep independent recovery copies** | Back up to an independent device or NAS, retain historical recovery points and check integrity. Clean builds and startup checks are optional per project. |

> [!WARNING]
> **Key permission limits:** Restrict AI from pushing directly or force-pushing to main and from merging on its own; block REST API and other routes that could bypass review, leaving final review and merge to people.

These are configuration and acceptance goals, not proof that controls are already enforced. The [OneDev handbook's sources and limits](docs/en/onedev.md#sources-and-limits) identify the reference version. The [GitHub guide](docs/en/github.md) maps the goals to GitHub's own platform rules and permissions.

## 5. Several settings, with AI to help you configure them

Configure manually from the handbook, or give the handbook and relevant skill to an AI assistant.

**Prefer visible Computer Use for assisted setup:** watch the actions, grant the permissions needed for the task and enter sensitive credentials yourself. After setup, sign out of the temporary administrator session and return AI to its restricted daily identity.

| Approach | Start here |
| --- | --- |
| **Local or self-hosted OneDev** | The main example, with configuration steps, permission boundaries and troubleshooting: [OneDev handbook](docs/en/onedev.md) · [Setup and security-acceptance skill](skills/gitguard-onedev-safety/SKILL.md) |
| **Online GitHub hosting** | Map the same workflow to GitHub branch rules, identities and permissions: [GitHub guide](docs/en/github.md) |
| **Other Git repository management platforms** | Start with the [shared workflow](docs/en/workflow.md), map the protection goals to the platform's identity, branch and API permissions, then verify the results with the [acceptance matrix](docs/en/security-acceptance.md). |

Initial setup has four parts:

1. **Define the scope:** choose the repository, main branch and separate human/AI identities.
2. **Configure the controls:** follow the manual yourself or use AI assistance within authorization.
3. **Verify protection:** follow [security acceptance](docs/en/security-acceptance.md) in an authorized isolated test repository; normal actions should work and forbidden actions should be refused.
4. **Arrange recovery:** leave the temporary administrator session and set up [independent backup and recovery checks](docs/en/backup-and-recovery.md).

You do not repeat the whole setup for each change. Recheck affected controls when permissions, rules or the deployment environment change.

### Check sensitive content before committing

Ask AI to follow the [public-content review guide](docs/en/public-content-review.md): define the release scope and checker mode, then inspect working files, staged bytes and outgoing history separately. The helper flags possible keys, machine paths, private-network addresses and similar issues; resolve and recheck findings before an authorized commit or push. It does not delete or replace content or detect all private information, and images/videos still need human review. Keep organization-specific secret/account matching lists in private configuration outside repositories. The [workflow skill](skills/gitguard-workflow/SKILL.md) gives the corresponding operating requirements.

## 6. After setup, four everyday steps

Let AI use the [workflow skill](skills/gitguard-workflow/SKILL.md) with your project's Git workflow:

| Step | What you do | What AI does |
| --- | --- | --- |
| **1. Local commit** | “Please follow Git.md and run step 1.” | Reads the project workflow, checks this change and commits locally. Nothing is uploaded yet. |
| **2. Push and prepare** | “Please follow Git.md and run step 2.” | Pushes the authorized feature branch and prepares a request title, description and check results. |
| **3. Human review and merge** | Open OneDev or GitHub's web interface, create the request, check source and target branches, fill the description, review the diff and checks, then merge. | Provides explanations and assistance. A person performs the final merge. |
| **4. Post-merge cleanup** | “I have merged it. Please perform the post-merge cleanup.” | Verifies the actual merged content, safely synchronizes local main and removes only confirmed completed branches. |

`Git.md` stands for your project's actual Git workflow document; its filename may differ.

**You decide when to commit, when to push and whether to merge. AI handles the authorized execution details.**

[Read the full workflow](docs/en/workflow.md)

## 7. What you can use

- **Handbook and quick start:** understand the controls, choose a deployment route and configure it. [Read the handbook](docs/en/README.md)
- **Two skills:** everyday collaboration/cleanup and OneDev setup/security acceptance. [Browse skills](skills/README.md)
- **Reusable templates:** handoff, request descriptions and acceptance records. [Browse templates](templates/README.md)
- **Deployment examples:** self-hosted OneDev and access restrictions. [Browse examples](examples/onedev/README.md)
- **Checks and packaging:** inspect public content, local links and skill packages. [Browse tools](scripts/README.md)
- **Animation and language integration:** show a video matching the page language. [Read the integration guide](docs/en/animation-and-language.md)

## 8. Common questions and usage notes

### Must I repeat setup for every change?

No. Use the four everyday steps above, then recheck affected settings when identities, permissions or the deployment environment change.

### Can a solo developer use Git Guard?

Yes, with the same human/AI division of work and separate temporary setup and restricted daily sessions. If platform rules require another reviewer, that requirement still applies.

### Does installing a skill protect the repository automatically?

No. Skills guide AI behavior. Enforced restrictions need server or hosting-platform configuration and [permission acceptance](docs/en/security-acceptance.md).

### Which languages and materials are available?

All eight languages provide an introduction, a quick start and all seven detailed handbook chapters. Translations remain review drafts; native-language editorial review is not claimed. See the [coverage index](docs/README.md).

All eight language entries include their matching 40-second MP4. The README language selects the video; no separate video-language menu is needed.

Adapt the handbook, skills and deployment examples to your actual environment. Passing document checks does not mean your repository has been configured or passed live security acceptance. A local preview or working-tree update is not a published release.

Third-party materials keep their own terms; see [video sound credits](assets/videos/README.md).

[Public-content review](docs/en/public-content-review.md) · [Repository](https://github.com/relayrun/gitguard)

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

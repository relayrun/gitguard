# Read-only checks and skill packaging

## Shared brand footer

Maintain the footer's logo, display size and main official website in
[one template](../assets/brand/footer.md.in). Do not edit generated page footers
individually. The generator calculates page-relative asset paths; the generated
Markdown can be displayed without a client-side script. The common footer does
not carry a product license. Keep the repository's root LICENSE and third-party
notices intact; GitHub detects the repository license from that file. All page
languages share the same brand footer; no license translations are needed.

Preview one page's exact change before applying it:

```sh
python3 -B scripts/sync_footers.py --page docs/zh-CN/onedev.md --diff
python3 -B scripts/sync_footers.py --page docs/zh-CN/onedev.md --write
python3 -B scripts/sync_footers.py --page docs/zh-CN/onedev.md --check
```

After reviewing the affected pages, synchronize all public reader pages:

```sh
python3 -B scripts/sync_footers.py --all --diff
python3 -B scripts/sync_footers.py --all --write
python3 -B scripts/sync_footers.py --all --check
```

Without `--write`, the tool does not change files. It replaces only a recognized
complete footer block, preserves the preceding page body and rejects missing or ambiguous markers,
unexpected content after a footer, and paths outside this project. The common
template is the maintained source; generated pages refresh when the tool runs.
The bulk selection excludes machine-facing SKILL.md instructions, GitHub form
and PR-template files under `.github/`, and reusable template bodies; their
directory README pages still receive the shared footer except under `.github/`.
Website resource pages supply branding in their shared reader wrapper. This tool
performs no Git or network operations.

`test_sync_footers.py` uses temporary sample bodies for all eight languages to
check root/nested page paths, shared-template updates, repeat runs, and
body/newline preservation. It also checks rejected unsafe inputs and exclusion
of reusable instruction/template bodies. These samples are test data, not
published page content or claims of native-language editorial review. Run it with:

```sh
python3 -B -m unittest discover -s scripts -p test_sync_footers.py -v
```

## Public-content checks and packaging

Python 3.9 or newer; standard library only. Set `PYTHONDONTWRITEBYTECODE=1` when running tools from a clean source tree.

```sh
python3 -B scripts/check_public_content.py --profile gitguard
python3 -B scripts/check_public_content.py --root /path/to/public-project --staged
python3 -B scripts/check_public_content.py --root /path/to/public-project --history origin/main..HEAD
python3 -B scripts/prepare_release.py --output ../gitguard-release --media-review /private/media-review.json
python3 -B scripts/check_public_content.py --root ../gitguard-release/source --profile gitguard --media-review /private/media-review.json
python3 -B scripts/package_skills.py --root ../gitguard-release/source --output ../gitguard-skill-packages --media-review /private/media-review.json
```

Replace the example project path and range with the actual reviewed target. Working-tree, index and history checks are separate. The history mode examines every selected commit snapshot, including files absent from the final tree, and refuses ranges larger than 200 commits rather than silently truncating. It never fetches or pushes.

The content checker reports paths/categories/line numbers, never the matching secret text. Exit 0 means no findings within its stated heuristics; 1 means findings; 2 means an incomplete check. It cannot recognize all private information, inspect binary attachments semantically, validate external links/fragments or choose a license. It refuses oversized/nonregular files and calls out binary material for manual review. Working-tree review includes ignored files except Git metadata, because ignored secrets can still be copied accidentally into a release.

Use the generic profile for adopting projects. The stricter gitguard profile additionally rejects this package's excluded actual project-management and website paths. Educational templates remain permitted.

The package builder makes a **new output directory outside the source**, preserves a hash manifest and includes a complete public reference snapshot so a generated skill works without the original repository. It performs no installation, network access, Git writes, deployment or backup.

`prepare_release.py` uses this project's explicit public root-file and directory
list, including the reviewed GitHub community templates under `.github/`.
It preserves but omits development directories such as `.vs`, `.vscode`,
`.idea` and bytecode caches, recording exclusions in the output's private
`REVIEW.json`. Only its `source/` directory is a public candidate. Unknown root
files, linked paths, oversize files and unresolved scanner findings stop the
operation. An omitted development directory is not certified clean. The default
whole-working-directory scanner still examines ignored files and reports
unreadable files as incomplete while preserving other findings.

The optional `--media-review` argument accepts a **private, previously reviewed**
receipt. Its JSON shape is `{"status":"reviewed","files":{"assets/example.png":"SHA256"}}`,
where each value is the actual 64-character SHA-256 digest of an individually
reviewed file. Keep the real receipt outside source, packages and Git history.
It resolves only binary-review findings for the exact PNG/MP4 bytes, reports
those dispositions separately, and never dismisses text secrets, unreadable
files, oversize files or changed media. Do not create a receipt merely to make a
check pass; without prior review, the findings remain outstanding. Exit 0 can
include explicitly recorded reviewed media, not a claim that binaries were
automatically inspected. Private secret-matching lists remain unsupported.

Each skill ZIP now includes the full checked public reference set, including
LICENSE, posters and video targets. Unzip one package into an independent
directory to check its references and bundled checker; original workspace paths
are not required. Existing output directories are never silently reused.

## Origin and sensitive inputs

The checker is a new Git Guard helper, not a migrated account-list or history-cleaning script. It does not read private matching lists. It recognizes a limited set of generic patterns, not arbitrary passwords or account numbers. See [public-content review](../docs/en/public-content-review.md#sensitive-matching-lists-stay-private): exact private matches and real account data belong outside every public source/package/history; tests use invented values only.

<!-- relayrun-footer -->

---

<a href="https://www.relayrun.net/"><img src="../assets/brand/relayrun-lockup.png" alt="RelayRun" width="128" height="128"></a>

**[WWW.RELAYRUN.NET](https://www.relayrun.net/)**

© 2026 RelayRun

<!-- /relayrun-footer -->

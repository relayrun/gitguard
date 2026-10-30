#!/usr/bin/env python3
"""Assemble two self-contained skill folders from one canonical source tree."""
import argparse
import hashlib
import json
import pathlib
import re
import sys
import zipfile
sys.dont_write_bytecode = True
import check_public_content as check
import prepare_release as release

NAMES = ("gitguard-workflow", "gitguard-onedev-safety")
LINK = re.compile(r"(\]\()(\.\./\.\./[^)]+)(\))")

def build(root, output, media_receipt=None):
    root, output = root.resolve(), output.resolve()
    if output == root or output.is_relative_to(root) or root.is_relative_to(output):
        raise ValueError("Use a new output directory outside the source tree")
    if output.exists():
        raise ValueError("Output must not exist; preserve existing user files")
    snapshot, source_review = release.validated_source(root, media_receipt)
    # Include all referenced public assets and LICENSE so extracted skills work alone.
    selected = {path: raw for path, (_, raw) in snapshot.items()}
    output.mkdir(parents=True)
    receipts = []
    for name in NAMES:
        folder = output / name
        source_prefix = folder / "references" / "source"
        for rel, raw in selected.items():
            target = source_prefix / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
        skill = selected["skills/" + name + "/SKILL.md"].decode("utf-8")
        skill = LINK.sub(lambda m: m.group(1) + "references/source/" + m.group(2)[6:] + m.group(3), skill)
        (folder / "SKILL.md").write_text(skill, encoding="utf-8")
        manifest = {p: hashlib.sha256(b).hexdigest() for p, b in sorted(selected.items())}
        (folder / "references" / "manifest.json").write_text(json.dumps(
            {"generated": True, "canonical_source_files": manifest}, indent=2) + "\n", encoding="utf-8")
        packaged = check.working_snapshot(folder)
        package_review = {'references/source/' + path: sha for path, sha in (media_receipt or {}).items()}
        errors, reviewed = check.media_review(packaged, check.inspect(packaged), package_review)
        if errors:
            raise ValueError("Packaged local links/content failed review")
        archive = output / (name + ".zip")
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as z:
            for p in sorted(folder.rglob("*")):
                if p.is_file():
                    z.write(p, p.relative_to(output).as_posix())
        receipts.append({"skill": name, "source_files": len(selected),
                         "reviewed_media": len(reviewed),
                         "archive_sha256": hashlib.sha256(archive.read_bytes()).hexdigest()})
    (output / "package-receipt.json").write_text(json.dumps(receipts, indent=2)+"\n", encoding="utf-8")
    (output / "source-review.json").write_text(json.dumps(source_review, indent=2)+"\n", encoding="utf-8")
    return receipts

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parent.parent)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--media-review", type=pathlib.Path, help="Private exact-hash media review receipt")
    args = ap.parse_args()
    print(json.dumps(build(args.root, args.output, check.read_media_review(args.media_review, args.root))))

if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as error:
        print(json.dumps({"error": type(error).__name__, "message": "Packaging incomplete; check the declared public scope, checker findings and media review."}))
        sys.exit(1)

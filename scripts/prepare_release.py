#!/usr/bin/env python3
"""Create a checked public source copy outside the development directory."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import sys
sys.dont_write_bytecode = True
import check_public_content as check

LOCALES = ('en', 'zh-CN', 'ja', 'de', 'fr', 'es', 'pt-BR', 'ru')
ROOT_FILES = {'.gitignore', '.gitattributes', 'LICENSE', 'README.md'} | {
    'README.' + lang + '.md' for lang in LOCALES if lang != 'en'}
ROOT_DIRS = {'docs', 'skills', 'templates', 'examples', 'scripts', 'assets', '.github'}
RUNTIME_DIRS = {'.git', '.vs', '.vscode', '.idea', '__pycache__', '.venv', 'node_modules', 'build', 'dist', '.astro'}


def public_snapshot(root):
    root = root.resolve()
    if not root.is_dir():
        raise ValueError('Source directory does not exist')
    files, excluded = {}, []
    def unreadable_directory(error):
        raise error

    for current, dirs, names in os.walk(root, followlinks=False, onerror=unreadable_directory):
        parent = Path(current)
        for name in list(dirs):
            path = parent / name
            rel = path.relative_to(root).as_posix()
            attrs = path.lstat()
            if path.is_symlink() or getattr(attrs, 'st_file_attributes', 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                raise ValueError('Linked/reparse directory in public input')
            if name in RUNTIME_DIRS:
                dirs.remove(name)
                excluded.append({'path': rel + '/', 'reason': 'development-runtime-directory'})
            elif parent == root and name not in ROOT_DIRS:
                raise ValueError('Undeclared root directory; review public file scope')
        for name in sorted(names):
            path = parent / name
            rel = path.relative_to(root).as_posix()
            attrs = path.lstat()
            if path.is_symlink() or getattr(attrs, 'st_file_attributes', 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                raise ValueError('Linked/reparse file in public input')
            if name == '.DS_Store' or name.startswith('._') or name.endswith(('.pyc', '.pyo')):
                excluded.append({'path': rel, 'reason': 'development-runtime-file'})
                continue
            if parent == root and name not in ROOT_FILES:
                raise ValueError('Undeclared root file; review public file scope')
            if not stat.S_ISREG(attrs.st_mode):
                raise ValueError('Nonregular public input')
            if attrs.st_size > check.MAX_FILE:
                files[rel] = ('oversize', b'')
            else:
                files[rel] = ('regular', path.read_bytes())
            if len(files) > check.MAX_FILES:
                raise ValueError('Public file count exceeds checker limit')
    return dict(sorted(files.items())), sorted(excluded, key=lambda row: row['path'])


def validated_source(root, media_receipt=None):
    files, excluded = public_snapshot(root)
    unresolved, reviewed = check.media_review(files, check.inspect(files, 'gitguard'), media_receipt)
    if unresolved:
        raise ValueError('Public source has unresolved findings: ' + json.dumps(unresolved))
    manifest = {name: hashlib.sha256(raw).hexdigest() for name, (_, raw) in files.items()}
    return files, {'scope': 'Explicit public source; development directories excluded, originals preserved',
                   'files': manifest, 'excluded': excluded, 'reviewed_media': reviewed,
                   'unresolved_findings': []}


def write_source(files, target):
    for name, (kind, raw) in files.items():
        if kind != 'regular':
            raise ValueError('Unchecked nonregular source')
        path = target / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)


def build(root, output, media_receipt=None):
    root, output = root.resolve(), output.resolve()
    if output.exists() or output == root or output.is_relative_to(root) or root.is_relative_to(output):
        raise ValueError('Use a new output directory outside source')
    files, report = validated_source(root, media_receipt)
    output.mkdir(parents=True)
    write_source(files, output / 'source')
    (output / 'REVIEW.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    return {'files': len(files), 'reviewed_media': len(report['reviewed_media']),
            'excluded_development_items': len(report['excluded']), 'published': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--media-review', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.root, args.output, check.read_media_review(args.media_review, args.root))))
    except (ValueError, OSError) as error:
        print(json.dumps({'error': type(error).__name__, 'message': 'Release preparation did not pass; review source scope and checker findings.'}))
        sys.exit(1)

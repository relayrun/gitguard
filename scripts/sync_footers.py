#!/usr/bin/env python3
"""Plan or synchronize Markdown footers from one shared brand template.

Planning is read-only by default. Select explicit --page paths or --all.
Use --write to apply the displayed selection, or --check for a CI check.
"""

import argparse
import difflib
import sys
from pathlib import Path
from string import Template

START = '<!-- relayrun-footer -->'
END = '<!-- /relayrun-footer -->'
SKIP_DIRS = {'.git', '.venv', 'node_modules', 'build', 'dist', '__pycache__'}


def checked_page(root, relative):
    """Require a regular Markdown page inside the selected project."""
    relative = Path(relative)
    if relative.is_absolute() or '..' in relative.parts or relative.suffix != '.md':
        raise ValueError('Select project-relative Markdown paths without parent traversal.')
    page = root / relative
    if not page.is_file() or page.resolve() != page:
        raise ValueError('A selected page is missing or uses a symbolic link.')
    page.resolve().relative_to(root)
    return page


def footer_for(root, relative):
    relative = Path(relative)
    prefix = '../' * (len(relative.parts) - 1)
    template = (root / 'assets/brand/footer.md.in').read_text(encoding='utf-8')
    footer = Template(template).substitute(root=prefix).rstrip() + '\n'
    if footer.count(START) != 1 or footer.count(END) != 1:
        raise ValueError('The shared template must contain one complete footer block.')
    return footer


def proposed_update(root, relative):
    root = Path(root).resolve()
    page = checked_page(root, relative)
    original = page.read_bytes()
    text = original.decode('utf-8')
    newline = '\r\n' if '\r\n' in text else '\n'
    footer = footer_for(root, relative)
    if text.count(START) > 1 or text.count(END) > 1:
        raise ValueError('Ambiguous footer markers; no update planned.')
    if END in text and (START not in text or text.index(END) < text.index(START)):
        raise ValueError('Unmatched footer end marker; no update planned.')
    if START in text:
        body, tail = text.split(START, 1)
        if END not in tail:
            raise ValueError('Incomplete footer block; no update planned.')
        if tail.split(END, 1)[1].strip():
            raise ValueError('Content follows the managed footer; no update planned.')
    else:
        body = text + (newline if text.endswith('\n') else newline * 2)
    updated = (body + footer.replace('\n', newline)).encode('utf-8')
    return page, original, updated


def reader_pages(root):
    """Reader pages get branding; reusable instructions/template bodies stay clean."""
    return sorted(p.relative_to(root).as_posix() for p in root.rglob('*.md')
                  if not any(part in SKIP_DIRS for part in p.relative_to(root).parts)
                  and p.name != 'SKILL.md'
                  and not (p.relative_to(root).parts[0] == 'templates' and p.name != 'README.md'))


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--page', action='append', help='Explicit relative page; may be repeated')
    selection.add_argument('--all', action='store_true', help='All reader Markdown pages; excludes SKILL files and reusable template bodies')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--write', action='store_true', help='Apply the selected footer updates')
    mode.add_argument('--check', action='store_true', help='Exit 1 if a selected footer is stale; no writes')
    parser.add_argument('--diff', action='store_true', help='Print the complete proposed differences')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    if args.all:
        pages = reader_pages(root)
    else:
        pages = list(dict.fromkeys(args.page))
    try:
        # Validate every selected page before writing any page.
        planned = [proposed_update(root, relative) for relative in pages]
    except (OSError, ValueError, KeyError, UnicodeError) as error:
        parser.exit(2, str(error) + '\n')
    changes = [(page, old, new) for page, old, new in planned if old != new]
    for page, old, new in changes:
        name = page.relative_to(root).as_posix()
        print(('UPDATE ' if args.write else 'WOULD UPDATE ') + name)
        if args.diff:
            print(''.join(difflib.unified_diff(old.decode('utf-8').splitlines(True),
                                             new.decode('utf-8').splitlines(True),
                                             fromfile=name, tofile=name)), end='')
    if args.write:
        # Detect intervening edits before applying this already validated selection.
        if any(page.read_bytes() != old for page, old, _ in planned):
            parser.exit(2, 'A page changed after planning; no updates applied.\n')
        for page, _, new in changes:
            page.write_bytes(new)
    print(f'{len(pages)} page(s) checked; {len(changes)} footer update(s)' +
          (' applied.' if args.write else ' planned. No files written.'))
    return 1 if args.check and changes else 0


if __name__ == '__main__':
    raise SystemExit(main())

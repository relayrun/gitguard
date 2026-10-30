#!/usr/bin/env python3
"""Behavior tests using fabricated data and disposable local repositories only."""
import contextlib
import importlib.util
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
import check_public_content as check

class ContentTests(unittest.TestCase):
    def test_valid_relative_links(self):
        files = {"README.md": ("regular", b"[Guide](docs/start.md)"),
                 "docs/start.md": ("regular", b"[Home](../README.md)")}
        self.assertEqual(check.inspect(files), [])

    def test_urls_and_mounts_are_not_host_paths(self):
        text = "https://example.com/guide http://service:6610/ ./nginx.conf:/etc/nginx/default.conf:ro"
        self.assertFalse(check.inspect({"README.md": ("regular", text.encode())}))

    def test_missing_and_escaping_links(self):
        result = check.inspect({"README.md": ("regular", b"[Missing](missing.md) [Outside](../private.md)")})
        self.assertEqual({x["category"] for x in result}, {"missing-local-link", "link-outside-package"})

    def test_secret_reporting_does_not_echo_value(self):
        fake = "gh" + "p_" + "a" * 36
        result = check.inspect({"note.md": ("regular", fake.encode())})
        self.assertEqual(result[0]["category"], "github-token")
        self.assertNotIn(fake, json.dumps(result))

    def test_machine_paths_and_private_addresses(self):
        synthetic = "/Us" + "ers/test-reader/project 192." + "168.5.6"
        result = check.inspect({"note.md": ("regular", synthetic.encode())})
        self.assertEqual({x["category"] for x in result}, {"machine-path", "private-address"})
        windows = "Z" + ":/" + "example-workspace/file.txt"
        windows_result = check.inspect({"note.md": ("regular", windows.encode())})
        self.assertEqual([x["category"] for x in windows_result], ["machine-path"])

    def test_nonregular_and_binary(self):
        files = {"link.md": ("symlink", b""), "artifact.bin": ("regular", b"\x00\xfe"),
                 "large.md": ("oversize", b"")}
        self.assertEqual(len(check.inspect(files)), 3)

    def test_public_profile_and_generic_template(self):
        files = {"AGENTS.md": ("regular", b"Private entry"),
                 "templates/agent-entry.example.md": ("regular", b"Generic example")}
        self.assertEqual(len(check.inspect(files, "gitguard")), 1)
        self.assertEqual(check.inspect(files, "generic"), [])

    def test_real_index_and_deleted_history(self):
        fake = ("gh" + "p_" + "b" * 36).encode()
        with tempfile.TemporaryDirectory(prefix="gitguard-check-fixture-") as d:
            root = pathlib.Path(d).resolve()
            hooks = root / "empty-hooks"
            hooks.mkdir()
            env = os.environ.copy()
            env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
            def run(*args):
                r = subprocess.run(["git", "-c", "core.hooksPath="+str(hooks),
                                    "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                                    "-c", "commit.gpgsign=false", "-C", str(root), *args],
                                   env=env, capture_output=True, timeout=20)
                self.assertEqual(r.returncode, 0, "Disposable Git fixture command failed")
                return r.stdout
            run("init", "-q")
            (root / "README.md").write_text("Clean fixture\n")
            run("add", "README.md"); run("commit", "-qm", "Clean initial fixture")
            (root / "note.md").write_bytes(fake)
            run("add", "note.md")
            # Worktree cleaned while staged bytes still contain a fabricated token.
            (root / "note.md").write_text("Clean working file\n")
            self.assertEqual(check.inspect(check.working_snapshot(root)), [])
            self.assertTrue(any(x["category"] == "github-token" for x in check.inspect(check.git_snapshot(root))))
            run("commit", "-qm", "Fabricated historical token")
            # Remove from the next commit; only history retains it.
            (root / "note.md").unlink()
            run("add", "-u"); run("commit", "-qm", "Remove fixture note")
            self.assertEqual(check.inspect(check.git_snapshot(root, "HEAD")), [])
            self.assertTrue(any(x["category"] == "github-token" for x in check.inspect(check.git_snapshot(root, "HEAD~1"))))
            result = subprocess.run([sys.executable, "-B", str(pathlib.Path(check.__file__).resolve()),
                                     "--root", str(root), "--history", "HEAD~2..HEAD"],
                                    capture_output=True, text=True, timeout=25)
            self.assertEqual(result.returncode, 1)
            self.assertNotIn(fake.decode(), result.stdout)
            self.assertEqual(json.loads(result.stdout.splitlines()[-1])["snapshots"], 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)

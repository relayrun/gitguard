"""Release-boundary and standalone-package regression tests with invented data."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile
import check_public_content as check
import prepare_release as release
import package_skills


class ReleaseTests(unittest.TestCase):
    def fixture(self, root):
        files = {
            'README.md': '[Guide](docs/en/start.md)\n![Brand](assets/brand/sample.png)\n',
            'LICENSE': 'Invented fixture license\n',
            'docs/en/start.md': '[Home](../../README.md)\n',
            'scripts/check_public_content.py': '# invented fixture\n',
        }
        for name in package_skills.NAMES:
            files['skills/'+name+'/SKILL.md'] = '# Sample\n[Guide](../../docs/en/start.md)\n[Checker](../../scripts/check_public_content.py)\n'
        for name, body in files.items():
            p = root/name; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(body, encoding='utf-8')
        media = root/'assets/brand/sample.png'; media.parent.mkdir(parents=True, exist_ok=True)
        media.write_bytes(b'\x89PNG\r\n\x00invented-media')
        return {'assets/brand/sample.png': hashlib.sha256(media.read_bytes()).hexdigest()}

    def test_runtime_is_declared_and_not_read_or_deleted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'source'; root.mkdir(); self.fixture(root)
            private=root/'.vs/cache'; private.parent.mkdir(); private.write_bytes(b'private fixture')
            original=Path.read_bytes
            def guarded(p):
                if '.vs' in p.parts: raise PermissionError('Occupied fixture')
                return original(p)
            with patch.object(Path,'read_bytes',guarded):
                files, exclusions=release.public_snapshot(root)
            self.assertNotIn('.vs/cache',files)
            self.assertEqual(exclusions,[{'path':'.vs/','reason':'development-runtime-directory'}])
            self.assertTrue(private.is_file())

    def test_unreadable_file_does_not_hide_other_findings(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/'locked').write_text('fixture')
            (root/'secret.txt').write_text('gh'+'p_'+'x'*36)
            original=Path.read_bytes
            def guarded(p):
                if p.name=='locked': raise PermissionError('Occupied fixture')
                return original(p)
            with patch.object(Path,'read_bytes',guarded):
                findings=check.inspect(check.working_snapshot(root))
            self.assertEqual({f['category'] for f in findings},{'unreadable','github-token'})

    def test_unknown_files_require_scope_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); self.fixture(root)
            (root/'unexpected.txt').write_text('fixture')
            with self.assertRaises(ValueError): release.public_snapshot(root)

    def test_unreadable_directory_stops_release_instead_of_skipping_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); self.fixture(root)
            def denied_walk(path, **options):
                options['onerror'](PermissionError('Unreadable public fixture directory'))
                return iter(())
            with patch.object(release.os, 'walk', denied_walk):
                with self.assertRaises(PermissionError):
                    release.build(root,root.parent/(root.name+'-release'))

    def test_media_receipt_cannot_approve_secrets_or_changed_bytes(self):
        fake=('gh'+'p_'+'x'*36).encode()
        files={'assets/sample.png':('regular',b'\x00media'), 'secret.txt':('regular',fake)}
        receipt={p:hashlib.sha256(raw).hexdigest() for p,(_,raw) in files.items()}
        outstanding, reviewed=check.media_review(files,check.inspect(files),receipt)
        self.assertEqual([f['category'] for f in outstanding],['github-token'])
        self.assertEqual(len(reviewed),1)
        files['assets/sample.png']=('regular',b'\x00changed')
        outstanding, reviewed=check.media_review(files,check.inspect(files),receipt)
        self.assertEqual(len(outstanding),2); self.assertFalse(reviewed)

    def test_standalone_packages_keep_all_references_and_license(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'source'; root.mkdir(); media=self.fixture(root)
            with self.assertRaises(ValueError): package_skills.build(root,Path(tmp)/'refused')
            out=Path(tmp)/'packages'
            receipts=package_skills.build(root,out,media)
            self.assertEqual(len(receipts),2)
            for name in package_skills.NAMES:
                isolated=Path(tmp)/'isolated'/name
                with zipfile.ZipFile(out/(name+'.zip')) as archive:
                    self.assertIsNone(archive.testzip())
                    archive.extractall(isolated)
                folder=isolated/name
                self.assertIn('references/source/docs/en/start.md',(folder/'SKILL.md').read_text())
                self.assertTrue((folder/'references/source/LICENSE').is_file())
                scoped={'references/source/'+p:sha for p,sha in media.items()}
                files=check.working_snapshot(folder)
                pending,_=check.media_review(files,check.inspect(files),scoped)
                self.assertEqual(pending,[])


if __name__ == '__main__':
    unittest.main()

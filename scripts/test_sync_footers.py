"""Safety and path tests for the footer generator, using isolated fixtures."""
from pathlib import Path
import tempfile
import unittest

from sync_footers import END, START, footer_for, proposed_update, reader_pages


# Temporary sample bodies, not published page content. Exercise text preservation
# and both root/nested reader paths for every supported language.
LANGUAGE_BODIES = {
    'en': '# Original content\n\nKeep this text unchanged.\n\n',
    'zh-CN': '# 原始内容\n\n保留这段文字，不作修改。\n\n',
    'ja': '# 元の内容\n\nこの文章を変更せずに保持します。\n\n',
    'de': '# Ursprünglicher Inhalt\n\nDiesen Text unverändert lassen.\n\n',
    'fr': '# Contenu original\n\nConserver ce texte sans modification.\n\n',
    'es': '# Contenido original\n\nConservar este texto sin cambios.\n\n',
    'pt-BR': '# Conteúdo original\n\nManter este texto sem alterações.\n\n',
    'ru': '# Исходное содержимое\n\nСохранить этот текст без изменений.\n\n',
}
PAGE_CASES = tuple(
    (relative, prefix, body)
    for language, body in LANGUAGE_BODIES.items()
    for relative, prefix in (
        ('README.md' if language == 'en' else f'README.{language}.md', ''),
        (f'docs/{language}/README.md', '../../'),
    )
)


class FooterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='gitguard-footer-test-')
        self.root = Path(self.temp.name).resolve()
        template = Path(__file__).resolve().parent.parent / 'assets/brand/footer.md.in'
        destination = self.root / 'assets/brand/footer.md.in'
        destination.parent.mkdir(parents=True)
        destination.write_bytes(template.read_bytes())

    def tearDown(self):
        self.temp.cleanup()

    def page(self, relative, content):
        page = self.root / relative
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_bytes(content.encode('utf-8'))
        return page

    def test_all_eight_languages_use_shared_footer_and_correct_paths(self):
        for relative, prefix, body in PAGE_CASES:
            with self.subTest(relative=relative):
                page = self.page(relative, body)
                _, before, after = proposed_update(self.root, relative)
                self.assertEqual(page.read_bytes(), before)  # Planning is read-only.
                text = after.decode('utf-8')
                self.assertIn(f'src="{prefix}assets/brand/relayrun-lockup.png"', text)
                self.assertIn('[WWW.RELAYRUN.NET](https://www.relayrun.net/)', text)
                self.assertNotIn('LICENSE', text)
                self.assertNotIn('MIT', text)

    def test_updates_complete_footer_without_changing_body(self):
        for relative, _, body in PAGE_CASES:
            with self.subTest(relative=relative):
                previous_footer = footer_for(self.root, relative).replace('width="128"', 'width="256"')
                self.page(relative, body + previous_footer)
                _, _, updated = proposed_update(self.root, relative)
                self.assertEqual(updated.decode('utf-8').split(START)[0], body)
                self.assertIn(b'width="128" height="128"', updated)
                self.assertNotIn(b'LICENSE', updated)

    def test_repeat_is_idempotent_and_template_change_reaches_each_page(self):
        for relative, _, body in PAGE_CASES:
            with self.subTest(relative=relative):
                page = self.page(relative, body)
                _, _, generated = proposed_update(self.root, relative)
                page.write_bytes(generated)
                self.assertEqual(proposed_update(self.root, relative)[1:], (generated, generated))
        template = self.root / 'assets/brand/footer.md.in'
        template.write_text(template.read_text(encoding='utf-8').replace('width="128"', 'width="120"'), encoding='utf-8')
        for relative, _, _ in PAGE_CASES:
            with self.subTest(relative=relative):
                self.assertIn(b'width="120"', proposed_update(self.root, relative)[2])

    def test_retains_crlf_and_body(self):
        for relative, _, body in PAGE_CASES:
            with self.subTest(relative=relative):
                original = (body + footer_for(self.root, relative)).replace('\n', '\r\n')
                self.page(relative, original)
                _, before, after = proposed_update(self.root, relative)
                self.assertEqual(before, after)

    def test_rejects_unmanaged_trailing_text_and_ambiguous_markers(self):
        for tail in (START, START + '\nUnfinished footer', START + '\n' + START,
                     START + '\n' + END + '\nUser text', END + '\n' + START,
                     END, START + '\n' + END + '\n' + END):
            with self.subTest(tail=tail):
                original = '# Body\n\n' + tail
                page = self.page('README.md', original)
                with self.assertRaises(ValueError):
                    proposed_update(self.root, 'README.md')
                self.assertEqual(page.read_bytes(), original.encode())

    def test_rejects_paths_outside_project_and_non_markdown(self):
        for relative in ('../outside.md', str(self.root.parent / 'outside.md'), 'LICENSE'):
            with self.subTest(relative=relative), self.assertRaises(ValueError):
                proposed_update(self.root, relative)

    def test_bulk_selection_preserves_adoptable_templates_and_machine_skills(self):
        localized_readers = [f'docs/{language}/workflow.md' for language in LANGUAGE_BODIES]
        pages = ['README.md', 'templates/README.md', 'templates/handoff.md',
                 'skills/README.md', 'skills/example/SKILL.md'] + localized_readers
        for relative in pages:
            self.page(relative, '# Original instructions\n')
        self.assertEqual(reader_pages(self.root),
                         sorted(['README.md', 'skills/README.md', 'templates/README.md'] + localized_readers))
        self.assertEqual((self.root/'skills/example/SKILL.md').read_text(), '# Original instructions\n')


if __name__ == '__main__':
    unittest.main()

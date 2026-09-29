from pathlib import Path
import importlib.util
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validate', ROOT / 'scripts/validate.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'investigate-customer'
        shutil.copytree(ROOT / 'skills/operations/investigate-customer', self.path)

    def test_every_skill_can_be_copied_independently(self):
        for source in (ROOT / 'skills').glob('*/*/SKILL.md'):
            with self.subTest(skill=source.parent.name), tempfile.TemporaryDirectory() as directory:
                target = Path(directory) / source.parent.name
                shutil.copytree(source.parent, target)
                self.assertEqual(module.validate_skill(target), [])

    def test_missing_feedback_reference_is_rejected(self):
        (self.path / 'references/feedback-loop.md').unlink()
        self.assertTrue(any('feedback-loop' in e for e in module.validate_skill(self.path)))

    def test_external_relative_dependency_breaks_portability(self):
        with (self.path / 'SKILL.md').open('a') as f:
            f.write('\n[Required context](../../private.md)\n')
        self.assertTrue(any('escapes' in e for e in module.validate_skill(self.path)))

    def test_private_path_in_correction_is_rejected(self):
        with (self.path / 'SKILL.md').open('a') as f:
            f.write('\nRead /Users/example/private/customer-record.json\n')
        self.assertTrue(any('private data' in e for e in module.validate_skill(self.path)))

    def test_general_correction_and_regression_remain_installable(self):
        # Tests packaging of an actual writable correction, not agent judgment.
        with (self.path / 'SKILL.md').open('a') as f:
            f.write('\nWhen account emails conflict, preserve unresolved candidates until an explicit provider mapping disambiguates them.\n')
        with (self.path / 'references/regression-cases.md').open('a') as f:
            f.write('\nInput: Two records share an email; neither has a mapping. Expected: report unresolved identity and do not mutate either.\n')
        self.assertEqual(module.validate_skill(self.path), [])

    def test_wrong_name_rejected(self):
        f = self.path / 'SKILL.md'
        f.write_text(f.read_text().replace('name: investigate-customer', 'name: another-skill', 1))
        self.assertTrue(any('name' in e for e in module.validate_skill(self.path)))

    def test_catalog_matches_published_files(self):
        self.assertEqual(module.validate_repo(ROOT), [])

if __name__ == '__main__':
    unittest.main()

"""Negative controls for the fixture and assessor, not tests of model reliability."""

from pathlib import Path
import tempfile
import subprocess
import unittest

from assess_fixture import assess
from create_fixture import create_fixture


class HarnessTests(unittest.TestCase):
    def test_archived_agent_patch_passes_independent_assessment(self):
        patch = Path(__file__).parent / 'results/2026-09-05/candidate.patch'
        with tempfile.TemporaryDirectory() as directory:
            repo = create_fixture(Path(directory) / 'repo')
            subprocess.run(['git', 'apply', str(patch.resolve())], cwd=repo, check=True)
            result = assess(repo, repo)
            self.assertTrue(result['passed'], result)

    def test_seeded_defects_are_detected_despite_green_wrapper(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = create_fixture(Path(directory) / 'repo')
            result = assess(repo, repo)
            checks = {check['name']: check['passed'] for check in result['checks']}
            self.assertFalse(result['passed'])
            self.assertTrue(checks['canonical-clean'])  # The intentionally lying wrapper.
            for name in ('original-acceptance-tests', 'child-failure-propagates',
                         'teardown-failure-propagates', 'independent-invariants',
                         'post-verification-mutation-detected'):
                self.assertFalse(checks[name], name)
            self.assertTrue(checks['user-work:user-notes.txt'])
            self.assertTrue(checks['user-work:user-scratch.txt'])

    def test_creation_never_overwrites_existing_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory) / 'repo'
            repo.mkdir()
            sentinel = repo / 'keep.txt'
            sentinel.write_text('existing user work')
            with self.assertRaises(FileExistsError):
                create_fixture(repo)
            self.assertEqual(sentinel.read_text(), 'existing user work')


if __name__ == '__main__':
    unittest.main()

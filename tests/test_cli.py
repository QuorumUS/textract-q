import os
import shutil
import tempfile
import unittest

from argcomplete import CompletionFinder

from textract.cli import get_parser


class CliCompletionTestCase(unittest.TestCase):
    """Make sure that shell completion of the filename argument works."""

    def setUp(self):
        self.directory = tempfile.mkdtemp()
        self.path = os.path.join(self.directory, "document.pdf")
        open(self.path, "w").close()

    def tearDown(self):
        shutil.rmtree(self.directory)

    def test_filename_completion(self):
        finder = CompletionFinder(get_parser())
        prefix = os.path.join(self.directory, "doc")
        self.assertEqual(self.path, finder.rl_complete(prefix, 0).strip())

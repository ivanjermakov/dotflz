import unittest

from dotflz.cli import *
from test.commons import *
from test.test_utils import get_config_path, count_files, tree

DOTFILES_DIR_PATH = 'dotfiles/'
ON = '../test_dir'
PASTE_ON = 'paste'


class TestCliPaste(unittest.TestCase):
    PWD = os.getcwd()

    def setUp(self) -> None:
        create_directory(DYN_TEST_DIR_PATH)
        os.chdir(DYN_TEST_DIR_PATH)
        print(os.getcwd())

    def tearDown(self) -> None:
        os.chdir(TestCliPaste.PWD)
        delete_file(DYN_TEST_DIR_PATH)

    def test_paste2(self):
        self._test_paste(2, 0)

    def test_paste3(self):
        self._test_paste(3, 0)

    def test_paste4(self):
        self._test_paste(4, 0)

    def test_paste5(self):
        self._test_paste(5, 2)

    def test_paste6(self):
        self._test_paste(6, 6)

    def test_paste7(self):
        self._test_paste(7, 7)

    def _test_paste(self, config_num, expect_files):
        copy(get_config_path(config_num), on=ON)
        self.assertEqual(expect_files, count_files(os.getcwd()))
        paste(get_config_path(config_num), on=PASTE_ON)
        tree()
        self.assertEqual(expect_files, count_files(PASTE_ON))

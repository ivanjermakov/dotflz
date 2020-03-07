import unittest

from dotflz.cli import *
from test.commons import *
from test.test_utils import *

DOTFILES_DIR_PATH = 'dotfiles/'
ON = '../test_dir'


class TestCliCopy(unittest.TestCase):
    PWD = os.getcwd()

    def setUp(self) -> None:
        create_directory(DYN_TEST_DIR_PATH)
        os.chdir(DYN_TEST_DIR_PATH)
        print(os.getcwd())

    def tearDown(self) -> None:
        os.chdir(TestCliCopy.PWD)
        delete_file(DYN_TEST_DIR_PATH)

    def test_copy1(self):
        with self.assertRaises(Exception):
            copy(get_config_path(1), on=ON)

    def test_copy1clean(self):
        with self.assertRaises(Exception):
            copy(get_config_path(1), True, on=ON)

    def test_copy2(self):
        self._test_copy(2, 0)

    def test_copy2clean(self):
        self._test_copy(2, 0, True)

    def test_copy3(self):
        self._test_copy(3, 0)

    def test_copy3clean(self):
        self._test_copy(3, 0, True)

    def test_copy4(self):
        self._test_copy(4, 0)

    def test_copy4clean(self):
        self._test_copy(4, 0, True)

    def test_copy5(self):
        self._test_copy(5, 2)

    def test_copy5clean(self):
        self._test_copy(5, 2, True)

    def test_copy6(self):
        self._test_copy(6, 6)

    def test_copy6clean(self):
        self._test_copy(6, 6, True)

    def test_copy7(self):
        self._test_copy(7, 7)

    def test_copy7clean(self):
        self._test_copy(7, 7, True)

    def _test_copy(self, config_num, expect_files, clean=False):
        copy(get_config_path(config_num), clean, on=ON)
        tree()
        self.assertEqual(expect_files, count_files(DOTFILES_DIR_PATH))

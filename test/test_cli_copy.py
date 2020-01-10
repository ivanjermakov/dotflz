import unittest

from dotflz.cli import *
from dotflz.parser import *
from test.commons import *


def get_config_path(config_number):
    return f'../config/{config_number}.yml'


class TestCliVerify(unittest.TestCase):
    PWD = os.getcwd()

    def setUp(self) -> None:
        create_directory(DYN_TEST_DIR_PATH)
        os.chdir(DYN_TEST_DIR_PATH)

    def tearDown(self) -> None:
        os.chdir(TestCliVerify.PWD)
        delete_file(DYN_TEST_DIR_PATH)

    def test_copy1(self):
        with self.assertRaises(Exception):
            copy(get_config_path(1))

    def test_copy2(self):
        copy(get_config_path(2))

    def test_copy3(self):
        copy(get_config_path(3))

    def test_copy4(self):
        copy(get_config_path(4))

    def test_copy5(self):
        copy(get_config_path(5))

    def test_copy6(self):
        copy(get_config_path(6))

    def test_copy7(self):
        copy(get_config_path(7))

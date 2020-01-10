import unittest

from dotflz.cli import *
from dotflz.parser import *
from test.commons import *


def get_config_path(config_number):
    return f'../config/{config_number}.yml'


class TestCliVerify(unittest.TestCase):
    PWD = os.getcwd()

    def setUp(self) -> None:
        os.chdir(TEST_DIR_PATH)

    def tearDown(self) -> None:
        os.chdir(TestCliVerify.PWD)

    def test_verify1(self):
        with self.assertRaises(Exception):
            verify(get_config_path(1))

    def test_verify2(self):
        verify(get_config_path(2))

    def test_verify3(self):
        verify(get_config_path(3))

    def test_verify4(self):
        verify(get_config_path(4))

    def test_verify5(self):
        verify(get_config_path(5))

    def test_verify6(self):
        verify(get_config_path(6))

    def test_verify7(self):
        verify(get_config_path(7))

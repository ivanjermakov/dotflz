import unittest

from dotflz.parser import *
from test.commons import *


def get_config_path(config_number):
    return f'../config/{config_number}.yml'


class TestParser(unittest.TestCase):
    PWD = os.getcwd()
    ON = '.'

    def setUp(self) -> None:
        os.chdir(TEST_DIR_PATH)

    def tearDown(self) -> None:
        os.chdir(TestParser.PWD)

    def test_not_parse_empty_config(self):
        """
        Parse configuration file 1
        """
        with self.assertRaises(AttributeError):
            parse_config(get_config_path(1), TestParser.ON)

    def test_parse_empty_valid_config(self):
        """
        Parse configuration file 2
        """
        config = parse_config(get_config_path(2), TestParser.ON)
        self.assertEqual('dotfiles/', config.name)
        self.assertEqual(0, len(config.items))

    def test_parse_config_3(self):
        config = parse_config(get_config_path(3), TestParser.ON)
        self.assertEqual(1, len(config.items))
        item = config.items[0]
        self.assertEqual('a', item.name)
        self.assertEqual('./a/', item.frm)
        self.assertEqual('a/', item.to)
        self.assertEqual(0, len(item.files))

    def test_parse_config_4(self):
        config = parse_config(get_config_path(4), TestParser.ON)
        item = config.items[0]
        self.assertEqual('a/', item.to)

    def test_parse_config_5(self):
        config = parse_config(get_config_path(5), TestParser.ON)
        item = config.items[0]
        self.assertEqual(2, len(item.files))
        self.assertEqual('c.html', item.files[0])
        self.assertEqual('c.txt', item.files[1])

    def test_parse_config_6(self):
        config = parse_config(get_config_path(6), TestParser.ON)
        self.assertEqual(4, len(config.items))
        self.assertEqual(2, len(config.items[3].files))
        self.assertEqual('ca/c.html', config.items[2].files[0])
        self.assertEqual('b.xml', config.items[3].files[1])

    def test_parse_config_7(self):
        config = parse_config(get_config_path(7), TestParser.ON)
        self.assertEqual(3, len(config.items[2].files))
        self.assertEqual(2, len(config.items[3].files))

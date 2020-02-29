import unittest

from dotflz.cli import *
from dotflz.parser import *
from test.commons import *

DOTFILES_DIR_PATH = 'dotfiles/'
ON = '../test_dir'


def get_config_path(config_number):
    return f'../config/{config_number}.yml'


def count_files(path):
    return sum([len(files) for r, d, files in os.walk(path)])


def print_tree():
    click.echo('tree:')
    for root, dirs, files in os.walk(DOTFILES_DIR_PATH):
        level = root.count(os.sep) if os.path.basename(root) else 0
        indent = '└───' * level
        click.echo('{}{}/'.format(indent, os.path.basename(root)))
        subindent = '    ' * (level) + '└───'
        for f in files:
            click.echo('{}{}'.format(subindent, f))


class TestCliCopy(unittest.TestCase):
    PWD = os.getcwd()

    def setUp(self) -> None:
        create_directory(DYN_TEST_DIR_PATH)
        os.chdir(DYN_TEST_DIR_PATH)

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
        copy(get_config_path(2), on=ON)
        print_tree()
        self.assertEqual(0, count_files(DOTFILES_DIR_PATH))

    def test_copy2clean(self):
        copy(get_config_path(2), True, on=ON)
        print_tree()
        self.assertEqual(0, count_files(DOTFILES_DIR_PATH))

    def test_copy3(self):
        copy(get_config_path(3), on=ON)
        print_tree()
        self.assertEqual(0, count_files(DOTFILES_DIR_PATH))

    def test_copy3clean(self):
        copy(get_config_path(3), True, on=ON)
        print_tree()
        self.assertEqual(0, count_files(DOTFILES_DIR_PATH))

    def test_copy4(self):
        copy(get_config_path(4), on=ON)
        print_tree()
        self.assertEqual(0, count_files(DOTFILES_DIR_PATH))

    def test_copy4clean(self):
        copy(get_config_path(4), True, on=ON)
        print_tree()
        self.assertEqual(0, count_files(DOTFILES_DIR_PATH))

    def test_copy5(self):
        copy(get_config_path(5), on=ON)
        print_tree()
        self.assertEqual(2, count_files(DOTFILES_DIR_PATH))

    def test_copy5clean(self):
        copy(get_config_path(5), True, on=ON)
        print_tree()
        self.assertEqual(2, count_files(DOTFILES_DIR_PATH))

    def test_copy6(self):
        copy(get_config_path(6), on=ON)
        print_tree()
        self.assertEqual(6, count_files(DOTFILES_DIR_PATH))

    def test_copy6clean(self):
        copy(get_config_path(6), True, on=ON)
        print_tree()
        self.assertEqual(6, count_files(DOTFILES_DIR_PATH))

    def test_copy7(self):
        copy(get_config_path(7), on=ON)
        print_tree()
        self.assertEqual(7, count_files(DOTFILES_DIR_PATH))

    def test_copy7clean(self):
        copy(get_config_path(7), True, on=ON)
        print_tree()
        self.assertEqual(7, count_files(DOTFILES_DIR_PATH))

import unittest

from dotflz.filesystem import *
from test.commons import *


class TestFilesystem(unittest.TestCase):
    TEST_FILE_PATH = 'testfile'
    TEST_FILE_FULL_PATH = DYN_TEST_DIR_PATH + TEST_FILE_PATH
    COPY_TEST_FILE_PATH = 'testfile2'
    COPY_TEST_FILE_FULL_PATH = DYN_TEST_DIR_PATH + COPY_TEST_FILE_PATH

    def test_create_directory(self):
        create_directory(DYN_TEST_DIR_PATH)
        self.assertTrue(os.path.exists(DYN_TEST_DIR_PATH))
        delete_file(DYN_TEST_DIR_PATH)

    def test_delete_file_as_directory(self):
        create_directory(DYN_TEST_DIR_PATH)
        delete_file(DYN_TEST_DIR_PATH)
        self.assertFalse(os.path.exists(DYN_TEST_DIR_PATH))

    def test_create_file(self):
        create_directory(DYN_TEST_DIR_PATH)
        create_file(TestFilesystem.TEST_FILE_FULL_PATH)
        self.assertTrue(os.path.exists(TestFilesystem.TEST_FILE_FULL_PATH))
        delete_file(DYN_TEST_DIR_PATH)

    def test_delete_file_as_file(self):
        create_directory(DYN_TEST_DIR_PATH)
        create_file(TestFilesystem.TEST_FILE_FULL_PATH)
        delete_file(TestFilesystem.TEST_FILE_FULL_PATH)
        self.assertFalse(os.path.exists(TestFilesystem.TEST_FILE_FULL_PATH))
        delete_file(DYN_TEST_DIR_PATH)

    def test_copy_file(self):
        create_directory(DYN_TEST_DIR_PATH)
        create_file(TestFilesystem.TEST_FILE_FULL_PATH)
        copy_file(TestFilesystem.TEST_FILE_FULL_PATH, TestFilesystem.COPY_TEST_FILE_FULL_PATH)
        self.assertTrue(os.path.exists(TestFilesystem.TEST_FILE_FULL_PATH))
        self.assertTrue(os.path.exists(TestFilesystem.COPY_TEST_FILE_FULL_PATH))
        delete_file(DYN_TEST_DIR_PATH)

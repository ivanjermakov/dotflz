from dotflz.filesystem import *

from test.commons import *


def create_directory(path):
    create_directory(path)


def delete_directory(path):
    delete_file(path)


def read_file(path):
    with open(path, 'r') as file:
        return file.read()


def get_config_path(config_number):
    return f'{CONFIG_DIR_PATH}{config_number}.yml'


def load_config(config_number):
    return read_file(get_config_path(config_number))

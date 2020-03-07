import os


def get_config_path(config_number):
    return f'../config/{config_number}.yml'


def count_files(path):
    return sum([len(files) for r, d, files in os.walk(path)])

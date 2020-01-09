from dotflz.filesystem import *


def create_directory(path):
    create_directory(path)


def delete_directory(path):
    delete_file(path)


def read_file(path):
    with open(path, 'r') as file:
        return file.read()

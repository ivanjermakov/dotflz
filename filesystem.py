import os
import subprocess

import click


def delete_file(name):
    subprocess.run(['bash', '-c', " ".join(['rm', '-r', name])], check=True)


def copy_file(from_path, to_path):
    click.echo('Copying file: {} -> {}'.format(from_path, to_path))
    os.makedirs(to_path, exist_ok=True)
    subprocess.run(['bash', '-c', " ".join(['cp', from_path, to_path])])


def mkdir(path):
    os.makedirs(path, exist_ok=True)

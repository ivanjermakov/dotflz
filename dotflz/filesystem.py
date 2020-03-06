import os
import subprocess

import click


def delete_file(path):
    click.echo('Deleting file: {}'.format(path))
    subprocess.run(['bash', '-c', " ".join(['rm', '-r', path])], check=True)


def create_file(path):
    click.echo('Creating file: {}'.format(path))
    os.makedirs(path, exist_ok=True)
    subprocess.run(['bash', '-c', " ".join(['touch', path])])


def copy_file(from_path, to_path):
    click.echo('Copying file: {} -> {}'.format(from_path, to_path))
    os.makedirs(to_path, exist_ok=True)
    subprocess.run(['bash', '-c', " ".join(['cp', from_path, to_path])])


def create_directory(path):
    click.echo('Creating directory: {}'.format(path))
    os.makedirs(path, exist_ok=True)

import os
import subprocess

import click


def delete_file(path: str) -> None:
    """
    Delete file.
    If file does not exist, it will be ignored

    :param path: path to file
    """
    click.echo('Deleting file: {}'.format(path))
    subprocess.run(['bash', '-c', " ".join(['rm', '-r', path])], check=True)


def create_file(path: str) -> None:
    """
    Create (touch) file.

    :param path: path to file to be created

    :raise exception if path does not exist
    """
    click.echo('Creating file: {}'.format(path))
    os.makedirs(path, exist_ok=True)
    subprocess.run(['bash', '-c', " ".join(['touch', path])])


def copy_file(from_path: str, to_path: str) -> None:
    """
    Copy file non-recursively.

    :param from_path: from file path
    :param to_path: to file path
    """
    click.echo('Copying file: {} -> {}'.format(from_path, to_path))
    os.makedirs(to_path, exist_ok=True)
    # TODO: fix recursiveness since it can cause untracked files being copied
    subprocess.run(['bash', '-c', " ".join(['cp', '-r', from_path, to_path])])


def create_directory(path: str) -> None:
    """
    Create directory.

    :param path: path to new directory
    """
    click.echo('Creating directory: {}'.format(path))
    os.makedirs(path, exist_ok=True)

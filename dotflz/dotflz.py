from datetime import datetime

from dotflz.parser import *


def _parse_config(config_path):
    """
    Parser wrapper with echoing
    :param config_path:
    :return:
    """
    click.echo(f'Config file: {config_path}')
    config = parse_config(config_path)
    click.echo('[\n' + '\n'.join('\t{}'.format(e) for _, e in enumerate(config.items)) + '\n]')
    return config


@click.group('dotflz')
def dotflz():
    """
    Utility to keep copies of dotfiles in one place.
    """
    pass


@dotflz.command(short_help='Copy files by specified configuration file')
@click.argument('config_path')
@click.option('-c', '--clean', is_flag=True, help='Delete files missing from config file.')
def copy(config_path, clean):
    """
    Copy files by according to CONFIG_PATH config file.
    """
    config = _parse_config(config_path)
    if clean:
        click.echo(f'Cleaning folder {config.name}')
        delete_file(config.name)
    for item in config.items:
        item.copy()


@dotflz.command(short_help='Replace original files with ones from configured directory.')
@click.argument('config_path')
def paste(config_path):
    """
    Replace original files with ones from configured directory according to CONFIG_PATH config file.
    """
    config = _parse_config(config_path)
    for item in config.items:
        item.paste()


@dotflz.command(short_help='Verify configuration file.')
@click.argument('config_path')
def verify(config_path):
    """
    Verify configuration file from CONFIG_PATH.
    """
    config = _parse_config(config_path)
    are_files_valid = []
    for entry in config.items:
        are_files_valid.append(entry.is_valid())
    error_count = len(list(filter(lambda e: not e, are_files_valid)))
    click.echo(f'verification complete with {error_count} error{"" if error_count == 1 else "s"}')
    if error_count != 0:
        exit(1)


@dotflz.command(short_help='Backup original files into backup directory.')
@click.argument('config_path')
@click.option('-d', '--dir', help='Backup directory name. Timestamp if not specified.')
@click.option('-c', '--clean', is_flag=True, help='Delete backup directory before copying if such exist.')
def backup(config_path, dir, clean):
    """
    Backup original files into backup directory according to CONFIG_PATH config file.
    """
    config = _parse_config(config_path)
    backup_dir_name = dir if dir else datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    if clean:
        click.echo(f'Cleaning folder {dir}')
        delete_file(dir)
    for item in config.items:
        for file in item.files:
            copy_file(item.frm + file, '{}/{}'.format(backup_dir_name, item.to))


@dotflz.command(short_help='Restore original files with specified backup directory.')
@click.argument('config_path')
@click.argument('backup_dir_name')
def restore(config_path, backup_dir_name):
    """
    Restore original files from BACKUP_DIR_NAME according to CONFIG_PATH config file.
    """
    config = _parse_config(config_path)
    for item in config.items:
        for file in item.files:
            copy_file('{}/{}{}'.format(backup_dir_name, item.to, file), item.frm)

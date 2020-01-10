import click

from dotflz import cli


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
    cli.copy(config_path, clean)


@dotflz.command(short_help='Replace original files with ones from configured directory.')
@click.argument('config_path')
def paste(config_path):
    """
    Replace original files with ones from configured directory according to CONFIG_PATH config file.
    """
    cli.parse_config(config_path)


@dotflz.command(short_help='Verify configuration file.')
@click.argument('config_path')
def verify(config_path):
    """
    Verify configuration file from CONFIG_PATH.
    """
    error_count = cli.verify(config_path)
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
    cli.backup(config_path, dir, clean)


@dotflz.command(short_help='Restore original files with specified backup directory.')
@click.argument('config_path')
@click.argument('backup_dir_name')
def restore(config_path, backup_dir_name):
    """
    Restore original files from BACKUP_DIR_NAME according to CONFIG_PATH config file.
    """
    cli.restore(config_path, backup_dir_name)

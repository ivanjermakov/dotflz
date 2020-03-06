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
@click.option('-o', '--on', help='Context path for relative configuration "from" paths')
def copy(config_path, clean, on):
    """
    Copy files by according to CONFIG_PATH config file.
    """
    cli.copy(config_path, clean, on)


@dotflz.command(short_help='Replace original files with ones from configured directory.')
@click.argument('config_path')
@click.option('-o', '--on', help='Context path for relative configuration "from" paths')
def paste(config_path, on):
    """
    Replace original files with ones from configured directory according to CONFIG_PATH config file.
    """
    cli.paste(config_path, on)


@dotflz.command(short_help='Verify configuration file.')
@click.argument('config_path')
@click.option('-o', '--on', help='Context path for relative configuration "from" paths')
def verify(config_path, on):
    """
    Verify configuration file from CONFIG_PATH.
    """
    error_count = cli.verify(config_path, on)
    if error_count != 0:
        exit(1)


@dotflz.command(short_help='Backup original files into backup directory.')
@click.argument('config_path')
@click.option('-d', '--dir', help='Backup directory name. Timestamp if not specified.')
@click.option('-c', '--clean', is_flag=True, help='Delete backup directory before copying if such exist.')
@click.option('-o', '--on', help='Context path for relative configuration "from" paths')
def backup(config_path, dir, clean, on):
    """
    Backup original files into backup directory according to CONFIG_PATH config file.
    """
    cli.backup(config_path, dir, clean, on)


@dotflz.command(short_help='Restore original files with specified backup directory.')
@click.argument('config_path')
@click.argument('backup_dir_name')
@click.option('-o', '--on', help='Context path for relative configuration "from" paths')
def restore(config_path, backup_dir_name, on):
    """
    Restore original files from BACKUP_DIR_NAME according to CONFIG_PATH config file.
    """
    cli.restore(config_path, backup_dir_name, on)

import click
import pkg_resources

from dotflz import cli

VERSION = f'v{pkg_resources.require("dotflz")[0].version}'
WELCOME_MESSAGE = f"""\

          $$\             $$\       $$$$$$\   $$\           
          $$ |            $$ |     $$  __$$\  $$ |          
     $$$$$$$ |  $$$$$$\ $$$$$$\    $$ /  \__| $$ |$$$$$$$$\ 
    $$  __$$ | $$  __$$\\_$$  _|   $$$$\      $$ |\____$$  |
    $$ /  $$ | $$ /  $$ | $$ |     $$  _|     $$ |  $$$$ _/ 
    $$ |  $$ | $$ |  $$ | $$ |$$\  $$ |       $$ | $$  _/   
    \$$$$$$$ | \$$$$$$  | \$$$$  | $$ |       $$ |$$$$$$$$\ 
     \_______|  \______/   \____/  \__|       \__|\________|
                                              dotflz {VERSION}
"""


@click.group('dotflz', invoke_without_command=True)
@click.pass_context
def dotflz(ctx: click.Context) -> None:
    """
    Utility to keep copies of dotfiles in one place.
    """
    click.echo(WELCOME_MESSAGE)
    click.echo(ctx.get_help())


@dotflz.command(short_help='Copy files by specified configuration file')
@click.argument('config_path')
@click.option('-c', '--clean', is_flag=True, help='Delete files missing from config file.')
@click.option('-o', '--on', help='Context path for relative configuration "from" paths')
def copy(config_path: str, clean: bool, on: str) -> None:
    """
    Copy files by according to CONFIG_PATH config file.
    """
    cli.copy(config_path, clean, on)


@dotflz.command(short_help='Replace original files with ones from configured directory.')
@click.argument('config_path')
@click.option('-o', '--on', help='Context path for relative configuration "from" paths')
def paste(config_path: str, on: str) -> None:
    """
    Replace original files with ones from configured directory according to CONFIG_PATH config file.
    """
    cli.paste(config_path, on)


@dotflz.command(short_help='Verify configuration file.')
@click.argument('config_path')
@click.option('-o', '--on', help='Context path for relative configuration "from" paths')
def verify(config_path: str, on: str) -> None:
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
def backup(config_path: str, dir: str, clean: bool, on: str) -> None:
    """
    Backup original files into backup directory according to CONFIG_PATH config file.
    """
    cli.backup(config_path, dir, clean, on)


@dotflz.command(short_help='Restore original files with specified backup directory.')
@click.argument('config_path')
@click.argument('backup_dir_name')
@click.option('-o', '--on', help='Context path for relative configuration "from" paths')
def restore(config_path: str, backup_dir_name: str, on: str) -> None:
    """
    Restore original files from BACKUP_DIR_NAME according to CONFIG_PATH config file.
    """
    cli.restore(config_path, backup_dir_name, on)

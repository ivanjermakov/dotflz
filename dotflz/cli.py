from datetime import datetime

from dotflz.config import Config
from dotflz.filesystem import *


def _parse_config(config_path: str, on: str, keep_globs: bool = False) -> Config:
    click.echo(f'Config file: {config_path} on {on}')
    config = Config.parse(config_path, on, keep_globs)
    return config


def copy(config_path: str, clean: bool = False, on: str = None) -> None:
    on = on if on else os.getcwd()
    config = _parse_config(config_path, on)
    config.make_dirs()
    if clean:
        click.echo(f'Cleaning folder {config.name}')
        delete_file(config.name)
    for item in config.items:
        item.copy()
    click.echo('Copying complete')


def paste(config_path: str, on: str = None) -> None:
    on = on if on else os.getcwd()
    config = _parse_config(config_path, on, keep_globs=True)
    for item in config.items:
        item.paste()
    click.echo('Pasting complete')


def verify(config_path: str, on: str = None) -> int:
    on = on if on else os.getcwd()
    config = _parse_config(config_path, on)
    are_files_valid = []
    for entry in config.items:
        are_files_valid.append(entry.is_valid())
    error_count = len(list(filter(lambda e: not e, are_files_valid)))
    click.echo(
        'Verification complete with {} error{} for {} file{}'.format(
            error_count, "" if error_count == 1 else "s", len(config.items), "" if len(config.items) == 1 else "s"
        )
    )
    return error_count


def backup(config_path: str, dir: str, clean: bool, on: str = None) -> None:
    on = on if on else os.getcwd()
    config = _parse_config(config_path, on)
    config.make_dirs()
    backup_dir_name = dir if dir else datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    if clean:
        click.echo(f'Cleaning folder {dir}')
        delete_file(dir)
    for item in config.items:
        for file in item.files:
            copy_file(item.frm + file, '{}/{}'.format(backup_dir_name, item.to))
    click.echo('Backup complete')


def restore(config_path: str, backup_dir_name: str, on: str = None) -> None:
    on = on if on else os.getcwd()
    config = _parse_config(config_path, on, keep_globs=True)
    for item in config.items:
        for file in item.files:
            copy_file('{}/{}{}'.format(backup_dir_name, item.to, file), item.frm)
    click.echo('Restore complete')

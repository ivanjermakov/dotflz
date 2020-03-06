from datetime import datetime

from dotflz.parser import *


def _parse_config(config_path, on):
    click.echo(f'Config file: {config_path} on {on}')
    config = parse_config(config_path, on)
    return config


def copy(config_path, clean=False, on=None):
    on = on if on else os.getcwd()
    config = _parse_config(config_path, on)
    config.make_dirs()
    if clean:
        click.echo(f'Cleaning folder {config.name}')
        delete_file(config.name)
    for item in config.items:
        item.copy()


def paste(config_path, on=None):
    on = on if on else os.getcwd()
    config = _parse_config(config_path, on)
    for item in config.items:
        item.paste()


def verify(config_path, on=None):
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


def backup(config_path, dir, clean, on=None):
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


def restore(config_path, backup_dir_name, on=None):
    on = on if on else os.getcwd()
    config = _parse_config(config_path, on)
    for item in config.items:
        for file in item.files:
            copy_file('{}/{}{}'.format(backup_dir_name, item.to, file), item.frm)

#!/usr/bin/env python3
import click

from parser import *


@click.command()
@click.argument('config_path')
def dotflz(config_path):
    click.echo(f'config file: {config_path}')
    entries = parse_config(config_path)
    click.echo('[\n' + '\n'.join('\t{}'.format(e) for _, e in enumerate(entries)) + '\n]')
    for entry in entries:
        entry.copy()


dotflz()

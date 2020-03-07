from typing import List

import yaml

from dotflz.config_item import ConfigItem
from dotflz.filesystem import *


class Config:
    """
    Describe parsed config passed to utility.
    """

    def __init__(self, name: str, items: List[ConfigItem]) -> None:
        """
        Constructor.

        :param name: config name
        :param items: config items
        """
        self.name = name
        self.items = items

    def make_dirs(self) -> None:
        """
        Make directory for config files.
        Directory name is config name itself.
        """
        os.makedirs(self.name, exist_ok=True)

    @staticmethod
    def parse(path: str, on: str, keep_globs: bool = False) -> 'Config':
        with open(path, 'r') as stream:
            items = []
            config_file = yaml.safe_load(stream)
            config_name = list(config_file.keys())[0]
            config_items = list(config_file.values())[0].items() if list(config_file.values())[0] else []
            for name, item_config in config_items:
                frm = os.path.expanduser(item_config['from']) if 'from' in item_config else ''
                to = os.path.expanduser(item_config['to']) if item_config.get('to') else name + '/'
                files_ = item_config['files']
                files = files_ if isinstance(files_, list) else [files_]
                items.append(ConfigItem(name, on, frm, to, files, config_name, keep_globs))
            config = Config(config_name, items)
            click.echo(f'Parsed config {path} with no errors')
            return config

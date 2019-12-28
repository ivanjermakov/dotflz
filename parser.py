import yaml

from config import *


def parse_config(path):
    with open(path, 'r') as stream:
        items = []
        config = yaml.safe_load(stream)
        config_name = list(config.keys())[0]
        config_items = list(config.values())[0].items()
        for name, item_config in config_items:
            items.append(ConfigItem(name, item_config, config_name))
        return Config(config_name, items)

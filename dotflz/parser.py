import yaml

from dotflz.config import *


def parse_config(path):
    with open(path, 'r') as stream:
        items = []
        config = yaml.safe_load(stream)
        config_name = list(config.keys())[0]
        config_items = list(config.values())[0].items()
        for name, item_config in config_items:
            frm = os.path.expanduser(item_config['from'])
            to = os.path.expanduser(item_config['to']) if item_config.get('to') else name + '/'
            files_ = item_config['files']
            files = files_ if isinstance(files_, list) else [files_]
            items.append(ConfigItem(name, frm, to, files, config_name))
        return Config(config_name, items)

import yaml

from dotflz.config import *


def parse_config(path, on):
    with open(path, 'r') as stream:
        items = []
        config_file = yaml.safe_load(stream)
        config_name = list(config_file.keys())[0]
        config_items = list(config_file.values())[0].items() if list(config_file.values())[0] else []
        for name, item_config in config_items:
            frm = os.path.expanduser(item_config['from'])
            to = os.path.expanduser(item_config['to']) if item_config.get('to') else name + '/'
            files_ = item_config['files']
            files = files_ if isinstance(files_, list) else [files_]
            items.append(ConfigItem(name, on, frm, to, files, config_name))
        config = Config(config_name, items)
        click.echo(f'Parsed config {path} with no errors')
        return config

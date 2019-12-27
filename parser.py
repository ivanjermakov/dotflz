import yaml

from copy_config import CopyConfig


def parse_config(path):
    with open(path, 'r') as stream:
        entries = []
        for name, entry_dict in yaml.safe_load(stream).items():
            entries.append(CopyConfig(name, entry_dict))
        return entries

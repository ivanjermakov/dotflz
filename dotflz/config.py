import glob
import itertools

from dotflz.filesystem import *


class Config:
    def __init__(self, name, items):
        self.name = name
        self.items = items
        os.makedirs(self.name, exist_ok=True)


class ConfigItem:
    def __init__(self, name, frm, to, files, config_name):
        """
        Constructor
        :param name: configuration item name
        :param frm: source directory
        :param to: destination directory
        :param files: list of source files within source directory
        :param config_name: name of config
        """
        self.name = name
        self.frm = frm
        self.to = to
        self.files = self._check_mask(files)
        self.config_name = config_name

    def __repr__(self):
        return f'{self.name}: {self.frm} -> {self.to} | {self.files}'

    def copy(self):
        mkdir(self.config_name + self.to)
        for f in self.files:
            copy_file(self.frm + f, self.config_name + self.to)

    def paste(self):
        for f in self.files:
            copy_file(self.config_name + self.to + f, self.frm)

    def is_valid(self):
        are_files_exist = []
        for f in self.files:
            full_f_path = self.frm + f
            is_f_exists = os.path.exists(full_f_path)
            if not is_f_exists:
                click.echo(f'File {full_f_path} does not exist')
            are_files_exist.append(is_f_exists)
        return all(are_files_exist)

    def _check_mask(self, files):
        result = []
        for f in files:
            if '*' in f:
                result = list(itertools.chain(
                    result,
                    self._find_by_mask(f)
                ))
            else:
                result.append(f)
        # remove duplicates
        result = list(set(result))
        return result

    def _find_by_mask(self, file):
        result = []
        masked_files = glob.glob(self.frm + file)
        masked_files = list(filter(lambda f: os.path.isfile(f), masked_files))
        click.echo('mask: {} -> {}{}'.format(file, masked_files, '' if len(masked_files) != 0 else ' | no matches'))
        for f in masked_files:
            result.append(f.replace(self.frm, ''))
        return result

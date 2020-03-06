import glob
import itertools

from dotflz.filesystem import *


class Config:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def make_dirs(self):
        os.makedirs(self.name, exist_ok=True)


class ConfigItem:
    def __init__(self, name, on, frm, to, files, config_name):
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
        if frm[0] == '/':
            click.echo('Absolute path detected, omitting "on" parameter')
            self.on = ''
        else:
            self.on = os.path.join(on, '')
        self.to = to
        self.files = self._check_pattern(files)
        self.config_name = config_name

    def __repr__(self):
        return f'{self.name}: {self.on}>{self.frm} -> {self.to} | {self.files}'

    def copy(self):
        create_directory(self.config_name + self.to)
        for f in self.files:
            copy_file(self.on + self.frm + f, self.config_name + self.to)

    def paste(self):
        for f in self.files:
            copy_file(self.config_name + self.to + f, self.on + self.frm)

    def is_valid(self):
        are_files_exist = []
        for f in self.files:
            full_f_path = self.on + self.frm + f
            is_f_exists = os.path.exists(full_f_path)
            if not is_f_exists:
                click.echo(f'File {full_f_path} does not exist')
            are_files_exist.append(is_f_exists)
        return all(are_files_exist)

    def _check_pattern(self, files):
        result = []
        for f in files:
            result = list(itertools.chain(
                result,
                self._find_by_pattern(f)
            ))
        # remove duplicates
        result = list(sorted(set(result), key=result.index))
        return result

    def _find_by_pattern(self, file):
        result = []
        masked_files = glob.glob(self.on + self.frm + file, recursive=True)
        masked_files = list(filter(lambda f: os.path.isfile(f), masked_files))
        click.echo('Pattern: {} -> {}{}'.format(self.frm + file, masked_files,
                                                '' if len(masked_files) != 0 else ' | no matches'))
        for f in masked_files:
            result.append(f.replace(self.on + self.frm, ''))
        return result

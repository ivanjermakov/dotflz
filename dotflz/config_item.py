import glob
import itertools
from typing import List

from dotflz.filesystem import *


class ConfigItem:
    """
    Describe single `Config` instance.
    """

    def __init__(self, name: str, on: str, frm: str, to: str, files: List[str], config_name: str,
                 keep_globs: bool = False) -> None:
        """
        Constructor.

        :param name: configuration item name
        :param frm: source directory
        :param to: destination directory
        :param files: list of source files within source directory
        :param config_name: name of config
        :param keep_globs: if true, globs wont be compiled to real files
        """
        self.name = name
        self.frm = frm
        if frm and frm[0] == '/':
            click.echo('Absolute path detected, omitting "on" parameter')
            self.on = ''
        else:
            self.on = os.path.join(on, '')
        self.to = to
        self.files = files if keep_globs else self._compile_patterns(files)
        self.config_name = config_name

    def __repr__(self) -> str:
        """
        Object description

        :return: object description
        """
        return f'{self.name}: {self.on}>{self.frm} -> {self.to} | {self.files}'

    def copy(self) -> None:
        """
        Copy config item files
        """
        create_directory(self.config_name + self.to)
        for f in self.files:
            copy_file(self.on + self.frm + f, self.config_name + self.to + os.path.dirname(f))

    def paste(self) -> None:
        """
        Paste config item files.
        Same as copy, but in reverse
        """
        for f in self.files:
            copy_file(self.config_name + self.to + f, self.on + self.frm)

    def is_valid(self) -> bool:
        """
        Check whether config valid or not.
        Config is valid if all source files are exist.
        :return: is valid or not
        """
        are_files_exist = []
        for f in self.files:
            full_f_path = self.on + self.frm + f
            is_f_exists = os.path.exists(full_f_path)
            if not is_f_exists:
                click.echo(f'File {full_f_path} does not exist')
            are_files_exist.append(is_f_exists)
        return all(are_files_exist)

    def _compile_patterns(self, files: List[str]) -> List[str]:
        """
        Compile glob patterns to real files.
        :param files: list of glob patterns
        :return: list of compilation result files
        """
        result = []
        for f in files:
            result = list(itertools.chain(
                result,
                self._compile_pattern(f)
            ))
        # remove duplicates
        result = list(sorted(set(result), key=result.index))
        return result

    def _compile_pattern(self, file: str) -> List[str]:
        """
        Compile glob pattern to real files.
        :param file: glob pattern
        :return: list of compilation result files
        """
        result = []
        masked_files = glob.glob(self.on + self.frm + file, recursive=True)
        masked_files = list(filter(lambda f: os.path.isfile(f), masked_files))
        click.echo('Pattern: {} -> {}{}'.format(self.frm + file, masked_files,
                                                '' if len(masked_files) != 0 else ' | no matches'))
        for f in masked_files:
            result.append(f.replace(self.on + self.frm, ''))
        return result

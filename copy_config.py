import os
import subprocess

import click


class CopyConfig:
    def __init__(self, name, entry_dict):
        self.name = name
        self.frm = os.path.expanduser(entry_dict['from'])
        self.to = os.path.expanduser(entry_dict['to']) if entry_dict.get('to') else name + '/'
        files_ = entry_dict['files']
        self.files = files_ if isinstance(files_, list) else [files_]

    def __repr__(self):
        return f'{self.name}: {self.frm} -> {self.to} | {self.files}'

    def copy(self):
        self.mkdir()
        for f in self.files:
            click.echo(f'Copying file {f}')
            self.copy_file(f)

    def is_valid(self):
        are_files_exist = []
        for f in self.files:
            full_f_path = self.frm + f
            is_f_exists = os.path.exists(full_f_path)
            if not is_f_exists:
                click.echo(f'File {full_f_path} does not exist')
            are_files_exist.append(is_f_exists)
        return all(are_files_exist)

    def mkdir(self):
        os.makedirs(self.to, exist_ok=True)

    def copy_file(self, file_path):
        subprocess.run(['bash', '-c', " ".join(['cp', self.frm + file_path, self.to])])

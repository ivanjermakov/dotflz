import os
import subprocess

import click


class CopyConfig:
    def __init__(self, name, entry_dict):
        self.name = name
        self.frm = entry_dict['from']
        self.to = entry_dict['to'] if entry_dict.get('to') else name + '/'
        files_ = entry_dict['files']
        self.files = files_ if isinstance(files_, list) else [files_]

    def __repr__(self):
        return f'{self.name}: {self.frm} -> {self.to} | {self.files}'

    def copy(self):
        self.mkdir()
        for f in self.files:
            click.echo(f'copying file {f}')
            self.copy_file(f)

    def mkdir(self):
        os.makedirs(self.to, exist_ok=True)

    def copy_file(self, file_path):
        subprocess.run(['bash', '-c', " ".join(['cp', self.frm + file_path, self.to])])

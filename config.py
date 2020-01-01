import os
import subprocess

import click


def delete_file(name):
    subprocess.run(['bash', '-c', " ".join(['rm', '-r', name])], check=True)


def copy_file(from_path, to_path):
    click.echo('Copying file: {} -> {}'.format(from_path, to_path))
    os.makedirs(to_path, exist_ok=True)
    subprocess.run(['bash', '-c', " ".join(['cp', from_path, to_path])])


class Config:
    def __init__(self, name, items):
        self.name = name
        self.items = items
        os.makedirs(self.name, exist_ok=True)


class ConfigItem:
    def __init__(self, name, entry_dict, config_name):
        self.name = name
        self.frm = os.path.expanduser(entry_dict['from'])
        self.to = os.path.expanduser(entry_dict['to']) if entry_dict.get('to') else name + '/'
        files_ = entry_dict['files']
        self.files = files_ if isinstance(files_, list) else [files_]
        self.config_name = config_name

    def __repr__(self):
        return f'{self.name}: {self.frm} -> {self.to} | {self.files}'

    def copy(self):
        self.mkdir()
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

    def mkdir(self):
        os.makedirs(self.config_name + self.to, exist_ok=True)
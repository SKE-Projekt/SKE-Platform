import uuid
import os
import subprocess

from ske_platform.conf.base_config import BaseConfig


class SandboxExecutor:
    def __init__(self, code, input_data):
        self.id = str(uuid.uuid4())
        self.code = code
        self.input_data = input_data

        self.source_file = '/tmp/' + self.id + '.ed'
        self.input_file  = '/tmp/' + self.id + '.in'
        self.output_file = '/tmp/' + self.id + '.out'

    def run(self):
        self.prepare()
        self.execute()
        self.read_output()
        self.clean()

    def prepare(self):
        with open(self.source_file, 'w+') as f:
            f.write(self.code + '\n')
        with open(self.input_file, 'w+') as f:
            f.write(self.input_data + '\n')

    def execute(self):
        command = f'{BaseConfig.ED_BINARY} {self.source_file} < {self.input_file} > {self.output_file}'
        self.return_code = os.system(command)

    def read_output(self):
        with open(self.output_file, 'r+') as f:
            self.output_data = f.readlines()
        self.output_data = ''.join(self.output_data)

    def clean(self):
        os.remove(self.source_file)
        os.remove(self.input_file)
        os.remove(self.output_file)

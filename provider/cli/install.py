from provider.colors import *
import shutil

from datetime import datetime

import os

class Install:
    def __init__(self, command, area, name):
        self.command = command
        self.area = area
        self.name = name
        
    def run(self):
        timestamp = int(datetime.now().timestamp())
        historic = "provider/cli/installs"
        installFile = f"{timestamp}_{self.name}"

        kit = self._valid_kits()[self.name] if self.name in self._valid_kits() else None

        if not kit:
            print('Invalid kit')
            return

        os.system(f'cd {historic} && git clone {kit['repository_url']} {installFile}')
        self._transfer_file(f'{historic+"/"+installFile}')
        # self._transfer_file(f'{historic+"/1768975778_ticket"}')

        print(f'\n {GREEN}[OCTAPUS] Kit installed: {kit['repository_url']} {RESET}\n')

    def _valid_kits(self):
        # Todo: transferir para uma API
        return {
            'ticket': {
                'repository_url': 'https://github.com/xama11/kit-ticket',
                'author': 'silvaleal',
                'sum-files': ['env'],
                'ignore-files': ['readme.md', '.git'],
            },
        }

    def _transfer_file(self, installPath):
        for file in os.listdir(installPath):
            if file in self._valid_kits()[self.name]['ignore-files']: continue
            
            fullPath = os.path.join(installPath, file).replace('\\', '/')

            if os.path.isdir(fullPath):
                self._transfer_file(fullPath)

            if not os.path.isdir(fullPath) and not "pycache" in fullPath:
                originalPath = "/".join(fullPath.split('/')[4:])
                projectPath = "/".join(os.path.dirname(os.path.abspath(__file__)).split('\\')[:-2])

                # print()
                # print(f"File: {fullPath}")
                # print(f'Moved to: {originalPath}')
                # print(projectPath+"/"+originalPath)
                # print()

                shutil.move(fullPath, projectPath+"/"+originalPath)
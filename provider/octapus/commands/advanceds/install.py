from provider.colors import *
from datetime import datetime
import shutil
import os

class Install:
    def __init__(self, command, area, name):
        self.command = command
        self.area = area
        self.name = name
        
    def run(self):
        timestamp = int(datetime.now().timestamp())
        historic = "provider/octapus/installs"
        installFile = f"{timestamp}_{self.name}"

        kit = self._valid_kits()[self.name] if self.name in self._valid_kits() else None

        if not kit:
            return print('Invalid kit')

        os.makedirs(historic, exist_ok=True)

        os.system(f'cd {historic} && git clone {kit["repository_url"]} {installFile}')
        self._transfer_file(f'{historic}/{installFile}')

        print(f'\n {GREEN}[OCTAPUS] Kit installed: {kit["repository_url"]} {RESET}\n')

    def _valid_kits(self):
        # Todo: transferir para uma API
        return {
            'ticket': {
                'repository_url': 'https://github.com/xama11/kit-ticket',
                'author': 'silvaleal',
                'sum-files': ['env'],
                'ignore-files': ['readme.md', '.git'],
            },
            'economy': {
                'repository_url': 'https://github.com/xama11/kit-economy',
                'author': 'silvaleal',
                'sum-files': ['env'],
                'ignore-files': ['readme.md', '.git'],
            },
        }

    def _transfer_file(self, path):
        for file in os.listdir(path):
            if file in self._valid_kits()[self.name]['ignore-files']: continue
            
            self._create_file(path, file) if not file in self._valid_kits()[self.name]['sum-files'] else self._sum_file(path, file)

    def _sum_file(self, path, file):
        fullPath = os.path.join(path, file).replace('\\', '/')

        originalPath = "/".join(fullPath.split('/')[4:])
        projectPath = "/".join(os.path.dirname(os.path.abspath(__file__)).split('\\')[:-4])
        newPosition = projectPath+"/"+originalPath
        
        # O arquivo env do kit deve ser somado no .env do projeto
        if originalPath == "env":
            newPosition = projectPath+"/.env"
    
        with open(fullPath, encoding='utf-8') as file_obj:
            kitFile = file_obj.read()

        # Certificar-se de que o diretório de destino existe
        os.makedirs(os.path.dirname(newPosition), exist_ok=True)

        with open(newPosition, 'a', encoding='utf-8') as oficialFile:
            oficialFile.write(f"\n{kitFile}")

    def _create_file(self, path, file):
        fullPath = os.path.join(path, file).replace('\\', '/')

        if os.path.isdir(fullPath):
            self._transfer_file(fullPath)

        if not os.path.isdir(fullPath) and not "pycache" in fullPath:
            originalPath = "/".join(fullPath.split('/')[4:])
            projectPath = "/".join(os.path.dirname(os.path.abspath(__file__)).split('\\')[:-4])
            newPosition = projectPath+"/"+originalPath

            # Certificar-se de que o diretório de destino existe
            os.makedirs(os.path.dirname(newPosition), exist_ok=True)

            shutil.move(fullPath, newPosition)

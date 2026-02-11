from datetime import datetime
from provider.colors import *
import os

class Make:
    def __init__(self, command, area, name):
        self.command = command
        self.area = area
        self.name = name
        
    def _paths(self):
        return {
            "command": 'application/cogs',
            "container": 'application/containers',
            "components": "application/containers/components",
            "scheduler": "application/schedulers",
            "decorator": "application/decorators",
            "migration": "database/migrations",
            "model": "database/models",
        }
    
    def run(self):

        if (os.path.exists(f'{self._paths()[self.area]}/{self.name.lower()}.py')):
            return f"\n{RED}[OCTAPUS] File '{self.name.lower()}.py' already exists\n{RESET}"

        isMigration = self.area == 'migration'

        filename = (
            f"{int(datetime.now().timestamp())}_{self.name}".lower()
            if isMigration
            else self.name.lower()
        )

        templatePath = f'provider/templates/{self.area}.py'
        outputPath = f'{self._paths()[self.area]}/{filename}.py'

        with open(templatePath, 'r') as original:
            content = (
                original.read()
                .replace('Example', self.name)
                .replace('example', self.name.lower())
            )

        with open(outputPath, 'w') as file:
            file.write(content)

        return f'\n{GREEN} [OCTAPUS] New {self.area}: ./{outputPath} (CTRL+Left Click)\n{RESET}'
from datetime import datetime

class Make:
    def __init__(self, command, area, name):
        self.command = command
        self.area = area
        self.name = name
        
    def paths(self):
        return {
            "command": 'application/cogs',
            "container": 'application/containers',
            "components": "application/containers/components",
            "decorator": "application/decorators",
            "migration": "database/migrations",
            "model": "database/models",
            "scheduler": "application/schedulers",
        }
    
    def run(self):
        isMigration = self.area == 'migration'

        filename = (
            f"{int(datetime.now().timestamp())}_{self.name}".lower()
            if isMigration
            else self.name.lower()
        )

        templatePath = f'provider/templates/{self.area}.py'
        outputPath = f'{self.paths()[self.area]}/{filename}.py'

        with open(templatePath, 'r') as original:
            content = (
                original.read()
                .replace('Example', self.name.capitalize())
                .replace('example', self.name.lower())
            )

        with open(outputPath, 'w') as file:
            file.write(content)

        return f'\n [OCTAPUS] New {self.area}: ./{outputPath} (CTRL+Left Click)\n'
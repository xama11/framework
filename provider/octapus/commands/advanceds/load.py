from provider.migrations.LoadMigrations import LoadMigrations
from provider.colors import *

class Load:
    def __init__(self, command, area, name):
        self.command = command
        self.area = area
        self.name = name
        
    def run(self):
        
        if self.name =='fresh' or self.name == 'refresh':
            loader = LoadMigrations(rebuild=(self.name == 'refresh'))
            loader.loader()
            
            print(
                f'\n {RED}ALERT:{RESET}'
                f' If you want to update an already loaded migration, use: '
                f'{BLUE}python3 octapus.py load:migrate --refresh{RESET}'
            )
            return f'\n{GREEN} [OCTAPUS] Migrations loaded{RESET}\n'
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
                f'\n {RED}ALERT{RESET}\n'
                f' [PT-BR] Se você quer atualizar uma migration já carregada, use: '
                f'{GREEN}python3 octapus.py load:migrate --refresh{RESET}\n'
                f' [EN] If you want to update an already loaded migration, use: '
                f'{GREEN}python3 octapus.py load:migrate --refresh{RESET}'
            )
            return f'\n{GREEN} [OCTAPUS] Migrations loaded{RESET}\n'
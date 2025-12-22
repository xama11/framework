from provider.bases.BaseLoader import BaseLoader
from provider.colors import *


class Load:
    def __init__(self, command, area, name):
        self.command = command
        self.area = area
        self.name = name
        
    def run(self):
        
        if self.name =='fresh':
            loader = BaseLoader()
            loader.run()
            
            print(
                f'\n {RED}ALERT{RESET}\n'
                f' [PT-BR] Se você quer atualizar uma migration já carregada, use: '
                f'{GREEN}python3 octapus.py load:migrate --refresh{RESET}\n'
                f' [EN] If you want to update an already loaded migration, use: '
                f'{GREEN}python3 octapus.py load:migrate --refresh{RESET}'
            )
            return f'\n [OCTAPUS] Migrations loaded\n'
        
        elif self.name =='refresh':
            loader = BaseLoader()
            loader.run(force=True)
            
            print(
                f'\n {RED}ALERT{RESET}\n'
                f' [PT-BR] Se você quer atualizar uma migration já carregada, use: '
                f'{GREEN}python3 octapus.py load:migrate --refresh{RESET}\n'
                f' [EN] If you want to update an already loaded migration, use: '
                f'{GREEN}python3 octapus.py load:migrate --refresh{RESET}'
            )
            return f'\n [OCTAPUS] Migrations loaded\n'
        
        elif self.name == '--check':
            return "checked"
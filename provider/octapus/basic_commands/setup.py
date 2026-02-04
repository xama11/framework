from provider.migrations.LoadMigrations import LoadMigrations
from provider.colors import *

import os

from octapus import OctapusCLI

class Setup:
    def __init__(self, command):
        self.command = command
        
    def run(self):

        if not os.path.exists('database/database.db'):
            print(f'{GREEN} [SETUP] Creating your database {RESET}')
            OctapusCLI(args=['load:migrations fresh']).manager()
        else:
            print(f'{RED} [SETUP] Database already exists {RESET}')

        useKits = input('\n* Do you want to install any kit? (y/n) ')

        if useKits == 'y':
            kitName = input('* Kit name: ')
            OctapusCLI(args=[f'install:kit', kitName]).manager()
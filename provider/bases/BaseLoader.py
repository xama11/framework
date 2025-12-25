from provider.database import Database
from provider.colors import *
import os
import sys
import importlib

from database.models.migrations import MigrationsModel
from database.models.seeds import SeedsModel


class BaseLoader:
    def __init__(self):
        self.connection = Database().connect()
        self.cursor = self.connection.cursor()
        
    def tables(self):
        allTables = {}
        
        for file in sorted(os.listdir('database/migrations')):
            if file.endswith('.py'):
                fileName = file.replace('.py', '')
                className = fileName.split('_')[1]
                
                migration = importlib.import_module(f'database.migrations.{fileName}')
                migrationClass = getattr(migration, className.capitalize())

                instance = migrationClass()
                
                allTables[fileName] = (instance.table())
        return allTables
    
    def seeders(self):
        allSeeders = {}
        for file in sorted(os.listdir('database/migrations')):
            if file.endswith('.py'):
                fileName = file.replace('.py', '')
                className = fileName.split('_')[1]
                
                migration = importlib.import_module(f'database.migrations.{fileName}')
                migrationClass = getattr(migration, className.capitalize())

                instance = migrationClass()
                allSeeders[fileName] = instance.seeders()
        return allSeeders

    def run(self, force:bool=False):
        self.loadMigrations(force)
        self.loadSeeders()
        self.connection.close()
        
    def loadMigrations(self, force: bool = False):
        tables = self.tables()

        if not force:
            for table in tables:
                tableName = table.split('_')[1]

                if tableName == 'migrations':
                    self.cursor.execute(tables[table])
                    self.connection.commit()
                    continue

                if not MigrationsModel().filter(migration=table).first():
                    self.cursor.execute(tables[table])
                    self.connection.commit()

                    MigrationsModel().add(migration=table)

                    print(
                        f"{GREEN} [OCTAPUS] Migration {table} loaded successfully "
                        f"(./database/migrations/{table}.py){RESET}"
                    )
                else:
                    print(
                        f"{RED} [OCTAPUS] Migration {table} is already loaded "
                        f"(./database/migrations/{table}.py){RESET}"
                    )

        else:
            if os.path.exists('database/database.db'):
                self.connection.close()
                os.remove('database/database.db')

                self.connection = Database().connect()
                self.cursor = self.connection.cursor()

            for table in tables:
                self.cursor.execute(tables[table])
                self.connection.commit()

                if 'migrations' not in table:
                    MigrationsModel().add(migration=table)

                    print(
                        f"{GREEN} [OCTAPUS] Migration {table} loaded successfully "
                        f"(./database/migrations/{table}.py){RESET}"
                    )
                    
    def loadSeeders(self):
        seeders = self.seeders()

        if not seeders:
            return

        for table in seeders:
            if not SeedsModel().filter(migration=table).first() and not 'migration' in table:
                for seed in seeders[table]:
                    print(f"{GREEN} [OCTAPUS] Seeders {table} loaded successfully{RESET}")
                    
                    self.cursor.execute(seed)
                    self.connection.commit()

                SeedsModel().add(migration=table)

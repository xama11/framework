from provider.database import Database
import os
import importlib

class BaseLoader:
    def __init__(self):
        self.connection = Database().connect()
        self.cursor = self.connection.cursor()
        
    def tables(self):
        allTables = {}
        for file in os.listdir('database/migrations'):
            if file.endswith('.py'):
                fileName = file.replace('.py', '')
                migration = importlib.import_module(f'database.migrations.{fileName}')
                migrationClass = getattr(migration, fileName.capitalize())

                instance = migrationClass()
                allTables[fileName] = (instance.table())
        return allTables
    
    def seeders(self):
        allSeeders = {}
        for file in os.listdir('database/migrations'):
            if file.endswith('.py'):
                fileName = file.replace('.py', '')
                migration = importlib.import_module(f'database.migrations.{fileName}')
                migrationClass = getattr(migration, fileName.capitalize())

                instance = migrationClass()
                allSeeders[fileName] = instance.seeders()
        return allSeeders

    def run(self):
        tables = self.tables()
        for table in tables:
            self.cursor.execute(tables[table])
            self.connection.commit()
            
        seeders = self.seeders()
        for table in seeders:
                
            for seed in seeders[table]:
                self.cursor.execute(seed)
                self.connection.commit()
        self.connection.close()
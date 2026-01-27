import os
import importlib
import sqlite3
from database.models.migrations import MigrationsModel
from provider.colors import *
from provider.database import Database

class LoadMigrations():
    def __init__(self, rebuild):
        self.rebuild = rebuild
        
        if self.rebuild and os.path.exists('database/database.db'):
            try:
                os.remove('database/database.db')
            except Exception as e:
                print(f"{RED} [ERROR] Failed to delete database: {e}{RESET}")

        self.conn = Database().connect()
        self.cursor = self.conn.cursor()
    
    def loader(self):
        for file in sorted(os.listdir('database/migrations')):
            if not file.endswith('.py'): continue
            
            fileName = file.split('_')[1][:-3]
            
            fileModule = importlib.import_module(f'database.migrations.{file[:-3]}', )
            fileClass = getattr(fileModule, str(fileName).capitalize())
            
            fileQuery = fileClass().query.get_sql()
            
            self._create(file, fileQuery)
        self.conn.close()
            
    def _create(self, file, query):
        name = file.split('_')[1][:-3]
        
        if file == '000000_migrations.py':
            self.cursor.execute(query)
            self.conn.commit()
            return

        if not MigrationsModel().filter(migration=file).first():
            self.cursor.execute(query)
            self.conn.commit()
            
            MigrationsModel().add(migration=file)
            
            return print(
                f"{GREEN} [OCTAPUS] Migration {file} loaded successfully "
                f"(./database/migrations/{file}){RESET}"
            )
        return print(
            f"{RED} [OCTAPUS] Migration {file} is already loaded "
            f"(./database/migrations/{file}){RESET}"
        )
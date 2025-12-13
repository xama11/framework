import sqlite3
import os

class Database:
    def __init__(self):
        self.driver = os.getenv('DB_DRIVE')
    
    def connect(self):
        if (self.driver.lower() == 'sqlite3'):
            import sqlite3
            return sqlite3.connect('database/database.db')
        elif (self.driver.lower() == 'mysql'):
            import pymysql
            return pymysql.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_DATABASE')
            )
        else:
            print(' [ERROR] Invalid database, please correct to a valid database.')
            print(' [ERROR] Wiki: https://github.com/silvaleal/dpy2-framework/wiki/1.-Database-Config')
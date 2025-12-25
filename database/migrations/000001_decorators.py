class Decorators:
    def table(self):
        return '''
            CREATE TABLE IF NOT EXISTS decorators (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                decoratorFile VARCHAR(150) NOT NULL,
                commandFile VARCHAR(150) NOT NULL
            );
            '''
    
    def seeders(self):
        return [] # INSERT INTO decorators () VALUES ()
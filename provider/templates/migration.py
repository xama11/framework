class Example:
    def table(self):
        return '''
            CREATE TABLE IF NOT EXISTS example (
                id INTEGER PRIMARY KEY AUTOINCREMENT
            );
            '''
    
    def seeders(self):
        return [] # INSERT INTO example () VALUES ()
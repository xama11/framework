class Test:
    def table(self):
        return '''
            CREATE TABLE IF NOT EXISTS test (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(45) DEFAULT "100"
            );
            '''
    
    def seeders(self):
        return [] # INSERT INTO test () VALUES ()
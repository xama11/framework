class Terminals:
    def table(self):
        return '''
            CREATE TABLE IF NOT EXISTS terminals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                command VARCHAR(45) NOT NULL,
                activated DATE DEFAULT CURRENT_TIMESTAMP
            );
            '''
    
    def seeders(self):
        return [] # INSERT INTO terminals () VALUES ()
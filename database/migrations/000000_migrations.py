class Migrations:
    def table(self):
        return '''
            CREATE TABLE IF NOT EXISTS migrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                migration VARCHAR(45) NOT NULL,
                activated DATE DEFAULT CURRENT_TIMESTAMP
            );
            '''
    
    def seeders(self):
        return [] # INSERT INTO migrations () VALUES ()
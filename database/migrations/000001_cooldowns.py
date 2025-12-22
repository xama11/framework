class Cooldowns:
    def table(self):
        return '''
             CREATE TABLE IF NOT EXISTS cooldowns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    userId BIGINT NOT NULL,
                    command VARCHAR(100) NOT NULL,
                    lastUsed DATETIME DEFAULT CURRENT_TIMESTAMP
                );
            '''
    
    def seeders(self):
        return [] # INSERT INTO cooldowns () VALUES ()
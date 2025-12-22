from datetime import datetime

class Schedulers:
    def table(self):
        return '''
            CREATE TABLE IF NOT EXISTS schedulers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date DATETIME DEFAULT CURRENT_TIMESTAMP,
                schedule VARCHAR(255) NOT NULL,
                scheduleId INTEGER NOT NULL,
                activated BOOLEAN DEFAULT 0
            );
            '''
    
    def seeders(self):
        return []
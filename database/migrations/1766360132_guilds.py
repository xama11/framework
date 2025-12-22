class Guilds:
    def table(self):
        return '''
            CREATE TABLE IF NOT EXISTS guilds (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                authorId BIGINT NOT NULL
            );
            '''
    
    def seeders(self):
        return [
            'INSERT INTO guilds (authorId) VALUES (1234)'
            ] # INSERT INTO guilds () VALUES ()
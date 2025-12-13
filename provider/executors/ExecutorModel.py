from pypika import Query

class ExecutorsModel:
    def __init__(self, conn, cursor, command, table : Query):
        self.conn = conn
        self.cursor = cursor
        self.command = command
        self.table = table

    def _commit_(self):
        self.cursor.execute(self.command.get_sql())
        lastByid = self.cursor.lastrowid
        self.conn.commit()
        self.conn.close()
        return lastByid
    
    def first(self):
        self.cursor.execute(self.command.get_sql())
        result = self.cursor.fetchone()
        self.conn.close()
        return result

    def all(self):
        self.cursor.execute(self.command.get_sql())
        result = self.cursor.fetchall()
        self.conn.close()
        return result
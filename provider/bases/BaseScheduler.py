from provider.database import Database
from datetime import datetime

class BaseScheduler:
    def __init__(self, scheduler, table, name):
        self.scheduler = scheduler
        self.table = table
        self.name = name

    def saveSchedule(self, methodRun, date):
        dateEvent = datetime.strptime(date[1], "%Y-%m-%d %H:%M:%S.%f")
        self.scheduler.add_job(methodRun, 'date', run_date=dateEvent, args=[date[3]])

    def getAction(self, id):
        conn = Database().connect()
        cursor = conn.cursor()

        query = f"SELECT * FROM {self.table} WHERE id = ?"

        cursor.execute(query, (id, ))
        result = cursor.fetchone()
        conn.close()
        return result

    def disable(self, id):
        conn = Database().connect()
        cursor = conn.cursor()

        query = f"UPDATE schedulers SET activated = 1 WHERE id = ?"

        cursor.execute(query, (id, ))
        result = conn.commit()
        conn.close()
        return result
    
    def getSchedulers(self):
        conn = Database().connect()
        cursor = conn.cursor()

        query = f"SELECT * FROM schedulers WHERE activated = 0"

        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result
    
    def getScheduleById(self, id):
        conn = Database().connect()
        cursor = conn.cursor()

        query = f"SELECT * FROM schedulers WHERE scheduleId = ?"

        cursor.execute(query, (id,))
        result = cursor.fetchone()
        conn.close()
        return result
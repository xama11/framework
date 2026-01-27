from provider.migrations.BaseMigration import BaseMigration
from pypika.functions import CurTimestamp

class Schedulers(BaseMigration):
    def __init__(self, table="schedulers"):
        super().__init__(table=table)
        self.creator()
    
    def creator(self):
        self.id()
        self.timestamp('date', default=CurTimestamp())
        self.string('schedule', size=255)
        self.integer('scheduleId')
        self.boolean('activated', default=False)

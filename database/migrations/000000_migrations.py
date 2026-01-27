from provider.migrations.BaseMigration import BaseMigration
from pypika.functions import CurTimestamp

class Migrations(BaseMigration):
    def __init__(self, table="migrations"):
        super().__init__(table=table)
        self.creator()
    
    def creator(self):
        self.id()
        self.string('migration', size=45)
        self.date('activated', default=CurTimestamp())

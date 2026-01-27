from provider.migrations.BaseMigration import BaseMigration
from pypika.functions import CurTimestamp

class Seeds(BaseMigration):
    def __init__(self, table="seeds"):
        super().__init__(table=table)
        self.creator()
    
    def creator(self):
        self.id()
        self.string('migration', size=45)
        self.date('activated', default=CurTimestamp())

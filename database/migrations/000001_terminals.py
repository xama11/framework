from provider.migrations.BaseMigration import BaseMigration
from pypika.functions import CurTimestamp

class Terminals(BaseMigration):
    def __init__(self, table="terminals"):
        super().__init__(table=table)
        self.creator()
    
    def creator(self):
        self.id()
        self.string('command', size=45)
        self.date('activated', default=CurTimestamp())

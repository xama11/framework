from provider.migrations.BaseMigration import BaseMigration
from pypika.functions import CurTimestamp

class Example(BaseMigration):
    def __init__(self, table="example"):
        super().__init__(table=table)
        self.creator()
    
    def creator(self):
        self.id()
        # self.string('name', size=45)
        # self.date('createdAt', default=CurTimestamp())

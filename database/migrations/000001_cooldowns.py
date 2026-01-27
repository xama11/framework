from provider.migrations.BaseMigration import BaseMigration
from pypika.functions import CurTimestamp

class Cooldowns(BaseMigration):
    def __init__(self, table="cooldowns"):
        super().__init__(table=table)
        self.creator()
    
    def creator(self):
        self.id()
        self.bigint('userId')
        self.string('command', size=100)
        self.timestamp('lastUsed', default=CurTimestamp())

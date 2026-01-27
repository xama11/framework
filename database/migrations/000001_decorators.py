from provider.migrations.BaseMigration import BaseMigration

class Decorators(BaseMigration):
    def __init__(self, table="decorators"):
        super().__init__(table=table)
        self.creator()
    
    def creator(self):
        self.id()
        self.string('decoratorFile', size=150)
        self.string('commandFile', size=150)

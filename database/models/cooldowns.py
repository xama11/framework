from provider.orm.BaseORM import BaseORM

class Cooldowns(BaseORM):
    def __init__(self, table='cooldowns'):
        super().__init__(table)
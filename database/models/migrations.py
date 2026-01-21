from provider.orm.BaseORM import BaseORM

class MigrationsModel(BaseORM):
    def __init__(self, table='migrations'):
        super().__init__(table)
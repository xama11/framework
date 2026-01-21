from provider.orm.BaseORM import BaseORM

class SeedsModel(BaseORM):
    def __init__(self, table='seeds'):
        super().__init__(table)
from provider.orm.BaseORM import BaseORM

class DecoratorsModel(BaseORM):
    def __init__(self, table='decorators'):
        super().__init__(table)
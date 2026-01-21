from provider.orm.BaseORM import BaseORM

class TerminalsModel(BaseORM):
    def __init__(self, table='terminals'):
        super().__init__(table)
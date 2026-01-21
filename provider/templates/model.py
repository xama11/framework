from provider.orm.BaseORM import BaseORM

class ExampleModel(BaseORM):
    def __init__(self, table='example'):
        super().__init__(table)
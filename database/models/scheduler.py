from provider.orm.BaseORM import BaseORM

class SchedulerModel(BaseORM):
    def __init__(self, table='schedulers'):
        super().__init__(table)
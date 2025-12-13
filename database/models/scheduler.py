from provider.bases.BaseModel import BaseModel

class Scheduler(BaseModel):
    def __init__(self, table='schedulers'):
        super().__init__(table)
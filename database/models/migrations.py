from provider.bases.BaseModel import BaseModel

class MigrationsModel(BaseModel):
    def __init__(self, table='migrations'):
        super().__init__(table)
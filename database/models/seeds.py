from provider.bases.BaseModel import BaseModel

class SeedsModel(BaseModel):
    def __init__(self, table='seeds'):
        super().__init__(table)
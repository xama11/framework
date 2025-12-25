from provider.bases.BaseModel import BaseModel

class DecoratorsModel(BaseModel):
    def __init__(self, table='decorators'):
        super().__init__(table)
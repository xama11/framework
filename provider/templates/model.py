from provider.bases.BaseModel import BaseModel

class ExampleModel(BaseModel):
    def __init__(self, table='example'):
        super().__init__(table)
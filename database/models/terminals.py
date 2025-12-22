from provider.bases.BaseModel import BaseModel

class TerminalsModel(BaseModel):
    def __init__(self, table='terminals'):
        super().__init__(table)
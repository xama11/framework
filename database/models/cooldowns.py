from provider.bases.BaseModel import BaseModel

class Cooldowns(BaseModel):
    def __init__(self, table='cooldowns'):
        super().__init__(table)
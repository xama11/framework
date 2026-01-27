from pypika import Query, Table, Column
from pypika.enums import SqlTypes

class BaseMigration:
    def __init__(self, table):
        self.table = table
        self.query = Query.create_table(self.table).if_not_exists()
    
    def id(self):
        self.query = self._create('id', column_type=SqlTypes.INTEGER, nullable=False).primary_key('id')
        return self.query
    
    def string(self, name, size=45, nullable=False, default=None):
        return self._create(name, column_type=SqlTypes.VARCHAR(size).get_sql(), nullable=nullable, default=default)
        
    def integer(self, name, nullable=False, default=None):
        return self._create(name, column_type=SqlTypes.INTEGER, nullable=nullable, default=default)

    def bigint(self, name, nullable=False, default=None):
        return self._create(name, column_type="BIGINT", nullable=nullable, default=default)

    def boolean(self, name, nullable=False, default=None):
        return self._create(name, column_type=SqlTypes.BOOLEAN, nullable=nullable, default=default)

    def float(self, name, nullable=False, default=None):
        return self._create(name, column_type=SqlTypes.FLOAT, nullable=nullable, default=default)

    def numeric(self, name, nullable=False, default=None):
        return self._create(name, column_type=SqlTypes.NUMERIC, nullable=nullable, default=default)

    def signed(self, name, nullable=False, default=None):
        return self._create(name, column_type=SqlTypes.SIGNED, nullable=nullable, default=default)

    def unsigned(self, name, nullable=False, default=None):
        return self._create(name, column_type=SqlTypes.UNSIGNED, nullable=nullable, default=default)
    
    def date(self, name, nullable=False, default=None):
        return self._create(name, column_type=SqlTypes.DATE, nullable=nullable, default=default)
        
    def time(self, name, nullable=False, default=None):
        return self._create(name, column_type=SqlTypes.TIME, nullable=nullable, default=default)
        
    def timestamp(self, name, nullable=False, default=None):
        return self._create(name, column_type=SqlTypes.TIMESTAMP, nullable=nullable, default=default)
        
    def _create(self, name, column_type, nullable, default=None,  size=None):
        
        if not size and default is not None:
            return self.query.columns(
                Column(name, column_type=column_type, nullable=nullable, default=default)
            )
            
        elif not size and default is None:
            return self.query.columns(
                    Column(name, column_type=column_type, nullable=nullable)
                )
            
        elif size and default is not None:
            return self.query.columns(
                    Column(name, column_type=column_type, size=size, nullable=nullable, default=default)
                )
        
        elif size and default is None:
            return self.query.columns(
                    Column(name, column_type=column_type, size=size, nullable=nullable)
                )
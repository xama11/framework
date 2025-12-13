# NOTE DEV:
# https://github.com/silvaleal/dpy2-framework/wiki/4.-models-database

from provider.builders.SQLQueryBuilder import SQLQueryBuilder
from provider.database import Database
from provider.executors.ExecutorModel import ExecutorsModel

from pypika import Query, Table

class BaseModel(SQLQueryBuilder, ExecutorsModel):
    def __init__(self, table):
        self.conn = Database().connect()
        self.cursor = self.conn.cursor()
        self.table = Table(table)
        self.command = Query()
        
        super().__init__(self.conn, self.cursor, self.command, self.table)
        
    def find(self, id):
        return self.filter(id=id).first()

    def get(self, params='*'):
        self._select_(params)
        
        return self

    def add(self, **kwargs):
        return self._insert_(**kwargs)._commit_()
    
    def delete(self, **kwargs):
        return self._remove_()._where_(**kwargs)._commit_()
    
    def filter(self, **kwargs):
        self._select_()._where_(**kwargs)
        
        return self
    
    def edit(self, where=None, **kwargs):
        self._update_(**kwargs)

        if where:
            self._where_(**where)

        return self._commit_()
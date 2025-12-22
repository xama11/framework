from pypika import Field, Table, JoinType, Order

class SQLQueryBuilder:
    def __init__(self, conn, cursor, comment, table):
        self.comment = comment
        self.table = table
    
    def _insert_(self, **kwargs):
        tables= []
        values = []

        for arg in kwargs:
            tables.append(arg)
            values.append(str(kwargs.get(arg)))

        self.command = self.command.from_(self.table).into(self.table).columns(tables).insert(values)
        return self
    
    def _select_(self, param='*'):
        self.command = self.command.from_(self.table).select(param)
        return self

    def _update_(self, **kwargs):
        for arg in kwargs:
            self.command = self.command.update(self.table).set(Field(arg), kwargs.get(arg))
        
        return self
    
    def limit(self, value):
        self.command = self.command.limit(value)
        return self
    
    def orderBy(self, table, order='desc'):
        order = Order.desc if order == 'desc' else Order.asc
        
        self.command = self.command.orderby(table, order=Order.desc)
        return self
 
    def _remove_(self):
        self.command = self.command.from_(self.table).delete()
        return self

    def _where_(self, *args, **kwargs):
        for expr in args:
            self.command = self.command.where(expr)

        for col, val in kwargs.items():
            self.command = self.command.where(getattr(self.table, col) == val)

        return self
    
    def _query_(self, query):
        self.command = query
        return self
    
    def _join_(self, table, condition, conditionValue, type='inner'):
        guilds = Table(table)
        
        self.command = self.command.join(guilds, getattr(JoinType, type)).on(getattr(self.table, condition) == getattr(guilds, conditionValue))
        
        return self
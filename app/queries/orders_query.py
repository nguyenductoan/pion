from queries.base_query import *

class OrdersQuery(BaseQuery):

    def all(self, limit=1000):
        return super(OrdersQuery, self).all(Order, limit)

    def find(self, id):
        return super(OrdersQuery, self).find(Order, id)


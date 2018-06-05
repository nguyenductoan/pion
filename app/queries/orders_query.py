from queries.base_query import *
import pdb


class OrdersQuery(BaseQuery):

    def all(self, limit=1000):
        return super(OrdersQuery, self).all(Order, limit)

    def find(self, id):
        return super(OrdersQuery, self).find(Order, id)

    def filter_by_user_id(self, user_id):
        return super(OrdersQuery, self).filter_by_user_id(Order, user_id)


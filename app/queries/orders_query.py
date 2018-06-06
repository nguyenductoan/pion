from queries.base_query import *

class OrdersQuery(BaseQuery):

    def __init__(self, model=Order):
        self.model = model


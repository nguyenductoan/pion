from queries.base_query import *

class UsersQuery(BaseQuery):

    def __init__(self, model=User):
        self.model = model


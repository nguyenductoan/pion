from queries.base_query import *

class UsersQuery(BaseQuery):

    def all(self, limit=1000):
        return super(UsersQuery, self).all(User, limit)

    def find(self, id):
        return super(UsersQuery, self).find(User, id)


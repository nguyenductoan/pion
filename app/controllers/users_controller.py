from .base_controller import *
from views.users import *

class UsersController(BaseController):

    def index(self):
        users_query = UsersQuery()
        users = users_query.all()

        context = {}
        context['users'] = users
        view_object = IndexView('users/index', context)

        status = 200
        return (view_object, status)


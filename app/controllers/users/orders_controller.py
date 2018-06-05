from ..base_controller import *
from views.users.orders import *

class OrdersController(BaseController):

    def index(self, params):
        user_id = params['users_id']
        orders_query = OrdersQuery()
        orders = orders_query.filter_by_user_id(user_id)

        context = {}
        context['orders'] = orders
        view_object = IndexView('users/orders/index', context)

        status = 200
        return (view_object, status)


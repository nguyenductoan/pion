from ..base_controller import *
from views.users.orders import *

class OrdersController(BaseController):

    def index(self, params):
        conditions = {'user_id': params['users_id']}
        orders_query = OrdersQuery()
        orders = orders_query.filter_by(conditions)

        context = {}
        context['orders'] = orders
        view_object = IndexView('users/orders/index', context)

        status = 200
        return (view_object, status)


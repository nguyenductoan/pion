from .base_controller import *
from views.orders import *

class OrdersController(BaseController):

    def index(self):
        orders_query = OrdersQuery()
        orders = orders_query.all()

        context = {}
        context['orders'] = orders
        view_object = IndexView('orders/index', context)

        status = 200
        return (view_object, status)


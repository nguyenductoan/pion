from controllers import *

def map_route(method, path, params):
    if method == 'GET':
        if path == '/orders':
            controller = OrdersController(params)
        elif path == '/users':
            controller = UsersController(params)
        else:
            controller = ApplicationController(params)
    elif method == 'POST':
        controller = ApplicationController(params)
    else:
        controller = ApplicationController(params)
    action = 'index'
    status = '200 OK'
    return (controller, action)


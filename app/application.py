import MySQLdb as sql
import pdb
from dao import *
from model import *
from queries import *
from controllers import *
from config import *
import json

def build_params(url_params, request_body):
    request_body = json.loads(request_body)
    params = url_params.split('&')
    for param in params:
        try:
            h = param.split('=')
            request_body[h[0]] = h[1]
        except ValueError as e:
            continue
    return request_body

def app(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    request_body = environ['REQUEST_BODY']
    host, url_params = path.split('?')
    request_params = build_params(url_params, environ['REQUEST_BODY'])

    controller, action = map_route(method, host, request_params)
    view_object, status = getattr(controller, action)()
    view = view_object.render()

    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    return view


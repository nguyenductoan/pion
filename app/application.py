import MySQLdb as sql
from pdb import *
from dao import *
from model import *
from queries import *
from controllers import *
from config import *
import json
import sys

def build_body_params(request_body):
    try:
        body_params = json.loads(request_body)
    except ValueError as e:
        body_params = {}
    return body_params

def build_url_params(path):
    url_params = {}
    segments = path.split('?')
    params_string = segments[1] if (len(segments) > 1) else None
    if not params_string: return {}
    params = params_string.split('&')
    for param in params:
        try:
            h = param.split('=')
            url_params[h[0]] = h[1]
        except ValueError as e:
            continue
    return url_params

def app(environ, start_response):
    route_tree = generate_route()

    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    request_body = environ['REQUEST_BODY']
    host = path.split('?')[0]

    # parse params from body of request
    body_params = build_body_params(environ['REQUEST_BODY'])
    # parse params from url of request (after question mark)
    url_params = build_url_params(path)

    controller_object, action_name, id_params = map_route(route_tree, method, host)

    # concatenating params
    params = body_params
    params.update(id_params)
    params.update(url_params)

    view_object, status = getattr(controller_object, action_name)(params)
    view = view_object.render()

    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    return view


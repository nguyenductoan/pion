import pdb
from controllers import *
from .route_node import RouteNode

def generate_route():
    route_families = [
        # (path, collections, members)
        ('orders', {'index': 'GET'}, {'show': 'GET'}),
        ('users',  {'index': 'GET'}, {'show': 'GET'}),
        ('users/:id/orders', {'index': 'GET'}, {'show': 'GET'})
    ]
    root_node = RouteNode('ApplicationController', 'index', 'GET', '')

    for route_family in route_families:
        route_path, collections, members = route_family
        segments = route_path.split('/')
        controller_path = ''
        current_node = root_node
        for segment in segments:
            # path does not include 'id'
            if segment != ':id': controller_path = '{path}/{segment}'.format(path=controller_path, segment=segment)
            node = current_node.find_or_create_child(segment)
            current_node = node

        segments_of_controller_path = controller_path.split('/')
        segments_of_controller_path = list(map(lambda e: e.title(), segments_of_controller_path))
        controller_name = ''.join(segments_of_controller_path)
        controller_name = '{name}Controller'.format(name=controller_name)
        controller_path = '{path}_controller'.format(path=controller_path)

        # add collection actions to tree
        for action, method in collections.items():
            node_name = action
            child_node = RouteNode(controller_name, action, method, node_name, controller_path)
            current_node.add_child(child_node)

        # create a ':id' node if there aren't have any 'member'
        if len(members) > 0:
            id_node = RouteNode(controller_name, None, None, ':id')
            current_node.add_child(id_node)
            current_node = id_node
        # add member actions to tree
        for action, method in members.items():
            node_name = action
            child_node = RouteNode(controller_name, action, method, node_name, controller_path)
            current_node.add_child(child_node)
    root_node.print_family()
    return root_node

def map_route(root, method, path):
    segments = path.split('/')
    segments = segments[1:len(segments)] # remove first slash
    node = find_route(root, method, segments)
    module = __import__('controllers')
    id_params = extract_id_params(node, segments)
    controller_object = getattr(module, node.controller_name)()
    return (controller_object, node.action_name, id_params)

def find_route(root, method, segments):
    if root is None: return None
    if len(segments) == 0:
        if root.method == method:
            return root
        else:
            return None
    else:
        current_segment = segments[0]
        next_node = root.find_child(current_segment)
        # if can not find any next node, current_node will be ':id' node
        if next_node is None: next_node = root.find_child(':id')
        segments = segments[1:len(segments)] # remove first element
        return find_route(next_node, method, segments)

def extract_id_params(leaf_node, segments):
    index = len(segments) - 1 # index of last element
    id_params = {}
    current_node = leaf_node
    while current_node is not None:
        if current_node.node_name == ':id':
            key = '{object_name}_id'.format(object_name=current_node.parent.node_name)
            id_params[key] = segments[index]
        current_node = current_node.parent
        index = index - 1
    return id_params


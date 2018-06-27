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

        # build path for a controller in route tree
        controller_node, controller_name, controller_path = build_path_for_controller(root_node, route_path)

        # add collection actions to tree
        add_collections_action_to_route_tree(controller_node, collections, controller_name, controller_path)

        # add member actions to tree
        add_member_actions_to_route_tree(controller_node, members, controller_name, controller_path)

    root_node.print_family()
    return root_node

# add nodes of a path-of-controller to route tree
# return controller node, controller_name and controller_path
def build_path_for_controller(root_node, string_path):
    controller_node = root_node
    path_segments = string_path.split('/')
    controller_path = ''
    for segment in path_segments:
        # path does not include 'id'
        if segment != ':id': controller_path = '{path}/{segment}'.format(path=controller_path, segment=segment)
        node = controller_node.find_or_create_child(segment)
        controller_node = node

    segments_of_controller_path = list(map(lambda e: e.title(), controller_path.split('/')))
    controller_name = ''.join(segments_of_controller_path)
    controller_name = '{name}Controller'.format(name=controller_name)
    controller_path = '{path}_controller'.format(path=controller_path)
    return (controller_node, controller_name, controller_path)

def add_collections_action_to_route_tree(current_node, collections, controller_name, controller_path):
    for action, method in collections.items():
        node_name = action
        child_node = RouteNode(controller_name, action, method, node_name, controller_path)
        current_node.add_child(child_node)

def add_member_actions_to_route_tree(current_node, members, controller_name, controller_path):
    # create a ':id' node if there is any member action'
    if len(members) > 0:
        id_node = RouteNode(controller_name, None, None, ':id')
        current_node.add_child(id_node)
        current_node = id_node

    for action, method in members.items():
        node_name = action
        child_node = RouteNode(controller_name, action, method, node_name, controller_path)
        current_node.add_child(child_node)

def map_route(root, method, path):
    path_segments = path.split('/')
    path_segments = path_segments[1:len(path_segments)] # remove first slash
    node = find_node(root, method, path_segments)
    module = __import__('controllers')
    id_params = extract_id_params(node, path_segments)
    controller_object = getattr(module, node.controller_name)()
    return (controller_object, node.action_name, id_params)

def find_node(root, method, path_segments):
    if root is None: return None
    if len(path_segments) == 0:
        if root.method == method:
            return root
        else:
            return None
    else:
        current_segment = path_segments[0]
        next_node = root.find_child(current_segment)
        # if can not find any next node, current_node will be ':id' node
        if next_node is None: next_node = root.find_child(':id')
        path_segments = path_segments[1:len(path_segments)] # remove first element
        return find_node(next_node, method, path_segments)

def extract_id_params(leaf_node, path_segments):
    index = len(path_segments) - 1 # index of last element
    id_params = {}
    current_node = leaf_node
    while current_node is not None:
        if current_node.node_name == ':id':
            key = '{object_name}_id'.format(object_name=current_node.parent.node_name)
            id_params[key] = path_segments[index]
        current_node = current_node.parent
        index = index - 1
    return id_params


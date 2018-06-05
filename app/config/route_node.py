import pdb

class RouteNode():

    def __init__(self, controller_name, action_name, method, node_name, controller_path=None):
        self.controller_name = controller_name
        self.action_name = action_name
        self.method = method
        self.node_name = node_name
        self.leaf = True
        self.controller_path = controller_path
        self.parent = None
        self.children = {}

    def add_child(self, child):
        self.leaf = False
        child.set_parent(self)
        self.children[child.node_name] = child

    def set_parent(self, parent):
        self.parent = parent

    def find_or_create_child(self, key):
        if key in self.children:
            return self.children[key]
        else:
            node = RouteNode(None, None, None, key)
            self.add_child(node)
            return node

    def find_child(self, key):
        if key in self.children:
            return self.children[key]
        else:
            return None

    def get_node_name(self):
        return self.node_name

    def print_family(self, path=''):
        if self.leaf:
            url = '{path}/{segment}'.format(path=path, segment=self.action_name)
            route_info = (url, self.controller_name, self.controller_path)
            print('{0:<50} {1:<25} {2:<25}'.format(*route_info))
        else:
            if self.node_name:
                path = '{path}/{node_name}'.format(path=path, node_name=self.node_name)
            for key, child_node in self.children.items():
                child_node.print_family(path)


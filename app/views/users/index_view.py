from ..base_view import *

class IndexView(BaseView):

    def __init__(self, template='users/index', context={}):
        self.template = env.get_template(template + '.html')
        self.context = context


from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
        loader = PackageLoader('application', 'templates'),
        autoescape = select_autoescape(['html', 'xml'])
    )

class HomeView:

    def __init__(self, template='index', context={}):
        self.template = env.get_template(template + '.html')
        self.context = context

    def render(self):
        return self.template.render(self.context)


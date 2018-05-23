from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
        loader = PackageLoader('application', 'templates'),
        autoescape = select_autoescape(['html', 'xml'])
    )

class BaseView:

    def render(self):
        return self.template.render(self.context)


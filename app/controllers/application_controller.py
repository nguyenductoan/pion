from .base_controller import *
from views.home_view import HomeView

class ApplicationController(BaseController):

    def index(self):
        context = {}
        view_object = HomeView('home', context)

        status = 200
        return (view_object, status)


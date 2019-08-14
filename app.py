from . import api

wsgi_app = api.Api()


@wsgi_app.route('/home')
def home(request, response):
    response.text = 'Привет! Это ГЛАВНАЯ страница'


@wsgi_app.route('/about')
def about(request, response):
    response.text = 'Привет! Это страница О НАС!'

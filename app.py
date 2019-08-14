from api import Api

app = Api()


@app.route('/home')
def home(request, response):
    response.text = 'Привет! Это ГЛАВНАЯ страница'


@app.route('/about')
def about(request, response):
    response.text = 'Привет! Это страница О НАС!'

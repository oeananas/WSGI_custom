from api import Api

app = Api()


@app.route('/')
def home(request, response):
    response.text = 'This is a main page'


@app.route('/home')
def home(request, response):
    response.text = 'This is a home page'


@app.route('/about')
def about(request, response):
    response.text = 'This is page with info about us'
